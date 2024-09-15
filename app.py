import pandas as pd
import plotly.express as px
import streamlit as st

st.title("Lebanese Offical Exchange Rate ")

url = "https://linked.aub.edu.lb/pkgcube/data/a9c0cb61966b5c9fa47a4a9bbd375039_20240906_142928.csv"

dfer = pd.read_csv(url)

dfer_n = dfer.loc[dfer.groupby("Year")["Value"].idxmax()]
dfer_new = dfer_n[dfer_n["Year"] >= 2013]


#creates a widget for the raw data to display to the user

show_data = st.checkbox("Show Raw Data Used")
if show_data:
    st.write(dfer)


st.write("""
This app visualizes the offical exchange rate trends of the Lebanese Pound against the US Dollar from 2013 - 2023.
""")


st.subheader("Figure 1: Scatter Plot Graph")

scatter_fig = px.scatter(dfer_new, x="Year", y="Value",size = "Value", title="Exchange Rate Over Time (Lebanese Pounds per USD)", labels={"Year": "Year", "Value": "Exchange Rate (LBP/USD)"}, 
              size_max=35, color = "Value")


scatter_fig.update_layout(title_x=0.1,  height=500,font=dict(size=18))



st.plotly_chart(scatter_fig)






st.subheader("Figure 2: Area Plot Graph")

figarea = px.area(dfer_new, x="Year", y="Value", title="Exchange Rate of Lebanese Pounds per USD during the last 10 years (2013-2023)", markers=True
)

figarea.update_layout(title_x=0.1,   font=dict(size=24)
)

# Display the area plot in Streamlit
st.plotly_chart(figarea)






st.subheader("Figure 3: Animated Scatter Plot Graph")


New_fig = px.scatter(dfer_new, x="Year", y="Value", size="Value", title="Exchange Rate Over Time (Lebanese Pounds per USD)", labels={"Year": "Year", "Value": "Exchange Rate (LBP/USD)"}, size_max=50, color_discrete_sequence=["Red"], hover_name="Value", animation_frame="Year", range_x=[2013, 2023], range_y=[0, 16000]
)

New_fig.update_layout(title_x=0.1, height=700, font=dict(size=18))

st.plotly_chart(New_fig)







st.subheader("Figure 4: Animated Bar Graph")


fig=px.bar(dfer_new, x="Item",y="Value", animation_frame="Year", labels={"Item":"LBP","Value":"Exchange Rate LBP/USD"}, height= 600, range_y=[0,16000], title="LBP Exchange Rate to USD (2013-2023)",text_auto=True)

fig.update_layout(title_x=0.1,font=dict(size=15))


st.plotly_chart(fig)























st.subheader("Figure 5:  Line Graph With a Year Slider")


start_year, end_year = st.slider(
    "Select a range of years for the graph below",
    min_value=int(dfer_new["Year"].min()),
    max_value=int(dfer_new["Year"].max()),
    value=(2013, 2023)
)

filtered_dfer_new = dfer_new[(dfer_new["Year"] >= start_year) & (dfer_new["Year"] <= end_year)]

line_chart = px.line(filtered_dfer_new, x="Year", y="Value", title=f"Exchange Rate Over Time (Lebanese Pounds per USD) from {start_year} to {end_year}",labels={"Year": "Year", "Value": "Exchange Rate (LBP/USD)"},markers=True)

line_chart.update_layout(title_x=0.1, font=dict(size=18))

st.plotly_chart(line_chart)








