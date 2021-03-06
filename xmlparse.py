import xml.etree.ElementTree as et
import re
from datetime import datetime
from datetime import date
import time



class Xmlp():

  #initiatlizes the class and prepares an XMLtree for parsing
  def __init__(self):
    self.tree = et.parse('data/realFM.xml')
    #self.tree = et.parse('FM2xml.xml')
    self.root = self.tree.getroot()


  #This function will return a list.
  #Inside that list will be one list per record.
  #The contents of each record will be in a specific order
  #as follows:

  #The Date the job was created
  #The Date the job is due
  #The Job's name
  #The Job's associated Filemaker Record Number
  #The Job's current status
  #The Artist assigned to the job
  #The Editor assigned to the job
  #The name of the job's client contact

  #In the case of a blank result, the word "None" will be
  #inserted.

  def fetchRecords(self):
    rList = []
    allfound = []

    for child in self.root:
      for row in child:
       idv = row.get('MODID')
       if not (idv == None):
           for col in row:
             for data in col:
               #print data.text
               if(data.text == None or data.text == '?'):
                 #print "FOUND ONE"
                 rList.append("NONE")    
               else:
                 rList.append(data.text)
           allfound.append(rList)
           rList = []

    #print "allfound is this big "+str(len(allfound))    
    #for record in allfound:
      #print record
    
    for record in allfound:
      #print record
      dateInfo = record[0].split('/')
      #print "dateInfo record[0] "+record[3]+' '+str(dateInfo)
      #year day month
      tempDate = date(int(dateInfo[2]),int(dateInfo[0]),int(dateInfo[1]))#pyDate
      record[0] = tempDate
      if (record[1] == 'NONE'):
     #   print "record[1] == NONE "+record[3]
        tempDate = date(int(dateInfo[2])+1,int(dateInfo[0]),int(dateInfo[1]))#pyDate
        record[1] = tempDate
      else:
    #    print "record[1] != NONE "+record[3] 
        dateInfo = record[1].split('/')
        tempDate = date(int(dateInfo[2]),int(dateInfo[0]),int(dateInfo[1]))#pyDate
        record[1] = tempDate
      

#    print "Record Fetch"
#      print k[0]        #open_date
#      print k[1]        #due_date_actual_delivery
#      print k[2]        #description
#      print k[3]        #project_number
#      print k[4]        #status
#      print k[5]        #artist_name
#      print k[6]        #editor_name
#      print k[7]        #client_contact_name
#      print "----End of Record"
#    for record in allfound:
#    	record[0] = #strip that bitch		and record [1]

    return allfound
 


if __name__ == "__main__":

  A = Xmlp()
  A.fetchRecords()

