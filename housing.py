import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn')

st.title('California Housing Data(1990) by QiuZiyan')

df = pd.read_csv('housing.csv')

# add a slider
price_slider = st.slider('Minimal Median House Price', 0, 500001, 200000)


st.header('See more filters in the sidebar:')

# add a multi selector
location_filter = st.sidebar.multiselect(
     'Choose the location type',
     df.ocean_proximity.unique(),  # options
     df.ocean_proximity.unique())  # defaults

# add a radio button widget
income_level = ['Low', 'Median', 'High']
income_filter = st.sidebar.radio('Choose income level', income_level)
if income_filter == 'Low':
    df = df[df.median_income <= 2.5]
elif income_filter == 'Middle':
    df = df[2.5 < df.median_income < 4.5]
else:
    df = df[df.median_income >= 4.5]

# filter by price
df = df[df.median_house_value >= price_slider]

# filter by ocean_proximity
df = df[df.ocean_proximity.isin(location_filter)]

# show on map
st.map(df)

# show the pop plot
st.header('Histogram of the Median House Value')
fig, ax = plt.subplots()
hist_data = df.median_house_value
hist_data.plot.hist(ax=ax, bins=30)
st.pyplot(fig)