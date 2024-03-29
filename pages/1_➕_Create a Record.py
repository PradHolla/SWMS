import streamlit as st
import requests
import json
import components.authenticate as authenticate

authenticate.set_auth_code()

if st.session_state["authenticated"]:
    authenticate.button_logout()
else:
    authenticate.button_login()

# if st.session_state["authenticated"]:
st.title('Add Website')
email = st.text_input('Email', value='prad@gmail.com', disabled=True)
website = st.text_input('Website', placeholder='https://www.google.com/')
frequency = st.number_input('Frequency (minutes)', value=5, min_value=1)
if st.button('Add'):
    # url = st.secrets["add_url"]

    # payload = json.dumps({
    # "email": email,
    # "website": website,
    # "time_freq": frequency
    # })
    # headers = {
    # 'Content-Type': 'application/json'
    # }

    # response = requests.request("POST", url, headers=headers, data=payload)
    st.write('Success')

# else:
#     st.title("Please login to view this page")