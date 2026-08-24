"""
AI Based Intelligent RF Spectrum Signal Identification System

File:
    testing/predict.py

Purpose:
    Perform single-signal RF modulation prediction using the
    trained improved CNN.

Input:
    IQ signal with shape (2, 128)

Model input:
    (128, 2)

Output:
    Predicted modulation class
    Prediction confidence
    Class probabilities
"""

import os
import argparse

import numpy as np
import tensorflow as tf


# ============================================================
# CONFIGURATION
# ============================================================

NUM_CLASSES = 11

DEFAULT_MODEL = (
    "best_improved_cnn_classifier.keras"
)


# ============================================================
# MODULATION CLASSES
# ============================================================

DEFAULT_CLASSES = [
    "8PSK",
    "AM-DSB",
    "AM-SSB",
    "BPSK",
    "CPFSK",
    "GFSK",
    "PAM4",
    "QAM16",
    "QAM64",
    "QPSK",
    "WBFM"
]


# ============================================================
# LOAD MODEL
# ============================================================

def load_model(model_path):
    """
    Load the trained improved CNN.
    """

    if not os.path.exists(model_path):

        raise FileNotFoundError(
            f"Model not found:\n"
            f"{os.path.abspath(model_path)}"
        )

    print(
        "\nLoading trained model..."
    )

    model = tf.keras.models.load_model(
        model_path
    )

    print(
        "Model loaded successfully."
    )

    return model


# ============================================================
# LOAD MODULATION CLASSES
# ============================================================

def load_modulation_classes(
    classes_path=None
):
    """
    Load modulation class names.

    If modulation_classes.npy is unavailable,
    use the project-defined class ordering.
    """

    if classes_path is not None:

        if os.path.exists(
            classes_path
        ):

            classes = np.load(
                classes_path,
                allow_pickle=True
            )

            return [
                str(item)
                for item in classes
            ]

    return DEFAULT_CLASSES


# ============================================================
# PREPARE IQ INPUT
# ============================================================

def prepare_iq_signal(
    iq_signal
):
    """
    Prepare an IQ signal for the improved CNN.

    Expected input:
        (2, 128)

    Model input:
        (128, 2)
    """

    iq_signal = np.asarray(
        iq_signal,
        dtype=np.float32
    )

    if iq_signal.shape != (
        2,
        128
    ):

        raise ValueError(
            "Expected IQ signal shape "
            "(2, 128), got "
            f"{iq_signal.shape}"
        )

    # Convert:
    #
    # (2, 128)
    #
    # to:
    #
    # (128, 2)

    prepared_signal = np.transpose(
        iq_signal
    )

    # Add batch dimension
    #
    # (128, 2)
    #
    # →
    #
    # (1, 128, 2)

    prepared_signal = np.expand_dims(
        prepared_signal,
        axis=0
    )

    return prepared_signal


# ============================================================
# PREDICT SIGNAL
# ============================================================

def predict_signal(
    model,
    iq_signal,
    modulation_classes
):
    """
    Predict the modulation type of one IQ signal.

    Returns
    -------
    dict
        Prediction information.
    """

    model_input = prepare_iq_signal(
        iq_signal
    )

    probabilities = model.predict(
        model_input,
        verbose=0
    )[0]

    predicted_index = int(
        np.argmax(probabilities)
    )

    predicted_class = (
        modulation_classes[
            predicted_index
        ]
    )

    confidence = float(
        probabilities[
            predicted_index
        ]
    )

    return {
        "predicted_class":
            predicted_class,

        "predicted_index":
            predicted_index,

        "confidence":
            confidence,

        "probabilities":
            probabilities
    }


# ============================================================
# DISPLAY PREDICTION
# ============================================================

