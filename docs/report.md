# 1. Traffic Prediction System

- **Project Title:** Traffic Prediction Analysis
- **Prepared for:** UMBC Data Science Master Degree Capstone by Dr. Chaojie (Jay) Wang - SPRING 2024 Semester
- **Author:** Naveen Reddy Garlapati
- **GitHub Profile:** https://github.com/naveen02589
- **Linkedin Profile:** https://www.linkedin.com/in/naveen-reddy-garlapati/
-  **Powerpoint Presentation:** https://github.com/naveen02589/UMBC-DATA606-Capstone/blob/main/docs/606_CapstoneProject.pptx
-  **Youtube video:** https://youtu.be/a8xQaagL6MA
-  **Application Interface:** https://forecasttraffic.streamlit.app/

# 2. Background
The core objective of this project is to develop a **Traffic Prediction Analysis** using data-driven techniques and machine learning models. The system is designed to derive insights from this analysis and then build a model that can be used to predict likelihood of traffic at particular times at different junctions in the city.

### Why does it matter?

- **Optimizing Traffic Flow:** Predicting traffic patterns helps optimize traffic flow by allowing authorities to implement strategies such as adjusting signal timings, optimizing routes, or deploying resources to alleviate congestion.
- **Reducing Commute Times:** By accurately predicting traffic conditions, commuters can plan their routes more effectively, potentially reducing commute times and enhancing overall productivity.
- **Enhancing Safety:** Anticipating traffic conditions enables authorities to implement measures to address potential safety hazards and reduce the likelihood of accidents.

### Research questions

1. How accurately can machine learning models predict traffic conditions at different junctions in the city?
2. What variables (e.g., time of day, junction) have the most significant impact on traffic patterns, and how can they be effectively incorporated into the prediction models?
3.  How do different machine learning algorithms compare in terms of their ability to predict traffic patterns, and which algorithms are most suitable for this task?
4. Can the developed models provide accurate real-time predictions of traffic conditions, and what are the challenges in implementing real-time prediction systems?

# 3. About Dataset

