# Study Project for system architecture 
#### Service responsible for authorization.
![Build Status](https://img.shields.io/github/workflow/status/unbrokenguy/sys-arch-auth-app/lint?label=linters)
* [Installation](#installation)
* [Setup](#setup)
* [Usage](#usage)
* [Related repositories](#related-repositories)
## Installation

#### Install poetry
```shell
pip install poetry
```

#### Install the project dependencies
```shell
poetry install 
```

## Setup

#### Make sure you have installed and started server
* [Configuration Server](https://github.com/unbrokenguy/sys-arch-conf-app)
#### Add environments
* SECRET_KEY: Your secret key for django application.
* CONF_APP_IP: [Configuration Server](https://github.com/unbrokenguy/sys-arch-conf-app) url
### Start current server
#### Spawn a shell within the virtual environment
```shell
poetry shell
```

#### Start server
```shell
cd src && python manage.py runserver 8002
```
Server will be available at this url  `http://localhost:8002/` or `http://127.0.0.1:8002/`
## Usage
* POST `/auth/sign_in/` - Sign in with email and password.
* POST `/auth/sign_up/` - Sign up with email, password, first name, last name.
* GET `/user/` - Retrieve authorized User. 
## Related repositories
1. [Data Server](https://github.com/unbrokenguy/sys-arch-server)
2. [Authorization Server](https://github.com/unbrokenguy/sys-arch-auth-app)
3. [Command line client](https://github.com/unbrokenguy/sys-arch-client)
4. [Front end](https://github.com/niyazm524/arch_client_web)