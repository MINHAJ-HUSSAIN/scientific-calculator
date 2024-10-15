# scientific_calculator_app.py

import streamlit as st
import math

# Function definitions for calculator operations
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed!"
    return a / b

def sine(a):
    return math.sin(math.radians(a))

def cosine(a):
    return math.cos(math.radians(a))

def tangent(a):
    return math.tan(math.radians(a))

def logarithm(a):
    if a <= 0:
        return "Error: Logarithm undefined for non-positive numbers!"
    return math.log(a)

def log10(a):
    if a <= 0:
        return "Error: Logarithm undefined for non-positive numbers!"
    return math.log10(a)

def exponent(a, b):
    return math.pow(a, b)

def square_root(a):
    if a < 0:
        return "Error: Square root of negative number is not allowed!"
    return math.sqrt(a)

def factorial(a):
    if a < 0:
        return "Error: Factorial of negative number is not defined!"
    if not float(a).is_integer():
        return "Error: Factorial is only defined for integers!"
    return math.factorial(int(a))

# Streamlit App
def main():
    st.title("🧮 Scientific Calculator")
    st.write("### Perform complex mathematical calculations with ease.")

    # Sidebar for operation selection
    st.sidebar.title("Select Operation")
    operation = st.sidebar.selectbox("Choose an operation", 
                                     ("Basic Arithmetic", "Trigonometric", "Logarithmic", "Exponential", "Square Root", "Factorial"))

    result = None  # Initialize result

    if operation == "Basic Arithmetic":
        st.header("Basic Arithmetic Operations")
        operation_type = st.selectbox("Operation", ("Add", "Subtract", "Multiply", "Divide"))
        col1, col2 = st.columns(2)
        with col1:
            num1 = st.number_input("Enter first number", value=0.0, key='basic_num1')
        with col2:
            num2 = st.number_input("Enter second number", value=0.0, key='basic_num2')
        
        if st.button("Calculate Basic"):
            if operation_type == "Add":
                result = add(num1, num2)
                st.success(f"{num1} + {num2} = {result}")
            elif operation_type == "Subtract":
                result = subtract(num1, num2)
                st.success(f"{num1} - {num2} = {result}")
            elif operation_type == "Multiply":
                result = multiply(num1, num2)
                st.success(f"{num1} * {num2} = {result}")
            elif operation_type == "Divide":
                result = divide(num1, num2)
                if isinstance(result, str):
                    st.error(result)
                else:
                    st.success(f"{num1} / {num2} = {result}")
    
    elif operation == "Trigonometric":
        st.header("Trigonometric Functions")
        trig_operation = st.selectbox("Function", ("Sine", "Cosine", "Tangent"))
        angle = st.number_input("Enter angle in degrees", value=0.0, key='trig_angle')
        
        if st.button("Calculate Trigonometric"):
            if trig_operation == "Sine":
                result = sine(angle)
                st.success(f"sin({angle}°) = {result}")
            elif trig_operation == "Cosine":
                result = cosine(angle)
                st.success(f"cos({angle}°) = {result}")
            elif trig_operation == "Tangent":
                result = tangent(angle)
                st.success(f"tan({angle}°) = {result}")
    
    elif operation == "Logarithmic":
        st.header("Logarithmic Functions")
        log_operation = st.selectbox("Function", ("Natural Logarithm (ln)", "Base-10 Logarithm (log)"))
        number = st.number_input("Enter number", value=1.0, key='log_number')
        
        if st.button("Calculate Logarithm"):
            if log_operation == "Natural Logarithm (ln)":
                result = logarithm(number)
                if isinstance(result, str):
                    st.error(result)
                else:
                    st.success(f"ln({number}) = {result}")
            elif log_operation == "Base-10 Logarithm (log)":
                result = log10(number)
                if isinstance(result, str):
                    st.error(result)
                else:
                    st.success(f"log({number}) = {result}")
    
    elif operation == "Exponential":
        st.header("Exponential Functions")
        base = st.number_input("Enter base", value=2.0, key='exp_base')
        exponent_power = st.number_input("Enter exponent", value=3.0, key='exp_power')
        
        if st.button("Calculate Exponentiation"):
            result = exponent(base, exponent_power)
            st.success(f"{base} ^ {exponent_power} = {result}")
    
    elif operation == "Square Root":
        st.header("Square Root")
        number = st.number_input("Enter number", value=0.0, key='sqrt_number')
        
        if st.button("Calculate Square Root"):
            result = square_root(number)
            if isinstance(result, str):
                st.error(result)
            else:
                st.success(f"√{number} = {result}")
    
    elif operation == "Factorial":
        st.header("Factorial")
        number = st.number_input("Enter number", value=1.0, step=1.0, key='fact_number')
        
        if st.button("Calculate Factorial"):
            result = factorial(number)
            if isinstance(result, str):
                st.error(result)
            else:
                st.success(f"{int(number)}! = {result}")
    
    st.markdown("---")
    st.write("### About")
    st.write("This is a **Scientific Calculator** built with [Streamlit](https://streamlit.io/). It supports various mathematical operations to help you perform complex calculations easily.")

if __name__ == "__main__":
    main()

