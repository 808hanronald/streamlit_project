#import streamlit as st
#st.title('Hello, Streamlit!')
#st.title("This is a Title")
#st.header("This is a Header")
#st.subheader("This is a Subheader")
#st.write('This is a standard text')
#st.markdown('This is a markdown showing **bold**, and *italics*')
#import pandas as pd
#df = pd.DataFrame({"A": [1,2,3], "B": [5,6,7]})
#st.dataframe(df)
## Get user name
#name = st.text_input('First Name')
## Print message with user name
#st.write(f"Hello, World!  My name is {name}!")

## Get user name
#name = st.text_input('First Name', value = 'Coding Dojo')
## Print message with user name
#st.write(f'Hello, World!,  My name is {name}!')

## If the button is pressed, print the message
#if st.button("Say hello."):
    #st.write(f'Hello, World!  My name is {name}.')

## Get date information
#date = st.date_input(label="Date of Birth")

#import datetime as dt
#date = st.date_input(label="Date of Birth", min_value = dt.date(1900,1,1),
                    #value = dt.date(2013,1,1))

## Create the selection box with all options
#season = st.selectbox('Favorite Season', ['Winter', 'Spring', 'Summer', 'Fall'])

## Add slider, text to be displayed, min value, max value and default value
#excitement = st.slider('How excited are you to learn Streamlit??  (1=Not at all; 10=Vary!',
                      #min_value = 1, max_value = 10, value = 5)


import streamlit as st
import datetime as dt  # moved all imports to the top
st.title('Hello, Streamlit!')

# Get the name
name = st.text_input("First Name", value = "Coding Dojo")
# Add Date Selection
date = st.date_input(label='Date of Birth',
                     min_value=dt.date(1900,1,1),
                     value=dt.date(2013,1,1))
# Create the select box with all options
season = st.selectbox('Favorite Season', ['Winter', 'Spring', 'Summer', 'Fall'])
# Adding user excitment
excitement = st.slider('How excited are you to learn Steamlit??  (1=Not at all; 10=Vary!)',
                     min_value = 1, max_value = 10, value = 5)
# If the button is pressed, print message
if st.button('Introduce me!'):
    st.markdown(f"""
    #### ***Hello, World!***  My name is **{name}**. 
    - I was born on **{date}**.
    - My Favorite season is **{season}**.
    - My excitement for learning streamlit is ... **{excitement}/10.**""")