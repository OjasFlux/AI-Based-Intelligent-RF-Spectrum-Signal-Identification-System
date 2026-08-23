# Prediction and Inference

## AI Based Intelligent RF Spectrum Signal Identification System

## 1. Introduction

The prediction stage is responsible for using the trained CNN model to identify the modulation type of an unseen RF signal.

During training, the CNN learns modulation characteristics from the RadioML dataset.

During prediction, the trained model is loaded and used without updating its weights.

The basic inference workflow is:

```text
Unseen IQ Signal
       ↓
Input Validation
       ↓
Preprocessing
       ↓
CNN Input Preparation
       ↓
Load Trained Model
       ↓
Model Prediction
       ↓
Class Probabilities
       ↓
Highest Probability
       ↓
Modulation Type
       ↓
Prediction Confidence
```

---

## 2. Purpose of the Prediction System

The purpose of the prediction system is to automatically identify the modulation type of an input RF signal.

The system receives:

```text
I/Q Signal
```

and produces:

```text
Predicted Modulation
+
Prediction Confidence
```

For example:

```text
Input:
IQ Signal

Output:

Modulation: QPSK
Confidence: 94.7%
```

The actual prediction and confidence depend on the input signal and trained model.

---

## 3. Trained Model

The prediction system uses the trained improved CNN model.

The expected saved model is:

```text
saved_models/
└── best_improved_cnn_classifier.keras
```

The trained model contains the learned parameters required for classification.

The prediction system does not retrain the model.

The workflow is:

```text
Saved Model
     ↓
Load Model
     ↓
Receive IQ Signal
     ↓
Preprocess Signal
     ↓
Predict
```

---

## 4. Input Signal

The prediction input must have the same basic representation used during model training.

The improved CNN expects:

```text
(128, 2)
```

for one signal.

The two channels are:

```text
Channel 0 → I
Channel 1 → Q
```

The input therefore represents:

```text
128 signal samples
        ×
2 channels
        ↓
I and Q
```

---

## 5. Input Shape Requirement

The trained model expects a batch dimension during prediction.

For one signal, the model input becomes:

```text
(1, 128, 2)
```

where:

```text
1   → Number of signals
128 → Signal sequence length
2   → I/Q channels
```

For multiple signals:

```text
(N, 128, 2)
```

where:

```text
N → Number of signals
```

---

## 6. Prediction Pipeline

The complete prediction pipeline is:

```text
Input IQ Signal
       │
       ▼
Check Signal Shape
       │
       ▼
Apply Same Preprocessing
       │
       ▼
Convert to CNN Input Format
       │
       ▼
Load Trained CNN
       │
       ▼
Generate Prediction
       │
       ▼
Obtain Class Probabilities
       │
       ▼
Find Highest Probability
       │
       ▼
Convert Class Index
       │
       ▼
Modulation Name
       │
       ▼
Display Confidence
```

---

## 7. Preprocessing During Prediction

The same preprocessing used during training must be applied to the prediction input.

This is important because the model was trained using a specific data representation.

The prediction process should therefore use:

```text
Training Preprocessing
        =
Prediction Preprocessing
```

The general process is:

```text
Raw IQ Signal
      ↓
Same Normalization
      ↓
Same Input Arrangement
      ↓
(128, 2)
      ↓
CNN
```

Using different preprocessing during prediction can significantly affect model performance.

---

## 8. Input Validation

Before prediction, the input signal should be checked.

Important checks include:

```text
1. IQ data exists
2. Signal contains I and Q channels
3. Correct number of samples
4. Correct numerical data type
5. No unexpected missing values
6. Correct input shape
```

The expected signal structure is:

```text
(128, 2)
```

before adding the batch dimension.

---

## 9. Input Reshaping

If a single signal has the shape:

```text
(128, 2)
```

a batch dimension is added:

```text
(1, 128, 2)
```

Conceptually:

```text
Single Signal
    ↓
(128, 2)
    ↓
Add Batch Dimension
    ↓
(1, 128, 2)
    ↓
CNN
```

