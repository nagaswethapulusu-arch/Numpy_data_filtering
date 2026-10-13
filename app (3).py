import numpy as np
import pandas as pd
import streamlit as st

st.title("NumPy Data Filtering")
st.write("Enter numbers, choose a condition and a threshold, and see the Boolean array and the filtered values.")

default_text = "78, 85, 62, 90, 71, 89, 70, 65, 92, 55, 50, 98"
user_text = st.text_input("Values (separated by commas)", value=default_text)

values, invalid = [], []
for item in user_text.split(","):
    item = item.strip()
    if item == "":
        continue
    try:
        values.append(float(item))
    except ValueError:
        invalid.append(item)

if invalid:
    st.warning("Ignored invalid values: " + ", ".join(invalid))

if len(values) == 0:
    st.error("Please enter at least one valid number.")
else:
    data = np.array(values)

    mode = st.radio("Filter type", ["Single condition", "Range (between two values)"], horizontal=True)

    if mode == "Single condition":
        c1, c2 = st.columns(2)
        operator = c1.selectbox("Condition", [">", "<", ">=", "<=", "==", "!="])
        threshold = c2.number_input("Threshold", value=70.0)
        if operator == ">":
            mask = data > threshold
        elif operator == "<":
            mask = data < threshold
        elif operator == ">=":
            mask = data >= threshold
        elif operator == "<=":
            mask = data <= threshold
        elif operator == "==":
            mask = data == threshold
        else:
            mask = data != threshold
        label = f"data {operator} {threshold:g}"
    else:
        low = st.number_input("Lower limit (included)", value=60.0)
        high = st.number_input("Upper limit (excluded)", value=80.0)
        mask = (data >= low) & (data < high)
        label = f"({low:g} <= data) & (data < {high:g})"

    st.header("Boolean array")
    st.code(f"Condition: {label}\nMask: {mask}")

    st.header("Filtered values")
    filtered = data[mask]
    if len(filtered) == 0:
        st.warning("No values match this condition.")
    else:
        st.write(filtered)
    st.write(f"{int(np.sum(mask))} of {len(data)} values match ({np.mean(mask) * 100:.1f}%).")

    table = pd.DataFrame({"Value": data, "Matches": mask})
    st.table(table)

    st.header("Explanation")
    st.write(
        "The condition is applied to every element and returns a Boolean array (True or False). "
        "Using that Boolean array inside square brackets, data[mask], returns only the matching values."
    )
