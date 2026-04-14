import streamlit as st
import pandas as pd

# -------------------------------
# Page Config
# -------------------------------
st.set_page_config(page_title="WAD Assignment App", layout="wide")

# -------------------------------
# Custom Styling (UI Design)
# -------------------------------
st.markdown("""
    <style>
    .main {
        background: linear-gradient(to right, #4facfe, #00f2fe);
    }
    .title {
        text-align: center;
        color: white;
        font-size: 40px;
        font-weight: bold;
    }
    .card {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0px 5px 15px rgba(0,0,0,0.2);
    }
    </style>
""", unsafe_allow_html=True)

# -------------------------------
# Title
# -------------------------------
st.markdown('<p class="title">WAD Assignment App</p>', unsafe_allow_html=True)
st.markdown("### Manasa Gunnam (2023000055)")

# -------------------------------
# Sample Data (No JSON errors)
# -------------------------------
students_data = [
    {"student_id": 101, "name": "Aarav", "department": "CSE", "cgpa": 8.5},
    {"student_id": 102, "name": "Diya", "department": "ECE", "cgpa": 7.8},
    {"student_id": 103, "name": "Rohan", "department": "IT", "cgpa": 9.1},
    {"student_id": 104, "name": "Sneha", "department": "CSE", "cgpa": 8.2}
]

employee_data = [
    {"emp_id": 101, "emp_name": "Rahul", "department": "IT", "salary": 50000},
    {"emp_id": 102, "emp_name": "Anjali", "department": "HR", "salary": 45000},
    {"emp_id": 103, "emp_name": "Arjun", "department": "Finance", "salary": 60000}
]

# -------------------------------
# Sidebar
# -------------------------------
option = st.sidebar.selectbox(
    "Select Module",
    ["Student Records", "Employee Search", "Product App"]
)

# -------------------------------
# 1. Student Records
# -------------------------------
if option == "Student Records":
    st.markdown("## 🎓 Student Records")

    df = pd.DataFrame(students_data)
    st.dataframe(df)

    st.markdown("### Students with CGPA > 8.0")
    high = df[df["cgpa"] > 8.0]
    st.dataframe(high)

# -------------------------------
# 2. Employee Search (Like Servlet)
# -------------------------------
elif option == "Employee Search":
    st.markdown("## 🔍 Employee Search")

    emp_id = st.number_input("Enter Employee ID", min_value=1, step=1)

    if st.button("Search"):
        df = pd.DataFrame(employee_data)
        result = df[df["emp_id"] == emp_id]

        if not result.empty:
            st.success("Employee Found!")
            st.dataframe(result)
        else:
            st.error("Employee not found!")

# -------------------------------
# 3. Product App
# -------------------------------
elif option == "Product App":
    st.markdown("## 🛒 Product Management")

    if "products" not in st.session_state:
        st.session_state.products = [
            {"product_id": 1, "product_name": "Laptop", "price": 60000, "category": "Electronics", "rating": 4.5},
            {"product_id": 2, "product_name": "Shoes", "price": 2000, "category": "Fashion", "rating": 4.0}
        ]

    products = st.session_state.products
    df = pd.DataFrame(products)

    st.dataframe(df)

    # Average Rating
    st.markdown("### ⭐ Average Rating")
    st.write(round(df["rating"].mean(), 2))

    # Add Product
    st.markdown("### ➕ Add Product")

    name = st.text_input("Product Name")
    price = st.number_input("Price", min_value=0.0)
    category = st.text_input("Category")
    rating = st.slider("Rating", 0.0, 5.0, 3.0)

    if st.button("Add Product"):
        new_product = {
            "product_id": len(products) + 1,
            "product_name": name,
            "price": price,
            "category": category,
            "rating": rating
        }

        st.session_state.products.append(new_product)
        st.success("Product Added!")
        st.rerun()
