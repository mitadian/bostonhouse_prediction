# Background and Overview
The Boston Housing dataset represents the 1970s Boston real estate market, combining environmental, structural, and socio-economic features such as crime, pollution, and housing characteristics. The objective is to predict median home values using multi-dimensional data while addressing known limitations like the capped target variable and historically biased features.

This project builds a supervised regression model to identify key price drivers and produce an interpretable, ethically aware real estate pricing model using modern machine learning practices. This helps buyers, sellers, and investors make informed decisions while highlighting which neighborhood and house characteristics drive value the most.

Insights and Recommendations are provided on the following areas:
- **House size drives the price:** The number of rooms (rm) has the strongest positive impact on house prices, making property size the most critical value lever
- **River proximity makes a significant price premium:** Houses located near the river (chas) are consistently valued higher, highlighting the importance of location-based amenities.
- **Neighborhood socioeconomic status affects prices:** A higher proportion of lower-status population (lstat) reduces the house prices, which acts as a risk
- **Education quality correlates with property value:** Higher student–teacher ratios (ptratio) are associated with lower house prices, suggesting education infrastructure influences demand.

An interactive app deployed with Streamlit can be accessed [here](https://bostonhouseprediction-bywwirtedm9mfdxjsovsi6.streamlit.app/)

# Data Structure Overview
This dataset provides a historical snapshot of the Boston housing market from the 1970s. It consists of 506 observations across 14 variables.
| Column   | Dtype   |
|----------|--------|
| crim     | float64|
| zn       | float64|
| indus    | float64|
| chas     | int64  |
| nox      | float64|
| rm       | float64|
| age      | float64|
| dis      | float64|
| rad      | int64  |
| tax      | int64  |
| ptratio  | float64|
| black    | float64|
| lstat    | float64|
| medv     | float64|

MEDV is the median value of owner-occupied homes in $1,000s. It represents the typical house price in a neighborhood, ignoring extreme outliers, and is the target variable we predict using features such as the number of rooms, crime rate, and proximity to the river.

# Insights
<img width="1780" height="480" alt="MEDV Scatterplots" src="https://github.com/user-attachments/assets/5d15f32a-4e85-41cb-963a-9505b2448c67" />

- **House Size (RM):** Houses with more rooms drive higher prices. Most Boston homes have 6–7 rooms, showing that size is the most significant price factor.  
- **Neighborhood Socioeconomic Status (LSTAT):** Higher percentages of lower-status populations correlate with lower house prices. Most neighborhoods range 5–15%, indicating many areas have a strong socioeconomic profile.  
- **Education Quality (PTRATIO):** Higher student-to-teacher ratios slightly reduce house prices. Most areas have a ratio around 20, suggesting moderate influence on pricing.  

<img width="1580" height="380" alt="MEDV Boxplot CHAS" src="https://github.com/user-attachments/assets/98073fd2-59f8-475d-b65a-1e06ccb003be" />

- **River Proximity (CHAS):** Houses near the river (CHAS=1) have higher prices than those farther away, indicating strong location-based premiums.

# Recommendations

- **Prioritize house size and location** in pricing and valuation models for higher accuracy.  
- **Leverage neighborhood socioeconomic data** to identify undervalued or high-risk areas.  
- **Consider education quality** as a secondary factor when making investment decisions.  
- **Handle skewed distributions and outliers** for predictive modeling improvements.  

