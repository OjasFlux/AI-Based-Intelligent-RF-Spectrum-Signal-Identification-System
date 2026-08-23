# Feature Extraction and Signal Representation

## AI Based Intelligent RF Spectrum Signal Identification System

## 1. Introduction

Feature extraction and signal representation are important parts of the RF signal identification system.

In this project, the **improved CNN uses the I/Q samples directly as its primary model input**.

Additional signal representations such as FFT, constellation diagrams, and spectrograms are generated mainly for:

- RF signal analysis
- Visualization
- Understanding signal characteristics
- Demonstration
- Future software dashboard integration

Therefore, the project distinguishes between:

```text
Primary AI Input
        ↓
Raw / Preprocessed I/Q Samples

Additional Signal Representations
        ↓
FFT
Constellation
Spectrogram
```

---

## 2. Signal Representation

An RF communication signal can be represented using two components:

```text
I → In-phase component
Q → Quadrature component
```

The RadioML dataset provides the signal in I/Q format.

The original signal representation used in the project is:

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
128 → Signal sequence length
2   → I and Q channels
```

---

## 3. Primary AI Feature Representation

The current improved CNN does not require conversion of the signal into an image before classification.

Instead, the CNN receives the I/Q sequence directly:

```text
Preprocessed IQ Signal
        ↓
Dimension Rearrangement
        ↓
(128, 2)
        ↓
Improved 1D CNN
        ↓
Feature Extraction
        ↓
Classification
```

The two input channels are:

```text
Channel 1 → I
Channel 2 → Q
```

This allows the network to learn useful signal characteristics directly from the I/Q sequence.

---

## 4. Why I/Q Samples Are Used

I/Q samples contain information about the amplitude and phase behavior of the received signal.

The I and Q components together provide a representation of the complex baseband signal.

Conceptually:

```text
Complex Baseband Signal
          │
          ├────────► I
          │
          └────────► Q
```

The CNN can learn patterns from the variation of I and Q over the signal sequence.

These learned patterns can be related to characteristics of different modulation schemes.

---

## 5. Feature Learning by CNN

The project uses deep learning so that the CNN can automatically learn useful features from the I/Q data.

Instead of manually defining all signal features, the CNN performs feature extraction through convolutional layers.

The process is:

```text
I/Q Samples
     ↓
Convolution
     ↓
Low-Level Signal Features
     ↓
Deeper Convolution
     ↓
Higher-Level Signal Features
     ↓
Feature Aggregation
     ↓
Classification
```

The network learns these features during training.

---

## 6. Convolutional Feature Extraction

The improved CNN uses `Conv1D` layers to process the sequential I/Q data.

The input is:

```text
128 × 2
```

The convolutional layers scan across the signal sequence and learn local patterns.

Conceptually:

```text
I/Q Sequence
      ↓
Conv1D
      ↓
Feature Maps
      ↓
More Conv1D Layers
      ↓
Higher-Level Feature Maps
```

The learned feature maps are then passed to later layers for classification.

---

## 7. Batch Normalization

Batch normalization is used after convolutional layers.

Its purpose is to improve training stability and help the network learn efficiently.

The simplified structure is:

```text
Conv1D
  ↓
Batch Normalization
  ↓
Activation
```

Batch normalization is used in the improved CNN architecture.

---

## 8. Residual Feature Extraction

The improved CNN uses residual blocks.

A residual block allows information from an earlier layer to be passed directly to a later layer.

Conceptually:

```text
             ┌──────────────────────┐
             │                      │
Input ───────┼──► Conv1D ─► Conv1D ─┼──► Add
             │                      │
             └──────────────────────┘
                        │
                        ▼
                    Activation
```

The residual connection helps maintain information flow through deeper feature extraction layers.

---

## 9. Pooling

Pooling layers are used to reduce the temporal dimension of the feature maps.

The simplified process is:

```text
Feature Maps
      ↓
Pooling
      ↓
Reduced Feature Representation
```

This helps reduce computational requirements while retaining important learned information.

---

## 10. Global Average Pooling

After the convolutional feature extraction stages, the improved CNN uses global average pooling.

The purpose is to convert the feature maps into a compact feature representation.

Conceptually:

```text
Feature Maps
      ↓
Global Average Pooling
      ↓
Compact Feature Vector
```

This feature vector is then passed to the dense classification layers.

---

## 11. FFT Feature Representation

Fast Fourier Transform (FFT) is used to examine the signal in the frequency domain.

The FFT converts a time-domain signal into a frequency-domain representation.

The basic process is:

```text
Time-Domain Signal
        ↓
       FFT
        ↓
