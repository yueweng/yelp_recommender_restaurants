# Restaurant Recommender using Yelp Dataset

### Getting the data
Yelp provides an API where I can query the businesses. In this project, I am focusing on getting the restaurants and so I limit my request to just restaurants and to the San Francisco area. I set up an app on Yelp and was given an API Key. Using that, I am able to start querying the results from the Yelp API

### Connecting to MongoDB
Once I got the data, I stored the data into a MongoDB Database

### Cleaning the data
The data collected from Yelp has different formatting. In order to understand and parse the data, I have to unpack the data, convert them into a list or dictionary in the format I want and saved it into a dataframe. Certain columns include string values and in order for data processing, I have to dummify the values.