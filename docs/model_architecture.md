# Model Architecture

## AI Based Intelligent RF Spectrum Signal Identification System

## 1. Introduction

The project uses a Convolutional Neural Network (CNN) based deep learning approach for automatic modulation classification.

The purpose of the model is to learn characteristics from RF I/Q signal samples and classify each signal into one of the supported modulation classes.

Two CNN approaches were developed during the project:

1. Original CNN — baseline model
2. Improved 1D Residual CNN — improved model

The improved CNN is currently selected as the final model candidate because it provides better test performance than the baseline model.

---

## 2. Model Objective

The objective of the AI model is:

```text
Input:
I/Q RF Signal

        ↓

CNN Feature Learning

        ↓

Classification

        ↓

Output:
Modulation Type
+
Prediction Probability
```

The model currently classifies the signal into 11 modulation classes.

---

## 3. Supported Modulation Classes

The output layer represents the following classes:

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

The number of output classes is therefore:

```text
11
```

---

## 4. Input Data

The original RadioML I/Q signal representation is:

```text
(2, 128)
```

where:

```text
2   → I and Q channels
128 → Signal samples
```

For the improved 1D CNN, the input is rearranged to:

```text
(128, 2)
```

where:

```text
128 → Sequential signal samples
2   → I and Q channels
```

Therefore, the model receives:

```text
128 × 2
```

input values for each signal sample.

---

## 5. Why 1D CNN Is Used

RF I/Q signals contain sequential information.

The signal samples occur in a specific order over time.

Therefore, the improved model treats the signal as a sequence:

```text
Sample 1
Sample 2
Sample 3
...
Sample 128
```

with I and Q represented as two channels.

A 1D CNN is suitable because its convolutional filters can learn local patterns along the signal sequence.

The model therefore follows:

```text
I/Q Sequence
     ↓
Conv1D
     ↓
Learned Signal Features
     ↓
Deeper Feature Extraction
     ↓
Classification
```

---

# 6. Original CNN Model

The first CNN was developed as a baseline model.

The purpose of the baseline model was to:

- Establish an initial performance
- Verify the complete training pipeline
- Provide a reference for later improvements
- Identify difficult modulation classes

The original model achieved approximately:

```text
Test Accuracy:
56.43%
```

This model was then used as the baseline for comparison.

---

## 7. Original Model Role

The baseline architecture established that the RF I/Q data could be classified using a CNN.

The development workflow was:

```text
I/Q Data
   ↓
Preprocessing
   ↓
Original CNN
   ↓
Training
   ↓
Testing
   ↓
56.43% Test Accuracy
```

The baseline results were then analyzed using:

- Confusion matrix
- Classification report
- Precision
- Recall
- F1-score
- Accuracy versus SNR

---

# 8. Improved CNN

After evaluating the baseline CNN, an improved 1D CNN architecture was developed.

The improved model uses:

- Conv1D layers
- Batch normalization
- ReLU activation
- Residual connections
- Max pooling
- Global average pooling
- Dense layers
- Dropout
- Softmax output

The overall architecture is:

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
ReLU
   │
   ▼
Residual Block 1
   │
   ▼
Max Pooling
   │
   ▼
Residual Block 2
   │
   ▼
Max Pooling
   │
   ▼
Residual Block 3
   │
   ▼
Max Pooling
   │
   ▼
Conv1D
   │
   ▼
Batch Normalization
   │
   ▼
Global Average Pooling
   │
   ▼
Dense Layer
   │
   ▼
Dropout
   │
   ▼
Dense Layer
   │
   ▼
Dropout
   │
   ▼
Softmax
   │
   ▼
11 Modulation Classes
```

---

# 9. Initial Convolution Layer

The improved model begins with a `Conv1D` layer.

The initial layer uses:

```text
Filters:
64

Kernel Size:
7

Padding:
same
```

The purpose of the initial convolution is to extract low-level patterns from the I/Q sequence.

The processing is:

```text
I/Q Input
   ↓
Conv1D
   ↓
