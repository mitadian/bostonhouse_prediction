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

# Executive Summary

(right into the juicy price)

# Insight Deep Dive
(more deep into executive summary)

# Recommendations
