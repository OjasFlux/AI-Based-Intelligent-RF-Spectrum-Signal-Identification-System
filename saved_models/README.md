# Saved Models

The `saved_models/` directory contains the trained Keras model files used by the RF modulation classification system.

These files contain the learned weights and configuration of the trained CNN models.

## Directory Structure

```text
saved_models/
├── README.md
├── best_cnn_modulation_classifier.keras
└── best_improved_cnn_classifier.keras
```

## 1. Baseline CNN

```text
File:
best_cnn_modulation_classifier.keras
```

This is the trained baseline CNN model.

It corresponds to:

```text
models/cnn_model.py
```

The baseline model was developed as the reference classification model.

Verified test performance:

```text
Overall Accuracy: 56.43%
```

## 2. Improved CNN

```text
File:
best_improved_cnn_classifier.keras
```

This is the trained improved CNN model.

It corresponds to:

```text
models/improved_cnn.py
```

The improved model uses the enhanced residual CNN architecture.

Verified test performance:

```text
Overall Accuracy: 62.29%
```

High-SNR performance:

```text
SNR >= 0 dB:
92.08%
```

## 3. Model File Format

The models are stored using the Keras format:

```text
.keras
```

This format stores the trained model information required to reload the model for inference and evaluation.

## 4. Relationship With Model Architecture

The architecture definitions are stored separately:

```text
models/
├── cnn_model.py
└── improved_cnn.py
```

The trained versions are stored here:

```text
saved_models/
├── best_cnn_modulation_classifier.keras
└── best_improved_cnn_classifier.keras
```

Therefore:

```text
Architecture
     +
Training
     ↓
Trained Model
     ↓
saved_models/
```

## 5. Model Loading

A trained model can be loaded using TensorFlow/Keras:

```python
import tensorflow as tf

model = tf.keras.models.load_model(
    "saved_models/best_improved_cnn_classifier.keras"
)
```

The baseline model can be loaded using:

```python
model = tf.keras.models.load_model(
    "saved_models/best_cnn_modulation_classifier.keras"
)
```

## 6. Usage

The saved models are used by:

```text
evaluation/
    ↓
Model performance evaluation

testing/
    ↓
Individual signal classification

Application
    ↓
Final RF modulation identification
```

## 7. Important

The `.keras` files are trained model artifacts.

They should not be manually edited.

If the model architecture or training configuration is changed, a new trained model should be generated and evaluated again.

## 8. Model Selection

Based on the completed evaluation:

```text
Baseline CNN
56.43%
      ↓
Improved CNN
62.29%
```

The improved CNN is currently the preferred model for the final software-based RF modulation classification system.

## 9. Reproducibility

The model architecture is maintained separately from the trained model file.

This allows the project to document:

```text
Model Architecture
        ↓
Training Procedure
        ↓
Trained Model
        ↓
Evaluation
        ↓
Final Prediction
```

## 10. Summary

The `saved_models/` directory provides the trained models required by the evaluation, testing, and final application stages.

```text
Baseline CNN
     ↓
best_cnn_modulation_classifier.keras

Improved CNN
     ↓
best_improved_cnn_classifier.keras
```
