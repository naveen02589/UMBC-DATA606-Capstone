# 1. Title and Author

### Project Title
Traffic Prediction Analysis

### Prepared for
UMBC Data Science Master Degree Capstone by Dr. Chaojie (Jay) Wang - SPRING 2024 Semester

### Author Name
Naveen Reddy Garlapati

### Profiles and Presentations
- **GitHub Profile:** https://github.com/naveen02589
- **Linkedin Profile:** https://www.linkedin.com/in/naveen-reddy-garlapati/

# 2. Background

### What is the Project about?

The core objective of this project is to develop a **Traffic Prediction Analysis** using data-driven techniques and machine learning models. The system is designed to derive insights from this analysis and then build a model that can be used to predict likelihood of traffic at particular times at different junctions in the city.

### Why does it matter?

- **Optimizing Traffic Flow:** Predicting traffic patterns helps optimize traffic flow by allowing authorities to implement strategies such as adjusting signal timings, optimizing routes, or deploying resources to alleviate congestion.
- **Reducing Commute Times:** By accurately predicting traffic conditions, commuters can plan their routes more effectively, potentially reducing commute times and enhancing overall productivity.
- **Enhancing Safety:** Anticipating traffic conditions enables authorities to implement measures to address potential safety hazards and reduce the likelihood of accidents.

### What are your research questions?

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

# Target/Label in ML Model
The primary target for the machine learning models in this project is the Vehicles. 

# Features/Predictors for ML Models
Key feature and predictor that will be used in the machine learning models for this project include: 
- Junction
- DateTime (and its derived attributes)

# EDA

# Model Training

 ## Models for Predictive Analytics:

 ## Training Procedure:

 ## Python Packages:

 ## Development Environments:

# Link to Presentation:
 - Presentation - https://github.com/naveen02589/UMBC-DATA606-Capstone/blob/main/docs/Traffic%20Prediction.pptx
# Web App Development:
Developed and deployed web application using streamlit for users to interact with it and get the forecasting of traffic
 - Streamlit Cloud link : https://forecasttraffic.streamlit.app/

# Conclusion
   

