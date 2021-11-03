import pandas as pd


def test(model):
    feature_cols_loans = ["amount", "duration", "payments"]
    loans_df_test = pd.read_csv("data/loan_test.csv", sep=";")
    X_test = loans_df_test[feature_cols_loans]
    y_pred = model.predict(X_test)

    loans_df_test["status"] = y_pred
    submission = loans_df_test[["loan_id", "status"]]
    submission = submission.rename(columns={"loan_id": "Id", "status": "Predicted"})

    submission.to_csv("results.csv", index=False)

    return submission
