# Flask TODO app
A simple flask app that uses minimum features to deliver a todo api 

# Tasks
- [x] Get todo
- [x] Create todo
- [x] Update todo
- [ ] Delete todo

# To get started

## Install pip


## create a virtual environment
```
python3 -m venv venv
```
## activate the virtual env
```
source venv/bin/activate
```

## Installation of packages using pip

```
pip install -r requirements.txt
```

## Before running the application

### config file
Steps to create a config file
- Create a copy of sample.config
- rename it to config.py
- optional: change the location and set the path 

### CMD/windows
```
set FLASK_APP=app
```
or
### Ubuntu
```
export FLASK_APP=app
```
# Run the application
```
flask run
```