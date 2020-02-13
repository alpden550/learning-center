# CRM For Learning Center

[![wemake-python-styleguide](https://img.shields.io/badge/style-wemake-000000.svg)](https://github.com/wemake-services/wemake-python-styleguide)

Flask app for learnig center's CRM

[![STEPIC-CRM-2020-02-13-15-39-51.png](https://i.postimg.cc/1tQPKbHB/STEPIC-CRM-2020-02-13-15-39-51.png)](https://postimg.cc/xktWfxBN)

[![Stepic-CRM-2020-02-13-15-40-35.png](https://i.postimg.cc/2SZPX23K/Stepic-CRM-2020-02-13-15-40-35.png)](https://postimg.cc/MnzPn077)

[![Stepic-CRM-2020-02-13-15-41-33.png](https://i.postimg.cc/1ttBb3J3/Stepic-CRM-2020-02-13-15-41-33.png)](https://postimg.cc/4KDp9ZDD)

[![Authorisation-Stepic-CRM-2020-02-13-15-38-16.png](https://i.postimg.cc/GppvmSYM/Authorisation-Stepic-CRM-2020-02-13-15-38-16.png)](https://postimg.cc/VJ3J7gKM)

## How to install

Download code or clone it from Github, and install dependencies.

If you have already installed Poetry, type command:

```bash
poetry install --no-dev
```

If not, should use a virtual environment for the best project isolation. Activate venv and install dependencies:

```bash
pip install -r requirements.txt
```

And set environment variables:

```env
export FLASK_DEBUG=true, if debug mode is need
export SECRET_KEY=some extra secret key
```

## How to run

You could immediately create a database and admin's account. Type `flask admin -n admin -p password` or `flask admin` to create default admin:

```bash
flask admin -n admin -p password -e test@mail.ru
```

And start web server:

```bash
flask run
```
