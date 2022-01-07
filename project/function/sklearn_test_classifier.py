# sklearn_test_classifier
from sklearn.neural_network import MLPClassifier

default_names = [
    "MLPClassifier", # Neural network models
    #"SVC", # Support Vector Machines
    #"KNeighborsClassifier", # k nearest neighbors method
    #"DecisionTreeClassifier", # decision trees
    #"Gaussian Naive Bayes", # Naïve Bayes
]

default_classifiers = [
    MLPClassifier(
        hidden_layer_sizes=100, # default : 100
        activation='relu', # default : relu
        solver='adam', # default : adam
        alpha=0.0001, # default : 0.0001
        batch_size='auto', # default : auto
        max_iter=1000, # default : 200
        # Many more config : https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html
    ),
    #SVC()
    #KNeighborsClassifier('weights': ['uniform', 'distance'],'n_neighbors': [1, 3, 5, 7, 9, 11, 13, 15]),
    #DecisionTreeClassifier(criterion=['gini', 'entropy'])
]

def sklearn_test_classifier(x_train, x_test, y_train, y_test, names=default_names,classifiers=default_classifiers):
    '''
    names = [
        "Nearest Neighbors",
        "Linear SVM",
        "RBF SVM",
        "Gaussian Process",
        "Decision Tree",
        "Random Forest",
        "Neural Net",
        "AdaBoost",
        "Naive Bayes",
        "QDA",
    ]

    classifiers = [
        KNeighborsClassifier(3),
        SVC(kernel="linear", C=0.025),
        SVC(gamma=2, C=1),
        GaussianProcessClassifier(1.0 * RBF(1.0)),
        DecisionTreeClassifier(max_depth=5),
        RandomForestClassifier(max_depth=5, n_estimators=10, max_features=1),
        MLPClassifier(alpha=1, max_iter=1000),
        AdaBoostClassifier(),
        GaussianNB(),
        QuadraticDiscriminantAnalysis(),
    ]
    '''
    scores = {}

    for name, classifier in zip(names, classifiers):
        classifier.fit(x_train, y_train)
        score = classifier.score(x_test, y_test)
        print(str(name) + str(score))
        scores[name] = score
