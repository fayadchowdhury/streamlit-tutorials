import streamlit as st

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