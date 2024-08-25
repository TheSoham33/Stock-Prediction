# For data manipulation
import numpy as np
import yfinance as yf
import pandas as pd

# To plot
import matplotlib.pyplot as plt


# For web app
import streamlit as st

def app():
    st.title('Stock price prediction')

    
    try:
        # Defining date
        first = st.date_input("Enter start date: ")
        end = st.date_input("Enter end date: ")       
        user_input =st.text_input('Enter ticker name: ')

        if st.button('Submit'):
            # Fetching data
            df = yf.download(user_input, start=first, end= end)
            st.subheader('Data set')
            print(df)
            st.write(df)

            # Dropping low, close, volume, high coloumns
            df = df.drop(['Low'], axis='columns')
            df = df.drop(['Close'], axis='columns')
            df = df.drop(['Volume'], axis='columns')
            df = df.drop(['High'], axis='columns')

            # Reset index
            df = df.reset_index()
            st.subheader("Open price and Adj Close Price")
            st.write(df)
            print(df)

            st.header("Now we will predict Adj Close price from Open price : ")

            # Dropping open, adj close value and date values into array in a new variable
            Date1 = df.drop(['Open','Adj Close'], axis='columns')
            Date1 = Date1[Date1.columns[-1]].values
            print(Date1)

            # Dropping date coloumn from df
            df = df.drop(['Date'], axis='columns')

            df.shape

            # Checking null values
            df.isnull().sum()

            # Converting open and adj close values into array in x and y respectively
            X = df[df.columns[:-1]].values
            y = df[df.columns[-1]].values
            X.shape
            print(X)
            print(y)

            # Defining training and testing length
            split_percentage = 0.8
            split = int(split_percentage*len(df))

            
            # Train data set
            X_train = X[:split]
            y_train = y[:split]

            # Test data set
            X_test = X[split:]
            y_test = y[split:]

            # Splitting date 
            D1 = Date1[:split]
            D2 = Date1[split:]

            # Training model with linear regression
            from sklearn.linear_model import LinearRegression
            model = LinearRegression().fit(X_train, y_train)

            # Predicting X_test dataset
            y_pred = model.predict(X_test)

            # Storing actual and predicted adj close price value in df
            df = pd.DataFrame({'Date':D2, 'Actual':y_test, 'Predicted':y_pred})
            df.index = pd.to_datetime(df['Date'])
            df = df.drop(['Date'], axis='columns')
            st.subheader('Actual Adj Close price vs Predicted Adj Close price')
            st.write(df)
            print(df)

            # Actual adj close value graph
            fig1 = plt.figure(figsize=(12,6))
            plt.plot(df['Actual'])
            plt.xlabel('Date')
            plt.ylabel('Price')
            plt.show()
            st.subheader('Original Graph')
            st.pyplot(fig1)

            # Predicted adj closse value graph
            fig2 = plt.figure(figsize=(12,6))
            plt.plot(df['Predicted'],'green')
            plt.xlabel('Date')
            plt.ylabel('Price')
            plt.show()
            st.subheader('Predicted Graph')
            st.pyplot(fig2)

            # Actual vs preicted adj close value graph
            fig3 = plt.figure(figsize=(12,6))
            plt.plot(df['Actual'])
            plt.plot(df['Predicted'],'green')
            plt.xlabel('Date')
            plt.ylabel('Price')
            plt.show()
            st.subheader('Original Graph vs Predicted Graph')
            st.pyplot(fig3)

            try:
                # Checking accuracy
                from sklearn.metrics import mean_squared_error, r2_score
                print("Mean squared error:",mean_squared_error(y_test,y_pred))
                print("Root Mean squared error:",np.sqrt(mean_squared_error(y_test,y_pred)))
                R = ("r2 Score:",r2_score(y_test,y_pred))

            
                st.subheader("Prediction accuracy by R2 Score")
                st.write("R2 score near 1 means that the model is able to predict the data very well. Give more data for more accuracy.")
                st.write(R)

            except:
                st.error("Maybe there is any null data in the dataset so we can't calculate the R2 score ")
    except:
        st.text("Please enter data correctly to continue...")
    #An R2 score near 1 means that the model is able to predict the data very well. Keeping track of every single metric can get tedious, 
    # so we pick one or two metrics to evaluate our model. A good practice is to make sure that the mean squared error is low and the explained 
    # variance score is high.

            
            
