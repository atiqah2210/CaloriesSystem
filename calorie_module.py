# calorie_module.py

# FOOD DATABASE (CREATIVE PART)
food_db = {
    "Nasi Lemak": 400,
    "Roti Canai": 300,
    "Fried Rice": 350,
    "Chicken Chop": 500,
    "Salad": 150,
    "Sandwich": 250,
    "Mee Goreng": 380,
    "Fruit Bowl": 120
}

# FUNCTION 1
def get_calorie(food):
    return food_db.get(food, 0)

# FUNCTION 2
def total_calories(food_list):
    return sum([get_calorie(food) for food in food_list])


# CLASS
class User:
    def __init__(self, name, age, weight, height):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height

    def bmi(self):
        return round(self.weight / ((self.height/100)**2), 2)

    # OVERLOADING
    def calorie_goal(self, target=None):
        if target is None:
            return 2000
        return target


# INHERITANCE
class HealthyUser(User):
    def calorie_goal(self, target=None):
        base = super().calorie_goal(target)
        return base - 300

    def suggestion(self):
        return "🥗 Choose low-fat food & drink more water!"