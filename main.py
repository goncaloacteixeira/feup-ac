import test_pipeline as test_pl
import train_pipeline as train_pl
import data_prep as dp
import matplotlib.pyplot as plt
from sklearn import tree

if __name__ == "__main__":
    loans_df_train = dp.data_preprocessing(dp.data_prep("train"))
    loans_df_test = dp.data_preprocessing(dp.data_prep("test"))

    unwanted_features = ["status", "loan_id"]
    features = [x for x in list(loans_df_train) if x not in unwanted_features]

    target = "status"

    model = train_pl.train(loans_df_train, features, target)

    # tree.export_graphviz(model, out_file="graph.dot", feature_names=features)

    submission = test_pl.test(model, loans_df_test, features, target)
