import streamlit as st
import requests
import json
import components.authenticate as authenticate

authenticate.set_auth_code()

if st.session_state["authenticated"]:
    authenticate.button_logout()
    access_token = st.session_state["access_token"]
else:
    authenticate.button_login()

# if st.session_state["authenticated"]:
st.title('View Websites')
email = st.text_input('Email', value='prad@gmail.com', disabled=True)
website = st.text_input('Website', placeholder='https://www.google.com/')
if st.button('View'):
    # url = st.secrets["get_url"]

    # payload = json.dumps({
    # "email": email,
    # "website": website
    # })
    # headers = {
    # 'Content-Type': 'application/json',
    # 'Authorization': f'Bearer {access_token}'
    # }

    # response = requests.request("GET", url, headers=headers, data=payload)
    # response = response.json()

    # formatted_response = []
    # for item in response:
    #     formatted_item = {}
    #     for key, value in item.items():
    #         if 'S' in value:
    #             formatted_item[key] = value['S']
    #         elif 'N' in value:
    #             if key in ['status_code', 'website_status']:
    #                 formatted_item[key] = int(value['N'])
    #             else:
    #                 formatted_item[key] = float(value['N'])
    #     formatted_response.append(formatted_item)
    # st.write("The times are in UTC. You can convert them to your local time zone using this website: https://www.timeanddate.com/worldclock/converter.html")
    st.write('table')

# else:
#     st.title("Please login to view this page")