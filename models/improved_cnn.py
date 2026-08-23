"""
AI Based Intelligent RF Spectrum Signal Identification System

File:
    models/improved_cnn.py

Purpose:
    Define the improved 1D residual CNN used for RF modulation
    classification.

Original architecture:
    Input (128, 2)
        ↓
    Conv1D 64
        ↓
    Residual Block 64
        ↓
    MaxPooling
        ↓
    Residual Block 128
        ↓
    MaxPooling
        ↓
    Residual Block 256
        ↓
    MaxPooling
        ↓
    Conv1D 256
        ↓
    Global Average Pooling
        ↓
    Dense 256
        ↓
    Dropout 0.40
        ↓
    Dense 128
        ↓
    Dropout 0.30
        ↓
    Softmax 11 Classes
"""

import tensorflow as tf

from tensorflow.keras.models import Model
from tensorflow.keras.layers import (
    Input,
    Conv1D,
    BatchNormalization,
    Activation,
    Add,
    MaxPooling1D,
    GlobalAveragePooling1D,
    Dense,
    Dropout,
)


def residual_block(
    x,
    filters,
    kernel_size=3
):
    """
    Create a residual CNN block.

    Parameters
    ----------
    x : tensor
        Input tensor.

    filters : int
        Number of convolution filters.

    kernel_size : int
        Convolution kernel size.

    Returns
    -------
    tensor
        Output tensor after residual processing.
    """

    shortcut = x

    # First convolution
    x = Conv1D(
        filters=filters,
        kernel_size=kernel_size,
        padding="same"
    )(x)

    x = BatchNormalization()(x)

    x = Activation("relu")(x)

    # Second convolution
    x = Conv1D(
        filters=filters,
        kernel_size=kernel_size,
        padding="same"
    )(x)

    x = BatchNormalization()(x)

    # Match shortcut dimensions
    if shortcut.shape[-1] != filters:

        shortcut = Conv1D(
            filters=filters,
            kernel_size=1,
            padding="same"
        )(shortcut)

        shortcut = BatchNormalization()(shortcut)

    # Residual connection
    x = Add()(
        [x, shortcut]
    )

    x = Activation("relu")(x)

    return x


def build_improved_cnn(
    input_shape=(128, 2),
    num_classes=11,
    learning_rate=0.001
):
    """
    Build the improved 1D residual CNN.

    Parameters
    ----------
    input_shape : tuple
        CNN input shape.

    num_classes : int
        Number of modulation classes.

    learning_rate : float
        Adam learning rate.

    Returns
    -------
    tensorflow.keras.Model
        Compiled improved CNN model.
    """

    input_layer = Input(
        shape=input_shape,
        name="IQ_Input"
    )

    # ========================================================
    # Initial Feature Extraction
    # ========================================================

    x = Conv1D(
        filters=64,
        kernel_size=7,
        padding="same"
    )(input_layer)

    x = BatchNormalization()(x)

    x = Activation("relu")(x)

    # ========================================================
    # Residual Block 1
    # ========================================================

    x = residual_block(
        x,
        filters=64,
        kernel_size=5
    )

    x = MaxPooling1D(
        pool_size=2
    )(x)

    # ========================================================
    # Residual Block 2
    # ========================================================

    x = residual_block(
        x,
        filters=128,
        kernel_size=5
    )

    x = MaxPooling1D(
        pool_size=2
    )(x)

    # ========================================================
    # Residual Block 3
    # ========================================================

    x = residual_block(
        x,
        filters=256,
        kernel_size=3
    )

    x = MaxPooling1D(
        pool_size=2
    )(x)

    # ========================================================
    # Feature Reduction
    # ========================================================

    x = Conv1D(
        filters=256,
        kernel_size=3,
        padding="same",
        activation="relu"
    )(x)

    x = BatchNormalization()(x)

    # ========================================================
    # Global Feature Pooling
    # ========================================================

    x = GlobalAveragePooling1D()(x)

    # ========================================================
    # Dense Classification Layers
    # ========================================================

    x = Dense(
        256,
        activation="relu"
    )(x)

    x = Dropout(
        0.40
    )(x)

    x = Dense(
        128,
        activation="relu"
    )(x)

    x = Dropout(
        0.30
    )(x)

    # ========================================================
    # Output Layer
    # ========================================================

    output_layer = Dense(
        num_classes,
        activation="softmax",
        name="Modulation_Output"
    )(x)

    # ========================================================
    # Create Model
    # ========================================================

    model = Model(
        inputs=input_layer,
        outputs=output_layer,
        name="Improved_ResNet_1D_Modulation_Classifier"
    )

    # ========================================================
    # Compile Model
    # ========================================================

    model.compile(

        optimizer=tf.keras.optimizers.Adam(
            learning_rate=learning_rate
        ),

        loss="categorical_crossentropy",

        metrics=[
            "accuracy"
        ]
    )

    return model


if __name__ == "__main__":

    print("=" * 70)
    print("IMPROVED CNN MODEL TEST")
    print("=" * 70)

    model = build_improved_cnn(
        input_shape=(128, 2),
        num_classes=11,
        learning_rate=0.001
    )

    print("\nModel created successfully.")

    print("\nModel name:")
    print(model.name)

    print("\nInput shape:")
    print(model.input_shape)

    print("\nOutput shape:")
    print(model.output_shape)

    print("\nModel summary:")
    model.summary()

    print("\n" + "=" * 70)
    print("IMPROVED CNN MODEL TEST COMPLETED")
    print("=" * 70)
