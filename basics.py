import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
import time

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

# Form elements
st.title("FORMS!!!")

if "user_data" not in st.session_state:
    print("No user data found; creating new user data dictionary")
    st.session_state["user_data"] = {}
else:
    print(f"Current user data (outside context manager):")
    print(st.session_state["user_data"])

with st.form(key="user_info_form"): # This is a context manager
    # Changing these elements does not rerun the entire app
    # This is because of the with context defined above
    st.session_state["user_data"]["name"] = st.text_input("Enter your name: ") # Stores name variable from st.text_input() in name
    st.session_state["user_data"]["age"] = st.number_input("Enter your age: ", min_value=0, max_value=100)
    # Dropdown select box
    st.session_state["user_data"]["gender"] = st.selectbox("Select your gender: ", ["Male", "Female", "Choose not to say"])
    # Date input
    st.session_state["user_data"]["dob"] = st.date_input("Enter your date of birth: ", min_value=datetime(1990,1,1), max_value=datetime.now())
    # Radio button
    st.session_state["user_data"]["graduated"] = st.radio("Have you graduated?", ["Yes", "No"])
    # Check box
    st.session_state["user_data"]["agree"] = st.checkbox("Can you work full time?")
    # Multi-select
    # st.session_state["user_data"]["languages"] = st.multiselect("Select languages you are comfortable with: ", sorted(["Python", "SQL", "JavaScript", "Java", "C++", "C#", "Ruby", "R", "Scala", "Go", "Rust", "C"]))
    # Slider
    # The problem with this is that it only updates aftert the submit_button is pressed
    # The way to address this is using Streamlit's session_state and callback functions outside the form context
    # An example is found in special_form.py
    # Commenting this out for now
    # for language in st.session_state["user_data"]["languages"]:
    #     print(f"Current user data (inside context manager):\n")
    #     print(st.session_state["user_data"])
    #     print(f"Tackling {language}")
    #     if "languages" not in st.session_state["user_data"]: # No expertise dictionary created; create one now
    #         st.session_state["user_data"]["languages"] = {}
    #     if language not in st.session_state["user_data"]["languages"]:
    #         st.session_state["user_data"]["languages"][language] = 5
    #     st.session_state["user_data"]["languages"][language] = st.slider(f"Rate your expertise in {language} from 1 to 10", min_value=1, max_value=10, key=language)
    #     # expertise = st.slider(f"Rate your expertise in {language} from 1 to 10", min_value=1, max_value=10)
    # Text area
    st.session_state["user_data"]["about"] = st.text_area("Tell us about yourself: ", max_chars=200)
    # Time input
    st.session_state["user_data"]["start_time_daily"] = st.time_input("Enter your daily start time: ", datetime.now().time())
    st.session_state["user_data"]["end_time_daily"] = st.time_input("Enter your daily end time: ", datetime.now().time())
    # File uploader
    st.session_state["user_data"]["uploaded_file"] = st.file_uploader("Upload your resume (PDF or DOC(X) only): ", type=["doc", "docx", "pdf"])
    # Color picker
    st.session_state["user_data"]["swag_color"] = st.color_picker("What would be your favourite colour for swag?: ", "#ffffff")


    submit_button = st.form_submit_button(label="Submit") # Define submit button to allow form to function properly
    # The submit_button variable is None/False until the submit button is pressed
    # Once the submit button is pressed, the app is rerun and the submit_button variable holds a truthy value
    # The conditional block is then entered
    if submit_button: # Or if st.form_submit_button(label="Submit"):
        # Check to see if all form elements are filled
        # Warn if not
        if not all(key in st.session_state["user_data"] for key in ["name", "age", "gender", "dob", "graduated", "agree", "about", "start_time_daily", "end_time_daily", "uploaded_file", "swag_color"]):
            st.warning("Please fill in all the fields!")
        else:
            st.balloons() # Shows balloons cuteee
            st.write(st.session_state["user_data"]) # Display the data

# Caching

@st.cache_data(ttl=60) # Caches the following function with its exact arguments call for 60 seconds
def fetch_data(name):
    time.sleep(5)
    return {
        "name": name
    }

st.write("Fetching data")
st.write(fetch_data("Fayad")) 
# The first run takes 5 seconds because of time.sleep(5)
# Consecutive runs within a 60 second period are instantaneous

# It is also possible to cache_resource. Check sources.