# Methodology

## AI Based Intelligent RF Spectrum Signal Identification System

## 1. Introduction

The methodology defines the complete procedure used to develop the AI-based RF spectrum signal identification system.

The project follows a software-based machine learning workflow in which RF signals are represented as I/Q samples, processed, used for CNN training, and finally classified according to their modulation type.

The methodology is divided into the following major stages:

```text
Problem Definition
       ↓
Dataset Collection
       ↓
Dataset Analysis
       ↓
Data Preprocessing
       ↓
Feature / Input Preparation
       ↓
CNN Model Development
       ↓
Model Training
       ↓
Model Evaluation
       ↓
Model Improvement
       ↓
Final Model Selection
       ↓
Prediction System
       ↓
Signal Visualization
       ↓
Software Dashboard
       ↓
Optional RTL-SDR Integration
```

---

## 2. Problem Definition

The first stage is to define the problem of automatic modulation classification.

In conventional communication systems, identifying the modulation type of an unknown RF signal may require prior knowledge or manual analysis.

The objective of this project is to develop an AI-based system that can automatically identify the modulation type from RF signal I/Q samples.

The basic problem is:

```text
Unknown RF Signal
       ↓
I/Q Samples
       ↓
AI Model
       ↓
Modulation Type
```

The system is intended to support applications such as:

- RF spectrum monitoring
- Wireless communication analysis
- Cognitive radio
- Signal identification
- Spectrum management
- Communication system monitoring

---

## 3. Dataset Collection

The project uses the **RadioML 2016.10a** dataset for software-based development and evaluation.

The dataset contains simulated RF communication signals represented as I/Q samples.

Each signal is associated with:

- Modulation type
- Signal-to-Noise Ratio (SNR)
- I/Q signal samples

The dataset contains 11 modulation classes used by this project:

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

The dataset contains SNR levels ranging from:

```text
-20 dB to +18 dB
```

---

## 4. Dataset Analysis

Before training the AI model, the dataset is analyzed to understand its structure.

The analysis includes:

- Number of samples
- Number of modulation classes
- Available SNR levels
- I/Q signal dimensions
- Data distribution
- Label structure

The signal format used in the project is:

```text
2 × 128
```

where:

```text
2   → I and Q channels
128 → Signal samples
```

The dataset analysis ensures that the data is correctly understood before preprocessing.

---

## 5. Data Preprocessing

The raw IQ data is prepared before being provided to the AI model.

The preprocessing workflow is:

```text
Raw Dataset
     ↓
Load Dataset
     ↓
Extract IQ Samples
     ↓
Extract Labels
     ↓
Extract SNR
     ↓
Normalize IQ Data
     ↓
Encode Labels
     ↓
Split Dataset
     ↓
Prepare CNN Input
```

---

## 6. IQ Signal Preparation

Each signal consists of two components:

```text
I → In-phase
Q → Quadrature
```

The original signal representation is:

```text
(2, 128)
```

For the improved 1D CNN, the signal is rearranged to:

```text
(128, 2)
```

This allows the CNN to process the 128 signal samples as a sequence while treating I and Q as two input channels.

The input structure becomes:

```text
Time Samples
     ↓
128 samples
     ×
2 channels
     ↓
I and Q
```

---

## 7. Signal Normalization

Signal normalization is performed to prepare the IQ samples for machine learning.

Normalization helps maintain a consistent numerical range and allows the neural network to learn signal characteristics more effectively.

The normalized signals are then stored in the processed dataset.

The processed data is stored under:

```text
data/processed/
```

---

## 8. Label Preparation

Each modulation type is converted into a numerical class label.

Conceptually:

```text
8PSK   → Class 0
AM-DSB → Class 1
AM-SSB → Class 2
...
QPSK   → Class 9
WBFM   → Class 10
```

The exact class-to-index mapping is stored in:

```text
modulation_classes.npy
```

The labels are converted into a format suitable for CNN classification.

---

## 9. Dataset Splitting

The processed dataset is divided into three parts:

```text
Training
Validation
Testing
```

The project uses an approximate distribution of:

```text
Training       → 70%
Validation     → 10%
Testing        → 20%
```

The purpose of each subset is:

### Training Dataset

Used to learn the relationship between IQ signal characteristics and modulation classes.

### Validation Dataset

Used during model training to monitor model performance on data that is not directly used for weight optimization.

### Testing Dataset

Used after training to measure performance on unseen signal samples.

The overall split is:

```text
                 Complete Dataset
                        │
          ┌─────────────┼─────────────┐
          ▼             ▼             ▼
      Training      Validation      Testing
        70%            10%            20%
```

---

## 10. Feature and Signal Representation

The project primarily uses raw I/Q samples as the input representation for the CNN.

Additional representations are used for signal analysis and visualization.

These include:

### I/Q Time-Domain Representation

Shows the amplitude variation of the I and Q components over the signal samples.

### FFT Representation

Converts the signal from the time domain to the frequency domain.

