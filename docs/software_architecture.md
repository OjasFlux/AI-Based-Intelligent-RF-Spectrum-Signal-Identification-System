# Software Architecture

## AI Based Intelligent RF Spectrum Signal Identification System

## 1. Introduction

The software architecture defines how the different Python modules of the project work together to form the complete RF signal identification system.

The project was initially developed using Jupyter notebooks for experimentation, dataset analysis, model development, training, and evaluation.

After validating the AI model, the project is organized into reusable Python modules.

The software architecture separates the project into:

```text
Data
   ↓
Features
   ↓
Model
   ↓
Evaluation
   ↓
Testing / Prediction
   ↓
Visualization
   ↓
Application
```

---

## 2. Overall Software Architecture

The complete software architecture is:

```text
                    INPUT DATA
                        │
                        ▼
              ┌──────────────────┐
              │      data/       │
              │                  │
              │ Dataset / IQ     │
              │ Processed Data   │
              └────────┬─────────┘
                       │
                       ▼
              ┌──────────────────┐
              │    features/     │
              │                  │
              │ Preprocessing    │
              │ Feature Utility  │
              └────────┬─────────┘
                       │
                       ▼
              ┌──────────────────┐
              │     models/      │
              │                  │
              │ CNN Architecture │
              │ Improved CNN     │
              └────────┬─────────┘
                       │
                       ▼
              ┌──────────────────┐
              │  saved_models/   │
              │                  │
              │ Trained CNN      │
              └────────┬─────────┘
                       │
              ┌────────┴─────────┐
              ▼                  ▼
      ┌──────────────┐    ┌──────────────┐
      │ evaluation/  │    │   testing/   │
      │              │    │              │
      │ Metrics      │    │ Prediction   │
      │ Confusion    │    │ Inference    │
      │ SNR Analysis │    │ Testing      │
      └──────┬───────┘    └──────┬───────┘
             │                   │
             └─────────┬─────────┘
                       ▼
              ┌──────────────────┐
              │ visualization/   │
              │                  │
              │ IQ Signal        │
              │ FFT              │
              │ Constellation    │
              │ Spectrogram      │
              └────────┬─────────┘
                       │
                       ▼
              ┌──────────────────┐
              │      app/        │
              │                  │
              │ Final Dashboard  │
              └──────────────────┘
```

---

## 3. Repository Structure

The main software-related structure is:

```text
project/
│
├── data/
│
├── features/
│
├── models/
│
├── saved_models/
│
├── evaluation/
│
├── testing/
│
├── visualization/
│
├── app/
│
├── notebooks/
│
└── docs/
```

Each directory has a specific responsibility.

---

## 4. Data Layer

The `data/` directory contains the dataset and processed data.

```text
data/
├── dataset/
│   └── RML2016.10a_dict.pkl
│
└── processed/
    ├── X_train.npy
    ├── X_val.npy
    ├── X_test.npy
    ├── y_train.npy
    ├── y_val.npy
    ├── y_test.npy
    ├── snr_train.npy
    ├── snr_val.npy
    ├── snr_test.npy
    └── modulation_classes.npy
```

The data layer provides the input required by the preprocessing and AI model.

---

## 5. Features Layer

The `features/` directory contains reusable signal-processing and preprocessing functions.

Planned structure:

```text
features/
├── preprocessing.py
└── feature_extraction.py
```

Responsibilities include:

- Loading data
- Preparing IQ signals
- Normalization
- Label preparation
- Input reshaping
- FFT generation
- Spectrogram generation
- Constellation generation

The feature layer prepares the signal before it reaches the AI model.

---

## 6. Model Layer

The `models/` directory contains the CNN architecture.

Planned structure:

```text
models/
├── cnn_model.py
└── improved_cnn.py
```

Responsibilities include:

- CNN architecture
- Improved CNN architecture
- Residual blocks
- Model creation
- Model compilation

The model layer should contain the architecture rather than the trained model weights.

---

## 7. Saved Models Layer

The `saved_models/` directory contains trained model files.

Example:

```text
saved_models/
└── best_improved_cnn_classifier.keras
```

The distinction is:

```text
models/
    ↓
How the model is built

saved_models/
    ↓
Trained model parameters
```

The saved model can be loaded for prediction without retraining.

---

## 8. Evaluation Layer

The `evaluation/` directory contains model evaluation functionality.

Planned structure:

```text
evaluation/
├── evaluate_model.py
├── classification_report.txt
├── confusion_matrix.png
├── normalized_confusion_matrix.png
├── accuracy_vs_snr.png
└── evaluation_summary.txt
```

The evaluation module is responsible for:

- Accuracy
- Precision
- Recall
- F1-score
- Confusion matrix
- SNR-based analysis
- Evaluation reports

---

## 9. Testing and Prediction Layer

The `testing/` directory contains prediction and testing functionality.

Planned structure:

```text
testing/
├── predict.py
└── test_model.py
```

The prediction module performs:

```text
Input IQ
   ↓
Preprocessing
   ↓
Load Saved Model
   ↓
Prediction
   ↓
Class Mapping
   ↓
Modulation + Confidence
```

The testing module verifies that the model and prediction pipeline operate correctly.

---

## 10. Visualization Layer

The `visualization/` directory contains RF signal visualization modules.

Planned structure:

```text
visualization/
├── time_domain.py
├── fft.py
├── constellation.py
└── spectrogram.py
```

The visualization layer can generate:

- I/Q time-domain plots
- FFT spectrum
- Constellation diagrams
- Spectrograms

These visualizations can be used independently or displayed through the final application.

---

## 11. Application Layer

The `app/` directory contains the final user-facing application.

