#============================================#
import tkinter as tk
import json
from tkinter import ttk
from tkinter import *
import random
import os, sys

from tkinter import scrolledtext
import folium
from folium import plugins
import webbrowser
import re
from tkinter.filedialog import askopenfilename
from folium.plugins import HeatMap
#================================================#
#tooltip for folium marker
tooltip = 'Click for more info'


# Create instance
win = tk.Tk()

# Add a title
win.title("Twitter Search")
win.configure(background='black')
#configures window size
win.minsize(width=400, height=500)
win.maxsize(width=400, height=500)

# Disable resizing the GUI
win.resizable(0,0)

#function to open file
def FileOpener():
    filename = askopenfilename()
    return filename
#function to display json file content
def displayJSON(filename):
    #opens file and reads each row
    with open(filename, encoding='utf-8') as data_file:
        for row in data_file:
            data = json.loads(row)
            #displays content from json file
            StringToScroll = "Place Full Name: "+data['place']['fullName'],"Country: ["+data['place']['countryCode']+ "]Date: " + data['createdAt']['$date'] + " latitude:[" + str(data['geoLocation']['latitude'])+ "] longitude:[" + str(data['geoLocation']['latitude']) + " ]Tweet Text:" + data['text'] +  "\n ...... Next Record ........\n"          
            createdAt= data['createdAt']['$date']
            #prints to console
            print("Geo-Location "+str(data['geoLocation']['latitude']))
            print("Tweet Text "+data['text'])
            print("Place Name: "+data['place']['name'])
            print("Country: "+data['place']['countryCode'])
            print("Place Full Name: "+data['place']['fullName'])
            print(" ...... Next Record ........\n")
            scr.insert(tk.INSERT,StringToScroll)
    
#fucntion to searchjson file
def SearchJSON(filename):
    #configures map
    map_osm = folium.Map(location=[53.472328361821766,-2.23959064483645])
    #gets user input from text box
    searchkeyword = name.get()
    #displays keyword in console
    print("you have entered ... "+searchkeyword)
    #opens file with encoding utf 8
    with open(filename, encoding='utf-8') as data_file:
        countt = 0
        #reads in each row from the data file and sets to variable data
        for row in data_file:
            data = json.loads(row)
            tempText = data['text']
            latt = data['geoLocation']['latitude']
            longg = data['geoLocation']['longitude']


            print("you have entered ... "+tempText)
            #for loop and if statement for keyword search
            if searchkeyword in tempText:
                countt = countt + 1
                StringToScroll = "\n\n["+str(countt)+"] Date: " + data['createdAt']['$date'] + "Tweet Text:" + data['text']
                folium.Marker([latt,longg], popup=folium.Popup(tempText,parse_html=True),tooltip=tooltip).add_to(map_osm)
                scr.insert(tk.INSERT,StringToScroll)

            else:
                #error message
                print("Nothing Found")
    #saves map
    map_osm.save('plotted.html')
            


#function for template searching        
def ComboSearch(filename):
    #initilizes arrays
    drugs = ["weed","crack","cocaine","drug","beer"]
    violence = ["stabbed","knife","attack","butcherd"]
    fraud = ["fraud","forgery","credit","bank"]
    #configures the map
    map_osm = folium.Map(location=[53.472328361821766,-2.23959064483645],zoom_start=6, tiles='Stamen Terrain')
    #gets selection from combobox
    searchkeyword = win.myWord.get()
    #if statement to check whats been selected
    if searchkeyword == 'Violence':
        with open(filename, encoding='utf-8') as data_file:
            #creates a count sets it to 0
            countt = 0
            for row in data_file:
                data = json.loads(row)
                tempText = data['text']
                latt = data['geoLocation']['latitude']
                longg = data['geoLocation']['longitude']

                print("you have entered ... "+tempText)
                #for loop and if statement for template searching
                for word in violence:
                    if word in tempText:
                        countt = countt + 1
                        StringToScroll = "\n\n["+str(countt)+"] Date: " + data['createdAt']['$date'] + "Tweet Text:" + data['text']
                        folium.Marker([latt,longg], popup=folium.Popup(tempText,parse_html=True)).add_to(map_osm)
                        scr.insert(tk.INSERT,StringToScroll)
                        
                    else:
                        print("Nothing Found")
                
        map_osm.save('plotted.html')
    #if statement for combo box selection being drugs
    if searchkeyword == 'Drugs':
        with open(filename, encoding='utf-8')as data_file:
            countt = 0
            for row in data_file:
                data = json.loads(row)
                tempText = data['text']
                latt = data['geoLocation']['latitude']
                longg = data['geoLocation']['longitude']
                #for loop and if statement for template searching
                for word in drugs:
                    if word in tempText:
                        countt = countt +1
                        StringToScroll = "\n\n["+str(countt)+"] Date: " + data['createdAt']['$date'] + "Tweet Text:" + data['text']
                        folium.Marker([latt,longg], popup=folium.Popup(tempText,parse_html=True)).add_to(map_osm)
                        scr.insert(tk.INSERT,StringToScroll)

                else:
                    print("Nothing Found")
                
        map_osm.save('plotted.html')
        
    #if statement for combo box selection being fraud
    if searchkeyword == 'Fraud':
        with open(filename, encoding='utf-8') as data_file:
            countt = 0
            for row in data_file:
                data=json.loads(row)
                tempText = data['text']
                latt = data['geoLocation']['latitude']
                longg = data['geoLocation']['longitude']
                #for loop and if statement for template searching
                for word in fraud:
                    if word in tempText:
                        countt = countt +1
                        StringToScroll = "\n\n["+str(countt)+"] Date: " + data['createdAt']['$date'] + "Tweet Text:" + data['text']
                        folium.Marker([latt,longg], popup=folium.Popup(tempText,parse_html=True)).add_to(map_osm)
                        scr.insert(tk.INSERT,StringToScroll)
                else:
                    print("Nothing Found")
        #saves map            
        map_osm.save('plotted.html')
        
