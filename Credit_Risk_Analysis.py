import streamlit as st
import xgboost as xgb
import pandas as pd

def load():
    model = xgb.XGBClassifier()
    model.load_model('xgb.json')
    return model
model = load()

st.header('Enter the information of the client:')

checking_status =st.selectbox('Status of existing checking account:',  ['0<=amount<200', '<0', '>=200', 'no checking'])

duration = st.number_input('Loan Duration:', min_value=4.0, max_value=60.0, value=4.0)

credit_amount = st.number_input('Credit amount:', min_value=250.0, max_value=18424.0, value=250.0)

installment_commitment = st.number_input('Number of committed installments:', min_value=1.0, max_value=4.0, value=1.0)

residence_since = st.number_input('Number of years residing in the given address:', min_value=1.0, max_value=30.0, value=1.0)

age = st.number_input('Age:', min_value=19.0, max_value=75.0, value=19.0)

existing_credits = st.number_input('Existing Credit Points:', min_value=1.0, max_value=4.0, value=1.0)

num_dependents = st.number_input('Number of dependent people:', min_value=1.0, max_value=8.0, value=1.0)

credit_history = st.selectbox('Credit History:',['all paid', 'critical/other existing credit', 'delayed previously', 'existing paid', 'no credits/all paid'])

purpose = st.selectbox('Purpose of Loan:',['business', 'domestic appliance', 'education', 'furniture/equipment', 'new car', 'other', 'radio/tv', 'repairs', 'retraining', 'used car'])

savings_status = st.selectbox('Savings Status:',['100<=amount<500', '500<=amount<1000', '<100', '>=1000', 'no known savings'])

employment =  st.selectbox('Years of Employment:',['1<=years<4', '4<=years<7', '<1', '>=7', 'unemployed'])

job = st.selectbox('Job type:',['high qualified/self employed', 'skilled', 'unemployed', 'unskilled resident'])

own_telephone = st.selectbox('Do you have a telephone:',['none', 'yes'])

foreign_worker = st.selectbox('Are you a foreign worker:',['no', 'yes'])


map1 = [checking_status,
credit_history,
purpose,
savings_status,
employment,
job,
own_telephone,
foreign_worker,]

mapper = [['0<=amount<200', '<0', '>=200', 'no checking'],
['all paid', 'critical/other existing credit', 'delayed previously', 'existing paid', 'no credits/all paid'],
['business', 'domestic appliance', 'education', 'furniture/equipment', 'new car', 'other', 'radio/tv', 'repairs', 'retraining', 'used car'],
['100<=amount<500', '500<=amount<1000', '<100', '>=1000', 'no known savings'],
['1<=years<4', '4<=years<7', '<1', '>=7', 'unemployed'],
['high qualified/self employed', 'skilled', 'unemployed', 'unskilled resident'],
['none', 'yes'],
['no', 'yes']]

def encode(var,pos):
    for j in mapper[pos]:
        if var == j:
            return mapper[pos].index(j)



checking_status = encode(checking_status,0)
print(checking_status)
credit_history = encode(credit_history,1)
purpose = encode(purpose,2)
savings_status = encode(savings_status,3)
employment = encode(employment,4)
job = encode(job,5)
own_telephone = encode(own_telephone,6)
foreign_worker = encode(foreign_worker,7)
        
data = [[checking_status, duration, credit_history, purpose,
       credit_amount, savings_status, employment,
       installment_commitment, residence_since, age, existing_credits,
       job, num_dependents,own_telephone, foreign_worker]]

col = ['checking_status', 'duration', 'credit_history', 'purpose',
       'credit_amount', 'savings_status', 'employment',
       'installment_commitment', 'residence_since', 'age', 'existing_credits',
       'job', 'num_dependents', 'own_telephone', 'foreign_worker']
x = pd.DataFrame(data = data, columns = col, index = [0])
#print(x)

class1 = {
    1:'SAFE',
    0:'RISKY'
}

if st.button('Predict'):
    price = model.predict(x)
    print(price)
    if price[0] == 1:
        st.success('It is SAFE to give loan to this client')
    else:
        st.error('It is RISKY to give loan to this client')

