import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Function to calculate BMI
def calculate_bmi(weight, height):
    try:
        bmi = weight / (height ** 2)
        return round(bmi, 2)
    except ZeroDivisionError:
        return "Height cannot be zero."

# Function to determine BMI category and health suggestions
def get_bmi_category(bmi):
    if bmi < 18.5:
        category = 'Underweight 🦵'
        suggestion = "Try to include more nutrient-rich foods in your diet. 🍲"
    elif 18.5 <= bmi < 24.9:
        category = 'Normal weight 💪'
        suggestion = "Keep up the good work! Maintain a balanced diet and regular exercise. 🏋️‍♀️"
    elif 25 <= bmi < 29.9:
        category = 'Overweight 🐘'
        suggestion = "Consider adjusting your diet and incorporating regular physical activity. 🚶‍♀️"
    else:
        category = 'Obesity 🍔'
        suggestion = "Consult a healthcare professional for a personalized health plan. 🩺"
    return category, suggestion

# Function to display BMI result graphically
def plot_bmi_graph(bmi):
    labels = ['Underweight', 'Normal weight', 'Overweight', 'Obesity']
    values = [18.5, 24.9, 29.9, 40]

    fig, ax = plt.subplots(figsize=(10, 7))
    ax.barh(labels, values, color=['#ffcccb', '#98fb98', '#ffcc00', '#ff6347'], edgecolor='black', height=0.8)

    # Adding the BMI marker
    ax.text(bmi, 2, f'Your BMI: {bmi}', va='center', ha='left', fontsize=12, color='black', fontweight='bold')

    ax.set_xlim(0, 40)
    ax.set_title("BMI Categories 📊", fontsize=16, fontweight='bold', color='purple')
    ax.set_xlabel("BMI Value", fontsize=14, color='green')
    ax.set_ylabel("Category", fontsize=14, color='blue')

    # Adding gridlines for better clarity
    ax.grid(True, linestyle='--', alpha=0.5)

    # Make the labels stand out
    for tick in ax.get_xticklabels():
        tick.set_fontsize(12)
        tick.set_fontweight('bold')
        tick.set_color('black')

    st.pyplot(fig)

# Streamlit App
def app():
    st.set_page_config(page_title="BMI Calculator", page_icon="⚖️", layout="wide")

    st.title("⚖️ **BMI Calculator Web App** ⚖️")
    st.markdown("Welcome to the most advanced BMI Calculator! Let's get started. 🚀")

    # Display a sidebar with user info
    st.sidebar.header("👤 User Info")
    name = st.sidebar.text_input("Enter your name:")
    age = st.sidebar.number_input("Enter your age:", min_value=0, max_value=120, value=25)

    # Gender selection
    gender = st.sidebar.radio("Select Gender:", ["Male", "Female"])

    st.sidebar.subheader("📏 Enter your details:")
    weight = st.number_input("Weight (kg):", min_value=1.0, step=0.1)
    height_cm = st.number_input("Height (cm):", min_value=1.0, step=1.0)

    # Convert cm to meters
    if height_cm > 0:
        height = height_cm / 100  # Convert cm to meters

    if st.button("🔎 Calculate BMI"):
        if weight > 0 and height > 0:
            bmi = calculate_bmi(weight, height)
            category, suggestion = get_bmi_category(bmi)

            # Display the result
            st.subheader(f"Hello {name}, Your BMI is: {bmi} 🏆")
            st.write(f"Category: {category}")
            st.write(f"Suggestion: {suggestion}")

            # Plot the BMI category graph
            plot_bmi_graph(bmi)

            # Store the result in history (in memory for now)
            if "history" not in st.session_state:
                st.session_state.history = []
            st.session_state.history.append({"Name": name, "Age": age, "BMI": bmi, "Category": category})

            st.success("Your BMI calculation is complete! 🎉")
            st.write("Triggering Balloons...")
            st.balloons()
        else:
            st.error("Please enter valid weight and height values. ⚠️")

    if st.session_state.get("history"):
        st.subheader("🧾 BMI Calculation History:")
        for record in st.session_state.history:
            st.write(f"Name: {record['Name']}, Age: {record['Age']}, BMI: {record['BMI']}, Category: {record['Category']}")

    # Add a footer
    st.markdown("---")
    st.markdown("Created with ❤️ by Tayyaba Ramzan 👩🏻‍💻")

if __name__ == "__main__":
    app()
