# Model Evaluation

## AI Based Intelligent RF Spectrum Signal Identification System

## 1. Introduction

Model evaluation is used to determine how accurately the trained AI model can identify the modulation type of unseen RF signals.

After training, the model is tested using signal samples that were not used for updating the model weights.

The evaluation process is:

```text
Trained CNN
     ↓
Unseen Test IQ Samples
     ↓
Predictions
     ↓
Compare With Actual Labels
     ↓
Performance Metrics
     ↓
Model Analysis
```

The evaluation stage helps determine:

- Overall classification accuracy
- Per-class performance
- Classification errors
- Effect of SNR on performance
- Difference between baseline and improved models
- Suitability of the trained model for prediction

---

## 2. Evaluation Dataset

The evaluation uses the test dataset generated during preprocessing.

The main files are:

```text
data/processed/
├── X_test.npy
├── y_test.npy
└── snr_test.npy
```

Where:

```text
X_test.npy
    ↓
Unseen IQ signal samples

y_test.npy
    ↓
Actual modulation labels

snr_test.npy
    ↓
SNR value for each test signal
```

The test dataset is kept separate from the training process.

---

## 3. Evaluation Workflow

The complete evaluation workflow is:

```text
Processed Test Dataset
          │
          ▼
     Load Test Data
          │
          ▼
    Load Trained CNN
          │
          ▼
     Model Prediction
          │
          ▼
 Predicted Class Probabilities
          │
          ▼
    Predicted Labels
          │
          ▼
 Compare Actual vs Predicted
          │
          ├───────────────┐
          ▼               ▼
   Classification     Confusion
      Metrics          Matrix
          │               │
          └───────┬───────┘
                  ▼
             SNR Analysis
                  │
                  ▼
          Final Evaluation
```

---

## 4. Evaluation Metrics

The project evaluates the model using:

- Accuracy
- Precision
- Recall
- F1-score
- Confusion matrix
- Normalized confusion matrix
- SNR-wise accuracy
- Prediction confidence

These metrics provide a more complete understanding of model performance than accuracy alone.

---

# 5. Accuracy

Accuracy represents the percentage of test signals correctly classified by the model.

The formula is:

```text
Accuracy =
Correct Predictions / Total Predictions
```

For example, if:

```text
1000 signals
```

are tested and:

```text
700 signals
```

are classified correctly:

```text
Accuracy = 700 / 1000
         = 70%
```

---

## 6. Baseline Model Accuracy

The original CNN was evaluated as the baseline model.

The measured test accuracy was approximately:

```text
56.43%
```

This result provides the reference performance for comparison with the improved CNN.

---

## 7. Improved Model Accuracy

The improved 1D residual CNN achieved approximately:

```text
62.29%
```

overall test accuracy.

The comparison is:

| Model | Test Accuracy |
|---|---:|
| Original CNN | 56.43% |
| Improved CNN | 62.29% |

The improvement is:

```text
62.29 - 56.43
= 5.86 percentage points
```

Therefore, the improved CNN performs better than the original baseline model on the evaluated test set.

---

# 8. Precision

Precision measures how many signals predicted as a particular modulation class actually belong to that class.

The formula is:

```text
Precision =
True Positives /
(True Positives + False Positives)
```

A high precision means that when the model predicts a particular modulation, it is usually correct.

---

# 9. Recall

Recall measures how many of the actual signals belonging to a modulation class were correctly identified.

The formula is:

```text
Recall =
True Positives /
(True Positives + False Negatives)
```

A high recall means that the model is able to detect most of the signals belonging to that class.

---

# 10. F1-Score

F1-score combines precision and recall into a single metric.

The formula is:

```text
F1-Score =
2 × Precision × Recall /
(Precision + Recall)
```

F1-score is useful when both false positives and false negatives need to be considered.

---

# 11. Classification Report

A classification report is generated for the test dataset.

It provides class-wise:

```text
Precision
Recall
F1-Score
Support
```

The report can be used to identify:

- Strongly classified modulation classes
- Weakly classified modulation classes
- Classes that are frequently confused
- Overall macro and weighted performance

The report is generated after the model produces predictions for the test dataset.

---

# 12. Supported Classes

The evaluation covers the following 11 modulation classes:

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

The confusion matrix and classification report use these classes.

---

# 13. Confusion Matrix

A confusion matrix compares:

```text
Actual Modulation
        vs
Predicted Modulation
```

The general structure is:

```text
                 Predicted
              ┌─────┬─────┬─────┐
              │  C1 │  C2 │ ... │
        ┌─────┼─────┼─────┼─────┤
Actual  │ C1  │     │     │     │
        ├─────┼─────┼─────┼─────┤
        │ C2  │     │     │     │
        ├─────┼─────┼─────┼─────┤
        │ ... │     │     │     │
        └─────┴─────┴─────┴─────┘
```

The diagonal represents correct predictions.

The off-diagonal elements represent classification errors.

---

# 14. Interpreting the Confusion Matrix

For example:

```text
Actual QPSK
      ↓
Predicted QPSK
```

represents a correct classification.

While:

