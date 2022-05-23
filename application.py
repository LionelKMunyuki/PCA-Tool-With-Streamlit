# Let's Import our libraries:

import streamlit as st
import pandas as pd
import plotly.express as px
from application_functions import pca_maker

# Next, Let's set spacing parameters for where our PCA Application will neatly reside:

st.set_page_config(layout="wide")
scatter_column, settings_column = st.columns((4, 1))

# Let's name our collumns:

scatter_column.title("Multi-Dimentional Analysis")

settings_column.title("Settings")

# I've created a scatter plot using PCA1 x-axis & PCA2 y-axis to plot each point individually and then color them using a different categorical variable.

# I wanted to engineer the project around the goal of giving users the ability to input  data.

# We'll use an IF statement to setup functionality of our Web App:

uploaded_file = settings_column.file_uploader("Choose File")

if uploaded_file is not None:
    data_import = pd.read_csv(uploaded_file)
    pca_data, cat_cols, pca_cols = pca_maker(data_import)

    categorical_variable= settings_column.selectbox("Variable Select", options=cat_cols)
    categorical_variable_2= settings_column.selectbox("Second Variable Select", options=cat_cols)

    pca_1= settings_column.selectbox("First Principle Component", options=pca_cols, index=0)
    pca_cols.remove(pca_1)
    pca_2= settings_column.selectbox("Second Principle Component", options=pca_cols)

   

    scatter_column.plotly_chart(px.scatter(data_frame = pca_data, x = pca_1, y = pca_2, color = categorical_variable, template="simple_white", height=800, hover_data=[categorical_variable_2]), use_container_width= True)

else:
    scatter_column.header("Pleace Choose A File")