# classifier_parameters_selection
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.utils._testing import ignore_warnings
from sklearn.exceptions import ConvergenceWarning
# classifiers, remove if your remove default
from sklearn.neural_network import MLPClassifier
from sklearn.svm import SVC

default_names = [
    "MLPClassifier", # Neural network models
    "SVC", # Support Vector Machines
    #"KNeighborsClassifier", # k nearest neighbors method
    #"DecisionTreeClassifier", # decision trees
    #"Gaussian Naive Bayes", # Naïve Bayes
]

default_classifiers = [
    MLPClassifier(),
    SVC(),
    #KNeighborsClassifier('weights': ['uniform', 'distance'],'n_neighbors': [1, 3, 5, 7, 9, 11, 13, 15]),
    #DecisionTreeClassifier(criterion=['gini', 'entropy'])
]

default_parameters = [
    {
        'hidden_layer_sizes': [100, 160, 180, 200], # default : 100
        'activation': ['logistic', 'relu', 'identity', 'tanh'], # default : relu
        'solver': ['lbfgs', 'sgd', 'adam'], # default : adam
        # 'alpha': ['0.0001'], # default : 0.0001
        # 'batch_size': ['auto'], # default : auto
        'max_iter': [600, 800, 1000], # default : 200
        # Many more config : https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html
    },
    {
        'C': [0.5, 1.0, 1.5, 2.0], # default=1.0
        'kernel': ['linear', 'poly', 'rbf', 'sigmoid', 'precomputed'], # {‘linear’, ‘poly’, ‘rbf’, ‘sigmoid’, ‘precomputed’} or callable, default=’rbf’
        'degree': [3], # default=3
        # 'gamma': ['scale', 'auto'], # {‘scale’, ‘auto’} or float, default=’scale’
        # 'coef0': [0.0], # default=0.0
        # Many more config : https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html
    }
]

@ignore_warnings(category=ConvergenceWarning)
def classifier_parameters_selection(x_train, x_test, y_train, y_test, names=default_names,classifiers=default_classifiers,parameters=default_parameters):
    """
    Exhaustive search over specified parameter for a large pannel of classifier
    :param dataframe x_train: the data to train the model
    :param dataframe x_test: the data to test the model
    :param dataframe y_train: the labels of the data to train the model
    :param dataframe y_train: the labels of the data to test the model
    :param array names: the names of the classifiers
    :param array classifiers: the function of the classifiers
    :param array parameters: the parameters of the classifiers
    :return:
    """
    clfs = {}
    for name, classifier, parameter in zip(names, classifiers, parameters):
        print(f"Start GridSearchCV for {name} classifier")
        clf = GridSearchCV(classifier, parameter, scoring='precision_macro')
        clf.fit(x_train, y_train)
        clf.predict(x_test)
        print(f"End GridSearchCV for {name} classifier")
        clfs[name] = clf
        pass
    for name, clf in clfs.items():
        print(f"Classification report for the best {name}\n{classification_report(y_test, clf.best_estimator_.predict(x_test))}")
        print(f"Confusion matrix for the best {name} classifier\n{confusion_matrix(y_test,clf.best_estimator_.predict(x_test))}")
        print(f"cv_results_ for {name} classifier\n{clf.cv_results_}")
        print(f"best_estimator_ for {name} classifier\n{clf.best_estimator_}")
        print(f"best_params_ for {name} classifier\n{clf.best_params_}")
        print(f"best_score_ for {name} classifier\n{clf.best_score_}")
        pass
    best_score=0
    for name, clf in clfs.items():
        if best_score < clf.best_score_:
            best_score = clf.best_score_
            best_clf = clf.best_estimator_
            pass
        pass
    return best_clf
