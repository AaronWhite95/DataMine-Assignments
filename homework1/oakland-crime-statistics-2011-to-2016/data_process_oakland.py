import pandas as pd
import json
import numpy
class MyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, numpy.integer):
            return int(obj)
        elif isinstance(obj, numpy.floating):
            return float(obj)
        elif isinstance(obj, numpy.ndarray):
            return obj.tolist()
        else:
            return super(MyEncoder, self).default(obj)

# "Agency", "Create Time", "Location", "Area Id", "Beat", "Priority", "Incident Type Id", "Incident Type Description", "Event Number", "Closed Time"

def Nominal(dataframe):
    resdic = {}
    col1 = dataframe["Agency"].value_counts()
    #col2 = dataframe["Create Time"].value_counts()
    col3 = dataframe["Location"].value_counts()
    col4 = dataframe["Area Id"].value_counts()
    col5 = dataframe["Beat"].value_counts()
    col6 = dataframe["Priority"].value_counts()
    col7 = dataframe["Incident Type Id"].value_counts()
    col8 = dataframe["Incident Type Description"].value_counts()
    #col9 = dataframe["Event Number"].value_counts()
    #col10 = dataframe["Closed Time"].value_counts()

    resdic["Agency"] = dict(col1)
    #resdic["col2"] = dict(col2)
    resdic["Location"] = dict(col3)
    resdic["Area Id"] = dict(col4)
    resdic["Beat"] = dict(col5)
    resdic["Priority"] = dict(col6)
    resdic["Incident Type Id"] = dict(col7)
    resdic["Incident Type Description"] = dict(col8)
    #resdic["col9"] = dict(col9)
    #resdic["col10"] = dict(col10)
    return resdic

if __name__ == '__main__':
    for year in range(2011, 2017):
        print("year:", year)
        dataframe = pd.read_csv("records-for-{}.csv".format(str(year)))
        columnsList = list(dataframe)
        if "Location 1" in columnsList:
            dataframe.rename(columns={"Location 1": "Location"}, inplace = True)
        elif "Location " in columnsList:
            dataframe.rename(columns={"Location ": "Location"}, inplace=True)
        order = ["Agency", "Create Time", "Location", "Area Id", "Beat", "Priority", "Incident Type Id", "Incident Type Description", "Event Number", "Closed Time"]
        dataframe = dataframe[order]
        res = Nominal(dataframe)

        with open("result-{},json".format(year), 'w', encoding="utf-8") as wf:
            json.dump(res, wf, cls=MyEncoder)

        #dataframe = dataframe.append(temdf, ignore_index=True)
        #print(len(dataframe))