```text
IQ Signal
    ↓
FFT
    ↓
Frequency Spectrum
```

### Constellation Representation

Uses the I and Q values to visualize signal symbol distribution.

```text
I → Horizontal Axis
Q → Vertical Axis
```

### Spectrogram

Displays the frequency characteristics of a signal over time.

These representations are useful for understanding signal characteristics and presenting the system results.

---

## 11. CNN Model Development

A CNN-based deep learning approach is used for automatic modulation classification.

The project initially develops a baseline CNN model.

The baseline model is used to establish a reference performance.

The initial CNN achieved approximately:

```text
Test Accuracy = 56.43%
```

This result is then used as the baseline for model improvement.

---

## 12. Improved CNN Development

After evaluating the baseline model, an improved 1D CNN architecture is developed.

The improved architecture is designed specifically to process sequential I/Q signal data.

The main structure is:

```text
I/Q Input
    ↓
Conv1D
    ↓
Batch Normalization
    ↓
Residual Block
    ↓
Pooling
    ↓
Residual Block
    ↓
Pooling
    ↓
Residual Block
    ↓
Pooling
    ↓
Feature Extraction
    ↓
Global Average Pooling
    ↓
Dense Layers
    ↓
Dropout
    ↓
Softmax
```

Residual connections are used to improve feature learning and information flow through the network.

---

## 13. Model Training

The improved CNN is trained using the training dataset.

During training:

```text
Training IQ Samples
        ↓
CNN
        ↓
Predicted Classes
        ↓
Compare With Actual Labels
        ↓
Calculate Loss
        ↓
Update Model Weights
```

The validation dataset is used to monitor model performance during training.

---

## 14. Training Configuration

The improved model uses:

```text
Optimizer:
Adam

Loss Function:
Categorical Crossentropy

Output Activation:
Softmax

Batch Size:
256

Maximum Epochs:
60
```

Training control mechanisms include:

- Early stopping
- Model checkpointing
- Learning-rate reduction

These techniques help prevent unnecessary training and improve training stability.

---

## 15. Early Stopping

Early stopping is used to monitor validation performance.

If the validation loss does not improve for a specified number of epochs, training can stop automatically.

The purpose is to:

- Reduce unnecessary training
- Reduce overfitting
- Preserve the best model weights

The best model is saved based on validation performance.

---

## 16. Model Checkpointing

During training, the best-performing model is saved.

The saved model is stored as a Keras model file.

The current improved model is represented by:

```text
best_improved_cnn_classifier.keras
```

The trained model can later be loaded without retraining the network.

---

## 17. Model Evaluation

After training, the improved CNN is evaluated using unseen test data.

The evaluation process is:

```text
Test IQ Samples
       ↓
Trained CNN
       ↓
Predicted Classes
       ↓
Compare With Actual Classes
       ↓
Performance Metrics
```

The following metrics are generated:

- Accuracy
- Precision
- Recall
- F1-score
- Confusion matrix
- Normalized confusion matrix
- Accuracy versus SNR
- Prediction confidence

---

## 18. Baseline and Improved Model Comparison

The project compares the original CNN with the improved CNN.

The baseline model achieved:

```text
56.43%
```

The improved CNN achieved:

```text
62.29%
```

The improvement is:

```text
62.29% - 56.43%
= 5.86 percentage points
```

Therefore, the improved CNN provides better overall test performance than the baseline model.

---

## 19. SNR-Based Evaluation

The model is evaluated separately at different SNR levels.

This is important because RF signals with low SNR contain more noise and are more difficult to classify.

The improved model achieved approximately:

```text
High SNR (>= 0 dB)
92.08%

Low SNR (< 0 dB)
32.39%
```

This demonstrates that classification performance depends strongly on signal quality.

The evaluation therefore does not rely only on overall accuracy.

---

## 20. Confusion Matrix Analysis

A confusion matrix is generated to understand how the model classifies individual modulation types.

The matrix compares:

```text
Actual Modulation
        vs
Predicted Modulation
```

The diagonal elements represent correct classifications.

Off-diagonal elements represent classification errors.

The confusion matrix helps identify modulation classes that are difficult for the model to distinguish.

---

## 21. Precision, Recall and F1-Score

The model is also evaluated using:

### Precision

Precision measures how many signals predicted as a particular modulation actually belong to that modulation class.

```text
Precision =
True Positives /
(True Positives + False Positives)
```

### Recall

Recall measures how many actual signals of a modulation class were correctly identified.

```text
Recall =
True Positives /
(True Positives + False Negatives)
```

### F1-Score

F1-score combines precision and recall.

```text
F1 =
2 × Precision × Recall /
(Precision + Recall)
```

These metrics provide more detailed information than accuracy alone.

---

## 22. Prediction Process

After selecting the trained model, an unseen IQ signal can be provided to the system.

The prediction workflow is:

