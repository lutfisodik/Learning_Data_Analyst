import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')

# Load data
day_df = pd.read_csv('day.csv')
hour_df = pd.read_csv('hour.csv')

# Sidebar untuk memilih visualisasi
st.sidebar.title('Choose Visualization')
visualization = st.sidebar.selectbox('Select Visualization', ('Seasonal Bike Usage', 'Weekly Bike Usage Trend', 'Weather Influence', 'Hourly Bike Usage'))

# Visualisasi berdasarkan pilihan di sidebar
st.title('Bike Sharing Data Analysis Dashboard')

if visualization == 'Seasonal Bike Usage':
    st.header('Seasonal Bike Usage Analysis')
    average_by_season = day_df.groupby('season')['cnt'].mean()
    st.bar_chart(average_by_season)

elif visualization == 'Weekly Bike Usage Trend':
    st.header('Weekly Bike Usage Trend Analysis')
    daily_trend = day_df.groupby('weekday')['cnt'].mean()
    st.line_chart(daily_trend)

elif visualization == 'Weather Influence':
    st.header('Weather Influence on Bike Usage Analysis')
    average_by_weather = day_df.groupby('weathersit')['cnt'].mean()
    st.bar_chart(average_by_weather)

elif visualization == 'Hourly Bike Usage':
    st.header('Hourly Bike Usage Analysis')
    hourly_usage = hour_df.groupby('hr')['cnt'].mean()
    st.line_chart(hourly_usage)

# Menambahkan informasi tambahan atau statistik deskriptif
# st.sidebar.title('Additional Information')
# st.sidebar.subheader('Descriptive Statistics')

# st.sidebar.write('Descriptive Statistics for Casual Users:')
# st.sidebar.write(day_df['casual'].describe())

# st.sidebar.write('Descriptive Statistics for Registered Users:')
# st.sidebar.write(day_df['registered'].describe())

# st.sidebar.write('Descriptive Statistics for Total Count:')
# st.sidebar.write(day_df['cnt'].describe())

# Menampilkan grafik histogram distribusi
st.subheader('Distribution of Users')
st.write('Histogram for Casual Users, Registered Users, and Total Count')
fig, ax = plt.subplots(figsize=(6, 4))
ax.hist(day_df['casual'], bins=30, alpha=0.5, label='Casual Users', color='blue')
ax.hist(day_df['registered'], bins=30, alpha=0.5, label='Registered Users', color='green')
ax.hist(day_df['cnt'], bins=30, alpha=0.5, label='Total Count', color='orange')
ax.legend()
st.pyplot(fig)

# # Menampilkan hubungan antara casual, registered, dan total count
# st.subheader('Relationship between Users')
# st.write('Scatter plot for Casual, Registered Users, and Total Count')
# fig, ax = plt.subplots(figsize=(6, 4))
# ax.hist(day_df['casual'], bins=30, alpha=0.5, label='Casual Users', color='blue')
# ax.hist(day_df['registered'], bins=30, alpha=0.5, label='Registered Users', color='green')
# ax.hist(day_df['cnt'], bins=30, alpha=0.5, label='Total Count', color='orange')
# ax.legend()
# st.pyplot(fig)

rfm_analysis = pd.read_csv('rfm_analysis.csv')
#RFM Analysis
st.title('RFM Analysis and Visualization')

# # Menampilkan tabel data RFM
# st.subheader('RFM Analysis Data')
# st.write(rfm_analysis.head())

# Visualisasi Recency
st.subheader('Recency Analysis Visualization')
fig_recency = plt.figure(figsize=(8, 6))
plt.bar(rfm_analysis['dteday'], rfm_analysis['Recency'], color='green')
plt.xlabel('Date')
plt.ylabel('Recency')
plt.title('Recency Analysis')
plt.xticks(rotation=45)
st.pyplot(fig_recency)

# Visualisasi Frequency
st.subheader('Frequency Analysis Visualization')
fig_frequency = plt.figure(figsize=(8, 6))
plt.plot(rfm_analysis['dteday'], rfm_analysis['Frequency'], marker='o', color='green')
plt.xlabel('Date')
plt.ylabel('Frequency')
plt.title('Frequency Analysis')
plt.xticks(rotation=45)
st.pyplot(fig_frequency)

# Visualisasi Monetary
st.subheader('Monetary Analysis Visualization')
fig_monetary = plt.figure(figsize=(8, 6))
plt.bar(rfm_analysis['dteday'], rfm_analysis['Monetary'], color='green')
plt.xlabel('Date')
plt.ylabel('Monetary')
plt.title('Monetary Analysis')
plt.xticks(rotation=45)
st.pyplot(fig_monetary)