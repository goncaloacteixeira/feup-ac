import pandas as pd
import utils


def data_prep(data_type):
    # process loans data
    loans_df = pd.read_csv("data/loan_" + data_type + ".csv", sep=";")
    loans_dates = [utils.parse_date(i) for i in loans_df["date"]]
    loans_years = [x[0] for x in loans_dates]
    loans_months = [x[1] for x in loans_dates]
    loans_days = [x[2] for x in loans_dates]

    # Add the new columns to the dataframe
    loans_df["loan_year"] = loans_years
    loans_df["loan_month"] = loans_months
    loans_df["loan_day"] = loans_days

    # Drop the unnecessary column
    loans_df = loans_df.drop(columns="date", axis=1)

    return loans_df
