import streamlit as st

# Define a function to calculate BMI
def calculate_bmi(weight, height):
    bmi = weight / (height/100)**2
    return round(bmi, 2)

# Define Streamlit app
def app():
    # Set page title
    st.set_page_config(page_title="BMI Calculator")

    # Define UI controls
    st.write("# BMI Calculator")
    name = st.text_input("Name")
    gender = st.radio("Gender", options=["Male", "Female", "Other"])
    age = st.number_input("Age", min_value=0, max_value=150, value=25)
    address = st.text_input("Address")
    hobbies = st.multiselect("Hobbies", options=["Reading", "Writing", "Traveling", "Sports"])
    weight = st.number_input("Weight (kg)", min_value=0.0, max_value=500.0, value=70.0, step=0.1)
    height = st.number_input("Height (cm)", min_value=0, max_value=300, value=170)

    # Calculate BMI on button click
    if st.button("Calculate BMI"):
        bmi = calculate_bmi(weight, height)
        st.write(f"**BMI:** {bmi}")

    # Show user details
    st.write("## User Details")
    st.write(f"**Name:** {name}")
    st.write(f"**Gender:** {gender}")
    st.write(f"**Age:** {age}")
    st.write(f"**Address:** {address}")
    st.write(f"**Hobbies:** {', '.join(hobbies)}")
    st.write(f"**Weight:** {weight} kg")
    st.write(f"**Height:** {height} cm")

# Run the Streamlit app
if __name__ == '__main__':
    app()
