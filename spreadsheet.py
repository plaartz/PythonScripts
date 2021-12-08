# Using Google API and gspread creates and updates a sheet with student tardys

import csv
import sys
import datetime
from datetime import timedelta, date
from time import sleep
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('/users/realtbnrlrtzy/desktop/random stuff/stuff/google spreadsheet/Adv Python Project-e3b02a21740d.json', scope)
gc = gspread.authorize(credentials) 

editor_email = 'laartz.porter.personal@gmail.com' # Email to be shared to
workingdir = '/Users/RealTBNRlrtzy/Desktop/random stuff/stuff/google spreadsheet/' # Working directory

def get_time_for_sheet(): # Gets time for sheet title
    return datetime.datetime.now().strftime("%Y-%m-%d")
def get_time_for_row(): # Gets time for the row
    return datetime.datetime.now().strftime("%H:%M:%S")
def getDate(): # Gets time as always increasing integer
    return datetime.datetime.now().strftime("%Y%m%d")

def newSheet(filename): # Creates new cvs and google sheet
    with open(filename, 'w') as csvfile: # Creates csv
        #print(filename)
        fieldnames = ['ID','First','Last','Time']
        writer = csv.writer(csvfile)
        writer.writerow(fieldnames) # Adds header to csv
        newWks = gc.create(get_time_for_sheet()) # Creates new google sheet
        newWks.share(editor_email, perm_type='user',role='owner') # Shares google sheet to var editor_email
        sleep(2)
        wks = gc.open(get_time_for_sheet()).sheet1
        wks.append_row(['Student ID','First name','Last name','Time']) # Adds header to google sheet
        print('New Creation')

def newTardy(sheetName, ID): # Appends ID, First, Last, Time to csv and sheet
    with open('/Users/RealTBNRlrtzy/Desktop/random stuff/stuff/google spreadsheet/students.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile, ['ID','First','Last','Level'])
        for row in reader:
            if row['ID'] == str(ID):
                print(row['First'], row['Last'])
                studentID = row['ID']
                firstName = row['First']
                lastName = row['Last']
                time = get_time_for_row()
    sheetTime = get_time_for_sheet()
    with open(sheetName, 'a') as writecsv:
        writer = csv.writer(writecsv)
        writer.writerow([studentID, firstName, lastName, time]) # Writes row in csv
    wks = gc.open(get_time_for_sheet()).sheet1
    wks.append_row([studentID, firstName, lastName, time]) # Writes row in google sheet


def main(): # Main function
    with open('/Users/RealTBNRlrtzy/Desktop/random stuff/stuff/google spreadsheet/last_date.txt', 'r') as ifDate: # Read date history from last_date.txt
        yDate = ifDate.readline() 
    if int(getDate()) > int(yDate): # If today is more than yesterday, call for newsheet
        newSheet(workingdir+'tardies/'+get_time_for_sheet()+'.csv')
        ifDate.close()
        isFile = True
    else:
        isFile = False
    if isFile is True:
        with open('/Users/RealTBNRlrtzy/Desktop/random stuff/stuff/google spreadsheet/last_date.txt', 'w') as textFile: # Rewrites date if above returned true
            textFile.write(getDate())
  
    for i in range(600):
        yourID = input('Student ID:\n')
        newTardy(workingdir+'tardies/'+get_time_for_sheet()+'.csv',yourID)
        i += 1
    
        
        
if  __name__ == '__main__':
    main()
