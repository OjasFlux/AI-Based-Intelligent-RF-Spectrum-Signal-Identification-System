# Model Training

## AI Based Intelligent RF Spectrum Signal Identification System

## 1. Introduction

Model training is the stage where the CNN learns the relationship between RF I/Q signal characteristics and their corresponding modulation classes.

The project follows two model development stages:

```text
Preprocessed Dataset
        ↓
Baseline CNN Training
        ↓
Baseline Evaluation
        ↓
Improved CNN Development
        ↓
Improved CNN Training
        ↓
Improved Model Evaluation
        ↓
Final Model Selection
```

The improved CNN is currently the final model candidate for the software-based system.

---

## 2. Training Objective

The objective of training is to teach the CNN to classify an input I/Q signal into one of the 11 supported modulation classes.

The training process is:

```text
I/Q Signal
    ↓
CNN
    ↓
Predicted Class Probabilities
    ↓
Compare With Actual Label
    ↓
Calculate Loss
    ↓
Update Model Weights
    ↓
Repeat
```

During training, the model gradually learns signal patterns that help distinguish different modulation types.

---

## 3. Training Dataset

The model is trained using the processed RadioML 2016.10a dataset.

The processed dataset is stored under:

```text
data/
└── processed/
```

The main training files are:

```text
X_train.npy
y_train.npy
```

where:

```text
X_train.npy → Training IQ signals
y_train.npy → Training modulation labels
```

The validation files are:

```text
X_val.npy
y_val.npy
```

The test files are:

```text
X_test.npy
y_test.npy
```

---

## 4. Training Data Flow

The training data flows through the following pipeline:

```text
RadioML 2016.10a
        ↓
Preprocessing
        ↓
Normalized IQ Data
        ↓
Train / Validation / Test Split
        ↓
Training Data
        ↓
CNN
        ↓
Predictions
        ↓
Loss Calculation
        ↓
Weight Update
```

---

## 5. Input Shape

The original IQ data is represented as:

```text
(samples, 2, 128)
```

For the improved CNN, the input is rearranged to:

```text
(samples, 128, 2)
```

The model therefore receives:

```text
128 → Signal sequence samples
2   → I and Q channels
```

The input shape of the improved CNN is:

```text
(128, 2)
```

---

## 6. Output Classes

The model has 11 output classes:

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

The final layer contains:

```text
11 neurons
```

with:

```text
Softmax activation
```

The output represents the predicted probability of each modulation class.

---

## 7. Baseline Model Training

The first CNN model was trained as a baseline.

The purpose of the baseline model was to:

- Verify the complete training pipeline
- Establish initial classification performance
- Identify difficult modulation classes
- Provide a reference for model improvement

The baseline CNN achieved approximately:

```text
Test Accuracy:
56.43%
```

This result was used as the reference point for the improved model.

---

## 8. Improved Model Training

After evaluating the baseline model, an improved 1D CNN with residual blocks was developed.

The improved architecture contains:

```text
Conv1D
     ↓
Batch Normalization
     ↓
ReLU
     ↓
Residual Blocks
     ↓
Max Pooling
     ↓
Deep Feature Extraction
     ↓
Global Average Pooling
     ↓
Dense Layers
     ↓
Dropout
     ↓
Softmax
```

The improved model is trained using the same prepared dataset while using a more advanced architecture for feature learning.

---

## 9. Training Configuration

The main training configuration is:

| Parameter | Value |
|---|---|
| Model | Improved 1D CNN |
| Input Shape | `(128, 2)` |
| Number of Classes | 11 |
| Optimizer | Adam |
| Initial Learning Rate | 0.001 |
| Loss Function | Categorical Crossentropy |
| Batch Size | 256 |
| Maximum Epochs | 60 |
| Early Stopping | Enabled |
| Model Checkpoint | Enabled |
| Learning Rate Reduction | Enabled |

The actual training duration may be less than the maximum number of epochs because early stopping can terminate training when validation performance stops improving.

---

## 10. Optimizer

The improved CNN uses the Adam optimizer.

Adam updates the trainable model parameters based on the calculated gradients.

The simplified training process is:

