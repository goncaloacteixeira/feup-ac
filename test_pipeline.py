def test(model, test_dataframe, features, target_variable):
    X_test = test_dataframe[features]
    y_pred = model.predict(X_test)

    test_dataframe[target_variable] = y_pred
    submission = test_dataframe[["loan_id", "status"]]
    submission = submission.rename(columns={"loan_id": "Id", "status": "Predicted"})

    submission.to_csv("results.csv", index=False)

    return submission
