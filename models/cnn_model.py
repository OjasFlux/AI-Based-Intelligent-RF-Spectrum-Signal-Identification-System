"""
AI Based Intelligent RF Spectrum Signal Identification System

File:
    models/cnn_model.py

Purpose:
    Baseline CNN model for RF modulation classification.

Source:
    04_cnn_model.ipynb

Input:
    (2, 128, 1)

Output:
    11 modulation classes
"""

import tensorflow as tf

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import (
    Conv2D,
    MaxPooling2D,
    BatchNormalization,
    Dropout,
    Flatten,
    Dense,
    Input
)


def build_cnn_model(
    input_shape=(2, 128, 1),
    num_classes=11
):
    """
    Build the baseline CNN model.

    Parameters
    ----------
    input_shape : tuple
        Input shape of the IQ signal.

    num_classes : int
        Number of modulation classes.

    Returns
    -------
    tensorflow.keras.Model
        Compiled baseline CNN model.
    """

    model = Sequential([

        # Input Layer
        Input(
            shape=input_shape
        ),

        # ====================================================
        # Convolution Block 1
        # ====================================================

        Conv2D(
            filters=32,
            kernel_size=(1, 5),
            activation="relu",
            padding="same"
        ),

        BatchNormalization(),

        MaxPooling2D(
            pool_size=(1, 2)
        ),

        Dropout(
            0.20
        ),

        # ====================================================
        # Convolution Block 2
        # ====================================================

        Conv2D(
            filters=64,
            kernel_size=(1, 3),
            activation="relu",
            padding="same"
        ),

        BatchNormalization(),

        MaxPooling2D(
            pool_size=(1, 2)
        ),

        Dropout(
            0.25
        ),

        # ====================================================
        # Convolution Block 3
        # ====================================================

        Conv2D(
            filters=128,
            kernel_size=(1, 3),
            activation="relu",
            padding="same"
        ),

        BatchNormalization(),

        Dropout(
            0.30
        ),

        # ====================================================
        # Classification Layers
        # ====================================================

        Flatten(),

        Dense(
            256,
            activation="relu"
        ),

        Dropout(
            0.50
        ),

        Dense(
            128,
            activation="relu"
        ),

        Dropout(
            0.30
        ),

        # ====================================================
        # Output Layer
        # ====================================================

        Dense(
            num_classes,
            activation="softmax"
        )
    ])

    # ========================================================
    # Compile
    # ========================================================

    model.compile(
        optimizer="adam",
        loss="categorical_crossentropy",
        metrics=["accuracy"]
    )

    return model


if __name__ == "__main__":

    print("=" * 70)
    print("BASELINE CNN MODEL TEST")
    print("=" * 70)

    model = build_cnn_model()

    print("\nCNN model created successfully.")

    print("\nModel name:")
    print(model.name)

    print("\nInput shape:")
    print(model.input_shape)

    print("\nOutput shape:")
    print(model.output_shape)

    print("\nModel architecture:")
    model.summary()

    # --------------------------------------------------------
    # Test with one sample
    # --------------------------------------------------------

    test_sample = tf.random.normal(
        (1, 2, 128, 1)
    )

    prediction = model.predict(
        test_sample,
        verbose=0
    )

    print("\nTest input shape:")
    print(test_sample.shape)

    print("\nPrediction shape:")
    print(prediction.shape)

    print("\nPrediction probability sum:")
    print(prediction.sum())

    print("\n" + "=" * 70)
    print("BASELINE CNN MODEL TEST COMPLETED")
    print("=" * 70)
