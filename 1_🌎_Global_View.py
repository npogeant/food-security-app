import numpy as np
import altair as alt
import pandas as pd
import streamlit as st
from google.cloud import storage
from google.oauth2 import service_account

from utils.utils import (  # pylint: disable=wrong-import-position, import-error
    create_metrics,
    create_map_chart,
    description_dict,
    create_bar_charts,
    create_line_charts,
    add_logo
)

st.set_page_config(
    page_title='Global View',
    page_icon="🌎",
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
    "<h3 style='text-align: left; color: black;'>🌎 Global View</h3><br>",
    unsafe_allow_html=True,
)

dimension = st.selectbox(
    'Select a dimension',
    [
        'Prevalence of severe food insecurity in the total population (percent) (3-year average)',
        'Number of people undernourished (million) (3-year average)',
    ],
)

st.markdown(
    f"<p><b>Dimension definition</b> : <em>{description_dict[dimension]}</em></p>",
    unsafe_allow_html=True,
)

dataframe = get_data()

# ---- CHARTS ----

st.markdown('<hr class="solid">', unsafe_allow_html=True)

with st.container():
    map = create_map_chart(dataframe, dimension)
    st.altair_chart(map, use_container_width=True, theme="streamlit")

st.markdown('<hr class="solid">', unsafe_allow_html=True)

pivot_evol = create_metrics(dataframe, dimension)
with st.container():

    st.markdown(
        "<h5 style='text-align: left; color: black; text-decoration: underline;'><br>Best Evolutions of the last 3 years</h5>",
        unsafe_allow_html=True,
    )

    best_evol = (
        pivot_evol.reset_index()
        .iloc[:, np.r_[0, -3:0]]
        .sort_values(by=pivot_evol.columns[-1])
    )
    col = st.columns(6)
    col[0].markdown("<h2></h2>", unsafe_allow_html=True)
    col[2].markdown("<h2></h2>", unsafe_allow_html=True)
    for idx, i in enumerate(best_evol.head(3).values):
        col[idx * 2 + 1].metric(
            label=i[0], value=i[2], delta=i[3], delta_color='inverse'
        )

    st.markdown(
        "<h5 style='text-align: left; color: black; text-decoration: underline;'><br>Worst Evolutions of the last 3 years</h5>",
        unsafe_allow_html=True,
    )

    worst_evol = (
        pivot_evol.reset_index()
        .iloc[:, np.r_[0, -3:0]]
        .sort_values(by=pivot_evol.columns[-1], ascending=False)
    )
    col = st.columns(6)
    col[0].markdown("<h2></h2>", unsafe_allow_html=True)
    col[2].markdown("<h2></h2>", unsafe_allow_html=True)
    for idx, i in enumerate(worst_evol.head(3).values):
        col[idx * 2 + 1].metric(
            label=i[0], value=i[2], delta=i[3], delta_color='inverse'
        )

st.markdown('<hr class="solid">', unsafe_allow_html=True)

with st.container():
    col1, col2 = st.columns(2)

    with col1.container():
        st.markdown(
            "<h5 style='text-align: center; color: black; text-decoration: underline;'><br>Ranking : Countries, Economies and Regions</h5>",
            unsafe_allow_html=True,
        )
        st.markdown("<h5></h5>", unsafe_allow_html=True)
        create_bar_charts(dataframe, dimension)

    with col2.container():
        st.markdown(
            "<h5 style='text-align: center; color: black; text-decoration: underline;'><br>Evolution : Countries, Economies and Regions</h5>",
            unsafe_allow_html=True,
        )
        st.markdown("<h5></h5>", unsafe_allow_html=True)
        create_line_charts(dataframe, dimension)
