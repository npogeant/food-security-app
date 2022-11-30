import numpy as np
import altair as alt
import pandas as pd
import streamlit as st
from streamlit.components.v1 import html

economies_category = [
    'Least Developed Countries',
    'Land Locked Developing Countries',
    'Small Island Developing States',
    'Low Income Food Deficit Countries',
    'Low income economies',
    'Lower-middle-income economies',
    'High-income economies',
    'Upper-middle-income economies',
]

regions_category = [
    'World',
    'Africa',
    'Eastern Africa',
    'Middle Africa',
    'Northern Africa',
    'Northern Africa (excluding Sudan)',
    'Southern Africa',
    'Western Africa',
    'Sub-Saharan Africa',
    'Sub-Saharan Africa (including Sudan)',
    'Northern America and Europe',
    'Northern America',
    'Europe',
    'Eastern Europe',
    'Northern Europe',
    'Southern Europe',
    'Western Europe',
    'Latin America and the Caribbean',
    'Central America',
    'Caribbean',
    'South America',
    'Asia',
    'Central Asia',
    'Eastern Asia',
    'Southern Asia',
    'Southern Asia (excluding India)',
    'South-eastern Asia',
    'Western Asia',
    'Central Asia and Southern Asia',
    'Eastern Asia and South-eastern Asia',
    'Western Asia and Northern Africa',
    'Oceania',
    'Australia and New Zealand',
    'Melanesia',
    'Micronesia',
    'Polynesia',
    'Oceania excluding Australia and New Zealand',
]

countries_category = [
    'Afghanistan',
    'Albania',
    'Algeria',
    'American Samoa',
    'Andorra',
    'Angola',
    'Antigua and Barbuda',
    'Argentina',
    'Armenia',
    'Australia',
    'Austria',
    'Azerbaijan',
    'Bahamas',
    'Bahrain',
    'Bangladesh',
    'Barbados',
    'Belarus',
    'Belgium',
    'Belize',
    'Benin',
    'Bermuda',
    'Bhutan',
    'Bolivia (Plurinational State of)',
    'Bosnia and Herzegovina',
    'Botswana',
    'Brazil',
    'Brunei Darussalam',
    'Bulgaria',
    'Burkina Faso',
    'Burundi',
    'Cabo Verde',
    'Cambodia',
    'Cameroon',
    'Canada',
    'Central African Republic',
    'Chad',
    'Chile',
    'China',
    'China, Hong Kong SAR',
    'China, Macao SAR',
    'China, mainland',
    'China, Taiwan Province of',
    'Colombia',
    'Comoros',
    'Congo',
    'Cook Islands',
    'Costa Rica',
    "Côte d'Ivoire",
    'Croatia',
    'Cuba',
    'Cyprus',
    'Czechia',
    "Democratic People's Republic of Korea",
    'Democratic Republic of the Congo',
    'Denmark',
    'Djibouti',
    'Dominica',
    'Dominican Republic',
    'Ecuador',
    'Egypt',
    'El Salvador',
    'Equatorial Guinea',
    'Eritrea',
    'Estonia',
    'Eswatini',
    'Ethiopia',
    'Fiji',
    'Finland',
    'France',
    'French Polynesia',
    'Gabon',
    'Gambia',
    'Georgia',
    'Germany',
    'Ghana',
    'Greece',
    'Greenland',
    'Grenada',
    'Guatemala',
    'Guinea',
    'Guinea-Bissau',
    'Guyana',
    'Haiti',
    'Honduras',
    'Hungary',
    'Iceland',
    'India',
    'Indonesia',
    'Iran (Islamic Republic of)',
    'Iraq',
    'Ireland',
    'Israel',
    'Italy',
    'Jamaica',
    'Japan',
    'Jordan',
    'Kazakhstan',
    'Kenya',
    'Kiribati',
    'Kuwait',
    'Kyrgyzstan',
    "Lao People's Democratic Republic",
    'Latvia',
    'Lebanon',
    'Lesotho',
    'Liberia',
    'Libya',
    'Lithuania',
    'Luxembourg',
    'Madagascar',
    'Malawi',
    'Malaysia',
    'Maldives',
    'Mali',
    'Malta',
    'Marshall Islands',
    'Mauritania',
    'Mauritius',
    'Mexico',
    'Micronesia (Federated States of)',
    'Mongolia',
    'Montenegro',
    'Morocco',
    'Mozambique',
    'Myanmar',
    'Namibia',
    'Nauru',
    'Nepal',
    'Netherlands',
    'New Caledonia',
    'New Zealand',
    'Nicaragua',
    'Niger',
    'Nigeria',
    'Niue',
    'North Macedonia',
    'Norway',
    'Oman',
    'Pakistan',
    'Palau',
    'Palestine',
    'Panama',
    'Papua New Guinea',
    'Paraguay',
    'Peru',
    'Philippines',
    'Poland',
    'Portugal',
    'Puerto Rico',
    'Qatar',
    'Republic of Korea',
    'Republic of Moldova',
    'Romania',
    'Russian Federation',
    'Rwanda',
    'Saint Kitts and Nevis',
    'Saint Lucia',
    'Saint Vincent and the Grenadines',
    'Samoa',
    'Sao Tome and Principe',
    'Saudi Arabia',
    'Senegal',
    'Serbia',
    'Seychelles',
    'Sierra Leone',
    'Singapore',
    'Slovakia',
    'Slovenia',
    'Solomon Islands',
    'Somalia',
    'South Africa',
    'South Sudan',
    'Spain',
    'Sri Lanka',
    'Sudan',
    'Suriname',
    'Sweden',
    'Switzerland',
    'Syrian Arab Republic',
    'Tajikistan',
    'Thailand',
    'Timor-Leste',
    'Togo',
    'Tokelau',
    'Tonga',
    'Trinidad and Tobago',
    'Tunisia',
    'Türkiye',
    'Turkmenistan',
    'Tuvalu',
    'Uganda',
    'Ukraine',
    'United Arab Emirates',
    'United Kingdom of Great Britain and Northern Ireland',
    'United Republic of Tanzania',
    'United States of America',
    'Uruguay',
    'Uzbekistan',
    'Vanuatu',
    'Venezuela (Bolivarian Republic of)',
    'Viet Nam',
    'Yemen',
    'Zambia',
    'Zimbabwe',
]

