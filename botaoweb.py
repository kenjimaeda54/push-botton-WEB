from flask import Flask,render_template
import datetime
import RPi.GPIO as GPIO
import time



app = Flask(__name__)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM) 
PORTAO=20

GPIO.setup(PORTAO,GPIO.IN)
    
@app.route("/")
def inicio():   
     while True:  
         time.sleep(3.90)
         if GPIO.input(PORTAO) == 0:
              return render_template('alerta.html')
         else:
              return render_template('portaoweb.html')
app.run(debug=True,host='0.0.0.0')

