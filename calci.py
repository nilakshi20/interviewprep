import streamlit as st

# Title for the app
st.title('Py Calci')

# Streamlit input fields for user interaction
operator = st.selectbox("Select an operator (+ - * /):", ["+", "-", "*", "/"])
num1 = st.number_input("Enter the 1st number:", value=0.0)
num2 = st.number_input("Enter the 2nd number:", value=0.0)

# Perform calculation and display the result when the button is pressed
if st.button("Calculate"):
    if operator == "+":
        result = num1 + num2
        st.write(f"Result: {round(result, 3)}")
    elif operator == "-":
        result = num1 - num2
        st.write(f"Result: {round(result, 3)}")
    elif operator == "*":
        result = num1 * num2
        st.write(f"Result: {round(result, 3)}")
    elif operator == "/":
        # Handle division by zero
        if num2 != 0:
            result = num1 / num2
            st.write(f"Result: {round(result, 3)}")
        else:
            st.error("Division by zero is not allowed.")
    else:
        st.error(f"{operator} is not valid")


