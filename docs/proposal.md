# 1. Title and Author

### Project Title
Traffic Prediction Analysis

### Prepared for
UMBC Data Science Master Degree Capstone by Dr. Chaojie (Jay) Wang

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
2. What variables (e.g., time of day, weather conditions, special events) have the most significant impact on traffic patterns, and how can they be effectively incorporated into the prediction models?
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

### Data Dictionary for Traffic Prediction Dataset

#### Traffic.csv
- **Purpose:** Provides comprehensive information about each recipe, including ingredients, cooking steps, and nutritional details.
- **Columns:**
  - **I. DateTime**
    - **Dtype:** Categorical (Data)
    - **Definition:** Time at which sensors collected the traffic data at different junctions
    - **Potential Values:** Dates ranging from 2015 to 2017
  - **II. Juction**
    - **Dtype:** Numerical (Integer)
    - **Definition:** Identifier of the junction where the traffic was collected
    - **Potential Values:** 4 unique values
  - **III. Vehicles**
    - **Dtype:** Numerical (Integer)
    - **Definition:** Number of vehicles observed at the specified junction during the corresponding time interval 
  - **IV.  ID**
    - **Dtype:** Categorical (Integer)
    - **Definition:** Unique Id of the sensor
  
# Target/Label in ML Model
The primary target for the machine learning models in this project is the Vehicles. 

# Features/Predictors for ML Models
Key feature and predictor that will be used in the machine learning models for this project include: DateTime derived attributes
