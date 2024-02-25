import snowflake.connector
import csv
import json

class DataTransfer:
    def __init__(self, snowflake_account, snowflake_user, snowflake_password, snowflake_database, snowflake_warehouse, snowflake_schema, snowflake_table):
        self.snowflake_account = snowflake_account
        self.snowflake_user = snowflake_user
        self.snowflake_password = snowflake_password
        self.snowflake_database = snowflake_database
        self.snowflake_warehouse = snowflake_warehouse
        self.snowflake_schema = snowflake_schema
        self.snowflake_table = snowflake_table

    def read_from_snowflake(self, query):
        conn = snowflake.connector.connect(
            user=self.snowflake_user,
            password=self.snowflake_password,
            account=self.snowflake_account,
            warehouse=self.snowflake_warehouse,
            database=self.snowflake_database,
            schema=self.snowflake_schema
        )

        cursor = conn.cursor()
        cursor.execute(query)

        columns = [col[0] for col in cursor.description]
        rows = cursor.fetchall()

        data = []
        for row in rows:
            data.append(dict(zip(columns, row)))

        conn.close()
        return data

# Example usage
transfer = DataTransfer(
    snowflake_account="PJNSAEP-EM62571",
    snowflake_user="GISTHACKATHON",
    snowflake_password="Gisthackathon-1",
    snowflake_database="EMAIL_DATABASE",
    snowflake_warehouse="COMPUTE_WH",
    snowflake_table="EMAILS",
    snowflake_schema="PUBLIC"
)

sql_query = "SELECT * FROM " + str(transfer.snowflake_table)

# Read data from Snowflake and convert to JSON
data = transfer.read_from_snowflake(sql_query)
print(data)