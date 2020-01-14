import os
import json
import time

os.system('rm cities.json') #remove cities.json file (this step might be unnecessary but haven't checked yet)
os.system('scrapy crawl cityscraper -o cities.json')    #this will crawl for new cities
#os.system('cp cities.json tutorial/spiders/cities.json')
os.system('touch master.json')  #create master.json file to hold all data
master= open("master.json","w+")    #loading master.json in python
master.write('{"banquets":{\r\n')   #master.josn formatting
master.close()  #writing master.json
cities=[]   #cities list to store names of cities (to ignore destination wedding)
os.system("rm -rf cities")  #remove previous set of cities for a fresh start
os.system("mkdir cities")   #make cities directory again
with open('cities.json') as json_file:  #open data present in cities.json
    data = json.load(json_file) #load data into a list using json library
    for c in data[0]['city'][:-1]:  #running the cities present in the 'cities.json' file through a loop ignoring the last entry 'destination wedding' due to formatting issues
        os.system('rm '+c+'.json')  #removing previous entries
        script= open(c+".sh","w");  #create a new script for each city <city>.sh (for low budget hyperthreading)
        script.write('scrapy crawl banquetscrapermore -a start_url="https://weddingz.in/banquet-halls/'+c+'/all/" -o '+c+'.json\n') #run crawler for each city, save the data to <cityname>.json file
        script.write('mv '+c+'.json cities')    #move every <city>.json files to another folder as they are completed
        script.close(); #write the script
        os.system('bash '+c+'.sh &')    #run the script in background to allow multiple scripts running at once
    while True: #this loop checks if all cities have been crawled
        list = os.listdir("cities") #just an arbitrary list to check if all the lists are completed
        if len(list)==len(data[0]['city'])-1:   #check if data from all cities has been recieved
            for c in data[0]['city'][:-1]:  #run a loop on all cities to add their data to a single master.json file
                os.system('rm '+c+'.sh')    #remove the script made for that city
                if os.stat('cities/'+c+'.json').st_size != 0:   #check if the <city>.json contains any data
                    master=open("master.json","a+") #open master.json file (append)
                    master.write('"'+c+'":')    #add city name (json formatting reasons)
                    master.close()  #write the changes to master.json
                    os.system('cat cities/'+c+'.json >> master.json')   #add contents of <city>.json to master.json
                    master=open("master.json","a+") #open master.json file (append)
                    master.write('\r\n,\r\n')   #formatting
                    master.close()  #write the changes to master.json
                    cities.append(c)    #add city name to the cities list
            break   #break the loop that checks if all cities ave been crawled
        time.sleep(1)   #adds an interval after each check to reduce cpu usage
with open('cities.json', 'w') as outfile:   #open cities.json as writeable file (overwrite, not append)
    json.dump(cities, outfile)  #write contents of cities converted to json format back to cities.json file
os.system("sed -i '' -e '$ d' master.json") #remove the extra space at the end added while adding cities to master.json file
master=open("master.json","a+") #open master.json file (append)
master.write('}}')  #json formatting
master.close()  #write the changes to master.json file
#master.close()
#os.system('scrapy crawl banquetscraper -o wed.json')
