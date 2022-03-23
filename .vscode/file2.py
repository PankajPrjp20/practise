from pyspark.sql import SparkSession
from pyspark.sql import *
from pyspark.sql.functions import * 
from pyspark.sql.types import StructType,StructField, StringType, IntegerType
from pyspark import SparkContext as sc
from smart_open import open, smart_open
import json
from fastavro import json_reader, parse_schema, writer

spark = SparkSession.builder.appName('Practise').getOrCreate()


# Path where json files are stored
p="s3://dummybucketpankaj/liveaudiance_output/json/"
myPath = f"{p}*.json"
lt = []

# Collecting path from S3 bucket
hadoopPath = sc._jvm.org.apache.hadoop.fs.Path(myPath)
hadoopFs = hadoopPath.getFileSystem(sc._jvm.org.apache.hadoop.conf.Configuration())
statuses = hadoopFs.globStatus(hadoopPath)

# Appending all the  Json file path in list lt
for status in statuses:
    lt.append(p+status.getPath().getName())

# Reading AVRO schema
with smart_open("s3://dummybucketpankaj/script/main_script/xandr_avro_sample.avsc") as fp:
    schema = parse_schema(json.load(fp))

# Itreating json files in list and converting to Avro format, Storing avro files with the same name as json file  
for i in lt:
    
    temp1=i.split('/')[-1]
    path=temp1.split('.json')[-2]
    with smart_open(f"s3://dummybucketpankaj/liveaudiance_output/testing_output/{path}.avro", "wb") as avro_file:
        with smart_open(i) as fp:
            writer(avro_file, schema, json_reader(fp, schema))
        
