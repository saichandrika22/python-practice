import streamlit as st

# -----------------------------
# Step 1: Menu Data (25 Items)
# -----------------------------
menu = [
    # Veg Items
    {"name": "Paneer Butter Masala", "price": 260, "type": "Veg"},
    {"name": "Dal Tadka", "price": 150, "type": "Veg"},
    {"name": "Veg Biryani", "price": 220, "type": "Veg"},
    {"name": "Mushroom Curry", "price": 240, "type": "Veg"},
    {"name": "Aloo Gobi", "price": 180, "type": "Veg"},
    {"name": "Palak Paneer", "price": 250, "type": "Veg"},
    {"name": "Veg Fried Rice", "price": 190, "type": "Veg"},
    {"name": "Paneer Tikka", "price": 270, "type": "Veg"},
    {"name": "Mixed Veg Curry", "price": 210, "type": "Veg"},
    {"name": "Masala Dosa", "price": 120, "type": "Veg"},

    # Non-Veg Items
    {"name": "Chicken Biryani", "price": 320, "type": "Non-Veg"},
    {"name": "Fish Curry", "price": 300, "type": "Non-Veg"},
    {"name": "Egg Fried Rice", "price": 200, "type": "Non-Veg"},
    {"name": "Chicken Tikka", "price": 280, "type": "Non-Veg"},
    {"name": "Mutton Curry", "price": 350, "type": "Non-Veg"},
    {"name": "Prawn Masala", "price": 370, "type": "Non-Veg"},
    {"name": "Butter Chicken", "price": 330, "type": "Non-Veg"},
    {"name": "Fish Fry", "price": 290, "type": "Non-Veg"},
    {"name": "Chicken Lollipop", "price": 250, "type": "Non-Veg"},
    {"name": "Egg Curry", "price": 180, "type": "Non-Veg"},

    # Drinks & Shakes
    {"name": "Cold Coffee", "price": 120, "type": "Drink"},
    {"name": "Mango Milkshake", "price": 130, "type": "Drink"},
    {"name": "Oreo Shake", "price": 150, "type": "Drink"},
    {"name": "Fresh Lime Soda", "price": 90, "type": "Drink"},
    {"name": "Masala Chai", "price": 60, "type": "Drink"}
]

# -----------------------------
# Step 2: Streamlit Setup
# -----------------------------
st.set_page_config(page_title="Restaurant Ordering System", page_icon="🍛", layout="centered")

st.title("🍽️ Restaurant Ordering System")
st.write("Welcome! Choose your mode, select your favorite dishes, and see your final bill instantly.")

# -----------------------------
# Step 3: Mode Selection
# -----------------------------
mode = st.radio("Choose Mode:", ("All Items", "Veg Only"))
veg_mode = mode == "Veg Only"

cart = {}

# -----------------------------
# Step 4: Display Menu by Category
# -----------------------------
# Veg Dishes
st.markdown("## 🥗 Veg Dishes")
for item in [i for i in menu if i["type"] == "Veg"]:
    col1, col2, col3, col4 = st.columns([3, 1, 1, 2])
    with col1:
        st.write(f"**{item['name']}**")
    with col2:
        st.write(f"₹{item['price']}")
    with col3:
        st.write(item["type"])
    with col4:
        qty = st.number_input(f"Qty ({item['name']})", min_value=0, max_value=10, step=1, key=item["name"])
        if qty > 0:
            cart[item["name"]] = {"quantity": qty, "price": item["price"], "subtotal": qty * item["price"], "type": item["type"]}

# Non-Veg Dishes
if not veg_mode:
    st.markdown("---")
    st.markdown("## 🍗 Non-Veg Dishes")
    for item in [i for i in menu if i["type"] == "Non-Veg"]:
        col1, col2, col3, col4 = st.columns([3, 1, 1, 2])
        with col1:
            st.write(f"**{item['name']}**")
        with col2:
            st.write(f"₹{item['price']}")
        with col3:
            st.write(item["type"])
        with col4:
            qty = st.number_input(f"Qty ({item['name']})", min_value=0, max_value=10, step=1, key=item["name"])
            if qty > 0:
                cart[item["name"]] = {"quantity": qty, "price": item["price"], "subtotal": qty * item["price"], "type": item["type"]}

# Drinks
st.markdown("---")
st.markdown("## 🥤 Drinks & Shakes")
for item in [i for i in menu if i["type"] == "Drink"]:
    col1, col2, col3, col4 = st.columns([3, 1, 1, 2])
    with col1:
        st.write(f"**{item['name']}**")
    with col2:
        st.write(f"₹{item['price']}")
    with col3:
        st.write(item["type"])
    with col4:
        qty = st.number_input(f"Qty ({item['name']})", min_value=0, max_value=10, step=1, key=item["name"])
        if qty > 0:
            cart[item["name"]] = {"quantity": qty, "price": item["price"], "subtotal": qty * item["price"], "type": item["type"]}

# -----------------------------
# Step 5: Order Summary
# -----------------------------
if st.button("🧾 Show Order Summary"):
    if not cart:
        st.warning("You haven’t added anything to your order yet!")
    else:
        total = sum(i["subtotal"] for i in cart.values())
        free_dessert = "🍨 Ice Cream" if total > 1000 else None

        st.subheader("✅ Order Summary")
        st.write("Here’s what you ordered:")

        summary_data = []
        for name, i in cart.items():
            summary_data.append([name, i["quantity"], f"₹{i['price']}", f"₹{i['subtotal']}"])
        st.table(summary_data)

        st.markdown(f"### 💰 Total: ₹{total}")
        if free_dessert:
            st.success(f"🎉 You get a free dessert: {free_dessert}!")
        else:
            st.info("Order ₹1000+ to get a free dessert 🍨")

        st.balloons()

st.caption("Made with ❤️ using Streamlit")
