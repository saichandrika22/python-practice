import streamlit as st

st.title("🎓 Multi-Student Grade Calculator")

# Subjects
subjects = ["Math", "Science", "English", "Social"]

# Function to calculate total, grade, and pass/fail
def evaluate_student(marks):
    total = sum(marks)
    average = total / len(marks)
    grade = (
        "A+" if average >= 90 else
        "A" if average >= 80 else
        "B" if average >= 70 else
        "C" if average >= 60 else
        "D" if average >= 50 else
        "F"
    )
    status = "Pass" if all(mark >= 35 for mark in marks) else "Fail"
    return total, grade, status

# Input for 4 students
for i in range(1, 5):
    st.subheader(f"Student {i}")
    name = st.text_input(f"Name of Student {i}", key=f"name_{i}")
    marks = []
    for subject in subjects:
        mark = st.number_input(f"{subject} Marks", min_value=0, max_value=100, key=f"{subject}_{i}")
        marks.append(mark)

    if st.button(f"Evaluate Student {i}", key=f"btn_{i}"):
        total, grade, status = evaluate_student(marks)
        st.success(f"{name} - Total: {total} | Grade: {grade} | Status: {status}")