# soen-6441
[![tests](https://github.com/urvil38/soen-6441/actions/workflows/tests.yaml/badge.svg)](https://github.com/urvil38/soen-6441/actions/workflows/tests.yaml)
[![coverage](docs/coverage-badge.svg)]()
[![pylint](https://github.com/urvil38/soen-6441/actions/workflows/pylint.yaml/badge.svg)](https://github.com/urvil38/soen-6441/actions/workflows/pylint.yaml)

## Setup:

- Install Python 3.x (https://wiki.python.org/moin/BeginnersGuide/Download)
- Clone the current repository

```console
git clone https://github.com/urvil38/soen-6441.git
cd soen-6441
```

- Setup virtual enviroment (venv)

```console
# install virtualenv using pip
pip install virtualenv

# this will create a venv directory in root of the repository
python3 -m venv venv

# activate the virtual env

# for Unix based systems
source ./venv/bin/activate

# for Windows
.\venv\Scripts\activate.bat //In CMD
.\venv\Scripts\activate.ps1 //In Powershel
```

- Install the dependencies

```console
pip install -r requirements.txt
```

## Run:

Execute the Cheers project (without using standard library functions)

-  Running the program in interactive mode:
```console
python3 src/incarnation_one.py

# print output in XML format
python3 src/incarnation_one.py xml

# print output in CSV format
python3 src/incarnation_one.py csv
```
This will start the program in interactive mode, prompting the user for input and displaying the results.

- Generating a CSV file:
```console
python3 src/incarnation_one.py generate csv > output.csv
```
This will generate a CSV file with the results and save it to output.csv.

- Generating an XML file:
```console
python3 src/incarnation_one.py generate xml > output.xml
```
This will generate an XML file with the results and save it to output.xml.


- Execute the Cheers project (with using standard library functions)

```console
python3 ./src/incarnation_two.py
```

## Tests:
- Run the following command from the root of the repository to execute all the tests:
```console
pytest --cov -v
```

- List out all the available tests():
```console
pytest --co -q
```

- If you want to run individual test, provide test function name in the `-k` argument of the `pytest` command as following:
```console
# execute only run test_generate_xml_response test

pytest -v -k test_generate_xml_response
```

## Run Pylint:

```console
# invoke the pylint linter on all the .py files as following
pylint src/*.py
```

## How to deactivate virtualenv?
Just execute following command to deactivate the virtualenv:
```console
deactivate
```
