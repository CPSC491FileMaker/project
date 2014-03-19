from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import QDateTime
import datetime, re
from datetime import time

class HandleLists:

  def __init__(self,MainWindow):
    self.window = MainWindow
    self.artStatus = False
    self.editStatus = False
    self.statStatus = False


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


  def checkEmp(self,employeeNames):
    for employee in employeeNames:
      for i in range(self.window.formLayout_3.count()):
        if (self.window.formLayout_3.itemAt(i).widget().text() == employee):
          self.empStatus = self.window.formLayout_3.itemAt(i).widget().isChecked()
          return
        else:
          self.empStatus = False

  def checkStat(self,status):
      for i in range(self.window.formLayout_4.count()):
        if(self.window.formLayout_4.itemAt(i).widget().text() == status):
          self.statStatus = self.window.formLayout_4.itemAt(i).widget().isChecked()
        else:
          self.statStatus = False

  #calclicked3, selectedDate is a PyDate
  def daily(self,selectedDate,allRecords):
    for record in allRecords:
      if(self.is_Selected(record)):
      #self.checkEmp([record[5],record[6]])
        if(self.artStatus or self.editStatus):
          for employee in self.window.employees:
            if(employee[0] == record[5]):
              color = employee[1]
              color = re.sub('[()]','',color)
              color = color.split(',')
        startDate = record[0]
        endDate = record[1]
        deltaStartEndDate = endDate - startDate
        deltaDate = endDate - selectedDate
        if( deltaStartEndDate.total_seconds() > 0):
          alphaValue = deltaDate.total_seconds() / deltaStartEndDate.total_seconds()
          alphaValue = 255 - (alphaValue*255)
        else:
          alphaValue = 255;
            
        if (selectedDate <= endDate and selectedDate >= startDate ):
          putMeInList = QtGui.QListWidgetItem(self.window.listWidget_7)
          putMeInList.setText(record[2]+", "+record[3]+", "+record[4]+", Artist: "+record[5]+", Editor: "+record[6])
          putMeInList.setBackgroundColor(QtGui.QColor(int(color[1]),int(color[2]),int(color[3]),alphaValue))
          self.window.listWidget_7.addItem(putMeInList)

  def weekly(self,selectedDate,allRecords):
    selectedDateDayOfWeek = selectedDate.dayOfWeek()
    selectedDate = selectedDate.toPyDate()
    rangeForSelectedDate = []
    if(selectedDateDayOfWeek == 1):#monday
      tempDate = selectedDate
      tempDate -= datetime.timedelta(days=1)
      rangeForSelectedDate.append(tempDate)
      tempDate += datetime.timedelta(days=1)
      rangeForSelectedDate.append(tempDate)
      tempDate += datetime.timedelta(days=1)
      rangeForSelectedDate.append(tempDate)
      tempDate += datetime.timedelta(days=1)
      rangeForSelectedDate.append(tempDate)
      tempDate += datetime.timedelta(days=1)
      rangeForSelectedDate.append(tempDate)
      tempDate += datetime.timedelta(days=1)
      rangeForSelectedDate.append(tempDate)
      tempDate += datetime.timedelta(days=1)
      rangeForSelectedDate.append(tempDate)
    elif(selectedDateDayOfWeek == 2):#tuesday
      tempDate = selectedDate
      tempDate -= datetime.timedelta(days=2)
      rangeForSelectedDate.append(tempDate)
      tempDate += datetime.timedelta(days=1)
      rangeForSelectedDate.append(tempDate)
      tempDate += datetime.timedelta(days=1)
      rangeForSelectedDate.append(tempDate)
      tempDate += datetime.timedelta(days=1)
      rangeForSelectedDate.append(tempDate)
      tempDate += datetime.timedelta(days=1)
      rangeForSelectedDate.append(tempDate)
      tempDate += datetime.timedelta(days=1)
      rangeForSelectedDate.append(tempDate)
      tempDate += datetime.timedelta(days=1)
      rangeForSelectedDate.append(tempDate)
    elif(selectedDateDayOfWeek == 3):#wednesday
      tempDate = selectedDate
      tempDate -= datetime.timedelta(days=3)
      rangeForSelectedDate.append(tempDate)
      tempDate += datetime.timedelta(days=1)
      rangeForSelectedDate.append(tempDate)
      tempDate += datetime.timedelta(days=1)
      rangeForSelectedDate.append(tempDate)
      tempDate += datetime.timedelta(days=1)
      rangeForSelectedDate.append(tempDate)
      tempDate += datetime.timedelta(days=1)
      rangeForSelectedDate.append(tempDate)
      tempDate += datetime.timedelta(days=1)
      rangeForSelectedDate.append(tempDate)
      tempDate += datetime.timedelta(days=1)
      rangeForSelectedDate.append(tempDate)
    elif(selectedDateDayOfWeek == 4):#thursday
      tempDate = selectedDate
      tempDate -= datetime.timedelta(days=4)
      rangeForSelectedDate.append(tempDate)
      tempDate += datetime.timedelta(days=1)
      rangeForSelectedDate.append(tempDate)
      tempDate += datetime.timedelta(days=1)
      rangeForSelectedDate.append(tempDate)
      tempDate += datetime.timedelta(days=1)
      rangeForSelectedDate.append(tempDate)
      tempDate += datetime.timedelta(days=1)
      rangeForSelectedDate.append(tempDate)
      tempDate += datetime.timedelta(days=1)
      rangeForSelectedDate.append(tempDate)
      tempDate += datetime.timedelta(days=1)
      rangeForSelectedDate.append(tempDate)
    elif(selectedDateDayOfWeek == 5):#friday
      tempDate = selectedDate
      tempDate -= datetime.timedelta(days=5)
      rangeForSelectedDate.append(tempDate)
      tempDate += datetime.timedelta(days=1)
      rangeForSelectedDate.append(tempDate)
      tempDate += datetime.timedelta(days=1)
      rangeForSelectedDate.append(tempDate)
      tempDate += datetime.timedelta(days=1)
      rangeForSelectedDate.append(tempDate)
      tempDate += datetime.timedelta(days=1)
      rangeForSelectedDate.append(tempDate)
      tempDate += datetime.timedelta(days=1)
      rangeForSelectedDate.append(tempDate)
      tempDate += datetime.timedelta(days=1)
      rangeForSelectedDate.append(tempDate)
    elif(selectedDateDayOfWeek == 6):#saturday
      tempDate = selectedDate
      tempDate -= datetime.timedelta(days=6)
      rangeForSelectedDate.append(tempDate)
      tempDate += datetime.timedelta(days=1)
      rangeForSelectedDate.append(tempDate)
      tempDate += datetime.timedelta(days=1)
      rangeForSelectedDate.append(tempDate)
      tempDate += datetime.timedelta(days=1)
      rangeForSelectedDate.append(tempDate)
      tempDate += datetime.timedelta(days=1)
      rangeForSelectedDate.append(tempDate)
      tempDate += datetime.timedelta(days=1)
      rangeForSelectedDate.append(tempDate)
      tempDate += datetime.timedelta(days=1)
      rangeForSelectedDate.append(tempDate)
    elif(selectedDateDayOfWeek == 7):#sunday
      tempDate = selectedDate
      tempDate -= datetime.timedelta(days=7)
      rangeForSelectedDate.append(tempDate)
      tempDate += datetime.timedelta(days=1)
      rangeForSelectedDate.append(tempDate)
      tempDate += datetime.timedelta(days=1)
      rangeForSelectedDate.append(tempDate)
      tempDate += datetime.timedelta(days=1)
      rangeForSelectedDate.append(tempDate)
      tempDate += datetime.timedelta(days=1)
      rangeForSelectedDate.append(tempDate)
      tempDate += datetime.timedelta(days=1)
      rangeForSelectedDate.append(tempDate)
      tempDate += datetime.timedelta(days=1)
      rangeForSelectedDate.append(tempDate)
    for date in rangeForSelectedDate:
        dow = date.weekday()
        for record in allRecords:
          self.is_Selected(record)
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
            if(dayOfWeek == 0):#listWidget_5 monday
              if (date <= endDate and date >= startDate ):
                putMeInList = QtGui.QListWidgetItem(self.window.listWidget_5)
                putMeInList.setText(record[0].isoformat()+"\n"+record[1].isoformat()+"\n"+record[2]+"\n"+record[3]+"\n"+record[4]+"\n"+record[5])
                putMeInList.setBackgroundColor(QtGui.QColor(int(color[1]),int(color[2]),int(color[3]),alphaValue))
                self.window.listWidget_5.addItem(putMeInList)
            elif(dayOfWeek == 1):#listWidget_6 tuesday
              if (date <= endDate and date >= startDate ):
                putMeInList = QtGui.QListWidgetItem(self.window.listWidget_6)
                putMeInList.setText(record[0].isoformat()+"\n"+record[1].isoformat()+"\n"+record[2]+"\n"+record[3]+"\n"+record[4]+"\n"+record[5])
                putMeInList.setBackgroundColor(QtGui.QColor(int(color[1]),int(color[2]),int(color[3]),alphaValue))
                self.window.listWidget_6.addItem(putMeInList)
            elif(dayOfWeek == 2):#listWidget_4 wednesday
              if (date <= endDate and date >= startDate ):
                putMeInList = QtGui.QListWidgetItem(self.window.listWidget_4)
                putMeInList.setText(record[0].isoformat()+"\n"+record[1].isoformat()+"\n"+record[2]+"\n"+record[3]+"\n"+record[4]+"\n"+record[5])
                putMeInList.setBackgroundColor(QtGui.QColor(int(color[1]),int(color[2]),int(color[3]),alphaValue))
                self.window.listWidget_4.addItem(putMeInList)
            elif(dayOfWeek == 3):#listWidget_3 thursday
              if (date <= endDate and date >= startDate ):
                putMeInList = QtGui.QListWidgetItem(self.window.listWidget_3)
                putMeInList.setText(record[0].isoformat()+"\n"+record[1].isoformat()+"\n"+record[2]+"\n"+record[3]+"\n"+record[4]+"\n"+record[5])
                putMeInList.setBackgroundColor(QtGui.QColor(int(color[1]),int(color[2]),int(color[3]),alphaValue))
                self.window.listWidget_3.addItem(putMeInList)
            elif(dayOfWeek == 4):#listWidget friday
              if (date <= endDate and date >= startDate ):
                putMeInList = QtGui.QListWidgetItem(self.window.listWidget)
                putMeInList.setText(record[0].isoformat()+"\n"+record[1].isoformat()+"\n"+record[2]+"\n"+record[3]+"\n"+record[4]+"\n"+record[5])
                putMeInList.setBackgroundColor(QtGui.QColor(int(color[1]),int(color[2]),int(color[3]),alphaValue))
                self.window.listWidget.addItem(putMeInList)
            elif(dayOfWeek == 5):#listWidget_8 saturday
              if (date <= endDate and date >= startDate ):
                putMeInList = QtGui.QListWidgetItem(self.window.listWidget_8)
                putMeInList.setText(record[0].isoformat()+"\n"+record[1].isoformat()+"\n"+record[2]+"\n"+record[3]+"\n"+record[4]+"\n"+record[5])
                putMeInList.setBackgroundColor(QtGui.QColor(int(color[1]),int(color[2]),int(color[3]),alphaValue))
                self.window.listWidget_8.addItem(putMeInList)
            elif(dayOfWeek == 6):#listWidget_2 sunday
              if (date <= endDate and date >= startDate ):
                putMeInList = QtGui.QListWidgetItem(self.window.listWidget_2)
                putMeInList.setText(record[0].isoformat()+"\n"+record[1].isoformat()+"\n"+record[2]+"\n"+record[3]+"\n"+record[4]+"\n"+record[5])
                putMeInList.setBackgroundColor(QtGui.QColor(int(color[1]),int(color[2]),int(color[3]),alphaValue))
                self.window.listWidget_2.addItem(putMeInList)
