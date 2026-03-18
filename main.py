import streamlit as st

st.title("Streamlit Testing Page")
st.write("Hello Streamlit")
st.write("streamlit for python")

st.header("SRINIVAS")
st.subheader("Python Trainer")

st.success("Success")

st.info("Information")

st.warning("Warning")

st.error("Error")

exp = ZeroDivisionError("Trying to divide by Zero")
st.exception(exp)

# Display a checkbox with the label 'Show/Hide'
if st.checkbox("Show/Hide"):
    # Show this text only when the checkbox is checked
    st.text("Showing the widget")

    # Create a radio button to select gender
status = st.radio("Select Gender:", ['Male', 'Female'])

# Display the selected option using success message
if status == 'Male':
    st.success("Male")
else:
    st.success("Female")

# Create a dropdown menu for selecting a hobby
hobby = st.selectbox("Select a Hobby:", ['Dancing', 'Reading', 'Sports'])

# Display the selected hobby
st.write("Your hobby is:", hobby)

# Create a multiselect box for choosing hobbies
hobbies = st.multiselect("Select Your Hobbies:", ['Dancing', 'Reading', 'Sports'])

# Display the number of selected hobbies
st.write("You selected", len(hobbies), "hobbies")

# A simple button that does nothing
st.button("Click Me")

# A button that displays text when clicked
if st.button("Click again"):
    st.text("Welcome to Streamlit")