Frequency-Domain Signal
```

The frequency spectrum can help identify characteristics such as:

- Frequency distribution
- Bandwidth
- Spectral shape
- Dominant frequency components

---

## 12. FFT in This Project

FFT is primarily used for **signal analysis and visualization** in the current implementation.

It is not the primary input representation of the improved CNN.

The current AI pipeline is:

```text
I/Q Samples
     ↓
Preprocessing
     ↓
Improved 1D CNN
     ↓
Modulation Classification
```

The visualization pipeline can separately generate:

```text
I/Q Samples
     ↓
FFT
     ↓
Frequency Spectrum
```

This distinction is important when explaining the project.

---

## 13. Constellation Diagram

A constellation diagram represents the relationship between the I and Q components.

The I component is plotted on the horizontal axis and the Q component is plotted on the vertical axis.

```text
             Q
             ↑
             │
        •    │    •
             │
─────────────┼─────────────► I
             │
        •    │    •
             │
```

Different modulation schemes can produce different distributions of points.

For example, digital modulation schemes may show characteristic symbol patterns.

---

## 14. Constellation Analysis

The constellation diagram is useful for:

- Understanding modulation characteristics
- Visual signal analysis
- Demonstrating modulation differences
- Investigating classification errors
- Supporting the final dashboard

The basic process is:

```text
I/Q Samples
      ↓
Separate I and Q
      ↓
Plot I vs Q
      ↓
Constellation Diagram
```

---

## 15. Spectrogram

A spectrogram represents how the frequency content of a signal changes over time.

It combines time and frequency information.

The conceptual process is:

```text
RF Signal
    ↓
Short-Time Fourier Transform
    ↓
Time-Frequency Representation
    ↓
Spectrogram
```

A spectrogram can help visualize:

- Frequency changes
- Signal duration
- Bandwidth
- Frequency activity
- Time-varying signal characteristics

---

## 16. Spectrogram in This Project

The spectrogram is primarily intended for:

- Signal visualization
- Signal analysis
- Demonstration
- Future dashboard display

The current improved CNN does not directly use the spectrogram as its input.

The current model input remains:

```text
I/Q Sequence
```

This should be clearly stated during the project presentation.

---

## 17. Comparison of Signal Representations

| Representation | Purpose | Current CNN Input |
|---|---|---|
| I/Q Samples | Primary signal representation | Yes |
| FFT | Frequency-domain analysis | No |
| Constellation | I/Q relationship visualization | No |
| Spectrogram | Time-frequency visualization | No |

Therefore:

```text
I/Q
 ↓
AI Classification

FFT
 ↓
Frequency Analysis

Constellation
 ↓
Modulation Visualization

Spectrogram
 ↓
Time-Frequency Analysis
```

---

## 18. Feature Extraction Pipeline

The complete signal representation workflow is:

```text
                    I/Q Signal
                        │
             ┌──────────┴──────────┐
             │                     │
             ▼                     ▼
      CNN Input Path       Visualization Path
             │                     │
             ▼             ┌───────┼────────┐
       Preprocessing       │       │        │
             │             ▼       ▼        ▼
             ▼            FFT  Constell. Spectrogram
       (128, 2)
             │
             ▼
       Improved CNN
             │
             ▼
       Learned Features
             │
             ▼
       Classification
```

---

## 19. Learned Features vs Hand-Crafted Features

Traditional signal classification methods may use manually designed features.

Examples include:

- Spectral features
- Statistical features
- Amplitude characteristics
- Phase characteristics
- Frequency-domain characteristics

In this project, the improved CNN learns useful features automatically from the I/Q input.

Therefore:

```text
Traditional Approach
        ↓
Manual Feature Engineering
        ↓
Classifier

This Project
        ↓
I/Q Samples
        ↓
CNN Automatically Learns Features
        ↓
Classifier
```

This reduces the need to manually define a large set of signal features.

---

## 20. Relationship Between Feature Extraction and Classification

The CNN combines feature extraction and classification into a single deep learning pipeline.

```text
I/Q Input
    ↓
Convolutional Layers
    ↓
Feature Extraction
    ↓
Residual Feature Learning
    ↓
Feature Aggregation
    ↓
Dense Layers
    ↓
Softmax
    ↓
Modulation Class
```

The convolutional layers learn features while the final layers perform classification.

---

## 21. Input Shape Transformation

The preprocessing stage initially produces data in the form:

```text
(samples, 2, 128)
```

The improved CNN requires:

```text
(samples, 128, 2)
```

Therefore, the dimensions are rearranged:

```text
Original:
(samples, 2, 128)

        ↓

Transpose

        ↓

