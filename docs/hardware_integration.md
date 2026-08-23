# Hardware Integration

## AI Based Intelligent RF Spectrum Signal Identification System

## 1. Introduction

Hardware integration is an optional extension of the software-based RF signal identification system.

The current project is developed and validated primarily using the RadioML 2016.10a dataset.

After the software system is stable, an RTL-SDR receiver can be connected to capture live RF signals and provide IQ samples to the trained AI model.

The intended hardware workflow is:

```text
RF Environment
      ↓
Antenna
      ↓
RTL-SDR
      ↓
IQ Samples
      ↓
Signal Preprocessing
      ↓
CNN Model
      ↓
Modulation Classification
      ↓
Confidence
      ↓
Visualization
      ↓
Dashboard
```

---

## 2. Purpose of Hardware Integration

The purpose of hardware integration is to demonstrate that the trained AI model can operate on signals captured from a real RF environment.

The software-only system uses:

```text
RadioML Dataset
```

The hardware extension replaces the dataset input with:

```text
RTL-SDR Live IQ Data
```

The AI classification stage remains conceptually the same.

---

## 3. Hardware Components

A basic hardware demonstration can use:

```text
1. RTL-SDR receiver
2. Suitable antenna
3. Computer
4. USB connection
5. RF signal source
```

The computer runs the signal acquisition software, preprocessing pipeline, trained CNN, and visualization interface.

---

## 4. RTL-SDR

RTL-SDR is a low-cost software-defined radio receiver.

It can receive RF signals over a broad range of frequencies depending on the specific RTL-SDR hardware.

The RTL-SDR provides digitized signal samples that can be processed by software.

The important point for this project is:

```text
RF Signal
    ↓
RTL-SDR
    ↓
Digital IQ Samples
```

These IQ samples can then be passed to the AI processing pipeline.

---

## 5. Basic Hardware Architecture

The hardware architecture is:

```text
             RF Signal
                 │
                 ▼
              Antenna
                 │
                 ▼
             RTL-SDR
                 │
                 │ USB
                 ▼
             Computer
                 │
                 ▼
        IQ Signal Acquisition
                 │
                 ▼
          Signal Processing
                 │
                 ▼
            CNN Model
                 │
                 ▼
       Modulation Classification
                 │
          ┌──────┴──────┐
          ▼             ▼
    Modulation      Confidence
          │             │
          └──────┬──────┘
                 ▼
            Visualization
                 │
                 ▼
             Dashboard
```

---

## 6. Current Project Status

The current project is primarily software-based.

Therefore:

```text
Software Dataset Classification
        ↓
Completed

RTL-SDR Live Classification
        ↓
Future / Optional Extension
```

The hardware integration should be implemented only after the software prediction pipeline is stable.

---

## 7. Hardware Integration Strategy

The recommended development sequence is:

```text
Step 1
Complete Software Model
        ↓
Step 2
Complete Prediction Module
        ↓
Step 3
Test Prediction Using Stored IQ Data
        ↓
Step 4
Connect RTL-SDR
        ↓
Step 5
Capture IQ Data
        ↓
Step 6
Verify IQ Format
        ↓
Step 7
Prepare Live IQ Data
        ↓
Step 8
Feed Data to CNN
        ↓
Step 9
Display Prediction
        ↓
Step 10
Build Real-Time Demonstration
```

---

## 8. RF Signal Acquisition

The RTL-SDR receives an RF signal through its antenna.

The receiver is tuned to a selected center frequency.

Conceptually:

```text
Antenna
   ↓
RF Signal
   ↓
RTL-SDR Tuning
   ↓
Selected RF Band
   ↓
IQ Samples
```

The center frequency and sample rate must be selected according to the signal being observed.

---

## 9. IQ Data Acquisition

The receiver provides complex signal samples.

Each complex sample contains:

```text
I → In-phase
Q → Quadrature
```

The live data therefore follows:

```text
Complex IQ
    ↓
I + jQ
    ↓
I Component
+
Q Component
```

The AI pipeline requires the IQ data to be converted into the same general representation expected by the trained model.

---

## 10. Required Input Compatibility

The trained CNN expects:

```text
128 signal samples
×
2 channels
```

