from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import QDateTime
import datetime, re
from datetime import time

'''
The main objective for this class is to populate the 
listwidgets that are part of the MainWindow
'''

class HandleLists:

  def __init__(self,MainWindow):
    self.window = MainWindow
    self.artStatus = False
    self.editStatus = False
    self.statStatus = False

  '''
  is_Selected is a function that takes single
  record from the XML file and checks to see if
  the record falls into the states selected in 
  MainWindow
  '''

  def is_Selected(self,singleRecord):
    self.artStatus = False
    self.editStatus = False
    self.statStatus = False
    for i in range(self.window.formLayout_3.count()):
      employeeCBText = self.window.formLayout_3.itemAt(i).widget().text()
      if(employeeCBText == singleRecord[5] or employeeCBText == singleRecord[6]):
        if(employeeCBText == singleRecord[5]):
          self.artStatus = self.window.formLayout_3.itemAt(i).widget().isChecked()
        if(employeeCBText == singleRecord[6]):
          self.editStatus = self.window.formLayout_3.itemAt(i).widget().isChecked()
        for j in range(self.window.formLayout_4.count()):
          statusCBText = self.window.formLayout_4.itemAt(j).widget().text()
          if(statusCBText == singleRecord[4]):
            self.statStatus = self.window.formLayout_4.itemAt(j).widget().isChecked()
    return (self.artStatus or self.editStatus) and self.statStatus

  '''
  weekFromADay takes a single date that was selected from the 
  calendar widget, it then returns a list for the week that
  the seleceted date falls in
  '''

  def weekFromADay(self,selectedDate):
    #QDate day of week monday = 1
    selectedDateDayOfWeek = selectedDate.dayOfWeek()
    selectedDate = selectedDate.toPyDate()
    weekSelectedDateIsIn = []
    tempDate = selectedDate - datetime.timedelta(days = selectedDateDayOfWeek)
    weekSelectedDateIsIn.append(tempDate)
    count = 0
    while(count < 6):
      tempDate += datetime.timedelta(days = 1)
      weekSelectedDateIsIn.append(tempDate)
      count += 1
    return (weekSelectedDateIsIn)

  '''
  recordsForARange takes in a week of dates and all the
  records, it returns a list of all the records that fall
  into that week 
  '''

  def recordsForARange(self,rangeOfDates,allRecords):
    relaventRecords = []
    for date in rangeOfDates:
      for record in allRecords:
        if(date <= record[1] and date >= record[0]):
          if record not in relaventRecords:
            relaventRecords.append(record)
    return relaventRecords

  '''
  daily takes care of actually populating the listwidget
  for the daily view in the MainWindow
  '''

  #calclicked3, selectedDate is a PyDate
  def daily(self,selectedDate,allRecords):
    for record in allRecords:
      if(self.is_Selected(record)):
        
        startDate = record[0]
        endDate = record[1]
        
        if (selectedDate <= endDate and selectedDate >= startDate ):
          deltaStartEndDate = endDate - startDate
          deltaDate = endDate - selectedDate
          for employee in self.window.employees:
            if(employee[0] == record[5]):
              color = employee[1]
              color = re.sub('[()]','',color)
              color = color.split(',')
          if( (deltaStartEndDate.total_seconds()) > 0):
            alphaValue = deltaDate.total_seconds() / deltaStartEndDate.total_seconds()
            alphaValue = 255 - (alphaValue*255)
          else:
            alphaValue = 255;
          jobDescription = re.sub('[\n]','',record[2])
          putMeInList = QtGui.QListWidgetItem(self.window.listWidget_7)
          putMeInList.setText(jobDescription+", "+"FM# "+record[3]+", "+record[4]+", Artist: "+record[5]+", Editor: "+record[6])
          putMeInList.setBackgroundColor(QtGui.QColor(int(color[1]),int(color[2]),int(color[3]),alphaValue))
          self.window.listWidget_7.addItem(putMeInList)

  '''
  weekly takes care of actually populating the listwidgets
  for the weekly view in the MainWindow
  '''

  def weekly(self,selectedDate,allRecords):
    rangeForSelectedDate = self.weekFromADay(selectedDate)
    weekRecords = self.recordsForARange(rangeForSelectedDate,allRecords)
    for date in rangeForSelectedDate:
        for record in weekRecords:
          if(self.is_Selected(record)):
            if(self.artStatus or self.editStatus):
              for employee in self.window.employees:
                if(employee[0] == record[5]):
                  color = employee[1]
                  color = re.sub('[()]','',color)
                  color = color.split(',')
            startDate = record[0]
            endDate = record[1]
            dayOfWeek = date.weekday()
            deltaStartEndDate = endDate - startDate
            deltaDate = endDate - date
            if (deltaStartEndDate.total_seconds() > 0):
              alphaValue = deltaDate.total_seconds() / deltaStartEndDate.total_seconds()
              alphaValue = 255 - (alphaValue * 255)
            else:
              alphaValue = 255
            jobDescription = re.sub('[\n]','',record[2])
            if(dayOfWeek == 0):#listWidget_5 monday
              putMeInList = QtGui.QListWidgetItem(self.window.listWidget_5)
              if (date <= endDate and date >= startDate ):
                putMeInList.setText("Days left: "+str(deltaDate.total_seconds()/86400)+"\n"+jobDescription+"\n"+"FM# "+record[3]+"\n"+record[4]+"\n"+record[5])
                putMeInList.setBackgroundColor(QtGui.QColor(int(color[1]),int(color[2]),int(color[3]),alphaValue))
              else:
                putMeInList.setText("\n\n\n\n")
                putMeInList.setBackgroundColor(QtGui.QColor(255,255,255,255))
              self.window.listWidget_5.addItem(putMeInList)
            elif(dayOfWeek == 1):#listWidget_6 tuesday
              putMeInList = QtGui.QListWidgetItem(self.window.listWidget_6)
              if (date <= endDate and date >= startDate ):
                putMeInList.setText("Days left: "+str(deltaDate.total_seconds()/86400)+"\n"+jobDescription+"\n"+"FM# "+record[3]+"\n"+record[4]+"\n"+record[5])
                putMeInList.setBackgroundColor(QtGui.QColor(int(color[1]),int(color[2]),int(color[3]),alphaValue))
              else:
                putMeInList.setText("\n\n\n\n")
                putMeInList.setBackgroundColor(QtGui.QColor(255,255,255,255))
              self.window.listWidget_6.addItem(putMeInList)
            elif(dayOfWeek == 2):#listWidget_4 wednesday
              putMeInList = QtGui.QListWidgetItem(self.window.listWidget_4)
              if (date <= endDate and date >= startDate ):
                putMeInList.setText("Days left: "+str(deltaDate.total_seconds()/86400)+"\n"+jobDescription+"\n"+"FM# "+record[3]+"\n"+record[4]+"\n"+record[5])
                putMeInList.setBackgroundColor(QtGui.QColor(int(color[1]),int(color[2]),int(color[3]),alphaValue))
              else:
                putMeInList.setText("\n\n\n\n")
                putMeInList.setBackgroundColor(QtGui.QColor(255,255,255,255))
              self.window.listWidget_4.addItem(putMeInList)
            elif(dayOfWeek == 3):#listWidget_3 thursday
              putMeInList = QtGui.QListWidgetItem(self.window.listWidget_3)
              if (date <= endDate and date >= startDate ):
                putMeInList.setText("Days left: "+str(deltaDate.total_seconds()/86400)+"\n"+jobDescription+"\n"+"FM# "+record[3]+"\n"+record[4]+"\n"+record[5])
                putMeInList.setBackgroundColor(QtGui.QColor(int(color[1]),int(color[2]),int(color[3]),alphaValue))
              else:
                putMeInList.setText("\n\n\n\n")
                putMeInList.setBackgroundColor(QtGui.QColor(255,255,255,255))
              self.window.listWidget_3.addItem(putMeInList)
            elif(dayOfWeek == 4):#listWidget friday
              putMeInList = QtGui.QListWidgetItem(self.window.listWidget)
              if (date <= endDate and date >= startDate ):
                putMeInList.setText("Days left: "+str(deltaDate.total_seconds()/86400)+"\n"+jobDescription+"\n"+"FM# "+record[3]+"\n"+record[4]+"\n"+record[5])
                putMeInList.setBackgroundColor(QtGui.QColor(int(color[1]),int(color[2]),int(color[3]),alphaValue))
              else:
                putMeInList.setText("\n\n\n\n")
                putMeInList.setBackgroundColor(QtGui.QColor(255,255,255,255))
              self.window.listWidget.addItem(putMeInList)
            elif(dayOfWeek == 5):#listWidget_8 saturday
              putMeInList = QtGui.QListWidgetItem(self.window.listWidget_8)
              if (date <= endDate and date >= startDate ):
                putMeInList.setText("Days left: "+str(deltaDate.total_seconds()/86400)+"\n"+jobDescription+"\n"+"FM# "+record[3]+"\n"+record[4]+"\n"+record[5])
                putMeInList.setBackgroundColor(QtGui.QColor(int(color[1]),int(color[2]),int(color[3]),alphaValue))
              else:
                putMeInList.setText("\n\n\n\n")
                putMeInList.setBackgroundColor(QtGui.QColor(255,255,255,255))
              self.window.listWidget_8.addItem(putMeInList)
            elif(dayOfWeek == 6):#listWidget_2 sunday
              putMeInList = QtGui.QListWidgetItem(self.window.listWidget_2)
              if (date <= endDate and date >= startDate ):
                putMeInList.setText("Days left: "+str(deltaDate.total_seconds()/86400)+"\n"+jobDescription+"\n"+"FM# "+record[3]+"\n"+record[4]+"\n"+record[5])
                putMeInList.setBackgroundColor(QtGui.QColor(int(color[1]),int(color[2]),int(color[3]),alphaValue))
              else:
                putMeInList.setText("\n\n\n\n")
                putMeInList.setBackgroundColor(QtGui.QColor(255,255,255,255))
              self.window.listWidget_2.addItem(putMeInList)

  '''
  biweekly takes care of actually populating the listwidgets
  for the biweekly view in the MainWindow 

  these are the liswidgets(LW) that correspond to the days
  in the biweekly view

  week1:
  sun = LW_9
  mon = LW_10
  tue = LW_11
  wed = LW_12
  thur = LW_13
  fri = LW_14
  sat = LW_15

  week 2:
  sun = LW_16
  mon = LW_17
  tue = LW_18
  wed = LW_19
  thur = LW_20
  fri = LW_21
  sat = LW_22
  '''

  def biweekly(self,selectedDate,allRecords):
    week1 = self.weekFromADay(selectedDate)
    week1Records = self.recordsForARange(week1,allRecords)
    newDate = selectedDate.addDays(7)
    week2 = self.weekFromADay(newDate)
    week2Records = self.recordsForARange(week2,allRecords)
    for date in week1:
        for record in week1Records:
          if(self.is_Selected(record)):
            if(self.artStatus or self.editStatus):
              for employee in self.window.employees:
                if(employee[0] == record[5]):
                  color = employee[1]
                  color = re.sub('[()]','',color)
                  color = color.split(',')
            startDate = record[0]
            endDate = record[1]
            dayOfWeek = date.weekday()
            deltaStartEndDate = endDate - startDate
            deltaDate = endDate - date
            jobDescription = re.sub('[\n]','',record[2])
            if (deltaStartEndDate.total_seconds() > 0):
              alphaValue = deltaDate.total_seconds() / deltaStartEndDate.total_seconds()
              alphaValue = 255 - (alphaValue * 255)
            else:
              alphaValue = 255
            if(dayOfWeek == 0):#week1 listWidget_10 monday
              putMeInList = QtGui.QListWidgetItem(self.window.listWidget_10)
              if (date <= endDate and date >= startDate ):
                putMeInList.setText("Days left: "+str(deltaDate.total_seconds()/86400)+"\n"+jobDescription+"\n"+"FM# "+record[3]+"\n"+record[4]+"\n"+record[5])
                putMeInList.setBackgroundColor(QtGui.QColor(int(color[1]),int(color[2]),int(color[3]),alphaValue))
              else:
                putMeInList.setText("\n\n\n\n")
                putMeInList.setBackgroundColor(QtGui.QColor(255,255,255,255))
              self.window.listWidget_10.addItem(putMeInList)
            elif(dayOfWeek == 1):#week1 listWidget_11 tuesday
              putMeInList = QtGui.QListWidgetItem(self.window.listWidget_11)
              if (date <= endDate and date >= startDate ):
                putMeInList.setText("Days left: "+str(deltaDate.total_seconds()/86400)+"\n"+jobDescription+"\n"+"FM# "+record[3]+"\n"+record[4]+"\n"+record[5])
                putMeInList.setBackgroundColor(QtGui.QColor(int(color[1]),int(color[2]),int(color[3]),alphaValue))
              else:
                putMeInList.setText("\n\n\n\n")
                putMeInList.setBackgroundColor(QtGui.QColor(255,255,255,255))
              self.window.listWidget_11.addItem(putMeInList)
            elif(dayOfWeek == 2):#week1 listWidget_12 wednesday
              putMeInList = QtGui.QListWidgetItem(self.window.listWidget_12)
              if (date <= endDate and date >= startDate ):
                putMeInList.setText("Days left: "+str(deltaDate.total_seconds()/86400)+"\n"+jobDescription+"\n"+"FM# "+record[3]+"\n"+record[4]+"\n"+record[5])
                putMeInList.setBackgroundColor(QtGui.QColor(int(color[1]),int(color[2]),int(color[3]),alphaValue))
              else:
                putMeInList.setText("\n\n\n\n")
                putMeInList.setBackgroundColor(QtGui.QColor(255,255,255,255))
              self.window.listWidget_12.addItem(putMeInList)
            elif(dayOfWeek == 3):#week1 listWidget_13 thursday
              putMeInList = QtGui.QListWidgetItem(self.window.listWidget_13)
              if (date <= endDate and date >= startDate ):
                putMeInList.setText("Days left: "+str(deltaDate.total_seconds()/86400)+"\n"+jobDescription+"\n"+"FM# "+record[3]+"\n"+record[4]+"\n"+record[5])
                putMeInList.setBackgroundColor(QtGui.QColor(int(color[1]),int(color[2]),int(color[3]),alphaValue))
              else:
                putMeInList.setText("\n\n\n\n")
                putMeInList.setBackgroundColor(QtGui.QColor(255,255,255,255))
              self.window.listWidget_13.addItem(putMeInList)
            elif(dayOfWeek == 4):#week1 listWidget_14 friday
              putMeInList = QtGui.QListWidgetItem(self.window.listWidget_14)
              if (date <= endDate and date >= startDate ):
                putMeInList.setText("Days left: "+str(deltaDate.total_seconds()/86400)+"\n"+jobDescription+"\n"+"FM# "+record[3]+"\n"+record[4]+"\n"+record[5])
                putMeInList.setBackgroundColor(QtGui.QColor(int(color[1]),int(color[2]),int(color[3]),alphaValue))
              else:
                putMeInList.setText("\n\n\n\n")
                putMeInList.setBackgroundColor(QtGui.QColor(255,255,255,255))
              self.window.listWidget_14.addItem(putMeInList)
            elif(dayOfWeek == 5):#week1 listWidget_15 saturday
              putMeInList = QtGui.QListWidgetItem(self.window.listWidget_15)
              if (date <= endDate and date >= startDate ):
                putMeInList.setText("Days left: "+str(deltaDate.total_seconds()/86400)+"\n"+jobDescription+"\n"+"FM# "+record[3]+"\n"+record[4]+"\n"+record[5])
                putMeInList.setBackgroundColor(QtGui.QColor(int(color[1]),int(color[2]),int(color[3]),alphaValue))
              else:
                putMeInList.setText("\n\n\n\n")
                putMeInList.setBackgroundColor(QtGui.QColor(255,255,255,255))
              self.window.listWidget_15.addItem(putMeInList)
            elif(dayOfWeek == 6):#week1 listWidget_9 sunday
              putMeInList = QtGui.QListWidgetItem(self.window.listWidget_9)
              if (date <= endDate and date >= startDate ):
                putMeInList.setText("Days left: "+str(deltaDate.total_seconds()/86400)+"\n"+jobDescription+"\n"+"FM# "+record[3]+"\n"+record[4]+"\n"+record[5])
                putMeInList.setBackgroundColor(QtGui.QColor(int(color[1]),int(color[2]),int(color[3]),alphaValue))
              else:
                putMeInList.setText("\n\n\n\n")
                putMeInList.setBackgroundColor(QtGui.QColor(255,255,255,255))
              self.window.listWidget_9.addItem(putMeInList)
    for date in week2:
        for record in week2Records:
          if(self.is_Selected(record)):
            if(self.artStatus or self.editStatus):
              for employee in self.window.employees:
                if(employee[0] == record[5]):
                  color = employee[1]
                  color = re.sub('[()]','',color)
                  color = color.split(',')
            startDate = record[0]
            endDate = record[1]
            dayOfWeek = date.weekday()
            deltaStartEndDate = endDate - startDate
            deltaDate = endDate - date
            if (deltaStartEndDate.total_seconds() > 0):
              alphaValue = deltaDate.total_seconds() / deltaStartEndDate.total_seconds()
              alphaValue = 255 - (alphaValue * 255)
            else:
              alphaValue = 255
            jobDescription = re.sub('[\n]','',record[2])
            if(dayOfWeek == 0):#week2 listWidget_17 monday
              putMeInList = QtGui.QListWidgetItem(self.window.listWidget_17)
              if (date <= endDate and date >= startDate ):
                putMeInList.setText("Days left: "+str(deltaDate.total_seconds()/86400)+"\n"+jobDescription+"\n"+"FM# "+record[3]+"\n"+record[4]+"\n"+record[5])
                putMeInList.setBackgroundColor(QtGui.QColor(int(color[1]),int(color[2]),int(color[3]),alphaValue))
              else:
                putMeInList.setText("\n\n\n\n")
                putMeInList.setBackgroundColor(QtGui.QColor(255,255,255,255))
              self.window.listWidget_17.addItem(putMeInList)
            elif(dayOfWeek == 1):#week2 listWidget_18 tuesday
              putMeInList = QtGui.QListWidgetItem(self.window.listWidget_18)
              if (date <= endDate and date >= startDate ):
                putMeInList.setText("Days left: "+str(deltaDate.total_seconds()/86400)+"\n"+jobDescription+"\n"+"FM# "+record[3]+"\n"+record[4]+"\n"+record[5])
                putMeInList.setBackgroundColor(QtGui.QColor(int(color[1]),int(color[2]),int(color[3]),alphaValue))
              else:
                putMeInList.setText("\n\n\n\n")
                putMeInList.setBackgroundColor(QtGui.QColor(255,255,255,255))
              self.window.listWidget_18.addItem(putMeInList)
            elif(dayOfWeek == 2):#week2 listWidget_19 wednesday
              putMeInList = QtGui.QListWidgetItem(self.window.listWidget_19)
              if (date <= endDate and date >= startDate ):
                putMeInList.setText("Days left: "+str(deltaDate.total_seconds()/86400)+"\n"+jobDescription+"\n"+"FM# "+record[3]+"\n"+record[4]+"\n"+record[5])
                putMeInList.setBackgroundColor(QtGui.QColor(int(color[1]),int(color[2]),int(color[3]),alphaValue))
              else:
                putMeInList.setText("\n\n\n\n")
                putMeInList.setBackgroundColor(QtGui.QColor(255,255,255,255))
              self.window.listWidget_19.addItem(putMeInList)
            elif(dayOfWeek == 3):#week2 listWidget_20 thursday
              putMeInList = QtGui.QListWidgetItem(self.window.listWidget_20)
              if (date <= endDate and date >= startDate ):
                putMeInList.setText("Days left: "+str(deltaDate.total_seconds()/86400)+"\n"+jobDescription+"\n"+"FM# "+record[3]+"\n"+record[4]+"\n"+record[5])
                putMeInList.setBackgroundColor(QtGui.QColor(int(color[1]),int(color[2]),int(color[3]),alphaValue))
              else:
                putMeInList.setText("\n\n\n\n")
                putMeInList.setBackgroundColor(QtGui.QColor(255,255,255,255))
              self.window.listWidget_20.addItem(putMeInList)
            elif(dayOfWeek == 4):#week2 listWidget_21 friday
              putMeInList = QtGui.QListWidgetItem(self.window.listWidget_21)
              if (date <= endDate and date >= startDate ):
                putMeInList.setText("Days left: "+str(deltaDate.total_seconds()/86400)+"\n"+jobDescription+"\n"+"FM# "+record[3]+"\n"+record[4]+"\n"+record[5])
                putMeInList.setBackgroundColor(QtGui.QColor(int(color[1]),int(color[2]),int(color[3]),alphaValue))
              else:
                putMeInList.setText("\n\n\n\n")
                putMeInList.setBackgroundColor(QtGui.QColor(255,255,255,255))
              self.window.listWidget_21.addItem(putMeInList)
            elif(dayOfWeek == 5):#week2 listWidget_22 saturday
              putMeInList = QtGui.QListWidgetItem(self.window.listWidget_22)
              if (date <= endDate and date >= startDate ):
                putMeInList.setText("Days left: "+str(deltaDate.total_seconds()/86400)+"\n"+jobDescription+"\n"+"FM# "+record[3]+"\n"+record[4]+"\n"+record[5])
                putMeInList.setBackgroundColor(QtGui.QColor(int(color[1]),int(color[2]),int(color[3]),alphaValue))
              else:
                putMeInList.setText("\n\n\n\n")
                putMeInList.setBackgroundColor(QtGui.QColor(255,255,255,255))
              self.window.listWidget_22.addItem(putMeInList)
            elif(dayOfWeek == 6):#week2 listWidget_16 sunday
              putMeInList = QtGui.QListWidgetItem(self.window.listWidget_16)
              if (date <= endDate and date >= startDate ):
                putMeInList.setText("Days left: "+str(deltaDate.total_seconds()/86400)+"\n"+jobDescription+"\n"+"FM# "+record[3]+"\n"+record[4]+"\n"+record[5])
                putMeInList.setBackgroundColor(QtGui.QColor(int(color[1]),int(color[2]),int(color[3]),alphaValue))
              else:
                putMeInList.setText("\n\n\n\n")
                putMeInList.setBackgroundColor(QtGui.QColor(255,255,255,255))
              self.window.listWidget_16.addItem(putMeInList)
