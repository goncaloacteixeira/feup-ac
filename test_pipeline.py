def test(model, test_dataframe, features, target_variable):
    X_test = test_dataframe[features]

    probs = model.predict_proba(X_test)[:, -1]

    test_dataframe[target_variable] = probs
    submission = test_dataframe[["loan_id", "status"]]
    submission = submission.rename(columns={"loan_id": "Id", "status": "Predicted"})

    submission.to_csv("results.csv", index=False)

    return submission
