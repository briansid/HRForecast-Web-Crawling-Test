![alt text](https://raw.githubusercontent.com/briansid/HRForecast-Web-Crawling-Test/master/sample_output/hrforecast_jobs.png)
# Installation steps:
1. Install PostgreSQL
```
apt-get install postgresql postgresql-contrib
```

2. Setup PostgreSQL
```
sudo -u postgres -i
initdb -D '/var/lib/postgres/data'
createuser --interactive
createdb myDatabaseName
```

3. Specify your database settings in ./hrforecast_test/hrforecast_test/settings.py
```
user="youruser",
passwd="yourpassword",
host="localhost",
port="5432",
db_name="myDatabaseName"
```

4. Install Python 3.7.1
```
apt-get install python
```

5. Install pip
```
apt-get install python3-pip
```

6. Create and activate virtual enviroment
```
virtualenv venv
source venv/bin/activate
```

7. Install dependencise
```
pip install -r requirements.txt
```

8. Go into spiders folder and run script.sh
```
cd hrforecast_test/hrforecast_test/spiders/
./script.sh
```


# View database tables:
1. Go to database shell
```
psql -d myDatabaseName
```

2. Show summary information about all tables in the current database:
```
\dt
```

3. Retrieve all data from tables
```
SELECT * FROM tablename;
```

4. Exit
```
\q
```

![alt text](https://raw.githubusercontent.com/briansid/HRForecast-Web-Crawling-Test/master/sample_output/gazprom_jobs.png)




