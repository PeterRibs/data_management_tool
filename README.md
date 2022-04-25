<<<<<<< HEAD
# Data manipulation Tool

Project producing a data manipulation service integrated to a PostgreSQL relational database.

## Technologies used

- Python.
- PostgreSQL.
- Docker compose.

## O projeto

Project steps:
- Read txt file with unconventional separator between columns.
- Manipulate the data in order to produce a table with a conventional separator between the columns, only the numeric digits of the CPFs and CNPJs and using '.' instead ',' to separate decimal (dataTransformationTool).
- Validate the records (CPF and CNPJ) in their respective fields in number of digits, equality of all digits and validation of the last two digits. With that, I produced two different tables, the first column of each table being the identifier (CPF or CNPJ) and the second column the validation (0 or 1) (datavalidation).
- Integration with the relational database of the general table and the ID validation tables (databaseManagement).
- The complete application was inserted in the app.py file and run using the run_app.py file.

For the steps, I used PostgreSQL 14.2 for the relational database, the Python 3.9 language (pandas, ramdom, psycopg2 packages) creating different files using classes in order to minimize the amount of code written and increase the application's performance and Docker compose to run and share application.

## Setup

- Docker: https://docs.docker.com/compose/
- PostgreSQL: https://www.postgresql.org/

After installation, you need to download the respective images in Docker.
- `docker pull python` - Python image.
- `docker pull postgres` - PostgreSQL image.

## Scripts

- `docker-compose up --build   ` - Trigger the service, building the application. 

In the run_app.py file you need to add eight arguments to the function:
- `App(arg1, arg2, arg3, arg4, arg5, arg6).all_process(arg7, arg8)`
  - arg1 ->  Name of the initial table that will be used to perform the manipulation.
  - arg2 -> Columns name of the new table.
  - arg3 -> Name of the database that will persist the data.
  - arg4 -> User PostgreSQL.
  - arg5 -> Senha PostgreSQL .
  - arg6 -> Local host.
  - arg7 -> Columns name of the general table.
  - arg8 -> Columns name of the CNPJ table.

To consult the table in database, uncomment the lines in `run_app.py` file.
=======
# IN PROGESS...
>>>>>>> c9f80cb7910b9a308c0caadc763266323645261f
