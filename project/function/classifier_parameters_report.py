# classifier_parameters_report
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.utils._testing import ignore_warnings
from sklearn.exceptions import ConvergenceWarning
# to add more parameters to the default classifier
import numpy as np
# classifiers, remove if your remove default
from sklearn.neural_network import MLPClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB

default_names = [
    "MLPClassifier", # Neural network models
    "SVC", # Support Vector Machines
    "KNeighborsClassifier", # k nearest neighbors method
    "DecisionTreeClassifier", # decision trees
    "GaussianNB", # Naïve Bayes
]

default_classifiers = [
    MLPClassifier(),
    SVC(),
    KNeighborsClassifier(),
    DecisionTreeClassifier(),
    GaussianNB(),
]

default_parameters = [
    {
        'hidden_layer_sizes': [100, 160, 180, 200], # default : 100
        'activation': ['logistic', 'relu', 'identity', 'tanh'], # default : relu
        'solver': ['lbfgs', 'sgd', 'adam'], # default : adam
        # 'alpha': ['0.0001'], # default : 0.0001
        # 'batch_size': ['auto'], # default : auto
        'max_iter': [600, 800], # default : 200
        # Many more config : https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html
    },
    {
        'C': [0.5, 1.0, 1.5, 2.0], # default=1.0
        'kernel': ['linear', 'poly', 'rbf', 'sigmoid'], # {‘linear’, ‘poly’, ‘rbf’, ‘sigmoid’, ‘precomputed’} or callable, default=’rbf’
        # 'degree': [3], # default=3
        'gamma': ['scale', 'auto'], # {‘scale’, ‘auto’} or float, default=’scale’
        # 'coef0': [0.0], # default=0.0
        # Many more config : https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html
    },
    {
        'weights': ['uniform', 'distance'],
        'n_neighbors': [3, 5, 7, 9],
        'leaf_size': [15, 20],
        # Many more config : https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html
    },
    {
        'criterion':['gini','entropy'],
        'max_depth':[5,10,15,20]
        # Many more config : https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html
    },
    {
        'var_smoothing': np.logspace(0,-9, num=100),
        # Many more config : https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.GaussianNB.html
    }
]

def classifier_parameters_selection(name, classifier, parameters, x_train, x_test, y_train, y_test):
    """
    Exhaustive search over specified parameter for a specific classifier
    :param array classifier: the function of the classifier
    :param array parameters: the parameters of the classifier
    :param dataframe x_train: the data to train the model
    :param dataframe x_test: the data to test the model
    :param dataframe y_train: the labels of the data to train the model
    :param dataframe y_train: the labels of the data to test the model
    :return: it returns the prediction
    """
    print(f"Start GridSearchCV for {name} classifier")
    clf = GridSearchCV(classifier, parameters, scoring='precision_macro')
    clf.fit(x_train, y_train)
    clf.predict(x_test)
    print(f"End GridSearchCV for {name} classifier")
    return clf

@ignore_warnings(category=ConvergenceWarning)
def classifier_parameters_report(report_path, x_train, x_test, y_train, y_test, names=default_names,classifiers=default_classifiers,parameters=default_parameters):
    """
    Exhaustive search over specified parameter for a large pannel of classifier.
    returns the best model and writes an html report
    :param string report_path: path to print html report
    :param dataframe x_train: the data to train the model
    :param dataframe x_test: the data to test the model
    :param dataframe y_train: the labels of the data to train the model
    :param dataframe y_train: the labels of the data to test the model
    :param array names: the names of the classifiers
    :param array classifiers: the function of the classifiers
    :param array parameters: the parameters of the classifiers
    :return: best classifier
    """
    clfs = {}
    for name, classifier, parameter in zip(names, classifiers, parameters):
        clf = classifier_parameters_selection(name, classifier, parameter, x_train, x_test, y_train, y_test)
        clfs[name] = clf
        pass
    #preparing report
    report = ''
    for name, clf in clfs.items():
        report = report + f'''
        <h2>Classifier {name}:</h2>
        '''
        print(f"Classification report for the best {name}\n{classification_report(y_test, clf.best_estimator_.predict(x_test))}")
        report = report + f'''
        <p>Classification report for the best {name}\n{classification_report(y_test, clf.best_estimator_.predict(x_test))}</p>
        '''
        print(f"Confusion matrix for the best {name} classifier\n{confusion_matrix(y_test,clf.best_estimator_.predict(x_test))}")
        report = report + f'''
        <p>Confusion matrix for the best {name} classifier\n{confusion_matrix(y_test,clf.best_estimator_.predict(x_test))}</p>
        '''
        print(f"cv_results_ for {name} classifier\n{clf.cv_results_}")
        report = report + f'''
        <p>cv_results_ for {name} classifier\n{clf.cv_results_}</p>
        '''
        print(f"best_estimator_ for {name} classifier\n{clf.best_estimator_}")
        report = report + f'''
        <p>best_estimator_ for {name} classifier\n{clf.best_estimator_}</p>
        '''
        print(f"best_params_ for {name} classifier\n{clf.best_params_}")
        report = report + f'''
        <p>best_params_ for {name} classifier\n{clf.best_params_}</p>
        '''
        print(f"best_score_ for {name} classifier\n{clf.best_score_}")
        report = report + f'''
        <p>best_score_ for {name} classifier\n{clf.best_score_}</p>
        '''
        pass
    # Prepares the full html document
    html = f'''
    <html>
        <head>
            <title>Classifier and parameter selection Report</title>
        </head>
        <body>
            <h1>Classifier and parameter selection Report</h1>
            {report}
        </body>
    </html>
    '''
    #writes the html report
    with open(report_path, 'w') as f:
        f.write(html)
        pass
    best_score=0
    for name, clf in clfs.items():
        if best_score < clf.best_score_:
            best_score = clf.best_score_
            best_clf = clf.best_estimator_
            pass
        pass
    return best_clf