The application can provide:

```text
Input Signal
     ↓
Prediction
     ↓
Modulation
     ↓
Confidence
     ↓
Visualization
```

The application can eventually display:

```text
Detected Modulation
Prediction Confidence
I/Q Signal
FFT
Constellation
Spectrogram
```

A dashboard framework such as Streamlit can be considered for the final software interface.

---

## 12. Notebook Layer

The `notebooks/` directory contains experimental development notebooks.

The notebooks are used for:

- Dataset analysis
- Preprocessing experiments
- Signal visualization
- Model development
- Training
- Evaluation

The notebooks document the development process.

However, the final software should not depend on notebooks for normal execution.

The reusable functionality should be moved into Python modules.

---

## 13. Documentation Layer

The `docs/` directory contains technical project documentation.

It includes:

```text
project_overview.md
system_architecture.md
methodology.md
dataset.md
preprocessing.md
feature_extraction.md
model_architecture.md
training.md
evaluation.md
prediction.md
software_architecture.md
hardware_integration.md
progress.md
```

The documentation explains how the complete project works.

---

## 14. Software Data Flow

The main software data flow is:

```text
Processed IQ Data
        ↓
features/preprocessing.py
        ↓
Prepared CNN Input
        ↓
models/improved_cnn.py
        ↓
Trained Model
        ↓
saved_models/
        ↓
testing/predict.py
        ↓
Prediction
        ↓
visualization/
        ↓
app/
```

---

## 15. Training Data Flow

Training uses:

```text
data/processed/
       ↓
Load Training Data
       ↓
features/
       ↓
Input Preparation
       ↓
models/
       ↓
CNN Training
       ↓
saved_models/
       ↓
Best Trained Model
```

---

## 16. Evaluation Data Flow

Evaluation uses:

```text
data/processed/X_test.npy
             +
data/processed/y_test.npy
             +
data/processed/snr_test.npy
             ↓
      Trained CNN
             ↓
       Predictions
             ↓
        evaluation/
             ↓
   Metrics and Graphs
```

---

## 17. Prediction Data Flow

Prediction uses:

```text
IQ Signal
    ↓
Preprocessing
    ↓
Input Shape (128, 2)
    ↓
Saved CNN
    ↓
Prediction Probabilities
    ↓
Highest Probability
    ↓
Class Mapping
    ↓
Modulation Name
    ↓
Confidence
```

---

## 18. Visualization Data Flow

The visualization system receives IQ data and generates different signal representations.

```text
IQ Signal
   │
   ├────► Time Domain
   │
   ├────► FFT
   │
   ├────► Constellation
   │
   └────► Spectrogram
```

The visualization output can then be displayed by the application.

---

## 19. Separation of Responsibilities

Each module should have a clear responsibility.

| Module | Responsibility |
|---|---|
| `data/` | Dataset and processed data |
| `features/` | Preprocessing and signal processing |
| `models/` | CNN architecture |
| `saved_models/` | Trained model |
| `evaluation/` | Performance evaluation |
| `testing/` | Prediction and testing |
| `visualization/` | Signal visualization |
| `app/` | User interface |
| `notebooks/` | Experiments |
| `docs/` | Documentation |

This separation makes the project easier to maintain.

---

## 20. Dependency Flow

The main dependency direction is:

```text
data
 ↓
features
 ↓
models
 ↓
saved_models
 ↓
testing
 ↓
visualization
 ↓
app
```

Evaluation operates mainly on:

```text
data + saved_models
```

and produces evaluation results.

---

## 21. Final Software Workflow

The final software workflow is:

```text
                    IQ SIGNAL
                        │
                        ▼
                Input Validation
                        │
                        ▼
                  Preprocessing
                        │
                        ▼
                  CNN Input
                  (128, 2)
                        │
                        ▼
                 Trained CNN
                        │
                        ▼
               Class Probabilities
                        │
                        ▼
                Modulation Type
                        +
                   Confidence
                        │
                        ▼
                 Visualization
                        │
                        ▼
                   Dashboard
```

---

## 22. Software and Future Hardware

The software architecture is designed so that the input source can eventually change.

Currently:

```text
RadioML Dataset
      ↓
Preprocessing
      ↓
CNN
```

Future:

```text
RTL-SDR
      ↓
Live IQ
      ↓
Preprocessing
      ↓
CNN
```

The main classification system can remain unchanged if the live IQ samples are correctly prepared.

---

## 23. Design Principle

The main design principle is:

```text
Separate Data
     ↓
Separate Processing
     ↓
Separate Model
     ↓
Separate Evaluation
     ↓
Separate Prediction
     ↓
Separate Visualization
     ↓
Application
```

This makes it possible to replace or improve individual components without rewriting the complete project.

---

## 24. Current Software Status

Completed:

```text
Dataset Analysis              ✅
Preprocessing                 ✅
CNN Development               ✅
Model Training                ✅
Model Evaluation              ✅
Signal Visualization          ✅
```

Implementation work remaining:

```text
Reusable Feature Modules      ⏳
Reusable Model Module         ⏳
Reusable Evaluation Module   ⏳
Prediction Module             ⏳
Visualization Modules         ⏳
Final Dashboard               ⏳
```

---

## 25. Summary

The software architecture converts the experimental notebook-based implementation into a modular Python project.

The architecture follows:

```text
DATA
 ↓
FEATURES
 ↓
MODEL
 ↓
EVALUATION
 ↓
PREDICTION
 ↓
VISUALIZATION
 ↓
APPLICATION
```

This structure provides a clean foundation for the final software system and allows future RTL-SDR hardware integration without redesigning the complete AI classification system.
