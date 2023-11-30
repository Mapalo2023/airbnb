# cli.py
import argparse
from airbnb_analysis.analysis import ExploratoryDataAnalysis
from airbnb_analysis.inference import Inference
from airbnb_analysis.summary import DataSummary
import pandas as pd
import os

def main(argv=None):
    parser = argparse.ArgumentParser(description="Airbnb Data Analysis.")
    # Set the default data path to the data/listings.csv relative to the script location
    default_data_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'listings.csv')
    parser.add_argument("--data-path", type=str, default=default_data_path, help="Path to the Airbnb dataset CSV file.")
    parser.add_argument("--action", type=str, choices=['summary', 'eda', 'inference'], required=True, help="The type of analysis to perform: summary, eda (exploratory data analysis), or inference.")
    parser.add_argument("--column", type=str, help="The column to analyze (required for some actions).")
    args = parser.parse_args(argv)

    # Load data
    data = pd.read_csv(args.data_path)

    # Perform action based on the user's choice
    if args.action == 'summary':
        summary = DataSummary(data)
        summary.data_info()
        if args.column:
            print(summary.statistical_summary(args.column))
        else:
            print("Column name required for this action.")
        pass
    elif args.action == 'eda':
        eda = ExploratoryDataAnalysis(data)
        if args.column:
            if args.column == 'neighbourhood':
                eda.bar_plot_neighbourhood()
            elif args.column == 'room_type':
                eda.bar_plot_room_type()
            elif args.column == 'price':
                eda.plot_price_distribution()
        pass
    elif args.action == 'inference':
        inference = Inference(data)
        if args.column:
            if args.column == 'price':
                print(inference.hypothesis_test_price_room_type())
        pass
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
