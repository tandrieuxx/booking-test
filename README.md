A simple app consisting of resources, users and bookings

### Usage

Requires Python 3.6

At first use, run these commands from the project directory (booking_test):
- (optional) `python -m venv env` to create a virtual environment (requires virtualenv)
- (optional) `.\env\Scripts\activate` on Windows or `source env/bin/activate` on Linux and OS X to activate the virtual
environment
- `pip install -r requirements.txt` to install python dependencies
- `python manage.py migrate` to initiate database structure
- `python manage.py loaddata initial` to create a basic dataset including an admin user (credentials admin/admin),
- `django-admin compilemessages` to compile translation files (requires gettext)
6 resources and 1 past booking

Run the development server by typing the command `python manage.py runserver` after activating the virtual environment
if you use one.

The website is accessible from localhost:8000 and the REST API from localhost:8000/api/

### Features

- Users can sign up and set their timezone
- Users can view the list of resources
- Users can book a resource and view the list of their bookings
- Users can edit a booking before it starts
- Users can cancel a booking before it ends
- Users can choose between French and English at sign up
- Users can choose their timezone at sign up
- Admin can manage resources (view, create, edit, remove)
- Admin can view all bookings with dates and times converted to their timezone
- Admin can edit and delete all bookings

### Technical

- Resources, Bookings and Users can be read, created, edited and deleted without authentication from the REST API.
Visit localhost:8000/api to get URIs.
- Persistence is enabled by a SQLite database file
- Bootstrap and Django Crispy Forms are used to get a simple but decent UI

### To be improved

- Find a better way to handle creation and edition forms (AJAX) so errors don't break the form
- Write unit tests
- Split files in folders to reorder code
- Secure REST API (which is not part of level 1)
- Allow users to edit their profile (and timezone)
- Make resource types dynamic (manageable by admin)
- Insert newly created bookings at the right position in the list without reloading the page
- Ask for confirmation when deleting something
