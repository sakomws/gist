## Prerequisites

Packages used:
* OpenAI API
* snowflake-converter
* csv

## Usage

The `DataTransfer` class takes the following Snowflake credentials as input:
* snowflake_account
* snowflake_user
* snowflake_password
* snowflake_database
* snowflake_warehouse
* snowflake_schema
* snowflake_table

Using these credentials, the `snowflake-converter` API is leveraged to read data from the Snowflake database.