# Gist

## Chat Backend
We are pulling data from Snowflake and processing: summarize with AI and create image. Then storing it into Google Cloud storage.
We expose as API /data it returns all emails: subject, body, sender, time, summary and image generated by ai. It is in Python.

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


## Multimodal Backend


## UI

## Data-platform
Pushing csv, json etc.
