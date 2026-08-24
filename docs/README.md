# Project Documentation

Documentation for the **AI Based Intelligent RF Spectrum Signal Identification System**.

## Documentation Index

### Project

- [Project Overview](project_overview.md)  
  Introduction, objectives, and overall project description.

- [Workflow](workflow.md)  
  Overall workflow of the complete system.

- [Methodology](methodology.md)  
  Main methodology used for RF signal identification.

- [Progress](progress.md)  
  Development progress and completed project stages.

- [Team Responsibilities](team_responsibilities.md)  
  Responsibilities and contribution areas of the project team.

---

### Dataset & Preprocessing

- [Dataset Information](dataset_information.md)  
  RadioML dataset information and characteristics.

- [Preprocessing](preprocessing.md)  
  IQ signal preprocessing and dataset preparation.

- [Feature Extraction](feature_extraction.md)  
  Signal processing and feature extraction methods.

---

### AI Model

- [Model Architecture](model_architecture.md)  
  CNN and improved CNN architecture.

- [Training](training.md)  
  Model training process and training results.

- [Evaluation](evaluation.md)  
  Model performance evaluation and SNR analysis.

- [Prediction](prediction.md)  
  Modulation prediction and inference process.

---

### System Architecture

- [Software Architecture](software_architecture.md)  
  Software components and their relationships.

- [System Architecture](system_architecture.md)  
  Complete system-level architecture.

- [Hardware Integration](hardware_integration.md)  
  Planned SDR hardware integration.

---

## Project Flow

```text
RadioML Dataset
       ↓
Dataset Analysis
       ↓
Data Preprocessing
       ↓
Feature Extraction
       ↓
CNN Model
       ↓
Model Training
       ↓
Model Evaluation
       ↓
Signal Prediction
       ↓
Signal Visualization
       ↓
Final RF Identification System
```

## Future Hardware Flow

```text
RTL-SDR / SDR Hardware
          ↓
     RF Signal
          ↓
      IQ Samples
          ↓
    Preprocessing
          ↓
     CNN Model
          ↓
Modulation Prediction
          ↓
Confidence + Visualization
```

## Documentation Purpose

These documents provide the technical reference for understanding the dataset, preprocessing, feature extraction, CNN model, training, evaluation, prediction, system architecture, and planned hardware integration.
