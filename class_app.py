# import packages
import pandas as pd
import numpy as np
import pickle
import streamlit as st
from PIL import Image

# load in the model to predict on the data
pickle_in = open("lr.pkl","rb")
lr = pickle.load(pickle_in)

# define functions for user input predictions
def prediction(income, education, parent, married, female, age):

    prediction = lr.predict(
        [[income, education, parent, married, female, age]])
    if prediction == 1:
        prediction = "LinkedIn User"
    else: prediction = "Not a LinkedIn User"    
    print(prediction)
    return prediction

def probs(income, education, parent, married, female, age):

    probs = lr.predict_proba(
        [[income, education, parent, married, female, age]])
    print(probs[:,1][0])
    return round(probs[:,1][0],3)

def main():
    st.title("LinkedIn User Prediction")
    
    html_temp = """
    <div style ="background-color:powderblue;padding:5px">
    <h4 style ="color:black;text-align:center;">Please fill out the fields below to get started:</h1>
    </div>
    """
 
    st.markdown(html_temp, unsafe_allow_html = True)

    # create fields for users to populate
    income = st.selectbox("**Income level**",
                      options = ["Less than $10,000", "$10 to under $20,000", "$20 to under $30,000", 
                                 "$30 to under $40,000", "$40 to under $50,000", "$50 to under $75,000",
                                 "$75 to under $100,000", "$100 to under $150,000", "$150,000 or more"])
    if income == "Less than $10,000":
        income = 1
    elif income == "$10 to under $20,000":
        income = 2
    elif income == "$20 to under $30,000":
        income = 3
    elif income == "$30 to under $40,000":
        income = 4
    elif income == "$40 to under $50,000":
        income = 5
    elif income == "$50 to under $75,000":
        income = 6
    elif income == "$75 to under $100,000":
        income = 7
    elif income == "$100 to under $150,000":
        income = 8
    else:
        income = 9
  
    education = st.selectbox("**Education level**",
                         options = ["Less than high school (Grades 1-8 or no formal schooling)", 
                                    "High school incomplete (Grades 9-11 or Grade 12 with NO diploma)",
                                    "High school graduate (Grade 12 with diploma or GED certificate)",
                                    "Some college, no degree (includes some community college)",
                                    "Two-year associate degree from a college or university",
                                    "Four-year college or university degree",
                                    "Some postgraduate or professional schooling, no postgraduate degree (e.g. some graduate school)",
                                    "Postgraduate or professional degree"])
   
    if education == "Less than high school (Grades 1-8 or no formal schooling)":
        education = 1
    elif education == "High school incomplete (Grades 9-11 or Grade 12 with NO diploma)":
        education = 2
    elif education == "High school graduate (Grade 12 with diploma or GED certificate)":
        education = 3
    elif education == "Some college, no degree (includes some community college)":
        education = 4
    elif education == "Two-year associate degree from a college or university":
        education = 5
    elif education == "Four-year college or university degree":
        education = 6
    elif education == "Some postgraduate or professional schooling, no postgraduate degree (e.g. some graduate school)":
        education = 7
    else:
        education = 8
    
    parent = st.selectbox("**Parental status**",
                         options = ["Parent", 
                                    "Not a parent"])

    if parent == "Parent":
        parent = 1
    else:
        parent = 0
 
    married = st.selectbox("**Marital status**",
                         options = ["Married", 
                                    "Not married"])

    if married == "Married":
        married = 1
    else:
        married = 0

    female = st.selectbox("**Gender Identification**",
                         options = ["Identifies as female", 
                                    "Does not identify as female"])

    if female == "Identifies as female":
        female = 1
    else:
        female = 0

    age = st.slider(label = "**Age (note: must be 18 or older to participate)**",
                min_value = 18,
                max_value =98,
                value = 18)

    result_1 = ""
    result_2 = ""

    # create prediction button
    if st.button("Predict Now!"):
        result_1 = prediction(income, education, parent, married, female, age)
        result_2 = probs(income, education, parent, married, female, age)
    st.success("**Result**: {}".format(result_1))
    st.success("**Probability that this person uses LinkedIn**: {}".format(result_2))

if __name__=='__main__':
    main()