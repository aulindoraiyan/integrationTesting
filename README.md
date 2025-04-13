# [ISE] 5.1.1 Integration Testing

## In-Class Activity

### One-Time Setup

1. Clone this repo into your cloud shell editor with `git clone <this repo>`
1. Create local virtual environment `python3 -m venv venv`
1. Install dependencies `pip install -r requirements.txt`

### Before starting work

1. Activate venv `source venv/bin/activate`

### Running the app

1. `streamlit run app.py`
1. Click on the "Local URL"

### Running the tests

1. `pytest tests/tests.py`

### Writing the tests

You're assignment is to write the tests marked TODO in the tests/tests.py file.

Make sure you test the additional functionality on the decrement button (the count is not allowed to go below 0).

If you finish this work and there's still time, add a 100x mode checkbox and write tests for that. How the 100x and 10x buttons interact/overlap is left up to you.

### Turning in your assignment

First, add your files with `git add`, and push them with `git push`. 

Then, your instructor will give you instructions for turning in your repo.