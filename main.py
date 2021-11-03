import test_pipeline as test_pl
import train_pipeline as train_pl
import pandas as pd

if __name__ == "__main__":
    feature_cols_loans = ["amount", "duration", "payments"]
    target = "status"
    loans_df = pd.read_csv("data/loan_train.csv", sep=";", parse_dates=["date"])
    loans_test_df = pd.read_csv("data/loan_test.csv", sep=";", parse_dates=["date"])

    model = train_pl.train(loans_df, feature_cols_loans, target)
    submission = test_pl.test(model, loans_test_df, feature_cols_loans, target)
