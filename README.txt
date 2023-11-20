12 Data Sciences Web Apps projets with Python and Streamlit

1) Simple Stock Price

- Using yfinance to download Price of a ticker (Google, Microsoft, gold etc.. )
- Using line_chart to show Data

2) Simple Bioinformatics DNA Count

- Cover Photo using PIL
- Sequence Input
- 4 ways to display the output
    Dict
    text
    DataFrame
    Bar Chart

3) EDA (Exploratory Data Analysis) BasketBall

- The "NBA Player Stats Explorer" app performs simple web scraping of NBA player statistics data from Basketball-reference.com.
- Users can explore player statistics based on the selected year, team(s), and position(s).
- The app displays player stats of the selected team(s) in a DataFrame.
- It provides an option to download the displayed data in CSV format.
- Users can generate an intercorrelation matrix heatmap to visualize relationships between different statistics.

4) EDA (Exploratory Data Analysis) Football

- The "NFL Football Stats (Rushing) Explorer" app performs simple web scraping of NFL Football player stats data, with a focus on rushing statistics.
- Users can explore rushing stats based on the selected year, team(s), and position(s).
- The app displays player rushing stats of the selected team(s) in a DataFrame.
- It provides an option to download the displayed rushing stats data in CSV format.
- Users can generate an intercorrelation matrix heatmap to visualize relationships between different rushing statistics.


5) EDA (Exploratory Data Analysis) S&P 500

- The "S&P 500 App" retrieves the list of S&P 500 companies from Wikipedia and provides an analysis of their stock closing prices (year-to-date).
- Users can select specific sectors to explore and display companies within those sectors.
- The app allows users to download the displayed S&P 500 data in CSV format.
- Users can choose the number of companies to visualize and view the closing price plots for the selected companies.




6) Crypto Price App

- The "Crypto Price App" retrieves cryptocurrency prices for the top 100 cryptocurrencies from CoinMarketCap.
- Users can select the currency for price display (USD, BTC, ETH) and choose specific cryptocurrencies to analyze.
- The app provides options to download the displayed cryptocurrency data in CSV format.
- Users can customize the number of top coins to display, select the percent change time frame (7 days, 24 hours, 1 hour), and sort values if needed.
- The app includes a bar plot of the percent price change for the selected time frame.



Certainly! Here's the README section for your Streamlit app for Iris Flower Classification:

7) Iris Flower Classification App

- The "Iris Flower Classification App" predicts the type of Iris flower based on user-input parameters using a Random Forest Classifier.
- Users can adjust the sepal length, sepal width, petal length, and petal width using sliders in the sidebar to make predictions.
- The app displays the user input parameters, the predicted class label, and the prediction probabilities for each class.




8) Penguin Species Classification
This section of the repository focuses on the classification of Palmer Penguin species using a RandomForestClassifier. It consists of two main files:

Penguin Model Training (penguin_model_training.py):

- Loads the cleaned penguin dataset and performs feature encoding.
- Encodes ordinal features like 'sex' and 'island' using one-hot encoding.
- Converts the target variable 'species' into numerical values.
- Trains a RandomForestClassifier on the preprocessed data.
- Saves the trained model as 'penguins_clf.pkl' using the pickle library.

Penguin Prediction App (penguin_classification_app.py):

- Utilizes Streamlit to create an interactive web application for predicting penguin species.
- Allows users to upload a CSV file with penguin features or manually input feature values.
- Displays the user input features, predicts the penguin species, and shows prediction probabilities.
- Integrates the pre-trained RandomForestClassifier (penguins_clf.pkl) to make predictions.

9) Boston House Price Prediction App

- The app showcases user-input parameters, which are then used to predict the median value of owner-occupied homes (MEDV).
- A RandomForestRegressor model is trained on the Boston Housing dataset to make predictions.
- The app employs SHAP (SHapley Additive exPlanations) values to interpret and visualize feature importance.
- Users can observe the predicted house price and explore feature importance plots.

10) Molecular Solubility Prediction Web App

The "Molecular Solubility Prediction Web App" predicts the solubility (LogS) values of molecules based on their SMILES input. This app utilizes molecular descriptors to estimate solubility, with data obtained from John S. Delaney's research on estimating aqueous solubility directly from molecular structure.

Usage:

- Enter the SMILES input for the molecules in the sidebar.
- Observe the calculated molecular descriptors for the input molecules.
- The app utilizes a pre-built model to predict LogS values for the provided molecules.
- View the predicted LogS values.