# similarity-hub

## Flexible entities similarity engine for external data source.

### Building Blocks [source](https://drive.google.com/file/d/1Ny9az4KV069HtQ5flKEluE9qjzwvwnAG/view?usp=sharing):

<img src="https://raw.githubusercontent.com/noamoss/similarity-hub/main/similarity-v01.jpg" />

### Project Boards:
- [Phase 1](https://github.com/noamoss/similiarity-hub/projects/1)


### Technical Stack:
- Flask
- PostgreSQL
- React

### prerequisites
- git
- python v.3.7.2+
- pipvenv
- postgresql 

### local env setup
- `pipenv install` (in the cloned repo folder)
- setup a new postgresql DB, and/or get an existing live DB credentials
- set a FALSK_ENV value "development":  `export FLASK_ENV=development` / add FLASK_ENV=development to the `.env` file
- set a FLASK_APP value "similarity": `export FLASK_ENV=similarity` / add FLASK_ENV=similarity to the `.env` file
  (set "production" for the live server))
- `pipenv shell`
- `cp _example.config.py config.py`
- set the relevant DB credentials in `config.py`
- `flask db init` (initialize local db)
- `flask db migrate -m "Initial db migration"`
- `flask db upgrade`
- `flask run`
