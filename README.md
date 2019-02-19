# Simple Read-Only API in Python

This is a simple read-only API application written in Python using Flask package.
The 'data.json' file is a JSON formatted data file with numeric county values as keys and its corresponding happiness index as values.

You can extract below data using this API
- Available happiness index value(s) for given list of counties
- Average happiness index value of given list of counties
- Standard Deviation of given list of counties within a range
- Counties and its happiness index within the given county range

## Getting Started

This is a simple Python application, so as long as you can run a Python code on your machine there should be no problem running this app.

### Prerequisites

```
Latest Python/pip and Flask package will be needed!
```

#### To Download Python

Windows users, if you don't already have Python available, please check here : http://timmyreilly.azurewebsites.net/python-flask-windows-development-environment-setup/ to see how to set up a Python/Flask environment on your machine.

MacOS users, if you don't already have Python available, please check here : https://docs.python-guide.org/starting/install3/osx/ and download the latest Python.

Linux users, if you don't already have Python available, please check here : https://docs.python-guide.org/starting/install3/linux/ and download the latest Python.

Once Python is installed, run the following command

```
pip install flask
```
to install Flask package.


### Installing
1. Download emsiAssignment zip file 
2. Unzip emsiAssignment-master.zip
3. Open Terminal application/virtual environment and change directory to emsiAssignment-master
```
cd /location/of/emsiAssignment-master  * this is an UNIX-like system command example
```

4. Run app.py

```
python3 app.py
```
If successful, you should see output like

```
 * Serving Flask app "app" (lazy loading)
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

## Get Data

While app.py is running on your terminal/virtual environment, open up another terminal/virtual environment. You are going to extract data from the flask app by using "curl" command.

To request data you need to know what URL the app is running on. The typical URL would be http://127.0.0.1:5000/. But it may be different, so check the last line of app.py output. You will see the URL that the application is running on. 

#### Print Whole Data

```
curl --request GET http://127.0.0.1:5000/
```
This will show you the whole happiness data in JSON format.

#### Print Happiness Index
```
curl --request GET http://127.0.0.1:5000/happiness?county=10001
```
If you want to look at multiple counties, use
```
curl --request GET http://127.0.0.1:5000/happiness?county=10001&county=10003&county=10005 ... &county=1001
```
Make sure you escape the ampersand character '&' if needed.

#### Print Average Happiness
```
curl --request GET http://127.0.0.1:5000/happiness/average?county=10001&county=10003&county=10005
```
This will show you the average happiness index value for counties 10001,10003 and 10005.

#### Print Standard Deviation

The Standard Deviation endpoint requires you to be give a range of counties.
```
curl --request GET http://127.0.0.1:5000/happiness/stdev?from=10000&to=10005
```
Both will show you the standard deviation of happiness index of counties(10001, 10003 and 10005, in this particular case) within the given range.

#### Print Counties Within Happiness Range

This endpoint requires you to give a range of happiness index.
```
curl --request GET http://127.0.0.1:5000/happiness/range?from=90&to=100
```
This will show you the list of all counties with index value that is within 90 and 100.

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

