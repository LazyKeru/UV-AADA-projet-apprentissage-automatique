# classifier_parameters_selection
from sklearn.model_selection import GridSearchCV

def classifier_parameters_selection(classifier, parameters, x_train, x_test, y_train, y_test):
    clf = GridSearchCV(classifier, parameters, scoring='precision_macro')
    clf.fit(x_train, y_train)
    predict = grid_search.predict(x_test)
    print(grid_search.best_estimator_, grid_search.best_params_, grid_search.best_score_)
    return scores