```text
Actual QPSK
      ↓
Predicted 8PSK
```

represents a misclassification.

The confusion matrix helps determine which modulation classes are difficult for the model to distinguish.

---

# 15. Normalized Confusion Matrix

A normalized confusion matrix represents classification results as proportions or percentages rather than raw sample counts.

It helps compare classification performance between classes even when the number of samples differs.

Conceptually:

```text
Correct Classification
        ↓
High diagonal value

Incorrect Classification
        ↓
Off-diagonal value
```

A stronger diagonal generally indicates better per-class classification.

---

# 16. SNR-Based Evaluation

SNR-based evaluation is one of the important parts of this project.

The RadioML dataset contains signals with different SNR levels.

The model is therefore evaluated separately at different SNR values.

The process is:

```text
Test Samples
      ↓
Group Samples by SNR
      ↓
Predict Each Group
      ↓
Calculate Accuracy
      ↓
Accuracy vs SNR
```

---

# 17. Why SNR Analysis Is Important

RF signal classification becomes more difficult when noise increases.

At low SNR:

```text
Signal
   +
High Noise
   ↓
Signal Characteristics Become Less Clear
   ↓
Classification Becomes Difficult
```

At higher SNR:

```text
Signal
   +
Lower Relative Noise
   ↓
Signal Characteristics Become Clearer
   ↓
Classification Becomes Easier
```

Therefore, overall accuracy alone does not fully describe the model's behavior.

---

# 18. High-SNR Performance

The improved model achieved approximately:

```text
High SNR (>= 0 dB):
92.08%
```

This indicates that the model performs significantly better when the signal quality is relatively high.

---

# 19. Low-SNR Performance

For lower SNR conditions:

```text
Low SNR (< 0 dB):
32.39%
```

The lower performance indicates that noise makes it more difficult for the CNN to identify the modulation characteristics.

This is an important limitation of the current model.

---

# 20. SNR Performance Comparison

The evaluation can be represented conceptually as:

```text
Classification Accuracy
        │
100%    │
        │                    ████████
 80%    │                    ████████
        │                  ██████████
 60%    │              ██████████████
        │          ██████████████████
 40%    │     ███████████████████████
        │ ███████████████████████████
 20%    │
        └──────────────────────────────
             Low SNR      High SNR
```

The actual accuracy at each SNR level is obtained from the evaluation output.

---

# 21. Accuracy vs SNR Graph

The project generates an accuracy-versus-SNR graph.

The graph contains:

```text
X-axis:
SNR (dB)

Y-axis:
Classification Accuracy
```

The purpose is to show how model performance changes with signal quality.

The expected relationship is:

```text
SNR increases
      ↓
Signal quality improves
      ↓
Classification accuracy generally improves
```

---

# 22. Prediction Confidence

The CNN produces a probability for each modulation class.

The highest probability is selected as the predicted modulation.

For example:

```text
8PSK    → 0.03
BPSK    → 0.05
QPSK    → 0.89
QAM16   → 0.02
...
```

The prediction is:

```text
QPSK
```

with a model probability of approximately:

```text
89%
```

The exact confidence depends on the input signal.

---

# 23. Confidence Interpretation

Prediction confidence should be interpreted as the model's probability output, not as a guarantee that the prediction is correct.

For example:

```text
Prediction:
QPSK

Confidence:
95%
```

does not mean the system is guaranteed to be 95% correct.

It means that the model assigned approximately 95% probability to the QPSK class for that particular input.

This distinction is important when presenting the system.

---

# 24. Evaluation of Unseen Data

The final model is evaluated using signals that were not used to update the model weights.

The workflow is:

```text
Training Data
     ↓
Model Learning

Validation Data
     ↓
Training Monitoring

Test Data
     ↓
Final Evaluation
```

This separation provides a more meaningful estimate of model performance.

---

# 25. Baseline vs Improved Model

The main model comparison is:

```text
Original CNN
     ↓
56.43%

        vs

Improved CNN
     ↓
62.29%
```

The improved model provides:

```text
5.86 percentage-point improvement
```

over the baseline model.

---

# 26. Why Overall Accuracy Is Not Enough

The overall accuracy of:

```text
62.29%
```

should not be interpreted alone.

The model also needs to be analyzed using:

```text
Precision
Recall
F1-Score
Confusion Matrix
SNR-Based Accuracy
```

For example, a model may have reasonable overall accuracy while performing poorly on a specific modulation class.

Therefore, class-level analysis is required.

---

# 27. Evaluation Visualization

The project generates several evaluation visualizations.

The important outputs include:

```text
Confusion Matrix
Normalized Confusion Matrix
Accuracy vs SNR
Training Accuracy
Validation Accuracy
Training Loss
Validation Loss
```

These visualizations help explain the behavior of the AI model.

---

# 28. Evaluation Directory

The final project evaluation results are intended to be organized under:

```text
evaluation/
├── evaluate_model.py
├── classification_report.txt
├── confusion_matrix.png
├── normalized_confusion_matrix.png
├── accuracy_vs_snr.png
└── evaluation_summary.txt
```

