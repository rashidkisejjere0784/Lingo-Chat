import streamlit as st
from sqlalchemy.sql import text
import bcrypt

if 'message' in st.session_state:
    st.warning("Please Login before viewing the Chats")
    st.session_state.clear()
    
st.markdown(
    """
    <div style="text-align: center; padding: 1rem;">
        <h1 style="color: #10B981; font-size: 2.5rem; font-weight: bold;">
            Log in  to Lingo Chat
        </h1>
        
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <style>
    .error {
        color: red; /* Error message color */
    }
    .success {
        color: green; /* Success message color */
    }

    <style/>
    """,
    unsafe_allow_html=True
)
email = st.text_input("✉️ Enter your Email")
password = st.text_input("🔑  Enter your password", type='password')

submit = st.button("Login")

def validateInput(field, label):
    if not field:
        st.error(f"{label} is required")

if submit:
    validateInput(email, "Email")
    validateInput(password, "Password")
    
    conn = st.connection('mysql', type='sql')
    with conn.session as s:
        # Query to fetch the hashed password for the entered email
        result = s.execute(
            text("SELECT id, name, email, password FROM users WHERE email = :email"),
            {'email': email}
        )
        user = result.fetchone()
        
    if user and bcrypt.checkpw(password.encode('utf-8'), user[3].encode('utf-8')):
        # Store user details in session state upon successful login
        st.session_state['user id'] = user[0]
        st.session_state['name'] = user[1]
        st.session_state['email'] = user[2]
        
        st.success("🎉 Login successful! ", icon="✅")
        st.switch_page("pages/chat.py") # Navigate to chat page
        
    else:
        st.error("Invalid email or password. Please try again.")