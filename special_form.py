import streamlit as st
from datetime import datetime

# Form elements
st.title("FORMS!!!")

# Create a sort of user_data object store in session_state
if "user_data" not in st.session_state:
    print("No user data found; creating new user data dictionary")
    st.session_state["user_data"] = {}

if "step" not in st.session_state:
    st.session_state["step"] = "entry"

def update_step(step):
    st.session_state["step"] = step
    if step == "exit":
        st.balloons()
    if step == "entry":
        st.session_state["user_data"] = {}

if st.session_state["step"] == "entry":
    # Check to see if "languages" key exists in st.session_state["user_data"]
    if "languages" in st.session_state["user_data"]:
        # On first run, by the time the program reaches here:
        # user_data is created
        # After a language is picked and the program reaches here:
        # user_data["languages"] exists
        # selected languages are added to the dictionary with slider value
        # After slider updates and the program reaches here:
        # old slider value still present until line 31 is reached
        # This is why line 33 prints the updated value as it updates
        # and line 23 prints it 1 step behind
        st.write(f"Languages that you are comfortable with")
        for lang in st.session_state["user_data"]["languages"]:
            st.write(f"{lang}: {st.session_state['user_data']['languages'][lang]} out of 10")

    languages = st.multiselect("Select languages you are comfortable with: ", sorted(["Python", "SQL", "JavaScript", "Java", "C++", "C#", "Ruby", "R", "Scala", "Go", "Rust", "C"]))
    st.session_state["user_data"]["languages"] = {}
    for language in languages:
        if language not in st.session_state["user_data"]["languages"]:
            st.session_state["user_data"]["languages"][language] = st.slider(f"Rate your expertise in {language} from 1 to 10", 1, 10)

    st.write(st.session_state["user_data"])

    # Without a callback, this will need to be pressed twice (or some element will have to update) to go to the correct page
    # This is because after the button is pressed, the app reruns all the way to line 41 and then enters the if block and updates the
    # session_state["step"] variable by which point the elif block is no longer entered
    # One hack is to use if instead of elif
    # A better way is to use a callback function 
    # if st.button("Next"):
    #     st.session_state["step"] = "exit"

    # update_step is a callback function defined above and the arguments to the function are passed in args
    st.button("Next", on_click=update_step, args=("exit",))

elif st.session_state["step"] == "exit":
    st.write("Thank you for your time")
    st.write(st.session_state["user_data"])
    st.write("Goodbye")
    st.button("Restart", on_click=update_step, args=("entry",))