def display_prediction(
    result,
    modulation_classes
):
    """
    Display prediction results.
    """

    print("\n" + "=" * 60)
    print("RF SIGNAL PREDICTION")
    print("=" * 60)

    print(
        "\nPredicted Modulation : "
        f"{result['predicted_class']}"
    )

    print(
        "Confidence           : "
        f"{result['confidence'] * 100:.2f}%"
    )

    print("\nClass Probabilities:")

    probabilities = (
        result["probabilities"]
    )

    sorted_indices = np.argsort(
        probabilities
    )[::-1]

    for index in sorted_indices:

        print(
            f"{modulation_classes[index]:8s} : "
            f"{probabilities[index] * 100:6.2f}%"
        )

    print("\n" + "=" * 60)
    print(
        "PREDICTION COMPLETED"
    )
    print("=" * 60)


# ============================================================
# LOAD SAMPLE FROM NUMPY FILE
# ============================================================

def load_iq_from_npy(
    file_path
):
    """
    Load one IQ signal from a NumPy file.

    Supported shapes:

        (2, 128)
        (128, 2)

    """

    if not os.path.exists(
        file_path
    ):

        raise FileNotFoundError(
            f"IQ file not found:\n"
            f"{os.path.abspath(file_path)}"
        )

    iq_signal = np.load(
        file_path
    )

    # Convert (128, 2)
    # to (2, 128)

    if iq_signal.shape == (
        128,
        2
    ):

        iq_signal = np.transpose(
            iq_signal
        )

    if iq_signal.shape != (
        2,
        128
    ):

        raise ValueError(
            "Expected IQ file shape "
            "(2,128) or (128,2), "
            f"got {iq_signal.shape}"
        )

    return iq_signal


# ============================================================
# DEMO SIGNAL
# ============================================================

def create_demo_iq_signal():
    """
    Create a simple IQ signal for testing
    the prediction pipeline.

    IMPORTANT:
        This is only a software pipeline test.
        It is NOT a real RadioML modulation sample.
    """

    time = np.arange(
        128
    )

    i_signal = np.cos(
        2 * np.pi * 0.1 * time
    )

    q_signal = np.sin(
        2 * np.pi * 0.1 * time
    )

    iq_signal = np.array(
        [
            i_signal,
            q_signal
        ],
        dtype=np.float32
    )

    return iq_signal


# ============================================================
# MAIN
# ============================================================

def main():

    parser = argparse.ArgumentParser(
        description=(
            "Predict RF modulation from "
            "an IQ signal."
        )
    )

    parser.add_argument(
        "--input",
        type=str,
        default=None,
        help=(
            "Path to an IQ .npy file. "
            "Shape must be (2,128) "
            "or (128,2)."
        )
    )

    parser.add_argument(
        "--model",
        type=str,
        default=None,
        help=(
            "Path to trained .keras model."
        )
    )

    args = parser.parse_args()

    # --------------------------------------------------------
    # Project Root
    # --------------------------------------------------------

    project_root = os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )

    # --------------------------------------------------------
    # Default Model
    # --------------------------------------------------------

    if args.model is None:

        model_path = os.path.join(
            project_root,
            "saved_models",
            DEFAULT_MODEL
        )

    else:

        model_path = args.model

    # --------------------------------------------------------
    # Classes
    # --------------------------------------------------------

    classes_path = os.path.join(
        project_root,
        "data",
        "processed",
        "modulation_classes.npy"
    )

    modulation_classes = (
        load_modulation_classes(
            classes_path
        )
    )

    # --------------------------------------------------------
    # Load Model
    # --------------------------------------------------------

    model = load_model(
        model_path
    )

    # --------------------------------------------------------
    # Input Signal
    # --------------------------------------------------------

    if args.input is not None:

        iq_signal = load_iq_from_npy(
            args.input
        )

        print(
            "\nInput IQ signal loaded:"
        )

        print(
            "Shape:",
            iq_signal.shape
        )

    else:

        print(
            "\nNo input file provided."
        )

        print(
            "Running software pipeline "
            "test using demo IQ signal."
        )

        iq_signal = (
            create_demo_iq_signal()
        )

    # --------------------------------------------------------
    # Prediction
    # --------------------------------------------------------

    result = predict_signal(
        model,
        iq_signal,
        modulation_classes
    )

    # --------------------------------------------------------
    # Display
    # --------------------------------------------------------

    display_prediction(
        result,
        modulation_classes
    )


if __name__ == "__main__":

    main()
