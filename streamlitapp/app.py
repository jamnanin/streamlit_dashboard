import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

# Read CSV file
csv_file = st.file_uploader("Upload CSV file", type=["csv"])
if csv_file is not None:
    df = pd.read_csv(csv_file)

    # Display CSV data on the first page
    st.header("CSV Data")
    st.write(df)

    # Create second page
    st.sidebar.header("National Statistics")

    # Allow user to select columns to use as selectors
    selector_cols = st.sidebar.multiselect(
        "Select columns to use as selectors:", df.columns.tolist()
    )

    # Filter dataframe by selected columns
    df_selectors = df[selector_cols]

    # Remove duplicate rows
    df_selectors = df_selectors.drop_duplicates()

    # Allow user to select page
    page = st.sidebar.selectbox("Select page", ["Country data", "Continent data"])

    if page == "Country data":
        ## Countries
        clist = df_selectors["country"].unique()
        country = st.selectbox("Select a country:", clist)
        col1, col2 = st.columns(2)
        fig = px.line(
            df[df["country"] == country],
            x="year",
            y="child_mortality_per_100",
            title="Child mortality per 1000",
        )

        col1.plotly_chart(fig, use_container_width=True)
        # fig = px.line(
        #     df[df["country"] == country],
        #     x="year",
        #     y="pop",
        #     title="Population Growth",
        # )

        # col2.plotly_chart(fig, use_container_width=True)
    else:
        pass
        ## Continents
        # contlist = df_selectors["continent"].unique()

        # continent = st.selectbox("Select a continent:", contlist)
        # col1, col2 = st.columns(2)
        # fig = px.line(
        #     df[df["continent"] == continent],
        #     x="year",
        #     y="gdpPercap",
        #     title="GDP per Capita",
        #     color="country",
        # )

        # col1.plotly_chart(fig)
        # fig = px.line(
        #     df[df["continent"] == continent],
        #     x="year",
        #     y="pop",
        #     title="Population",
        #     color="country",
        # )

        # col2.plotly_chart(fig, use_container_width=True)
