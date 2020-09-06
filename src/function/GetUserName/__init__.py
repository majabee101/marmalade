import logging

import azure.functions as func
import pyodbc 

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Have now entered the smartfoods budget function')
    userId = req.params.get('UserId')
    if(userId == None):
        return func.HttpResponse(
            "Unable to proceed. Check inputs and send a valid UserId.",
            status_code = 400
        )
    cnxn = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};Server=tcp:smartfoods.database.windows.net,1433;Database=smartfoods;Uid=azurecoder;Pwd=M!crosoft123")
    cursor = cnxn.cursor()
    cursor.execute('SELECT a.UserName FROM Users a WHERE a.UserId = ' + userId)
    userName = cursor.fetchone()[0]
    return func.HttpResponse(
        userName,
        status_code = 200
    )
