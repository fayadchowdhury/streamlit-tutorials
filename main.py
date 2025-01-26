import streamlit as st
import pandas as pd
import numpy as np

# Will write anything that we give it
# Also performs necessary formatting
st.write("Hello, world! This is my first Streamlit app!")
st.write(
    {
        "key1": "value1",
        "key2": 2
    }
)
st.write([1, 2, 3, 4, 5])
st.write(True)

# Streamlit also evaluates and renders expressions
3+5

# Any time there is a change in the file, the entire file is run from top to bottom
pressed = st.button("First button")
if pressed:
    st.write("You pressed the first button!")

pressed = st.button("Second button")
if pressed:
    st.write("You pressed the second button!")

# With the above setup, if you hit the first button, it says "You pressed the first button!"
# But then if you hit the second button, it removes the "You pressed the first button!" and
# says "You pressed the second button!" instead
# This is because the entire app code gets run and the buttons are re-initialized
# with just the second button being pressed

# Text elements
st.title("Title")
st.header("Header")
st.subheader("Subheader")
st.markdown("This is **Markdown** text") # Works with all kinds of markdown
st.caption("Caption")
st.code("print('Hello, world!')") # Code block
st.divider() # Horizontal line

# Images
st.image("static/cat.png") # Also possible to set width with width parameter

# Data display
data = pd.DataFrame(
    {
        "Name": ["Alice", "Bob", "Charlie", "David"],
        "Age": [23, 34, 45, 56],
        "Occupation": ["Engineer", "Doctor", "Artist", "Chef"]
    }
)
st.dataframe(data) # Displays data in a table

editable_df = st.data_editor(data) # Allows editing of the data
print(editable_df) # This will print the edited data after rerunning the entire script

st.table(data) # Displays data in a table

st.metric("Metric", 100) # Displays a metric
st.metric("Number of rows", data.shape[0])

sample_dict = {
    "name": "Alice",
    "age": 23,
    "skills": ["Python", "SQL", "ML"]
}

st.json(sample_dict) # Displays JSON data, can also be achieved with st.write()

# Chart elements

data = pd.DataFrame(
    {
        "A": np.random.randn(20),
        "B": np.random.randn(20),
        "C": np.random.randn(20),
    }
)

# Area chart
st.area_chart(data)

# Bar chart
st.bar_chart(data)

# Line chart
st.line_chart(data)

# Scatter plot
scatter_data = pd.DataFrame(
    np.random.randn(20, 2),
    columns=["A", "B"]
)
st.scatter_chart(scatter_data)

# Map element
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4], # co-ordinates around SF
    columns=["lat", "lon"]
)

st.map(map_data)

# It is also possible to do matplotlib.pyplot charts but they look mad ugly