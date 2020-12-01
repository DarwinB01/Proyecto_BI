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


#Nombre del bucket donde se guardara la informacion
BUCKET_NAME = 'bucketvirgen'

# POST
auth_response = requests.post(DEEZER_REDIRECT_URI, {
    'grant_type': 'client_credentials',
    'client_id': DEEZER_APP_ID,
    'client_secret': DEEZER_APP_SECRET,
})


# base URL of all Deezer API endpoints
BASE_URL = 'https://api.deezer.com/artist/8798/playlists'
#BASE_URL ='https://api.deezer.com/artist/7961888/fans'

# actual GET request with proper header
response = requests.get(BASE_URL);
res = response.json()
print(res)
print()
print(type(res))

with open('anuel_aa_fans.json', 'w') as f:
    json.dump(res, f, indent=4, sort_keys=True)

'''
ruta='C://Users//user//PycharmProjects//dezzerApi//Artistas//J BALVIN//PlayList'
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

#s3.Bucket(BUCKET_NAME).put_object(Key='MJ_playList.json', Body=data)
#s3.Object(BUCKET_NAME, 'anuel_aa_fans.json').put(Body=open('test/Artist/Anuel aa/playList/anuel_aa_fans.json', 'rb'))

#s3 = boto3.resource('s3')
#BUCKET = "test"

#s3.Bucket(BUCKET_NAME).upload_file("C://Users//lenovo//Documents//BI", "dump/BI")


client = boto3.client(
    's3',
    aws_access_key_id=ACCESS_KEY_ID,
    aws_secret_access_key=ACCESS_SECRET_KEY,
)

#ANUEl AA
upload_file_key = 'Artistas/'+'Anuel aa/'+'palyList/' + 'anuel_aa_playList.json'
client.upload_file('anuel_aa_playList.json', BUCKET_NAME, upload_file_key)

upload_file_key = 'Artistas/'+'Anuel aa/'+'fans/' + 'anuel_aa_fans.json'
client.upload_file('anuel_aa_fans.json', BUCKET_NAME, upload_file_key)

#ZION
upload_file_key = 'Artistas/'+'Zion/'+'palyList/' + 'Zion_playList.json'
client.upload_file('Zion_playList.json', BUCKET_NAME, upload_file_key)

upload_file_key = 'Artistas/'+'Zion/'+'fans/' + 'Zion_fans.json'
client.upload_file('Zion_fans.json', BUCKET_NAME, upload_file_key)

#Yandel
upload_file_key = 'Artistas/'+'Yandel/'+'palyList/' + 'Yandel_playList.json'
client.upload_file('Yandel_playList.json', BUCKET_NAME, upload_file_key)

upload_file_key = 'Artistas/'+'Yandel/'+'fans/' + 'Yandel_fans.json'
client.upload_file('Yandel_fans.json', BUCKET_NAME, upload_file_key)

#Tigres del norte
upload_file_key = 'Artistas/'+'Tigres del Norte/'+'palyList/' + 'Tigres del Norte_playList.json'
client.upload_file('Tigres del Norte_playList.json', BUCKET_NAME, upload_file_key)

upload_file_key = 'Artistas/'+'Tigres del Norte/'+'fans/' + 'Tigres del Norte_fans.json'
client.upload_file('Tigres del Norte_fans.json', BUCKET_NAME, upload_file_key)

#Silvestre
upload_file_key = 'Artistas/'+'Silvestre/'+'palyList/' + 'Silvestre_playList.json'
client.upload_file('Silvestre_playList.json', BUCKET_NAME, upload_file_key)

upload_file_key = 'Artistas/'+'Silvestre/'+'fans/' + 'Silvestre_fans.json'
client.upload_file('Silvestre_fans.json', BUCKET_NAME, upload_file_key)

#Sech
upload_file_key = 'Artistas/'+'Sech/'+'palyList/' + 'Sech_playList.json'
client.upload_file('Sech_playList.json', BUCKET_NAME, upload_file_key)

upload_file_key = 'Artistas/'+'Sech/'+'fans/' + 'Sech_fans.json'
client.upload_file('Sech_fans.json', BUCKET_NAME, upload_file_key)
'''
#Romeo Santos
upload_file_key = 'Artistas/'+'Romeo Santos/'+'palyList/' + 'Romeo Santos_playList.json'
client.upload_file('Romeo Santos_playList.json', BUCKET_NAME, upload_file_key)

