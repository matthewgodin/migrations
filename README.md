# migrations

## Description

A simple Postgres utility inspired by Laravel Migrations. Uses Python 3.

## Usage

Create a database migration:

```bash
python migrations.py make <migration-name>
```

Perform all migrations that haven't been performed:
```bash
python migrations.py migrate
```
