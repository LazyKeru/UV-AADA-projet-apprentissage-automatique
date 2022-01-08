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

## Commit convention :
- build: Changes that affect the build system or external dependencies (example scopes: gulp, broccoli, npm)
- ci: Changes to our CI configuration files and scripts (examples: CircleCi, SauceLabs)
- docs: Documentation only changes
- feat: A new feature
- fix: A bug fix
- perf: A code change that improves performance
- refactor: A code change that neither fixes a bug nor adds a feature
- test: Adding missing tests or correcting existing tests
