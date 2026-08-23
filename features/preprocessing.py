"""
AI Based Intelligent RF Spectrum Signal Identification System

File:
    features/preprocessing.py

Purpose:
    Reusable preprocessing pipeline for the RadioML 2016.10a
    dataset before CNN training.

Pipeline:
    Dataset Loading
        ↓
    IQ Signal Combination
        ↓
    Label Encoding
        ↓
    IQ Normalization
        ↓
    Train / Validation / Test Split
        ↓
    Save Processed Data
"""

import os
import pickle
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder


def load_dataset(dataset_path):
    """
    Load the RadioML 2016.10a dataset.

    Parameters
    ----------
    dataset_path : str
        Path to RML2016.10a_dict.pkl.

    Returns
    -------
    dataset : dict
        Loaded RadioML dataset.
    """

    if not os.path.exists(dataset_path):
        raise FileNotFoundError(
            f"Dataset not found:\n{os.path.abspath(dataset_path)}"
        )

    print("Dataset found:")
    print(os.path.abspath(dataset_path))

    print("\nLoading RadioML 2016.10a dataset...")

    with open(dataset_path, "rb") as file:
        dataset = pickle.load(file, encoding="latin1")

    print("Dataset loaded successfully.")

    return dataset


def extract_dataset_information(dataset):
    """
    Extract modulation classes and SNR values.

    Returns
    -------
    modulation_types : list
        Sorted modulation class names.

    snr_values : list
        Sorted SNR values.
    """

    modulation_types = sorted(
        set(key[0] for key in dataset.keys())
    )

    snr_values = sorted(
        set(key[1] for key in dataset.keys())
    )

    return modulation_types, snr_values


def combine_iq_signals(dataset):
    """
    Combine all IQ signals, modulation labels and SNR values.

    Returns
    -------
    X : np.ndarray
        Combined IQ signals.

    y : np.ndarray
        Modulation labels.

    snr_labels : np.ndarray
        SNR value corresponding to each signal.
    """

    X_list = []
    y_list = []
    snr_list = []

    for (modulation, snr), signals in dataset.items():

        X_list.append(signals)

        number_of_signals = signals.shape[0]

        y_list.extend(
            [modulation] * number_of_signals
        )

        snr_list.extend(
            [snr] * number_of_signals
        )

    X = np.concatenate(
        X_list,
        axis=0
    )

    y = np.array(y_list)

    snr_labels = np.array(snr_list)

    return X, y, snr_labels


def encode_labels(y):
    """
    Encode modulation labels into integer class IDs.

    Returns
    -------
    y_encoded : np.ndarray
        Integer encoded labels.

    label_encoder : LabelEncoder
        Fitted label encoder.
    """

    label_encoder = LabelEncoder()

    y_encoded = label_encoder.fit_transform(y)

    return y_encoded, label_encoder


def normalize_iq_signals(X):
    """
    Normalize each IQ signal using its maximum magnitude.

    The normalization follows the original notebook:

        magnitude = sqrt(I^2 + Q^2)

        X_normalized = X / max_magnitude

    Returns
    -------
    X_normalized : np.ndarray
        Normalized IQ signals.
    """

    magnitude = np.sqrt(
        X[:, 0, :] ** 2 +
        X[:, 1, :] ** 2
    )

    max_magnitude = np.max(
        magnitude,
        axis=1,
        keepdims=True
    )

    # Prevent division by zero
    max_magnitude[
        max_magnitude == 0
    ] = 1.0

    X_normalized = (
        X /
        max_magnitude[:, np.newaxis, :]
    )

    return X_normalized


def split_dataset(
    X_normalized,
    y_encoded,
    snr_labels,
    test_size=0.20,
    validation_size=0.125,
    random_state=42
):
    """
    Split data into training, validation and testing sets.

    The split follows the original notebook:

        First:
            80% train+validation
            20% test

        Second:
            87.5% training
            12.5% validation

    This results in:

        Training   = 70%
        Validation = 10%
        Testing    = 20%

    Returns
    -------
    tuple
        X_train
        X_val
        X_test
        y_train
        y_val
        y_test
        snr_train
        snr_val
        snr_test
    """

    (
        X_train_full,
        X_test,
        y_train_full,
        y_test,
        snr_train_full,
        snr_test
    ) = train_test_split(
        X_normalized,
        y_encoded,
        snr_labels,
        test_size=test_size,
        random_state=random_state,
        stratify=y_encoded
    )

    (
        X_train,
        X_val,
        y_train,
        y_val,
        snr_train,
        snr_val
    ) = train_test_split(
        X_train_full,
        y_train_full,
        snr_train_full,
        test_size=validation_size,
        random_state=random_state,
        stratify=y_train_full
    )

    return (
        X_train,
        X_val,
        X_test,
        y_train,
        y_val,
        y_test,
        snr_train,
        snr_val,
        snr_test
    )


