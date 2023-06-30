# Credit_Risk_Analysis
Credit Risk is assesed by analysing the reputation of our customer.   
In other words, it indicates the credibility of the borrower.  

In this project I have used a Machine Learning model to predict how likelihood of repayment.
The model makes use of customer data and provides an analysis of the risk involved.  

The data is acquired from: [DATASET](https://www.kaggle.com/datasets/ppb00x/credit-risk-customers) 
The classes in the dataset are highly skewed. To avoid problems related to class imbalance SMOTE oversampling technique is used.   
After preprocessing the data the model is built using XGBoost Classifier.  
The accuracy of the final model is 82.50% and the confusion matrix and classification report are as follows:  
![confusion](https://github.com/ISHA-2112/Credit_Risk_Analysis/assets/89999331/7e3b3b0e-6646-4e01-9693-cf5095956eb9)
![classification](https://github.com/ISHA-2112/Credit_Risk_Analysis/assets/89999331/6bd1bcdd-96cb-4183-bf72-bbff4fa16227)

The model is then deployed using Streamlit Cloud.  
The deployed model takes in customer information and predicts if risk is associated.  
An overview of the application:  
![stream1](https://github.com/ISHA-2112/Credit_Risk_Analysis/assets/89999331/e1f90fff-3039-4747-a4f0-52050f926477)
![stream2](https://github.com/ISHA-2112/Credit_Risk_Analysis/assets/89999331/0da5a567-bcf6-4688-b2aa-1f31fc992ec6)