Low-Level Feature Maps
```

---

# 10. Batch Normalization

Batch normalization is applied after the initial convolution.

The structure is:

```text
Conv1D
   ↓
Batch Normalization
   ↓
ReLU
```

Batch normalization helps stabilize the training process and improves the flow of activations through the network.

---

# 11. ReLU Activation

The model uses the ReLU activation function in the feature extraction layers.

ReLU can be represented as:

```text
ReLU(x) = max(0, x)
```

It introduces non-linearity into the network and allows the CNN to learn more complex relationships in the I/Q signal.

---

# 12. Residual Blocks

The improved CNN contains residual blocks.

A residual block allows the original input information to bypass convolutional transformations and be combined with the processed features.

Conceptually:

```text
                 ┌──────────────────────┐
                 │                      │
                 │      Shortcut        │
                 │                      │
Input ───────────┼───────────────┐      │
                 │               │      │
                 ▼               │      │
              Conv1D             │      │
                 │               │      │
                 ▼               │      │
          Batch Normalization   │      │
                 │               │      │
                 ▼               │      │
               ReLU             │      │
                 │               │      │
                 ▼               │      │
              Conv1D             │      │
                 │               │      │
                 ▼               │      │
          Batch Normalization   │      │
                 │               │      │
                 └─────── Add ◄─┘
                         │
                         ▼
                       ReLU
```

Residual connections help preserve information and support deeper feature learning.

---

# 13. Residual Block 1

The first residual block operates with:

```text
Filters:
64

Kernel Size:
5
```

It extracts initial higher-level signal characteristics.

After the block:

```text
Residual Block 1
       ↓
Max Pooling
```

Pooling reduces the temporal feature representation.

---

# 14. Residual Block 2

The second residual block increases the feature representation:

```text
Filters:
128

Kernel Size:
5
```

This allows the network to learn more complex signal characteristics.

The structure is:

```text
Residual Block 2
       ↓
Max Pooling
```

---

# 15. Residual Block 3

The third residual block uses:

```text
Filters:
256

Kernel Size:
3
```

This block extracts deeper and more complex features.

The structure is:

```text
Residual Block 3
       ↓
Max Pooling
```

---

# 16. Feature Refinement Layer

After the residual blocks, another convolutional layer is used:

```text
Filters:
256

Kernel Size:
3

Activation:
ReLU
```

This layer further refines the learned feature representation.

The output is then normalized using batch normalization.

---

# 17. Global Average Pooling

The feature maps are converted into a compact representation using:

```text
GlobalAveragePooling1D
```

The process is:

```text
Deep Feature Maps
       ↓
Global Average Pooling
       ↓
Feature Vector
```

This reduces the dimensionality before the dense classification layers.

---

# 18. Dense Classification Layers

After feature extraction, the model uses fully connected layers.

The first dense layer contains:

```text
256 neurons
```

followed by:

```text
Dropout = 0.40
```

The second dense layer contains:

```text
128 neurons
```

followed by:

```text
Dropout = 0.30
```

The structure is:

```text
Feature Vector
     ↓
Dense 256
     ↓
Dropout 0.40
     ↓
Dense 128
     ↓
Dropout 0.30
     ↓
Output Layer
```

---

# 19. Dropout

Dropout is used to reduce overfitting.

During training, dropout temporarily removes a portion of neuron connections.

The improved model uses:

```text
Dropout 1 → 0.40
Dropout 2 → 0.30
```

This encourages the network to learn more general features rather than relying too heavily on individual neurons.

---

# 20. Output Layer

The final layer is a dense layer with:

```text
11 output neurons
```

The activation function is:

```text
Softmax
```

The output represents the predicted probability of each modulation class.

Conceptually:

```text
                    Softmax
                       │
       ┌───────────────┼───────────────┐
       ▼               ▼               ▼
     8PSK            BPSK            QPSK ...
       │               │               │
       └───────────────┼───────────────┘
                       ▼
                Highest Probability
                       │
                       ▼
              Predicted Modulation
