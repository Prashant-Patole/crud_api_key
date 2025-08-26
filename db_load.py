import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.post import ImgPost, Base  # Assuming your model is in models.py

# Your DB connection string
DATABASE_URL = "postgresql://neondb_owner:npg_TQUZnR89hEzC@ep-lucky-feather-a1pm07nw-pooler.ap-southeast-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require"

# Create DB engine
engine = create_engine(DATABASE_URL)

# Create session
SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()

# Sample food names and image URLs
food_names = [
    "Pizza Margherita", "Veg Burger", "Paneer Tikka", "Chicken Biryani", "Momos",
    "Pasta Alfredo", "Chocolate Cake", "Gulab Jamun", "Ice Cream", "Sushi",
    "Caesar Salad", "Tandoori Chicken", "Spring Rolls", "Veg Sandwich", "Masala Dosa",
    "Idli Sambar", "Ramen", "Fish Curry", "Pav Bhaji", "French Fries",
    "Cheeseburger", "Hakka Noodles", "Falafel Wrap", "Shawarma", "Kebab Platter",
    "Vada Pav", "Onion Rings", "Tomato Soup", "Club Sandwich", "Dal Makhani",
    "Pesarattu", "Aloo Paratha", "Egg Curry", "Pani Puri", "Chole Bhature",
    "Malai Kofta", "Veg Pulao", "Hyderabadi Haleem", "Bhel Puri", "Dhokla",
    "Gajar Ka Halwa", "Kheer", "Rasgulla", "Modak", "Puran Poli",
    "Tacos", "Burrito", "Nachos", "Quesadilla", "Guacamole",
    "Fried Rice", "Manchurian", "Kung Pao Chicken", "Dim Sum", "Peking Duck",
    "Shahi Paneer", "Rajma Chawal", "Butter Chicken", "Palak Paneer", "Baingan Bharta",
    "Matar Paneer", "Kadhi Pakora", "Bhindi Masala", "Veg Thali", "Non-Veg Thali",
    "Stuffed Capsicum", "Veg Cutlet", "Pakora", "Samosa", "Bread Pakora",
    "Veg Momos", "Chicken Momos", "Paneer Momos", "Pasta Arrabbiata", "Lasagna",
    "Spaghetti Carbonara", "Risotto", "Focaccia", "Garlic Bread", "Bruschetta",
    "Blueberry Muffin", "Cupcake", "Brownie", "Pancakes", "Waffles",
    "Apple Pie", "Cheesecake", "Tiramisu", "Pudding", "Donut",
    "Smoothie Bowl", "Milkshake", "Cold Coffee", "Hot Chocolate", "Green Tea",
    "Masala Chai", "Filter Coffee", "Lassi", "Buttermilk", "Tender Coconut Water"
]

