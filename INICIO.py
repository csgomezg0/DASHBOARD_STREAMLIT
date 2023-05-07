import streamlit as st

from st_pages import Page, add_page_title, show_pages

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)


st.title("Main Page")
st.write("# Welcome to Streamlit! 👋")

st.sidebar.success("Select a page above.")



"## Declaring the pages in your app:"

show_pages(
    [
        Page("PAGES\HOME.py", "Home", "🏠"),
        Page("PAGES\dashboard.py", "Dash", "🏠"),
        # Can use :<icon-name>: or the actual icon
        Page("PAGES\page2.py", "Example two", ":books:"),
        # The pages appear in the order you pass them
   ]
)

add_page_title()  # Optional method to add title and icon to current page

    
st.markdown(
    """
    Streamlit is an open-source app framework built specifically for
    Machine Learning and Data Science projects.
    **👈 Select a demo from the sidebar** to see some examples
    of what Streamlit can do!
    ### Want to learn more?
    - Check out [streamlit.io](https://streamlit.io)
    - Jump into our [documentation](https://docs.streamlit.io)
    - Ask a question in our [community
        forums](https://discuss.streamlit.io)
    ### See more complex demos
    - Use a neural net to [analyze the Udacity Self-driving Car Image
        Dataset](https://github.com/streamlit/demo-self-driving)
    - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
"""
)