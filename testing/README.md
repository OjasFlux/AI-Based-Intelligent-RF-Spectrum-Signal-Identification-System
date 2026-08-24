# Testing

The `testing/` directory contains the single-signal prediction and inference functionality of the RF modulation classification system.

This module represents the stage where a trained CNN receives an IQ signal and produces a predicted modulation class with a confidence score.

## Directory Structure

```text
testing/
├── __init__.py
├── predict.py
└── README.md
```

## 1. Purpose

The testing pipeline is:

```text
IQ Signal
    ↓
Input Validation
    ↓
Input Reshaping
    ↓
Load Trained CNN
    ↓
Prediction
    ↓
Softmax Probabilities
    ↓
Predicted Modulation
    ↓
Confidence
```

## 2. Current Model

The testing module uses the improved CNN:

```text
best_improved_cnn_classifier.keras
```

The improved CNN expects:

```text
(128, 2)
```

where:

```text
128 → IQ samples
2   → I/Q channels
```

## 3. Input Format

The prediction function accepts a single IQ signal with:

```text
(2, 128)
```

The input is automatically converted to:

```text
(128, 2)
```

for the improved CNN.

The batch dimension is then added:

```text
(128, 2)
     ↓
(1, 128, 2)
```

## 4. Prediction Output

The system produces:

```text
Predicted Modulation
Confidence
Class Probabilities
```

Example:

```text
Predicted Modulation : QPSK
Confidence           : 94.72%
```

The probabilities for all 11 modulation classes are also displayed.

## 5. Supported Modulation Classes

```text
8PSK
AM-DSB
AM-SSB
BPSK
CPFSK
GFSK
PAM4
QAM16
QAM64
QPSK
WBFM
```

## 6. Using a NumPy IQ File

An IQ sample can be supplied using:

```powershell
python testing/predict.py --input path/to/iq_signal.npy
```

The file can contain either:

```text
(2, 128)
```

or:

```text
(128, 2)
```

The testing module automatically converts the data to the required model format.

## 7. Using a Specific Model

A specific Keras model can be supplied:

```powershell
python testing/predict.py --model path/to/model.keras --input path/to/iq_signal.npy
```

## 8. Default Model

If no model is specified, the system searches for:

```text
saved_models/best_improved_cnn_classifier.keras
```

## 9. Software Pipeline Test

If no input file is supplied:

```powershell
python testing/predict.py
```

the script generates a small synthetic IQ signal.

This is only used to verify that:

```text
Model Loading
       ↓
Input Preparation
       ↓
Prediction
       ↓
Result Display
```

works correctly.

The synthetic signal should **not** be considered a valid RadioML benchmark sample or a real-world classification result.

## 10. Output

The output is presented as:

```text
============================================================
RF SIGNAL PREDICTION
============================================================

Predicted Modulation : QPSK
Confidence           : XX.XX%

Class Probabilities:
8PSK     : XX.XX%
AM-DSB   : XX.XX%
AM-SSB   : XX.XX%
BPSK     : XX.XX%
CPFSK    : XX.XX%
GFSK     : XX.XX%
PAM4     : XX.XX%
QAM16    : XX.XX%
QAM64    : XX.XX%
QPSK     : XX.XX%
WBFM     : XX.XX%

============================================================
PREDICTION COMPLETED
============================================================
```

The actual prediction depends on the trained model and input signal.

## 11. Relationship With Training

Training produces:

```text
Trained CNN
    ↓
saved_models/
```

Testing then loads that trained model:

```text
saved_models/
    ↓
testing/predict.py
    ↓
Prediction
```

Testing does not retrain the model.

## 12. Relationship With Evaluation

Evaluation measures the model across the complete test dataset:

```text
Test Dataset
    ↓
Evaluation
    ↓
Accuracy / F1 / Confusion Matrix / SNR
```

Testing performs individual inference:

```text
One IQ Signal
    ↓
Prediction
```

Therefore:

```text
evaluation/
    → How well does the model perform overall?

testing/
    → What does the model predict for this signal?
```

## 13. Future Live SDR Integration

The testing module is designed as the inference stage that can later receive IQ data from SDR hardware.

The intended future pipeline is:

```text
RTL-SDR / SDR Hardware
        ↓
IQ Samples
        ↓
Signal Preprocessing
        ↓
128-Sample Window
        ↓
Improved CNN
        ↓
Modulation Prediction
        ↓
Confidence
        ↓
User Interface
```

The current `predict.py` does not directly control SDR hardware. It currently accepts stored IQ data and provides a software inference pipeline.

## 14. Important Limitation

A prediction confidence value is the model's softmax output.

For example:

```text
Confidence = 95%
```

does not automatically mean that the prediction is physically 95% certain.

Confidence should be interpreted together with:

```text
SNR
Signal quality
Model performance
Training data
Class distribution
```

## 15. Final Application Flow

The testing module will eventually form the core inference component of the final demonstration:

```text
RF Signal
    ↓
IQ Acquisition
    ↓
Preprocessing
    ↓
CNN
    ↓
Modulation Classification
    ↓
Confidence
    ↓
Visualization
```

## 16. Summary

The `testing/` directory provides the inference interface for the trained RF modulation classifier.

Its main responsibility is:

```text
Receive IQ Signal
       ↓
Prepare Signal
       ↓
Load Trained Model
       ↓
Predict Modulation
       ↓
Display Class + Confidence
```

The current implementation supports stored NumPy IQ signals and provides the foundation for future live SDR integration.