- **Data sources:** [Traffic Prediction Dataset on Kaggle](https://www.kaggle.com/datasets/fedesoriano/traffic-prediction-dataset)
- **Data size:** 1.68 MB
- **Data shape:** 
  - `Traffic.csv` - 48120 rows, 4 columns
- **Time period:** The datasets collectively cover a time span of (from 11/01/2015 to 06/30/2017), representing a comprehensive period of culinary trends and user interactions.
- **What does each row represent?**
  - This dataset contains 48.1k (48120) observations of the number of vehicles each hour in four different junctions. Each row in the dataset represents a single observation or data point captured at a specific time interval  for a particular junction

- **Data Dictionary:**
   Traffic.csv

| Column Name  | Data Type | Definition | Potential Values (Categorical) |
|--------------|-----------|---------------------------------------------------|--------------------------------|
| DateTime     | Categorical (Date) | Time at which sensors collected the traffic data at different junctions | '11/1/2015  12:00:00 AM' ...|
| Juction      | Numerical (Integer) | Identifier of the junction where the traffic was collected | 1, 2, 3, 4 |
| Vehicles     | Numerical (Integer) | Number of vehicles observed at the specified junction during the corresponding time interval | 6,9 ... |
| ID           | Categorical (Integer) | Unique Id of the sensor | 20151101001, 20151101031 ... |

- **Target/Label in ML Model**
The primary target for the machine learning models in this project is the Vehicles. 

- **Features/Predictors for ML Model**
Key feature and predictor that will be used in the machine learning models for this project include: 
- Junction
- DateTime (and its derived attributes)

# 4. Exploratory Data Analysis(EDA)

- There are no missing values and duplicate rows in the dataset. 

- Several new features were derived from the DateTime column to capture different aspects of time that might influence traffic patterns.
- Target encoding was applied to various time-based features to integrate aggregate statistics related to traffic volume (Vehicles). For each feature like Month, Quarter, day_of_month, day_of_week, Time, and day_of_year, aggregate statistics including standard deviation (std), maximum (max), minimum (min), mean, and median were computed. These statistics provide a comprehensive summary that helps the models understand typical traffic behaviors associated with these temporal features.

- Visualizations and statistics provided insights into traffic patterns, highlighting peak times and the impact of weather. .

### Visualizations
- 4.1 vehicular movement over time at different junctions
  
![image](https://github.com/naveen02589/UMBC-DATA606-Capstone/assets/30066521/0293f390-c69b-4e76-ba19-fda5d68a88d8)

- 4.2 vehicular movement by month at different junctions

![image](https://github.com/naveen02589/UMBC-DATA606-Capstone/assets/30066521/d6f29d96-a7d8-4b51-9c45-e8bd6e0afcd2)

- 4.3 vehicular movement by year at different junctions
![image](https://github.com/naveen02589/UMBC-DATA606-Capstone/assets/30066521/93446def-b582-4727-9d8b-3bdbdf9d5b6d)

- 4.4 Average vehicular movement by day of the month at different junctions
![image](https://github.com/naveen02589/UMBC-DATA606-Capstone/assets/30066521/2fd02815-c89b-4c40-9834-ccab943416e2)

- 4.5 Average vehicular movement by day of the week at different junctions
![image](https://github.com/naveen02589/UMBC-DATA606-Capstone/assets/30066521/f45feace-4d32-49f2-a1e7-85b13dac817e)

- 4.6 Average Hourly Traffic at Different Junctions

![image](https://github.com/naveen02589/UMBC-DATA606-Capstone/assets/30066521/769bcf18-0216-450a-b7ae-6ebd9a3f3d27)


# 5. Model Training

 ### Models for Predictive Analytics:

Experimented with various regressor models including ( linear regression, Lasso and Ridge, catboost, LGBM, Decision Tree, Random Forest, SVR) 
    
LightGBM models were trained separately for each junction to accommodate unique traffic patterns. Cross-validation and time series split techniques were utilized.

Performance was measured using RMSE, MAPE, and MAE.

### Python Packages:

- pandas and numpy for data manipulation.
- matplotlib and seaborn for data visualization.
- sklearn for model preparation and evaluation metrics like RMSE, MAPE, and MAE.
- lightgbm for building the regression models.
- pickle for saving the trained models for later use.

### Development Environments:

The project is developed using Jupyter Notebook, hosted on Google Colab, which provides a powerful cloud-based environment that supports interactive data analysis and collaborative features.
The models and scripts are also compatible with standard Python environments, ensuring they can be run locally or in other cloud environments as required.

 ### Training Procedure:

 - Models are trained using a time series approach specific to each junction, ensuring the temporal patterns are respected.
- Splitting the data into 80 - 20 for training and testing. A validation set is separated from the main dataset to evaluate the model's performance during the training phase.
- Dropped irrelevant columns for the model training.
- LightGBM, a gradient boosting framework, is utilized for its efficiency in handling large datasets and its ability to handle categorical features directly.

### How will you measure and compare the performance of the models?:

The performance of the models is primarily evaluated using three metrics: Root Mean Square Error (RMSE), Mean Absolute Percentage Error (MAPE), and Mean Absolute Error (MAE).
These metrics provide insights into the accuracy and reliability of the predictions, with lower values indicating better performance.

- Model Performance Summary:

| Model            | RMSE  | MAPE  |
|------------------|-------|-------|
| Linear Regression| 7.63  | 21.37%|
| Lasso            | 8.61  | 25.11%|
| Ridge            | 7.93  | 22.27%|
| CatBoost         | 6.74  | 18.65%|
| LightGBM         | 4.58  | 13.84%|
| XGBoost          | 4.71  | 14.60%|
| AdaBoost         | 5.93  | 20.24%|
| Gradient Boosting| 5.06  | 15.64%|
| Decision Tree    | 5.43  | 17.31%|
| Random Forest    | 4.91  | 15.18%|
| SVR              | 13.92 | 42.00%|
| Linear SVR       | 25.09 | 100.00%|


# 6. Application of Trained Models:

The trained models could be deployed in a traffic management system to provide real-time predictions and analytics, potentially integrated via a tool like Streamlit for easy access by city planners.

Developed and deployed web application using streamlit for users to interact with it and get the forecasting of traffic
 - Streamlit Cloud deployment of Application link : https://forecasttraffic.streamlit.app/

# 7. Conclusion
   The project demonstrates the potential of machine learning in enhancing traffic management. Limitations include the need for real-time data integration and potential biases in historical data.

The analysis indicates that Junction 1 is the most susceptible to traffic congestion. It is recommended that the traffic prediction application be used to monitor road conditions, particularly during peak traffic times. Motorists are advised to consider alternative routes, such as Junction 4, to avoid delays.

