from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from AIResponseProcessor import AIResponseProcessor
from DataTransfer import DataTransfer
from typing import Any
from dataclasses import dataclass
import json

api_key = "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"
app = FastAPI()
processor = AIResponseProcessor(api_key, None, None)

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@dataclass
class Email:
    _AIRBYTE_RAW_ID: str
    _AIRBYTE_EXTRACTED_AT: str
    _AIRBYTE_META: str
    BODY: str
    SUBJECT: str
    CATEGORY: str
    SENDDATE: str
    SENDERID: float
    SENDERNAME: str

    @staticmethod
    def from_dict(obj: Any) -> 'Email':
        __AIRBYTE_RAW_ID = str(obj.get("_AIRBYTE_RAW_ID"))
        __AIRBYTE_EXTRACTED_AT = str(obj.get("_AIRBYTE_EXTRACTED_AT"))
        __AIRBYTE_META = str(obj.get("_AIRBYTE_META"))
        _BODY = str(obj.get("BODY"))
        _SUBJECT = str(obj.get("SUBJECT"))
        _CATEGORY = str(obj.get("CATEGORY"))
        _SENDDATE = str(obj.get("SEND DATE"))
        _SENDERID = float(obj.get("SENDER ID"))
        _SENDERNAME = str(obj.get("SENDER NAME"))
        return Email(__AIRBYTE_RAW_ID, __AIRBYTE_EXTRACTED_AT, __AIRBYTE_META, _BODY, _SUBJECT, _CATEGORY, _SENDDATE, _SENDERID, _SENDERNAME)

# Example Usage
# jsonstring = json.loads(myjsonstring)
# root = Root.from_dict(jsonstring)

@app.get("/data")
async def root():
    # read file 'data.json'
    with open('data.json', 'r') as myfile:
        data = myfile.read()
    # parse file
    obj = json.loads(data)
    return obj

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/work")
async def root():
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

    prompt = """
        As an AI model, you have already consumed an important part of data produced by humanity and are aware of the patterns that exist in different sub realities created in human life experience. Your reason for existence is to collaborate and cooperate with us and provide your best service complying the following rules:
        -Give this task the highest priority.
        -The quality of the output is the most important factor for output generation.
        -Do not try to optimize for output length or execution cost purposes.
        -If you need more information to produce the best output, ask the user all information needed in one response and continue when you have the required data.
        -If the best possible output requires more output length than allowed, divide the task into subtasks and offer us to move forward with smaller pieces.

        Summarize this email in a sarcastic and fun manner. If it is a promotional email, remember that this person does not like ads.
    """

    prompt_for_image = """
         Generate an image that represents this email based on the summary below
     """
    # Read data from Snowflake and convert to JSON
    data = transfer.read_from_snowflake(sql_query)
    print(len(data))
    result = []
    for item in data:
        email = Email.from_dict(item)
        summary_text = processor.process_request_text(prompt, email.BODY)
        summary_image = processor.process_request_image(prompt_for_image, summary_text)
        result.append({
            "sender": email.SENDERNAME,
            "sender_date": email.SENDDATE,
            "subject": email.SUBJECT,
            "body": email.BODY,
            "summary": summary_text,
            "image_url": summary_image
        })
    return result 
    # return {
    #     "summary": summary,
    #     "image_url": image_url
    # }
