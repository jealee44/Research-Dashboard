import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Import data from data.py
from data import df_alif_tlif, df_olif_xlif

# Streamlit App
st.title("Spinal Surgery Outcomes Dashboard")

# Sidebar
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["ALIF PPF vs TLIF PSI", "OLIF vs XLIF"])

if page == "ALIF PPF vs TLIF PSI":
    st.header("ALIF PPF vs TLIF PSI Outcomes")
    
    st.subheader("Revision Rates")
    fig, ax = plt.subplots()
    sns.barplot(x='Cohort', y='Revision_rate', data=df_alif_tlif, ax=ax)
    st.pyplot(fig)
    
    st.subheader("Time to Revision (days)")
    fig, ax = plt.subplots()
    sns.boxplot(x='Cohort', y='Time_to_revision_days', data=df_alif_tlif, ax=ax)
    st.pyplot(fig)
    
    st.subheader("PI-LL Mismatch Correction")
    fig, ax = plt.subplots()
    sns.barplot(x='Cohort', y='PI_LL_mismatch_correction', data=df_alif_tlif, ax=ax)
    st.pyplot(fig)
    
    st.subheader("ODI Improvement")
    fig, ax = plt.subplots()
    sns.boxplot(x='Cohort', y='ODI_improvement', data=df_alif_tlif, ax=ax)
    st.pyplot(fig)
    
    st.subheader("VAS Improvement")
    fig, ax = plt.subplots()
    sns.boxplot(x='Cohort', y='VAS_improvement', data=df_alif_tlif, ax=ax)
    st.pyplot(fig)
    
elif page == "OLIF vs XLIF":
    st.header("OLIF vs XLIF Outcomes")
    
    st.subheader("Revision Rates")
    fig, ax = plt.subplots()
    sns.barplot(x='Cohort', y='Revision_rate', data=df_olif_xlif, ax=ax)
    st.pyplot(fig)
    
    st.subheader("Time to Revision (days)")
    fig, ax = plt.subplots()
    sns.boxplot(x='Cohort', y='Time_to_revision_days', data=df_olif_xlif, ax=ax)
    st.pyplot(fig)
    
    st.subheader("PI-LL Mismatch Correction")
    fig, ax = plt.subplots()
    sns.barplot(x='Cohort', y='PI_LL_mismatch_correction', data=df_olif_xlif, ax=ax)
    st.pyplot(fig)
    
    st.subheader("ODI Improvement")
    fig, ax = plt.subplots()
    sns.boxplot(x='Cohort', y='ODI_improvement', data=df_olif_xlif, ax=ax)
    st.pyplot(fig)
    
    st.subheader("VAS Improvement")
    fig, ax = plt.subplots()
    sns.boxplot(x='Cohort', y='VAS_improvement', data=df_olif_xlif, ax=ax)
    st.pyplot(fig)
