import streamlit as st
import numpy as np

classes={
    'A':np.array([40.39473684, 87.        , 18.63157895]),
    'B':np.array([32.69230769, 86.53846154, 82.12820513]),
    'C':np.array([44.89473684, 48.70526316, 42.63157895]),
    'D':np.array([24.82142857, 28.71428571, 74.25      ])
}

def calculate_distance(a,b):
    return sum((a-b)**2)

def f(Age,Annual_Income,Spending_Score):
    inp=np.array([Age,Annual_Income,Spending_Score])
    temp=[]
    for c in classes:
        temp.append([c,calculate_distance(classes[c],inp)])
    temp.sort(key=lambda x: x[1])
    return temp[0][0]



st.title('Assign class to customers')

# Input features
Age=st.number_input('Age')
Annual_Income=st.number_input('Annual Income (k$)')
Spending_Score=st.number_input('Spending Score (1-100)')


# Calculate output
output=f(Age,Annual_Income,Spending_Score)

# Display output
st.write('Assigned class: ', output)