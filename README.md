# Basketball Statistics API

An API that represents the solution to the Challenge phase of "5 dana u oblacima" competition 2023.

## Build

In order to build the application (set it up) follow the steps below:

### Create a python environment

Run the following command:
```bash
python -m venv env
```
This will create a new directory ./env/ containing all our dependencies.

### Activate the environment

Now we need to activate the environment. This will tell the terminal that we want to use binaries defined in ./env/

To achieve that run the following command based on your operating system:

**Linux**
```bash
source ./env/bin/activate
```
**Windows**
```bash
.\env\Scripts\Activate.ps1
```

### Install dependencies

Now we have to install the dependencies listed in `requirements.txt`

Run the following command:
```bash
python -m pip install -r requirements.txt
```

## Run

Run the following command in order to start the app:
```bash
uvicorn app.main:app
```

## Test

If you want to run the tests, you can do that by running the command `pytest`
