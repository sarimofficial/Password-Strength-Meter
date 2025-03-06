import streamlit as st
import re

def check_password_strength(password):
    """Evaluate password strength and provide feedback."""
    strength = 0
    feedback = []
    
    # Check length
    if len(password) >= 12:
        strength += 3
    elif 8 <= len(password) < 12:
        strength += 2
        feedback.append("Consider using 12+ characters 🔑")
    else:
        feedback.append("Too short - use at least 8 characters ⚠️")
    
    # Check for uppercase letters
    if re.search(r'[A-Z]', password):
        strength += 1
    else:
        feedback.append("Add uppercase letters 🔠")
    
    # Check for lowercase letters
    if re.search(r'[a-z]', password):
        strength += 1
    else:
        feedback.append("Add lowercase letters 🔡")
    
    # Check for numbers
    if re.search(r'\d', password):
        strength += 1
    else:
        feedback.append("Include numbers 🔢")
    
    # Check for special characters
    if re.search(r'[^A-Za-z0-9]', password):
        strength += 2
    else:
        feedback.append("Add special characters (!@#$%^&*) 💥")

    return strength, feedback

# Streamlit interface
st.title("Password Strength Meter 🔒")

password = st.text_input("Enter your password:", type="password")

if password:
    strength, suggestions = check_password_strength(password)
    
    st.subheader("Result:")
    if strength >= 8:
        st.success("Strong Password ✅")
    elif 5 <= strength < 8:
        st.warning("Moderate Password 📉")
    else:
        st.error("Weak Password ❌")
    
    if suggestions:
        st.write("Suggestions to improve:")
        for suggestion in suggestions:
            st.markdown(f"- {suggestion}")

    # Progress bar visualization
    st.progress(strength/10)
    st.caption(f"Strength score: {strength}/10")

    # Footer
st.markdown("---")
st.write("© 2025 **Created by Muhammad Sarim **. All rights reserved.")