def save_processed_data(
    processed_data_dir,
    X_train,
    X_val,
    X_test,
    y_train,
    y_val,
    y_test,
    snr_train,
    snr_val,
    snr_test,
    modulation_classes
):
    """
    Save processed datasets and metadata as .npy files.
    """

    os.makedirs(
        processed_data_dir,
        exist_ok=True
    )

    np.save(
        os.path.join(
            processed_data_dir,
            "X_train.npy"
        ),
        X_train
    )

    np.save(
        os.path.join(
            processed_data_dir,
            "X_val.npy"
        ),
        X_val
    )

    np.save(
        os.path.join(
            processed_data_dir,
            "X_test.npy"
        ),
        X_test
    )

    np.save(
        os.path.join(
            processed_data_dir,
            "y_train.npy"
        ),
        y_train
    )

    np.save(
        os.path.join(
            processed_data_dir,
            "y_val.npy"
        ),
        y_val
    )

    np.save(
        os.path.join(
            processed_data_dir,
            "y_test.npy"
        ),
        y_test
    )

    np.save(
        os.path.join(
            processed_data_dir,
            "snr_train.npy"
        ),
        snr_train
    )

    np.save(
        os.path.join(
            processed_data_dir,
            "snr_val.npy"
        ),
        snr_val
    )

    np.save(
        os.path.join(
            processed_data_dir,
            "snr_test.npy"
        ),
        snr_test
    )

    np.save(
        os.path.join(
            processed_data_dir,
            "modulation_classes.npy"
        ),
        modulation_classes
    )


def preprocess_dataset(
    dataset_path,
    processed_data_dir
):
    """
    Run the complete preprocessing pipeline.

    Returns
    -------
    dict
        Processed datasets and metadata.
    """

    print("=" * 60)
    print("DATA PREPROCESSING STARTED")
    print("=" * 60)

    # 1. Load dataset
    dataset = load_dataset(dataset_path)

    # 2. Dataset information
    modulation_types, snr_values = (
        extract_dataset_information(dataset)
    )

    print(
        "\nNumber of modulation classes:",
        len(modulation_types)
    )

    print(
        "Modulation classes:",
        modulation_types
    )

    print(
        "\nNumber of SNR levels:",
        len(snr_values)
    )

    print(
        "SNR values:",
        snr_values
    )

    # 3. Combine IQ signals
    print("\nCombining IQ signals...")

    X, y, snr_labels = combine_iq_signals(
        dataset
    )

    print("\nCombined dataset shape:")
    print("X shape:", X.shape)
    print("y shape:", y.shape)
    print("SNR shape:", snr_labels.shape)

    # 4. Encode labels
    y_encoded, label_encoder = encode_labels(y)

    print("\nLabel encoding:")

    for index, modulation in enumerate(
        label_encoder.classes_
    ):
        print(
            f"{index} -> {modulation}"
        )

    # 5. Normalize IQ
    print("\nNormalizing IQ signals...")

    X_normalized = normalize_iq_signals(X)

    print(
        "Normalization completed."
    )

    print(
        "Normalized shape:",
        X_normalized.shape
    )

    # 6. Split dataset
    print(
        "\nCreating training, validation "
        "and testing datasets..."
    )

    (
        X_train,
        X_val,
        X_test,
        y_train,
        y_val,
        y_test,
        snr_train,
        snr_val,
        snr_test
    ) = split_dataset(
        X_normalized,
        y_encoded,
        snr_labels
    )

    # 7. Display final shapes
    print("\nFinal dataset shapes:")

    print(
        "X_train:",
        X_train.shape
    )

    print(
        "X_val:",
        X_val.shape
    )

    print(
        "X_test:",
        X_test.shape
    )

    print(
        "\ny_train:",
        y_train.shape
    )

    print(
        "y_val:",
        y_val.shape
    )

    print(
        "y_test:",
        y_test.shape
    )

    # 8. Save processed data
    print(
        "\nSaving processed data..."
    )

    save_processed_data(
        processed_data_dir,
        X_train,
        X_val,
        X_test,
        y_train,
        y_val,
        y_test,
        snr_train,
        snr_val,
        snr_test,
        label_encoder.classes_
    )

    # 9. Summary
    total_samples = len(
        X_normalized
    )

    print("\n" + "=" * 60)
    print("FINAL DATA SPLIT")
    print("=" * 60)

    print(
        f"Training:   {len(X_train)} "
        f"samples "
        f"({len(X_train) / total_samples * 100:.2f}%)"
    )

    print(
        f"Validation: {len(X_val)} "
        f"samples "
        f"({len(X_val) / total_samples * 100:.2f}%)"
    )

    print(
        f"Testing:    {len(X_test)} "
        f"samples "
        f"({len(X_test) / total_samples * 100:.2f}%)"
    )

    print("\nSaved files:")

    for filename in sorted(
        os.listdir(processed_data_dir)
    ):
        print("-", filename)

    print("\n" + "=" * 60)
    print(
        "DATA PREPROCESSING "
        "COMPLETED SUCCESSFULLY"
    )
    print("=" * 60)

    print(
        f"Total samples: {total_samples}"
    )

    print(
        "Modulation classes:",
        len(label_encoder.classes_)
    )

    print(
        "Input shape for CNN:",
        X_train.shape[1:]
    )

    return {
        "X_train": X_train,
        "X_val": X_val,
        "X_test": X_test,
        "y_train": y_train,
        "y_val": y_val,
        "y_test": y_test,
        "snr_train": snr_train,
        "snr_val": snr_val,
        "snr_test": snr_test,
        "modulation_classes":
            label_encoder.classes_
    }


if __name__ == "__main__":

    PROJECT_ROOT = os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )

    DATASET_PATH = os.path.join(
        PROJECT_ROOT,
        "data",
        "dataset",
        "RML2016.10a_dict.pkl"
    )

    PROCESSED_DATA_DIR = os.path.join(
        PROJECT_ROOT,
        "data",
        "processed"
    )

    preprocess_dataset(
        DATASET_PATH,
        PROCESSED_DATA_DIR
    )
