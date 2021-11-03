import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics


def train():
    loans_df = pd.read_csv("data/loan_train.csv", sep=";", parse_dates=["date"])

    feature_cols_loans = ["amount", "duration", "payments"]
    X = loans_df[feature_cols_loans]
    y = loans_df["status"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

    print("Training data...")

    # Create Decision Tree classifier object
    clf = DecisionTreeClassifier()

    # Train Decision Tree Classifier
    clf = clf.fit(X_train, y_train)

    # Predict the response for test dataset
    y_pred = clf.predict(X_test)

    # Model Accuracy, how often is the classifier correct?
    print("Accuracy:", metrics.accuracy_score(y_test, y_pred))

    # return the model
    return clf
