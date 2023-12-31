# cli.py

import argparse
import os
from airbnb_analysis.analysis import ExploratoryDataAnalysis
from airbnb_analysis.inference import Inference
from airbnb_analysis.summary import DataSummary
import pandas as pd

ARG_DEFAULTS = {
    'data_path': os.path.join(os.path.dirname(__file__), '..', 'data', 'listings.csv'),
}

def generate_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Airbnb Data Analysis.")
    
    parser.add_argument("--data-path", type=str, default=ARG_DEFAULTS['data_path'],
                        help="Path to the Airbnb dataset CSV file. Defaults to %(default)s")
    parser.add_argument("--action", type=str, choices=['summary', 'eda', 'inference'], 
                        required=True, help="The type of analysis to perform: summary, eda, or inference.")
    parser.add_argument("--column", type=str, 
                        help="The column to analyze (required for some actions).")
    
    return parser
 
def main(argv=None):
    parser = generate_parser()
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
        
    elif args.action == 'eda':
        eda = ExploratoryDataAnalysis(data)
        if args.column:
            if args.column == 'neighbourhood':
                eda.bar_plot_neighbourhood()
            elif args.column == 'room_type':
                eda.bar_plot_room_type()
            elif args.column == 'price':
                eda.plot_price_distribution()
        elif args.column == 'minimum_nights':
            if args.plot_type == 'boxplot':
                eda.plot_minimum_nights_distribution()
            elif args.plot_type == 'histogram':
                eda.plot_minimum_nights_distribution_seaborn()
            else:
                print("Invalid plot type specified for minimum_nights")
        elif args.column == 'number_of_reviews':
            if args.plot_type == 'boxplot':
                eda.plot_number_of_reviews_distribution()
            elif args.plot_type == 'histogram':
                eda.plot_number_of_reviews_distribution_seaborn()
            else:
                print("Invalid plot type specified for number_of_reviews")
        else:
            print("Column name required for this action.")        
        
    elif args.action == 'inference':
        inference = Inference(data)
        if args.column:
            if args.column == 'price':
                print(inference.hypothesis_test_price_room_type())
        else:
            parser.print_help()
