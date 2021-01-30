# similiarity-hub

## Flexible entities similiarity engine for external data source.

### Building Blocks [source](https://drive.google.com/file/d/1Ny9az4KV069HtQ5flKEluE9qjzwvwnAG/view?usp=sharing):

<img src="https://raw.githubusercontent.com/noamoss/similiarity-hub/main/similiarity-v01.jpg" />

### Project Boards:
- [Phase 1](https://github.com/noamoss/similiarity-hub/projects/1)


### Techinical Stack:

### prerequisites
- git
- python v.3.7.2+
- pipvenv
- postgresql 

### local env setup
- `pipenv install` (in the cloned repo folder)
- setup a new postgresql DB, and/or get an existing live DB credentials
- set a FALSK_ENV value: "development":  `export FLASK_ENV=development`
  (set "production" for the live server))
- `cp _example.config.py config.py`
- set the relevant DB crednetials in `config.py`
- `flask db init` (initialize local db)
- `flask db migrate -m "Initial db migration"`
- `flask db upgrade`
- `flask run`