Therefore:

```text
(128, 2)
```

must be prepared before inference.

Live IQ data may initially contain many more samples:

```text
RTL-SDR
   ↓
Large IQ Buffer
   ↓
Signal Segmentation
   ↓
128-Sample Segment
   ↓
I/Q Arrangement
   ↓
(128, 2)
```

---

## 11. Signal Segmentation

RTL-SDR continuously produces samples.

The CNN cannot necessarily process an unlimited stream as one input.

Therefore, the live signal can be divided into segments.

For example:

```text
Continuous IQ Stream
────────────────────────────────────

       │────128────│
                    │────128────│
                                 │────128────│
```

Each segment can be passed independently to the CNN.

The exact segmentation strategy will depend on the final real-time implementation.

---

## 12. Sliding Window Processing

A future implementation can use a sliding window.

Conceptually:

```text
IQ Stream:

[----------------------------]

Window 1:
[128 samples]

Window 2:
    [128 samples]

Window 3:
        [128 samples]

Window 4:
            [128 samples]
```

This allows the system to continuously classify incoming signals.

---

## 13. Hardware Preprocessing

The live IQ data must be prepared using preprocessing compatible with the training data.

The basic process is:

```text
RTL-SDR IQ
     ↓
Signal Selection
     ↓
Segmentation
     ↓
Normalization
     ↓
Reshape
     ↓
(128, 2)
     ↓
CNN
```

The exact preprocessing must be validated experimentally because real hardware signals can differ from the simulated training dataset.

---

## 14. Frequency Selection

The RTL-SDR must be tuned to an appropriate center frequency.

The selected frequency depends on the signal being demonstrated.

The basic concept is:

```text
RF Spectrum
────────────────────────────────────
        │
        ▼
   Selected Center
     Frequency
        │
        ▼
      RTL-SDR
```

The project should only receive signals within the capabilities of the hardware and antenna.

---

## 15. Sample Rate

The RTL-SDR sample rate determines how many IQ samples are acquired per second.

The sample rate must be chosen according to:

- Signal bandwidth
- Desired spectrum view
- Processing capability
- USB data throughput
- Real-time requirements

A higher sample rate produces more data and therefore increases processing requirements.

---

## 16. Gain

RTL-SDR receivers generally provide adjustable gain settings.

Gain affects the received signal level.

Conceptually:

```text
Low Gain
   ↓
Weak Signal

Appropriate Gain
   ↓
Usable Signal

Excessive Gain
   ↓
Possible Saturation / Distortion
```

The gain should be adjusted experimentally for the demonstration.

---

## 17. Antenna Considerations

The antenna affects the quality of the received RF signal.

Important factors include:

- Frequency range
- Antenna type
- Location
- Orientation
- Distance from signal source
- Interference
- Physical environment

A suitable antenna should be selected for the intended demonstration frequency.

---

## 18. Live Signal Processing Pipeline

The complete live processing pipeline is:

```text
                 LIVE RF
                    │
                    ▼
                 Antenna
                    │
                    ▼
                RTL-SDR
                    │
                    ▼
              IQ Acquisition
                    │
                    ▼
             Signal Buffer
                    │
                    ▼
            Signal Segmentation
                    │
                    ▼
              Preprocessing
                    │
                    ▼
                (128, 2)
                    │
                    ▼
              Trained CNN
                    │
                    ▼
           Class Probabilities
                    │
                    ▼
          Modulation Prediction
                    │
             ┌──────┴──────┐
             ▼             ▼
       Modulation       Confidence
             │             │
             └──────┬──────┘
                    ▼
             Visualization
                    │
                    ▼
                Dashboard
```

---

## 19. Software-Hardware Boundary

The hardware is responsible for:

```text
RF Reception
      ↓
IQ Acquisition
```

The software is responsible for:

```text
IQ Processing
      ↓
CNN Classification
      ↓
Visualization
```

Therefore:

```text
HARDWARE
RTL-SDR
    ↓
IQ

SOFTWARE
IQ
 ↓
Preprocessing
 ↓
CNN
 ↓
Classification
 ↓
Dashboard
```

---

## 20. Hardware Interface

The RTL-SDR is connected to the computer using USB.

