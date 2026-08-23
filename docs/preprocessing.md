# Data Preprocessing

## AI Based Intelligent RF Spectrum Signal Identification System

## 1. Introduction

Data preprocessing is an important stage of the AI-based RF spectrum signal identification system.

The RadioML 2016.10a dataset contains RF signals represented as I/Q samples. Before these signals can be used by the CNN model, they must be loaded, organized, prepared, and divided into suitable datasets.

The preprocessing pipeline converts the raw dataset into a format that can be directly used for CNN training, validation, and testing.

The overall preprocessing workflow is:

```text
Raw RadioML Dataset
        ↓
Load Dataset
        ↓
Extract IQ Samples
        ↓
Extract Modulation Labels
        ↓
Extract SNR Values
        ↓
Convert Data to NumPy Arrays
        ↓
Normalize / Prepare IQ Data
        ↓
Encode Modulation Labels
        ↓
Train / Validation / Test Split
        ↓
Save Processed Data
        ↓
CNN Input
```

---

## 2. Input Dataset

The preprocessing stage uses the RadioML 2016.10a dataset.

The expected dataset file is:

```text
RML2016.10a_dict.pkl
```

The dataset is stored locally in:

```text
data/
└── dataset/
    └── RML2016.10a_dict.pkl
```

The dataset contains signal samples associated with:

- Modulation type
- SNR level
- I/Q samples

---

## 3. Dataset Structure

The RadioML dataset is organized using keys representing:

```text
(Modulation Type, SNR)
```

For example:

```text
(BPSK, -20)
(BPSK, -18)
(BPSK, -16)
...
(QPSK, 0)
(QPSK, 2)
...
(WBFM, 18)
```

Each key contains multiple IQ signal samples.

The preprocessing process reads these entries and converts them into separate arrays for:

```text
X → Signal data
y → Modulation labels
SNR → Signal-to-noise ratio
```

---

## 4. I/Q Signal Representation

Each RF signal is represented using two components:

```text
I → In-phase component
Q → Quadrature component
```

The original signal shape used by the project is:

```text
(2, 128)
```

where:

```text
2   → I and Q channels
128 → Samples per signal
```

Therefore, one signal can be represented as:

```text
I[0], I[1], ..., I[127]
Q[0], Q[1], ..., Q[127]
```

The data is stored in NumPy format after preprocessing.

---

## 5. Loading the Dataset

The preprocessing process first checks whether the expected dataset file exists.

Conceptually:

```text
Check Dataset
      │
      ├── Dataset Found
      │       ↓
      │   Load Dataset
      │
      └── Dataset Not Found
              ↓
        Display Error
```

The dataset is loaded from:

```text
data/dataset/RML2016.10a_dict.pkl
```

The loaded object contains the modulation and SNR indexed signal data.

---

## 6. Extracting IQ Samples

For every dataset entry, the preprocessing stage extracts the corresponding IQ signal samples.

The extracted data is stored in:

```text
X
```

The corresponding modulation class is stored in:

```text
y
```

The SNR value is stored separately.

Conceptually:

```text
Dataset Entry
     │
     ├──────────────► IQ Signal → X
     │
     ├──────────────► Modulation → y
     │
     └──────────────► SNR → SNR array
```

---

## 7. Modulation Classes

The project currently uses 11 modulation classes:

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

Each modulation class is converted into a numerical label for machine learning.

The class names are stored separately so that numerical predictions can later be converted back into readable modulation names.

---

## 8. Label Encoding

Machine learning models require numerical labels.

Therefore, modulation names are mapped to integer class indices.

Conceptually:

```text
Modulation Name
       ↓
Numerical Class
       ↓
CNN Training
```

For example, the mapping follows the ordering stored in:

```text
modulation_classes.npy
```

The numerical labels are stored in:

```text
y_train.npy
y_val.npy
y_test.npy
```

The class-name mapping is stored in:

```text
modulation_classes.npy
```

---

## 9. Signal Normalization

The IQ signals are prepared so that their numerical values are suitable for machine learning.

Normalization provides a consistent signal scale and helps the CNN learn useful signal characteristics.

The general preprocessing concept is:

