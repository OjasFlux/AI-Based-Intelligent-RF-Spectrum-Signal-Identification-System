"""
AI Based Intelligent RF Spectrum Signal Identification System

File:
    evaluation/evaluate_model.py

Purpose:
    Reusable evaluation pipeline for the baseline and improved CNN
    modulation classifiers.

Supported models:
    baseline
    improved

Evaluation:
    - Overall accuracy
    - Classification report
    - Precision
    - Recall
    - F1-score
    - Confusion matrix
    - Normalized confusion matrix
    - Accuracy vs SNR
    - High-SNR accuracy
    - Low-SNR accuracy
    - Prediction confidence
    - Sample predictions
"""

import os
import argparse

import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    ConfusionMatrixDisplay,
    precision_recall_fscore_support
)


# ============================================================
# MODEL CONFIGURATION
# ============================================================

MODEL_CONFIG = {

    "baseline": {
        "model_filename":
            "best_cnn_modulation_classifier.keras",

        "name":
            "Baseline CNN",

        "input_type":
            "baseline"
    },

    "improved": {
        "model_filename":
            "best_improved_cnn_classifier.keras",

        "name":
            "Improved CNN",

        "input_type":
            "improved"
    }
}


# ============================================================
# DATA LOADING
# ============================================================

def load_test_data(processed_data_dir):
    """
    Load processed test data.

    Returns
    -------
    tuple
        X_test
        y_test
        snr_test
        modulation_classes
    """

    X_test = np.load(
        os.path.join(
            processed_data_dir,
            "X_test.npy"
        )
    )

    y_test = np.load(
        os.path.join(
            processed_data_dir,
            "y_test.npy"
        )
    )

    snr_test = np.load(
        os.path.join(
            processed_data_dir,
            "snr_test.npy"
        )
    )

    modulation_classes = np.load(
        os.path.join(
            processed_data_dir,
            "modulation_classes.npy"
        )
    )

    return (
        X_test,
        y_test,
        snr_test,
        modulation_classes
    )


# ============================================================
# INPUT PREPARATION
# ============================================================

def prepare_model_input(
    X_test,
    model_type
):
    """
    Prepare IQ data according to the selected model.

    Baseline CNN:
        (samples, 2, 128)
        →
        (samples, 2, 128, 1)

    Improved CNN:
        (samples, 2, 128)
        →
        (samples, 128, 2)
    """

    if model_type == "baseline":

        return X_test[..., np.newaxis]

    if model_type == "improved":

        return np.transpose(
            X_test,
            (0, 2, 1)
        )

    raise ValueError(
        f"Unknown model type: {model_type}"
    )


# ============================================================
# MODEL LOADING
# ============================================================

def load_trained_model(model_path):
    """
    Load a trained Keras model.
    """

    if not os.path.exists(model_path):

        raise FileNotFoundError(
            f"Trained model not found:\n"
            f"{os.path.abspath(model_path)}"
        )

    print("\nModel found:")
    print(
        os.path.abspath(model_path)
    )

    print("\nLoading trained model...")

    model = tf.keras.models.load_model(
        model_path
    )

    print(
        "Trained model loaded successfully."
    )

    return model


# ============================================================
# PREDICTION
# ============================================================

def generate_predictions(
    model,
    X_test,
    batch_size=256
):
    """
    Generate class predictions and confidence values.
    """

    print(
        "\nGenerating predictions..."
    )

    prediction_probabilities = (
        model.predict(
            X_test,
            batch_size=batch_size,
            verbose=1
        )
    )

    y_pred = np.argmax(
        prediction_probabilities,
        axis=1
    )

    prediction_confidence = np.max(
        prediction_probabilities,
        axis=1
    )

    return (
        prediction_probabilities,
        y_pred,
        prediction_confidence
    )


# ============================================================
# CLASSIFICATION REPORT
# ============================================================

def calculate_classification_metrics(
    y_test,
    y_pred,
    modulation_classes
):
    """
    Calculate classification report and
    precision, recall, F1-score.
    """

    report = classification_report(
        y_test,
        y_pred,
        target_names=modulation_classes,
        digits=4,
        zero_division=0
    )

    (
        precision,
        recall,
        f1_score,
        support
    ) = precision_recall_fscore_support(
        y_test,
        y_pred,
        labels=np.arange(
            len(modulation_classes)
        ),
        zero_division=0
    )

    return (
        report,
        precision,
        recall,
        f1_score,
        support
    )


