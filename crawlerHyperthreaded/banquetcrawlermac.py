import os
import json
import time

cities=[]   #cities list to store names of cities (to ignore destination wedding)
os.system("rm -rf banquets")  #remove previous set of cities for a fresh start
os.system("mkdir banquets")   #make cities directory again
with open('cities.json') as json_file:  #open data present in cities.json
    data = json.load(json_file) #load data into a list using json library
    for c in data[0]['city'][:-1]:  #running the cities present in the 'cities.json' file through a loop ignoring the last entry 'destination wedding' due to formatting issues
        os.system('rm banquets/'+c+'.json')  #removing previous entries
        script= open(c+".sh","w");  #create a new script for each city <city>.sh (for low budget hyperthreading)
        script.write('scrapy crawl banquetscrapermore -a start_url="https://weddingz.in/banquet-halls/'+c+'/all/" -o '+c+'.json\n') #run crawler for each city, save the data to <cityname>.json file
        script.write('mv '+c+'.json banquets')    #move every <city>.json files to another folder as they are completed
        script.close(); #write the script
        os.system('bash '+c+'.sh &')    #run the script in background to allow multiple scripts running at once
