import streamlit as st

st.title("Experimenting with layout elements")

# Sidebar layout
# st.sidebar.<insert whatever element>
st.sidebar.title("Sidebar")
st.sidebar.header("This is the sidebar header")
st.sidebar.write("This is the sidebar")
sidebar_input = st.sidebar.text_input("Enter something in the sidebar")

# Tabs layout
tabs = st.tabs(["First tab", "Second tab", "Third tab"])

# To put content within a tab, use the with context manager
with tabs[0]:
    st.title("First tab")
    st.write("This is the first tab")

with tabs[1]:
    st.title("Second tab")
    st.write("This is the second tab")

with tabs[2]:
    st.title("Third tab")
    st.write("This is the third tab")

# Columns layout
cols = st.columns(3)

# Similar way to access elements within a column
with cols[0]:
    st.title("First column")
    st.write("This is the first column")

with cols[1]:
    st.title("Second column")
    st.write("This is the second column")

with cols[2]:
    st.title("Third column")
    st.write("This is the third column")

# Containers
with st.container(border=True):
    st.subheader("This is a subheader for a container")
    st.divider()
    st.write("This is within a container")
    st.write("This is also within a container")
    st.write("Containers are logical groupings of elements")

# Empty placeholder
placeholder = st.empty() # Can be converted to any element
placeholder.write("This is an empty placeholder")

if st.button(label="Update placeholder"):
    # placeholder.header("This is an updated placeholder")
    placeholder.image("static/cat.png")

# Expander
# Whatever is within an expander is also within a container
with st.expander("Click to expand"):
    st.image("static/cat.png")
    st.write("This is within an expander")
    st.write("Expander is a collapsible container")

if st.button(label="Hover over me for help", help="Haha no help here lmao"):
    st.write("I see you've made it")

# Handling sidebar input
if sidebar_input:
    st.write(sidebar_input)