```text
Raw IQ Values
      ↓
Signal Scaling / Normalization
      ↓
Normalized IQ Values
      ↓
CNN Input
```

The exact normalization implementation should remain consistent between:

- Training
- Validation
- Testing
- Future prediction

This is important because the model expects the same input representation during inference as it received during training.

---

## 10. Dataset Splitting

After the IQ signals and labels are prepared, the dataset is divided into:

```text
Training Dataset
Validation Dataset
Testing Dataset
```

The project uses an approximate distribution of:

```text
Training       → 70%
Validation     → 10%
Testing        → 20%
```

The purpose of each dataset is different.

### Training Dataset

Used to train the CNN and update model weights.

### Validation Dataset

Used during training to monitor how the model performs on unseen validation samples.

### Testing Dataset

Used after training to measure the final performance of the model.

---

## 11. Dataset Split Workflow

The complete split can be represented as:

```text
                 Processed Dataset
                        │
            ┌───────────┼───────────┐
            │           │           │
            ▼           ▼           ▼
        Training    Validation    Testing
          70%          10%          20%
            │           │           │
            ▼           ▼           ▼
          CNN         CNN         Final
        Training    Monitoring   Evaluation
```

The test data remains separate from model training.

---

## 12. SNR Data Handling

The SNR value associated with every signal is retained during preprocessing.

This allows the project to analyze model performance at different signal quality levels.

The SNR arrays are:

```text
snr_train.npy
snr_val.npy
snr_test.npy
```

These values are not only useful for dataset organization but are also used later to generate:

```text
Accuracy vs SNR
```

graphs.

---

## 13. Processed Dataset Files

After preprocessing, the following files are generated:

```text
data/
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

---

## 14. Meaning of Processed Files

### `X_train.npy`

Contains the training IQ signal samples.

```text
X_train
```

is used as the input to the CNN during training.

---

### `X_val.npy`

Contains validation IQ samples.

These samples are used to monitor model performance during training.

---

### `X_test.npy`

Contains unseen test IQ samples.

These samples are used for final model evaluation.

---

### `y_train.npy`

Contains the numerical modulation labels corresponding to the training samples.

---

### `y_val.npy`

Contains the numerical modulation labels corresponding to the validation samples.

---

### `y_test.npy`

Contains the numerical modulation labels corresponding to the test samples.

---

### `snr_train.npy`

Contains SNR values corresponding to the training signals.

---

### `snr_val.npy`

Contains SNR values corresponding to the validation signals.

---

### `snr_test.npy`

Contains SNR values corresponding to the test signals.

These values are used during performance analysis.

---

### `modulation_classes.npy`

Contains the names of the modulation classes.

It is used to convert numerical predictions into readable output.

For example:

```text
Class Index
     ↓
9
     ↓
QPSK
```

---

## 15. CNN Input Preparation

The baseline CNN and improved CNN use the processed IQ data.

The original representation is:

```text
(samples, 2, 128)
```

For the improved 1D CNN, the data is rearranged to:

```text
(samples, 128, 2)
```

The reason is that the improved CNN processes the signal as a sequence.

The resulting structure is:

```text
128 → Signal sequence length
2   → I and Q channels
```

Therefore, a single model input has:

```text
128 × 2
```

values.

---

## 16. Data Flow to the Improved CNN

The complete preprocessing flow for the improved model is:

```text
Raw Dataset
      ↓
IQ Samples
      ↓
Normalization
      ↓
Label Encoding
      ↓
Train / Validation / Test Split
      ↓
IQ Dimension Rearrangement
      ↓
(128, 2)
      ↓
Improved 1D CNN
```

---

## 17. Preventing Data Leakage

The test dataset must not be used during model training.

The intended workflow is:

```text
Training Data
     ↓
Model Weight Updates

Validation Data
     ↓
Training Monitoring

Testing Data
     ↓
Final Evaluation
```

The test set is only used after the model has been trained.

This helps provide a more reliable estimate of how the trained model performs on unseen data.

---

## 18. Data Verification

After preprocessing, the generated data should be checked before starting model training.

Important checks include:

```text
Check 1:
Training data exists

Check 2:
Validation data exists

Check 3:
Testing data exists

