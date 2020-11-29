#!/usr/bin/python3
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
ACCESS_KEY_ID =  "AKIARHXSAHVRH7ISFHFN"
ACCESS_SECRET_KEY = "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"

#Nombre del bucket donde se guardara la informacion
BUCKET_NAME = 'buckettestbi2'


# POST
auth_response = requests.post(DEEZER_REDIRECT_URI, {
    'grant_type': 'client_credentials',
    'client_id': DEEZER_APP_ID,
    'client_secret': DEEZER_APP_SECRET,
})


# base URL of all Deezer API endpoints
BASE_URL = 'https://api.deezer.com/artist/355896/playlists'

#BASE_URL ='https://api.deezer.com/artist/7961888/fans'

# actual GET request with proper header
response = requests.get(BASE_URL);
res = response.json()
print(res)
print()
print(type(res))

with open('Giovanny Ayala_playList.json', 'w') as f:
    json.dump(res, f, indent=4, sort_keys=True)

'''
ruta='C://Users//user//PycharmProjects//dezzerApi//Artistas//Sech//PlayList'
with open(os.path.join(ruta, 'PlayList JBalvin.json'), 'w') as f:
    json.dump(r, f, indent=4, sort_keys=True)
'''
data = open('anuel_aa_fans.json', 'rb')

s3 = boto3.resource(
    's3',
    aws_access_key_id=ACCESS_KEY_ID,
    aws_secret_access_key=ACCESS_SECRET_KEY,
    config=Config(signature_version='s3v4')
)

s3.Bucket(BUCKET_NAME).put_object(Key='Giovanny Ayala_playList.json', Body=data)
#s3.Object(BUCKET_NAME, 'anuel_aa_fans.json').put(Body=open('test/Artist/Anuel aa/playList/anuel_aa_fans.json', 'rb'))

#s3 = boto3.resource('s3')
#BUCKET = "test"

#s3.Bucket(BUCKET_NAME).upload_file("C://Users//lenovo//Documents//BI", "dump/BI")


client = boto3.client(
    's3',
    aws_access_key_id=ACCESS_KEY_ID,
    aws_secret_access_key=ACCESS_SECRET_KEY,
)

upload_file_key = 'Artistas/'+'Anuel aa/'+'palyList/' + 'anuel_aa_playList.json'
client.upload_file('anuel_aa_playList.json', BUCKET_NAME, upload_file_key)

upload_file_key = 'Artistas/'+'Anuel aa/'+'fans/' + 'anuel_aa_fans.json'
client.upload_file('anuel_aa_fans.json', BUCKET_NAME, upload_file_key)


upload_file_key = 'Artistas/'+'Anuel aa/'+'palyList/' + 'MJ_playList.json'
client.upload_file('MJ_playList.json', BUCKET_NAME, upload_file_key)

print ("Done")
