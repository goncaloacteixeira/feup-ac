import pandas as pd
import utils
from numpy import array
from sklearn.preprocessing import LabelEncoder


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

    # to join the dispositions table we could count, for each account, the number of disponents
    dispositions_df = pd.read_csv("data/disp.csv", sep=";")
    disponents = dispositions_df.groupby('account_id')['type'].apply(lambda x: (x == 'DISPONENT').sum()).reset_index(
        name='account_disponents')
    # add the owner id
    owners = dispositions_df[dispositions_df.type == "OWNER"][["account_id", "client_id"]].rename(
        columns={"client_id": "owner_id"})
    df = pd.merge(df, owners, on="account_id")
    df = pd.merge(df, disponents, on="account_id")

    # join clients data
    clients_df = pd.read_csv("data/client.csv", sep=";")
    clients_df = utils.parse_client_dates(clients_df).rename(columns={"client_id": "owner_id"})

    df = pd.merge(df, clients_df, on="owner_id")

    return df


def data_preprocessing(df):
    # integer encode
    label_encoder = LabelEncoder()

    frequency = df["frequency"]
    values = array(frequency)
    integer_encoded = label_encoder.fit_transform(values)
    df["frequency"] = integer_encoded

    return df
