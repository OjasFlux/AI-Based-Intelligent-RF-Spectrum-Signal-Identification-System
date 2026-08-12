# Dataset Information

## AI Based Intelligent RF Spectrum Signal Identification System

---

## 1. Overview

This document describes the dataset used for the **AI Based Intelligent RF Spectrum Signal Identification System**.

The project uses the **RadioML 2016.10a dataset** for developing an Automatic Modulation Classification system using Artificial Intelligence and Deep Learning.

The dataset contains radio frequency signal samples generated using different modulation techniques under different Signal-to-Noise Ratio (SNR) conditions. The signals are represented using **IQ (In-phase and Quadrature) samples**.

The dataset will be used for:

- Dataset analysis
- Signal visualization
- Data preprocessing
- AI model training
- Model validation
- Model testing
- Performance evaluation

---

## 2. Selected Dataset

### Dataset Name

**RadioML 2016.10a**

RadioML is a dataset commonly used for research and experimentation in radio signal processing and Automatic Modulation Classification.

The dataset contains:

- Multiple modulation techniques
- IQ signal samples
- Different SNR conditions
- Analog and digital modulation signals

The dataset will provide the input data required for training and testing the AI model.

---

## 3. Dataset Structure

The dataset is organized based on:

- Modulation Type
- Signal-to-Noise Ratio (SNR)

The general structure is:

```text
(Modulation Type, SNR)
          |
          v
      IQ Samples
```

For example:

```text
(QPSK, 10)
     |
     v
IQ Signal Samples
```

This means that a group of IQ signal samples belongs to a specific modulation type at a particular SNR value.

---

## 4. IQ Signal Representation

RF signals are represented using **IQ samples**.

IQ consists of two components:

- **I — In-phase component**
- **Q — Quadrature component**

Together, they represent a complex signal:

```text
RF Signal
    |
    v
IQ Representation
    |
+---+---+
|       |
v       v
I       Q
```

Mathematically:

```text
Signal = I + jQ
```

Where:

- `I` is the In-phase component.
- `Q` is the Quadrature component.
- `j` represents the imaginary component.

The IQ samples will be used as the main input to the AI model.

---

## 5. Modulation Classes

The dataset contains different modulation techniques.

The expected modulation classes include:

- 8PSK
- AM-DSB
- AM-SSB
- BPSK
- CPFSK
- GFSK
- PAM4
- QAM16
- QAM64
- QPSK
- WBFM

The AI model will learn the characteristics of these modulation types and classify an unknown signal.

```text
Unknown IQ Signal
        |
        v
     AI Model
        |
        v
Predicted Modulation

BPSK / QPSK / QAM16 / QAM64 / etc.
```

---

## 6. Signal-to-Noise Ratio

**SNR** stands for **Signal-to-Noise Ratio**.

It represents the relationship between the useful signal and unwanted noise.

```text
High SNR

Signal: ██████████
Noise : ██


Low SNR

Signal: ██████
Noise : █████
```

A high SNR generally represents a cleaner signal, while a low SNR represents a signal with more noise.

Using multiple SNR levels helps the AI model learn to classify modulation types under different noise conditions.

---

## 7. Dataset Analysis

Before training the AI model, the dataset will be analyzed using Python.

The analysis will determine:

- Number of modulation classes
- Names of modulation types
- Available SNR values
- Number of SNR levels
- Number of samples
- Samples per modulation and SNR combination
- Shape of IQ data
- Total number of signals

The analysis workflow is:

```text
RadioML Dataset
       |
       v
Load Using Python
       |
       v
Extract Dataset Information
       |
       +--> Modulation Types
       |
       +--> SNR Values
       |
       +--> IQ Sample Shape
       |
       v
Calculate Dataset Statistics
```

---

## 8. IQ Sample Dimensions

The exact IQ sample dimensions will be confirmed after loading the dataset.

A typical structure is:

```text
(Number of Signals, 2, Number of IQ Samples)
```

The value `2` represents:

```text
2
|
+--> I Component
|
+--> Q Component
```

For example:

```text
(1000, 2, 128)
```

This can be interpreted as:

- `1000` → Number of signal examples
- `2` → I and Q components
- `128` → Number of samples per component

The actual dimensions will be obtained directly from the dataset.

---

## 9. Dataset Analysis Results

The following information will be filled after executing the dataset analysis program.

| Parameter | Result |
|---|---|
| Dataset Name | RadioML 2016.10a |
| Number of Modulation Classes | To be confirmed |
| Modulation Types | To be extracted |
| Number of SNR Levels | To be confirmed |
| SNR Range | To be extracted |
| IQ Sample Shape | To be extracted |
| Samples per Combination | To be confirmed |
| Total Signal Samples | To be calculated |

---

## 10. Dataset Usage in the Project

The dataset will move through the following stages:

```text
RadioML Dataset
       |
       v
Dataset Loading
       |
       v
Dataset Analysis
       |
       v
Data Preprocessing
       |
       v
Training Data + Testing Data
       |
       v
CNN Model
       |
       v
Modulation Prediction
       |
       v
Performance Evaluation
```

The dataset is the primary source of information used to train and evaluate the AI-based modulation classification system.

---

## 11. Dataset Handling

The original dataset will be kept unchanged.

The processing workflow will be:

```text
Original Dataset
       |
       v
Dataset Loader
       |
       v
Preprocessed Data
       |
       v
Training and Testing Data
```

This separation helps maintain a clear distinction between:

- Original data
- Processed data
- Experimental results

---

## 12. Role of the Dataset in AI Training

Each RF signal sample is associated with its correct modulation label.

For example:

```text
IQ Signal
    |
    v
Correct Label: QPSK
```

During training:

```text
IQ Signal + Correct Modulation Label
                |
                v
            CNN Training
                |
                v
        Learn Signal Patterns
```

After training, the system receives an unknown signal:

```text
Unknown IQ Signal
        |
        v
   Trained CNN
        |
        v
Predicted Modulation Type
```

---

## 13. Conclusion

The **RadioML 2016.10a dataset** provides the RF signal data required for the software implementation of this project.

The first technical task is to analyze and understand the dataset, including its modulation classes, SNR values, IQ sample structure, and number of signal samples.

After completing dataset analysis, the project will proceed to:

1. Data preprocessing
2. Signal visualization
3. Feature preparation
4. CNN model development
5. Model training
6. Testing and performance evaluation
