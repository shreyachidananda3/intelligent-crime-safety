# Intelligent Crime & Safety Recommendation System

A machine-learning based system for analyzing NYC crime patterns and generating data-driven safety insights from historical crime records.

## Overview

This project analyzes NYC crime data using Python and machine-learning techniques to identify spatial and temporal crime patterns.

The system performs data preprocessing, exploratory analysis, crime clustering, predictive modeling, and recommendation generation based on location and time.

The goal is to demonstrate how data science and machine learning can be applied to cybersecurity, public safety, and risk-analysis problems.

## Key Features

* NYC crime data preprocessing and cleaning
* Crime pattern analysis by borough, time, and crime type
* Temporal feature engineering
* Spatial and temporal K-Means clustering
* XGBoost crime-category prediction
* Location- and time-based safety insights
* Automated data visualizations
* Modular Python-based architecture
* Local execution without paid cloud services

## System Architecture

```text
NYC Crime Dataset
        |
        v
Data Preprocessing
        |
        v
Feature Engineering
        |
        +--------------------+
        |                    |
        v                    v
Crime Pattern Analysis   K-Means Clustering
        |                    |
        |                    v
        |              Spatial/Time Patterns
        |                    
        v
XGBoost Prediction
        |
        v
Safety Recommendation Engine
        |
        v
Data-Driven Safety Insights
```

## Machine Learning Approach

### K-Means Clustering

K-Means clustering is used to identify groups of crime records based on:

* Latitude
* Longitude
* Hour of day

The resulting clusters represent recurring spatial and temporal patterns in the analyzed dataset.

### XGBoost Prediction

An XGBoost classification model is used to predict the reported crime law category using features including:

* Borough
* Hour
* Month
* Latitude
* Longitude

The model is evaluated using a separate test set to measure classification performance.

## Safety Recommendation

The recommendation component analyzes crime activity for a selected borough and requested hour.

It identifies:

* Reported crime activity around the requested time
* Common crime types during that period
* Relative activity levels within the analyzed sample

The system provides a data-driven insight rather than claiming that a location is inherently safe or unsafe.

## Data
