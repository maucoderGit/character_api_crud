# Characters API.

An API is an easy way for two or more systems to communicate and share data by requests and responses.

Today I publish my character API project, with the popular ORM from Django and using simple attributes for the models, it only has 2 attributes:

- name: A character name from a TV series such as Rick, Morty, Sheldon, etc...
- appears_in: name of the series, anime, or movie that it appears.

## CRUD System.

Like a crud, we have four options: create, read, update, and delete.

The endpoints of this API are:

### Get

- API/characters/: to get all the characters.
- API/characters/id: to get a character by an integer id.

### Post

- API/characters/: to make a post request.

### Put

- API/characters/id: to make an update request by integer id.

### Delete

- API/characters/id: to make a delete request by integer id.

## Extra information

The admin user in this project is:

- Username: maucoder 
- Password: Contraseña