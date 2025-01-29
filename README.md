# Streamlit Basics

## Overview
This project is a demonstration of basic Streamlit concepts using Poetry for dependency management. The project structure includes multiple scripts showcasing different Streamlit functionalities, including basic UI elements, layout management, special form handling, and a multi-page application.

## Installation
To set up the project, follow these steps:

1. Clone the repository.
2. Install dependencies using Poetry:
   ```sh
   poetry install
3. Run the application using:
    ```sh
    poetry run streamlit <name_of_file>.py

## Project Structure

### basics.py

This script includes fundamental Streamlit elements such as:
- Text display (st.write, st.text, st.markdown)
- Interactive widgets (st.button, st.checkbox, st.radio)
- Data display (st.table, st.dataframe)

### layout.py

This script focuses on layout management using:
- st.columns for side-by-side components
- st.expander for collapsible sections
- st.sidebar for navigation and settings

### special_form.py

This script demonstrates a special form layout with:
- st.form for grouping multiple inputs
- st.form_submit_button for handling form submission
- Various input fields like st.text_input, st.slider, and st.selectbox

### main.py and pages/ Directory

This part of the project implements a multi-page Streamlit app. It includes:
- A main landing page (main.py)
- Additional pages inside the pages/ directory, allowing modular content and navigation
- Streamlit’s built-in st.page_link and st.navigation with st.Page for seamless multi-page integration

## Reference Materials

This project is primarily based on the concepts explained in the following resources:
- A tutorial video by Tech With Tim: [Watch here](https://youtu.be/o8p7uQCGD0U?si=y8syabtiHGXMJoJH)
- [Streamlit official documentation](https://docs.streamlit.io) - The API reference section is particularly useful
- Some code snippets were generated using GitHub Copilot Autocomplete for efficiency.

## Conclusion

This project provides a structured approach to understanding and implementing Streamlit applications using Poetry. It covers essential UI elements, layout management, form handling, and multi-page app development.