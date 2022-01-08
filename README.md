# UV-AADA-projet-apprentissage-automatique
The objective of this project is to create a system for recognizing human actions using inertial sensors. We will us the sensors implemented in a smartphone to collect data to recognise different actions. The inertial sensors on board the smartphone are the accelerometer, the gyroscope and the magnetometer.

## Flowchart of our project

flowchart LR
    dataset(Data collected)--load_data-->load_data(Function which takes our dataset and tranforms it into a dataFrame with which we can work)
    load_data--feature_extraction-->feature_extraction(Function which tranforms the human action into vectors and extracts the features of those actions)
    feature_extraction--train_test_split_local-->train_test_split_local(Function which divides the data frame into four parts)
    feature_extraction-->x_train(x_train data of the train dataset) & y_train(y_train label of the train dataset) & x_test(x_test data of the test dataset) & y_test(y_test label of the test dataset)
    x_train & y_train & x_test & y_test --standarize_data-->standarize_data(Function which standarize the training and test data set)
    standarize_data--classifier_parameters_selection-->classifier_parameters_selection(Function which realize an exhaustive search over specified parameter for a large pannel of classifier)
    classifier_parameters_selection-->results(We are left with the best classifier from our test)



## workflows

### semantic-version

[![semantic-version](https://img.shields.io/github/workflow/status/LazyKeru/UV-AADA-projet-apprentissage-automatique/Semantic-version?style=plastic)](https://github.com/LazyKeru/UV-AADA-projet-apprentissage-automatique/actions/workflows/semantic-versioning.yml)

## Commit convention :
- build: Changes that affect the build system or external dependencies (example scopes: gulp, broccoli, npm)
- ci: Changes to our CI configuration files and scripts (examples: CircleCi, SauceLabs)
- docs: Documentation only changes
- feat: A new feature
- fix: A bug fix
- perf: A code change that improves performance
- refactor: A code change that neither fixes a bug nor adds a feature
- test: Adding missing tests or correcting existing tests

## Libraries needed / used :

numpy, pandas, matplotlib, SciPy, Scikit-Learn

## To do list :

- [X] load_data module
- [X] trace_signal module
- [X] feature_extraction module
- [X] train_test_split_local module
- [X] standarize_data module
- [x] sklearn_teach_classifiers module
- [x] classifier_parameters_selection module
- [x] classifier_parameters_report module
- [ ] tutorial
- [x] requirements.txt
- [ ] better desciption
- [ ] save_model module
