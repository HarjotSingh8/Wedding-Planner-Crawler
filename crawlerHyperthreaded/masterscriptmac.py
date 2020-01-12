import os
import json

os.system('rm cities.json')
os.system('scrapy crawl cityscraper -o cities.json')    #this will crawl for new celebrities
os.system('cp cities.json tutorial/spiders/cities.json')
os.system('touch master.json')
master= open("master.json","w+")
master.write('{"banquets":{\r\n')
master.close()
#os.system('cat chandigarh.json >> master.json')
cities=[]
os.system("rm -rf cities")
os.system("mkdir cities")
with open('cities.json') as json_file:
    data = json.load(json_file)
    #print("data = ")
    #print(data[0]['city'][0])
    #print("this was data")
    for c in data[0]['city'][:-1]:
        #print('city: '+c)         #just verbose output for debugging purposes
        #os.system('rm '+c+'.json')  #removing previous entries
        script= open(c+".sh","w");
        script.write('scrapy crawl banquetscrapermore -a start_url="https://weddingz.in/banquet-halls/'+c+'/all/" -o '+c+'.json\n')
        script.write('mv '+c+'.json cities')
        script.close();
        os.system('bash '+c+'.sh &')
        #os.system('gnome-terminal -e "scrapy crawl banquetscrapermore -a start_url="https://weddingz.in/banquet-halls/'+c+'/all/" -o '+c+'.json ; mv '+c+'.json cities"')
    while True:
        list = os.listdir("cities")
        if len(list)==len(data[0]['city'])-1:
            for c in data[0]['city'][:-1]:
                os.system('rm '+c+'.sh')
                master=open("master.json","a+")
                master.write('"'+c+'":')
                master.close()
                os.system('cat cities/'+c+'.json >> master.json')
                master=open("master.json","a+")
                master.write('\r\n,\r\n')
                master.close()
                if os.stat('cities/'+c+'.json').st_size == 0:
                    os.system("sed -i '' -e '$ d' master.json")
                    os.system("sed -i '' -e '$ d' master.json")
                else:
                    cities.append(c)

            break
        '''master=open("master.json","a+")
        master.write('"'+c+'":')
        master.close()
        os.system('cat '+c+'.json >> master.json')
        master=open("master.json","a+")
        master.write('\r\n,\r\n')
        master.close()
        if os.stat(c+'.json').st_size == 0:
            os.system('sed -i "$ d" master.json')
            os.system('sed -i "$ d" master.json')
        else:
            cities.append(c)'''
#print(cities)
with open('cities.json', 'w') as outfile:
    json.dump(cities, outfile)
os.system("sed -i '' -e '$ d' master.json")
master=open("master.json","a+")
master.write('}}')
master.close()
#master.close()
#os.system('scrapy crawl banquetscraper -o wed.json')