```

---

# 21. Softmax Output

Softmax converts the model output into probability values.

For example, an output could conceptually look like:

```text
8PSK    → 0.03
AM-DSB  → 0.02
AM-SSB  → 0.01
BPSK    → 0.04
CPFSK   → 0.02
GFSK    → 0.03
PAM4    → 0.01
QAM16   → 0.02
QAM64   → 0.01
QPSK    → 0.81
WBFM    → 0.00
```

The highest probability corresponds to:

```text
QPSK
```

and the system can report the corresponding probability as the prediction confidence.

The exact probability depends on the input signal.

---

# 22. Complete Improved CNN Architecture

The improved CNN can be summarized as:

```text
Input
(128, 2)
   │
   ▼
Conv1D
64 filters
kernel = 7
   │
   ▼
Batch Normalization
   │
   ▼
ReLU
   │
   ▼
Residual Block
64 filters
kernel = 5
   │
   ▼
MaxPooling1D
   │
   ▼
Residual Block
128 filters
kernel = 5
   │
   ▼
MaxPooling1D
   │
   ▼
Residual Block
256 filters
kernel = 3
   │
   ▼
MaxPooling1D
   │
   ▼
Conv1D
256 filters
kernel = 3
   │
   ▼
Batch Normalization
   │
   ▼
GlobalAveragePooling1D
   │
   ▼
Dense
256
   │
   ▼
Dropout
0.40
   │
   ▼
Dense
128
   │
   ▼
Dropout
0.30
   │
   ▼
Dense
11
   │
   ▼
Softmax
   │
   ▼
Modulation Prediction
```

---

# 23. Model Training Configuration

The improved model is trained using:

| Parameter | Value |
|---|---|
| Optimizer | Adam |
| Learning Rate | 0.001 initially |
| Loss Function | Categorical Crossentropy |
| Output Activation | Softmax |
| Batch Size | 256 |
| Maximum Epochs | 60 |
| Early Stopping | Enabled |
| Model Checkpointing | Enabled |
| Learning Rate Reduction | Enabled |

The actual number of epochs can be lower than the maximum because early stopping can terminate training when validation performance stops improving.

---

# 24. Optimizer

The project uses the Adam optimizer.

Adam is used to update the model parameters during training.

The basic training loop is:

```text
Input Signal
     ↓
CNN
     ↓
Prediction
     ↓
Calculate Loss
     ↓
Adam Optimizer
     ↓
Update Weights
     ↓
Next Training Step
```

---

# 25. Loss Function

The model uses:

```text
Categorical Crossentropy
```

as its loss function.

The loss measures the difference between:

```text
Actual Modulation
        and
Predicted Class Probabilities
```

The training process attempts to minimize this loss.

---

# 26. Model Training Control

The improved model uses three important callbacks.

### Early Stopping

Stops training when validation performance stops improving for the configured patience period.

### Model Checkpoint

Saves the best model based on validation accuracy.

### Reduce Learning Rate

Reduces the learning rate when validation loss stops improving.

The training control flow is:

```text
Training
   ↓
Validation
   ↓
Improvement?
 ┌─┴──────────┐
Yes           No
 │             │
 ▼             ▼
Continue   Reduce LR /
           Early Stop
```

---

# 27. Model Performance

The baseline CNN achieved approximately:

```text
56.43% Test Accuracy
```

The improved CNN achieved:

```text
62.29% Test Accuracy
```

Therefore:

```text
Improvement =
62.29 - 56.43

= 5.86 percentage points
```

The improved architecture therefore provides better overall performance on the test dataset.

---

# 28. High-SNR Performance

The improved model was also evaluated according to SNR.

The measured performance was approximately:

```text
High SNR (>= 0 dB)
92.08%
```

while:

```text
Low SNR (< 0 dB)
32.39%
```

This shows that the model performs significantly better when the signal quality is higher.

---

# 29. Why the Improved Model Was Selected

The improved model was selected because:

1. It provides better test accuracy than the baseline CNN.
2. It is designed specifically for sequential I/Q signal processing.
3. It uses residual feature learning.
4. It provides strong high-SNR performance.
5. It produces class probabilities that can be used for confidence display.
6. It can be reused later for unseen IQ signal prediction.
7. It can potentially be connected to an RTL-SDR-based input pipeline.

The model is therefore the current final model candidate for the software implementation.

---

# 30. Saved Model

The best trained improved model is stored as:

```text
best_improved_cnn_classifier.keras
```

The project keeps trained model files separately from model architecture code.

The intended repository structure is:

```text
models/
├── cnn_model.py
└── improved_cnn.py

