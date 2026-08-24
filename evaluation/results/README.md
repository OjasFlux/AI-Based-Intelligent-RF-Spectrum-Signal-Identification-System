# Evaluation Results

This directory contains the final evaluation results of the RF modulation classification models.

Two CNN models were evaluated using the same test dataset:

- Baseline CNN
- Improved CNN

The evaluation focuses on overall classification accuracy, SNR-dependent performance, and class-level prediction behavior.

---

# Overall Model Performance

| Model | Overall Accuracy | High-SNR Accuracy (≥ 0 dB) | Low-SNR Accuracy (< 0 dB) |
|---|---:|---:|---:|
| Baseline CNN | **56.43%** | **83.24%** | **29.51%** |
| Improved CNN | **62.29%** | **92.08%** | **32.39%** |

The improved CNN provides:

- Higher overall classification accuracy
- Better performance at high SNR
- Better performance at low SNR
- Improved robustness compared with the baseline CNN

---

# 1. Baseline CNN Results

The baseline CNN is the reference model used for comparison.

## Overall Accuracy

```text
56.43%
```

## High-SNR Performance

```text
83.24%
```

for:

```text
SNR ≥ 0 dB
```

## Low-SNR Performance

```text
29.51%
```

for:

```text
SNR < 0 dB
```

---

## Baseline Accuracy vs SNR

The following graph shows how the baseline CNN classification accuracy changes with signal-to-noise ratio.

![Baseline Accuracy vs SNR](baseline_accuracy_vs_snr.png)

### Interpretation

The baseline CNN performs poorly at very low SNR because the modulation characteristics are heavily affected by noise.

As SNR increases, the signal becomes easier to distinguish and classification accuracy improves significantly.

---

## Baseline Confusion Matrix

![Baseline Confusion Matrix](baseline_confusion_matrix.png)

### Interpretation

The confusion matrix shows the relationship between:

```text
True Modulation
        ↓
Predicted Modulation
```

The diagonal elements represent correctly classified samples.

Off-diagonal values indicate confusion between modulation classes.

---

## Baseline Normalized Confusion Matrix

![Baseline Normalized Confusion Matrix](baseline_normalized_confusion_matrix.png)

### Interpretation

The normalized confusion matrix represents classification performance relative to the number of samples in each true class.

Values closer to:

```text
1.00
```

on the diagonal indicate stronger classification performance for that class.

---

# 2. Improved CNN Results

The improved CNN is the enhanced model developed to improve modulation classification performance.

## Overall Accuracy

```text
62.29%
```

## High-SNR Performance

```text
92.08%
```

for:

```text
SNR ≥ 0 dB
```

## Low-SNR Performance

```text
32.39%
```

for:

```text
SNR < 0 dB
```

---

## Improved Accuracy vs SNR

![Improved Accuracy vs SNR](improved_accuracy_vs_snr.png)

### Interpretation

The improved CNN shows a strong relationship between signal quality and classification accuracy.

At low SNR, the model has difficulty distinguishing modulation characteristics because the signal is strongly affected by noise.

As SNR increases, the classification accuracy improves substantially.

The improved model reaches its strongest performance at higher SNR levels.

---

## Improved Confusion Matrix

![Improved Confusion Matrix](improved_confusion_matrix.png)

### Interpretation

The confusion matrix provides class-level information about the improved CNN.

The diagonal represents correct predictions, while off-diagonal elements represent incorrect classifications.

This allows frequently confused modulation classes to be identified.

---

## Improved Normalized Confusion Matrix

![Improved Normalized Confusion Matrix](improved_normalized_confusion_matrix.png)

### Interpretation

The normalized confusion matrix makes it easier to compare the classification performance of individual modulation classes.

A strong diagonal indicates that the model correctly identifies a large proportion of samples for that class.

---

# 3. Baseline vs Improved CNN

The main comparison is:

```text
Baseline CNN
     ↓
56.43%

Improved CNN
     ↓
62.29%
```

The improvement in overall accuracy is:

```text
62.29 - 56.43
= 5.86 percentage points
```

The improved CNN therefore performs better than the baseline model on the same evaluation dataset.

---

