# Car price prediction

<p align="center"> 
  <img src="/graphics and presentation/dataset-cover.jpg" alt="Car price prediction" height="282px" width="637">
</p>


> **Master's degree in Computer Engineering, Cybersecurity and Artificial Intelligence - University of Cagliari**

> **Artificial Intelligence**

> **Authors**: Federico Moro - Nicola Scema


***
# Table of Contents
1. [Installation](#installation)
2. [Project Goal](#project-goal)
3. [Problem Formulation](#problem-formulation)
4. [Models Overview](#model-overview)
5. [Conclusions](#conclusions)

***

## Installation

- Download the ZIP code or clone the repository with
  ```bash
  git clone https://github.com/Federico0307/AI-s_Project
  ```
- Install the requirements with

  ```bash
  pip3 install -r requirements.txt
  ```
- Run the file `ai's_project.py` to start the prediction

## Project goal

In the automotive market, accurately determining the future value of a vehicle is a complex challenge, influenced by a myriad of factors such as make, model, age, mileage, condition and market trends. Buyers and sellers often rely on subjective evaluations resulting in inconsistencies and potential disappointment in deals.

The proposed project aims to test the accuracy of a predictive model capable of estimating the future market price of a car based on a series of characteristics and technical specifications. This project could have practical applications in providing accurate and reliable predictions to support both buyers and sellers in the process of evaluating the value of cars.

## Problem formulation

The main problem addressed in this project is the need for a reliable, data-driven approach to predicting the future market price of a car. Leveraging machine learning techniques, the objective is to analyze the results of predictive models that can provide accurate estimates based on specific car attributes.

Key aspects of the problem include:

* **Data Collection**: Use of a comprehensive data set where various car attributes such as make, model, year of production, mileage, and condition are present.
  <p align="center"> 
  <img src="/graphics and presentation/dataset_example.png" alt="dataset" height="282px" width="637">
</p>

* **Data Preprocessing**: Cleaning and preprocessing the data to manage missing values, and outliers, and ensure the dataset's consistency.

* **Feature Selection**: Identifying the most significant features that influence car prices to enhance the model's accuracy and efficiency. The features that were considered are: Year, Mileage and Condition, where Condition was transformed from the original dataset by having a string type as a value and we changed it to integer to add this value to the feature calculation as well (‘Fair’:0, ‘Good’:1, ‘Excellent’:2).

* **Model Development**: Trying various machine learning algorithms (Linear Regression and Random Forest) to determine the most effective model for price prediction.

* **Model Evaluation**: Utilizing metrics such as R-squared (R²) and cross-validation to assess the predictive model's performance.

## Model Overview
For the estimation of the future price, we compared the following models:

* **Linear regression:** it is a simple yet powerful statistical method used to model the relationship between a dependent variable and one or more independent variables. The goal is to find the best-fitting line (or hyperplane in multiple dimensions) that predicts the dependent variable based on the independent variables

  The reasons that led us to consider this model for our project are: simplicity, linear regression is easy to implement and interpret and it provides a good basis for understanding relationships between features. Speed, is computationally less intensive than more   
  complex models, making it suitable for small to medium-sized datasets. Linearity, the model assumes a linear relationship between the dependent variable (price) and the independent variables (features), which is often a good initial approximation.

* **Random Forest:** this model is a versatile and powerful ensemble learning method used for classification and regression tasks. It operates by constructing many decision trees during training and outputting the mode of the classes (classification) or mean prediction (regression) of the individual trees. This method leverages both bootstrapping (sampling with replacement) and feature randomness (considering a random subset of features at each split) to create a diverse set of trees.

  The reasons that led us to consider this model for our project are: multiple decision trees that in this model construct a series of decision trees during training and produce the average of the tree predictions to obtain a final prediction. This approach reduces   
  variance and improves robustness compared to individual decision trees. Robustness and stability, due to the combination of multiple trees and random feature selection, the Random Forest tends to be less sensitive to noisy data and outliers than single decision trees.   Interpretability, Although less interpretable than single trees, the Random Forest provides feature relevance, which can be used to understand which variables contribute most to predictions.

## Conclusions

In conclusion, we present the results obtained. For greater completeness, and a more accurate comparison, in addition to evaluating the performance of the two models tested through cross-validation. 

Generally, the results were very good and correlated with all the evaluation methods tested. The best results were obtained with the Linear Regression model where we obtained a value for R Squared Error of 0.9999999997824319 and in the cross-validation [1. 1. 1. 1. 1.] while for the Random Forest model, we obtained slightly lower results than for the Linear Regression, R Squared error 0.9995321269374119 and cross-validation [0.99490502 0.99486784 0.99325442 0.9949444 0.99378503].

<p align="center"> 
  <img src="/graphics and presentation/linear_regression_ev.png" alt="Linear Regression" height="450px" width="450px">
  <img src="/graphics and presentation/random_forest_ev.png" alt="Random Forest" height="450px" width="450px">
</p>


  

