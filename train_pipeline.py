from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics


def train(dataframe, features, target_variable):
    X = dataframe[features]
    y = dataframe[target_variable]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

    print("Training data...")

    # Create Decision Tree classifier object
    clf = DecisionTreeClassifier(min_samples_leaf=10)

    # Train Decision Tree Classifier
    clf = clf.fit(X_train, y_train)

    # Predict the response for test dataset
    y_pred = clf.predict_proba(X_test)[:, -1]

    # Model Area Under the Curve, the higher the better
    auc = metrics.roc_auc_score(y_test, y_pred)
    print("AUC Score: ", auc)

    # return the model and the data used to test
    return clf