# 4. SNR Performance Comparison

The high-SNR comparison is:

```text
Baseline CNN
83.24%

Improved CNN
92.08%
```

Improvement:

```text
92.08 - 83.24
= 8.84 percentage points
```

The improved model therefore shows a substantial improvement when the received signal has adequate SNR.

---

# 5. Low-SNR Performance Comparison

The low-SNR comparison is:

```text
Baseline CNN
29.51%

Improved CNN
32.39%
```

Improvement:

```text
32.39 - 29.51
= 2.88 percentage points
```

The improvement is smaller at low SNR because classification becomes significantly more difficult when the signal is heavily corrupted by noise.

---

# 6. What the Results Demonstrate

The evaluation demonstrates three important characteristics of RF modulation classification.

### 1. Signal Quality Matters

Classification accuracy depends strongly on SNR.

```text
Low SNR
   ↓
More Noise
   ↓
Harder Classification
```

and:

```text
High SNR
   ↓
Cleaner Signal
   ↓
Better Classification
```

### 2. Model Architecture Matters

The improved residual CNN performs better than the baseline CNN.

```text
Baseline CNN
56.43%

        ↓

Improved CNN
62.29%
```

### 3. Classification Is Class-Dependent

The confusion matrices show that some modulation types are easier to distinguish than others.

This is particularly important for visually similar modulation classes.

---

# 7. Evaluation Pipeline

The results were generated using the following pipeline:

```text
RadioML 2016.10a
        ↓
Data Preprocessing
        ↓
Train / Validation / Test Split
        ↓
Trained CNN
        ↓
Test Dataset
        ↓
Predictions
        ↓
Evaluation
        ├── Accuracy
        ├── Precision
        ├── Recall
        ├── F1-Score
        ├── Confusion Matrix
        └── Accuracy vs SNR
```

---

# 8. Modulation Classes

The classifier evaluates the following 11 modulation classes:

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

---

# 9. Important Result

The current preferred model for the final software system is:

```text
Improved CNN
```

because it achieved:

```text
Overall Accuracy:
62.29%

High-SNR Accuracy:
92.08%

Low-SNR Accuracy:
32.39%
```

The model is therefore used as the current candidate for the final RF modulation identification pipeline.

---

# 10. Final Project Pipeline

The evaluation results connect the machine-learning system to the final application:

```text
RF / IQ Signal
       ↓
Signal Preprocessing
       ↓
Feature Representation
       ↓
Improved CNN
       ↓
Modulation Classification
       ↓
Confidence Score
       ↓
Visualization
       ↓
Final User Interface
```

The eventual live system can extend this pipeline to:

```text
RTL-SDR / SDR Hardware
       ↓
Live IQ Acquisition
       ↓
Signal Processing
       ↓
Improved CNN
       ↓
Modulation Prediction
       ↓
Confidence
       ↓
Live Spectrum / Spectrogram / Constellation
```

---

# 11. Result Files

The directory contains the following visual results:

```text
Baseline:
├── baseline_accuracy_vs_snr.png
├── baseline_confusion_matrix.png
└── baseline_normalized_confusion_matrix.png

Improved:
├── improved_accuracy_vs_snr.png
├── improved_confusion_matrix.png
└── improved_normalized_confusion_matrix.png
```

Text reports are also generated:

```text
baseline_classification_report.txt
baseline_accuracy_vs_snr.txt
baseline_evaluation_summary.txt

improved_classification_report.txt
improved_accuracy_vs_snr.txt
improved_evaluation_summary.txt
```

---

# 12. Final Summary

| Measurement | Baseline CNN | Improved CNN |
|---|---:|---:|
| Overall Accuracy | 56.43% | **62.29%** |
| High-SNR Accuracy | 83.24% | **92.08%** |
| Low-SNR Accuracy | 29.51% | **32.39%** |

The evaluation confirms that the improved CNN provides better classification performance than the baseline CNN.

The results also demonstrate that RF modulation classification performance is strongly dependent on signal quality, particularly SNR.

These evaluation results form the quantitative basis for selecting the improved CNN for the next stage of the project: **the final visualization and live RF signal identification system**.
