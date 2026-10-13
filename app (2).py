import numpy as np
import pandas as pd
import streamlit as st

st.title("NumPy Array Operations")
st.write("Enter two arrays (numbers separated by commas) to see addition, subtraction, multiplication and division.")


def parse(text):
    values, invalid = [], []
    for item in text.split(","):
        item = item.strip()
        if item == "":
            continue
        try:
            values.append(float(item))
        except ValueError:
            invalid.append(item)
    return values, invalid


col1, col2 = st.columns(2)
text_a = col1.text_input("Array a", value="10, 20, 30, 40, 50")
text_b = col2.text_input("Array b", value="2, 4, 5, 8, 10")

values_a, invalid_a = parse(text_a)
values_b, invalid_b = parse(text_b)

if invalid_a or invalid_b:
    st.warning("Ignored invalid values: " + ", ".join(invalid_a + invalid_b))

if len(values_a) == 0 or len(values_b) == 0:
    st.error("Please enter at least one valid number in both arrays.")
else:
    a = np.array(values_a)
    b = np.array(values_b)

    st.write(f"Shape of a: {a.shape}, shape of b: {b.shape}")

    if a.shape != b.shape:
        st.error("The arrays must have the same shape. NumPy raises a ValueError when the shapes do not match.")
        try:
            a + b
        except ValueError as error:
            st.code(f"ValueError: {error}")
    else:
        division = np.divide(a, b, out=np.full(a.shape, np.nan), where=(b != 0))
        result = pd.DataFrame({
            "a": a,
            "b": b,
            "a + b": a + b,
            "a - b": a - b,
            "a * b": a * b,
            "a / b": division,
        })
        st.table(result)
        if (b == 0).any():
            st.info("Division by zero is not possible, so those results are shown as NaN.")

        st.header("Explanation")
        st.write(
            "NumPy applies each operation to every pair of elements at once (vectorization). "
            "It is shorter than writing a loop and much faster for large arrays."
        )
