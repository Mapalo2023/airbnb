import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

class Inference:
    """
    A class to perform inference analysis on my Airbnb data.
    """
    def __init__(self, url):
        """
        Initializes the Inference object with data from the specified URL.
        
        Parameters:
        url (str): The URL where the CSV data file is located.
        """
        self.data = pd.read_csv(url)

    def scatter_plot_price_minimum_nights(self):
        """
        Creates a scatter plot between the 'price' and 'minimum_nights' columns of the data.
        """
        self.data.plot.scatter(x='price', y='minimum_nights', title="minimum_nights")
        
    def scatter_plot_price_minimum_nights_seaborn(self):
        """
        Creates a scatter plot between the 'price' and 'minimum_nights' columns of the data using Seaborn.
        
        Returns:
        - None. Displays the plot.
        """
        plt.figure(figsize=(10, 6))
        sns.scatterplot(data=self.data, x='price', y='minimum_nights')
        plt.title("Scatter plot of Price vs Minimum Nights")
        plt.show()

    def scatter_plot_minimum_nights_number_of_reviews(self):
        """
        Creates a scatter plot between the 'minimum_nights' and 'number_of_reviews' columns of the data.
        """
        self.data.plot.scatter(x='minimum_nights', y='number_of_reviews', title="minimum_nights")
        
    
    def scatter_plot_minimum_nights_number_of_reviews_seaborn(self):
        """
        Creates a scatter plot between the 'minimum_nights' and 'number_of_reviews' columns of the data using Seaborn.
        
        Returns:
        - None. Displays the plot.
        """
        plt.figure(figsize=(10, 6))
        sns.scatterplot(data=self.data, x='minimum_nights', y='number_of_reviews')
        plt.title("Scatter plot of Minimum Nights vs Number of Reviews")
        plt.show()

        
    def catplot_price_neighbourhood(self, figsize=(10, 6)):
        """
        Creates a categorical scatter plot between the 'price' and 'neighbourhood' columns of the data.
        
        Parameters:
        - figsize (tuple): Specifies the figure size. Default is (10, 6).
        
        Returns:
        - None. Displays the plot.
        """
        warnings.simplefilter(action='ignore', category=FutureWarning)
        
        plt.figure(figsize=figsize)
        sns.catplot(data=self.data, x="price", y="neighbourhood", alpha=0.6, height=figsize[1], aspect=figsize[0]/figsize[1])
        plt.xscale('log')  # Set log scale on x-axis for better visualization if data is skewed
        plt.title("Categorical scatter plot of Price vs Neighbourhood")
        plt.show()

    def catplot_price_room_type(self, figsize=(10, 6)):
        """
        Creates a categorical scatter plot between the 'price' and 'room_type' columns of the data.
        
        Parameters:
        - figsize (tuple): Specifies the figure size. Default is (10, 6).
        
        Returns:
        - None. Displays the plot.
        """
        warnings.simplefilter(action='ignore', category=FutureWarning)
        
        plt.figure(figsize=figsize)
        sns.catplot(data=self.data, x="price", y="room_type", alpha=0.6, height=figsize[1], aspect=figsize[0]/figsize[1])
        plt.xscale('log')  # Set log scale on x-axis for better visualization if data is skewed
        plt.title("Categorical scatter plot of Price vs Room Type")
        plt.show()
        
    def crosstab_room_type_neighbourhood(self):
        """
        Computes a crosstab of counts between the 'room_type' and 'neighbourhood' columns of the data.

        Returns:
        - crosstab (DataFrame): The computed crosstab DataFrame.
        """
        crosstab = pd.crosstab(index=self.data['room_type'], columns=self.data['neighbourhood'])
        return crosstab
    
    def plot_crosstab_bar(self):
        """
        Computes a crosstab of counts between the 'room_type' and 'neighbourhood' columns of the data,
        and creates a bar plot of this crosstab.

        Returns:
        - ax (Axes): The axes object with the plot.
        """
        crosstab = pd.crosstab(index=self.data['room_type'], columns=self.data['neighbourhood'])
        ax = crosstab.plot.bar(figsize=(12, 7), rot=0)
        ax.set(ylabel='Count', title='Neighbourhood vs. Room Type')
        ax.legend(title='Neighbourhood', bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.tight_layout()
        plt.show()
        return ax
    
    def catplot_price_room_type_neighbourhood(self):
        """
        Creates a categorical bar plot displaying the average price for each room type,
        separated by neighbourhood.

        Returns:
        - g (FacetGrid): The Seaborn FacetGrid object with the plot.
        """
        g = sns.catplot(x='price', y='room_type', hue='neighbourhood', kind='bar', data=self.data, legend=False)
        g.fig.set_figwidth(12)
        g.fig.set_figheight(7)
        g.ax.legend(title='Neighbourhood', bbox_to_anchor=(1.05, 1), loc='upper left')
        g.set_axis_labels("Average Price", "Room Type")
        return g