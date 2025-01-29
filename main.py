import streamlit as st

# Create default logged_in key and set it to False
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

# Sets the page title to show on the tab
# Can also be used to specify an icon
# st.set_page_config(page_title="Home", page_icon=":material/home:")

# It is possible to set up pages by creating a folder called pages
# and then creating files for the pages. They show up on the sidebar
# in the order that they show up in the folder (alphanumerically
# ordered).

# But the more preferred way of doing that is using st.navigation
# and st.Page. In that case, the entrypoint file becomes sort of a
# router - it should not contain any UI ideally

# The individual page files can be outside the pages/ directory too.
dashboard_page = st.Page("pages/1_dashboard.py", title="Dashboard", icon=":material/dashboard:")
data_page = st.Page("pages/2_data.py", title="Data", icon=":material/database:")
about_page = st.Page("pages/3_about.py", title="About", icon=":material/info:")
profile_page = st.Page("pages/4_profile.py", title="Profile", icon=":material/person:")
account_page = st.Page("pages/5_account.py", title="Account", icon=":material/manage_accounts:")

# It is also possible to do functions for pages
def login_page_render():
    if st.button(label="Log in"):
        st.session_state["logged_in"] = True
        st.rerun() # This will rerun the app from this entrypoint

def logout_page_render():
    if st.button(label="Log out"):
        st.session_state["logged_in"] = False
        st.rerun() # This will rerun the app from this entrypoint

login_page = st.Page(login_page_render, title="Log in", icon=":material/login:")
logout_page = st.Page(logout_page_render, title="Log out", icon=":material/logout:")

if st.session_state["logged_in"]:
    pg = st.navigation( # Grouping under tabs within sidebar
        {
            "Stocks": [dashboard_page, data_page],
            "Account": [profile_page, account_page, logout_page],
            "Misc": [about_page], # This isn't really ungrouped the way I want it
        }
    )
else:
    pg = st.navigation([login_page])

# pg = st.navigation([dashboard_page, data_page])
pg.run() # This does not play well with multiple set_page_config() calls, configure when reating st.Page

# It is also possible to set up the navigation in the sidebar with st.page_links
if st.session_state["logged_in"]:
    with st.sidebar:
        # This is also not grouped the way I want it
        st.markdown("#### Stocks")
        st.page_link("pages/1_dashboard.py", label="Dashboard", icon=":material/dashboard:")
        st.page_link("pages/2_data.py", label="Data", icon=":material/database:")
        st.markdown("#### Account")
        st.page_link("pages/4_profile.py", label="Profile", icon=":material/person:")
        st.page_link("pages/5_account.py", label="Account", icon=":material/manage_accounts:")
        # st.page_link(logout_page_render, label="Log out", icon=":material/logout:") # Invalid, page_links does not support functions
        st.page_link("pages/3_about.py", label="About", icon=":material/info:")
else:
    pass # No way to do log out since that is a function