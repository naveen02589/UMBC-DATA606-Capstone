from math import ceil
from tqdm import tqdm
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import pickle
import matplotlib.pyplot as plt
import seaborn as sns
import gc
import streamlit as st
import datetime
import requests
traffic_data = pd.read_csv(r'https://raw.githubusercontent.com/naveen02589/UMBC-DATA606-Capstone/main/data/traffic_clean.csv')
traffic_data.drop('ID', axis=1, inplace=True)

columns_to_drop1 = ['Quartermedian_vehicles', 'day_of_weekmin_vehicles', 'Quartermax_vehicles', 'Quarter', 'Quartermin_vehicles', 'day_of_weekmedian_vehicles', 'Vehicles', 'Seconds', 'Junction']
columns_to_drop2 = ['Year', 'Quartermax_vehicles', 'Quartermedian_vehicles', 'day_of_weekmedian_vehicles', 'day_of_weekmin_vehicles', 'Quartermin_vehicles', 'Quarter', 'Vehicles', 'Seconds', 'Junction']
columns_to_drop3 = ['Quartermax_vehicles', 'Quarter', 'Monthmax_vehicles', 'Monthmin_vehicles', 'Timemedian_vehicles', 'Quarterstd_vehicles', 'Timemin_vehicles', 'Year', 'Quartermedian_vehicles', 'day_of_weekmedian_vehicles', 'day_of_weekmean_vehicles', 'day_of_weekmin_vehicles', 'day_of_weekmax_vehicles', 'Quartermean_vehicles', 'day_of_monthmin_vehicles', 'Quartermin_vehicles', 'Vehicles', 'Seconds', 'Junction']
columns_to_drop4 = ['Quarter', 'day_of_weekmin_vehicles', 'Monthmin_vehicles', 'day_of_weekmedian_vehicles', 'Year', 'Quartermedian_vehicles', 'Quartermean_vehicles', 'Quartermin_vehicles', 'Quartermax_vehicles', 'day_of_year', 'Quarterstd_vehicles', 'Month', 'Monthmean_vehicles', 'Vehicles', 'Seconds', 'Junction']

models = {}

for i in range(1, 5):
	url = f"https://raw.githubusercontent.com/naveen02589/UMBC-DATA606-Capstone/main/models/junction{i}_model.pkl"
	# Download the file
	response = requests.get(url)
	response.raise_for_status()  # Ensure that the download was successful
	# Load the model from the downloaded content
	models[i] = pickle.loads(response.content)

def welcome_message():
    return "Welcome to the Traffic Prediction System"

def compute_traffic_prediction(junction, datetime_input):
    cols = ['DateTime', 'Junction', 'Year', 'Month', 'day_of_month', 'day_of_week', 'Date', 'Time', 'day_of_year']
    new_data = pd.DataFrame(columns=cols)
    print("datetime_input:", datetime_input)
    print("Type of datetime_input:", type(datetime_input))
    new_data['DateTime'] = pd.to_datetime(datetime_input)
    if not isinstance(datetime_input, (list, pd.Series)):
        datetime_input = [datetime_input]
  
    new_data['DateTime'] = pd.to_datetime(datetime_input)
    new_data['Year'] = new_data['DateTime'].dt.year
    new_data['Month'] = new_data['DateTime'].dt.month
    new_data['day_of_month'] = new_data['DateTime'].dt.day
    new_data['Junction'] = junction
    new_data['day_of_week'] = new_data['DateTime'].dt.dayofweek
    new_data['Date'] = new_data['DateTime'].dt.date
    new_data['Time'] = new_data['DateTime'].dt.hour
    new_data['day_of_year'] = new_data['DateTime'].dt.dayofyear
    new_data['Seconds'] = pd.to_timedelta(new_data['DateTime'].dt.strftime('%H:%M:%S')).dt.total_seconds().astype(int)
    new_data['DateTime'] = new_data['DateTime'].values.astype(np.int64) // 10 ** 9

    with open('Labelencoder.pkl', 'rb') as file:
        encoder = pickle.load(file)
    new_data['Date'] = encoder.fit_transform(new_data['Date'])

    merged_data = pd.concat([traffic_data, new_data], axis=0)

    def feature_aggregation(df):
        feature_set = ['Month', 'Quarter', 'day_of_month', 'day_of_week', 'Time', 'day_of_year']
        for feature in tqdm(feature_set):
            stats = df.groupby(feature)['Vehicles'].agg(['std', 'max', 'min', 'mean', 'median'])
            stats.columns = [f"{feature}{suffix}_vehicles" for suffix in stats.columns]
            stats = stats.astype({col: np.float32 for col in stats.columns})
            stats.reset_index(inplace=True)
            df = df.merge(stats, on=feature, how='left')
            gc.collect()
        return df

    new_data = feature_aggregation(merged_data).tail(len(new_data))
    
    columns_to_drop = [columns_to_drop1, columns_to_drop2, columns_to_drop3, columns_to_drop4][junction - 1]
    prediction_data = new_data.drop(columns_to_drop, axis=1).reset_index(drop=True)
    predictions = models[junction].predict(prediction_data)
    predictions = [ceil(num) for num in predictions]
    
    if isinstance(datetime_input, str):
        return predictions[0]
    else:
        return pd.DataFrame({'Number of Vehicles Predictions': predictions})

