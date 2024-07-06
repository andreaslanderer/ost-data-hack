import pandas as pd
import argparse
from sklearn.model_selection import train_test_split


def main(dataset):
   train_X, train_y = load_data(dataset)

def load_data(dataset):
    random_state = 42
    test_size = 0.2
    all_data = pd.read_csv(dataset)
    train_X, test_X, train_y, test_y = train_test_split(all_data.drop(columns=["NObeyesdad"]), all_data["NObeyesdad"], test_size=test_size, random_state=random_state)
    train_X.to_csv('datahack_train_X.csv')
    train_y.to_csv('datahack_test.csv')
    test_X.to_csv('datahack_train_X.csv')
    test_y.to_csv('datahack_test.csv')
    print(f"No samples: {len(all_data)} - split test_size={test_size} --> {(1-test_size)*100}% train, {test_size*100}% test")
    print(f"split random_seed = {random_state}")
    return train_X, train_y

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset", help="input dataset path", default="data/train.csv")
    args = parser.parse_args()
    main( args.dataset) 