# similiarity-hub

## Flexible entities similiarity engine for external data source.

### Building Blocks [source](https://drive.google.com/file/d/1Ny9az4KV069HtQ5flKEluE9qjzwvwnAG/view?usp=sharing):

<img src="https://raw.githubusercontent.com/noamoss/similiarity-hub/main/similiarity-v01.jpg" />

### Project Boards:
- [Phase 1](https://github.com/noamoss/similiarity-hub/projects/1)


### Techinical Stack:


### Setup and installation
- git clone
- `pip install pipenv`
- `pipenv install` (in the cloned repo folder)
- setup a new postgresql DB, or get an existing DB credentials
- set a FALSK_ENV value: "development" / "production" (i.e. `export FLASK_ENV=development`)
- `cp _config.py config.py`
- set the relevant DB crednetials in `config.py`
- `flask run`