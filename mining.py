from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neural_network import MLPClassifier


def cross_validation(model, x, y):
    accuracy = cross_val_score(model, x, y, scoring='accuracy', cv=5)
    return accuracy


def classification_algorithms(features, Y):
    names = [
        "Decision Tree",
        "Random Forest",
        "Neural Net",
        "AdaBoost",
        "Naive Bayes",
        "Gradient Boosting"]

    classifiers = [

        DecisionTreeClassifier(max_depth=5),
        RandomForestClassifier(max_depth=5, n_estimators=10, max_features=1),
        MLPClassifier(alpha=1, max_iter=1000),
        AdaBoostClassifier(),
        GaussianNB(),
        GradientBoostingClassifier(random_state=0)]

    for name, clf in zip(names, classifiers):
        accuracy = cross_validation(clf, features, Y)
        print("{} : {}".format(name, accuracy))
