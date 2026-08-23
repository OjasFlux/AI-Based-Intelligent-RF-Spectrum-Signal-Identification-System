# Evaluation

The `evaluation/` directory contains the reusable evaluation pipeline for the RF modulation classification models.

The evaluation methodology is based on:

```text
06_model_evaluation.ipynb
08_improved_model_evaluation.ipynb
```

The evaluation system supports both the baseline CNN and the improved CNN.

---

## Directory Structure

```text
evaluation/
├── __init__.py
├── evaluate_model.py
├── results/
└── README.md
```

---

## 1. Purpose

The evaluation stage determines how well the trained CNN models classify RF modulation signals.

The evaluation pipeline is:

```text
Processed Test Data
        ↓
Load Trained Model
        ↓
Prepare IQ Input
        ↓
Generate Predictions
        ↓
Calculate Metrics
        ↓
Confusion Matrix
        ↓
SNR Analysis
        ↓
Confidence Analysis
        ↓
Save Evaluation Results
```

---

## 2. Supported Models

Two models are supported.

### Baseline CNN

```text
Model:
Baseline CNN

Input:
(2, 128, 1)

Model File:
best_cnn_modulation_classifier.keras
```

### Improved CNN

```text
Model:
Improved CNN

Input:
(128, 2)

Model File:
best_improved_cnn_classifier.keras
```

---

## 3. Test Dataset

Evaluation uses the processed test data:

```text
data/processed/
├── X_test.npy
├── y_test.npy
├── snr_test.npy
└── modulation_classes.npy
```

The same test dataset is used to compare the baseline and improved models.

---

## 4. Input Preparation

The processed IQ data initially has the form:

```text
(samples, 2, 128)
```

The baseline CNN requires:

```text
(samples, 2, 128, 1)
```

Therefore an additional channel dimension is added.

The improved CNN requires:

```text
(samples, 128, 2)
```

Therefore the I/Q and sample dimensions are transposed.

```text
Baseline:

(samples, 2, 128)
        ↓
(samples, 2, 128, 1)


Improved:

(samples, 2, 128)
        ↓
(samples, 128, 2)
```

---

## 5. Prediction

The trained Keras model generates probability values for all 11 modulation classes.

The predicted class is obtained using the highest probability:

```text
Softmax Probabilities
        ↓
Maximum Probability
        ↓
Predicted Modulation
```

Prediction confidence is calculated as:

```text
Confidence =
Maximum Softmax Probability
```

---

## 6. Evaluation Metrics

The evaluation pipeline calculates:

```text
Overall Accuracy
Precision
Recall
F1-Score
Classification Report
Confusion Matrix
Normalized Confusion Matrix
```

These metrics provide both overall and per-class performance.

---

## 7. Classification Report

The classification report contains:

```text
Precision
Recall
F1-Score
Support
```

for every modulation class.

The report is saved as:

```text
baseline_classification_report.txt
```

or:

```text
improved_classification_report.txt
```

depending on the evaluated model.

---

## 8. Confusion Matrix

The confusion matrix shows:

```text
True Modulation
        vs
Predicted Modulation
```

It helps identify modulation classes that are frequently confused with each other.

The generated files are:

```text
baseline_confusion_matrix.png
baseline_normalized_confusion_matrix.png
```

or:

```text
improved_confusion_matrix.png
improved_normalized_confusion_matrix.png
```

---

## 9. Normalized Confusion Matrix

The normalized confusion matrix represents each row as a proportion of the true class.

This makes it easier to compare classification performance across classes.

Example interpretation:

```text
0.90
```

on the diagonal means approximately:

```text
90% of samples from that true class
were correctly classified.
```

---

## 10. Accuracy vs SNR

RF modulation classification performance depends strongly on signal-to-noise ratio.

The evaluation therefore calculates accuracy separately for every available SNR level.

The process is:

```text
Test Dataset
      ↓
Group Samples by SNR
      ↓
Calculate Accuracy
      ↓
Accuracy vs SNR
```

The output graph is:

```text
*_accuracy_vs_snr.png
```

---

## 11. High-SNR and Low-SNR Performance

The evaluation separates the test data into:

```text
High SNR:
SNR >= 0 dB

Low SNR:
SNR < 0 dB
```

Accuracy is calculated independently for both groups.

This provides a clearer understanding of model performance under clean and noisy signal conditions.

---

## 12. Prediction Confidence