```text
Input Batch
    ↓
Forward Pass
    ↓
Prediction
    ↓
Loss Calculation
    ↓
Backpropagation
    ↓
Adam Optimizer
    ↓
Weight Update
```

This process is repeated for multiple batches and epochs.

---

## 11. Loss Function

The model uses:

```text
Categorical Crossentropy
```

as the classification loss function.

The loss measures the difference between:

```text
Actual Class
      and
Predicted Class Probabilities
```

The training process attempts to minimize this loss.

Conceptually:

```text
Actual Label
     +
Predicted Probability
     ↓
Categorical Crossentropy
     ↓
Loss Value
     ↓
Backpropagation
```

---

## 12. Batch Size

The improved model uses:

```text
Batch Size = 256
```

This means that approximately 256 training samples are processed together before the model weights are updated.

The basic process is:

```text
Training Dataset
      ↓
Batch 1 → 256 samples
      ↓
Weight Update

Batch 2 → 256 samples
      ↓
Weight Update

Batch 3 → 256 samples
      ↓
Weight Update

...
```

The final batch may contain fewer samples depending on the total training dataset size.

---

## 13. Epochs

The maximum training configuration uses:

```text
60 epochs
```

An epoch represents one complete pass through the training dataset.

Conceptually:

```text
Epoch 1
   ↓
Complete Training Dataset
   ↓
Epoch 2
   ↓
Complete Training Dataset
   ↓
...
   ↓
Epoch 60
```

The model may stop before reaching 60 epochs if early stopping is triggered.

---

## 14. Validation During Training

The validation dataset is used to monitor model performance during training.

The training process therefore uses:

```text
Training Data
      ↓
Update Weights

Validation Data
      ↓
Measure Generalization
```

The validation data is not directly used to update the model weights.

This helps identify whether the model is learning useful general features or beginning to overfit the training data.

---

## 15. Early Stopping

Early stopping is used to prevent unnecessary training.

The basic concept is:

```text
Train Model
     ↓
Check Validation Performance
     ↓
Improving?
   ┌───┴───┐
  Yes      No
   │        │
   ▼        ▼
Continue  Wait
Training    │
            ▼
     No Improvement
            │
            ▼
       Stop Training
```

Early stopping helps:

- Reduce unnecessary computation
- Reduce overfitting
- Preserve the best validation performance

---

## 16. Model Checkpointing

Model checkpointing is used to save the best-performing model during training.

The purpose is to ensure that the best model is retained even if later epochs produce worse validation performance.

The saved model is:

```text
best_improved_cnn_classifier.keras
```

The general workflow is:

```text
Training
   ↓
Validation Accuracy
   ↓
Better Than Previous Best?
   ├── Yes → Save Model
   └── No  → Continue
```

---

## 17. Learning Rate Reduction

A learning-rate reduction mechanism is used when validation performance stops improving.

The concept is:

```text
Training
   ↓
Validation Performance
   ↓
Plateau Detected
   ↓
Reduce Learning Rate
   ↓
Continue Training
```

Reducing the learning rate can allow the model to make smaller parameter updates when it approaches a better solution.

---

## 18. Forward Pass

During the forward pass, the input signal moves through the CNN.

```text
I/Q Input
   ↓
Conv1D
   ↓
Residual Blocks
   ↓
Pooling
   ↓
Feature Extraction
   ↓
Global Average Pooling
   ↓
Dense Layers
   ↓
Softmax
   ↓
Class Probabilities
```

The model produces a probability distribution across all 11 modulation classes.

---

## 19. Loss Calculation

The predicted probabilities are compared with the actual class label.

For example:

```text
Actual:
QPSK

Predicted:
8PSK    → 0.02
AM-DSB  → 0.01
...
QPSK    → 0.91
...
WBFM    → 0.01
```

The difference between the actual class and predicted distribution contributes to the training loss.

The model then uses this loss to update its weights.

---

## 20. Backpropagation

After calculating the loss, gradients are calculated through backpropagation.

The simplified process is:

```text
Loss
 ↓
Calculate Gradients
 ↓
Backpropagation
 ↓
Adam Optimizer
 ↓
Update Weights
```

This allows the model to gradually improve its predictions.

---

## 21. Training Loop

The complete training loop can be represented as:

