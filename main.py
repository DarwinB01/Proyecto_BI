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
ACCESS_KEY_ID =  ""
ACCESS_SECRET_KEY = ""

#Nombre del bucket donde se guardara la informacion
BUCKET_NAME = 'buckettestbi2'

# POST
auth_response = requests.post(DEEZER_REDIRECT_URI, {
    'grant_type': 'client_credentials',
    'client_id': DEEZER_APP_ID,
    'client_secret': DEEZER_APP_SECRET,
})

id_Artist = ['9041042', '7961888', '5536564', '3839','725','355896','4860761','993569','67781','259', '1272674','5412407','525343','13611','517429','17046']
name_Artist = ['Alzate', 'Anuel', 'Arcangel', 'Daddy Yankee', 'Don Omar', 'Giovany Ayala', 'J Balvin ','Jhon Alex Castaño','Julio Jaramillo','Michael Jackson','Romeo Santos','Sech','Silveste ','Tigres del norte','Yandel','Zion ']

BASE_URL_ARTIST = ''
BASE_URL_FANS = ''

for i in range(len(id_Artist)):
    # base URL of all Deezer API endpoints
    BASE_URL_ARTIST = 'https://api.deezer.com/artist/' + id_Artist[i] + '/playlists'
    # actual GET request with proper header
    response = requests.get(BASE_URL_ARTIST);
    res = response.json()

    with open(name_Artist[i] + '_playlist.json', 'w') as f:
        json.dump(res, f, indent=4, sort_keys=True)


    BASE_URL_FANS = 'https://api.deezer.com/artist/' + id_Artist[i] + '/fans'
    # actual GET request with proper header
    response2 = requests.get(BASE_URL_FANS);
    res2 = response2.json()

    with open(name_Artist[i] + '_fans.json', 'w') as f:
        json.dump(res2, f, indent=4, sort_keys=True)

client = boto3.client(
    's3',
    aws_access_key_id=ACCESS_KEY_ID,
    aws_secret_access_key=ACCESS_SECRET_KEY,
)

for i in range(len(name_Artist)):
    upload_file_key = 'Artistas/'+ name_Artist[i]+'/playList/' + name_Artist[i]+'_playlist.json'
    client.upload_file(name_Artist[i]+'_playList.json', BUCKET_NAME, upload_file_key)


    upload_file_key = 'Artistas/' + name_Artist[i]+'/fans/' +name_Artist[i]+ '_fans.json'
    client.upload_file(name_Artist[i]+'_fans.json', BUCKET_NAME, upload_file_key)

