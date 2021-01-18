# dimsim

* Run the following command to extract cities:

```
python lat_long_expansion.py
```

* Run the following commands to create Neo4j Import Tool CSV files:

```
python json_to_csv_business.py
```
```
python json_to_csv_user.py
```
```
python json_to_csv_reviews.py
```
```
python json_to_csv_cities.py
```
```
python json_to_csv_categories.py
```
```
python photo_json_to_csv.py
```

* Navigate to the Neo4j home directory and run the following command from terminal:

```


Neo4j Version: 1.4.0
Importing the contents of these files into /path/to/data/databases/yelp.db:
```

* Update the neo4j.conf file to contain this line:

```
dbms.active_database=yelp.db
```

* Restart Neo4j and go