---

## 10. Loading the Model

The trained model can be loaded using TensorFlow/Keras.

Conceptually:

```python
import tensorflow as tf

model = tf.keras.models.load_model(
    "saved_models/best_improved_cnn_classifier.keras"
)
```

The loaded model can then be used for inference.

```text
Saved Model
     ↓
TensorFlow/Keras
     ↓
Loaded CNN
```

---

## 11. Generating Predictions

After preparing the input, the model generates class probabilities.

Conceptually:

```python
probabilities = model.predict(signal)
```

The output contains probabilities corresponding to the 11 modulation classes.

For example:

```text
8PSK    → 0.02
AM-DSB  → 0.01
AM-SSB  → 0.01
BPSK    → 0.04
CPFSK   → 0.02
GFSK    → 0.01
PAM4    → 0.01
QAM16   → 0.03
QAM64   → 0.01
QPSK    → 0.83
WBFM    → 0.01
```

The values above are only an example of the output format.

The actual values depend on the input signal.

---

## 12. Selecting the Predicted Class

The class with the highest probability is selected.

Conceptually:

```text
Class Probabilities
       ↓
Find Maximum Probability
       ↓
Class Index
       ↓
Modulation Name
```

For example:

```text
QPSK → 0.83
```

is the highest probability.

Therefore:

```text
Predicted Modulation:
QPSK
```

---

## 13. Modulation Class Mapping

The numerical model output must be converted into a readable modulation name.

The project uses the class mapping stored in:

```text
data/processed/modulation_classes.npy
```

The mapping is conceptually:

```text
Class Index
     ↓
Modulation Name
```

For example:

```text
Predicted Class Index
        ↓
Class Mapping
        ↓
QPSK
```

The exact mapping used during prediction must be the same mapping used during model training.

---

## 14. Prediction Confidence

The highest model probability can be displayed as the prediction confidence.

For example:

```text
Predicted Modulation:
QPSK

Confidence:
83%
```

The confidence value is obtained from the model's output probability for the predicted class.

The value can be converted to percentage form:

```text
Confidence (%) =
Maximum Probability × 100
```

---

## 15. Important Confidence Note

Prediction confidence represents the model's output probability.

It should not automatically be interpreted as a guaranteed probability that the classification is correct in the real world.

For example:

```text
Prediction:
QPSK

Model Confidence:
95%
```

means that the model assigned approximately 95% probability to the QPSK class for that input.

It does not guarantee that the physical signal is actually QPSK.

---

## 16. Prediction Using Test Data

During software development, the prediction system can first be tested using samples from:

```text
data/processed/X_test.npy
```

The corresponding actual labels are stored in:

```text
data/processed/y_test.npy
```

This allows individual predictions to be compared with known labels.

The workflow is:

```text
X_test
  ↓
Select One Signal
  ↓
Prediction
  ↓
Predicted Modulation
  ↓
Compare With y_test
  ↓
Correct / Incorrect
```

---

## 17. Example Test Prediction

For one test signal:

```text
Actual Modulation:
QPSK

Model Prediction:
QPSK

Confidence:
92%
```

The prediction is correct because:

```text
Actual = Predicted
```

Another example:

```text
Actual Modulation:
QPSK

Model Prediction:
8PSK

Confidence:
61%
```

This represents a classification error.

---

## 18. Prediction and Confusion Matrix

Individual predictions contribute to the overall confusion matrix.

The relationship is:

```text
Individual Predictions
        ↓
Actual vs Predicted
        ↓
All Test Samples
        ↓
Confusion Matrix
```

Therefore, the prediction module and evaluation module are closely related but serve different purposes.

### Prediction

Focuses on:

```text
One or more input signals
        ↓
Predicted modulation
```

### Evaluation

Focuses on:

```text
Large test dataset
        ↓
Overall model performance
```

---

## 19. Single Signal Prediction

The final software should support prediction of an individual signal.

The workflow is:

```text
One IQ Signal
      ↓
Preprocessing
      ↓
Shape (128, 2)
      ↓
Add Batch Dimension
      ↓
Shape (1, 128, 2)
      ↓
CNN
      ↓
Prediction
      ↓
Modulation + Confidence
```

---

## 20. Batch Prediction

The system can also predict multiple signals at once.

For example:

```text
100 IQ Signals
      ↓
Shape:
(100, 128, 2)
      ↓
CNN
      ↓
100 Predictions
```

Batch prediction is useful for:

- Test dataset evaluation
- Performance measurement
- Faster processing
- SNR-based evaluation

---

## 21. Prediction From a Saved Model

The final prediction system should not require model retraining.

The workflow is:

```text
Start Application
       ↓
Load Saved CNN
       ↓
Wait for Input
       ↓
Receive IQ Signal
       ↓
Preprocess
       ↓
Predict
       ↓
Display Result
```

This makes the trained AI model reusable.

---

## 22. Prediction Software Module

The reusable prediction implementation is planned under:

```text
testing/
├── test_model.py
└── predict.py
```

The main prediction functionality will be implemented in:

```text
testing/predict.py
```

The module can contain functions such as:

```python
load_model()
load_class_names()
preprocess_input()
predict_modulation()
get_prediction_confidence()
```

The exact implementation will be finalized during software integration.

---

## 23. Testing Module

The file:

```text
testing/test_model.py
```

can be used to verify that:

- The model loads correctly
- Input shape is valid
- Prediction executes successfully
- Output contains the expected number of classes
- Class mapping works correctly
- Prediction output has valid probability values

---

## 24. Prediction Output Format

A simple prediction output can be:

```text
====================================
RF SIGNAL CLASSIFICATION RESULT
====================================

Predicted Modulation : QPSK
Confidence           : 94.72%

====================================
```

The actual confidence depends on the input signal.

---

## 25. Extended Prediction Output

The final dashboard can display additional information:

```text
-----------------------------------------
RF SIGNAL CLASSIFICATION
-----------------------------------------

Modulation:
QPSK

Confidence:
94.72%

Signal Samples:
128

I/Q Channels:
2

SNR:
Available when provided

-----------------------------------------
```

This can later be combined with signal visualizations.

---

## 26. Prediction With Visualization

The final software can connect prediction with visualization.

The workflow is:

```text
IQ Signal
    │
    ├──────────────► CNN
    │                  │
    │                  ▼
    │            Modulation
    │                  +
    │             Confidence
    │
    ├──────────────► Time Domain
    │
    ├──────────────► FFT
    │
    ├──────────────► Constellation
    │
    └──────────────► Spectrogram
```

This provides both:

```text
AI Classification
+
RF Signal Analysis
```

---

## 27. Prediction Dashboard

The eventual software dashboard can display:

```text
┌─────────────────────────────────────────────┐
│ AI BASED RF SIGNAL IDENTIFICATION SYSTEM   │
├─────────────────────────────────────────────┤
│                                             │
│ Predicted Modulation: QPSK                 │
│ Confidence:            94.72%              │
│                                             │
├───────────────────┬─────────────────────────┤
│ I/Q Signal        │ FFT Spectrum            │
│                   │                         │
├───────────────────┼─────────────────────────┤
│ Constellation     │ Spectrogram             │
│                   │                         │
└───────────────────┴─────────────────────────┘
```

The exact dashboard design can be finalized during the application development stage.

---

## 28. Prediction Error Handling

The prediction module should handle invalid inputs.

Examples include:

```text
Dataset file missing
Model file missing
Incorrect input shape
Invalid numerical values
Missing I/Q channel
Incorrect sample length
```

The system should display a clear error rather than producing an invalid prediction.

For example:

```text
Error:
Expected input shape (128, 2)
Received shape (64, 2)
```

---

## 29. Prediction From Future RTL-SDR Input

The prediction system can later receive IQ samples from an RTL-SDR.

The planned workflow is:

