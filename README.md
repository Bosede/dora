# Telco Churn Analaysis

## Project Setup & Installation
- Create a virtual environment and activate it
```
$ python3 -m venv env
```
- Clone the project
```
$ git clone https://github.com/Bosede/dora
```
- Install requirements
```
$ pip install -r requirements.txt
```

## Overview
Telecommunication Companies (Telcos) cannot avoid churning customers. However, a deep dive into their data can help understand the reason for the churn and take steps to reduce the churn to the absolute minimum.

This project begins with an exploration of the telco data then proceeds with a segmentation of customers using the KMeans clustering algorithm. 

## Data
The data was sourced from AI Saturdays and includes 7043 observations of customers and features that describe their interaction with the telecommunication company's services. 


## Findings
In these observations, the telco suffered a 27% churn rate with low tenure customers more likely to churn. Using the KMeans algorithm, the customers were divided into five segments, and this prompted an investigation across segments. The customers in Cluster 1 were noticed to have the highest churn rate of 37%.

This type of deep dive analysis is important to maintaining profitability and competitive edge.