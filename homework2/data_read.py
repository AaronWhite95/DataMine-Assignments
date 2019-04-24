import pymysql as mdb
from config import host, port, user, passwd, dbname, dataset_table_name, data_file_path
import pandas as pd

class Data_read(object):
    def __init__(self):
        pass

    def dataread(self):
        for year in range(2011, 2017):
            print("year:", year)
            dataframe = pd.read_csv(data_file_path + "/records-for-{}.csv".format(str(year)))
            columnsList = list(dataframe)
            if "Location 1" in columnsList:
                dataframe.rename(columns={"Location 1": "Location"}, inplace = True)
            elif "Location " in columnsList:
                dataframe.rename(columns={"Location ": "Location"}, inplace=True)
            order = ["Agency", "Create Time", "Location", "Area Id", "Beat", "Priority", "Incident Type Id", "Incident Type Description", "Event Number", "Closed Time"]
            newdf = dataframe[order]
            resdf = pd.DataFrame(newdf, columns=["Agency", "Location", "Area Id", "Beat", "Priority", "Incident Type Id", "Incident Type Description", "Event Number"])
            reslist = resdf.values.tolist()
            reslist.insert(0, ["Agency", "Location", "Area Id", "Beat", "Priority", "Incident Type Id", "Incident Type Description", "Event Number"])

            return reslist
