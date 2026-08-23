# Features

The `features/` directory contains the reusable signal preprocessing and signal-analysis functions used by the AI Based Intelligent RF Spectrum Signal Identification System.

The modules in this directory convert raw RF/IQ data into formats that can be used for machine-learning, signal analysis, evaluation, and visualization.

## Directory Structure

```text
features/
├── __init__.py
├── preprocessing.py
├── feature_extraction.py
└── README.md
```

## 1. Purpose

The main responsibilities of this directory are:

```text
Raw RF Dataset
      ↓
Preprocessing
      ↓
Normalized IQ Data
      ↓
Signal Analysis
      ├── FFT Spectrum
      ├── Constellation
      ├── Spectrogram
      ├── Amplitude
      └── Phase
```

The feature-processing stage is separated from the model stage so that the same processing functions can be reused by training, testing, evaluation, and the final application.

---

# 2. `preprocessing.py`

The `preprocessing.py` module contains the complete preprocessing pipeline for the RadioML 2016.10a dataset.

## Responsibilities

The module performs:

```text
Dataset Loading
       ↓
Dataset Information Extraction
       ↓
IQ Signal Combination
       ↓
Modulation Label Creation
       ↓
Label Encoding
       ↓
IQ Normalization
       ↓
Train / Validation / Test Split
       ↓
Processed Data Saving
```

## 3. Dataset Loading

The module loads:

```text
RML2016.10a_dict.pkl
```

using Python's `pickle` module.

The dataset contains IQ signal samples indexed by:

```text
(Modulation, SNR)
```

---

# 4. Modulation Labels

The preprocessing module extracts the modulation types from the dataset and uses `LabelEncoder` to convert modulation names into integer class IDs.

The project contains:

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

The resulting class mapping is saved as:

```text
modulation_classes.npy
```

---

# 5. IQ Signal Representation

The RadioML signals contain two channels:

```text
Channel 0 → I
Channel 1 → Q
```

The signal representation used by the preprocessing pipeline is:

```text
(2, 128)
```

where:

```text
2   → I/Q channels
128 → samples per signal
```

---

# 6. IQ Normalization

Each IQ signal is normalized independently.

The magnitude is calculated as:

```text
Magnitude = √(I² + Q²)
```

The maximum magnitude of the signal is then used for normalization.

The process is:

```text
I/Q Signal
    ↓
Calculate Magnitude
    ↓
Find Maximum Magnitude
    ↓
Normalize I and Q
```

A zero maximum magnitude is protected against division by zero.

---

# 7. Dataset Splitting

The preprocessing pipeline performs a stratified dataset split.

First:

```text
80% → Training + Validation
20% → Testing
```

Then the training-plus-validation portion is divided into:

```text
87.5% → Training
12.5% → Validation
```

The resulting overall split is:

```text
Training    → 70%
Validation  → 10%
Testing     → 20%
```

The split uses:

```text
random_state = 42
```

and stratification based on modulation labels.

---

# 8. Processed Data Files

The preprocessing module generates:

```text
data/processed/
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

These files provide the interface between preprocessing and the machine-learning pipeline.

---

# 9. `feature_extraction.py`

The `feature_extraction.py` module provides reusable RF signal-analysis functions.

It generates:

```text
IQ Signal
   ├── FFT Spectrum
   ├── Constellation Data
   ├── Amplitude
   ├── Phase
   └── Spectrogram
```

These representations are useful for:

- Signal analysis
- Visualization
- Debugging
- RF signal interpretation
- Final application display

---

# 10. Complex IQ Representation

The I and Q channels are converted into a complex signal:

```text
Complex IQ = I + jQ
```

This representation is used for frequency-domain and time-frequency analysis.

---

# 11. FFT Spectrum

The module provides FFT calculation using:

```text
NumPy FFT
```

The FFT produces:

```text
Frequency Axis
+
Magnitude Spectrum
```

A decibel representation is also available.

Conceptually:

```text
IQ Signal
    ↓
FFT
    ↓
Frequency Spectrum
    ↓
Magnitude / dB
```

The FFT can be shifted so that zero frequency appears at the center.

---

# 12. Constellation Data

The constellation representation uses:

```text
X-axis → I
Y-axis → Q
```

The module returns the I and Q values required to generate a constellation diagram.

This representation is useful for visually understanding modulation behavior.

Examples include:

```text
BPSK
QPSK
8PSK
QAM16
QAM64
```

---

# 13. Amplitude

The instantaneous signal amplitude is calculated using:

```text
Amplitude = √(I² + Q²)
```

This provides the magnitude of the received complex signal over time.

---

# 14. Phase

The instantaneous phase is calculated from the complex IQ signal.

The phase is unwrapped to make the phase progression easier to analyze.

```text
IQ
 ↓
Complex Signal
 ↓
Angle
 ↓
Unwrapped Phase
```

---

# 15. Spectrogram

The spectrogram provides a time-frequency representation of the IQ signal.

The output contains:

```text
Frequency
Time
Power
```

The power can also be represented in decibels.

Conceptually:

```text
IQ Signal
     ↓
STFT
     ↓
Time-Frequency Representation
     ↓
Spectrogram
```

Because the input is complex IQ data, the STFT uses the two-sided frequency representation.

---

# 16. Main Feature Extraction Function

The module provides:

```python
extract_signal_features()
```

This function generates the main signal-analysis outputs together.

The returned information includes:

```text
fft_frequency
fft_magnitude
constellation_i
constellation_q
amplitude
phase
spectrogram_frequency
spectrogram_time
spectrogram_power
```

---

# 17. Testing

The module contains a standalone test section.

Run:

```powershell
python features/feature_extraction.py
```

The preprocessing module can be tested using:

```powershell
python features/preprocessing.py
```

Successful execution confirms that the reusable feature-processing modules can run independently of the Jupyter notebooks.

---

# 18. Relationship With Other Modules

The feature-processing stage connects the dataset with the AI models and application.

```text
data/
   ↓
features/preprocessing.py
   ↓
data/processed/
   ↓
models/
   ↓
evaluation/
   ↓
testing/
   ↓
visualization/
   ↓
application
```

---

# 19. Important Design Principle

The feature-analysis functions are kept separate from the CNN model.

The project therefore distinguishes between:

```text
Signal Processing / Analysis
```

and:

```text
Machine Learning Classification
```

The CNN receives the model-specific input format required by its architecture, while FFT, constellation, and spectrogram functions are available for signal interpretation and visualization.

---

# 20. Summary

The `features/` directory provides the reusable signal-processing foundation of the project.

It contains:

```text
preprocessing.py
    ↓
Dataset preparation

feature_extraction.py
    ↓
FFT
Constellation
Spectrogram
Amplitude
Phase
```

These modules allow the project to move from notebook-based experimentation toward a reusable software pipeline.