The exact filenames may be adjusted as the final evaluation scripts are organized.

---

# 29. Evaluation Script

The reusable evaluation implementation will eventually be stored in:

```text
evaluation/evaluate_model.py
```

The script will perform tasks such as:

```text
Load Test Dataset
      ↓
Load Trained Model
      ↓
Generate Predictions
      ↓
Calculate Accuracy
      ↓
Generate Classification Report
      ↓
Generate Confusion Matrix
      ↓
Calculate SNR-Wise Accuracy
      ↓
Save Evaluation Results
```

This allows evaluation to be performed without opening a Jupyter notebook.

---

# 30. Evaluation Notebook

The experimental evaluation is documented in:

```text
notebooks/08_improved_model_evaluation.ipynb
```

The notebook is used for:

- Model testing
- Classification metrics
- Confusion matrix
- SNR analysis
- Performance visualization
- Result verification

The reusable evaluation code will later be moved into:

```text
evaluation/evaluate_model.py
```

---

# 31. Evaluation Reproducibility

To reproduce the evaluation:

### Step 1

Ensure the processed test data exists:

```text
data/processed/X_test.npy
data/processed/y_test.npy
data/processed/snr_test.npy
```

### Step 2

Ensure the trained model is available.

```text
saved_models/
└── best_improved_cnn_classifier.keras
```

### Step 3

Load the trained model.

### Step 4

Load the test IQ signals.

### Step 5

Prepare the input shape:

```text
(samples, 128, 2)
```

### Step 6

Generate predictions.

### Step 7

Compare predicted labels with actual labels.

### Step 8

Generate evaluation metrics.

### Step 9

Generate confusion matrix.

### Step 10

Calculate accuracy at different SNR levels.

---

# 32. Evaluation Workflow for the Final System

The final evaluation pipeline will be:

```text
Saved Model
     │
     ▼
Test IQ Data
     │
     ▼
Same Preprocessing
     │
     ▼
CNN Prediction
     │
     ▼
Predicted Labels
     │
     ├─────────────► Accuracy
     │
     ├─────────────► Precision
     │
     ├─────────────► Recall
     │
     ├─────────────► F1-Score
     │
     ├─────────────► Confusion Matrix
     │
     └─────────────► SNR Analysis
```

---

# 33. Current Evaluation Results

The current verified model results are:

```text
Original CNN Test Accuracy:
56.43%

Improved CNN Test Accuracy:
62.29%

Improved CNN High-SNR Accuracy:
92.08%

Improved CNN Low-SNR Accuracy:
32.39%
```

These values represent the current project evaluation results.

---

# 34. Interpretation of Current Results

The results demonstrate two important points.

### Model Improvement

The improved CNN performs better than the original baseline:

```text
56.43%
     ↓
62.29%
```

### Effect of SNR

The model performs much better at higher SNR:

```text
Low SNR:
32.39%

High SNR:
92.08%
```

Therefore, signal quality is a major factor affecting modulation classification performance.

---

# 35. Current Limitations

The current evaluation has several limitations.

### 1. Dataset Dependency

The model is trained and tested using RadioML 2016.10a.

### 2. Low-SNR Performance

Classification performance decreases significantly at low SNR.

### 3. Simulated Data

The dataset does not represent every possible real-world RF environment.

### 4. Hardware Validation

Live RF classification using RTL-SDR has not yet been validated as part of the current software model evaluation.

### 5. Limited Modulation Classes

The current system supports 11 modulation classes.

---

# 36. Future Evaluation Improvements

Future evaluation can include:

- Real-world RF signals
- RTL-SDR captured signals
- Additional modulation types
- More SNR conditions
- Different sampling rates
- Different bandwidths
- Noise robustness testing
- Interference testing
- Cross-dataset evaluation
- Real-time classification performance
- Inference latency
- CPU/GPU resource usage

---

# 37. Evaluation for Future RTL-SDR

When hardware integration is implemented, evaluation can be extended:

```text
RTL-SDR
   ↓
Live RF Signal
   ↓
IQ Samples
   ↓
Preprocessing
   ↓
CNN
   ↓
Prediction
   ↓
Compare With Known Signal
   ↓
Hardware Classification Performance
```

This will allow comparison between:

```text
Dataset-Based Classification
        vs
Live RF Classification
```

---

# 38. Evaluation Summary

The evaluation stage verifies whether the trained CNN can correctly classify unseen RF I/Q signals.

The project currently reports:

```text
Baseline Accuracy:
56.43%

Improved Accuracy:
62.29%

High-SNR Accuracy:
92.08%

Low-SNR Accuracy:
32.39%
```

The model is evaluated using multiple metrics and visualizations rather than accuracy alone.

The complete evaluation process is:

```text
Test IQ Data
     ↓
Trained CNN
     ↓
Predictions
     ↓
Accuracy
     ↓
Precision / Recall / F1
     ↓
Confusion Matrix
     ↓
SNR Analysis
     ↓
Performance Interpretation
```

The evaluation results provide the basis for selecting the improved CNN as the current final model candidate and moving toward the prediction and software integration stages.