saved_models/
└── best_improved_cnn_classifier.keras
```

The distinction is:

```text
models/
    ↓
Model architecture and code

saved_models/
    ↓
Trained model
```

---

# 31. Model Loading

The trained model can be loaded later without retraining.

Conceptually:

```python
import tensorflow as tf

model = tf.keras.models.load_model(
    "best_improved_cnn_classifier.keras"
)
```

The loaded model can then be used for inference.

```text
Saved CNN
    ↓
Load Model
    ↓
Preprocessed IQ Signal
    ↓
Prediction
```

---

# 32. Prediction Output

The model produces a probability distribution across the 11 classes.

The prediction system can extract:

```text
Predicted Class
Prediction Confidence
```

For example:

```text
Predicted Modulation:
QPSK

Confidence:
94.7%
```

The exact output depends on the signal presented to the model.

---

# 33. Model Architecture in the Final Software

The final software will use the trained model as follows:

```text
Input IQ Signal
       ↓
Preprocessing
       ↓
Input Shape
(128, 2)
       ↓
Improved CNN
       ↓
Softmax
       ↓
11 Class Probabilities
       ↓
Highest Probability
       ↓
Modulation Type
+
Confidence
```

---

# 34. Future Live Signal Operation

For future RTL-SDR integration:

```text
RTL-SDR
   ↓
Live IQ Samples
   ↓
Signal Segmentation
   ↓
Preprocessing
   ↓
(128, 2)
   ↓
Improved CNN
   ↓
Modulation Classification
```

The live signal preprocessing must produce an input representation compatible with the training data.

---

# 35. Model Architecture Files

The model architecture will eventually be moved from the experimental notebooks into reusable Python modules.

The planned files are:

```text
models/
├── cnn_model.py
└── improved_cnn.py
```

The improved model implementation will contain the reusable architecture used for training and inference.

The development notebook remains available under:

```text
notebooks/07_improved_cnn_model.ipynb
```

The notebook documents the experimental model development process.

---

# 36. Model Development Workflow

The model development process followed:

```text
Preprocessed IQ Data
        ↓
Baseline CNN
        ↓
Train
        ↓
Evaluate
        ↓
56.43%
        ↓
Analyze Performance
        ↓
Improve Architecture
        ↓
Improved 1D Residual CNN
        ↓
Train
        ↓
Evaluate
        ↓
62.29%
        ↓
Select Improved Model
```

---

# 37. Model Architecture Status

The following stages are complete:

```text
Baseline CNN Design          ✅
Baseline Training            ✅
Baseline Evaluation          ✅
Improved CNN Design          ✅
Residual Blocks              ✅
Model Training               ✅
Model Evaluation             ✅
Model Comparison             ✅
Final Model Candidate        ✅
```

The next stage is to convert the validated model architecture into reusable project code.

---

# 38. Summary

The project uses an improved 1D residual CNN for automatic modulation classification from I/Q signal samples.

The model accepts:

```text
(128, 2)
```

I/Q input and performs automatic feature extraction using convolutional and residual layers.

The learned features are aggregated and passed through dense classification layers.

The final softmax layer produces probabilities for 11 modulation classes.

The improved model achieved:

```text
Overall Test Accuracy:
62.29%

High-SNR Accuracy:
92.08%
```

The improved model is therefore the current final model candidate for the software-based RF signal identification system.

The complete model flow is:

```text
I/Q Signal
    ↓
Conv1D
    ↓
Residual Feature Learning
    ↓
Pooling
    ↓
Deep Feature Extraction
    ↓
Global Average Pooling
    ↓
Dense Layers
    ↓
Softmax
    ↓
11 Modulation Classes
    ↓
Prediction + Confidence
```
