import streamlit as st
import json
from streamlit_lottie import st_lottie

def app():
    
    st.title('Stock Market Prediction Using Machine Learning')
    st.header('What is Stock Market Predcition?')

    def load_lottiefile(filepath: str):
        with open(filepath, "r") as f:
            return json.load(f)



    with st.container():
            left_column, right_column= st.columns(2)
            with left_column:
                def load_lottiefile(filepath:str):
                        with open(filepath,"r") as f:
                            return json.load(f)
                lottie_coding=load_lottiefile("lottiefiles/questions.json")
                st_lottie(
                lottie_coding,
                speed=1,
                reverse=False,
                loop=True,
                quality="high",
                # renderer="svg",
                height="400px",
                width="300px",
                key=None,
                )
 
            st.write(
                """Stock market prediction is the act of trying to determine the future value of a company stock or other financial instrument traded on an exchange. The successful prediction of a stock's future price could yield significant profit. The efficient-market hypothesis suggests that stock prices reflect all currently available information and any price changes that are not based on newly revealed information thus are inherently unpredictable. Others disagree and those with this viewpoint possess myriad methods and technologies which purportedly allow them to gain future price information."""
)
                
            
            st.header('What do we do?')

            with st.container():
                    left_column, right_column= st.columns(2)
                    with left_column:
                        def load_lottiefile(filepath:str):
                                with open(filepath,"r") as f:
                                        return json.load(f)
                        lottie_coding=load_lottiefile("lottiefiles/graph.json")
                        st_lottie(
                        lottie_coding,
                        speed=1,
                        reverse=False,
                        loop=True,
                        quality="high",
                        # renderer="svg",
                        height="400px",
                        width="300px",
                        key=None,
                        )

                    st.write(
                            """
                            - We gather realtime data and previous data from the internet
                            - We also gather data from the .csv files.
                            - For a better understanding and analysis of the stock market we will show you three graphs which are as follows:
                                - Compare actual value vs Prediction value
                                - Original Graph
                                - Prediction Graph
                                - Original vs Prediction Graph
                            
                                """
                        )
            st.header("Advantages of Stock Market Prediction")
            with st.container():
                    left_column, right_column= st.columns(2)
                    with left_column:
                        def load_lottiefile(filepath:str):
                                with open(filepath,"r") as f:
                                        return json.load(f)
                        lottie_coding=load_lottiefile("lottiefiles/advan.json")
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
                    - Removes the Investment Bias
                    - Develops the Habit of Complete Analysis
                    - Minimizes Your Losses
                    - Assures Consistency
                    """

            )
            st.header("How to use this WebApp?")
            with st.container():
                        left_column, right_column= st.columns(2)
                        with left_column:
                                def load_lottiefile(filepath:str):
                                        with open(filepath,"r") as f:
                                                return json.load(f)
                        lottie_coding=load_lottiefile("lottiefiles/how.json")
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
                    You can gather data by using two techniques in our webapp:-
                     - To fetch the data from Yahoo server head over to the navigation panel and select "Fetch data from Yahoo" option
                    - To fetch the data from .csv file head over to the navigation panel and select "Fetch data from .csv file" option
                    """
            )
  