# Question 1

```sql
SELECT count(1) FROM `project_name.dezoomcamp.fhv_tripdata_native`;
```


# Question 2
```sql
select count(distinct Affiliated_base_number) FROM `project_name.dezoomcamp.fhv_tripdata_external`;
select count(distinct Affiliated_base_number) FROM `project_name.dezoomcamp.fhv_tripdata_native`;
```

# Question 3
```sql
select count(1) FROM `massive-weft-375905.dezoomcamp.fhv_tripdata_native` where PUlocationID is null and DOlocationID is null; 
```

# Question 5
```sql
CREATE OR REPLACE TABLE project_name.dezoomcamp.fhv_tripdata_clustered
PARTITION BY
  date(pickup_datetime)
CLUSTER BY
  affiliated_base_number
AS (
  SELECT * FROM `project_name.dezoomcamp.fhv_tripdata_native`
);

select distinct affiliated_base_number from project_name.dezoomcamp.fhv_tripdata_native
where date(pickup_datetime) between '2019-03-01' and '2019-03-31';

select distinct affiliated_base_number from project_name.dezoomcamp.fhv_tripdata_clustered
where date(pickup_datetime) between '2019-03-01' and '2019-03-31'
```