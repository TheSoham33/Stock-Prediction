import streamlit as st
from streamlit_lottie import st_lottie
import json

def app():
    st.title('Hello!')

    def load_lottiefile(filepath: str):
        with open(filepath, "r") as f:
            return json.load(f)



    with st.container():
        left_column, right_column= st.columns(2)
        with left_column:
            def load_lottiefile(filepath:str):
                with open(filepath,"r") as f:
                    return json.load(f)
            lottie_coding=load_lottiefile("lottiefiles/about.json")
            st_lottie(
            lottie_coding,
            speed=1,
            reverse=False,
            loop=True,
            quality="high",
            # renderer="svg",
            height="200px",
            width="300px",
            key=None,
            )
    
    st.write(
        """ 
        We developed this webapp for people who have a interest on the stock market and if you are just getting into it and you are developing a key interest,our webapp is the greatest option available for you.
        """
        )
