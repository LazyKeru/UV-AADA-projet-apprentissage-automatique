# UV-AADA-projet-apprentissage-automatique
The objective of this project is to create a system for recognizing human actions using inertial sensors. We will us the sensors implemented in a smartphone to collect data to recognise different actions. The inertial sensors on board the smartphone are the accelerometer, the gyroscope and the magnetometer.

## How to test our project

### install dependencies

#### if you are using python2

``` bash
$ pip install -r requirements.txt
```

#### if you are using python3

``` bash
$ pip3 install -r requirements.txt
```

### run our main test function

#### if you are using python2

``` bash
$ python main.py
```

#### if you are using python3

``` bash
$ python3 main.py
```

#### best model

SVC classifier with the following parameters :
- 'C': 1.0
- 'gamma': 'scale'
- 'kernel': 'linear'

##### Confusion matrix for the best SVC classifier :

```
[[3 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]
 [0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]
 [0 0 3 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]
 [0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 3 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 3 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 2 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 3 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 3 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0 0 2 0 0 0 0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0 0 0 2 0 0 0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0 0 0 0 3 0 0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 5 0 0 0 1 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 3 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 2 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0]
 [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0]
 [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 2 0]
 [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 3]]
```

In the field of machine learning and specifically the problem of statistical classification, a confusion matrix, also known as an error matrix,[9] is a specific table layout that allows visualization of the performance of an algorithm, typically a supervised learning one (in unsupervised learning it is usually called a matching matrix).

How to read the matrix :
| Total population |    Positive (PP)    |    Negative (PN)    |
|------------------|---------------------|---------------------|
|   Positive (P)   | True positive (TP)  | False negative (FN) |
|   Negative (N)   | False positive (FP) | True negative (TN)  |

As we can see with the matrix, this model obtained almost a 100% True Positive and True Negative

##### One of the best score obtained with this SVC classifier :

0.9554212454212454

## To do list :

- [X] load_data module
- [X] trace_signal module
- [X] feature_extraction module
- [X] train_test_split_local module
- [X] standarize_data module
- [x] sklearn_teach_classifiers module
- [x] classifier_parameters_selection module
- [x] classifier_parameters_report module
- [x] tutorial
- [x] requirements.txt
- [ ] better desciption
- [ ] save_model module

## workflows

### semantic-version

[![semantic-version](https://img.shields.io/github/workflow/status/LazyKeru/UV-AADA-projet-apprentissage-automatique/Semantic-version?style=plastic)](https://github.com/LazyKeru/UV-AADA-projet-apprentissage-automatique/actions/workflows/semantic-versioning.yml)

### Run Python Tests
[![Run Python Tests](https://img.shields.io/github/workflow/status/LazyKeru/UV-AADA-projet-apprentissage-automatique/Semantic-version?style=plastic)](https://github.com/LazyKeru/UV-AADA-projet-apprentissage-automatique/actions/workflows/python-tests.yml)
#### test are runned for:
- ./project/function/load_data module with ./tests/test_load_data
- ./project/function/feature_extraction with ./tests/test_feature_extraction.py

## Commit convention :
- build: Changes that affect the build system or external dependencies (example scopes: gulp, broccoli, npm)
- ci: Changes to our CI configuration files and scripts (examples: CircleCi, SauceLabs)
- docs: Documentation only changes
- feat: A new feature
- fix: A bug fix
- perf: A code change that improves performance
- refactor: A code change that neither fixes a bug nor adds a feature
- test: Adding missing tests or correcting existing tests
