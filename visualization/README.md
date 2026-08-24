# Visualization

The `visualization/` directory contains visualization utilities for interpreting RF/IQ signals and presenting model-related signal information.

The visualization module reuses the signal-processing functions from:

```text
features/feature_extraction.py
```

## Directory Structure

```text
visualization/
├── __init__.py
├── visualize_signal.py
├── results/
└── README.md
```

## 1. Purpose

The visualization stage converts IQ data into understandable graphical representations.

```text
IQ Signal
    ↓
Visualization
    ├── I/Q Waveform
    ├── FFT Spectrum
    ├── Constellation
    ├── Spectrogram
    ├── Amplitude
    └── Phase
```

These visualizations help with signal analysis, debugging, model interpretation, documentation, and final project demonstrations.

## 2. I/Q Waveform

The I/Q waveform displays:

```text
I signal
Q signal
```

against the sample index.

It helps visualize how the in-phase and quadrature components change over time.

## 3. FFT Spectrum

The FFT visualization displays the frequency-domain representation of the signal.

```text
IQ Signal
    ↓
FFT
    ↓
Frequency Spectrum
```

It can help identify frequency characteristics and signal energy distribution.

## 4. Constellation Diagram

The constellation diagram uses:

```text
X-axis → I
Y-axis → Q
```

It provides a visual representation of the IQ samples.

Different modulation schemes can produce different characteristic distributions.

Examples include:

```text
BPSK
QPSK
8PSK
QAM16
QAM64
```

## 5. Spectrogram

The spectrogram displays signal behavior in both time and frequency.

```text
Time
  ×
Frequency
  ×
Power
```

It is generated using the STFT-based function from:

```text
features/feature_extraction.py
```

## 6. Amplitude

The amplitude visualization displays:

```text
√(I² + Q²)
```

over the signal samples.

This shows how the signal magnitude changes over time.

## 7. Phase

The phase visualization displays the unwrapped phase of the complex IQ signal.

```text
I + jQ
   ↓
Phase
   ↓
Unwrapped Phase
```

## 8. Reusing Feature Functions

The visualization module does not duplicate the signal-processing algorithms.

Instead, it imports functions from:

```python
features.feature_extraction
```

This keeps the project modular.

The relationship is:

```text
features/
    ↓
Signal Processing Functions
    ↓
visualization/
    ↓
Graphical Representation
```

## 9. Input Format

The visualization module accepts IQ signals with either:

```text
(2, 128)
```

or:

```text
(128, 2)
```

The data is internally converted to:

```text
(2, 128)
```

for visualization.

## 10. Using an IQ File

Run:

```powershell
python visualization/visualize_signal.py --input path/to/iq_signal.npy
```

The generated images are saved under:

```text
visualization/results/
```

unless another output directory is specified.

## 11. Default Software Test

If no input file is provided:

```powershell
python visualization/visualize_signal.py
```

the module generates a simple demo IQ signal.

This is only a software pipeline test.

It is not a RadioML benchmark sample and should not be used as an actual classification-performance result.

## 12. Generated Visualizations

A typical run produces:

```text
visualization/results/
├── demo_iq_waveform.png
├── demo_fft.png
├── demo_constellation.png
├── demo_spectrogram.png
├── demo_amplitude.png
└── demo_phase.png
```

## 13. Relationship With Testing

The testing module produces the classification result:

```text
Predicted Modulation
Confidence
```

The visualization module provides the signal representation:

```text
I/Q
FFT
Constellation
Spectrogram
Amplitude
Phase
```

Together they can form the final demonstration:

```text
IQ Signal
    ↓
┌─────────────────────────────┐
│ Signal Visualizations       │
├─────────────────────────────┤
│ CNN Prediction              │
│ Modulation                  │
│ Confidence                  │
└─────────────────────────────┘
```

## 14. Relationship With Evaluation

Evaluation generates model-performance visualizations such as:

```text
Confusion Matrix
Normalized Confusion Matrix
Accuracy vs SNR
```

The `visualization/` directory focuses primarily on **signal-level visualization**.

Therefore:

```text
evaluation/
    → Model performance visualization

visualization/
    → RF signal visualization
```

## 15. Future Live SDR Visualization

The intended final system can eventually connect:

```text
SDR Hardware
     ↓
Live IQ Samples
     ↓
Signal Processing
     ↓
Visualization
     +
CNN Prediction
```

This can provide a live demonstration of the RF signal identification system.

## 16. Final Demonstration Concept

The final software demonstration can display:

```text
RF/IQ Input
      ↓
┌──────────────────────────────┐
│ I/Q Waveform                 │
│ FFT Spectrum                 │
│ Constellation                │
│ Spectrogram                  │
└──────────────────────────────┘
      ↓
Improved CNN
      ↓
┌──────────────────────────────┐
│ Predicted Modulation         │
│ Confidence                   │
│ SNR                          │
└──────────────────────────────┘
```

This provides both the signal-level evidence and the AI classification result.

## 17. Summary

The `visualization/` directory provides the visual interpretation layer of the project.

It generates:

```text
I/Q Waveform
FFT Spectrum
Constellation
Spectrogram
Amplitude
Phase
```

The module is designed to work with stored IQ data now and can later be connected to live SDR data for the final project demonstration.
