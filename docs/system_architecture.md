# System Architecture

## AI Based Intelligent RF Spectrum Signal Identification System

## 1. Introduction

The AI Based Intelligent RF Spectrum Signal Identification System is designed to automatically identify the modulation type of a received RF signal using artificial intelligence.

The system processes RF signal information in the form of I/Q samples and applies a trained CNN-based deep learning model to classify the signal into one of the supported modulation classes.

The software-based system is initially developed and validated using the RadioML 2016.10a dataset.

An optional future hardware implementation can use an RTL-SDR receiver to capture live RF signals and provide IQ samples to the same processing and classification pipeline.

---

## 2. Overall System Architecture

The complete software architecture is represented as:

```text
                    RF Signal / Dataset
                           │
                           ▼
                  ┌──────────────────┐
                  │  Data Collection  │
                  └────────┬─────────┘
                           │
                           ▼
                  ┌──────────────────┐
                  │  Data Loading    │
                  └────────┬─────────┘
                           │
                           ▼
                  ┌──────────────────┐
                  │ Preprocessing    │
                  │                  │
                  │ • Normalization  │
                  │ • Label Encoding │
                  │ • Data Splitting │
                  └────────┬─────────┘
                           │
                           ▼
                  ┌──────────────────┐
                  │ Feature / Input  │
                  │ Preparation      │
                  │                  │
                  │ • IQ Samples     │
                  │ • FFT             │
                  │ • Spectrogram    │
                  └────────┬─────────┘
                           │
                           ▼
                  ┌──────────────────┐
                  │ CNN AI Model     │
                  │                  │
                  │ Feature Learning │
                  │ Classification   │
                  └────────┬─────────┘
                           │
                           ▼
                  ┌──────────────────┐
                  │   Prediction     │
                  └────────┬─────────┘
                           │
                           ▼
              ┌────────────────────────────┐
              │ Modulation Classification  │
              └─────────────┬──────────────┘
                            │
                ┌───────────┴───────────┐
                ▼                       ▼
       Modulation Type           Confidence Score
                │                       │
                └───────────┬───────────┘
                            ▼
                  ┌──────────────────┐
                  │ Visualization    │
                  │                  │
                  │ • IQ Signal      │
                  │ • FFT Spectrum   │
                  │ • Constellation  │
                  │ • Spectrogram    │
                  └────────┬─────────┘
                           │
                           ▼
                  ┌──────────────────┐
                  │ Software Output  │
                  │ / Dashboard      │
                  └──────────────────┘
```

---

## 3. Main System Components

The system is divided into the following major components:

1. Data Collection
2. Data Preprocessing
3. Feature and Input Preparation
4. AI Model
5. Model Training
6. Model Evaluation
7. Modulation Prediction
8. Signal Visualization
9. Software Output
10. Optional Hardware Integration

---

## 4. Data Collection Layer

The initial implementation uses the RadioML 2016.10a dataset.

The dataset provides RF communication signals represented using I/Q samples.

Each signal contains:

```text
I → In-phase component
Q → Quadrature component
```

The dataset contains multiple modulation classes and SNR levels.

The dataset is used for:

- AI model development
- Training
- Validation
- Testing
- Performance analysis

The dataset is documented in:

```text
docs/dataset.md
```

---

## 5. Data Preprocessing Layer

The raw dataset cannot be directly used without preparation.

The preprocessing stage performs:

- Loading the dataset
- Extracting IQ samples
- Creating modulation labels
- Encoding modulation labels
- Normalizing IQ signals
- Splitting the dataset
- Preparing CNN input

The project uses:

```text
70% → Training
10% → Validation
20% → Testing
```

The preprocessing workflow is:

```text
Raw IQ Data
     │
     ▼
Load Dataset
     │
     ▼
Extract I/Q Samples
     │
     ▼
Normalize
     │
     ▼
Encode Labels
     │
     ▼
Train / Validation / Test Split
     │
     ▼
Processed Dataset
```

---

## 6. Feature and Input Preparation

