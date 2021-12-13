
from __future__ import print_function
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

import json


# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# El ID de la hoja de calculos
SPREADSHEET_ID = '1nY9qc-c7p-kbeTCwKUHdB2DeCKKrYJniFLjN00MNQU8'

#Letras entre las que se encuentran los datos buscados en mi hoja de calculo
RANGE_NAME = '!B:I'


# El fichero credentials.json es el que descargamos mediante la consola de Google Cloud

def acceder_a_formulario():

    ####  configuracion del token de acceso a la API de Gooogle Sheet ####

    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())


    #### Peticion de los datos a la API ####

    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()

    # Pedimos los valores del rango y decidimos si los agrupamos
    # en una matriz fila = fila_hoja_calculo
    # o en una matriz fila = columna_hoja_calculo
    # Ver Google Sheets API:
    # https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets.values/get

    request = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME)
    response = request.execute()
    # Descripcion del objeto response:
    # https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets.values#ValueRange
    # Es un diccionario. En "values" esta el array /matriz de datos
    # get solo carga las filas con datos
    values = response["values"]


    if not values:
        print('No data found.')
    else:
        # Nombres de las columnas de la hoja de calculo
        # Partes de una bici
        columnNames = values[0]
        # Valores de la primera fila de datos (la fila 2)
        # Caracteristicas de este modelo de bici
        # La ultima fila tiene la entrada del formulario
        # mas reciente
        lastRowValues = values[-1]
        # Diccionario con partes de la bici y su valor
        # para este modelo
        document = dict(zip(columnNames, lastRowValues))

        # Crer documento JSON en un archivo para 
        # cargar en MongoATLAS
        json.dump(document, fp=open('naves.json', 'w'), indent=4)


if __name__ == '__main__':
    acceder_a_formulario()