```text
                Training Dataset
                       │
                       ▼
                 Select Batch
                       │
                       ▼
                  CNN Forward
                       │
                       ▼
                   Prediction
                       │
                       ▼
                 Loss Function
                       │
                       ▼
                Backpropagation
                       │
                       ▼
                Adam Optimizer
                       │
                       ▼
                 Update Weights
                       │
                       ▼
                  Next Batch
                       │
                       ▼
                 Next Epoch
```

This process continues until the training reaches the maximum number of epochs or early stopping terminates training.

---

## 22. Training and Validation Curves

Training history can be used to generate:

```text
Training Accuracy
Validation Accuracy
Training Loss
Validation Loss
```

These curves help analyze model learning.

A typical visualization contains:

```text
Accuracy
  │
  │       Training
  │      /
  │     /
  │    /     Validation
  │   /      /
  │  /      /
  └──────────────────► Epoch
```

and:

```text
Loss
  │\
  │ \
  │  \     Training
  │   \
  │    \________
  │
  │       Validation
  │      /
  │     /
  └──────────────────► Epoch
```

The actual curves depend on the training run.

---

## 23. Detecting Overfitting

Training and validation curves can help identify overfitting.

A possible overfitting pattern is:

```text
Training Accuracy
       ↑
       │
       │       ─────────
       │      /
       │     /
       │____/
       
Validation Accuracy
       ↑
       │    ─────
       │   /
       │  /
       │_/________
```

If training performance continues improving while validation performance stops improving or decreases, the model may be overfitting.

Early stopping and dropout help reduce this risk.

---

## 24. Training the Improved CNN

The improved CNN training workflow is:

```text
Processed Dataset
       │
       ▼
Load X_train
Load y_train
       │
       ▼
Prepare CNN Input
       │
       ▼
Build Improved CNN
       │
       ▼
Compile Model
       │
       ▼
Train Model
       │
       ├──────────────► Validation Dataset
       │                       │
       │                       ▼
       │                Validation Metrics
       │
       ▼
Save Best Model
       │
       ▼
Evaluate on Test Data
```

---

## 25. Model Compilation

Before training, the CNN is compiled using:

```text
Optimizer:
Adam

Loss:
Categorical Crossentropy

Metrics:
Accuracy
```

Conceptually:

```python
model.compile(
    optimizer="adam",
    loss="categorical_crossentropy",
    metrics=["accuracy"]
)
```

The exact implementation is maintained in the project training code.

---

## 26. Training Output

During training, important information can include:

```text
Epoch
Training Loss
Training Accuracy
Validation Loss
Validation Accuracy
Learning Rate
```

This information is stored in the training history and can later be used for visualization.

---

## 27. Saved Model

The best improved model is stored as:

```text
best_improved_cnn_classifier.keras
```

The intended project structure is:

```text
saved_models/
└── best_improved_cnn_classifier.keras
```

The model can later be loaded for prediction without repeating the training process.

---

## 28. Model Comparison

The training process resulted in two main model versions.

| Model | Test Accuracy |
|---|---:|
| Original CNN | 56.43% |
| Improved CNN | 62.29% |

The improved model provides:

```text
62.29% - 56.43%
= 5.86 percentage-point improvement
```

Therefore, the improved CNN is selected as the current final model candidate.

---

## 29. High-SNR Training Result

The improved model was evaluated according to SNR.

The model achieved approximately:

```text
High SNR (>= 0 dB):
92.08%
```

The low-SNR performance was approximately:

```text
Low SNR (< 0 dB):
32.39%
```

This indicates that the model performs substantially better when the received signal has a higher signal-to-noise ratio.

---

## 30. Why SNR Matters During Training

The training dataset contains signals with different SNR levels.

This allows the model to encounter both relatively clean and noisy signal conditions.

Conceptually:

```text
High SNR
   ↓
Clearer Signal Characteristics
   ↓
Easier Classification

Low SNR
   ↓
More Noise
   ↓
Hidden Signal Characteristics
   ↓
More Difficult Classification
```

SNR-based analysis is therefore an important part of model evaluation.

---

## 31. Reproducible Training Workflow

To reproduce the model training process:

### Step 1