CNN Input:
(samples, 128, 2)
```

This does not change the actual signal values.

It only changes the arrangement so that the temporal dimension is processed as the sequence dimension.

---

## 22. Example of Input Preparation

For one signal:

```text
Original:

2 × 128

Channel 0 → I
Channel 1 → Q
```

After rearrangement:

```text
128 × 2

Column 1 → I
Column 2 → Q
```

Conceptually:

```text
Sample 0 → [I0, Q0]
Sample 1 → [I1, Q1]
Sample 2 → [I2, Q2]
...
Sample 127 → [I127, Q127]
```

This is the format provided to the improved 1D CNN.

---

## 23. Feature Extraction and SNR

The quality of the available signal features depends strongly on SNR.

At low SNR:

```text
Signal
   +
High Noise
   ↓
Difficult Feature Extraction
   ↓
Difficult Classification
```

At high SNR:

```text
Signal
   +
Lower Relative Noise
   ↓
Clearer Signal Characteristics
   ↓
Better Classification
```

This is reflected in the project's SNR-based evaluation.

The improved model achieved approximately:

```text
SNR >= 0 dB
92.08% accuracy
```

while:

```text
SNR < 0 dB
32.39% accuracy
```

This demonstrates the strong relationship between signal quality and classification performance.

---

## 24. Feature Visualization for Model Analysis

The additional signal representations are useful when investigating model predictions.

For example:

```text
Incorrect Prediction
        ↓
Check IQ Signal
        ↓
Check Constellation
        ↓
Check FFT
        ↓
Check Spectrogram
        ↓
Analyze Possible Reason
```

This can help the development team understand why certain modulation classes are difficult to classify.

---

## 25. Feature Extraction Software Module

The final project will contain reusable feature and signal-processing functions in:

```text
features/
```

The planned structure is:

```text
features/
├── preprocessing.py
└── feature_extraction.py
```

The `feature_extraction.py` module can contain reusable functions for:

```python
compute_fft()
generate_spectrogram()
create_constellation()
prepare_iq_input()
```

The exact implementation can be refined during the software integration stage.

---

## 26. Visualization Modules

Visualization-specific functions will be maintained under:

```text
visualization/
```

The planned structure is:

```text
visualization/
├── time_domain.py
├── fft.py
├── constellation.py
└── spectrogram.py
```

This separation keeps the signal-processing and visualization components organized.

---

## 27. Feature Extraction During Future Live Operation

If RTL-SDR hardware is integrated later, the signal-processing pipeline can become:

```text
RTL-SDR
   ↓
Live IQ Samples
   ↓
Signal Segmentation
   ↓
Preprocessing
   ↓
      ┌───────────────────────┐
      │                       │
      ▼                       ▼
 CNN Input              Visualization
      │                       │
      ▼                 ┌─────┼─────┐
   CNN Model             ▼     ▼     ▼
      │                 FFT  Const. Spectrogram
      ▼
Modulation Classification
```

The same trained model can then be used to classify appropriately prepared live IQ data.

---

## 28. Feature Extraction Summary

The project uses two main categories of signal representation.

### Primary AI Representation

```text
Preprocessed I/Q Samples
        ↓
Improved 1D CNN
        ↓
Automatic Feature Learning
        ↓
Modulation Classification
```

### Supporting Signal Representations

```text
I/Q Samples
   ├──► FFT
   ├──► Constellation
   └──► Spectrogram
```

The supporting representations are primarily used for signal analysis and visualization.

---

## 29. Current Feature Processing Status

The current project has completed:

```text
I/Q Signal Extraction          ✅
I/Q Data Preparation           ✅
CNN Input Reshaping            ✅
CNN Automatic Feature Learning ✅
FFT Analysis                   ✅
Constellation Visualization    ✅
Spectrogram Visualization      ✅
```

The reusable feature-processing modules will be implemented during the transition from notebook-based development to the final Python project structure.

---

## 30. Summary

The project primarily uses preprocessed I/Q samples as the input to the improved CNN.

The CNN automatically learns useful signal features through convolutional and residual feature extraction layers.

FFT, constellation diagrams, and spectrograms are additionally generated to analyze and visualize the RF signals.

The distinction between these representations is:

```text
                RF IQ Signal
                     │
          ┌──────────┴──────────┐
          │                     │
          ▼                     ▼
     AI Classification      Visualization
          │                     │
          ▼              ┌──────┼──────┐
     I/Q → CNN            ▼      ▼      ▼
                         FFT  Constell. Spectrogram
          │
          ▼
   Modulation Type
          +
      Confidence
```

This approach allows the system to combine AI-based automatic classification with traditional RF signal visualization techniques.
