# Load transformed data to Snowflake
import snowflake.connector
ctx = snowflake.connector.connect(
    user='YOUR_USER',
    password='YOUR_PASSWORD',
    account='YOUR_ACCOUNT'
)
cs = ctx.cursor()
cs.execute('CREATE DATABASE IF NOT EXISTS FLIGHTS_DB')
print('Connected to Snowflake and created database')
