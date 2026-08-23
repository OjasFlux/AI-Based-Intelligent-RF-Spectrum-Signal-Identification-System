# Models

The `models/` directory contains the machine-learning architectures used for RF modulation classification.

The project contains two CNN approaches:

```text
Baseline CNN
     ↓
Reference Model

Improved CNN
     ↓
Enhanced Classification Model
```

The baseline model provides a reference for measuring the improvement achieved by the improved architecture.

---

# 1. Directory Structure

```text
models/
├── __init__.py
├── cnn_model.py
├── improved_cnn.py
└── README.md
```

---

# 2. Model Development Strategy

The project follows a two-stage model-development approach:

```text
RadioML Dataset
       ↓
Baseline CNN
       ↓
Baseline Evaluation
       ↓
Improved CNN
       ↓
Improved Evaluation
       ↓
Final Model Selection
```

This allows the project to demonstrate measurable improvement rather than presenting only a single model.

---

# 3. Baseline CNN

The baseline model is implemented in:

```text
models/cnn_model.py
```

The architecture originated from:

```text
04_cnn_model.ipynb
```

The baseline model is a 2D CNN.

---

# 4. Baseline CNN Input

The baseline CNN uses the input shape:

```text
(2, 128, 1)
```

where:

```text
2   → I/Q channels
128 → signal samples
1   → convolution channel dimension
```

---

# 5. Baseline CNN Architecture

The architecture is:

```text
Input
(2, 128, 1)
       ↓
Conv2D
32 Filters
Kernel (1,5)
       ↓
Batch Normalization
       ↓
MaxPooling2D
(1,2)
       ↓
Dropout 0.20
       ↓
Conv2D
64 Filters
Kernel (1,3)
       ↓
Batch Normalization
       ↓
MaxPooling2D
(1,2)
       ↓
Dropout 0.25
       ↓
Conv2D
128 Filters
Kernel (1,3)
       ↓
Batch Normalization
       ↓
Dropout 0.30
       ↓
Flatten
       ↓
Dense 256
       ↓
Dropout 0.50
       ↓
Dense 128
       ↓
Dropout 0.30
       ↓
Dense 11
Softmax
```

---

# 6. Baseline Model Compilation

The baseline CNN uses:

```text
Optimizer:
Adam

Loss:
Categorical Crossentropy

Metric:
Accuracy
```

The final output layer uses:

```text
Softmax
```

with:

```text
11 output classes
```

---

# 7. Baseline Model Purpose

The baseline model is not necessarily the final production model.

Its primary purpose is to provide:

```text
Reference Architecture
        +
Reference Performance
```

The improved CNN can then be compared against this baseline.

---

# 8. Baseline Model Result

The baseline evaluation achieved:

```text
Test Accuracy:
56.43%
```

This result is used as the reference point for the improved model.

---

# 9. Improved CNN

The improved model is implemented in:

```text
models/improved_cnn.py
```

The improved model uses a 1D residual CNN architecture.

The model processes the I/Q signal as a sequence of samples.

---

# 10. Improved CNN Input

The improved CNN uses:

```text
Input Shape:
(128, 2)
```

where:

```text
128 → signal samples
2   → I/Q channels
```

This differs from the baseline model's 2D input representation.

---

# 11. Improved CNN Architecture

The improved architecture contains:

```text
Input
(128, 2)
      ↓
Conv1D
64 Filters
      ↓
Batch Normalization
      ↓
ReLU
      ↓
Residual Block
64 Filters
      ↓
MaxPooling
      ↓
Residual Block
128 Filters
      ↓
MaxPooling
      ↓
Residual Block
256 Filters
      ↓
MaxPooling
      ↓
Conv1D
256 Filters
      ↓
Global Average Pooling
      ↓
Dense 256
      ↓
Dropout 0.40
      ↓
Dense 128
      ↓
Dropout 0.30
      ↓
Dense 11
Softmax
```

---

# 12. Residual Blocks

The improved CNN uses residual connections.

A residual block follows the concept:

```text
Input
  │
  ├───────────────┐
  │               │
  ▼               │
Conv1D            │
  ↓               │
BatchNorm         │
  ↓               │
ReLU              │
  ↓               │
Conv1D            │
  ↓               │
BatchNorm         │
  │               │
  └────── Add ◄───┘
          ↓
        ReLU
```

When the number of channels changes, a `1x1` convolution is used to match the shortcut dimensions.