Ensure the processed dataset exists:

```text
data/processed/
```

### Step 2

Verify the following files:

```text
X_train.npy
X_val.npy
X_test.npy

y_train.npy
y_val.npy
y_test.npy
```

### Step 3

Open the improved CNN development notebook:

```text
notebooks/07_improved_cnn_model.ipynb
```

### Step 4

Load the processed data.

### Step 5

Prepare the CNN input shape:

```text
(samples, 128, 2)
```

### Step 6

Build the improved CNN.

### Step 7

Compile the model.

### Step 8

Train using the training dataset.

### Step 9

Monitor validation performance.

### Step 10

Save the best-performing model.

### Step 11

Evaluate the saved model using the test dataset.

---

## 32. Training Notebook

The improved CNN training experiment is documented in:

```text
notebooks/07_improved_cnn_model.ipynb
```

The notebook is useful for:

- Experimentation
- Training visualization
- Model development
- Hyperparameter testing
- Reproducing the development process

The final reusable training implementation will later be moved into Python project modules.

---

## 33. Planned Training Module

The final project can contain a reusable training script such as:

```text
training/
└── train_model.py
```

If a separate `training/` folder is added later, it can contain the final training pipeline.

A reusable training script can perform:

```text
Load Processed Data
        ↓
Build Model
        ↓
Compile Model
        ↓
Train Model
        ↓
Validate Model
        ↓
Save Best Model
        ↓
Save Training History
```

This will allow model training without relying on the Jupyter notebook.

---

## 34. Training Reproducibility

For reproducible experiments, the project should maintain consistent:

- Dataset
- Preprocessing
- Input shape
- Model architecture
- Training configuration
- Random seed where applicable
- Validation procedure
- Test procedure

The same preprocessing used during training must also be used during future inference.

---

## 35. Training and Final Prediction

Training and prediction are separate stages.

### Training

```text
Large Training Dataset
        ↓
CNN
        ↓
Learn Model Parameters
        ↓
Save Trained Model
```

### Prediction

```text
New IQ Signal
        ↓
Same Preprocessing
        ↓
Saved CNN
        ↓
Prediction
        ↓
Modulation Type
```

The trained model should not need to be retrained for every new signal.

---

## 36. Training Limitations

The current model is trained using the RadioML 2016.10a dataset.

Therefore, its performance depends on how closely future input signals match the characteristics of the training data.

Important factors include:

- Signal format
- Sampling characteristics
- SNR
- Modulation type
- Frequency representation
- Noise characteristics
- Preprocessing

Real-world RF signals may contain additional impairments that are not fully represented by the training dataset.

This is an important consideration for future RTL-SDR integration.

---

## 37. Future Training Improvements

Possible improvements include:

- More training data
- Additional modulation classes
- Data augmentation
- Better noise modeling
- More advanced CNN architectures
- CNN-LSTM architectures
- Transformer-based signal models
- Hyperparameter optimization
- Improved low-SNR classification
- Real-world RF data fine-tuning

These improvements can be considered after the current software pipeline is stable.

---

## 38. Current Training Status

The training stages completed so far are:

```text
Training Dataset Preparation       ✅
Baseline CNN Training              ✅
Baseline Model Evaluation          ✅
Improved CNN Training              ✅
Validation During Training         ✅
Model Checkpointing                ✅
Early Stopping                     ✅
Learning Rate Reduction            ✅
Best Model Selection               ✅
Test Evaluation                    ✅
```

---

## 39. Training Summary

The model training process converts the prepared I/Q dataset into a trained deep learning classifier.

The complete training workflow is:

```text
Processed IQ Data
       ↓
Input Preparation
       ↓
Improved CNN
       ↓
Forward Pass
       ↓
Loss Calculation
       ↓
Backpropagation
       ↓
Adam Optimization
       ↓
Validation
       ↓
Best Model Selection
       ↓
Saved CNN
       ↓
Test Evaluation
```

The improved CNN achieved approximately:

```text
Overall Test Accuracy:
62.29%

High-SNR Accuracy:
92.08%
```

The trained model is now ready for the next stage:

```text
Model
  ↓
Evaluation
  ↓
Prediction
  ↓
Software Integration
```
