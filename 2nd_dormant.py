from pyspark.sql import SparkSession
from pyspark.sql.types import StructType,StructField
from pyspark.sql.functions import explode
from pyspark.sql.types import *
from pyspark.sql.functions import broadcast
from pyspark.sql.window import Window
import pyspark.sql.functions as F
from pyspark.sql.functions import countDistinct ,col ,when ,split ,lower, lit
from pyspark.sql.functions import concat_ws,col,array
import re
import argparse
from datetime import date
today = date.today()
# Create the parser
my_parser = argparse.ArgumentParser(description='dormant_email_reactivation_airflow')

# Add the arguments
my_parser.add_argument('file4path',
                       type=str,
                       help='the input date for source data.')

my_parser.add_argument('inputpath',
                       type=str,
                       help='the input date for source data.')

my_parser.add_argument('outputpath',
                       type=str,
                       help='the input date for source data.')


args = my_parser.parse_args()
file4path=args.file4path
inputpath = args.inputpath
outputpath = args.outputpath




spark = SparkSession.builder \
    .appName("dormant_email_reactivation_airflow") \
    .getOrCreate()

zschema = StructType([
    StructField("hem", StringType(), True)
])


df1=spark.read.csv("{}last_email/{}".format(file4path,today),sep=",",header=True)

df2=spark.read.csv("{}script_2_input.tsv".format(inputpath),sep="\t",schema=zschema)


join_df = df2.join(df1, df1.hems.contains(df2.hem), how='left')

join_df.write.csv("{}/file_join/join_file_t".format(outputpath),header=True,mode="overwrite")

join_df = join_df.select("rawemail")


join_df.write.csv("{}/file_join/{}".format(outputpath,today),header=True,mode="overwrite")
#pankaj
#pankaj