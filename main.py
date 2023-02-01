from typing import Optional
from models import Run_info
from fastapi import FastAPI
from mongoengine import connect
import json

app = FastAPI()
connect(db="Cern", host="localhost", port=27023)


#Get all data
@app.get("/")
def index():
    return {"message": "CERN hehe"}

@app.get("/get_all_rundb")
def get_all_rundb():
    rundb= Run_info.objects().to_json()
    rundblist= json.loads(rundb)

    return{"rundb": rundblist}

#Get data by ID
@app.get("/get_rundb/{some_id}")
def get_rundb(some_id):
    print(some_id)
    run_db=Run_info.objects.get(someID=some_id)

    run_dict = {
                   "some_id": run_db.someID,
                   "Fillnumber": run_db.Fillnumber,
                   'dphaseShift1': run_db.phaseShift1,
                   "phaseShift2": run_db.phaseShift2,
                   "StartTime": run_db.StartTime,
                   "StartTimeC": run_db.StartTimeC,
                   "Entries": run_db.Entries,
                   "lumiAtIP1": run_db.lumiAtIP1,
                   "lumiAtIP1withSNDLHC": run_db.lumiAtIP1withSNDLHC,
                   "OfflineMonitoring": run_db.OfflineMonitoring              
                }
    return run_dict

#Querying



    
