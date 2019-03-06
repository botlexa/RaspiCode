import RPi.GPIO as GPIO
import time
import sys
import logging
import psycopg2
import json
import tkinter
import pygame

from db_util import make_conn, fetch_one_row_data, fetch_data, execute_query

window = tkinter.Tk()
window.title("Alexa Automated Form Filling Software")
label = tkinter.Label(window, text = "Welcome to ICICI bank, please sit in front of the chair to start filling the form !").pack()
pygame.mixer.init()

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN)         #Read output from PIR motion sensor
def getcustomername(custid):
    conn = make_conn()
    query_cmd = "select Name from UserMaster where UserID = " + str(custid) + ';'
    result = fetch_one_row_data(conn, query_cmd)
    conn.close() 
    return result
def getformname(custid):
     conn = make_conn()
     query_cmd = "select TemplateName from TemplateMaster where UserID" = + str(custid)+';'
     result = fetch_data(conn, query_cmd)
     conn.close()
def getformdata(formid):
    conn = make_conn()

    query_cmd = "select FieldMaster.FieldName, FieldDetails.FieldValue from FieldDetails " \
                "INNER JOIN FieldMaster ON FieldMaster.FieldMasterID = FieldDetails.FieldMasterID " \
                "WHERE FieldDetails.TemplateCustomerMappingID = " + str(formid) + ";"
    result = fetch_data(conn, query_cmd)
    conn.close()
    return result

while True:
	i=GPIO.input(11)
	if i==1:                                        #When output from PIR is HIGH,i.e customer is sitting infront of the alexa
        pygame.mixer.music.load("invokealexa.wav")  #Wav file which contains the alexa voice activation command
        pygame.mixer.music.play()
        sleep(10)                                   #Delay till customer fills the name
        uname= getcustomername(custid)
        tkinter.Label(window, text = "Username: ").grid(row = 0)
        tkinter.Label(window, text = str(uname)).grid(row = 0, column=1)

        formname= getformname(custid)
        tkinter.Label(window, text = "FormName : ").grid(row = 1)
        tkinter.Label(window, text = str(formname)).grid(row = 1, column=1)

        formdata= getformdata(formid)
        tkinter.Label(window, text = "Form Details :").grid(row = 2)
        tkinter.Label(window, text = str(formdata)).grid(row = 2, column=1)        
        sleep(10)
	elif i==1:               #When output from PIR is LOW, i.e no motion
	    sleep(2)
window.mainloop()
time.sleep(0.1)