def main():
    st.title("Traffic Prediction Interface")
    welcome_html = """
    <div style="background-color:lightblue;padding:10px">
    <h2 style="color:white;text-align:center;">Traffic Prediction Interface</h2>
    </div>
    """
    st.markdown(welcome_html, unsafe_allow_html=True)

    # Similar UI setup as original with Streamlit widgets for input and predictions.
    # The processing for predictions would go here using the compute_traffic_prediction function.

def main():
    st.title("Traffic Prediction Interface")
    st.markdown(welcome_message(), unsafe_allow_html=True)

    # Sidebar for date and time input
    date = st.sidebar.date_input("Select Date", datetime.datetime.today())
    time = st.sidebar.time_input("Select Time", datetime.datetime.now())
    #datetime_input = datetime.datetime.combine(date, time)
    date_str = date.strftime("%Y-%m-%d")
    time_str = time.strftime("%H:%M:%S")
    datetime_input = date_str + ' ' + time_str
    datetime_input = pd.to_datetime(datetime_input)
    junction = st.sidebar.selectbox("Select Junction", options=[1, 2, 3, 4])

    if st.sidebar.button("Predict Traffic"):
        prediction = compute_traffic_prediction(junction, datetime_input)
        st.success("Traffic prediction completed successfully!")
        st.write(f"The predicted traffic at Junction {junction} on {date} at {time} is approximately: {prediction.iloc[0, 0]} \u00B1 4 vehicles.")

    # File uploader for batch predictions
    with st.expander("Upload CSV for batch predictions"):
        uploaded_file = st.file_uploader("Choose a file", type="csv")
        if uploaded_file is not None:
            data = pd.read_csv(uploaded_file)
            data['DateTime'] = pd.to_datetime(data['DateTime'])
            predictions = compute_traffic_prediction(junction, data['DateTime'])
            print(type(data['DateTime'].iloc[0]))
            st.write("Batch predictions processed successfully.")
            forecast_predictions = pd.concat([data, predictions], axis=1)
            st.dataframe(forecast_predictions)
            
            st.download_button("Download Predictions", data=forecast_predictions.to_csv(), file_name='batch_predictions.csv', mime='text/csv')
    # Real-time forecasting range
    with st.expander("Real-time forecasting"):
        start_date = st.date_input("Start Date", datetime.datetime.today())
        start_time = st.time_input("Start Time", datetime.datetime.now().time())
        end_date = st.date_input("End Date", datetime.datetime.today())
        end_time = st.time_input("End Time", datetime.datetime.now().time())
        
        startdate_str = start_date.strftime("%Y-%m-%d")
        starttime_str = start_time.strftime("%H:%M:%S")
        start_datetime = startdate_str + ' ' + starttime_str
        #start_datetime = pd.to_datetime(start_datetime)
        
        enddate_str = end_date.strftime("%Y-%m-%d")
        endtime_str = end_time.strftime("%H:%M:%S")
        end_datetime= enddate_str + ' ' + endtime_str
        #end_datetime = pd.to_datetime(end_datetime)
  
        forecast_range = pd.date_range(start=start_datetime, end=end_datetime, freq='H')
        
        if st.button("Generate Forecast"):
            forecast_range_junc = pd.DataFrame({'DateTime': forecast_range})
            forecast_range_junc['DateTime'] = pd.to_datetime(forecast_range_junc['DateTime'])
            print(type(forecast_range_junc['DateTime'].iloc[0]))
            forecast_predictions = compute_traffic_prediction(junction, forecast_range_junc['DateTime'])
            st.success("Forecast generated successfully!")
            forecast_predictions = pd.concat([forecast_range_junc, forecast_predictions], axis=1)
            st.dataframe(forecast_predictions)
            
            st.download_button("Download Forecast Data", data=forecast_predictions.to_csv(), file_name='forecast_data.csv', mime='text/csv')

            # Plotting the forecast
            plt.figure(figsize=(24, 10))
            sns.lineplot(data=forecast_predictions, x='DateTime', y='Number of Vehicles Predictions')
            st.pyplot(plt)
			
			
   
if __name__ == '__main__':
    main()