Check 4:
Labels match signal counts

Check 5:
SNR values match signal counts

Check 6:
Input dimensions are correct

Check 7:
Number of modulation classes is correct
```

The expected relationship is:

```text
Number of X samples
        =
Number of y labels
        =
Number of corresponding SNR values
```

---

## 19. Example Data Relationship

For a dataset subset:

```text
X_test[i]
```

represents one IQ signal.

The corresponding:

```text
y_test[i]
```

represents its modulation class.

And:

```text
snr_test[i]
```

represents its SNR.

Therefore:

```text
X_test[i]
      │
      ├──────► y_test[i]
      │          │
      │          └── Modulation Type
      │
      └──────► snr_test[i]
                 │
                 └── SNR Level
```

All three values refer to the same signal sample.

---

## 20. Preprocessing Notebook

The preprocessing implementation was developed and tested in:

```text
notebooks/02_data_preprocessing.ipynb
```

The notebook is used for:

- Loading the raw dataset
- Preparing IQ samples
- Preparing labels
- Preparing SNR values
- Splitting the data
- Saving processed arrays

The reusable preprocessing implementation will later be moved into:

```text
features/preprocessing.py
```

This allows the final software system to perform the same preprocessing without depending on a Jupyter notebook.

---

## 21. Reusable Preprocessing Module

The final project will use a Python module similar to:

```text
features/
└── preprocessing.py
```

The module will contain reusable functions such as:

```python
load_dataset()
normalize_iq()
encode_labels()
split_dataset()
save_processed_data()
```

The exact function names can be finalized during implementation.

The important goal is to keep the preprocessing logic consistent between development and final software execution.

---

## 22. Preprocessing and Future Live RF Signals

The preprocessing stage is also important for future RTL-SDR integration.

The trained model expects a specific IQ data format.

Therefore, live RF data must eventually follow a compatible pipeline:

```text
RTL-SDR
   ↓
Live IQ Samples
   ↓
Select Signal Segment
   ↓
Match Expected Sample Length
   ↓
Apply Same Preprocessing
   ↓
Convert to CNN Input Format
   ↓
Trained CNN
```

The same preprocessing logic should be reused for both dataset-based signals and future live signals wherever applicable.

---

## 23. Software Data Pipeline

The complete software data pipeline is:

```text
RadioML Dataset
       │
       ▼
Dataset Loader
       │
       ▼
IQ Extraction
       │
       ├──────────────► Modulation Label
       │
       └──────────────► SNR
       │
       ▼
Normalization
       │
       ▼
Dataset Split
       │
       ▼
Processed NumPy Files
       │
       ▼
CNN Input Preparation
       │
       ▼
AI Model
```

---

## 24. Data Directory Structure

The project uses the following data structure:

```text
data/
│
├── dataset/
│   ├── README.md
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

The raw and processed datasets may be kept locally rather than committed directly to GitHub if they are too large.

---

## 25. Preprocessing Status

The following preprocessing stages have been completed:

```text
Raw Dataset Loading             ✅
IQ Sample Extraction            ✅
Modulation Label Extraction     ✅
SNR Extraction                  ✅
Label Encoding                  ✅
IQ Data Preparation             ✅
Dataset Splitting               ✅
Processed Data Generation      ✅
CNN Input Preparation           ✅
```

---

## 26. Preprocessing Output

The final output of this stage is a set of processed datasets ready for AI model training and evaluation.

```text
Processed IQ Signals
        +
Modulation Labels
        +
SNR Information
        ↓
CNN Training / Validation / Testing
```

The processed data forms the connection between the raw RF dataset and the AI model.

---

## 27. Summary

The preprocessing stage converts the raw RadioML 2016.10a dataset into structured data suitable for deep learning.

The main operations are:

```text
Load
 ↓
Extract
 ↓
Normalize
 ↓
Encode
 ↓
Split
 ↓
Reshape
 ↓
Save
```

The resulting processed data is used by the CNN-based automatic modulation classification system.

The preprocessing stage therefore provides the foundation for:

```text
AI Model Training
        ↓
Model Evaluation
        ↓
Modulation Prediction
        ↓
Final RF Signal Identification System
```
