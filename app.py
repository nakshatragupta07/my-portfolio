import streamlit as st
import numpy as np
import pandas as pandas
import matplotlib.pyplot as plt

# Title of the app
st.title('My Portfolio App')

# Sidebar for user input
st.sidebar.header('User Input Features')
selected_feature = st.sidebar.selectbox('Select a feature', ('Feature 1', 'Feature 2', 'Feature 3'))

# Main content
st.header('Main Content Area')
st.write(f'You selected: {selected_feature}')

# Example plot
st.header('Example Plot')
data = np.random.randn(100)
fig, ax = plt.subplots()
ax.hist(data, bins=20)
st.pyplot(fig)

# Example DataFrame
st.header('Example DataFrame')
df = pd.DataFrame({
    'Column 1': np.random.randn(100),
    'Column 2': np.random.randn(100)
})
st.write(df)
