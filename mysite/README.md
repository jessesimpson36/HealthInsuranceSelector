# Setup 
1. Copy the repo
2. Open `<repo>/mysite` in PyCharm (I promise Django development will be MUCH easier and its free to students)
3. Open a terminal and type `npm install` to install the dependencies in package.json
4. You should be able to run `python manage.py runserver` and the application should be served.

# Django Commands
### Base Command
* `python manage.py ____`

### Run the Server
* `python manage.py runserver` - runs the server

### Create a new app
* `python manage.py startapp <name>` - creates a new application of that name

### Database Commands
* `python manage.py makemigrations <app name>` - migrates an app's models
* `python manage.py migrate`   - migrates python models into the sqllite database
* `python manage.py shell` - access to an interactive shell where you can work with the db

### Creating an Admin
* `python manage.py createsuperuser` - create an admin user for the admin interface


# How to Create an App (a page)
1. Run `python manage.py <app name>`
2. A new folder is created call <app name>
3. Open `mysite/mysite/settings.py`
4. Scroll down to `INSTALLED_APPS` and add to the top `<app name>.apps.<App name>Config`
