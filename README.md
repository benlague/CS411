# CS411
## Project setup
### 1. Clone repository
```bash
git clone git@github.com:benlague/CS411.git
```
### 2. Connect IDE to development docker container
Developing in a reproducable development environment is very important especially when working in large teams. Very often what happens is teamates have different operatin systems with different versions of software installed and configured in different ways and this leads to the annyoing "it works on my machine but not yours" problem.

Most IDE's support hooking up to a local docker container as the development environment.

#### VS Code users
For VS Code users its straightforward, this project includes the setup configuration for hooking up to a container in vscode (in the `.devcontainer` directory).
Go through the directions here to setup your local dev container:
https://code.visualstudio.com/docs/remote/containers

### 3. Install dependencies
#### Backend (python) dependencies
```bash
make install-deps-py
```
#### Frontend (JavaScript) dependencies
```bash
make install-deps-js
```
#### Alternativly install all dependencies at once
```bash
make install-deps
```
### 4. Initialize database (apply migrations)
```bash
make db-upgrade
```
The above make goal will create all the tables defined in the `migrations/versions` folder.
### 5. Run the backend API server
```bash
make run-server
```
### 6. Run the frontend server
```bash
make run-client
```

## Project Structure
```
├── docs                                # All non code related documents
├── migrations                          # Maintained by alembic the database migration tool
│   └── versions                        # Database migration revisions are places here
└── src                                 # All source code
    ├── javascript                      # All javascript (frontend) source code
    └── python                          # All python (backend) source code
        ├── services                    # Backend services
        │   ├── api                     # The backend API service
        │   │   ├── libs                # Small libraries used within the api service
        │   │   ├── models              # Data descriptor of the api service (database models)
        │   │   ├── resources           # API Resources exposed by the api service
        │   │   └── schemas             # Serializer for our data structures
        └── tests                       # All python tests
            ├── integration             # Integrations tests
            └── unit                    # Unit tests (directory structure should match the python directory)
```

## Testing
### Backend (python)
#### Run unit tests with Pytest
```bash
make unit-tests-py
```
#### Run integration tests with Pytest
```bash
make integration-tests-py
```
### Frontend (JavaScript)
TBD

## Continuous Integration
Using Github Actions https://docs.github.com/en/free-pro-team@latest/actions to automate CI workflows.
CI is run on every pull request made against the `main` branch.
For now the CI includes the following steps:
1. lint
2. unit test
3. integration test

See `.github/workflows/ci.yml` for the definition of the CI workflow being run

## Utilities
### `make lint-py`
#### Description:
Runs a flake8 linter on all python code
### `make lint-js`
#### Description:
Runs a eslint linter on all javascript code
### `make lint`
#### Description:
Runs both `make lint-py` and `make lint-js` (quick way to lint all the code)
### `make install-deps-py`
#### Description:
Installs all the python packages required by our project
### `make install-deps-js`
#### Description:
Installs all the javascript packages required by our project
### `make install-deps`
#### Description:
Installs all packages (python & javascript) required by our project
### `make run-server`
#### Parameters:
`ENVIRONMENT` (optional, default: dev) - Must be one of (dev, test, prod). Used to determine configuration settings for the backend Flask API.<br>
`FLASK_DEBUG` (optional, default: 1) - Must be one of (0, 1). If set to 1, the Flask app will "hot reload" on code changes.
#### Description:
Starts serving the backend Flask API using the builtin development server (should not be used in production)
#### Usage:
`make run-server ENVIRONMENT=dev FLASK_DEBUG=0`
### `make run-client`
#### Description:
Starts serving the frontend Vue web application using the builting Vue development server (should not be used in production).
### `make db-migrate`
#### Parameters:
`ENVIRONMENT` (optional, default: dev) - Must be one of (dev, test, prod). Used to determine configuration settings for the backend Flask API.<br>
`MESSAGE` - The description of the migration (kind of like a commit message).
#### Description:
Will create a new database migration script in the `migrations/versions` folder. See https://flask-migrate.readthedocs.io/en/latest/#command-reference for more details.
#### Usage:
`make db-migrate ENVIRONMENT=dev MESSAGE="Adds a users table"`
### `make db-upgrade`
#### Parameters:
`ENVIRONMENT` (optional, default: dev) - Must be one of (dev, test, prod). Used to determine configuration settings for the backend Flask API.
#### Description:
Upgrades the database to the latest migration. See https://flask-migrate.readthedocs.io/en/latest/#command-reference for more details.
### `make db-downgrade`
#### Parameters:
`ENVIRONMENT` (optional, default: dev) - Must be one of (dev, test, prod). Used to determine configuration settings for the backend Flask API.
#### Description:
Downgrades the database to the previous migration. See https://flask-migrate.readthedocs.io/en/latest/#command-reference for more details.
### `make unit-tests-py`
#### Description:
Runs unit-tests with pytest located in `src/python/tests/unit`
### `make integration-tests-py`
Runs integration tests with pytest located in `src/python/tests/integration`