upload_file_key = 'Artistas/'+'Romeo Santos/'+'fans/' + 'Romeo Santos_fans.json'
client.upload_file('Romeo Santos_fans.json', BUCKET_NAME, upload_file_key)
'''
#Michael Jackson
upload_file_key = 'Artistas/'+'Michael Jackson/'+'palyList/' + 'MJ_playList.json'
client.upload_file('MJ_playList.json', BUCKET_NAME, upload_file_key)

upload_file_key = 'Artistas/'+'Michael Jackson/'+'fans/' + 'MJ_fans.json'
client.upload_file('MJ_fans.json', BUCKET_NAME, upload_file_key)

#Julio Jaramillo
upload_file_key = 'Artistas/'+'Julio Jaramillo/'+'palyList/' + 'Julio Jaramillo_playList.json'
client.upload_file('Julio Jaramillo_playList.json', BUCKET_NAME, upload_file_key)

upload_file_key = 'Artistas/'+'Julio Jaramillo/'+'fans/' + 'Julio Jaramillo_fans.json'
client.upload_file('Julio Jaramillo_fans.json', BUCKET_NAME, upload_file_key)

#Jhon Alex Castaño
upload_file_key = 'Artistas/'+'Jhon Alex Castaño/'+'palyList/' + 'Jhon Alex Castaño_playList.json'
client.upload_file('Jhon Alex Castaño_playList.json', BUCKET_NAME, upload_file_key)

upload_file_key = 'Artistas/'+'Jhon Alex Castaño/'+'fans/' + 'Jhon Alex Castaño_fans.json'
client.upload_file('Jhon Alex Castaño_fans.json', BUCKET_NAME, upload_file_key)

#J Balvin
upload_file_key = 'Artistas/'+'J Balvin/'+'palyList/' + 'J Balvin_playList.json'
client.upload_file('J Balvin_playList.json', BUCKET_NAME, upload_file_key)

upload_file_key = 'Artistas/'+'J Balvin/'+'fans/' + 'J Balvin_fans.json'
client.upload_file('J Balvin_fans.json', BUCKET_NAME, upload_file_key)

#Giovanny Ayala
upload_file_key = 'Artistas/'+'Giovanny Ayala/'+'palyList/' + 'Giovanny Ayala_playList.json'
client.upload_file('Giovanny Ayala_playList.json', BUCKET_NAME, upload_file_key)

upload_file_key = 'Artistas/'+'Giovanny Ayala/'+'fans/' + 'Giovanny Ayala_fans.json'
client.upload_file('Giovanny Ayala_fans.json', BUCKET_NAME, upload_file_key)

#Don Omar
upload_file_key = 'Artistas/'+'Don Omar/'+'palyList/' + 'Don Omar_playList.json'
client.upload_file('Don Omar_playList.json', BUCKET_NAME, upload_file_key)

upload_file_key = 'Artistas/'+'Don Omar/'+'fans/' + 'Don Omar_fans.json'
client.upload_file('Don Omar_fans.json', BUCKET_NAME, upload_file_key)

#Daddy Yankee
upload_file_key = 'Artistas/'+'Daddy Yankee/'+'palyList/' + 'Daddy Yankee_playList.json'
client.upload_file('Daddy Yankee_playList.json', BUCKET_NAME, upload_file_key)

upload_file_key = 'Artistas/'+'Daddy Yankee/'+'fans/' + 'Daddy Yankee_fans.json'
client.upload_file('Daddy Yankee_fans.json', BUCKET_NAME, upload_file_key)

#Arcangel
upload_file_key = 'Artistas/'+'Arcangel/'+'palyList/' + 'Arcangel_playList.json'
client.upload_file('Arcangel_playList.json', BUCKET_NAME, upload_file_key)

upload_file_key = 'Artistas/'+'Arcangel/'+'fans/' + 'Arcangel_fans.json'
client.upload_file('Arcangel_fans.json', BUCKET_NAME, upload_file_key)

print ("Done")
