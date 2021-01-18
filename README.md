# Instructions 

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
SET DATA=C:\Users\simor\AppData\Local\Neo4j\Relate\Data\dbmss\dbms-b4b08652-f6fb-4c7b-a9fb-6a3721cc4f9a\import

bin\neo4j-admin.bat import 
--mode=csv 
--database=yelp.db 
--nodes:Business  %DATA%\business_header.csv,%DATA%\business.csv 
--nodes:User %DATA%\user_header.csv,%DATA%\user.csv 
--nodes:Review %DATA%\review_header.csv,%DATA%\review.csv 
--nodes:City %DATA%\city_header.csv,%DATA%\city.csv 
--nodes:Category %DATA%\category_header.csv,%DATA%\category.csv 
--nodes:Photo %DATA%\photo_header.csv,%DATA%\photo.csv
--relationships:FRIENDS %DATA%\user_FRIENDS_user_header.csv,%DATA%\user_FRIENDS_user.csv 
--relationships:WROTE %DATA%\user_WROTE_review_header.csv,%DATA%\user_WROTE_review.csv 
--relationships:REVIEWS %DATA%\review_REVIEWS_business_header.csv,%DATA%\review_REVIEWS_business.csv 
--relationships:IN_CITY %DATA%\business_IN_CITY_city_header.csv,%DATA%\business_IN_CITY_city.csv 
--relationships:IN_CATEGORY %DATA%\business_IN_CATEGORY_category_header.csv,%DATA%\business_IN_CATEGORY_category.csv
--relationships:HAS_PHOTO %DATA%\business_HAS_PHOTO_photo_header.csv,%DATA%\business_HAS_PHOTO_photo.csv
--ignore-missing-nodes=true 
--multiline-fields=true

Neo4j Version: 1.4.0
Importing the contents of these files into /path/to/data/databases/yelp.db:
```

* Update the neo4j.conf file to contain this line:

```
dbms.active_database=yelp.db
```

* Restart Neo4j and go