#function to show plotted results     
def ShowPlottedSearchResults():
    #opens plot 
    webbrowser.open_new_tab('plotted.html')
#function to showheatmap
def ShowHeatMap():
    #opens heatmap in web browser
    webbrowser.open_new_tab('heatmap.html')

#regular expression function    
def regularexpression(filename):
    #gets userinput
    userinput = regex.get()
    #creates a count
    countt = 0
    #opens file
    with open(filename, errors='ignore') as data_file:
        for row in data_file:
            data = json.loads(row)
            countt = countt +1
            #compiles user input as regex
            regex_object = re.compile(userinput)
            #variable matches will equal the regular expression values found
            matches = re.findall(regex_object, row)
            scr.insert(tk.INSERT,"\n\n["+str(countt)+ data['createdAt']['$date'] + str(matches)+ "\nFrom Tweet:" + data['text'])

def DensitySearch(filename):
    #makes an array
    datas = []
    #sets up folium
    map_osm = folium.Map(location=[53.472328361821766,-2.23959064483645],control_scale = True,zoom_start=11)
    #opens file
    with open(filename,'r', encoding='utf-8') as data_file:
        for row in data_file:
            data=json.loads(row)
            #loads location data
            latt = data['geoLocation']['latitude']
            longg = data['geoLocation']['longitude']
            #appends array to include location as list
            datas.append([latt,longg])
            plugins.HeatMap(datas, min_opacity = 10, max_val = 100).add_to(map_osm)
        #saves map
        map_osm.save('heatmap.html')
                       

               


# Changing our Label
ttk.Label(win, text="Enter a keyword:").grid(column=0, row=0,sticky='W')
# Adding a Textbox Entry widget
name = tk.StringVar()
nameEntered = ttk.Entry(win, width=23, textvariable=name)
nameEntered.grid(column=0,columnspan=2, row=1,sticky='W')
# Adding a Button
action = ttk.Button(win, text="Search Keyword",width=15, command=lambda: SearchJSON(FileOpener()))
action.grid(column=1, row=1,sticky='W')
# Adding a DisplayButton
action = ttk.Button(win, text="Display Tweet", command=lambda: displayJSON(FileOpener())).place(x=210,y=455)
# RegTextBox
regex = tk.StringVar()
nameEntered = ttk.Entry(win, width=23, textvariable=regex)
nameEntered.grid(column=0,columnspan=2, row=5,sticky='W')
# Add a label regex
bLabel = ttk.Label(win, text="Input Regex: ")
bLabel.grid(column=0,row=4,sticky='W')
#Adding a regex Button
action = ttk.Button(win, text="Regex Search",width=15, command=lambda: regularexpression(FileOpener()))
action.grid(column=1,row=5,sticky='W')
#Add a heatmap display button
action = ttk.Button(win, text="Display Heatmap",command = ShowHeatMap).place(x=110,y=455)
# Add a label combobox
bLabel = ttk.Label(win, text="Select a template: ")
bLabel.grid(column=0,row=2,sticky='W')
#Adding a Combo Box
win.myWord = tk.StringVar()
win.combo = ttk.Combobox(win, width = 20, textvariable = win.myWord)
win.combo['values'] = ('Violence','Drugs','Fraud')
win.combo.grid(column =0,columnspan=2, row =3,sticky='W')
# Adding a ComboBox Button
action = ttk.Button(win, text="Search Template",width=15, command=lambda: ComboSearch(FileOpener()))
action.grid(column=1, row = 3,stick='W')
# Adding a button to clear
action = ttk.Button(win, text="Clear",command=lambda: scr.delete(1.0,tk.END)).place(x=295,y=455)
#Adding a densitybutton
action = ttk.Button(win, text="Density", command=lambda: DensitySearch(FileOpener())).place(x=295,y=107)
# Using a scrolled Text control
scrolW = 45
scrolH = 20
scr = scrolledtext.ScrolledText(win, width=scrolW, height=scrolH, wrap=tk.WORD)
scr.grid(column=0,row=7,columnspan=3)
# Adding a Button
action = ttk.Button(win, text="Show Plot Search",command=ShowPlottedSearchResults).place(x=0,y=455)
# Place cursor into name Entry
nameEntered.focus()

win.mainloop()
