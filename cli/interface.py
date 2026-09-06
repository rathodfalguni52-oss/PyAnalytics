import argparse

def create_parser():
    parser=argparse.ArgumentParser(description="PyAnalytics - Data Processing Tool")
    parser.add_argument(
        "--file",
        required=True,
        help="Path to CSV or JSON file"
    )

    return parser

def get_argument():
    parser=create_parser()
    return parser.parse_args()