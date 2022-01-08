# sklearn_test_classifier
from sklearn.neural_network import MLPClassifier
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV

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

def classifier_parameters_selection(classifier, parameters, x_train, x_test, y_train, y_test):
    """
    Exhaustive search over specified parameter for a specific classifier
    :param array classifier: the function of the classifier
    :param array parameters: the parameters of the classifier
    :param dataframe x_train: the data to train the model
    :param dataframe x_test: the data to test the model
    :param dataframe y_train: the labels of the data to train the model
    :param dataframe y_train: the labels of the data to test the model
    :return:
    """
    clf = GridSearchCV(classifier, parameters, scoring='precision_macro')
    clf.fit(x_train, y_train)
    clf.predict(x_test)
    print(grid_search.best_estimator_, grid_search.best_params_, grid_search.best_score_)
    return scores

def sklearn_classifier(x_train, x_test, y_train, y_test, names=default_names,classifiers=default_classifiers,parameters=default_parameters):
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
    scores = {}
    for name, classifier, parameter in zip(names, classifiers, parameters):
        classifier_parameters_selection(classifier, parameter, x_train, x_test, y_train, y_test)
        # classifier.fit(x_train, y_train)
        # score = classifier.score(x_test, y_test)
        # print(str(name) + " : " + str(score))
        # scores[name] = score
