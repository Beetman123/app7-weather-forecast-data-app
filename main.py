import streamlit as st
import plotly.express as px
from backend import get_data

# Add title, text input, slider, selectbox, and subheader
st.title("Weather Forecast for the Next Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of forecasted days")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))
st.subheader(f"Temperature for the next {days} days in {place}")

try:
    if place:
        # Get the temperature/sky data
        filtered_data = get_data(place, days)

        if option == "Temperature":
            temperatures = [dict["main"]["temp"] for dict in filtered_data]
            temperatures = [each/10 for each in temperatures]
            dates = [dict["dt_txt"] for dict in filtered_data]
            # Create a temperature plot
            figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature (C)"})
            st.plotly_chart(figure)

        else: # option = Sky
            weather_forecast = [dict["weather"][0]["main"] for dict in filtered_data]
            for weather in weather_forecast:
                st.image(f"images/{str(weather).lower()}.png", width=115)
except KeyError:
    st.write(f"Our apologies but we couldn't find {place} in our database")
