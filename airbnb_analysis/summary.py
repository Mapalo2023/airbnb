import pandas as pd
from IPython.display import display
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

class DataSummary:
    """
    A class to perform data summary on my Airbnb data.
    """
    def __init__(self, url):
        """
        Initializes the DataSummary object with the provided data.
        
        Parameters:
        data (pd.DataFrame): The data to be summarized.
        """
        self.data = pd.read_csv(url)


    def display_head(self):
        """
        Displays the first five rows of the data.
        
        Returns:
        None
        """
        display(self.data.head())

    def display_tail(self):
        """
        Displays the last five rows of the data.
        
        Returns:
        None
        """
        display(self.data.tail())


    def get_shape(self):
        """
        Returns the shape of the data (number of rows and columns).
        
        Returns:
        tuple: A tuple containing the number of rows and columns.
        """
        return self.data.shape


    def missing_value_percent(self):
        """
        Calculates and returns the percentage of missing values in the data.
        
        Returns:
        pd.Series: A Series containing the percentage of missing values for each column.
        """
        return self.data.isna().sum() / len(self.data) * 100


    def data_info(self):
        """
        Displays a brief summary of the data including data types and non-null value counts.
        
        Returns:
        None
        """
        self.data.info()
        

    def categorical_descriptive_statistics(self):
        """
        Computes descriptive statistics for categorical variables in the data.
        
        The result's index will include count, unique, top, and freq. Analyzes both 
        numeric and object series, as well as DataFrame columns.
        
        Returns:
        pd.DataFrame: Descriptive statistics of categorical variables.
        """
        return self.data.describe(include=['object'])

    def numerical_descriptive_statistics(self):
        """
        Computes descriptive statistics for numerical variables in the data.
        
        The result's index will include: count, mean, std, min, 25%, 50%, 75%, and max.
        
        Returns:
        pd.DataFrame: Descriptive statistics of numerical variables.
        """
        return self.data.describe()

    def data_types(self):
        """
        Returns the data types of each column in the data.
        
        Returns:
        pd.Series: A Series containing data types of each column.
        """
        return self.data.dtypes

