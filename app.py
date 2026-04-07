import streamlit as st
from calorie_module import calculate_calories, calorie_status, User, HealthyUser

st.set_page_config(page_title="Calorie System", layout="centered")

st.title("🍽️ Daily Food Calorie Calculator")
st.write("Track your daily calorie intake easily!")

# INPUT
name = st.text_input("Enter your name")
age = st.number_input("Enter age", min_value=1)
weight = st.number_input("Weight (kg)", min_value=1.0)
height = st.number_input("Height (cm)", min_value=1.0)

food1 = st.number_input("Food 1 Calories", min_value=0)
food2 = st.number_input("Food 2 Calories", min_value=0)
food3 = st.number_input("Food 3 Calories", min_value=0)

mode = st.selectbox("Select Mode", ["Normal", "Healthy"])

target = st.number_input("Optional Target Calories (0 = default)", min_value=0)

# BUTTON
if st.button("Calculate"):

    try:
        if name == "":
            raise ValueError("Name cannot be empty!")

        foods = [food1, food2, food3]

        # OBJECT
        if mode == "Normal":
            user = User(name, age, weight, height)
        else:
            user = HealthyUser(name, age, weight, height)

        total = calculate_calories(foods)
        status = calorie_status(total)

        # Overloading usage
        if target == 0:
            goal = user.calorie_goal()
        else:
            goal = user.calorie_goal(target)

        bmi = user.bmi()

        # OUTPUT
        st.success(f"Hello {user.name} 👋")
        st.write(f"🔥 Total Calories: {total}")
        st.write(f"📊 Status: {status}")
        st.write(f"🎯 Calorie Goal: {goal}")
        st.write(f"💪 BMI: {bmi}")

        if mode == "Healthy":
            st.info(user.suggestion())

    except ValueError as e:
        st.error(f"Error: {e}")

    except Exception as e:
        st.error("Something went wrong!")