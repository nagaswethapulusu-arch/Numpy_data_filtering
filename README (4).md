# NumPy Array Operations

A beginner-friendly Python project that creates two NumPy arrays and performs **addition, subtraction, multiplication, and division** on them, to understand **vectorized numerical operations**.

## Objective

Understand vectorized numerical operations using NumPy.

## Tools Used

- Python 3
- NumPy
- Jupyter Notebook
- Streamlit (for the live demo)

## Dataset

Two manually created arrays of the same shape:

```python
a = np.array([10, 20, 30, 40, 50])
b = np.array([2, 4, 5, 8, 10])
```

## Approach

1. **Create the arrays** with `np.array()`.
2. **Check the shape** of both arrays with `.shape`. They must match for element-wise operations.
3. **Perform the operations directly on the arrays:** `a + b`, `a - b`, `a * b`, `a / b`.
4. **Show the same operations with NumPy functions:** `np.add()`, `np.subtract()`, `np.multiply()`, `np.divide()`.
5. **Extras:** operations with a single number (broadcasting), a shape mismatch error, safe division when the divisor contains zeros, and a speed comparison with Python lists.

## Results

| Operation | Result |
|-----------|--------|
| `a + b` | [12 24 35 48 60] |
| `a - b` | [ 8 16 25 32 40] |
| `a * b` | [ 20  80 150 320 500] |
| `a / b` | [5. 5. 6. 5. 5.] |

## Sample Output

```
Array a: [10 20 30 40 50]
Array b: [ 2  4  5  8 10]
Shape of a: (5,)
Shape of b: (5,)
Same shape: True
a + b = [12 24 35 48 60]
a - b = [ 8 16 25 32 40]
a * b = [ 20  80 150 320 500]
a / b = [5. 5. 6. 5. 5.]
```

Shape mismatch:

```
Error: operands could not be broadcast together with shapes (5,) (3,)
```

## Explanation of Vectorized Operations

**Vectorization** means applying an operation to a whole array at once without writing a loop. With `a + b`, NumPy adds the elements at the same positions: 10 + 2, 20 + 4, 30 + 5 and so on.

- Operations are **element-wise**.
- The arrays must have the **same shape** (or compatible shapes). Different shapes such as 5 and 3 raise a `ValueError`.
- Division with `/` returns **floats**, even for whole-number answers (`20 / 4 = 5.0`).
- A single number can be combined with an array (**broadcasting**): `a + 5` adds 5 to every element.
- Vectorized code is **shorter and much faster** than Python loops. NumPy runs the loop in compiled code and stores numbers in a compact block of memory. The notebook includes a timing test. Times differ from computer to computer, but NumPy is much faster.

## How to Run

1. Install Python, NumPy and Jupyter Notebook:
   ```
   pip install notebook numpy
   ```
2. Clone or download this repository.
3. Open a terminal in the project folder and run:
   ```
   python -m notebook
   ```
4. Open `numpy_array_operations.ipynb`.
5. Run all cells from top to bottom (`Shift + Enter`).

## Limitations

- Arrays are typed in manually.
- Only 1D arrays are used. NumPy also supports 2D and higher dimensions.
- Dividing by zero gives `inf` or `nan` with a warning unless it is handled (the notebook shows a safe method).

## Possible Improvements

- Use 2D arrays (matrices) and matrix multiplication with `np.dot()`.
- Add more operations such as power, modulus and square root.
- Plot the results with Matplotlib.

## Author

SwethaPulusu
