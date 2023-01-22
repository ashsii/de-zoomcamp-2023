# Data ingestion

Running locally

```bash
URL="https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2019-01.csv.gz"

python ingest_data.py \
  --user=root \
  --password=root \
  --host=localhost \
  --port=5432 \
  --db=ny_taxi \
  --table_name=green_taxi_trips \
  --url=${URL}
```

Build the image

```bash
docker build -t data_ingest:v001 .
```

Run the script with Docker

```bash
URL="https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_2021-01.csv.gz"

docker run -it \
  --network=pg-network \
  data_ingest:v001 \
    --user=root \
    --password=root \
    --host=pg-database \
    --port=5432 \
    --db=ny_taxi \
    --table_name=green_taxi_trips \
    --url=${URL}
```

### Docker-Compose 

Docker-Compose will: Create postgres and pgadmin sessions and ingest zones and green taxi data. Requires data_ingest:v001 docker file be built.


Run it:

```bash
docker-compose up
```

Run in detached mode:

```bash
docker-compose up -d
```

Shutting it down:

```bash
docker-compose down
```

Note: to make pgAdmin configuration persistent, create a folder `data_pgadmin`. Change its permission via

```bash
sudo chown 5050:5050 data_pgadmin
```

and mount it to the `/var/lib/pgadmin` folder:

```yaml
services:
  pgadmin:
    image: dpage/pgadmin4
    volumes:
      - ./data_pgadmin:/var/lib/pgadmin
    ...
```

# Solutions to SQL questions. Completed in pgAdmin Query Tool

## Question 3. Count records 

How many taxi trips were totally made on January 15?

Tip: started and finished on 2019-01-15. 

Remember that `lpep_pickup_datetime` and `lpep_dropoff_datetime` columns are in the format timestamp (date and hour+min+sec) and not in date.

```sql
SELECT count(1)
FROM green_taxi_trips 
WHERE to_date(lpep_pickup_datetime::TEXT,'YYYY-MM-DD') = '2019-01-15'
AND to_date(lpep_dropoff_datetime::TEXT,'YYYY-MM-DD') = '2019-01-15';
```

## Question 4. Largest trip for each day

Which was the day with the largest trip distance
Use the pick up time for your calculations.

```sql
SELECT lpep_pickup_datetime
FROM green_taxi_trips
ORDER BY trip_distance DESC
LIMIT 1;
```

## Question 5. The number of passengers

In 2019-01-01 how many trips had 2 and 3 passengers?
 
```sql
SELECT 
	COUNT(CASE WHEN passenger_count = 2 THEN 1 ELSE null END) AS NumberOf2Pass,
	COUNT(CASE WHEN passenger_count = 3 THEN 1 ELSE null END) AS NumberOf3Pass
FROM green_taxi_trips 
WHERE passenger_count IN (2,3)
AND to_date(lpep_pickup_datetime::TEXT,'YYYY-MM-DD') = '2019-01-01';
```

## Question 6. Largest tip

For the passengers picked up in the Astoria Zone which was the drop off zone that had the largest tip?
We want the name of the zone, not the id.

Note: it's not a typo, it's `tip` , not `trip`

```sql
SELECT dz."Zone"
FROM green_taxi_trips g
LEFT JOIN zones dz on g."DOLocationID" = dz."LocationID"
LEFT JOIN zones pz on g."PULocationID" = pz."LocationID"
WHERE pz."Zone" = 'Astoria' # pick up Astoria
ORDER BY tip_amount DESC
LIMIT 1;
```
