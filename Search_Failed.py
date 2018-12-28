import numpy as np
import pandas as pd 
import xlrd

data = pd.read_excel("Japan.xlsx")
Failed = data[data["Result"] == "Fail"].reset_index(drop = True)

#Threshold
speed_test_threshold = 30
print("Total: " + str(len(Failed)) , "Router Failed")


def Filter():
    for i in range(len(Failed)):
        #Model
        Model = data["Model"] == Failed.loc[i,"Model"]
        #Network Type
        Network_Type = data["Network Type"] == Failed.loc[i,"Network Type"]
        #Interface
        Interface = data["Interface"] == Failed.loc[i,"Interface"]
        #Baseline
        Baseline = data["Diamond Mode"] == "Baseline"
        Base = data[(Model & Network_Type & Interface & Baseline)].reset_index(drop = True)
        Compare(i,Failed,Base)


def Compare(i,Failed,Base):
    global speed_test_threshold
    reprot = ""
    print(i , Failed.loc[i,"Brand"] , " " , Failed.loc[i,"Model"] , " " , Failed.loc[i,"Network Type"] , " " , Failed.loc[i,"Interface"])
    if type(Failed.loc[i,"Speedtest-DL(Mbps)"]) == str:
        print("Connection Failed")
    else:
        DL_speed_persentage = (1 - Failed.loc[i,"Speedtest-DL(Mbps)"] / Base.loc[0,"Speedtest-DL(Mbps)"]) * 100
        UL_speed_persentage = (1 - Failed.loc[i,"Speedtest-UL(Mbps)"] / Base.loc[0,"Speedtest-UL(Mbps)"]) * 100
        if int(DL_speed_persentage) > speed_test_threshold:
            reprot = reprot +  "DL Speed Drop " + str(int(DL_speed_persentage)) + "%\n"
        if int(UL_speed_persentage) > speed_test_threshold:
            reprot = reprot +  "UL Speed Drop " + str(int(UL_speed_persentage)) + "%\n"
        if Failed.loc[i,"wrs21"] == "Fail":
            reprot = reprot + "wrs21 Failed\n"
        if Failed.loc[i,"Streaming"] == "Fail": 
            reprot = reprot + "Streaming Failed\n"
    print(reprot)
    
Filter()
        

        
