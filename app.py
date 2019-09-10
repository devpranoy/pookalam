# importing packages
from flask import Flask ,render_template, redirect, url_for, session, request, logging
#import requests
#import json
import random
import numpy 
from PIL import Image
import time
import pandas as pd

app = Flask(__name__) #app initialisation

@app.route('/', methods=['GET','POST']) #landing page intent
def home():
    if request.method == 'POST':
        colors=[]
        files = []
        try:
            for item in request.form:
                colors.append(item)
            data = pd.read_csv("1.csv")
            for index, row in data.iterrows():
                if row['color'] in colors:
                    files.append(row['file'])
        
            data1 = random.choice(files)
            data1 = str(data1)
            
            data2 = data1.split('/')
            data = data2[-1]
            print(data)
            return render_template("result.html",data=data)

                


        except:
            return redirect(url_for('home')) #display the html template
    
    return render_template("index.html") #display the html template



if __name__=='__main__':
	app.run(debug=True,host="0.0.0.0",port=8000) 
    #use threaded=True instead of debug=True for production
    # use port =80 for using the http port



#sample code for form data recieve
# request.form['name']
# Sample Code for JSON send data to api

#url = 'URL_FOR_API'
#data = {'TimeIndex':time1 ,'Name':name,'PhoneNumber':phone}
#headers = {'content-type': 'application/json'}
#r=requests.post(url, data=json.dumps(data), headers=headers)
#data = r.json()
#print(data)


#Sample code for JSON recieve data from API

#url = 'URL_FOR_API'
#headers = {'content-type': 'application/json'}
#r=requests.get(url, headers=headers)
#data = r.json()
#count = data['Count']