# ============================================================
# CONFUSION MATRIX
# ============================================================

def generate_confusion_matrices(
    y_test,
    y_pred,
    modulation_classes,
    results_dir,
    prefix
):
    """
    Generate and save normal and normalized
    confusion matrices.
    """

    cm = confusion_matrix(
        y_test,
        y_pred
    )

    # --------------------------------------------------------
    # Normal Confusion Matrix
    # --------------------------------------------------------

    fig, ax = plt.subplots(
        figsize=(12, 10)
    )

    display = ConfusionMatrixDisplay(
        confusion_matrix=cm,
        display_labels=modulation_classes
    )

    display.plot(
        ax=ax,
        xticks_rotation=45,
        colorbar=True
    )

    plt.title(
        f"{prefix.title()} CNN - "
        "Confusion Matrix"
    )

    plt.tight_layout()

    confusion_path = os.path.join(
        results_dir,
        f"{prefix}_confusion_matrix.png"
    )

    plt.savefig(
        confusion_path,
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()

    # --------------------------------------------------------
    # Normalized Confusion Matrix
    # --------------------------------------------------------

    cm_normalized = confusion_matrix(
        y_test,
        y_pred,
        normalize="true"
    )

    fig, ax = plt.subplots(
        figsize=(12, 10)
    )

    display_normalized = (
        ConfusionMatrixDisplay(
            confusion_matrix=cm_normalized,
            display_labels=modulation_classes
        )
    )

    display_normalized.plot(
        ax=ax,
        xticks_rotation=45,
        colorbar=True,
        values_format=".2f"
    )

    plt.title(
        f"{prefix.title()} CNN - "
        "Normalized Confusion Matrix"
    )

    plt.tight_layout()

    normalized_path = os.path.join(
        results_dir,
        f"{prefix}_normalized_confusion_matrix.png"
    )

    plt.savefig(
        normalized_path,
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()

    return (
        cm,
        cm_normalized
    )


# ============================================================
# ACCURACY VS SNR
# ============================================================

def calculate_snr_accuracy(
    y_test,
    y_pred,
    snr_test
):
    """
    Calculate classification accuracy
    separately for each SNR level.
    """

    unique_snr_values = sorted(
        np.unique(snr_test)
    )

    snr_accuracy = []

    for snr in unique_snr_values:

        indices = np.where(
            snr_test == snr
        )[0]

        accuracy = accuracy_score(
            y_test[indices],
            y_pred[indices]
        )

        snr_accuracy.append(
            accuracy
        )

    return (
        unique_snr_values,
        snr_accuracy
    )


# ============================================================
# SNR PLOT
# ============================================================

def generate_snr_plot(
    unique_snr_values,
    snr_accuracy,
    results_dir,
    prefix
):
    """
    Generate accuracy versus SNR graph.
    """

    plt.figure(
        figsize=(10, 6)
    )

    plt.plot(
        unique_snr_values,
        np.array(snr_accuracy) * 100,
        marker="o"
    )

    plt.title(
        f"{prefix.title()} CNN "
        "Classification Accuracy vs SNR"
    )

    plt.xlabel(
        "SNR (dB)"
    )

    plt.ylabel(
        "Accuracy (%)"
    )

    plt.grid(True)

    plt.tight_layout()

    path = os.path.join(
        results_dir,
        f"{prefix}_accuracy_vs_snr.png"
    )

    plt.savefig(
        path,
        dpi=300
    )

    plt.close()

    return path


# ============================================================
# SAVE SNR RESULTS
# ============================================================

def save_snr_results(
    unique_snr_values,
    snr_accuracy,
    overall_accuracy,
    high_snr_accuracy,
    low_snr_accuracy,
    results_dir,
    prefix
):
    """
    Save SNR performance results to text.
    """

    path = os.path.join(
        results_dir,
        f"{prefix}_accuracy_vs_snr.txt"
    )

    with open(
        path,
        "w"
    ) as file:

        file.write(
            f"{prefix.title()} CNN "
            "Classification Accuracy vs SNR\n"
        )

        file.write(
            "=" * 60 + "\n\n"
        )

        for snr, accuracy in zip(
            unique_snr_values,
            snr_accuracy
        ):

            file.write(
                f"SNR {snr} dB: "
                f"{accuracy * 100:.2f}%\n"
            )

        file.write("\n")

        file.write(
            f"Overall Accuracy: "
            f"{overall_accuracy * 100:.2f}%\n"
        )

        file.write(
            f"High SNR Accuracy (>= 0 dB): "
            f"{high_snr_accuracy * 100:.2f}%\n"
        )

        file.write(
            f"Low SNR Accuracy (< 0 dB): "
            f"{low_snr_accuracy * 100:.2f}%\n"
        )

    return path


# ============================================================
# EVALUATION SUMMARY
# ============================================================

def save_evaluation_summary(
    model_name,
    overall_accuracy,
    test_loss,
    high_snr_accuracy,
    low_snr_accuracy,
    prediction_confidence,
    correct_indices,
    incorrect_indices,
    best_snr,
    worst_snr,
    results_dir,
    prefix
):
    """
    Save final evaluation summary.
    """

    path = os.path.join(
        results_dir,
        f"{prefix}_evaluation_summary.txt"
    )

    with open(
        path,
        "w"
    ) as file:

        file.write(
            "AI Based Intelligent RF Spectrum "
            "Signal Identification System\n"
        )

        file.write(
            f"{model_name} Evaluation Summary\n"
        )

        file.write(
            "=" * 60 + "\n\n"
        )

        file.write(
            f"Overall Test Accuracy: "
            f"{overall_accuracy * 100:.2f}%\n"
        )

        if test_loss is not None:

            file.write(
                f"Test Loss: "
                f"{test_loss:.4f}\n"
            )

        file.write(
            f"High SNR Accuracy (>= 0 dB): "
            f"{high_snr_accuracy * 100:.2f}%\n"
        )

        file.write(
            f"Low SNR Accuracy (< 0 dB): "
            f"{low_snr_accuracy * 100:.2f}%\n"
        )

        file.write(
            f"Average Confidence: "
            f"{np.mean(prediction_confidence) * 100:.2f}%\n"
        )

        file.write(
            f"Correct Predictions: "
            f"{len(correct_indices)}\n"
        )

        file.write(
            f"Incorrect Predictions: "
            f"{len(incorrect_indices)}\n"
        )

        file.write(
            f"Best SNR: {best_snr} dB\n"
        )

        file.write(
            f"Worst SNR: {worst_snr} dB\n"
        )

    return path


# ============================================================
# MAIN EVALUATION
# ============================================================

def evaluate_model(
    model_type,
    project_root,
    batch_size=256
):
    """
    Run the complete evaluation pipeline.

    Parameters
    ----------
    model_type : str
        Either "baseline" or "improved".

    project_root : str
        Root directory of the project.

    batch_size : int
        Prediction batch size.

    Returns
    -------
    dict
        Evaluation results.
    """

    if model_type not in MODEL_CONFIG:

        raise ValueError(
            "model_type must be "
            "'baseline' or 'improved'"
        )

    config = MODEL_CONFIG[
        model_type
    ]

    model_name = config["name"]

    # --------------------------------------------------------
    # Paths
    # --------------------------------------------------------

    processed_data_dir = os.path.join(
        project_root,
        "data",
        "processed"
    )

    saved_models_dir = os.path.join(
        project_root,
        "saved_models"
    )

    results_dir = os.path.join(
        project_root,
        "evaluation",
        "results"
    )

    os.makedirs(
        results_dir,
        exist_ok=True
    )

    model_path = os.path.join(
        saved_models_dir,
        config["model_filename"]
    )

    prefix = model_type

    print("=" * 70)
    print(
        f"{model_name.upper()} EVALUATION"
    )
    print("=" * 70)

    # --------------------------------------------------------
    # Load test data
    # --------------------------------------------------------

    print("\nLoading test data...")

    (
        X_test,
        y_test,
        snr_test,
        modulation_classes
    ) = load_test_data(
        processed_data_dir
    )

    print(
        "Test data loaded successfully."
    )

    print(
        "\nX_test shape:",
        X_test.shape
    )

    print(
        "y_test shape:",
        y_test.shape
    )

    print(
        "SNR shape:",
        snr_test.shape
    )

    print(
        "Number of classes:",
        len(modulation_classes)
    )

    # --------------------------------------------------------
    # Prepare model input
    # --------------------------------------------------------

    X_test_cnn = prepare_model_input(
        X_test,
        model_type
    )

    print(
        "\nModel input shape:",
        X_test_cnn.shape
    )

    # --------------------------------------------------------
    # Load model
    # --------------------------------------------------------

    model = load_trained_model(
        model_path
    )

    # --------------------------------------------------------
    # Direct model evaluation
    # --------------------------------------------------------

    test_loss = None

    if model_type == "improved":

        test_loss, test_accuracy = (
            model.evaluate(
                X_test_cnn,
                tf.keras.utils.to_categorical(
                    y_test,
                    num_classes=len(
                        modulation_classes
                    )
                ),
                batch_size=batch_size,
                verbose=1
            )
        )

        print(
            f"\nTest Loss: {test_loss:.4f}"
        )

        print(
            f"Test Accuracy: "
            f"{test_accuracy * 100:.2f}%"
        )

    # --------------------------------------------------------
    # Predictions
    # --------------------------------------------------------

    (
        prediction_probabilities,
        y_pred,
        prediction_confidence
    ) = generate_predictions(
        model,
        X_test_cnn,
        batch_size=batch_size
    )

    # --------------------------------------------------------
    # Overall accuracy
    # --------------------------------------------------------

    overall_accuracy = accuracy_score(
        y_test,
        y_pred
    )

    correct_indices = np.where(
        y_test == y_pred
    )[0]

    incorrect_indices = np.where(
        y_test != y_pred
    )[0]

    print("\n" + "=" * 70)
    print("OVERALL PERFORMANCE")
    print("=" * 70)

    print(
        f"Accuracy: "
        f"{overall_accuracy * 100:.2f}%"
    )

    print(
        "Correct Predictions:",
        len(correct_indices)
    )

    print(
        "Incorrect Predictions:",
        len(incorrect_indices)
    )

    print(
        f"Average Confidence: "
        f"{np.mean(prediction_confidence) * 100:.2f}%"
    )

    # --------------------------------------------------------
    # Classification report
    # --------------------------------------------------------

    (
        report,
        precision,
        recall,
        f1_score,
        support
    ) = calculate_classification_metrics(
        y_test,
        y_pred,
        modulation_classes
    )

    print("\n" + "=" * 70)
    print("CLASSIFICATION REPORT")
    print("=" * 70)

    print(report)

    report_path = os.path.join(
        results_dir,
        f"{prefix}_classification_report.txt"
    )

    with open(
        report_path,
        "w"
    ) as file:

        file.write(report)

    # --------------------------------------------------------
    # Confusion matrices
    # --------------------------------------------------------

    (
        cm,
        cm_normalized
    ) = generate_confusion_matrices(
        y_test,
        y_pred,
        modulation_classes,
        results_dir,
        prefix
    )

    # --------------------------------------------------------
    # Accuracy vs SNR
    # --------------------------------------------------------

    (
        unique_snr_values,
        snr_accuracy
    ) = calculate_snr_accuracy(
        y_test,
        y_pred,
        snr_test
    )

    print("\n" + "=" * 70)
    print("ACCURACY VS SNR")
    print("=" * 70)

    for snr, accuracy in zip(
        unique_snr_values,
        snr_accuracy
    ):

        print(
            f"SNR {snr:>3} dB : "
            f"{accuracy * 100:.2f}%"
        )

    generate_snr_plot(
        unique_snr_values,
        snr_accuracy,
        results_dir,
        prefix
    )

    # --------------------------------------------------------
    # High / Low SNR
    # --------------------------------------------------------

    high_snr_threshold = 0

    high_indices = np.where(
        snr_test >= high_snr_threshold
    )[0]

    low_indices = np.where(
        snr_test < high_snr_threshold
    )[0]

    high_snr_accuracy = accuracy_score(
        y_test[high_indices],
        y_pred[high_indices]
    )

    low_snr_accuracy = accuracy_score(
        y_test[low_indices],
        y_pred[low_indices]
    )

    print("\n" + "=" * 70)
    print("SNR PERFORMANCE")
    print("=" * 70)

    print(
        f"High SNR (>= 0 dB): "
        f"{high_snr_accuracy * 100:.2f}%"
    )

    print(
        f"Low SNR (< 0 dB): "
        f"{low_snr_accuracy * 100:.2f}%"
    )

    # --------------------------------------------------------
    # Best / worst SNR
    # --------------------------------------------------------

    best_index = np.argmax(
        snr_accuracy
    )

    worst_index = np.argmin(
        snr_accuracy
    )

    best_snr = unique_snr_values[
        best_index
    ]

    worst_snr = unique_snr_values[
        worst_index
    ]

    # --------------------------------------------------------
    # Confidence
    # --------------------------------------------------------

    correct_confidence = 0

    incorrect_confidence = 0

    if len(correct_indices) > 0:

        correct_confidence = np.mean(
            prediction_confidence[
                correct_indices
            ]
        )

    if len(incorrect_indices) > 0:

        incorrect_confidence = np.mean(
            prediction_confidence[
                incorrect_indices
            ]
        )

    print("\n" + "=" * 70)
    print("CONFIDENCE ANALYSIS")
    print("=" * 70)

    print(
        f"Overall Confidence: "
        f"{np.mean(prediction_confidence) * 100:.2f}%"
    )

    print(
        f"Correct Prediction Confidence: "
        f"{correct_confidence * 100:.2f}%"
    )

    print(
        f"Incorrect Prediction Confidence: "
        f"{incorrect_confidence * 100:.2f}%"
    )

    # --------------------------------------------------------
    # Save SNR results
    # --------------------------------------------------------

    save_snr_results(
        unique_snr_values,
        snr_accuracy,
        overall_accuracy,
        high_snr_accuracy,
        low_snr_accuracy,
        results_dir,
        prefix
    )

    # --------------------------------------------------------
    # Save summary
    # --------------------------------------------------------

    save_evaluation_summary(
        model_name,
        overall_accuracy,
        test_loss,
        high_snr_accuracy,
        low_snr_accuracy,
        prediction_confidence,
        correct_indices,
        incorrect_indices,
        best_snr,
        worst_snr,
        results_dir,
        prefix
    )

    # --------------------------------------------------------
    # Final output
    # --------------------------------------------------------

    print("\n" + "=" * 70)
    print(
        f"{model_name.upper()} "
        "EVALUATION COMPLETED"
    )
    print("=" * 70)

    print(
        f"\nOverall Accuracy: "
        f"{overall_accuracy * 100:.2f}%"
    )

    print(
        f"High SNR Accuracy: "
        f"{high_snr_accuracy * 100:.2f}%"
    )

    print(
        f"Low SNR Accuracy: "
        f"{low_snr_accuracy * 100:.2f}%"
    )

    print(
        f"Best SNR: "
        f"{best_snr} dB"
    )

    print(
        f"Worst SNR: "
        f"{worst_snr} dB"
    )

    return {
        "model": model_name,
        "accuracy": overall_accuracy,
        "test_loss": test_loss,
        "high_snr_accuracy":
            high_snr_accuracy,
        "low_snr_accuracy":
            low_snr_accuracy,
        "average_confidence":
            np.mean(
                prediction_confidence
            ),
        "best_snr":
            best_snr,
        "worst_snr":
            worst_snr,
        "y_test":
            y_test,
        "y_pred":
            y_pred,
        "confidence":
            prediction_confidence,
        "snr_values":
            unique_snr_values,
        "snr_accuracy":
            snr_accuracy
    }


# ============================================================
# COMMAND-LINE INTERFACE
# ============================================================

def main():

    parser = argparse.ArgumentParser(
        description=(
            "Evaluate the RF modulation "
            "classification CNN."
        )
    )

    parser.add_argument(
        "--model",
        choices=[
            "baseline",
            "improved"
        ],
        default="improved",
        help=(
            "Model to evaluate. "
            "Default: improved"
        )
    )

    parser.add_argument(
        "--batch-size",
        type=int,
        default=256,
        help=(
            "Prediction batch size. "
            "Default: 256"
        )
    )

    args = parser.parse_args()

    project_root = os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )

    evaluate_model(
        model_type=args.model,
        project_root=project_root,
        batch_size=args.batch_size
    )


if __name__ == "__main__":
    main()
