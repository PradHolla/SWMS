import streamlit as st
import requests
import json
import components.authenticate as authenticate

st.set_page_config(page_title='Serverless Website Monitoring Application', page_icon=':globe_with_meridians:', layout='wide', initial_sidebar_state='auto')

st.header('Serverless Website Monitoring Application')
st.write('This app monitors websites and sends a notification if the website is down.')

authenticate.set_st_state_vars()

# Add login/logout buttons
if st.session_state["authenticated"]:
    authenticate.button_logout()
else:
    authenticate.button_login()
