A simple app consisting of resources, users and bookings

### Usage

Run the development server by typing the command `python manage.py runserver`

The website is accessible from localhost:8000 and the REST API from localhost:8000/api/

### Features

- Users can sign up and set their timezone
- Users can view the list of resources
- Users can book a resource and view the list of their bookings
- Users can edit a booking before it starts
- Users can cancel a booking before it ends
- Admin can manage resources (view, create, edit, remove)
- Admin can view all bookings with dates and times converted to their timezone
- Admin can edit and delete all bookings

### Technical

- Resources, Bookings and Users can be read, created, edited and deleted without authentication from the REST API.
Visit localhost:8000/api to get URIs.
- Persistence is enabled by a SQLite database file
- Bootstrap and Django Crispy Forms are used to get a simple but decent UI

### To be improved

- Find a better way to handle creation and edition forms (AJAX) so errors can be returned
- Write unit tests
- Split files in folders to reorder code
- Secure REST API (which is not part of level 1)
- Allow users to edit their profile (and timezone)
- Make resource types dynamic (manageable by admin)
