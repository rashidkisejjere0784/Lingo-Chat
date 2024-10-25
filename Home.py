import streamlit as st
from streamlit_chat import message, AvatarStyle

# Database connection
conn = st.connection('mysql', type='sql')



# Main title and introductory text with a banner
st.markdown(
    "<h1 style='text-align: center; color: #4CAF50;'>🌍 Welcome to Lingo Chat</h1>",
    unsafe_allow_html=True
)
st.markdown(
    "<p style='text-align: center; color: #333; font-size: 18px;'>"
    "Connect with people from around the world in multiple languages! "
    "Powered by Google Translate for real-time multilingual communication.</p>",
    unsafe_allow_html=True
)

# CTA button to create an account or login
st.write("")
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("Create an Account", key="create_account", help="Click to create a new account and start chatting!"):
        st.switch_page("pages/register.py")
    if st.button("Login", key="login", help="Login to join the chat community."):
        st.switch_page("pages/login.py")
    

# Section for key features
st.markdown(
    """
    <hr style='border: 1px solid #ddd;'/>
    <h3 style='text-align: center; color: #4CAF50;'>Features:</h3>
    <ul style='font-size: 16px; color: #555;'>
        <li>Chat in multiple languages seamlessly</li>
        <li>Powered by Google Translate for real-time translation</li>
        <li>Connect with a global community</li>
    </ul>
    """, unsafe_allow_html=True
)

# Footer information or branding
st.write("")
st.markdown(
    "<p style='text-align: center; color: #888;'>© 2024 Lingo Chat. Made with ❤️ by Language Lovers.</p>",
    unsafe_allow_html=True
)
