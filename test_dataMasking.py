from dataMasking import *
from pyspark.sql import SparkSession
from pyspark.sql.functions import udf
from pyspark.sql.types import StringType
import pandas as pd

# spark config
spark = SparkSession.builder \
    .master("local") \
    .appName("Testing data masking udfs") \
    .getOrCreate()

# dummy data
columns = ["cust_id", "cust_name", "dob", "salary", "email_id", "ssn"]
data = [(201, "Gulam Jeelani", "01-01-1972", 200520, "princejeelani08@gmail.com", "852-36-9147"),
        (202, "Nithin Joy A", "23-05-1984", 150580, "nithin.a05@yahoo.com", "945-13-6250"),
        (203, "Saurabh Nautiyal", "15-11-1991", 235410, "saurabh.nautiyal1@live.com", "225-00-4785"),
        (204, "Livingston Anthony Swamy", "20-04-1954", 854621, "livingston.A@microsoft.com", "415-00-7539")]

# creating dataframe
raw_df = pd.DataFrame(data,  columns = columns)
print("==> Original Data <==")
raw_df.head()

# perform shuffle operation
col_list = ["cust_id", "cust_name", "ssn"]
shuffled_df = shuffle(raw_df, col_list)

shuffled_df = spark.createDataFrame(shuffled_df)
# registering udfs
subs_udf = udf(lambda c: substitution(c), StringType())
two_layer_udf = udf(lambda c: two_layer_masking(c), StringType())

# applying udfs to all the columns
masked_df = shuffled_df.select(
        subs_udf("cust_id").alias("Customer ID"),
        two_layer_udf("cust_name").alias("Customer Name"),
        two_layer_udf("dob").alias("Date of Birth"),
        subs_udf("salary").alias("Salary"),
        two_layer_udf("email_id").alias("Email id"),
        two_layer_udf("ssn").alias("SSN")
        )

print("==> Masked Data <==")
masked_df.show(4, False)
