#Customer Lifetime Value (CLV) Prediction:

live render link: https://clv-prediction.onrender.com/

Overview
This project aims to predict Customer Lifetime Value (CLV) by analyzing customer purchasing patterns using machine learning models. We implement LSTM, Prophet, and ARIMA models to forecast future purchasing behavior and calculate the CLV.

Additionally, the project includes an interactive dashboard for customer analysis, deployed using Flask with Tableau embedded for visualization.

Project Workflow
1. Data Preprocessing
Cleaning and preparing customer purchase data.
Generating time-series features and handling missing values.
2. Model Training
ARIMA: Classical time-series forecasting model.
Prophet: A robust forecasting tool developed by Facebook for univariate data.
LSTM: Deep learning model designed for time-series predictions using sequential data.
3. Forecasting
Forecast customer credit points for 2015 using the best-performing model.
Calculate Customer Lifetime Value (CLV) using forecasted credit points, where CLV = Credit Points * 5000.
4. Deployment
Deployed using Flask as a web app.
Embedded Tableau Public dashboards for customer insights and visual analytics.
5. Visualization
The web app includes an interactive dashboard that provides insights into customer behavior and forecasts.
Includes a line chart comparing actual and forecasted credit points.
Features
Multiple forecasting models (ARIMA, Prophet, LSTM) to predict customer lifetime value.
Interactive Flask app with embedded Tableau for data visualization.
CLV Calculation: Forecasted credit points are used to calculate the CLV.
Tools/Technologies Used
Python for data analysis and modeling.
Flask for deploying the web application.
Jupyter Notebook for model development and experimentation.
Tableau Public for creating interactive visual dashboards.
