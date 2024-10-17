import streamlit as st

def main():
    st.title("Simple Calculator App")
    
    # Getting user input
    num1 = st.number_input("Enter first number:", value=0.0, format="%.2f")
    num2 = st.number_input("Enter second number:", value=0.0, format="%.2f")
    
    operation = st.selectbox("Select an operation:", ('Addition', 'Subtraction', 'Multiplication', 'Division'))
    
    # Perform the selected operation
    result = None
    if operation == 'Addition':
        result = num1 + num2
    elif operation == 'Subtraction':
        result = num1 - num2
    elif operation == 'Multiplication':
        result = num1 * num2
    elif operation == 'Division':
        if num2 != 0:
            result = num1 / num2
        else:
            st.error("Cannot divide by zero!")
    
    # Displaying the result
    if result is not None:
        st.success(f"Result: {result}")

if __name__ == "__main__":
    main()
