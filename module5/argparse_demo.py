import argparse


parser = argparse.ArgumentParser(description="Process some integers.")
parser.add_argument('filename', type=str, help="The file to process")
args = parser.parse_args()
print(f"Processing {args.filename}")