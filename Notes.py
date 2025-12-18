# 6. Databricks Free Account Creation on GCP
# databrics setup ==> 9:10 / 17:44



# databricks is unified multicloud lakehouse architecture platform support GCP, AWS, Azure
# databrick used for data ingestion, data processing, data transformation 
# entire data (landing, bronze, silver, gold) stored in GCS
# for propelry govering of data from begining to end of pipline we are going to use unit catalog, which is unified data governance solution provided by databricks
# we are going to use unity catalog for governanvce layer
# unity catalog is unified data governance solution provided by databricks
# catalog (dev_catalog) => first component of unity catalog or collection of schemas 
# unity catalog manages entire access control for data stored in GCS
# Delta table (provised plenty of features like ACID transaction, schema enforcement, time travel, etc)
#   1. Versioning comes in picture
#  2. Acid properties
#  3. data stored in parquate data
# 4. logs are stored in the form of json files
# 5. data is stored in the form of managed tables only
# 5. you get plenty of features when you use delta tables
# Want to read data from GCS (raw_traffic, raw_roads) and load it into bronze tables (delta tables) for that I am uding autoloader schema
# spark.readStream
        # .format("cloudFiles")
# Above indicate this is autoloader schema  
# autoloader schema is used to load data from cloud storage (GCS, S3, ADLS) into delta tables
# autoloader schema automatically detect new files arriving in the cloud storage location and load it into delta tables
# autoloader schema support two modes
# 1. file notification mode
# 2. directory listing mode
# autoloader => is a data injestion utility for incremenlty loading your data from cloud storage into delta lake tables
# autoloader is data injestion framework developed by databricks to incremenlty load data from cloud storage into delta tables
# Structtype, structfield are two funciton used to create custom schema in pyspark
#         .load(landing+'/raw_traffic/') => from where it identifis it's is dev project gcs bucket landing location ?
# How dev project, dev prohect gcs configured with dev workspace ?
# .trigger(availableNow=True) => stops the streaming once data is written --> batch 
# readStream, writeStream => structured streaming
# streaming data processing is used when data is arriving in continous fashion
# -----------------------------------
# Role of data engineer
# 1. Data injestinon
# 2. Data storage and management
# 3. Data Processing and transformation
# 4. Data quality and governance
# 5. data pipeline orchestration
# 6. Performance Optimization
# 7. Monitoring and maintenance
# -----------------------------------
# region selecton 
# cost, availability, single or multi region, target user location (less performane, cost will be more, less availability, high latency, network issues)
# -----------------------------------
# Project Implementation guide/steps:


# Databrics setup
    #   Create two projects in GCP
    #       dev (project-dev-01122025)
    #       uat (project-uat-01122025)
    
    #   Go to databrics console
    #       Delete default workspace, metastore
    #       Create uc metastore (gcp-dbx-metastore)  
    #       region (us-central1)
    #       gcs bucket ( gcp-dbx-ms-01122025)
    #       grant permission to gcs bucket 

    #   Create two workspaces
    #       dev (dbx-dev-workspace) (us-central1) (project-dev-01122025)
    #       uat (dbx-uat-workspace) (us-central1) (project-uat-01122025)

    #   Assign the workspaces to the us metastore



# Setup infra dev env:
#       create dev gcs bucket

#       setup folders
#           landing
#               raw_traffic
#               raw_roads
#           checkpoints
#           medallian
#               bronze
#               silver
#               gold

#       Create catalog => dev_catalog

#       Create dev storage credentials (bkt-dev-creds)

#       Create 5 external locations to access GCS:
#           landing_dev
#           checkpoints_dev
#           bronze_dev
#           silver_dev
#           gold_dev

#       create databrick cluster (dev-cluster)



# development steps:
#       create schemas dynamically (01 NB)
#           bronze
#           silver
#           gold

#       creating bronze tables dynamically (02 NB)
#           raw_roards
#           raw_traffic

#       load to bronze (03 NB) (autoloader)
#           landing to bronze tables
#       Silver_traffic_transformations (04 NB) (Structured streaming)
#           bronze --> clea, transformed --> silver tables
#       Silver_roads_transformations (05 NB) (Structured streaming)
#           bronze --> clea, transformed --> silver tables
#       gold_transformations (06 NB) (structured streaming)
#           silver --> aggregated --> gold tables
#           gold tables
#               gold_traffic
#               gold_roads
#               traffic volume by year
#               traffic volume by region
#               road usage statistics
#               ev adoption trends 

# workflow oorchestraion:
#       ensure all your notebooks are production ready with error handling and logging mechanisms in place.
#       create workflow (ETL workflow) --> parameter => (env = dev)
#           task1: load to bronze (03 NB)
#           task2: silver_traffic_transformations (04 NB)
#           task3: silver_roads_transformations (05 NB)
#           task4: gold_transformations (06 NB)
#       trigger
#           file arrival: raw_traffic gcs location


# setup github: (dev --> uat --> prod)
#       go to github and create account
#       create repo : (gcp-dbx-traffic)
#       integrate github with databricks
#       create branches
#           main (prod)
#           dev
#           uat


# back to dev
#       move dev code to dev branch
#       commit and push the changes (warning: install databricks on top of github)
#       update pipeline to git (url, branch) for all tasks and choose notebook path
#       run and test pipeline => success