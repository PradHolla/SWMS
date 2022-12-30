import streamlit as st
import requests
import json

st.set_page_config(page_title='Website Monitor', page_icon=':globe_with_meridians:', layout='wide', initial_sidebar_state='auto')
st.sidebar.title('Actions')
action = st.sidebar.radio('Options', ['Create', 'Delete', 'View'])

if action == 'Create':
    st.title('Add Website')
    email = st.text_input('Email')
    website = st.text_input('Website')
    frequency = st.number_input('Frequency (minutes)', min_value=1)
    if st.button('Add') and email and website and frequency:
        url = st.secrets["add_url"]

        payload = json.dumps({
        "email": email,
        "website": website,
        "time_freq": frequency
        })
        headers = {
        'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        st.write(response.text)

elif action == 'Delete':
    st.title('Delete Website')
    email = st.text_input('Email')
    website = st.text_input('Website')
    if st.button('Delete'):
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

elif action == 'View':
    st.title('View Websites')
    email = st.text_input('Email')
    website = st.text_input('Website')
    if st.button('View'):
        url = st.secrets["get_url"]

        payload = json.dumps({
        "email": email,
        "website": website
        })
        headers = {
        'Content-Type': 'application/json'
        }

        response = requests.request("GET", url, headers=headers, data=payload)
        st.table(response.json())
