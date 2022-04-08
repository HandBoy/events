# the-eye

## REST Application: Start Project

```shell
# Create an env file in root
$ cp .env.default .env

# Add enviroments values in this file.

# Python path
$ which python3

# Create virtual enviroment
$ virtualenv --python='/usr/bin/python3' .venv

# Activate virtual enviroment
$ source .venv/bin/activate 

# Install requirements
$ make install

# Run database 
$ make psql_start

# Create and apply migrations 
$ make db

# Run project
$ make run
```