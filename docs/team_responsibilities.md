# Team Responsibilities

## AI Based Intelligent RF Spectrum Signal Identification System

---

## 1. Overview

This document defines the responsibilities of the project team for the development of the **AI Based Intelligent RF Spectrum Signal Identification System**.

The project is divided into different technical modules to allow team members to work efficiently. However, all members are expected to understand the complete project workflow and support each other during development and integration.

The current phase of the project focuses on the **software implementation** of Automatic Modulation Classification using Artificial Intelligence.

---

## 2. Project Workflow

The complete project workflow is:

```text
RadioML Dataset
       |
       v
Dataset Analysis
       |
       v
Data Preprocessing
       |
       v
IQ Signal / Feature Preparation
       |
       v
CNN Model Development
       |
       v
Model Training
       |
       v
Testing and Prediction
       |
       v
Performance Evaluation
       |
       v
Final Software System
```

Each team member will take primary responsibility for a specific part of this workflow.

---

## 3. Member 1 - Dataset and Preprocessing

### Primary Responsibility

[SINDHU](https://github.com/sindhuuujiddi-png) is responsible for understanding, loading, and preparing the RadioML dataset.

### Tasks

- Obtain the RadioML 2016.10a dataset.
- Understand the dataset structure.
- Load the dataset using Python.
- Identify modulation classes.
- Identify SNR values.
- Check IQ sample dimensions.
- Calculate dataset statistics.
- Prepare modulation labels.
- Organize the data for preprocessing.
- Split the dataset into training and testing data.

### Expected Output

```text
RadioML Dataset
       |
       v
Dataset Successfully Loaded
       |
       v
Dataset Structure Identified
       |
       v
Preprocessed Data
       |
       v
Training and Testing Data
```

---

## 4. Member 2 - Signal Analysis and Visualization

### Primary Responsibility

[RAMYA](https://github.com/shaivaramya437-ui) is responsible for analyzing and visualizing the RF IQ signals.

### Tasks

- Understand I and Q signal components.
- Plot I component waveforms.
- Plot Q component waveforms.
- Create I-Q constellation plots.
- Compare signals at different SNR levels.
- Analyze different modulation types visually.
- Explore FFT-based signal representation.
- Prepare signal visualization results.

### Expected Output

```text
IQ Samples
    |
    +--> I Signal Plot
    |
    +--> Q Signal Plot
    |
    +--> Constellation Plot
    |
    +--> FFT Analysis
    |
    v
Signal Visualization Results
```

---

## 5. Member 3 - AI Model Development

### Primary Responsibility

[SUJAN](https://github.com/OjasFlux) is responsible for developing the Artificial Intelligence model for modulation classification.

### Tasks

- Understand the CNN input requirements.
- Design the CNN architecture.
- Define convolution layers.
- Define activation functions.
- Define classification layers.
- Configure the model for multiple modulation classes.
- Compile the CNN model.
- Train the initial model.
- Monitor training and validation performance.
- Improve the model architecture if required.
- Save the trained model.

### Expected Output

```text
Prepared IQ Data
       |
       v
CNN Architecture
       |
       v
Model Training
       |
       v
Trained CNN Model
       |
       v
Saved Model
```

---

## 6. Member 4 - Testing and Performance Evaluation

### Primary Responsibility

[YOGESH](https://github.com/Yogesh077X) is responsible for testing the trained model and evaluating its performance.

### Tasks

- Load the trained model.
- Test the model using unseen signal samples.
- Generate modulation predictions.
- Calculate classification accuracy.
- Calculate precision.
- Calculate recall.
- Calculate F1-score.
- Generate a confusion matrix.
- Compare predicted and actual modulation labels.
- Prepare performance graphs.

### Expected Output

```text
Trained Model
       |
       v
Testing Data
       |
       v
Modulation Predictions
       |
       v
Performance Metrics
       |
       +--> Accuracy
       |
       +--> Precision
       |
       +--> Recall
       |
       +--> F1-Score
       |
       +--> Confusion Matrix
       |
       v
Final Evaluation Results
```

---

## 7. Project Coordination and Joint Work

The project will not be treated as four completely independent tasks.

All team members will participate in understanding the complete system.

The team will work together during:

- Project planning.
- Dataset understanding.
- Technical discussions.
- Integration of different modules.
- Testing.
- Debugging.
- Final documentation.
- Presentation preparation.

One team member may coordinate the overall workflow and work jointly with all modules to ensure that the individual components integrate correctly.

The coordination workflow is:

```text
Dataset
   |
   v
Preprocessing
   |
   v
Signal Analysis
   |
   v
AI Model
   |
   v
Testing
   |
   v
Evaluation
   |
   v
Final Integration
```

---

## 8. Collaboration Method

The team will follow a collaborative development approach.

Each member will:

1. Understand their assigned module.
2. Develop the required code or documentation.
3. Test their work.
4. Share progress with the team.
5. Help integrate their work with other modules.
6. Support other members when required.

The project should progress as one connected system rather than separate programs.

---

## 9. Daily Progress Discussion

The team should regularly discuss:

- Work completed.
- Current problems.
- Code or dataset issues.
- Dependencies between modules.
- Next tasks.
- Integration requirements.

A simple daily workflow can be:

```text
Previous Work
      |
      v
Progress Discussion
      |
      v
Identify Problems
      |
      v
Assign Next Tasks
      |
      v
Development
      |
      v
Testing
      |
      v
Update Team
```

---

## 10. Final Integration

After individual modules are completed, all components will be integrated into one complete software system.

The final integration workflow will be:

```text
RadioML Dataset
       |
       v
Dataset Loader
       |
       v
Data Preprocessing
       |
       v
Signal / Feature Preparation
       |
       v
Trained CNN Model
       |
       v
Modulation Prediction
       |
       v
Performance Evaluation
       |
       v
Final Output
```

The final system should allow a user to provide an RF IQ signal and receive the predicted modulation type along with performance information.

---

## 11. Conclusion

The responsibilities are divided to ensure efficient project development while maintaining collaboration between all team members.

Each member has a primary responsibility, but the complete project workflow will be understood and supported by the entire team.

The project will progress step by step from dataset analysis to preprocessing, signal analysis, AI model development, testing, performance evaluation, and final software integration.
