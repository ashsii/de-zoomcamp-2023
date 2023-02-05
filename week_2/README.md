# Question 1

## Install
```bash
prefect block register -m prefect_gcp
```

Setup Prefect with 2 blocks:
GCP Credentials to Service Account
GCP Cloud Bucket




## Run
```bash
python etl_web_to_gcs.py 
```

# Question 2

## Build
```bash
prefect deployment build parameterized_flow.py:etl_parent_flow -n "Parameterized ETL Web to GCS"
```

## Apply
```bash
prefect deployment apply etl_parent_flow-deployment.yaml 
```

## Run agent
```bash
prefect agent start --work-queue "default"
```
Play with Cron in Prefect UI 

0 5 1 * *

# Question 3 
## Build
```bash
prefect deployment build parameterized_gcs_to_bq.py:etl_gcs_to_bq -n "Parameterized ETL GCS to BQ"
```
## Apply
```bash
prefect deployment apply etl_gcs_to_bq-deployment.yaml
```
# Question 4

Setup github block directed to this repo

## Run
```bash
python github_flow.py 
```
Custom Run in Prefect UI

# Question 5 & 6
Reuse deployment from question 4

Setup secret block

