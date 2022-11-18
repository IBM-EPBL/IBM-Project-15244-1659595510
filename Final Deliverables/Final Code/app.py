from flask import Flask, render_template, flash, request, session,send_file
from flask import render_template, redirect, url_for, request

import sys

import pickle


import numpy as np

app = Flask(__name__)
app.config['DEBUG']
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

@app.route("/")
def homepage():
    return render_template('home.html')



@app.route("/result", methods=['GET', 'POST'])
def result():
    if request.method == 'POST':

        vehicleType = request.form['s1']
        yearOfRegistration = request.form['t1']
        gearbox = request.form['s2']
        powerPS = request.form['t3']
        kilometer = request.form['t4']
        monthOfRegistration = request.form['t5']
        fuelType = request.form['s3']
        brand = request.form['s4']
        notRepairedDamage = request.form['s5']


        s1 = 0
        s2 = 0
        s3 = 0
        s4 = 0
        s5 = 0

        if(vehicleType=="bus"):
            s1 = 0
        elif(vehicleType=="limousine"):
            s1 = 1
        elif (vehicleType == "coupe"):
            s1 = 2
        elif (vehicleType == "convertible"):
            s1 = 3

        elif (vehicleType == "small car"):
            s1 = 4


        if (gearbox == "automatic"):
            s2 = 0
        elif (gearbox == "manual"):
            s2 = 1
        elif (gearbox == "not-declared"):
            s2 = 2

        if (fuelType == "diesel"):
            s3 = 0
        elif (fuelType == "petrol"):
            s3 = 1
        elif (fuelType == "not-declared"):
            s3 = 2

        if (brand == "audi"):
            s4 = 0
        elif (brand == "bmw"):
            s4 = 1
        elif (brand == "skoda"):
            s4 = 2
        elif (brand == "honda"):
            s4 = 3






        if (notRepairedDamage == "No"):
            s5 = 0
        elif (notRepairedDamage == "not-declared"):
            s5 = 1








        filename = 'Model/prediction-rfc-model.pkl'
        classifier = pickle.load(open(filename, 'rb'))

        data = np.array([[s1,yearOfRegistration, s2, powerPS,'0',kilometer, monthOfRegistration,s3,s4,s5 ]])

        my_prediction = classifier.predict(data)

        print(my_prediction)


        print(my_prediction[0])
        da = ("%.2f" % round(my_prediction[0], 2))

        return render_template('home.html',res=da)









if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)