
import collections
import csv
from functools import reduce

csvfile = open("911_Calls_for_Service_(Last_30_Days).csv", "r")
list911= csv.DictReader(csvfile)
 

filteredList = list(filter(lambda x: x["zip_code"] !="" and x["neighborhood"] != "", list911))



for i in range(len(filteredList)):
    for a in ["totalresponsetime", "dispatchtime", "totaltime"]:
        if(filteredList[i][a] != ""):
            filteredList[i].update({a: float(filteredList[i][a])})
        else:
            filteredList[i].update({a:0})



totalResponseTime = reduce(lambda x, y: x + float(y["totalresponsetime"]), filteredList,0)
avgResponseTime = (totalResponseTime/len(filteredList))
print(f"The averge responese time is: {avgResponseTime}")

totalDispatchTime = reduce(lambda x, y: x + float(y["dispatchtime"]), filteredList,0)
avgDispatchTime = (totalDispatchTime/len(filteredList))
print(f"The averge dispatch time is: {avgDispatchTime}")

totalTime = reduce(lambda x, y: x + float(y["totaltime"]), filteredList,0)
avgTime = (totalTime/len(filteredList))
print(f"The averge total time is: {avgTime}")


neighborhoods = []

# print(filteredList[0])

for i in filteredList:
    neighborhoods.append(i["neighborhood"])



neighborhood = set(neighborhoods)

result = collections.defaultdict(list)

for d in filteredList:
    result[d["ï»¿X"]].append(d)

result_list = list(result.values())

print(result_list[0])