The computer runs the software required to communicate with the receiver.

A possible software stack is:

```text
RTL-SDR
   ↓
RTL-SDR Driver
   ↓
Python SDR Interface
   ↓
IQ Acquisition
   ↓
NumPy
   ↓
Signal Processing
   ↓
TensorFlow / Keras
   ↓
CNN
```

The exact RTL-SDR Python library can be selected during hardware implementation.

---

## 21. Possible Python Hardware Libraries

Depending on the final hardware setup, libraries such as the following may be considered:

```text
pyrtlsdr
SoapySDR
GNU Radio
NumPy
SciPy
```

The final project should select the library that provides reliable communication with the available RTL-SDR hardware.

---

## 22. Live Prediction Architecture

The final live prediction architecture can be:

```text
RTL-SDR
   │
   ▼
IQ Capture Module
   │
   ▼
Preprocessing Module
   │
   ▼
Prediction Module
   │
   ▼
Saved CNN
   │
   ▼
Class Mapping
   │
   ▼
Result
   │
   ├────► Modulation
   │
   ├────► Confidence
   │
   └────► Signal Visualization
```

---

## 23. Hardware Software Modules

A future hardware implementation can introduce a module such as:

```text
hardware/
└── rtl_sdr_receiver.py
```

Its responsibility can be:

```text
Connect RTL-SDR
      ↓
Configure Receiver
      ↓
Set Frequency
      ↓
Set Sample Rate
      ↓
Set Gain
      ↓
Capture IQ
```

The hardware module should provide IQ data to the existing software pipeline.

---

## 24. Separation of Hardware and AI

The AI model should not directly control RF hardware.

Instead, the architecture should remain modular:

```text
RTL-SDR Module
      ↓
IQ Data
      ↓
Preprocessing Module
      ↓
AI Model
      ↓
Prediction
```

This makes it possible to test the AI system independently using stored IQ data.

---

## 25. Software-Only Fallback

If the RTL-SDR is unavailable, the project can continue operating using stored IQ data.

```text
                 INPUT
                   │
          ┌────────┴────────┐
          ▼                 ▼
    RadioML Dataset       RTL-SDR
          │                 │
          │                 ▼
          │              Live IQ
          │                 │
          └────────┬────────┘
                   ▼
             Preprocessing
                   ↓
                  CNN
                   ↓
              Prediction
```

This is useful for development and testing.

---

## 26. Demonstration Concept

For a hardware demonstration, the system can be configured to:

```text
1. Connect RTL-SDR
2. Connect antenna
3. Tune to selected RF frequency
4. Capture IQ samples
5. Display live spectrum
6. Prepare IQ segment
7. Send segment to CNN
8. Predict modulation
9. Display confidence
10. Display signal visualization
```

The exact signal used should be selected based on legal availability and local RF conditions.

---

## 27. Important Demonstration Limitation

The trained model was developed using RadioML 2016.10a.

RadioML signals are simulated dataset signals.

A real RF signal captured by RTL-SDR may differ in:

- Sampling rate
- Carrier frequency
- Bandwidth
- Pulse shaping
- Noise
- Frequency offset
- Phase offset
- Hardware distortion
- Interference
- Signal format

Therefore, a live RTL-SDR demonstration should not automatically be considered equivalent to the dataset evaluation.

The live signal pipeline must be experimentally validated.

---

## 28. Real-Time Processing

For real-time classification, the system must process incoming samples quickly enough.

The processing loop can be:

```text
Capture IQ
    ↓
Buffer
    ↓
Preprocess
    ↓
CNN Inference
    ↓
Display Result
    ↓
Capture Next Buffer
```

Performance depends on:

- Computer CPU/GPU
- RTL-SDR sample rate
- Buffer size
- CNN inference time
- Visualization workload
- Python processing overhead

---

## 29. Real-Time Output

The final hardware demonstration can display:

```text
-----------------------------------------
LIVE RF SIGNAL IDENTIFICATION
-----------------------------------------

Center Frequency : XXXX MHz
Sample Rate      : XXXX MS/s

Detected Modulation : QPSK
Confidence          : XX.XX%

-----------------------------------------

[ Live I/Q Signal ]

[ Live FFT Spectrum ]

[ Constellation ]

[ Spectrogram ]

-----------------------------------------
```

