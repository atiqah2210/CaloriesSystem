# calorie_module.py

# FUNCTION 1
def calculate_calories(food_calories):
    return sum(food_calories)

# FUNCTION 2
def calorie_status(total):
    if total < 1500:
        return "Under Intake"
    elif 1500 <= total <= 2500:
        return "Normal Intake"
    else:
        return "Over Intake"


# CLASS
class User:
    def __init__(self, name, age, weight, height):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height

    # METHOD 1 (calculation)
    def bmi(self):
        return round(self.weight / ((self.height/100) ** 2), 2)

    # METHOD 2 (OVERLOADING concept guna default parameter)
    def calorie_goal(self, target=None):
        if target is None:
            return 2000  # normal default
        else:
            return target


# INHERITANCE (Subclass)
class HealthyUser(User):
    def calorie_goal(self, target=None):
        base = super().calorie_goal(target)
        return base - 300  # healthy mode (reduce calories)

    def suggestion(self):
        return "Eat more vegetables 🥗 and reduce sugar!"