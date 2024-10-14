
# Trading_Platform_Data_Platorm

  

#### Workflow

1. Install Localstack and write docker compose file :white_check_mark:
2. Create s3 buckets using localstack with partition based on source, stock, time :white_square_button:
3. write python to ingest data from yahoo finance :white_square_button:
4. use apache iceberg as data catalog :white_square_button:
5. use pyspark to process the data :white_square_button:
6. store gold layer data in duck db :white_square_button:


#### Further Enhancements
1. Orchestrate the flow using Apache Airflow
2. work on scalability with integration with Kubernetes
3. work on steps to migrate the architecture on cloud with least downtime possible 