import pandas as pd
import csv

def get_restaurants_df():
  """
    Get restaurants dataframe from csv file
    
    Parameters
    ----------
    None
    

    Returns
    -------
    restaurants_df: DataFrame
    
  """
  restaurants_df = pd.read_csv('data/restaurants.csv')
  restaurants_df.drop(columns=['Unnamed: 0'], inplace=True)
  return restaurants_df

def get_user_reviews_df():
  """
    Get users dataframe from csv file
    
    Parameters
    ----------
    None
    

    Returns
    -------
    users_df: DataFrame
    
  """
  user_reviews_df = pd.read_csv('data/user_reviewss.csv', encoding='utf-8')
  user_reviews_df.drop(columns=['Unnamed: 0'], inplace=True)
  return user_reviews_df