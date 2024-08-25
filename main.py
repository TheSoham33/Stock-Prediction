import Home
import stck2
import Stck3
import About_us
import streamlit as st
PAGES = {
    "Home": Home,
    "Fetch data from Yahoo": stck2,
    "Fetch data from csv file": Stck3,
    "About us": About_us
}
st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()