```text
Antenna
   ↓
RTL-SDR
   ↓
RF Signal
   ↓
IQ Samples
   ↓
Signal Buffer
   ↓
Extract Required Samples
   ↓
Preprocessing
   ↓
(128, 2)
   ↓
Trained CNN
   ↓
Modulation Prediction
   ↓
Confidence
```

The live signal pipeline must ensure that the data representation is compatible with the training data.

---

## 30. Live Prediction Considerations

When live RF input is added, several parameters must be handled correctly:

- Center frequency
- Sample rate
- Signal bandwidth
- Gain
- IQ format
- Number of samples
- Signal segmentation
- Normalization
- Noise conditions

The model cannot simply receive arbitrary raw RF data.

The live data must first be converted into an appropriate IQ representation.

---

## 31. Dataset Prediction vs Live Prediction

The two prediction sources can be represented as:

### Software Prediction

```text
RadioML Dataset
      ↓
Processed IQ
      ↓
CNN
      ↓
Prediction
```

### Live Hardware Prediction

```text
RTL-SDR
      ↓
Live RF
      ↓
IQ Samples
      ↓
Preprocessing
      ↓
CNN
      ↓
Prediction
```

The AI classification stage can remain the same if both inputs are correctly prepared.

---

## 32. Prediction Latency

For the final real-time system, prediction latency can be measured.

Important values include:

```text
Signal Acquisition Time
Preprocessing Time
CNN Inference Time
Visualization Time
Total Prediction Time
```

The total processing time can be represented as:

```text
Total Time =
Acquisition
+
Preprocessing
+
Inference
+
Output
```

Real-time performance will depend on the computer, model size, input processing, and future RTL-SDR configuration.

---

## 33. Prediction Reliability

Prediction reliability depends on several factors:

```text
Signal Quality
      +
Training Data
      +
Preprocessing
      +
Model Performance
      +
Modulation Class
      +
SNR
```

The current evaluation shows that SNR has a strong influence on classification performance.

Therefore, predictions at low SNR should be interpreted carefully.

---

## 34. Prediction Pipeline in Final Software

The final software prediction pipeline is:

```text
                    INPUT
                      │
                      ▼
                IQ Signal
                      │
                      ▼
              Input Validation
                      │
                      ▼
                Preprocessing
                      │
                      ▼
                Shape (128,2)
                      │
                      ▼
               Load CNN Model
                      │
                      ▼
                 Prediction
                      │
                      ▼
             Class Probabilities
                      │
                      ▼
             Highest Probability
                      │
                      ▼
              Modulation Name
                      │
                      ▼
              Confidence Score
                      │
                      ▼
                 Visualization
                      │
                      ▼
                   OUTPUT
```

---

## 35. Current Prediction Status

The project has completed the model training and evaluation stages required before building the reusable inference system.

Current status:

```text
Trained CNN Model             ✅
Saved Model                   ✅
Test Dataset                  ✅
Model Evaluation              ✅
Class Mapping                 ✅
Prediction Logic              ⏳
Reusable predict.py           ⏳
Prediction Testing            ⏳
Dashboard Integration         ⏳
RTL-SDR Live Prediction       ⏳
```

The next implementation step is to convert the prediction logic from the notebook environment into:

```text
testing/predict.py
```

---

## 36. Prediction Summary

The prediction system uses the trained improved CNN to identify the modulation type of unseen I/Q signals.

The complete process is:

```text
Unseen IQ Signal
       ↓
Preprocessing
       ↓
Input Shape (128, 2)
       ↓
Trained Improved CNN
       ↓
11 Class Probabilities
       ↓
Highest Probability
       ↓
Modulation Type
       +
Confidence
```

The same prediction architecture can later be used for:

```text
RadioML Test Signals
        ↓
Software Demonstration
        ↓
Final Dashboard
        ↓
Optional RTL-SDR Live Signals
```

The prediction stage therefore forms the bridge between the trained AI model and the final user-facing RF signal identification system.
