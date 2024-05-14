# Overview
A user-friendly and informative web application for a rehab center to provide resources, support, and information to individuals seeking help for addiction or rehabilitation.

### Target audience
Individuals struggling with addiction, their families, healthcare professionals, and anyone seeking information on addiction treatment and recovery.

### Key Goals:
- Provide comprehensive information about the rehab center's services, programs, and treatment approaches.
- Offer resources and support to aid individuals in their journey towards recovery.
- Increase awareness of addiction-related issues and reduce stigma.

**This application system can be run locally as described in the [Running the Application](#running-the-application) section.**

# Running the Application Locally
The section allows for development and contribution towards the system.
When running the application locally we assume one has already installed *python 3.x (x being the most recent version of python)*
if not please install from the official [python website](https://www.python.org/downloads/)

### Clone the repository.
```
git clone https://github.com/Jabrahamjohn/Rehab.git
```
### Move into the repository
```
cd rehab_app
```
### Check if you have pip installed
```
python3.x -m pip --version
```
**If you dont have it installed visit [pip documentation](https://pip.pypa.io/en/stable/installation/)**
### Install virtual environment
```
python3.x -m pip install virtualenv 
```
### Create virtual environment
```
python3.x -m virtualenv env
```
### Activate the environment
(For macOS/Linux)
```
source venv/bin/activate 
```
(For Windows)
```
source ./env/Scripts/activate 
```
### Install dependencies
```
pip install -r requirements.txt 
```
### Run the application
```
python app.py (runs the application)
```

## Authors

* Abraham John - [https://github.com/Jabrahamjohn](https://github.com/Jabrahamjohn)
* Margaret Maina - [https://github.com/maggywairigu](https://github.com/maggywairigu)
