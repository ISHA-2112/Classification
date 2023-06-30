# Credit_Risk_Analysis
Credit Risk is assessed by analysing the reputation of our customers. In other words, it indicates the credibility of the borrower.  

In this project, I have used a Machine Learning model to predict the likelihood of repayment.
The model makes use of customer data and provides an analysis of the risk involved.  

The data is acquired from: [Kaggle](https://www.kaggle.com/datasets/ppb00x/credit-risk-customers)  

The classes in the dataset are highly skewed. To avoid problems related to class imbalance SMOTE oversampling technique is used. 

After preprocessing the data the model is built using XGBoost Classifier.  

The accuracy of the final model is 82.50% and the confusion matrix and classification report are as follows:  
&nbsp;<br>
&nbsp;<br>
&nbsp;<br>
![confusion](https://github.com/ISHA-2112/Credit_Risk_Analysis/assets/89999331/554a85ba-f40d-496b-bcb3-f50aada95fc4)
![classification](https://github.com/ISHA-2112/Credit_Risk_Analysis/assets/89999331/cb54f28b-fdd7-450b-aaf3-69aefe8825a7)
&nbsp;<br>
&nbsp;<br>
&nbsp;<br>
<hr>
&nbsp;<br>
&nbsp;<br>
The model is then deployed using Streamlit Cloud.  
The deployed model takes in customer information and predicts if any risk is associated.  
An overview of the application:    
&nbsp;<br>
&nbsp;<br>
&nbsp;<br>  

![stream1](https://github.com/ISHA-2112/Credit_Risk_Analysis/assets/89999331/e1f90fff-3039-4747-a4f0-52050f926477)
![stream2](https://github.com/ISHA-2112/Credit_Risk_Analysis/assets/89999331/0da5a567-bcf6-4688-b2aa-1f31fc992ec6)  
&nbsp;<br>
&nbsp;<br>
<hr>
&nbsp;<br>
&nbsp;<br>
The link to the application is: [STREAMLIT_APP](https://creditriskanalysis-isha-2112.streamlit.app/)
