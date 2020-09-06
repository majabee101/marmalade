import logging

import azure.functions as func
import pyodbc 

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Have now entered the smartfoods budget function')
    userId = req.params.get('UserId')
    budget = req.params.get('Budget')
    if(userId == None or budget == None):
        return func.HttpResponse(
            "Unable to proceed. Check inputs and send a valid UserId or Budget.",
            status_code = 400
        )
    cnxn = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};Server=tcp:smartfoods.database.windows.net,1433;Database=smartfoods;Uid=azurecoder;Pwd=***")
    cursor = cnxn.cursor()
    cursor.execute('UPDATE Budgets SET Budget = ' + budget + ' WHERE UserId = ' + userId)
    cnxn.commit()
    return func.HttpResponse(
        "Budget has been updated to " + budget,
        status_code = 200
    )
