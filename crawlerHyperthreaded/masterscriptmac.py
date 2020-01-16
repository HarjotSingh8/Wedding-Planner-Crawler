import os
import json
import time
import hashlib
os.system('mkdir banquets')
os.system('rm cities.json') #remove cities.json file (this step might be unnecessary but haven't checked yet)
os.system('scrapy crawl cityscraper -o cities.json')    #this will crawl for new cities
os.system('touch master.json')  #create master.json file to hold all data
cities=[]   #cities list to store names of cities (to ignore destination wedding)
checks=1
os.system('python banquetcrawlermac.py &')
with open('cities.json') as json_file:  #open data present in cities.json
    data = json.load(json_file) #load data into a list using json library
    for c in data[0]['city'][:-1]:  #running the cities present in the 'cities.json' file through a loop ignoring the last entry 'destination wedding' due to formatting issues
        cities.append(c)
dict={}
dict['cities']=cities
while checks>0: #this loop checks if all cities have been crawled
    list = os.listdir("banquets") #just an arbitrary list to check if all the lists are completed
    if len(list)==len(cities):   #check if banquet data from all cities has been recieved
        checks=checks-1
        print(checks)
        dict['banquets'] = {}
        count=0
        for c in cities:  #run a loop on all cities to add their data to a single master.json file
            dict['banquets'][c]= {}
            os.system('rm '+c+'.sh')    #remove the script made for that city
            if os.stat('banquets/'+c+'.json').st_size != 0:   #check if the <city>.json contains any data
                with open('banquets/'+c+'.json') as json_file:  #open data present in cities.json
                    data = json.load(json_file) #load data into a list using json library
                    for d in data:  #running the cities present in the 'cities.json' file through a loop ignoring the last entry 'destination wedding' due to formatting issues
                        count+=1
                        if(count==1000):
                            print("broke")
                            break
                        hash = hashlib.sha256(d["name"].encode('utf-8')).hexdigest()
                        dict['banquets'][c][hash] = {}
                        for e in d:
                            dict['banquets'][c][hash][e]=d[e]
                        #print(hashlib.sha256(d["name"].encode('utf-8')).hexdigest())
    time.sleep(1)   #adds an interval after each check to reduce cpu usage
print(cities)
with open('cities.json', 'w') as outfile:   #open cities.json as writeable file (overwrite, not append)
    json.dump(cities, outfile)  #write contents of cities converted to json format back to cities.json file
with open('master.json', 'w') as outfile:   #open cities.json as writeable file (overwrite, not append)
    json.dump(dict, outfile, indent=2)  #write contents of cities converted to json format back to cities.json file
