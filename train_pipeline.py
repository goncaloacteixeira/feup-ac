from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics


def train(dataframe, features, target_variable):
    X = dataframe[features]
    y = dataframe[target_variable]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=1)

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
