# NumPy Data Filtering

A beginner-friendly Python project that uses **NumPy conditions** to identify values that are **above, below, or equal to a threshold**, and **Boolean indexing** to return the matching values.

## Objective

Practice Boolean indexing and numerical filtering.

## Tools Used

- Python 3
- NumPy
- Jupyter Notebook
- Streamlit (for the live demo)

## Dataset

Manually created marks of 12 students, plus a second example with daily sales values.

| Student | Marks |
|---------|-------|
| Asha | 78 |
| Ravi | 85 |
| Meena | 62 |
| Kiran | 90 |
| Swetha | 71 |
| Harsh | 89 |
| Rupesh | 70 |
| Akhil | 65 |
| Divya | 92 |
| Teja | 55 |
| Nikhil | 50 |
| Priya | 98 |

## Approach

1. **Create a NumPy array** of the marks.
2. **Write a condition** such as `marks > 70`. NumPy returns a Boolean array with `True` or `False` for every element.
3. **Use Boolean indexing:** `marks[marks > 70]` returns only the values where the condition is `True`.
4. **Try different operators and thresholds:** `>`, `<`, `>=`, `<=`, `==`, `!=`.
5. **Combine conditions** with `&` (and), `|` (or) and `~` (not), with brackets around each condition.
6. **Use the same mask on the names array** to find which students match, and `np.where()` to get their positions.
7. **Count the matches** with `np.sum()` and calculate the pass percentage with `np.mean()`.
8. **Repeat the idea on a sales dataset.**

## Sample Output

```
Condition: marks > 70
Boolean array: [ True  True False  True  True  True False False  True False False  True]
Data type: bool
Filtered values: [78 85 90 71 89 92 98]
```

Different thresholds:

```
Marks above 50: [78 85 62 90 71 89 70 65 92 55 98]  (count = 11)
Marks above 60: [78 85 62 90 71 89 70 65 92 98]  (count = 10)
Marks above 70: [78 85 90 71 89 92 98]  (count = 7)
Marks above 80: [85 90 89 92 98]  (count = 5)
Marks above 90: [92 98]  (count = 2)
```

Combined conditions:

```
60 to 79      : [78 62 71 70 65]
Below 55 or above 95: [50 98]
Outside 60 to 79    : [85 90 89 92 55 50 98]
```

Names and positions:

```
Students with marks >= 85: ['Ravi' 'Kiran' 'Harsh' 'Divya' 'Priya']
Positions: [ 1  3  5  8 11]
  Ravi: 85
  Kiran: 90
  Harsh: 89
  Divya: 92
  Priya: 98
```

## What is a Boolean Array?

A Boolean array contains only `True` and `False`. When a condition is applied to a NumPy array, NumPy checks every element and returns a Boolean array of the same shape. It acts as a **mask**: `True` means keep the value and `False` means skip it.

## What is Boolean Indexing?

Boolean indexing means using a Boolean array inside square brackets to select elements. `marks[marks > 70]` keeps only the elements where the mask is `True`. It filters the data without a loop and returns a new array, so the original array is unchanged.

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
4. Open `numpy_data_filtering.ipynb`.
5. Run all cells from top to bottom (`Shift + Enter`).

## Limitations

- Data is typed in manually.
- The Python words `and` and `or` do not work on arrays. `&` and `|` with brackets must be used.
- Only 1D arrays are used. Filtering also works on 2D arrays.

## Possible Improvements

- Filter rows of a 2D array (for example marks of several subjects).
- Read the data from a CSV file.
- Plot the filtered values with Matplotlib.

## Author

SwethaPulusu
