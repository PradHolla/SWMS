import streamlit as st
import requests
import json
import components.authenticate as authenticate

authenticate.set_auth_code()

if st.session_state["authenticated"]:
    authenticate.button_logout()
else:
    authenticate.button_login()

if st.session_state["authenticated"]:
    st.title('Delete Website')
    email = st.text_input('Email', value=st.session_state["user_info"]["email"], disabled=True)
    website = st.text_input('Website', placeholder='https://www.google.com/')
    if st.button('Delete') and email and website:
        url = st.secrets["delete_url"]

        payload = json.dumps({
        "email": email,
        "website": website
        })
        headers = {
        'Content-Type': 'application/json'
        }

        response = requests.request("DELETE", url, headers=headers, data=payload)
        st.write(response.text)

else:
    st.title("Please login to view this page")