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

    # Add the account data
    accounts_df = pd.read_csv("data/account.csv", sep=";")
    accounts_dates = [utils.parse_date(i) for i in accounts_df["date"]]
    accounts_years = [x[0] for x in accounts_dates]
    accounts_months = [x[1] for x in accounts_dates]
    accounts_days = [x[2] for x in accounts_dates]
    # Add the new columns to the dataframe
    accounts_df["account_year"] = accounts_years
    accounts_df["account_month"] = accounts_months
    accounts_df["account_day"] = accounts_days
    # Drop the unnecessary column
    accounts_df = accounts_df.drop(columns="date", axis=1)
    accounts_df = accounts_df.rename(columns={"district_id": "account_district_id"})

    # merge loans with account data
    df = pd.merge(loans_df, accounts_df, on="account_id")

    return df