img_urls = [
    "https://source.unsplash.com/400x300/?pizza",
    "https://source.unsplash.com/400x300/?burger",
    "https://source.unsplash.com/400x300/?paneer",
    "https://source.unsplash.com/400x300/?biryani",
    "https://source.unsplash.com/400x300/?momos",
    "https://source.unsplash.com/400x300/?pasta",
    "https://source.unsplash.com/400x300/?cake",
    "https://source.unsplash.com/400x300/?gulabjamun",
    "https://source.unsplash.com/400x300/?icecream",
    "https://source.unsplash.com/400x300/?sushi",
    "https://source.unsplash.com/400x300/?salad",
    "https://source.unsplash.com/400x300/?tandoori",
    "https://source.unsplash.com/400x300/?springrolls",
    "https://source.unsplash.com/400x300/?sandwich",
    "https://source.unsplash.com/400x300/?dosa",
    "https://source.unsplash.com/400x300/?idli",
    "https://source.unsplash.com/400x300/?ramen",
    "https://source.unsplash.com/400x300/?fishcurry",
    "https://source.unsplash.com/400x300/?pavbhaji",
    "https://source.unsplash.com/400x300/?fries",
    "https://source.unsplash.com/400x300/?cheeseburger",
    "https://source.unsplash.com/400x300/?noodles",
    "https://source.unsplash.com/400x300/?falafel",
    "https://source.unsplash.com/400x300/?shawarma",
    "https://source.unsplash.com/400x300/?kebab",
    "https://source.unsplash.com/400x300/?vadapav",
    "https://source.unsplash.com/400x300/?onionrings",
    "https://source.unsplash.com/400x300/?soup",
    "https://source.unsplash.com/400x300/?clubsandwich",
    "https://source.unsplash.com/400x300/?dal",
    "https://source.unsplash.com/400x300/?pesarattu",
    "https://source.unsplash.com/400x300/?paratha",
    "https://source.unsplash.com/400x300/?eggcurry",
    "https://source.unsplash.com/400x300/?panipuri",
    "https://source.unsplash.com/400x300/?cholebhature",
    "https://source.unsplash.com/400x300/?kofta",
    "https://source.unsplash.com/400x300/?pulao",
    "https://source.unsplash.com/400x300/?haleem",
    "https://source.unsplash.com/400x300/?bhelpuri",
    "https://source.unsplash.com/400x300/?dhokla",
    "https://source.unsplash.com/400x300/?halwa",
    "https://source.unsplash.com/400x300/?kheer",
    "https://source.unsplash.com/400x300/?rasgulla",
    "https://source.unsplash.com/400x300/?modak",
    "https://source.unsplash.com/400x300/?puranpoli",
    "https://source.unsplash.com/400x300/?tacos",
    "https://source.unsplash.com/400x300/?burrito",
    "https://source.unsplash.com/400x300/?nachos",
    "https://source.unsplash.com/400x300/?quesadilla",
    "https://source.unsplash.com/400x300/?guacamole",
    "https://source.unsplash.com/400x300/?friedrice",
    "https://source.unsplash.com/400x300/?manchurian",
    "https://source.unsplash.com/400x300/?kungpaochicken",
    "https://source.unsplash.com/400x300/?dimsum",
    "https://source.unsplash.com/400x300/?pekingduck",
    "https://source.unsplash.com/400x300/?shahipaneer",
    "https://source.unsplash.com/400x300/?rajma",
    "https://source.unsplash.com/400x300/?butterchicken",
    "https://source.unsplash.com/400x300/?palakpaneer",
    "https://source.unsplash.com/400x300/?bainganbharta",
    "https://source.unsplash.com/400x300/?matarpaneer",
    "https://source.unsplash.com/400x300/?kadhi",
    "https://source.unsplash.com/400x300/?bhindi",
    "https://source.unsplash.com/400x300/?vegthali",
    "https://source.unsplash.com/400x300/?nonvegthali",
    "https://source.unsplash.com/400x300/?stuffedcapsicum",
    "https://source.unsplash.com/400x300/?cutlet",
    "https://source.unsplash.com/400x300/?pakora",
    "https://source.unsplash.com/400x300/?samosa",
    "https://source.unsplash.com/400x300/?breadpakora",
    "https://source.unsplash.com/400x300/?vegmomos",
    "https://source.unsplash.com/400x300/?chickenmomos",
    "https://source.unsplash.com/400x300/?paneermomos",
    "https://source.unsplash.com/400x300/?arrabbiata",
    "https://source.unsplash.com/400x300/?lasagna",
    "https://source.unsplash.com/400x300/?spaghetti",
    "https://source.unsplash.com/400x300/?risotto",
    "https://source.unsplash.com/400x300/?focaccia",
    "https://source.unsplash.com/400x300/?garlicbread",
    "https://source.unsplash.com/400x300/?bruschetta",
    "https://source.unsplash.com/400x300/?blueberrymuffin",
    "https://source.unsplash.com/400x300/?cupcake",
    "https://source.unsplash.com/400x300/?brownie",
    "https://source.unsplash.com/400x300/?pancakes",
    "https://source.unsplash.com/400x300/?waffles",
    "https://source.unsplash.com/400x300/?applepie",
    "https://source.unsplash.com/400x300/?cheesecake",
    "https://source.unsplash.com/400x300/?tiramisu",
    "https://source.unsplash.com/400x300/?pudding",
    "https://source.unsplash.com/400x300/?donut",
    "https://source.unsplash.com/400x300/?smoothiebowl",
    "https://source.unsplash.com/400x300/?milkshake",
    "https://source.unsplash.com/400x300/?coldcoffee",
    "https://source.unsplash.com/400x300/?hotchocolate",
    "https://source.unsplash.com/400x300/?greentea",
    "https://source.unsplash.com/400x300/?masalachai",
    "https://source.unsplash.com/400x300/?filtercoffee",
    "https://source.unsplash.com/400x300/?lassi",
    "https://source.unsplash.com/400x300/?buttermilk",
    "https://source.unsplash.com/400x300/?coconutwater"
]

# Generate 100 rows
for _ in range(100):
    food = random.choice(food_names)
    img = random.choice(img_urls)
    price = round(random.uniform(50, 500), 2)  # Price between 50 and 500

    description = {
        "food_name": food,
        "price": price
    }

    new_item = ImgPost(
        img=img,
        description=str(description)  # store as string, can use JSON if preferred
    )
    session.add(new_item)

# Commit all
session.commit()
session.close()

print("✅ 100 rows inserted successfully!")
