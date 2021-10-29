import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics

loans_df = pd.read_csv("data/loan_train.csv", sep=";", parse_dates=["date"])

feature_cols_loans = ["account_id", "amount", "duration", "payments"]
X = loans_df[feature_cols_loans]
y = loans_df["status"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

# Create Decision Tree classifier object
clf = DecisionTreeClassifier()

# Train Decision Tree Classifier
clf = clf.fit(X_train, y_train)

# Predict the response for test dataset
y_pred = clf.predict(X_test)

# Model Accuracy, how often is the classifier correct?
print("Accuracy:", metrics.accuracy_score(y_test, y_pred))

loans_df_test = pd.read_csv("data/loan_test.csv", sep=";")
X_test = loans_df_test[feature_cols_loans]
y_pred = clf.predict(X_test)

loans_df_test["status"] = y_pred
submission = loans_df_test[["loan_id", "status"]]
submission = submission.rename(columns={"loan_id": "Id", "status": "Predicted"})

submission.to_csv("results.csv", index=False)

print(submission)
