# fastapi_sqlalchemy_alembic

This repo is used as a part of a mitrais backend test, Used Fastapi and pydantic with Sqlalchemy, postgresql, Alembic(for migrations).


## System Requirements
    
    - Python 3 or higher
    - Fastapi
    - pydantic
    - Alembic
    - Sqlachemy
    - psycopg2
    - Uvicorn


## How to build

    Create python env
        - python3 -m venv env
    
    Activate python environment
        - source env/bin/activate

    Install requirements.txt
        - pip install -r requirements.txt

    Change database connection (database_name, username, password)
        - overwrite file .env
            DATABASE_URL=postgresql://user:password@localhost/db_name

        - overwrite file alembic.ini
            sqlalchemy.url = driver://your_username:your_password@localhost:3306/your_database_name


## How to run (Run in Terminal if use Linux Flavour)

    1. Run alembic migration
        - alembic upgrade head
    
    2. Run project
        - uvicorn main:app --reload

    3. Open browser and go to:
        http://localhost:8000


## Documentation And API testing

    Read documentation
        redoc - http://localhost:8000/redoc

    Try API testing
        swagger - http://localhost:8000/docs

## If there are additions or changes table

    - alembic revision -m "your command"
    - coding in def upgrade or def downgrade in file last version (directory alembic)
    - alembic upgrade head
        output when success (approximately) :
            INFO  [alembic.runtime.migration] Context impl MySQLImpl.
            INFO  [alembic.runtime.migration] Will assume transactional DDL.
            INFO  [alembic.runtime.migration] Running upgrade  -> version, version_command
            
## Screenshot 
        - Registration
            ![Image of Register view]
            (https://github.com/4happycode/mitrais_test/blob/main/register_view.jpeg)
        
        - Registration after submiting form
            ![Image of Register view]
            (https://github.com/4happycode/mitrais_test/blob/main/register_view_after_submiting.jpeg)


