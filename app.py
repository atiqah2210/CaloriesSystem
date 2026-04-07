import streamlit as st
from calorie_module import food_db, total_calories, User, HealthyUser

st.set_page_config(page_title="Smart Calorie Tracker", layout="centered")

st.title("🍱 Smart Food Calorie Tracker")
st.write("Select your meals and track calories easily!")

# USER INFO
name = st.text_input("Name")
age = st.number_input("Age", min_value=1)
weight = st.number_input("Weight (kg)", min_value=1.0)
height = st.number_input("Height (cm)", min_value=1.0)

mode = st.selectbox("Mode", ["Normal", "Healthy"])

st.markdown("---")

# FOOD SELECTION (CREATIVE)
st.subheader("🍽️ Select Your Meals")

breakfast = st.selectbox("Breakfast", list(food_db.keys()))
lunch = st.selectbox("Lunch", list(food_db.keys()))
dinner = st.selectbox("Dinner", list(food_db.keys()))
snack = st.selectbox("Snack", list(food_db.keys()))

target = st.number_input("Target Calories (optional)", min_value=0)

# BUTTON
if st.button("Calculate Calories 🔥"):
    try:
        if name == "":
            raise ValueError("Name is required!")

        food_list = [breakfast, lunch, dinner, snack]

        # OBJECT
        if mode == "Normal":
            user = User(name, age, weight, height)
        else:
            user = HealthyUser(name, age, weight, height)

        total = total_calories(food_list)

        # GOAL (OVERLOADING)
        if target == 0:
            goal = user.calorie_goal()
        else:
            goal = user.calorie_goal(target)

        bmi = user.bmi()

        st.success(f"Hello {name} 👋")
        st.write(f"🔥 Total Calories: {total}")
        st.write(f"🎯 Goal: {goal}")
        st.write(f"💪 BMI: {bmi}")

        # STATUS + PROGRESS
        progress = min(total / goal, 1.0)
        st.progress(progress)

        if total < goal:
            st.info("Good! You are under your calorie goal 👍")
        else:
            st.warning("You exceeded your calorie goal ⚠️")

        if mode == "Healthy":
            st.success(user.suggestion())

    except ValueError as e:
        st.error(e)

    except Exception:
        st.error("Unexpected error occurred!")