dimensions_dict = {
    'Prevalence of severe food insecurity in the total population (percent) (3-year average)': '210401',
    'Number of people undernourished (million) (3-year average)': '210011',
}

description_dict = {
    'Prevalence of severe food insecurity in the total population (percent) (3-year average)': 'The prevalence of severe food insecurity is an estimate of the percentage of people in the population who live in households classified as severely food insecure. The assessment is conducted using data collected with the Food Insecurity Experience Scale or a compatible experience-based food security measurement questionnaire (such as the HFSSM).',
    'Number of people undernourished (million) (3-year average)': 'Estimated number of people at risk of undernourishment. It is calculated by applying the estimated prevalence of undernourishment to total population in each period.',
}

def add_logo():
    st.markdown(
        """
        <style>
            [data-testid="stSidebarNav"] {
                background-image: url(https://upload.wikimedia.org/wikipedia/commons/thumb/d/db/FAO_logo.svg/1008px-FAO_logo.svg.png);
                background-repeat: no-repeat;
                padding-top: 100px;
                background-position: 20px 20px;
                background-size: 150px;
                background-position: 50% 10%;
            }
            [data-testid="stSidebarNav"]::before {
                content: "FAO - Analysis";
                margin-left: 20px;
                margin-top: 20px;
                font-size: 19px;
                position: relative;
                top: 100px;
                font-weight: bold;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )
    
def create_bar_charts(dataframe, dimension):

    categories_dict = {
        'Countries': countries_category,
        'Economies': economies_category,
        'Regions': regions_category,
    }

    # with st.container():
    # col = st.columns(3)

    for category, list in categories_dict.items():

        year = dataframe[dataframe['Year'].str.contains('-')]['Year'].max()

        # Filter the data to keep last years values from the specific dimension
        source = dataframe[
            (dataframe['Item Code'] == dimensions_dict[dimension])
            & (dataframe['Year'] == year)
            & (dataframe['Element'] == 'Value')
        ]

        # Keep countries only
        source = source.query("Area in @list")

        # Count missing values and remove them
        missing_values = source['Value'].isna().sum()
        source = source[source['Value'].isna() == False]

        # Preprocess the string values into numeric ones
        source['Value'] = np.where(
            source['Value'].str.contains('<'),
            source['Value'].str.replace('<', ''),
            source['Value'],
        ).astype(float)

        if 'severe food insecurity' in dimension:
            title = f'Most Food Insecure {category} of the last 3 years'
            xAxis_format = "format(datum.value,'.0%')"

            source['Value'] = source['Value'] / 100

        elif 'people undernourished' in dimension:
            title = (
                f'{category} with the most undernourished people of the last 3 years'
            )
            xAxis_format = "format(datum.value,'~s')+' M'"
        else:
            print('There is some issue...')

        chart = (
            alt.Chart(source)
            .transform_window(
                rank='rank(Value)', sort=[alt.SortField('Value', order='descending')]
            )
            .transform_filter(alt.datum.rank <= 10)
            .mark_bar()
            .encode(
                x=alt.X('Value:Q', axis=alt.Axis(labelExpr=xAxis_format), title=None),
                y=alt.Y('Area:O', sort='-x', title=None),
            )
            .properties(
                width=450,
                height=300,
                title={
                    "text": [title],
                    "subtitle": ['The values used are the :', f'{dimension}'],
                    "anchor": "start",
                    "align": "left",
                    "color": "Black",
                    "subtitleColor": "Grey",
                    "fontSize": 18,
                    "subtitleFontSize": 13,
                },
            )
        )
        st.altair_chart(chart, use_container_width=True, theme="streamlit")

    return


def create_line_charts(dataframe, dimension):

    categories_dict = {
        'Countries': countries_category,
        'Economies': economies_category,
        'Regions': regions_category,
    }

    for category, list in categories_dict.items():

        source = dataframe[
            (dataframe['Item Code'] == dimensions_dict[dimension])
            & (dataframe['Element'] == 'Value')
        ]
        source = source.query("Area in @list")

        source = source[
            ~source['Area'].isin(source[source['Value'].isna()]['Area'].unique())
        ]

        source['Value'] = np.where(
            source['Value'].str.contains('<'),
            source['Value'].str.replace('<', ''),
            source['Value'],
        ).astype(float)

        source = pd.pivot_table(
            source, values='Value', index=['Area', 'Year Code']
        ).reset_index()
        source['Year'] = pd.to_datetime(source['Year Code'].astype(str).str[-4:])
        source = source.sort_values(by='Year')

        if 'severe food insecurity' in dimension:
            title = f'Evolution of Food Insecurity by {category}'
            xAxis_format = "format(datum.value,'.0%')"

            source['Value'] = source['Value'] / 100

        elif 'people undernourished' in dimension:
            title = f'Evolution of Undernourished People by {category}'
            xAxis_format = "format(datum.value,'~s')+' M'"
        else:
            print('There is some issue...')

        selection = alt.selection_multi(fields=['Area'], bind='legend')

        chart = (
            alt.Chart(source)
            .mark_line()
            .encode(
                x=alt.X('Year:T', title=None),
                y=alt.Y('Value:Q', axis=alt.Axis(labelExpr=xAxis_format), title=None),
                color=alt.Color(
                    'Area:N',
                    legend=None,
                    scale=alt.Scale(
                        scheme='category20b',
                    ),
                ),
                opacity=alt.condition(selection, alt.value(1), alt.value(0.2)),
            )
            .properties(
                width=450,
                height=300,
                title={
                    "text": [title],
                    "subtitle": [f'The values used are the {dimension.lower()}'],
                    "anchor": "start",
                    "align": "left",
                    "color": "Black",
                    "subtitleColor": "Grey",
                    "fontSize": 18,
                    "subtitleFontSize": 13,
                },
            )
            .add_selection(selection)
        )

        st.altair_chart(chart, use_container_width=True, theme="streamlit")

    return


def create_map_chart(dataframe, dimension):

    url = 'https://raw.githubusercontent.com/deldersveld/topojson/master/world-countries-sans-antarctica.json'
    topjson = alt.topo_feature(url, "countries1")

    dataframe['Area'] = np.where(
        dataframe['Area'] == 'Bolivia (Plurinational State of)',
        'Bolivia',
        np.where(
            dataframe['Area'] == 'Brunei Darussalam',
            'Brunei',
            np.where(
                dataframe['Area'] == 'Czechia',
                'Czech Republic',
                np.where(
                    dataframe['Area'] == 'Timor-Leste',
                    'East Timor',
                    np.where(
                        dataframe['Area'] == 'Guinea-Bissau',
                        'Guinea Bissau',
                        np.where(
                            dataframe['Area'] == 'Iran',
                            'Iran (Islamic Republic of)',
                            np.where(
                                dataframe['Area'] == "Côte d'Ivoire",
                                'Ivory Coast',
                                np.where(
                                    dataframe['Area'] == 'North Macedonia',
                                    'Macedonia',
                                    np.where(
                                        dataframe['Area'] == 'Republic of Moldova',
                                        'Moldova',
                                        np.where(
                                            dataframe['Area'] == 'Serbia',
                                            'Republic of Serbia',
                                            np.where(
                                                dataframe['Area'] == 'Congo',
                                                'Republic of the Congo',
                                                np.where(
                                                    dataframe['Area']
                                                    == 'Russian Federation',
                                                    'Russia',
                                                    np.where(
                                                        dataframe['Area']
                                                        == 'Republic of Korea',
                                                        'South Korea',
                                                        np.where(
                                                            dataframe['Area']
                                                            == "Democratic People's Republic of Korea",
                                                            'North Korea',
                                                            np.where(
                                                                dataframe['Area']
                                                                == 'Iran (Islamic Republic of)',
                                                                'Iran',
                                                                np.where(
                                                                    dataframe['Area']
                                                                    == 'China, Taiwan Province of',
                                                                    'Taiwan',
                                                                    np.where(
                                                                        dataframe[
                                                                            'Area'
                                                                        ]
                                                                        == 'Bahamas',
                                                                        'The Bahamas',
                                                                        np.where(
                                                                            dataframe[
                                                                                'Area'
                                                                            ]
                                                                            == 'Türkiye',
                                                                            'Turkey',
                                                                            np.where(
                                                                                dataframe[
                                                                                    'Area'
                                                                                ]
                                                                                == 'United Kingdom of Great Britain and Northern Ireland',
                                                                                'United Kingdom',
                                                                                np.where(
                                                                                    dataframe[
                                                                                        'Area'
                                                                                    ]
                                                                                    == 'Venezuela (Bolivarian Republic of)',
                                                                                    'Venezuela',
                                                                                    np.where(
                                                                                        dataframe[
                                                                                            'Area'
                                                                                        ]
                                                                                        == 'Sub-Saharan Africa',
                                                                                        'Western Sahara',
                                                                                        np.where(
                                                                                            dataframe[
                                                                                                'Area'
                                                                                            ]
                                                                                            == 'Syrian Arab Republic',
                                                                                            'Syria',
                                                                                            dataframe[
                                                                                                'Area'
                                                                                            ],
                                                                                        ),
                                                                                    ),
                                                                                ),
                                                                            ),
                                                                        ),
                                                                    ),
                                                                ),
                                                            ),
                                                        ),
                                                    ),
                                                ),
                                            ),
                                        ),
                                    ),
                                ),
                            ),
                        ),
                    ),
                ),
            ),
        ),
    )

    year = dataframe[dataframe['Year'].str.contains('-')]['Year'].max()

    # Filter the data to keep last years values from the specific dimension
    source = dataframe[
        (dataframe['Item Code'] == dimensions_dict[dimension])
        & (dataframe['Year'] == year)
        & (dataframe['Element'] == 'Value')
    ]

    # Preprocess the string values into numeric ones
    source['Value'] = np.where(
        source['Value'].str.contains('<'),
        source['Value'].str.replace('<', ''),
        source['Value'],
    ).astype(float)

    source['Value'] = source['Value'].fillna(0)

    if 'severe food insecurity' in dimension:
        title = f'Food Insecurity Map'
        legend_format = "format(datum.value,'.0%')"
        tooltip_format = ".1%"
        tooltip_title = "Food Insecurity"

        source['Value'] = source['Value'] / 100

    elif 'people undernourished' in dimension:
        title = f'Undernourished People Map'
        legend_format = "format(datum.value,'~s')+' M'"
        tooltip_format = "m"
        tooltip_title = "Number of people (in M)"
    else:
        print('There is some issue...')

    map = (
        alt.Chart(topjson)
        .mark_geoshape()
        .encode(
            tooltip=[
                alt.Tooltip('properties.name:N', title='Country'),
                alt.Tooltip('Value:Q', title=tooltip_title, format=tooltip_format),
            ],
            color=alt.condition(
                'datum.Value !== 0',
                alt.Color(
                    'Value:Q',
                    title=' ',
                    legend=alt.Legend(labelExpr=legend_format),
                    scale=alt.Scale(scheme='reds'),
                ),
                alt.value('lightgray'),
            ),
        )
        .transform_lookup(
            lookup='properties.name', from_=alt.LookupData(source, 'Area', ['Value'])
        )
        .properties(
            width=1000,
            height=500,
            title={
                "text": [title],
                "subtitle": [f'The values used are the {dimension.lower()}'],
                "anchor": "start",
                "align": "left",
                "color": "Black",
                "subtitleColor": "Grey",
                "fontSize": 18,
                "subtitleFontSize": 13,
            },
        )
    )

    return map


def create_metrics(dataframe, dimension):

    source = dataframe[
        (dataframe['Item Code'] == dimensions_dict[dimension])
        & (dataframe['Element'] == 'Value')
    ]
    source = source.query("Area in @countries_category")

    source = source[source['Value'].isna() == False]

    source['Value'] = np.where(
        source['Value'].str.contains('<'),
        source['Value'].str.replace('<', ''),
        source['Value'],
    ).astype(float)

    pivot_evol = pd.pivot_table(
        source, values='Value', columns='Year Code', index='Area'
    )
    pivot_evol['pct_change_last_values'] = (
        pivot_evol.iloc[:, np.r_[-2, -1]].pct_change(axis='columns').iloc[:, -1]
    )
    pivot_evol['pct_change_last_values'] = pivot_evol['pct_change_last_values'].round(1)
    pivot_evol = pivot_evol[pivot_evol['pct_change_last_values'].isna() == False]

    if 'severe food insecurity' in dimension:
        pivot_evol.iloc[:, -2] = pivot_evol.iloc[:, -2].astype(str) + '%'

    elif 'people undernourished' in dimension:
        pivot_evol.iloc[:, -2] = pivot_evol.iloc[:, -2].astype(str) + 'M'

    else:
        print('There is some issue...')

    return pivot_evol


def create_line_chart(dataframe, dimension, country):

    source = dataframe[
        (dataframe['Item Code'] == dimensions_dict[dimension])
        & (dataframe['Element'] == 'Value')
    ]
    source = source.query("Area == @country")

    source = source[
        ~source['Area'].isin(source[source['Value'].isna()]['Area'].unique())
    ]

    source['Value'] = np.where(
        source['Value'].str.contains('<'),
        source['Value'].str.replace('<', ''),
        source['Value'],
    ).astype(float)

    source = pd.pivot_table(
        source, values='Value', index=['Area', 'Year Code']
    ).reset_index()
    source['Year'] = pd.to_datetime(source['Year Code'].astype(str).str[-4:])
    source = source.sort_values(by='Year')

    if 'severe food insecurity' in dimension:
        title = f'Evolution of Food Insecurity in {country}'
        xAxis_format = "format(datum.value,'.0%')"

        source['Value'] = source['Value'] / 100

    elif 'people undernourished' in dimension:
        title = f'Evolution of Undernourished People in {country}'
        xAxis_format = "format(datum.value,'~s')+' M'"
    else:
        print('There is some issue...')

    selection = alt.selection_multi(fields=['Area'], bind='legend')

    chart = (
        alt.Chart(source)
        .mark_line()
        .encode(
            x=alt.X('Year:T', axis=alt.Axis(format="%Y"), title=None),
            y=alt.Y('Value:Q', axis=alt.Axis(labelExpr=xAxis_format), title=None),
            color=alt.Color(
                'Area:N',
                legend=None,
                scale=alt.Scale(
                    scheme='category20b',
                ),
            ),
            opacity=alt.condition(selection, alt.value(1), alt.value(0.2)),
        )
        .properties(
            width=450,
            height=300,
            title={
                "text": [title],
                "subtitle": [f'The values used are the {dimension.lower()}'],
                "anchor": "start",
                "align": "left",
                "color": "Black",
                "subtitleColor": "Grey",
                "fontSize": 18,
                "subtitleFontSize": 13,
            },
        )
        .add_selection(selection)
    )

    # st.altair_chart(chart, use_container_width=True, theme="streamlit")

    return chart


def get_rank(dataframe, dimension, country):

    year = dataframe[dataframe['Year'].str.contains('-')]['Year'].max()

    source = dataframe[
        (dataframe['Item Code'] == dimensions_dict[dimension])
        & (dataframe['Year'] == year)
        & (dataframe['Element'] == 'Value')
    ]
    source = source.query("Area in @countries_category")

    source = source[source['Value'].isna() == False]

    source['Value'] = np.where(
        source['Value'].str.contains('<'),
        source['Value'].str.replace('<', ''),
        source['Value'],
    ).astype(float)
    source['Rank'] = (
        source['Value'].rank(method='dense', na_option='bottom').astype(int)
    )

    country_rank = source[source['Area'] == country]['Rank'].iloc[0]

    return country_rank
