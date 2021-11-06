import test_pipeline as test_pl
import train_pipeline as train_pl
import data_prep as dp

if __name__ == "__main__":
    feature_cols_loans = ["amount",
                          "duration",
                          "payments",
                          "loan_year",
                          "loan_month",
                          "loan_day",
                          ]
    target = "status"

    loans_df_train = dp.data_prep("train")
    loans_df_test = dp.data_prep("test")

    model = train_pl.train(loans_df_train, feature_cols_loans, target)
    submission = test_pl.test(model, loans_df_test, feature_cols_loans, target)
