# soen-6441

[![Pylint](https://github.com/urvil38/soen-6441/actions/workflows/pylint.yaml/badge.svg)](https://github.com/urvil38/soen-6441/actions/workflows/pylint.yaml)

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
python3 src/main.py
```
This will start the program in interactive mode, prompting the user for input and displaying the results.

- Generating a CSV file:
```console
python3 src/main.py generate csv > output.csv
```
This will generate a CSV file with the results and save it to output.csv.

- Generating an XML file:
```console
python3 src/main.py generate xml > output.xml
```
This will generate an XML file with the results and save it to output.xml.


- Execute the Cheers project (with using standard library functions)

```console
python3 ./src/app_with_lib.py
```

- Plot the cos function

```console
python3 ./src/plot.py
```

## Setup Pylint:

- Install pylint using pip: (make sure your python virtual environment is active)

```console
pip install pylint

# invoke the pylint linter on all the .py files as following
pylint src/*.py
```