---

# 13. Global Average Pooling

Instead of directly flattening the convolution output, the improved model uses:

```text
GlobalAveragePooling1D
```

This reduces the feature representation before the dense classification layers.

The resulting features are passed to:

```text
Dense 256
     ↓
Dropout
     ↓
Dense 128
     ↓
Dropout
     ↓
Softmax
```

---

# 14. Improved Model Compilation

The improved model uses:

```text
Optimizer:
Adam

Loss:
Categorical Crossentropy

Metric:
Accuracy
```

The learning rate is configurable when creating the model.

The default implementation uses:

```text
Learning Rate:
0.001
```

---

# 15. Number of Classes

Both models classify the same 11 modulation classes:

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

The final layer therefore contains:

```text
11 neurons
```

with:

```text
Softmax activation
```

---

# 16. Model Comparison

The project compares:

| Model | Architecture | Input | Test Accuracy |
|---|---|---|---:|
| Baseline CNN | 2D CNN | `(2,128,1)` | 56.43% |
| Improved CNN | 1D Residual CNN | `(128,2)` | 62.29% |

The improved model provides a higher overall test accuracy than the baseline.

---

# 17. High-SNR Performance

The improved model also shows substantially better performance at higher SNR values.

Verified result:

```text
High-SNR Accuracy (SNR ≥ 0 dB):
92.08%
```

The project also evaluates performance separately at low SNR:

```text
Low-SNR Accuracy (SNR < 0 dB):
32.39%
```

This demonstrates that signal quality has a significant effect on modulation classification performance.

---

# 18. Saved Model

The trained improved model is saved separately from the architecture code.

The trained model file is:

```text
saved_models/
└── best_improved_cnn_classifier.keras
```

The architecture in:

```text
models/improved_cnn.py
```

defines how the model is constructed.

The saved `.keras` file contains the trained model state.

---

# 19. Model Usage

The model architecture can be created using:

```python
from models.improved_cnn import build_improved_cnn

model = build_improved_cnn(
    input_shape=(128, 2),
    num_classes=11
)
```

The baseline model can be created using:

```python
from models.cnn_model import build_cnn_model

model = build_cnn_model(
    input_shape=(2, 128, 1),
    num_classes=11
)
```

---

# 20. Prediction Flow

The trained model will eventually be used by the testing and application modules.

The overall flow is:

```text
IQ Signal
     ↓
Preprocessing
     ↓
Correct Model Input Shape
     ↓
Trained CNN
     ↓
Softmax Probabilities
     ↓
Highest Probability Class
     ↓
Predicted Modulation
```

---

# 21. Model and Notebook Relationship

The notebooks remain as the experimental development record:

```text
04_cnn_model.ipynb
        ↓
Baseline CNN

05_model_training.ipynb
        ↓
Baseline Training

06_model_evaluation.ipynb
        ↓
Baseline Evaluation

07_improved_cnn_model.ipynb
        ↓
Improved CNN

08_improved_model_evaluation.ipynb
        ↓
Improved Evaluation
```

The reusable Python implementations are maintained in:

```text
models/
```

This separates experimentation from the final software architecture.

---

# 22. Testing the Model Modules

The baseline model can be tested using:

```powershell
python models/cnn_model.py
```

The improved model can be tested using:

```powershell
python models/improved_cnn.py
```

These tests verify that the model architecture can be constructed and that the expected input/output shapes are valid.

---

# 23. Design Principle

The `models/` directory should contain model architecture definitions only.

Training logic should be separated into the appropriate training workflow.

Evaluation logic should be separated into:

```text
evaluation/
```

Prediction logic should be separated into:

```text
testing/
```

This keeps the project modular and easier to maintain.

---

# 24. Model Pipeline

The final AI pipeline is:

```text
RadioML Dataset
       ↓
Preprocessing
       ↓
Normalized IQ
       ↓
CNN
       ↓
Feature Extraction
       ↓
Classification
       ↓
11 Modulation Classes
       ↓
Confidence Score
```

---

# 25. Summary

The `models/` directory contains the two main CNN architectures developed during the project.

```text
Baseline CNN
    ↓
56.43% Test Accuracy
```

and:

```text
Improved Residual CNN
    ↓
62.29% Test Accuracy
    ↓
92.08% High-SNR Accuracy
```

The baseline establishes the reference performance, while the improved CNN provides the current model for the final software classification pipeline.
