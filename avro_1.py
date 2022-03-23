# import avro

# from avro.datafile import DataFileReader, DataFileWriter
# from avro.io import DatumReader, DatumWriter

# reader =  DataFileReader(open(r"C:\Users\u27l79\Downloads\part-00000-dfaa87c1-a4c4-4ead-a229-0a088732ce14-c000.avro","rb"),DatumReader())
# for user in read
# er:
#     print(user) 

# from pyspark.sql import SparkSession
# from pyspark.sql import *
# from pyspark.sql.functions import * 
# from pyspark.sql.types import StructType,StructField, StringType, IntegerType
# from pyspark import SparkContext as sc
# from smart_open import open
# from benedict import benedict
# import json
# from awscli.clidriver import create_clidriver

# spark = SparkSession.builder.appName('Practise').getOrCreate()

# structureSchema  = StructType([StructField('id',StringType(),True),StructField('segments',StringType(),True)])

# data = spark.read.options(delimiter='\t').schema(structureSchema).csv(f's3://liveaudiences/xandr/li_nonid_audiences/20220105/part-r-00000-06ed0383-cfbd-4b16-8971-238ece5e6238.gz')




# df = data.select('id',split(col('segments'), ',').alias("new_segments")).drop('segments')

# df2= df.select(df.id, explode(df.new_segments).alias('segment'))

# structureSchema  = StructType([
#     StructField('Audience_Name',StringType(),True),
#     StructField('LiveAudience_ID',IntegerType(),True),
#     StructField('Xandr_ID',IntegerType(),True)
# ])
# data1 = spark.read.options(delimiter='\t').schema(structureSchema).csv('s3://liveaudiences/xandr/mapping/liveaudience_to_xandr_mapping.tsv').dropna()

# newDF = df2.join(data1, df2.segment == data1.LiveAudience_ID, 'inner').drop('LiveAudience_ID', 'Audience_Name', 'segment')

# newDF1 = newDF.select(\
#              'id', \
#              lit("liveintent.com").alias('source'),\
#              ('Xandr_ID'), \
#              lit("").alias('code'),\
#              lit(13191).cast('long').alias('member_id'),\
#              lit(0).cast('long').alias('expiration'),\
#              lit(0).cast('long').alias('timestamp'),\
#              lit(0).cast('long').alias('value')
#             )

# n=newDF1.select(struct( 
#     struct('id', 'member_id').alias("external_id")).alias('uid'),
#     struct(newDF1['Xandr_ID'].cast('long').alias('id'), 'expiration' ).alias('segments')).groupby('uid').agg(collect_list('segments').alias('segments'))
# # n.write.format('json').mode("overwrite").save(f's3://dummybucketpankaj/dummy6/1_1/json/20220228/')
# n.write.format('avro').mode("overwrite").save(f's3://dummybucketpankaj/dummy6/1_1/avro/20220228/')
# # n.write.format('text').mode("overwrite").save(f's3://dummybucketpankaj/dummy6/1_1/text/20220228/')



# p="s3://lasso-dmd-partner-liveintent-comm/download/cluster/lasson_nonID_apnx_maid/US/20220206/_FORMAT"
# s1=s.replace("FORMAT.json"," ")
# print(s1.split("/"),'_')

# c = cp.replace(cp.split('/')[-1],'')

# cp = s.replace('FORMAT.json','')
# # print(cp)

# cp = p.replace('/_FORMAT','').replace(p.split('/')[-2],'')
# print(cp)
# c = cp.replace(cp.split('/')[-1],'')

# # dt = getlatestDate(c)
# print(c)


