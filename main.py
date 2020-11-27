import requests
import json
import boto3
from botocore.client import Config
import os

#Datos necesarios para la conexion con la API

DEEZER_APP_ID = "446922"
DEEZER_APP_SECRET = "13ff2539f9cad5050430e6544fa6cd2e"
DEEZER_REDIRECT_URI = "http://developers.deezer.com/api"

#Credenciales aws
ACCESS_KEY_ID =  "AKIAQRVRDMTQ3ZSRA6HT"
ACCESS_SECRET_KEY = "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"
BUCKET_NAME = 'buckettestbi'


# POST
auth_response = requests.post(DEEZER_REDIRECT_URI, {
    'grant_type': 'client_credentials',
    'client_id': DEEZER_APP_ID,
    'client_secret': DEEZER_APP_SECRET,
})


# base URL of all Deezer API endpoints
BASE_URL = 'https://api.deezer.com/artist/7961888/playlists'


# actual GET request with proper header
response = requests.get(BASE_URL);
res = response.json()
print(res)
print()
print(type(res))

with open('anuel_aa_playList.json', 'w') as f:
    json.dump(res, f, indent=4, sort_keys=True)


data = open('anuel_aa_playList.json', 'rb')

s3 = boto3.resource(
    's3',
    aws_access_key_id=ACCESS_KEY_ID,
    aws_secret_access_key=ACCESS_SECRET_KEY,
    config=Config(signature_version='s3v4')
)
#s3.Bucket(BUCKET_NAME).put_object(Key='anuel_aa_playList.json', Body=data)

client = boto3.client(
    's3',
    aws_access_key_id=ACCESS_KEY_ID,
    aws_secret_access_key=ACCESS_SECRET_KEY,
)

for file in os.listdir():
    if '.json' in file:
        file_upload = BUCKET_NAME
        file_upload_key = 'test/Artist/Anuel aa/playList/'+ str(file)
        client.upload_file(file,file_upload, file_upload_key)


print ("Done")