The values shown will depend on the actual hardware configuration and received signal.

---

## 30. Hardware Safety and Legal Considerations

The RTL-SDR is primarily a receiver.

The project should only receive signals that can legally be monitored.

The demonstration should avoid transmitting unauthorized signals or interfering with licensed communication systems.

A safe demonstration can use:

- Publicly receivable signals where permitted
- Controlled laboratory signal sources
- Appropriate low-power test setups
- Signals generated within legal and safe conditions

The exact permitted frequencies and signals depend on local regulations.

---

## 31. Hardware Integration Testing

Before connecting the AI model, hardware reception should be tested separately.

### Test 1

Verify that the RTL-SDR is detected.

```text
Computer
   ↓
RTL-SDR
   ↓
Detected
```

### Test 2

Verify IQ acquisition.

```text
RTL-SDR
   ↓
IQ Samples
   ↓
NumPy Array
```

### Test 3

Verify spectrum display.

```text
IQ
 ↓
FFT
 ↓
Spectrum
```

### Test 4

Verify signal segmentation.

```text
IQ Stream
 ↓
128-Sample Segment
```

### Test 5

Verify CNN input compatibility.

```text
Segment
 ↓
(128, 2)
 ↓
CNN
```

### Test 6

Verify classification output.

```text
CNN
 ↓
Modulation + Confidence
```

---

## 32. Hardware Integration Testing Workflow

The complete testing process is:

```text
RTL-SDR Detection
       ↓
IQ Acquisition
       ↓
Signal Visualization
       ↓
Signal Segmentation
       ↓
Preprocessing
       ↓
CNN Input Validation
       ↓
Prediction
       ↓
Result Display
```

Each stage should be verified independently before combining the entire pipeline.

---

## 33. Future Hardware Enhancements

Possible future extensions include:

- Real-time spectrum scanning
- Automatic signal detection
- Multiple frequency monitoring
- Signal recording
- Signal replay in controlled environments
- SNR estimation
- Frequency estimation
- Bandwidth estimation
- Real-time alerts
- Signal database
- Live classification history

These should be implemented only after the basic live classification pipeline is stable.

---

## 34. Final Hardware Architecture

The intended complete system is:

```text
                       RF ENVIRONMENT
                              │
                              ▼
                           ANTENNA
                              │
                              ▼
                          RTL-SDR
                              │
                              ▼
                         IQ STREAM
                              │
                              ▼
                     SIGNAL PROCESSING
                              │
                              ▼
                       IQ SEGMENT
                         (128,2)
                              │
                              ▼
                     TRAINED CNN MODEL
                              │
                              ▼
                  MODULATION CLASSIFICATION
                              │
                     ┌────────┴────────┐
                     ▼                 ▼
                MODULATION         CONFIDENCE
                     │                 │
                     └────────┬────────┘
                              ▼
                       VISUALIZATION
                              │
                              ▼
                         DASHBOARD
```

---

## 35. Hardware Integration Status

Current status:

```text
Software Dataset Pipeline       ✅
CNN Model                       ✅
Model Evaluation                ✅
Prediction Pipeline             ⏳
RTL-SDR Connection              ⏳
Live IQ Acquisition             ⏳
Live Signal Preprocessing       ⏳
Live CNN Classification         ⏳
Real-Time Dashboard             ⏳
```

Hardware integration is therefore treated as a later extension after the software prediction system is completed.

---

## 36. Summary

The optional RTL-SDR integration provides a path from the software-based AI model to live RF signal classification.

The final concept is:

```text
Real RF Signal
      ↓
RTL-SDR
      ↓
IQ Samples
      ↓
Preprocessing
      ↓
128 × 2 CNN Input
      ↓
Trained CNN
      ↓
Modulation
      +
Confidence
      ↓
Visualization
      ↓
Dashboard
```

The important design principle is to keep the hardware acquisition layer separate from the AI classification layer.

This allows the trained model to be tested using both:

```text
Stored Dataset IQ
```

and, after proper validation:

```text
Live RTL-SDR IQ
```

without redesigning the complete AI system.