The project primarily uses raw I/Q samples as the input representation for the CNN.

The I and Q components contain information about the amplitude and phase characteristics of the RF signal.

Additional signal representations are generated for analysis and visualization, including:

- Time-domain I/Q signals
- FFT frequency spectrum
- Constellation diagrams
- Spectrograms

These representations help understand the differences between modulation types and support the analysis of model behavior.

---

## 7. AI Model Layer

The project uses a Convolutional Neural Network-based classifier.

Two model approaches were investigated:

### Original CNN

The first CNN was developed as a baseline model.

Its test accuracy was approximately:

```text
56.43%
```

### Improved CNN

An improved 1D CNN architecture was subsequently developed for I/Q signal processing.

The improved model achieved:

```text
Overall Test Accuracy: 62.29%
```

and approximately:

```text
High-SNR Accuracy (SNR >= 0 dB): 92.08%
```

The improved model is currently selected as the project's final model candidate.

---

## 8. CNN Input

The original I/Q data has the shape:

```text
(samples, 2, 128)
```

For the improved 1D CNN, the data is rearranged to:

```text
(samples, 128, 2)
```

where:

```text
128 → Signal samples / time sequence
2   → I and Q channels
```

Therefore, a single CNN input has the structure:

```text
128 time samples
       ×
2 signal channels
```

---

## 9. CNN Processing

The improved CNN performs feature extraction directly from the I/Q sequence.

The simplified processing structure is:

```text
I/Q Input
   │
   ▼
Conv1D
   │
   ▼
Batch Normalization
   │
   ▼
Residual Feature Block
   │
   ▼
Pooling
   │
   ▼
Residual Feature Block
   │
   ▼
Pooling
   │
   ▼
Residual Feature Block
   │
   ▼
Feature Aggregation
   │
   ▼
Dense Layers
   │
   ▼
Softmax Output
```

The final softmax layer produces probabilities for the supported modulation classes.

---

## 10. Classification Output

The model produces a probability for each supported modulation class.

The class with the highest predicted probability is selected as the predicted modulation.

Conceptually:

```text
                  CNN
                   │
                   ▼
        ┌────────────────────┐
        │ Class Probabilities │
        └─────────┬──────────┘
                  │
       ┌──────────┼───────────┐
       ▼          ▼           ▼
     BPSK       QPSK        8PSK ...
       │          │           │
       └──────────┼───────────┘
                  ▼
          Highest Probability
                  │
                  ▼
          Predicted Modulation
```

The system can also display the prediction confidence.

---

## 11. Model Evaluation Layer

The model is evaluated using an independent test dataset.

The evaluation includes:

- Overall accuracy
- Precision
- Recall
- F1-score
- Confusion matrix
- Normalized confusion matrix
- Accuracy versus SNR
- Prediction confidence

The SNR-based analysis is particularly important because RF classification performance changes with signal quality.

---

## 12. SNR-Based Performance

The improved model demonstrated significantly better classification performance at higher SNR levels.

The evaluation showed approximately:

```text
High SNR (>= 0 dB):
92.08%

Low SNR (< 0 dB):
32.39%
```

This demonstrates that signal quality has a major effect on automatic modulation classification.

At low SNR, noise can hide important modulation characteristics.

At higher SNR, the modulation characteristics become easier for the AI model to distinguish.

---

## 13. Signal Visualization Layer

The system provides multiple methods for visualizing RF signals.

### Time Domain

Displays the I and Q signal amplitudes over the sample sequence.

```text
Sample Number
      │
      ▼
I/Q Amplitude
```

### FFT Spectrum

Displays the frequency-domain representation of the signal.

```text
IQ Signal
    ↓
FFT
    ↓
Frequency Spectrum
```

### Constellation Diagram

Displays the relationship between I and Q values.

```text
I → Horizontal Axis
Q → Vertical Axis
```

### Spectrogram

Displays how the frequency content changes with time.

These visualizations are useful for:

