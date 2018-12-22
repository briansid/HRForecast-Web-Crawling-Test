# Installation steps:
1. Install PostgreSQL
> apt-get install postgresql postgresql-contrib

2. Setup PostgreSQL
> sudo -u postgres -i
> initdb -D '/var/lib/postgres/data'
> createuser --interactive
> createdb myDatabaseName

3. Specify your database settings in ./hrforecast_test/hrforecast_test/settings.py
> 	user="youruser",
>     passwd="yourpassword",
>     host="localhost",
>     port="5432",
>     db_name="myDatabaseName"

3. Install Python 3.7.1
> apt-get install python

4. Install pip
> apt-get install python3-pip

5. Create and activate virtual enviroment
> python -m virtualenv env

6. Install dependencise
> pip install -r ./hrforecast_test/hrforecast_test/requirements.txt

7. Run
> ./hrforecast_test/hrforecast_test/spiders/script.sh


# View database tables:
1. Go to database shell
> psql -d myDatabaseName

2. Show summary information about all tables in the current database:
> \dt

3. Acces all data from tables
> SELECT * FROM tablename;

4. Exit
> \q

![alt text](HRForecast-Web-Crawling-Test/gazprom_jobs.png)
![alt text](HRForecast-Web-Crawling-Test/hrforecast_jobs.png)