```text
Unseen IQ Signal
       ↓
Preprocessing
       ↓
CNN Input Preparation
       ↓
Trained CNN
       ↓
Class Probabilities
       ↓
Highest Probability
       ↓
Predicted Modulation
```

The output contains:

```text
Modulation Type
Prediction Confidence
```

For example:

```text
Predicted Modulation : QPSK
Confidence           : 94.7%
```

The actual confidence value depends on the input signal and model prediction.

---

## 23. Signal Visualization During Prediction

When a signal is classified, the system can also generate visual representations.

The prediction interface can display:

```text
             Predicted Modulation
                      │
                      ▼
              Confidence Score
                      │
        ┌─────────────┼─────────────┐
        ▼             ▼             ▼
    Time Domain      FFT       Constellation
                      │
                      ▼
                 Spectrogram
```

These visualizations help users understand the received signal and the classification result.

---

## 24. Software Integration

After validating the AI model, the project moves from notebook-based experimentation to reusable Python modules.

The intended architecture is:

```text
features/
     ↓
Preprocessing

models/
     ↓
CNN Architecture

saved_models/
     ↓
Trained Model

testing/
     ↓
Prediction

visualization/
     ↓
Signal Visualization

evaluation/
     ↓
Performance Analysis

app/
     ↓
Final Dashboard
```

This separation makes the project easier to maintain and extend.

---

## 25. Final Software Workflow

The complete software workflow is:

```text
Input IQ Signal
       ↓
Data Validation
       ↓
Preprocessing
       ↓
CNN Input Preparation
       ↓
Load Trained Model
       ↓
Model Prediction
       ↓
Modulation Classification
       ↓
Confidence Calculation
       ↓
Signal Visualization
       ↓
Display Results
```

---

## 26. Optional RTL-SDR Methodology

After completing the software implementation, the system can optionally be connected to an RTL-SDR receiver.

The hardware-based methodology is:

```text
RF Environment
      ↓
Antenna
      ↓
RTL-SDR Receiver
      ↓
RF Tuning
      ↓
IQ Sample Acquisition
      ↓
Signal Preprocessing
      ↓
CNN Model
      ↓
Modulation Classification
      ↓
Visualization
      ↓
Dashboard
```

The same trained AI model can be used if the live IQ data is prepared in a compatible format.

---

## 27. Hardware Integration Considerations

The optional RTL-SDR implementation requires consideration of:

- Center frequency
- Sampling rate
- Signal bandwidth
- Gain
- IQ sample format
- Buffer size
- Noise level
- Signal preprocessing
- Model input format

The hardware implementation is treated as an extension after the software-based model is validated.

---

## 28. Complete Methodology

The complete methodology can therefore be summarized as:

```text
                    Problem Definition
                           │
                           ▼
                    Dataset Collection
                           │
                           ▼
                     Dataset Analysis
                           │
                           ▼
                    Data Preprocessing
                           │
                           ▼
                 IQ / Feature Preparation
                           │
                           ▼
                    CNN Development
                           │
                           ▼
                     Model Training
                           │
                           ▼
                    Model Evaluation
                           │
                           ▼
                    Model Improvement
                           │
                           ▼
                  Final Model Selection
                           │
                           ▼
                    Prediction System
                           │
                           ▼
                 Signal Visualization
                           │
                           ▼
                   Software Dashboard
                           │
                           ▼
                Optional RTL-SDR System
```

---

## 29. Current Methodology Status

The following stages have been completed:

```text
Problem Definition             ✅
Dataset Collection             ✅
Dataset Analysis               ✅
Data Preprocessing             ✅
IQ Input Preparation           ✅
Baseline CNN Development       ✅
Baseline CNN Training          ✅
Baseline Evaluation            ✅
Improved CNN Development       ✅
Improved CNN Training          ✅
Improved Evaluation            ✅
```

The next implementation stages are:

```text
Reusable Python Modules
        ↓
Prediction Engine
        ↓
Testing
        ↓
Visualization Modules
        ↓
Software Dashboard
        ↓
Complete System Integration
        ↓
Optional RTL-SDR Integration
```

---

## 30. Methodology Summary

The project follows a systematic machine learning methodology for automatic RF modulation classification.

The approach begins with the RadioML 2016.10a dataset and processes its I/Q signal samples through preprocessing and input preparation stages.

A baseline CNN is first developed and evaluated.

An improved 1D CNN with residual feature blocks is then developed to improve classification performance.

The improved model is evaluated using overall accuracy, precision, recall, F1-score, confusion matrix, and SNR-based performance.

Once the model is validated, it can be integrated into a reusable prediction system and later connected to a software dashboard.

An RTL-SDR receiver can be added as an optional hardware extension to enable live RF signal acquisition and classification.

The methodology therefore provides a complete path from:

```text
RF Dataset
     ↓
Signal Processing
     ↓
Artificial Intelligence
     ↓
Modulation Classification
     ↓
Signal Visualization
     ↓
Software System
     ↓
Optional Live RF Hardware
```