The evaluation calculates:

```text
Overall Prediction Confidence
Correct Prediction Confidence
Incorrect Prediction Confidence
```

This helps analyze how confident the model is when making classifications.

---

## 13. Best and Worst SNR

The evaluation identifies:

```text
Best SNR
```

where the classification accuracy is highest, and:

```text
Worst SNR
```

where the classification accuracy is lowest.

This information is included in the evaluation summary.

---

## 14. Evaluation Results

The evaluation results are stored under:

```text
evaluation/results/
```

Typical output files include:

```text
evaluation/results/
├── baseline_classification_report.txt
├── baseline_confusion_matrix.png
├── baseline_normalized_confusion_matrix.png
├── baseline_accuracy_vs_snr.png
├── baseline_accuracy_vs_snr.txt
├── baseline_evaluation_summary.txt
│
├── improved_classification_report.txt
├── improved_confusion_matrix.png
├── improved_normalized_confusion_matrix.png
├── improved_accuracy_vs_snr.png
├── improved_accuracy_vs_snr.txt
└── improved_evaluation_summary.txt
```

---

## 15. Running the Baseline Evaluation

From the project root:

```powershell
python evaluation/evaluate_model.py --model baseline
```

This evaluates:

```text
best_cnn_modulation_classifier.keras
```

---

## 16. Running the Improved Evaluation

From the project root:

```powershell
python evaluation/evaluate_model.py --model improved
```

This evaluates:

```text
best_improved_cnn_classifier.keras
```

The improved model is the default if `--model` is not specified.

Therefore:

```powershell
python evaluation/evaluate_model.py
```

is equivalent to:

```powershell
python evaluation/evaluate_model.py --model improved
```

---

## 17. Batch Size

The default prediction batch size is:

```text
256
```

It can be changed using:

```powershell
python evaluation/evaluate_model.py --model improved --batch-size 128
```

This may be useful when system memory is limited.

---

## 18. Verified Project Results

The completed notebook evaluation produced the following verified results.

### Baseline CNN

```text
Overall Test Accuracy:
56.43%

High SNR Accuracy (SNR >= 0 dB):
83.24%

Low SNR Accuracy (SNR < 0 dB):
29.51%
```

### Improved CNN

```text
Overall Test Accuracy:
62.29%

High SNR Accuracy (SNR >= 0 dB):
92.08%

Low SNR Accuracy (SNR < 0 dB):
32.39%
```

The improved CNN therefore provides better overall and high-SNR classification performance than the baseline CNN.

---

## 19. Evaluation Comparison

```text
Baseline CNN
      ↓
56.43%
      ↓
Evaluation
      ↓
Improved CNN
      ↓
62.29%
```

The evaluation stage provides the evidence required to compare the two model architectures.

---

## 20. Relationship With Other Project Modules

The evaluation module receives data from:

```text
data/processed/
```

and trained models from:

```text
saved_models/
```

It produces results for:

```text
testing/
visualization/
documentation/
final presentation
```

The complete relationship is:

```text
data/processed/
       ↓
evaluation/
       ↑
saved_models/
       ↓
Evaluation Results
       ↓
Analysis
       ↓
Final Model Selection
```

---

## 21. Evaluation and Final Model

The evaluation stage is used to select the model for the final prediction system.

Current results show:

```text
Baseline CNN:
56.43%

Improved CNN:
62.29%
```

Therefore the improved CNN is currently the preferred model for the final software classification pipeline.

---

## 22. Reproducibility

The evaluation uses:

```text
Same processed test dataset
Same modulation labels
Same trained model
Same prediction procedure
Same evaluation metrics
```

This allows the baseline and improved models to be compared using the same evaluation conditions.

---

## 23. Important Note

The evaluation script does not retrain the model.

It only:

```text
Loads trained model
       ↓
Loads test data
       ↓
Runs predictions
       ↓
Calculates evaluation metrics
       ↓
Saves results
```

Training remains a separate stage of the project.

---

## 24. Summary

The `evaluation/` directory converts the model-testing work from the experimental notebooks into a reusable evaluation pipeline.

It evaluates:

```text
Accuracy
Precision
Recall
F1-Score
Confusion Matrix
SNR Performance
Prediction Confidence
```

for both:

```text
Baseline CNN
```

and:

```text
Improved CNN
```

This provides the quantitative evidence used to select the improved CNN for the final RF modulation classification system.
