# Multi-Constellation GNSS Signal Reliability Prediction and Error Enhancement Using Machine Learning

## Overview

This project presents an end-to-end framework for analyzing Multi-Constellation GNSS observations and improving positioning reliability using Machine Learning. The framework processes raw GNSS observations collected from a Javad geodetic-grade receiver, extracts signal quality features from RINEX observation files, performs statistical analysis, evaluates positioning errors under different environmental conditions, and applies supervised machine learning techniques for GNSS reliability assessment.

The project was developed as part of an internship at the **National Remote Sensing Centre (NRSC), Indian Space Research Organisation (ISRO)**.

---

## Key Features

* Multi-Constellation GNSS Data Processing
* RINEX Observation File Analysis
* Feature Extraction from Satellite Measurements
* GNSS Statistical Analysis
* Position Error Assessment
* Environmental Performance Comparison
* Machine Learning-Based Reliability Classification
* Interactive Dashboard Visualization
* Comparative Analysis under Different Signal Conditions

---

## Experimental Environments

The datasets were collected under three different environmental conditions:

* Open Sky
* Metal Plate
* Aluminium Foil

These environments simulate varying levels of signal obstruction, attenuation, and multipath effects.

---

## GNSS Constellations

The framework supports observations from:

* GPS
* GLONASS
* Galileo
* BeiDou
* NavIC
* QZSS
* SBAS

---

## Project Workflow

Raw GNSS Data Collection

↓

JPS to RINEX Conversion

↓

Observation Processing

↓

Feature Extraction

↓

Dataset Generation

↓

Statistical Analysis

↓

Position Error Analysis

↓

Machine Learning Model Training

↓

Performance Evaluation

↓

Interactive Dashboard

---

## Machine Learning Models

The following supervised learning models were implemented and evaluated:

* Random Forest
* Support Vector Machine (SVM)
* XGBoost
* LightGBM

---

## Technologies Used

### Programming Language

* Python

### GNSS Tools

* Javad GNSS Receiver
* JPS2RIN
* RTKLIB
* GeoRinex
* GNSS-Lib-Py

### Python Libraries

* Pandas
* NumPy
* Matplotlib
* Scikit-learn
* XGBoost
* LightGBM
* Streamlit

---

## Project Structure

```
GNSS-Multi-Constellation-ML
│
├── data/
│
├── scripts/
│
├── dashboard/
│
├── output/
│
├── images/
│
├── report/
│
├── requirements.txt
│
├── README.md
│
├── LICENSE
│
└── .gitignore
```

---

## Results

The proposed framework successfully analyzed GNSS observations collected under different environmental conditions and demonstrated the impact of signal degradation on positioning performance. Machine learning models effectively classified environmental conditions using extracted GNSS signal features, while the developed dashboard provided intuitive visualization of statistical metrics, satellite visibility, and positioning performance.

---

## Future Improvements

* Real-Time GNSS Reliability Prediction
* Deep Learning-Based Signal Classification
* Multi-Frequency GNSS Analysis
* GNSS + IMU Sensor Fusion
* Cloud-Based GNSS Monitoring Platform
* Real-Time Dashboard Deployment

---

## Author

**Sadhvika Nallathigala**

B.Tech – Computer Science and Engineering (Artificial Intelligence)

ICFAI Foundation for Higher Education

Intern – National Remote Sensing Centre (NRSC), ISRO
