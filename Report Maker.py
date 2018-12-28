import pandas as pd 
import xlrd

data = pd.read_excel("Japan.xlsx")
Model = data.Model.unique()
print(Model)

#Settings
R2 = data["Network Type"] == "R2"
B2 = data["Network Type"] == "B2"
Wired = data["Interface"] == "Wired"
Wifi = data["Interface"] == "Wifi"
Base = data["Diamond Mode"] == "Baseline"
Normal = data["Diamond Mode"] == "Normal mode"
Compatibility = data["Diamond Mode"] == "Compatibility mode"
X = data["Diamond Mode"] == "X mode"

def Initialized():
    for i in Model:
        check_data(i)




def check_data(Model):
    router = data[data["Model"] == Model]
    #router.reset_index(drop = True)
    try:
        if len(router[(R2)]) == 0:
            print(Model + " No Router Mode")
        if router[(B2)].empty:
            print(Model + " No Bridge Mode")
        else:
            if router[(R2 & Wired)].empty:
                print(Model + " R2 No Wired data")
            if router[(R2 & Wifi)].empty:
                print(Model + " R2 No Wifi data")
            if router[(B2 & Wired)].empty:
                print(Model + " B2 No Wired data")
            if router[(B2 & Wifi)].empty:
                print(Model + " B2 No Wifi data")     
    except ValueError:
       print("Somethin Wrong with Model")

        

Initialized()