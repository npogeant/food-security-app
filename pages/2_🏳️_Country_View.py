import numpy as np
import altair as alt
import pandas as pd
import streamlit as st
from google.cloud import storage
from google.oauth2 import service_account

from utils.utils import (  # pylint: disable=wrong-import-position, import-error
    get_rank,
    create_line_chart,
    countries_category,
    add_logo
)

st.set_page_config(
    page_title='Country View',
    page_icon="🏳️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

with open("utils/static/style.css", "r") as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# ---- SIDEBAR ----

add_logo()

# ---- DATA ----

@st.experimental_memo
def get_data():

    # Create API client.
    credentials = service_account.Credentials.from_service_account_info(
        st.secrets["gcp_service_account"],
        scopes=["https://www.googleapis.com/auth/cloud-platform"],
    )

    GCP_PROJECT_ID = st.secrets["google_cloud_storage"][
        'GCP_PROJECT_ID'
    ]  # os.getenv('GCP_PROJECT_ID')
    STORAGE_BUCKET_NAME = st.secrets["google_cloud_storage"][
        'STORAGE_BUCKET_NAME'
    ]  # os.getenv('STORAGE_BUCKET_NAME')
    FILENAME = 'Food_Security_Data_E_All_Data_(Normalized).csv'
    storage_client = storage.Client(project=GCP_PROJECT_ID, credentials=credentials)

    dataframe = pd.read_csv(
        'gs://' + STORAGE_BUCKET_NAME + '/' + FILENAME,
        encoding='cp1252',
        storage_options={'token': credentials},
        low_memory=False,
    )

    return dataframe


# Create the title
st.markdown(
    "<h3 style='text-align: left; color: black;'>🏳️ Country View</h2><br>",
    unsafe_allow_html=True,
)

country = st.selectbox('Select a country', countries_category)

dataframe = get_data()

# ---- CHARTS ----
try:

    with st.container():
        col1, col2, col3, col4 = st.columns(4)

        col1.markdown("<h2></h2>", unsafe_allow_html=True)

        rank1 = get_rank(
            dataframe,
            'Prevalence of severe food insecurity in the total population (percent) (3-year average)',
            country,
        )
        rank2 = get_rank(
            dataframe,
            'Number of people undernourished (million) (3-year average)',
            country,
        )
        linechart = create_line_chart(
            dataframe,
            'Prevalence of severe food insecurity in the total population (percent) (3-year average)',
            country,
        )
        linechart_2 = create_line_chart(
            dataframe,
            'Number of people undernourished (million) (3-year average)',
            country,
        )

        col2.metric(
            label='Ranking in countries with least food insecurity', value=rank1
        )
        col3.metric(
            label='Ranking in countries with least undernourished people', value=rank2
        )

        col4.markdown("<h2></h2>", unsafe_allow_html=True)

    st.markdown("<h2></h2>", unsafe_allow_html=True)

    with st.container():
        col1, col2 = st.columns(2)

        col1.altair_chart(linechart, use_container_width=True, theme="streamlit")

        col2.altair_chart(linechart_2, use_container_width=True, theme="streamlit")

except IndexError:

    st.error('This country has missing values, please change selection...')

with st.container():

    st.markdown(
        "<h5 style='text-align: center; color: black; text-decoration: underline;'>The Entire Dataset :</h5>",
        unsafe_allow_html=True,
    )

    st.dataframe(dataframe)
