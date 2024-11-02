import streamlit as st
from sqlalchemy.sql import text
import bcrypt

# Apply custom CSS styling for enhanced UI
st.markdown(
    """
    <style>
    body {
        background-color: #f9f9f9; /* Light background */
        font-family: 'Arial', sans-serif;
    }
    .header {
        text-align: center;
        color: #4CAF50; /* Theme color */
        font-size: 2.5rem;
        font-weight: bold;
        margin: 20px 0;
    }
    .input-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        margin-bottom: 20px;
    }
    .input {
        width: 100%;
        max-width: 400px; /* Maximum width for input fields */
        padding: 12px;
        border-radius: 5px;
        border: 1px solid #ddd;
        font-size: 16px;
        transition: border-color 0.3s;
    }
    .input:focus {
        border-color: #4CAF50; /* Highlight border on focus */
        outline: none;
    }
    .button {
        width: 100%;
        max-width: 400px; /* Maximum width for button */
        padding: 12px;
        border: none;
        border-radius: 5px;
        background-color: #4CAF50; /* Theme color */
        color: white;
        font-weight: bold;
        font-size: 1rem;
        cursor: pointer;
        transition: background-color 0.3s, transform 0.2s;
    }
    .button:hover {
        background-color: #45a049; /* Darker green on hover */
        transform: translateY(-2px); /* Slight lift on hover */
    }
    .error {
        color: red; /* Error message color */
    }
    .success {
        color: green; /* Success message color */
    }
    .footer {
        text-align: center;
        margin-top: 20px;
        font-size: 0.9rem;
        color: #555;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title for the registration form
st.markdown("<h1 class='header'>Register into Lingo Chat</h1>", unsafe_allow_html=True)

# Input fields with classes for styling
name = st.text_input("👤 Enter your Name", key="name_input", placeholder="Your Name", help="Please enter your full name.")
email = st.text_input("✉️ Enter your Email", key="email_input", placeholder="Your Email Address", help="Please enter a valid email address.")
password = st.text_input("🔑 Enter your Password", type='password', key="password_input", placeholder="Your Password", help="Please enter a strong password.")
confirm_password = st.text_input("🔒 Confirm Password", type='password', key="confirm_password_input", placeholder="Confirm your Password", help="Please confirm your password.")

# Submit button
submit = st.button("Register", key="register_button", help="Click to create a new account", use_container_width=True)

# Input validation function
def validateInput(field, label):
    if not field:
        st.error(f"{label} is required.")

# Form Submission Logic
if submit:
    # Validate input fields
    validateInput(name, "Name")
    validateInput(email, "Email")
    validateInput(password, "Password")
    validateInput(confirm_password, "Confirm Password")
    
    # Check if passwords match
    if password != confirm_password:
        st.error("🚫 Passwords do not match. Please try again.")
    else:
        # Hash the password before storing it
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        
        # MySQL Database connection
        conn = st.connection('mysql', type='sql')
        with conn.session as s:
            # Execute the insert statement
            result = s.execute(
                text("INSERT INTO users (name, email, password) VALUES (:name, :email, :password)"),
                {'name': name, 'email': email, 'password': hashed_password}
            )
            s.commit()
            
            # Get the last inserted row id
            last_user_id = result.lastrowid
            
        st.success("🎉 Registration successful! You can now log in.", icon="✅")
        # Store user details in session state with unique keys
        st.session_state['user_id'] = last_user_id
        st.session_state['registered_name'] = name  # Changed key name to avoid conflict
        st.session_state['registered_email'] = email  # Changed key name to avoid conflict
        
        st.switch_page("pages/chat.py")

# Footer for additional information
#st.markdown("<div class='footer'>Already have an account? <a href='pages/login.py'>Log in here</a>.</div>", unsafe_allow_html=True)
