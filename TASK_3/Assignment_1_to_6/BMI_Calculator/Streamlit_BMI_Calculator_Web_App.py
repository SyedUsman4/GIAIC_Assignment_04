import streamlit as st

def calculate_bmi(weight, height):
    """Calculate BMI using weight (kg) and height (m)."""
    return weight / (height ** 2)

def bmi_classification(bmi):
    """Classify the BMI into categories."""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

def main():
    # Set up the Streamlit app
    st.set_page_config(page_title="BMI Calculator", page_icon="⚖️", layout="centered")
    
    # Title and description
    st.title("⚖️ BMI Calculator")
    st.write("Calculate your Body Mass Index (BMI) and understand your weight status.")
    
    # Input fields
    weight = st.number_input("Enter your weight (kg):", min_value=1.0, max_value=300.0, step=0.1)
    height = st.number_input("Enter your height (m):", min_value=0.5, max_value=2.5, step=0.01)
    
    # Calculate BMI
    if st.button("Calculate BMI"):
        if weight > 0 and height > 0:
            bmi = calculate_bmi(weight, height)
            classification = bmi_classification(bmi)
            
            # Display results
            st.success(f"Your BMI is **{bmi:.2f}**.")
            st.info(f"Classification: **{classification}**.")
            
            # Display BMI chart for reference
            st.write("### BMI Classification Chart")
            st.write("| BMI Range       | Classification  |")
            st.write("|-----------------|-----------------|")
            st.write("| < 18.5          | Underweight     |")
            st.write("| 18.5 - 24.9     | Normal weight   |")
            st.write("| 25 - 29.9       | Overweight      |")
            st.write("| ≥ 30            | Obesity         |")
        else:
            st.error("🚨 Please enter valid weight and height values!")

if __name__ == "__main__":
    main()