- Signal analysis
- Project demonstration
- Model interpretation
- Debugging
- Final dashboard display

---

## 14. Software Output Layer

The final software system is intended to display the detected signal information in a user-friendly interface.

The expected output includes:

```text
Detected Modulation
Prediction Confidence
Signal Information
I/Q Signal
FFT Spectrum
Constellation Diagram
Spectrogram
System Status
```

A future dashboard can combine these components into a single interface.

---

## 15. Optional Hardware Architecture

The software system can later be connected to an RTL-SDR receiver.

The optional hardware architecture is:

```text
             Antenna
                │
                ▼
           RTL-SDR
                │
                ▼
        RF Signal Reception
                │
                ▼
             IQ Data
                │
                ▼
        Signal Preprocessing
                │
                ▼
        Trained CNN Model
                │
                ▼
       Modulation Prediction
                │
                ▼
          Visualization
                │
                ▼
            Dashboard
```

The hardware implementation is an optional extension of the software-based system.

---

## 16. Software-Only Architecture

The current validated implementation uses the RadioML dataset.

```text
RadioML Dataset
      │
      ▼
Data Preprocessing
      │
      ▼
IQ Samples
      │
      ▼
Improved CNN
      │
      ▼
Modulation Prediction
      │
      ▼
Evaluation / Visualization
```

This software-based architecture is the foundation for later hardware integration.

---

## 17. Final System Workflow

The complete project workflow is:

```text
1. Define Problem
        ↓
2. Collect Dataset
        ↓
3. Analyze Dataset
        ↓
4. Preprocess IQ Signals
        ↓
5. Prepare Features / Inputs
        ↓
6. Develop CNN
        ↓
7. Train CNN
        ↓
8. Evaluate CNN
        ↓
9. Select Final Model
        ↓
10. Build Prediction System
        ↓
11. Integrate Visualization
        ↓
12. Build Software Dashboard
        ↓
13. Test Complete System
        ↓
14. Optional RTL-SDR Integration
```

---

## 18. Current System Status

The following stages have been completed:

```text
Dataset Analysis              ✅
Data Preprocessing            ✅
Signal Visualization          ✅
Original CNN Development      ✅
Original CNN Training         ✅
Original Model Evaluation     ✅
Improved CNN Development      ✅
Improved CNN Training         ✅
Improved Model Evaluation     ✅
```

The current project is moving from the experimental notebook stage toward reusable software modules and the final prediction system.

---

## 19. Repository Relationship

The system architecture maps to the GitHub repository as follows:

```text
data/
    ↓
Dataset and processed data

features/
    ↓
Preprocessing and feature preparation

models/
    ↓
CNN architecture

saved_models/
    ↓
Trained CNN model

evaluation/
    ↓
Model performance and results

visualization/
    ↓
RF signal visualization modules

testing/
    ↓
Prediction and testing modules

notebooks/
    ↓
Development and experimentation

docs/
    ↓
Project documentation

app/
    ↓
Final software dashboard
```

---

## 20. Future Extension

The system can be extended with:

- RTL-SDR live RF signal acquisition
- Real-time modulation classification
- Real-time spectrum monitoring
- Signal recording
- Automatic signal logging
- More modulation classes
- Improved deep learning architectures
- SNR estimation
- Signal quality estimation
- Real-time alerts
- Advanced RF visualization

These features can be added after the core software classification system is stable.

---

## 21. Summary

The system architecture combines RF signal processing, I/Q data analysis, deep learning, signal visualization, and software-based classification.

The core architecture is:

```text
RF Signal
    ↓
I/Q Data
    ↓
Preprocessing
    ↓
CNN Feature Extraction
    ↓
Modulation Classification
    ↓
Confidence
    ↓
Visualization
    ↓
Software Dashboard
```

The current software implementation is based on the RadioML 2016.10a dataset, while RTL-SDR integration is planned as an optional hardware extension.

The architecture is designed so that the same trained AI model can eventually receive appropriately prepared IQ samples from either a dataset or a live RF receiver.
