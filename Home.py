import streamlit as st
from streamlit_chat import message, AvatarStyle

# Database connection
conn = st.connection('mysql', type='sql')

# Main title and introductory text with a banner
st.markdown(
    """
    <div style="text-align: center; padding: 2rem; background-color: #f3f4f6;">
        <h1 style="color: #10B981; font-size: 2.5rem; font-weight: bold; margin-bottom: 0.5rem;">
            🌍 Welcome to Lingo Chat
        </h1>
        <p style="color: #4B5563; font-size: 1.125rem;">
            Connect with people from around the world in multiple languages! Powered by Google Translate for real-time multilingual communication.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

# CTA buttons with hover effects
st.write("")
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button(
        "Create an Account",
        key="create_account",
        help="Click to create a new account and start chatting!",
    ):
        st.switch_page("pages/register.py")
    if st.button("Login", key="login", help="Login to join the chat community."):
        st.switch_page("pages/login.py")

# Features section with a more styled list
st.markdown(
    """
    <hr style='border: 1px solid #E5E7EB; margin: 2rem 0;'/>
    <div style="text-align: center;">
        <h3 style="color: #10B981; font-size: 1.75rem; font-weight: 600;">
            Features
        </h3>
        <ul style="list-style-type: none; padding: 0; font-size: 1rem; color: #6B7280; line-height: 1.75;">
            <li style="padding: 0.5rem; border-bottom: 1px solid #E5E7EB;">Chat in multiple languages seamlessly</li>
            <li style="padding: 0.5rem; border-bottom: 1px solid #E5E7EB;">Powered by Google Translate for real-time translation</li>
            <li style="padding: 0.5rem;">Connect with a global community</li>
        </ul>
    </div>
    """,
    unsafe_allow_html=True
)

# Footer with branding and hover effect on the text
st.write("")
st.markdown(
    """
    <div style="text-align: center; color: #9CA3AF; font-size: 0.875rem; padding: 1rem;">
        © 2024 Lingo Chat. Made with ❤️ by Language Lovers.
    </div>
    """,
    unsafe_allow_html=True
)
