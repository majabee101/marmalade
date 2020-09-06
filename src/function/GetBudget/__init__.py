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
    cnxn = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};Server=tcp:smartfoods.database.windows.net,1433;Database=smartfoods;Uid=azurecoder;Pwd=****")
    cursor = cnxn.cursor()
    cursor.execute('SELECT Budget FROM Budgets a WHERE a.UserId = ' + userId)
    budget = cursor.fetchone()[0]
    return func.HttpResponse(
        '{:.2f}'.format(round(budget, 2)),
        status_code = 200
    )
