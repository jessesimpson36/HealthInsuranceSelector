# HealthInsuranceSelector

This will be where the webapp for our health insurance selector will be.
The app itself will hopefully sort best health insurance plans based on
user preferences.

# Setup 
1. Copy/ Clone the repo
2. Open `<repo>/mysite` in a linux terminal
3. type `npm install` to install the dependencies in package.json
4. You should be able to run `python manage.py runserver` and the application should be run.
5. Open an internet browser and go to localhost:8000

# Important notes about the program
* There is no message displayed to the user for invalid input, it just returns the user to the input page.
* If there is no match for health insurance plans given your zipcode, age, smoking status, diseases, and benefits, the program will return you to the input page. Any combination of the remaining inputs should still return results.
