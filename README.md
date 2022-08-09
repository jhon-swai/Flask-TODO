# Install pip


# create a virtual environment
```
python3 -m venv venv
```
# activate the virtual env
```
source venv/bin/activate
```

# Installation of packages using pip

```
pip install -r requirements.txt
```

# Before running the application
## CMD/windows
```
set FLASK_APP=app
```
or
## Ubuntu
```
export FLASK_APP=app
```
# Run the application
```
flask run
```