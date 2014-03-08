# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Calendar_v03_SLOTSINC.ui'
#
# Created: Sat Mar  1 15:57:42 2014
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import QDateTime
import atexit,os,helper, xmlparse, addEmployee, addStatus, removeEmployee, removeStatus, re
from datetime import date
import datetime

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):

    employees = []
    statuses = []
    #empCheckBoxes = []
    #statCheckBoxes = []    
    empStatus = False
    statStatus = False

    def goodbye(self):
      currentdir = os.path.dirname(os.path.realpath(__file__))
      files = os.listdir(currentdir)
      for file in files:
          if file.endswith(".pyc"):
              os.remove(os.path.join(currentdir,file))
          if file.endswith("~"):
              os.remove(os.path.join(currentdir,file))
          if file.endswith(".swp"):
              os.remove(os.path.join(currentdir,file))

    def addStatClicked(self):
      addStatWindow = QtGui.QDialog()
      addStat = addStatus.Ui_Dialog(self)
      addStat.setupUi(addStatWindow)
      addStatWindow.exec_()
    
    def addEmpClicked(self):
      addEmpWindow = QtGui.QDialog()
      addEmp = addEmployee.Ui_Dialog(self)
      addEmp.setupUi(addEmpWindow)
      addEmpWindow.exec_()
    
    def contactClicked(self):
        print "stub"

    def remEmpClicked(self):
      remEmpWindow = QtGui.QDialog()
      remEmp = removeEmployee.Ui_Dialog(self)
      remEmp.setupUi(remEmpWindow)
      remEmpWindow.exec_()

    def remStatClicked(self):
      remStatWindow = QtGui.QDialog()
      remStat = removeStatus.Ui_Dialog(self)
      remStat.setupUi(remStatWindow)
      remStatWindow.exec_()   

 
    def updateRecordsClicked(self):
      records = xml.fetchRecords()   
   
    def populateCheckboxes(self):
      #self.empCheckBoxes = []
      #self.statCheckBoxes = []
      ind =2
      #self.formLayout_6.addWidget(self.pushButton_2)
      for person in self.employees:
        ind += 1
        self.checkBox = QtGui.QCheckBox(self.scrollAreaWidgetContents_2)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.formLayout_6.addWidget(self.checkBox)     
        #self.empCheckBoxes.append(self.checkBox)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.formLayout.setWidget(0,QtGui.QFormLayout.LabelRole,self.scrollArea_2)
        self.checkBox.setText(QtGui.QApplication.translate("MainWindow", person[0], None, QtGui.QApplication.UnicodeUTF8))
      ind =2 
      #self.formLayout_7.addWidget(self.pushButton_3)
      for status in self.statuses:
        ind += 1
        self.checkBox_3 = QtGui.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_3.setObjectName(_fromUtf8("checkBox3"))
        self.formLayout_7.addWidget(self.checkBox_3)
        #self.statCheckBoxes.append(self.checkBox_3)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.formLayout_3.setWidget(0,QtGui.QFormLayout.LabelRole,self.scrollArea)
        self.checkBox_3.setText(QtGui.QApplication.translate("MainWindow", status, None, QtGui.QApplication.UnicodeUTF8))
        
      #print "empCheckBoxes "+str(self.empCheckBoxes)
      #for cb in self.empCheckBoxes:
        #print cb.isChecked()

      #print "statCheckBoxes "+str(self.statCheckBoxes)
      #for cb in self.statCheckBoxes:
        #print cb.text()

    def refreshCheckboxes(self):
        for i in reversed(range(self.formLayout_6.count())):
            item = self.formLayout_6.itemAt(i)
            if isinstance(item, QtGui.QWidgetItem):
                item.widget().close()
            self.formLayout_6.removeItem(item)

        for i in reversed(range(self.formLayout_7.count())): 
            item = self.formLayout_7.itemAt(i)
            if isinstance(item, QtGui.QWidgetItem):
                item.widget().close()
            self.formLayout_7.removeItem(item) 
        self.populateCheckboxes()
    
    #formLayout_6 == employee checkBoxes
    def checkEmp(self,employeeName):
      count = 0
      #print "in checkEmp "
      #for checkBox in self.empCheckBoxes:
      for i in range(self.formLayout_6.count()):
        #print "cb.text "+str(i)+' '+self.formLayout_6.itemAt(i).widget().text()
        if (self.formLayout_6.itemAt(i).widget().text() == employeeName):
          self.empStatus = self.formLayout_6.itemAt(i).widget().isChecked()
          #print "empStatus "+str(self.empStatus)
          return
        else:
          self.empStatus = False

    #formLayout_7 == status checkBoxes
    def checkStat(self,status):
      #print "in checkStat "
      #for checkBox in self.statCheckBoxes:
      for i in range(self.formLayout_7.count()):
        #print "cb.text "+self.formLayout_7.itemAt(i).widget().text()
        if(self.formLayout_7.itemAt(i).widget().text() == status):
          self.statStatus = self.formLayout_7.itemAt(i).widget().isChecked()
          #print "statStatus "+str(statStatus)
        else:
          self.statStatus = False

        #horizontalLayout_4
    #listWidget_2 == Sunday
    #listWidget_5 == Monday
    #listWidget_6 == Tuesday
    #listWidget_4 == Wednesday
    #listWidget_3 == Thursday
    #listWidget == Friday
    #listWidget_8 == Saturday
    #weekly view
    def calclicked2(self):
        print "about to clear lists"

        #for i in range(self.horizontalLayout_4.count()):
         # self.horizontalLayout_4.itemAt(i).widget().addItem('test')
          #for item in allitems:
           # print "i: "+str(i)+' '+item
          # print str(self.horizontalLayout_4.itemAt(i).widget().contains())

        for i in range(self.horizontalLayout_4.count()):
         # allitems = self.horizontalLayout_4.itemAt(i).widget().findItems('',QtCore.Qt.MatchRegExp)
          #for item in allitems:
           # print "i: "+str(i)+' '+item
          # print str(self.horizontalLayout_4.itemAt(i).widget().contains())

          self.horizontalLayout_4.itemAt(i).widget().clear()

        selectedDate = self.calendarWidget_2.selectedDate()
        self.dateEdit_2.setDate(selectedDate)
        self.fill_labels2(selectedDate)
        self.calendarWidget_2.hide()
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
          print "rangeForSelectedDate"
          for date in rangeForSelectedDate:
            print date
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
          print "rangeForSelectedDate"
          for date in rangeForSelectedDate:
            print date
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
          print "rangeForSelectedDate"
          for date in rangeForSelectedDate:
            print date
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
          print "rangeForSelectedDate"
          for date in rangeForSelectedDate:
            print date
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
          print "rangeForSelectedDate"
          for date in rangeForSelectedDate:
            print date
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
          print "rangeForSelectedDate"
          for date in rangeForSelectedDate:
            print date
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
          print "rangeForSelectedDate"
          for date in rangeForSelectedDate:
            print date

        for date in rangeForSelectedDate:
          print "date "+str(date)
          dow = date.weekday()
          print "day of the week"+str(date.weekday())
          for record in records:
            self.checkEmp(record[5])
            if(self.empStatus):
              #print "empStatus is true"
              for employee in self.employees:
                if(employee[0] == record[5]):
                  color = employee[1]
                  color = re.sub('[()]','',color)
                  color = color.split(',')
             #check statStatus
              startDate = record[0]
              endDate = record[1]
              dayOfWeek = date.weekday()
              #selectedDate = selectedDate.toPyDate()
              #print "selectedDate "+str(selectedDate)
              deltaStartEndDate = endDate - startDate
              deltaDate = endDate - date
              if (deltaStartEndDate.total_seconds() > 0):
                alphaValue = deltaDate.total_seconds() / deltaStartEndDate.total_seconds()
              else:
                alphaValue = -2
              if(dayOfWeek == 0):#listWidget_5 monday
                if (date <= endDate and date >= startDate ):
                  #print "startDate: "+ startDate.__repr__()
                  #print "date: "+selectedDate.__repr__()
                  #print "endDate: "+endDate.__repr__()
                  putMeInList = QtGui.QListWidgetItem(self.listWidget_5)
                  #putMeInList.setWordWrap(True)
                  putMeInList.setText(record[0].isoformat()+"\n"+record[1].isoformat()+"\n"+record[2]+"\n"+record[3]+"\n"+record[4]+"\n"+record[5])
                  putMeInList.setBackgroundColor(QtGui.QColor(int(color[0]),int(color[1]),int(color[2]),255-(alphaValue*255)))
                  self.listWidget_5.addItem(putMeInList)
              elif(dayOfWeek == 1):#listWidget_6 tuesday
                if (date <= endDate and date >= startDate ):
                  #print "startDate: "+ startDate.__repr__()
                  #print "date: "+selectedDate.__repr__()
                  #print "endDate: "+endDate.__repr__()
                  putMeInList = QtGui.QListWidgetItem(self.listWidget_6)
                  #putMeInList.setWordWrap(True)
                  putMeInList.setText(record[0].isoformat()+"\n"+record[1].isoformat()+"\n"+record[2]+"\n"+record[3]+"\n"+record[4]+"\n"+record[5])
                  putMeInList.setBackgroundColor(QtGui.QColor(int(color[0]),int(color[1]),int(color[2]),255-(alphaValue*255)))
                  self.listWidget_6.addItem(putMeInList)
              elif(dayOfWeek == 2):#listWidget_4 wednesday
                if (date <= endDate and date >= startDate ):
                  #print "startDate: "+ startDate.__repr__()
                  #print "date: "+selectedDate.__repr__()
                  #print "endDate: "+endDate.__repr__()
                  putMeInList = QtGui.QListWidgetItem(self.listWidget_4)
                  #putMeInList.setWordWrap(True)
                  putMeInList.setText(record[0].isoformat()+"\n"+record[1].isoformat()+"\n"+record[2]+"\n"+record[3]+"\n"+record[4]+"\n"+record[5])
                  putMeInList.setBackgroundColor(QtGui.QColor(int(color[0]),int(color[1]),int(color[2]),255-(alphaValue*255)))
                  self.listWidget_4.addItem(putMeInList)
              elif(dayOfWeek == 3):#listWidget_3 thursday
                if (date <= endDate and date >= startDate ):
                  #print "startDate: "+ startDate.__repr__()
                  #print "date: "+selectedDate.__repr__()
                  #print "endDate: "+endDate.__repr__()
                  putMeInList = QtGui.QListWidgetItem(self.listWidget_3)
                  #putMeInList.setWordWrap(True)
                  putMeInList.setText(record[0].isoformat()+"\n"+record[1].isoformat()+"\n"+record[2]+"\n"+record[3]+"\n"+record[4]+"\n"+record[5])
                  putMeInList.setBackgroundColor(QtGui.QColor(int(color[0]),int(color[1]),int(color[2]),255-(alphaValue*255)))
                  self.listWidget_3.addItem(putMeInList)
              elif(dayOfWeek == 4):#listWidget friday
                if (date <= endDate and date >= startDate ):
                  #print "startDate: "+ startDate.__repr__()
                  #print "date: "+selectedDate.__repr__()
                  #print "endDate: "+endDate.__repr__()
                  putMeInList = QtGui.QListWidgetItem(self.listWidget)
                  #putMeInList.setWordWrap(True)
                  putMeInList.setText(record[0].isoformat()+"\n"+record[1].isoformat()+"\n"+record[2]+"\n"+record[3]+"\n"+record[4]+"\n"+record[5])
                  putMeInList.setBackgroundColor(QtGui.QColor(int(color[0]),int(color[1]),int(color[2]),255-(alphaValue*255)))
                  self.listWidget.addItem(putMeInList)
              elif(dayOfWeek == 5):#listWidget_8 saturday
                if (date <= endDate and date >= startDate ):
                  #print "startDate: "+ startDate.__repr__()
                  #print "date: "+selectedDate.__repr__()
                  #print "endDate: "+endDate.__repr__()
                  putMeInList = QtGui.QListWidgetItem(self.listWidget_8)
                  #putMeInList.setWordWrap(True)                  
                  putMeInList.setText(record[0].isoformat()+"\n"+record[1].isoformat()+"\n"+record[2]+"\n"+record[3]+"\n"+record[4]+"\n"+record[5])
                  putMeInList.setBackgroundColor(QtGui.QColor(int(color[0]),int(color[1]),int(color[2]),255-(alphaValue*255)))
                  self.listWidget_8.addItem(putMeInList)
              elif(dayOfWeek == 6):#listWidget_2 sunday
                if (date <= endDate and date >= startDate ):
                  #print "startDate: "+ startDate.__repr__()
                  #print "date: "+selectedDate.__repr__()
                  #print "endDate: "+endDate.__repr__()
                  putMeInList = QtGui.QListWidgetItem(self.listWidget_2)
                  #putMeInList.setWordWrap(True)
                  putMeInList.setText(record[0].isoformat()+"\n"+record[1].isoformat()+"\n"+record[2]+"\n"+record[3]+"\n"+record[4]+"\n"+record[5])
                  putMeInList.setBackgroundColor(QtGui.QColor(int(color[0]),int(color[1]),int(color[2]),255-(alphaValue*255)))
                  self.listWidget_2.addItem(putMeInList)
            #listWidget_2 == Sunday
    #listWidget_5 == Monday
    #listWidget_6 == Tuesday
    #listWidget_4 == Wednesday
    #listWidget_3 == Thursday
    #listWidget == Friday
    #listWidget_8 == Saturday
   
         
    def calclicked(self):
        self.dateEdit_3.setDate(self.calendarWidget.selectedDate())
        self.fill_labels1((self.calendarWidget.selectedDate()))
        self.calendarWidget.hide()    

    def calclicked3(self):
        self.listWidget_7.clear()
        selectedDate = self.calendarWidget_3.selectedDate() #QDate
        #print "selectedDate from Widget "+str(selectedDate)
        self.dateEdit.setDate(selectedDate) #datebox
        self.calendarWidget_3.hide() #calanderbox
        selectedDateString = selectedDate.toString("Mdyyyy")
        #print "selectedDateString "+selectedDateString
        #print "selectedDate: "+str(selectedDate)
        selectedDate = selectedDate.toPyDate()
        #print "selectedDate: "+str(selectedDate)
        
        for record in records:
          self.checkEmp(record[5])
          if(self.empStatus):
              for employee in self.employees:
                if(employee[0] == record[5]):
                  color = employee[1]
                  color = re.sub('[()]','',color)
                  color = color.split(',')
              #print "MADE IT PAST CHECKEMP"
              #print "color "+str(color)
            #self.checkStat(record[4])
            #if(self.statStatus):
              startDate = record[0]
              #print "startDate "+str(startDate)
              endDate = record[1]
              #print "endDate "+str(endDate)
              #print "selectedDate "+str(selectedDate)
              deltaStartEndDate = endDate - startDate
              #print "deltaStartEndDate "+str(deltaStartEndDate.total_seconds())
              deltaDate = endDate - selectedDate
              #print "deltaDate "+str(deltaDate.total_seconds())
              if( deltaStartEndDate.total_seconds() > 0):
                alphaValue = deltaDate.total_seconds() / deltaStartEndDate.total_seconds()
              else:
                alphaValue = -2;
              #print "alphaValue "+str(alphaValue)
              if (selectedDate <= endDate and selectedDate >= startDate ):
                #print "startDate: "+ startDate.__repr__()
                #print "date: "+selectedDate.__repr__()
                #print "endDate: "+endDate.__repr__()
                putMeInList = QtGui.QListWidgetItem(self.listWidget_7)
                putMeInList.setText(record[2]+", "+record[3]+", "+record[4]+", "+record[5])
                putMeInList.setBackgroundColor(QtGui.QColor(int(color[0]),int(color[1]),int(color[2]),255-(alphaValue*255)))
                self.listWidget_7.addItem(putMeInList)    

    def fill_labels1(self, p_Date):
        day = int(p_Date.dayOfWeek())
        if day == 1:
           sun=p_Date.addDays(-1)
           self.label_8.setText(QtGui.QApplication.translate("MainWindow", sun.toString("dddd MMM dd"), None, QtGui.QApplication.UnicodeUTF8))
           self.label_9.setText(QtGui.QApplication.translate("MainWindow", p_Date.toString("dddd MMM dd"), None, QtGui.QApplication.UnicodeUTF8))
           p_Date = p_Date.addDays(1)
           self.label_10.setText(QtGui.QApplication.translate("MainWindow", p_Date.toString("dddd MMM dd"), None, QtGui.QApplication.UnicodeUTF8))
           p_Date=p_Date.addDays(1)
           self.label_11.setText(QtGui.QApplication.translate("MainWindow", p_Date.toString("dddd MMM dd"), None, QtGui.QApplication.UnicodeUTF8))
           p_Date=p_Date.addDays(1)
           self.label_12.setText(QtGui.QApplication.translate("MainWindow", p_Date.toString("dddd MMM dd"), None, QtGui.QApplication.UnicodeUTF8))
           p_Date=p_Date.addDays(1)
           self.label_13.setText(QtGui.QApplication.translate("MainWindow", p_Date.toString("dddd MMM dd"), None, QtGui.QApplication.UnicodeUTF8))
           p_Date=p_Date.addDays(1)
           self.label_14.setText(QtGui.QApplication.translate("MainWindow", p_Date.toString("dddd MMM dd"), None, QtGui.QApplication.UnicodeUTF8))
           p_Date=p_Date.addDays(1)
           self.label_15.setText(QtGui.QApplication.translate("MainWindow", p_Date.toString("dddd MMM dd"), None, QtGui.QApplication.UnicodeUTF8))
           p_Date=p_Date.addDays(1)
           self.label_16.setText(QtGui.QApplication.translate("MainWindow", p_Date.toString("dddd MMM dd"), None, QtGui.QApplication.UnicodeUTF8))
           p_Date=p_Date.addDays(1)
           self.label_17.setText(QtGui.QApplication.translate("MainWindow", p_Date.toString("dddd MMM dd"), None, QtGui.QApplication.UnicodeUTF8))
           p_Date=p_Date.addDays(1)
           self.label_18.setText(QtGui.QApplication.translate("MainWindow", p_Date.toString("dddd MMM dd"), None, QtGui.QApplication.UnicodeUTF8))
           p_Date=p_Date.addDays(1)
           self.label_19.setText(QtGui.QApplication.translate("MainWindow", p_Date.toString("dddd MMM dd"), None, QtGui.QApplication.UnicodeUTF8))
           p_Date=p_Date.addDays(1)
           self.label_20.setText(QtGui.QApplication.translate("MainWindow", p_Date.toString("dddd MMM dd"), None, QtGui.QApplication.UnicodeUTF8))
           p_Date=p_Date.addDays(1)
           self.label_21.setText(QtGui.QApplication.translate("MainWindow", p_Date.toString("dddd MMM dd"), None, QtGui.QApplication.UnicodeUTF8))
        if day == 2:
           sun=p_Date.addDays(-2)
           mon=p_Date.addDays(-1)
           self.label_8.setText(QtGui.QApplication.translate("MainWindow", sun.toString("dddd MMM dd"), None, QtGui.QApplication.UnicodeUTF8))
           self.label_9.setText(QtGui.QApplication.translate("MainWindow", mon.toString("dddd MMM dd"), None, QtGui.QApplication.UnicodeUTF8))
           self.label_10.setText(QtGui.QApplication.translate("MainWindow", p_Date.toString("dddd MMM dd"), None, QtGui.QApplication.UnicodeUTF8))
           p_Date=p_Date.addDays(1)
           self.label_11.setText(QtGui.QApplication.translate("MainWindow", p_Date.toString("dddd MMM dd"), None, QtGui.QApplication.UnicodeUTF8))
           p_Date=p_Date.addDays(1)
           self.label_12.setText(QtGui.QApplication.translate("MainWindow", p_Date.toString("dddd MMM dd"), None, QtGui.QApplication.UnicodeUTF8))
           p_Date=p_Date.addDays(1)
           self.label_13.setText(QtGui.QApplication.translate("MainWindow", p_Date.toString("dddd MMM dd"), None, QtGui.QApplication.UnicodeUTF8))
           p_Date=p_Date.addDays(1)
           self.label_14.setText(QtGui.QApplication.translate("MainWindow", p_Date.toString("dddd MMM dd"), None, QtGui.QApplication.UnicodeUTF8))
           p_Date=p_Date.addDays(1)
           self.label_15.setText(QtGui.QApplication.translate("MainWindow", p_Date.toString("dddd MMM dd"), None, QtGui.QApplication.UnicodeUTF8))
           p_Date=p_Date.addDays(1)
           self.label_16.setText(QtGui.QApplication.translate("MainWindow", p_Date.toString("dddd MMM dd"), None, QtGui.QApplication.UnicodeUTF8))
           p_Date=p_Date.addDays(1)
           self.label_17.setText(QtGui.QApplication.translate("MainWindow", p_Date.toString("dddd MMM dd"), None, QtGui.QApplication.UnicodeUTF8))
           p_Date=p_Date.addDays(1)
           self.label_18.setText(QtGui.QApplication.translate("MainWindow", p_Date.toString("dddd MMM dd"), None, QtGui.QApplication.UnicodeUTF8))
           p_Date=p_Date.addDays(1)
           self.label_19.setText(QtGui.QApplication.translate("MainWindow", p_Date.toString("dddd MMM dd"), None, QtGui.QApplication.UnicodeUTF8))
           p_Date=p_Date.addDays(1)
           self.label_20.setText(QtGui.QApplication.translate("MainWindow", p_Date.toString("dddd MMM dd"), None, QtGui.QApplication.UnicodeUTF8))
           p_Date=p_Date.addDays(1)
           self.label_21.setText(QtGui.QApplication.translate("MainWindow", p_Date.toString("dddd MMM dd"), None, QtGui.QApplication.UnicodeUTF8))
        if day == 3:
           sun=p_Date.addDays(-3)
           mon=p_Date.addDays(-2)
           tues=p_Date.addDays(-1)
           self.label_8.setText(QtGui.QApplication.translate("MainWindow", sun.toString("dddd MMM dd"), None, QtGui.QApplication.UnicodeUTF8))
           self.label_9.setText(QtGui.QApplication.translate("MainWindow", mon.toString("dddd MMM dd"), None, QtGui.QApplication.UnicodeUTF8))
           self.label_10.setText(QtGui.QApplication.translate("MainWindow",tues.toString("dddd MMM dd"), None, QtGui.QApplication.UnicodeUTF8))
           self.label_11.setText(QtGui.QApplication.translate("MainWindow", p_Date.toString("dddd MMM dd"), None, QtGui.QApplication.UnicodeUTF8))
           p_Date=p_Date.addDays(1)
           self.label_12.setText(QtGui.QApplication.translate("MainWindow", p_Date.toString("dddd MMM dd"), None, QtGui.QApplication.UnicodeUTF8))
           p_Date=p_Date.addDays(1)
           self.label_13.setText(QtGui.QApplication.translate("MainWindow", p_Date.toString("dddd MMM dd"), None, QtGui.QApplication.UnicodeUTF8))
           p_Date=p_Date.addDays(1)
           self.label_14.setText(QtGui.QApplication.translate("MainWindow", p_Date.toString("dddd MMM dd"), None, QtGui.QApplication.UnicodeUTF8))
           p_Date=p_Date.addDays(1)
           self.label_15.setText(QtGui.QApplication.translate("MainWindow", p_Date.toString("dddd MMM dd"), None, QtGui.QApplication.UnicodeUTF8))
           p_Date=p_Date.addDays(1)
           self.label_16.setText(QtGui.QApplication.translate("MainWindow", p_Date.toString("dddd MMM dd"), None, QtGui.QApplication.UnicodeUTF8))
           p_Date=p_Date.addDays(1)
           self.label_17.setText(QtGui.QApplication.translate("MainWindow", p_Date.toString("dddd MMM dd"), None, QtGui.QApplication.UnicodeUTF8))
           p_Date=p_Date.addDays(1)
           self.label_18.setText(QtGui.QApplication.translate("MainWindow", p_Date.toString("dddd MMM dd"), None, QtGui.QApplication.UnicodeUTF8))
           p_Date=p_Date.addDays(1)
           self.label_19.setText(QtGui.QApplication.translate("MainWindow", p_Date.toString("dddd MMM dd"), None, QtGui.QApplication.UnicodeUTF8))
           p_Date=p_Date.addDays(1)
           self.label_20.setText(QtGui.QApplication.translate("MainWindow", p_Date.toString("dddd MMM dd"), None, QtGui.QApplication.UnicodeUTF8))
           p_Date=p_Date.addDays(1)
           self.label_21.setText(QtGui.QApplication.translate("MainWindow", p_Date.toString("dddd MMM dd"), None, QtGui.QApplication.UnicodeUTF8))
        if day == 4:
           sun=p_Date.addDays(-4)
           mon=p_Date.addDays(-3)
           tues=p_Date.addDays(-2)
           wed=p_Date.addDays(-1)
           self.label_8.setText(QtGui.QApplication.translate("MainWindow", sun.toString("dddd MMM dd"), None, QtGui.QApplication.UnicodeUTF8))
           self.label_9.setText(QtGui.QApplication.translate("MainWindow", mon.toString("dddd MMM dd"), None, QtGui.QApplication.UnicodeUTF8))
           self.label_10.setText(QtGui.QApplication.translate("MainWindow", tues.toString("dddd MMM dd"), None, QtGui.QApplication.UnicodeUTF8))
           self.label_11.setText(QtGui.QApplication.translate("MainWindow", wed.toString("dddd MMM dd"), None, QtGui.QApplication.UnicodeUTF8))
           self.label_12.setText(QtGui.QApplication.translate("MainWindow", p_Date.toString("dddd MMM dd"), None, QtGui.QApplication.UnicodeUTF8))
           p_Date=p_Date.addDays(1)
           self.label_13.setText(QtGui.QApplication.translate("MainWindow", p_Date.toString("dddd MMM dd"), None, QtGui.QApplication.UnicodeUTF8))
           p_Date=p_Date.addDays(1)
           self.label_14.setText(QtGui.QApplication.translate("MainWindow", p_Date.toString("dddd MMM dd"), None, QtGui.QApplication.UnicodeUTF8))
           p_Date=p_Date.addDays(1)
           self.label_15.setText(QGui.QApplication.translate("MainWindow", p_Date.toString("dddd MMM dd"), None, QtGui.QApplication.UnicodeUTF8))
           p_Date=p_Date.addDays(1)
           self.label_16.setText(QtGui.QApplication.translate("MainWindow", p_Date.toString("dddd MMM dd"), None, QtGui.QApplication.UnicodeUTF8))
           p_Date=p_Date.addDays(1)
           self.label_17.setText(QtGui.QApplication.translate("MainWindow", p_Date.toString("dddd MMM dd"), None, QtGui.QApplication.UnicodeUTF8))
           p_Date=p_Date.addDays(1)
           self.label_18.setText(QtGui.QApplication.translate("MainWindow", p_Date.toString("dddd MMM dd"), None, QtGui.QApplication.UnicodeUTF8))
           p_Date=p_Date.addDays(1)
           self.label_19.setText(QtGui.QApplication.translate("MainWindow", p_Date.toString("dddd MMM dd"), None, QtGui.QApplication.UnicodeUTF8))
           p_Date=p_Date.addDays(1)
           self.label_20.setText(QtGui.QApplication.translate("MainWindow", p_Date.toString("dddd MMM dd"), None, QtGui.QApplication.UnicodeUTF8))
           p_Date=p_Date.addDays(1)
           self.label_21.setText(QtGui.QApplication.translate("MainWindow", p_Date.toString("dddd MMM dd"), None, QtGui.QApplication.UnicodeUTF8))
        if day == 5:
           sun=p_Date.addDays(-5)
           mon=p_Date.addDays(-4)
           tues=p_Date.addDays(-3)
           wed=p_Date.addDays(-2)
           thurs=p_Date.addDays(-1)
           self.label_8.setText(QtGui.QApplication.translate("MainWindow", sun.toString("dddd MMM dd"), None, QtGui.QApplication.UnicodeUTF8))
           self.label_9.setText(QtGui.QApplication.translate("MainWindow", mon.toString("dddd MMM dd"), None, QtGui.QApplication.UnicodeUTF8))
           self.label_10.setText(QtGui.QApplication.translate("MainWindow", tues.toString("dddd MMM dd"), None, QtGui.QApplication.UnicodeUTF8))
           self.label_11.setText(QtGui.QApplication.translate("MainWindow", wed.toString("dddd MMM dd"), None, QtGui.QApplication.UnicodeUTF8))
           self.label_12.setText(QtGui.QApplication.translate("MainWindow", thurs.toString("dddd MMM dd"), None, QtGui.QApplication.UnicodeUTF8))
           self.label_13.setText(QtGui.QApplication.translate("MainWindow", p_Date.toString("dddd MMM dd"), None, QtGui.QApplication.UnicodeUTF8))
           p_Date=p_Date.addDays(1)
           self.label_14.setText(QtGui.QApplication.translate("MainWindow", p_Date.toString("dddd MMM dd"), None, QtGui.QApplication.UnicodeUTF8))
           p_Date=p_Date.addDays(1)
           self.label_15.setText(QtGui.QApplication.translate("MainWindow", p_Date.toString("dddd MMM dd"), None, QtGui.QApplication.UnicodeUTF8))
           p_Date=p_Date.addDays(1)
           self.label_16.setText(QtGui.QApplication.translate("MainWindow", p_Date.toString("dddd MMM dd"), None, QtGui.QApplication.UnicodeUTF8))
           p_Date=p_Date.addDays(1)
           self.label_17.setText(QtGui.QApplication.translate("MainWindow", p_Date.toString("dddd MMM dd"), None, QtGui.QApplication.UnicodeUTF8))
           p_Date=p_Date.addDays(1)
           self.label_18.setText(QtGui.QApplication.translate("MainWindow", p_Date.toString("dddd MMM dd"), None, QtGui.QApplication.UnicodeUTF8))
           p_Date=p_Date.addDays(1)
           self.label_19.setText(QtGui.QApplication.translate("MainWindow", p_Date.toString("dddd MMM dd"), None, QtGui.QApplication.UnicodeUTF8))
           p_Date=p_Date.addDays(1)
           self.label_20.setText(QtGui.QApplication.translate("MainWindow", p_Date.toString("dddd MMM dd"), None, QtGui.QApplication.UnicodeUTF8))
           p_Date=p_Date.addDays(1)
           self.label_21.setText(QtGui.QApplication.translate("MainWindow", p_Date.toString("dddd MMM dd"), None, QtGui.QApplication.UnicodeUTF8))
        if day == 6:
           sun=p_Date.addDays(-6)
           mon=p_Date.addDays(-5)
           tues=p_Date.addDays(-4)
           wed=p_Date.addDays(-3)
           thurs=p_Date.addDays(-2)
           fri=p_Date.addDays(-1)
           self.label_8.setText(QtGui.QApplication.translate("MainWindow", sun.toString("dddd MMM dd"), None, QtGui.QApplication.UnicodeUTF8))
           self.label_9.setText(QtGui.QApplication.translate("MainWindow", mon.toString("dddd MMM dd"), None, QtGui.QApplication.UnicodeUTF8))
           self.label_10.setText(QtGui.QApplication.translate("MainWindow", tues.toString("dddd MMM dd"), None, QtGui.QApplication.UnicodeUTF8))
           self.label_11.setText(QtGui.QApplication.translate("MainWindow", wed.toString("dddd MMM dd"), None, QtGui.QApplication.UnicodeUTF8))
           self.label_12.setText(QtGui.QApplication.translate("MainWindow", thurs.toString("dddd MMM dd"), None, QtGui.QApplication.UnicodeUTF8))
           self.label_13.setText(QtGui.QApplication.translate("MainWindow", fri.toString("dddd MMM dd"), None, QtGui.QApplication.UnicodeUTF8))
           self.label_14.setText(QtGui.QApplication.translate("MainWindow", p_Date.toString("dddd MMM dd"), None, QtGui.QApplication.UnicodeUTF8))
           p_Date=p_Date.addDays(1)
           self.label_15.setText(QtGui.QApplication.translate("MainWindow", p_Date.toString("dddd MMM dd"), None, QtGui.QApplication.UnicodeUTF8))
           p_Date=p_Date.addDays(1)
           self.label_16.setText(QtGui.QApplication.translate("MainWindow", p_Date.toString("dddd MMM dd"), None, QtGui.QApplication.UnicodeUTF8))
           p_Date=p_Date.addDays(1)
           self.label_17.setText(QtGui.QApplication.translate("MainWindow", p_Date.toString("dddd MMM dd"), None, QtGui.QApplication.UnicodeUTF8))
           p_Date=p_Date.addDays(1)
           self.label_18.setText(QtGui.QApplication.translate("MainWindow", p_Date.toString("dddd MMM dd"), None, QtGui.QApplication.UnicodeUTF8))
           p_Date=p_Date.addDays(1)
           self.label_19.setText(QtGui.QApplication.translate("MainWindow", p_Date.toString("dddd MMM dd"), None, QtGui.QApplication.UnicodeUTF8))
           p_Date=p_Date.addDays(1)
           self.label_20.setText(QtGui.QApplication.translate("MainWindow", p_Date.toString("dddd MMM dd"), None, QtGui.QApplication.UnicodeUTF8))
           p_Date=p_Date.addDays(1)
           self.label_21.setText(QtGui.QApplication.translate("MainWindow", p_Date.toString("dddd MMM dd"), None, QtGui.QApplication.UnicodeUTF8))
        if day == 7:
           self.label_8.setText(QtGui.QApplication.translate("MainWindow", p_Date.toString("dddd MMM dd"), None, QtGui.QApplication.UnicodeUTF8))
           p_Date=p_Date.addDays(1) 
           self.label_9.setText(QtGui.QApplication.translate("MainWindow", p_Date.toString("dddd MMM dd"), None, QtGui.QApplication.UnicodeUTF8))
           p_Date = p_Date.addDays(1)
           self.label_10.setText(QtGui.QApplication.translate("MainWindow", p_Date.toString("dddd MMM dd"), None, QtGui.QApplication.UnicodeUTF8))
           p_Date=p_Date.addDays(1)
           self.label_11.setText(QtGui.QApplication.translate("MainWindow", p_Date.toString("dddd MMM dd"), None, QtGui.QApplication.UnicodeUTF8))
           p_Date=p_Date.addDays(1)
           self.label_12.setText(QtGui.QApplication.translate("MainWindow", p_Date.toString("dddd MMM dd"), None, QtGui.QApplication.UnicodeUTF8))
           p_Date=p_Date.addDays(1)
           self.label_13.setText(QtGui.QApplication.translate("MainWindow", p_Date.toString("dddd MMM dd"), None, QtGui.QApplication.UnicodeUTF8))
           p_Date=p_Date.addDays(1)
           self.label_14.setText(QtGui.QApplication.translate("MainWindow", p_Date.toString("dddd MMM dd"), None, QtGui.QApplication.UnicodeUTF8))
           p_Date=p_Date.addDays(1)
           self.label_15.setText(QtGui.QApplication.translate("MainWindow", p_Date.toString("dddd MMM dd"), None, QtGui.QApplication.UnicodeUTF8))
           p_Date=p_Date.addDays(1)
           self.label_16.setText(QtGui.QApplication.translate("MainWindow", p_Date.toString("dddd MMM dd"), None, QtGui.QApplication.UnicodeUTF8))
           p_Date=p_Date.addDays(1)
           self.label_17.setText(QtGui.QApplication.translate("MainWindow", p_Date.toString("dddd MMM dd"), None, QtGui.QApplication.UnicodeUTF8))
           p_Date=p_Date.addDays(1)
           self.label_18.setText(QtGui.QApplication.translate("MainWindow", p_Date.toString("dddd MMM dd"), None, QtGui.QApplication.UnicodeUTF8))
           p_Date=p_Date.addDays(1)
           self.label_19.setText(QtGui.QApplication.translate("MainWindow", p_Date.toString("dddd MMM dd"), None, QtGui.QApplication.UnicodeUTF8))
           p_Date=p_Date.addDays(1)
           self.label_20.setText(QtGui.QApplication.translate("MainWindow", p_Date.toString("dddd MMM dd"), None, QtGui.QApplication.UnicodeUTF8))
           p_Date=p_Date.addDays(1)
           self.label_21.setText(QtGui.QApplication.translate("MainWindow", p_Date.toString("dddd MMM dd"), None, QtGui.QApplication.UnicodeUTF8))

    
    def fill_labels2(self, p_Date):
        day = int(p_Date.dayOfWeek())
        if day == 1:
           sun=p_Date.addDays(-1)
           self.label_7.setText(QtGui.QApplication.translate("MainWindow", sun.toString("dddd MMM dd"), None, QtGui.QApplication.UnicodeUTF8))
           self.label_6.setText(QtGui.QApplication.translate("MainWindow", p_Date.toString("dddd MMM dd"), None, QtGui.QApplication.UnicodeUTF8))
           p_Date = p_Date.addDays(1)
           self.label_5.setText(QtGui.QApplication.translate("MainWindow", p_Date.toString("dddd MMM dd"), None, QtGui.QApplication.UnicodeUTF8))
           p_Date=p_Date.addDays(1)
           self.label_4.setText(QtGui.QApplication.translate("MainWindow", p_Date.toString("dddd MMM dd"), None, QtGui.QApplication.UnicodeUTF8))
           p_Date=p_Date.addDays(1)
           self.label_3.setText(QtGui.QApplication.translate("MainWindow", p_Date.toString("dddd MMM dd"), None, QtGui.QApplication.UnicodeUTF8))
           p_Date=p_Date.addDays(1)
           self.label_2.setText(QtGui.QApplication.translate("MainWindow", p_Date.toString("dddd MMM dd"), None, QtGui.QApplication.UnicodeUTF8))
           p_Date=p_Date.addDays(1)
           self.label.setText(QtGui.QApplication.translate("MainWindow", p_Date.toString("dddd MMM dd"), None, QtGui.QApplication.UnicodeUTF8))
        if day == 2:
           sun=p_Date.addDays(-2)
           mon=p_Date.addDays(-1)
           self.label_7.setText(QtGui.QApplication.translate("MainWindow", sun.toString("dddd MMM dd"), None, QtGui.QApplication.UnicodeUTF8))
           self.label_6.setText(QtGui.QApplication.translate("MainWindow", mon.toString("dddd MMM dd"), None, QtGui.QApplication.UnicodeUTF8))
           self.label_5.setText(QtGui.QApplication.translate("MainWindow", p_Date.toString("dddd MMM dd"), None, QtGui.QApplication.UnicodeUTF8))
           p_Date=p_Date.addDays(1)
           self.label_4.setText(QtGui.QApplication.translate("MainWindow", p_Date.toString("dddd MMM dd"), None, QtGui.QApplication.UnicodeUTF8))
           p_Date=p_Date.addDays(1)
           self.label_3.setText(QtGui.QApplication.translate("MainWindow", p_Date.toString("dddd MMM dd"), None, QtGui.QApplication.UnicodeUTF8))
           p_Date=p_Date.addDays(1)
           self.label_2.setText(QtGui.QApplication.translate("MainWindow", p_Date.toString("dddd MMM dd"), None, QtGui.QApplication.UnicodeUTF8))
           p_Date=p_Date.addDays(1)
           self.label.setText(QtGui.QApplication.translate("MainWindow", p_Date.toString("dddd MMM dd"), None, QtGui.QApplication.UnicodeUTF8))
        if day == 3:
           sun=p_Date.addDays(-3)
           mon=p_Date.addDays(-2)
           tues=p_Date.addDays(-1)
           self.label_7.setText(QtGui.QApplication.translate("MainWindow", sun.toString("dddd MMM dd"), None, QtGui.QApplication.UnicodeUTF8))
           self.label_6.setText(QtGui.QApplication.translate("MainWindow", mon.toString("dddd MMM dd"), None, QtGui.QApplication.UnicodeUTF8))
           self.label_5.setText(QtGui.QApplication.translate("MainWindow", tues.toString("dddd MMM dd"), None, QtGui.QApplication.UnicodeUTF8))
           self.label_4.setText(QtGui.QApplication.translate("MainWindow", p_Date.toString("dddd MMM dd"), None, QtGui.QApplication.UnicodeUTF8))
           p_Date=p_Date.addDays(1)
           self.label_3.setText(QtGui.QApplication.translate("MainWindow", p_Date.toString("dddd MMM dd"), None, QtGui.QApplication.UnicodeUTF8))
           p_Date=p_Date.addDays(1)
           self.label_2.setText(QtGui.QApplication.translate("MainWindow", p_Date.toString("dddd MMM dd"), None, QtGui.QApplication.UnicodeUTF8))
           p_Date=p_Date.addDays(1)
           self.label.setText(QtGui.QApplication.translate("MainWindow", p_Date.toString("dddd MMM dd"), None, QtGui.QApplication.UnicodeUTF8))
        if day == 4:
           sun=p_Date.addDays(-4)
           mon=p_Date.addDays(-3)
           tues=p_Date.addDays(-2)
           wed=p_Date.addDays(-1)
           self.label_7.setText(QtGui.QApplication.translate("MainWindow", sun.toString("dddd MMM dd"), None, QtGui.QApplication.UnicodeUTF8))
           self.label_6.setText(QtGui.QApplication.translate("MainWindow", mon.toString("dddd MMM dd"), None, QtGui.QApplication.UnicodeUTF8))
           self.label_5.setText(QtGui.QApplication.translate("MainWindow", tues.toString("dddd MMM dd"), None, QtGui.QApplication.UnicodeUTF8))
           self.label_4.setText(QtGui.QApplication.translate("MainWindow", wed.toString("dddd MMM dd"), None, QtGui.QApplication.UnicodeUTF8))
           self.label_3.setText(QtGui.QApplication.translate("MainWindow", p_Date.toString("dddd MMM dd"), None, QtGui.QApplication.UnicodeUTF8))
           p_Date=p_Date.addDays(1)
           self.label_2.setText(QtGui.QApplication.translate("MainWindow", p_Date.toString("dddd MMM dd"), None, QtGui.QApplication.UnicodeUTF8))
           p_Date=p_Date.addDays(1)
           self.label.setText(QtGui.QApplication.translate("MainWindow", p_Date.toString("dddd MMM dd"), None, QtGui.QApplication.UnicodeUTF8))
        if day == 5:
           sun=p_Date.addDays(-5)
           mon=p_Date.addDays(-4)
           tues=p_Date.addDays(-3)
           wed=p_Date.addDays(-2)
           thurs=p_Date.addDays(-1)
           self.label_7.setText(QtGui.QApplication.translate("MainWindow", sun.toString("dddd MMM dd"), None, QtGui.QApplication.UnicodeUTF8))
           self.label_6.setText(QtGui.QApplication.translate("MainWindow", mon.toString("dddd MMM dd"), None, QtGui.QApplication.UnicodeUTF8))
           self.label_5.setText(QtGui.QApplication.translate("MainWindow", tues.toString("dddd MMM dd"), None, QtGui.QApplication.UnicodeUTF8))
           self.label_4.setText(QtGui.QApplication.translate("MainWindow", wed.toString("dddd MMM dd"), None, QtGui.QApplication.UnicodeUTF8))
           self.label_3.setText(QtGui.QApplication.translate("MainWindow", thurs.toString("dddd MMM dd"), None, QtGui.QApplication.UnicodeUTF8))
           self.label_2.setText(QtGui.QApplication.translate("MainWindow", p_Date.toString("dddd MMM dd"), None, QtGui.QApplication.UnicodeUTF8))
           p_Date=p_Date.addDays(1)
           self.label.setText(QtGui.QApplication.translate("MainWindow", p_Date.toString("dddd MMM dd"), None, QtGui.QApplication.UnicodeUTF8))
        if day == 6:
           sun=p_Date.addDays(-6)
           mon=p_Date.addDays(-5)
           tues=p_Date.addDays(-4)
           wed=p_Date.addDays(-3)
           thurs=p_Date.addDays(-2)
           fri=p_Date.addDays(-1)
           self.label_7.setText(QtGui.QApplication.translate("MainWindow", sun.toString("dddd MMM dd"), None, QtGui.QApplication.UnicodeUTF8))
           self.label_6.setText(QtGui.QApplication.translate("MainWindow", mon.toString("dddd MMM dd"), None, QtGui.QApplication.UnicodeUTF8))
           self.label_5.setText(QtGui.QApplication.translate("MainWindow", tues.toString("dddd MMM dd"), None, QtGui.QApplication.UnicodeUTF8))
           self.label_4.setText(QtGui.QApplication.translate("MainWindow", wed.toString("dddd MMM dd"), None, QtGui.QApplication.UnicodeUTF8))
           self.label_3.setText(QtGui.QApplication.translate("MainWindow", thurs.toString("dddd MMM dd"), None, QtGui.QApplication.UnicodeUTF8))
           self.label_2.setText(QtGui.QApplication.translate("MainWindow", fri.toString("dddd MMM dd"), None, QtGui.QApplication.UnicodeUTF8))
           self.label.setText(QtGui.QApplication.translate("MainWindow", p_Date.toString("dddd MMM dd"), None, QtGui.QApplication.UnicodeUTF8))
        if day == 7:
           self.label_7.setText(QtGui.QApplication.translate("MainWindow", p_Date.toString("dddd MMM dd"), None, QtGui.QApplication.UnicodeUTF8))
           p_Date=p_Date.addDays(1) 
           self.label_6.setText(QtGui.QApplication.translate("MainWindow", p_Date.toString("dddd MMM dd"), None, QtGui.QApplication.UnicodeUTF8))
           p_Date=p_Date.addDays(1) 
           self.label_5.setText(QtGui.QApplication.translate("MainWindow", p_Date.toString("dddd MMM dd"), None, QtGui.QApplication.UnicodeUTF8))
           p_Date=p_Date.addDays(1) 
           self.label_4.setText(QtGui.QApplication.translate("MainWindow", p_Date.toString("dddd MMM dd"), None, QtGui.QApplication.UnicodeUTF8))
           p_Date=p_Date.addDays(1) 
           self.label_3.setText(QtGui.QApplication.translate("MainWindow", p_Date.toString("dddd MMM dd"), None, QtGui.QApplication.UnicodeUTF8))
           p_Date=p_Date.addDays(1)
           self.label_2.setText(QtGui.QApplication.translate("MainWindow", p_Date.toString("dddd MMM dd"), None, QtGui.QApplication.UnicodeUTF8))
           p_Date=p_Date.addDays(1)
           self.label.setText(QtGui.QApplication.translate("MainWindow", p_Date.toString("dddd MMM dd"), None, QtGui.QApplication.UnicodeUTF8))



    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1123, 871)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1123, 871))
        MainWindow.setMaximumSize(QtCore.QSize(1123, 871))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.frame_2 = QtGui.QFrame(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMinimumSize(QtCore.QSize(200, 200))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.verticalLayout.addWidget(self.frame_2)
        self.toolBox = QtGui.QToolBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolBox.sizePolicy().hasHeightForWidth())
        self.toolBox.setSizePolicy(sizePolicy)
        self.toolBox.setMinimumSize(QtCore.QSize(200, 600))
        self.toolBox.setAutoFillBackground(True)
        self.toolBox.setObjectName(_fromUtf8("toolBox"))
        self.page_3 = QtGui.QWidget()
        self.page_3.setGeometry(QtCore.QRect(0, 0, 200, 542))
        self.page_3.setObjectName(_fromUtf8("page_3"))
        self.page_4 = QtGui.QWidget()
        self.page_4.setGeometry(QtCore.QRect(0,0,200,542))
        self.page_4.setObjectName(_fromUtf8("page_4"))
        self.formLayoutWidget = QtGui.QWidget(self.page_4)
        self.formLayoutWidget.setGeometry(QtCore.QRect(0, 0, 200, 531))
        self.formLayoutWidget.setObjectName(_fromUtf8("formLayoutWidget"))
        self.formLayout = QtGui.QFormLayout(self.formLayoutWidget)
        self.formLayout.setMargin(0)
        self.formLayout.setVerticalSpacing(2)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.formLayoutWidget_3 = QtGui.QWidget(self.page_3)
        self.formLayoutWidget_3.setGeometry(QtCore.QRect(0,0,200,531)) #181
        self.formLayoutWidget_3.setObjectName(_fromUtf8("formLayoutWidget_3"))
        self.formLayout_3 = QtGui.QFormLayout(self.formLayoutWidget_3)
        self.formLayout_3.setMargin(0)
        self.formLayout_3.setVerticalSpacing(2)
        self.formLayout_3.setObjectName(_fromUtf8("formLayout_3"))
        self.scrollArea=QtGui.QScrollArea(self.formLayoutWidget)
        self.verticalLayoutWidget = QtGui.QWidget(self.frame_2)
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        #self.TopFrameLayout = QtGui.QVeritcalLayout(self.verticalLayoutWidget)
        self.TopFrameLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.TopFrameLayout.setGeometry(QtCore.QRect(0,0,200,200))
        self.TopFrameLayout.setObjectName(_fromUtf8("TopFrameLayout"))
        self.TopFrameLayout.setContentsMargins(10,10,10,10)
        self.pushButton = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 20, 139, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.TopFrameLayout.addWidget(self.pushButton)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMinimumSize(QtCore.QSize(183,510))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea_2"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0,0,200,94))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.formLayout_7 = QtGui.QFormLayout(self.scrollAreaWidgetContents)
        self.formLayout_7.setObjectName(_fromUtf8("formLayout_7"))
        #self.pushButton_3 = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_3 = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.scrollArea_2 = QtGui.QScrollArea(self.formLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea_2.sizePolicy().hasHeightForWidth())
        self.scrollArea_2.setSizePolicy(sizePolicy)
        self.scrollArea_2.setMinimumSize(QtCore.QSize(183, 510))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName(_fromUtf8("scrollArea_2"))
        self.scrollAreaWidgetContents_2 = QtGui.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 200, 94))
        self.scrollAreaWidgetContents_2.setObjectName(_fromUtf8("scrollAreaWidgetContents_2"))
        self.formLayout_6 = QtGui.QFormLayout(self.scrollAreaWidgetContents_2)
        self.formLayout_6.setObjectName(_fromUtf8("formLayout_6"))
        #self.pushButton_2 = QtGui.QPushButton(self.scrollArea)
        #self.pushButton_2 = QtGui.QPushButton(self.scrollAreaWidgetContents_2)
        self.pushButton_2 = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        #self.formLayout_6.addWidget(self.pushButton_2)
        #self.formLayout.setWidget(0,QtGui.QFormLayout.SpanningRole,self.pushButton_3)
        self.toolBox.addItem(self.page_3, _fromUtf8(""))
        self.toolBox.addItem(self.page_4, _fromUtf8(""))
        self.verticalLayout.addWidget(self.toolBox)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.dateEdit_3 = QtGui.QDateEdit(self.tab)
        today = QtCore.QDate.currentDate()                            #current date in QDate Object format
        self.dateEdit_3.setDate(today)
        self.dateEdit_3.setGeometry(QtCore.QRect(310,0,300,30))
        self.dateEdit_3.setObjectName(_fromUtf8("dateEdit_3"))
        self.horizontalLayoutWidget_4 = QtGui.QWidget(self.tab)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(10, 30, 871, 31))
        self.horizontalLayoutWidget_4.setObjectName(_fromUtf8("horizontalLayoutWidget_4"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_5.setMargin(0)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_8 = QtGui.QLabel(self.horizontalLayoutWidget_4)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.horizontalLayout_5.addWidget(self.label_8)
        self.label_9 = QtGui.QLabel(self.horizontalLayoutWidget_4)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.horizontalLayout_5.addWidget(self.label_9)
        self.label_10 = QtGui.QLabel(self.horizontalLayoutWidget_4)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.horizontalLayout_5.addWidget(self.label_10)
        self.label_11 = QtGui.QLabel(self.horizontalLayoutWidget_4)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.horizontalLayout_5.addWidget(self.label_11)
        self.label_12 = QtGui.QLabel(self.horizontalLayoutWidget_4)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.horizontalLayout_5.addWidget(self.label_12)
        self.label_13 = QtGui.QLabel(self.horizontalLayoutWidget_4)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.horizontalLayout_5.addWidget(self.label_13)
        self.label_14 = QtGui.QLabel(self.horizontalLayoutWidget_4)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.horizontalLayout_5.addWidget(self.label_14)
        self.horizontalLayoutWidget_5 = QtGui.QWidget(self.tab)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(10, 380, 871, 31))
        self.horizontalLayoutWidget_5.setObjectName(_fromUtf8("horizontalLayoutWidget_5"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_6.setMargin(0)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_15 = QtGui.QLabel(self.horizontalLayoutWidget_5)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.horizontalLayout_6.addWidget(self.label_15)
        self.label_16 = QtGui.QLabel(self.horizontalLayoutWidget_5)
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.horizontalLayout_6.addWidget(self.label_16)
        self.label_17 = QtGui.QLabel(self.horizontalLayoutWidget_5)
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.horizontalLayout_6.addWidget(self.label_17)
        self.label_18 = QtGui.QLabel(self.horizontalLayoutWidget_5)
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.horizontalLayout_6.addWidget(self.label_18)
        self.label_19 = QtGui.QLabel(self.horizontalLayoutWidget_5)
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.horizontalLayout_6.addWidget(self.label_19)
        self.label_20 = QtGui.QLabel(self.horizontalLayoutWidget_5)
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.horizontalLayout_6.addWidget(self.label_20)
        self.label_21 = QtGui.QLabel(self.horizontalLayoutWidget_5)
        self.label_21.setAlignment(QtCore.Qt.AlignCenter)
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.horizontalLayout_6.addWidget(self.label_21)
        self.horizontalLayoutWidget_6 = QtGui.QWidget(self.tab)
        self.horizontalLayoutWidget_6.setGeometry(QtCore.QRect(10, 60, 871, 321))
        self.horizontalLayoutWidget_6.setObjectName(_fromUtf8("horizontalLayoutWidget_6"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_7.setSpacing(1)
        self.horizontalLayout_7.setMargin(0)
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.listWidget_9 = QtGui.QListWidget(self.horizontalLayoutWidget_6)
        self.listWidget_9.setObjectName(_fromUtf8("listWidget_9"))
        self.horizontalLayout_7.addWidget(self.listWidget_9)
        self.listWidget_10 = QtGui.QListWidget(self.horizontalLayoutWidget_6)
        self.listWidget_10.setObjectName(_fromUtf8("listWidget_10"))
        self.horizontalLayout_7.addWidget(self.listWidget_10)
        self.listWidget_11 = QtGui.QListWidget(self.horizontalLayoutWidget_6)
        self.listWidget_11.setObjectName(_fromUtf8("listWidget_11"))
        self.horizontalLayout_7.addWidget(self.listWidget_11)
        self.listWidget_12 = QtGui.QListWidget(self.horizontalLayoutWidget_6)
        self.listWidget_12.setObjectName(_fromUtf8("listWidget_12"))
        self.horizontalLayout_7.addWidget(self.listWidget_12)
        self.listWidget_13 = QtGui.QListWidget(self.horizontalLayoutWidget_6)
        self.listWidget_13.setObjectName(_fromUtf8("listWidget_13"))
        self.horizontalLayout_7.addWidget(self.listWidget_13)
        self.listWidget_14 = QtGui.QListWidget(self.horizontalLayoutWidget_6)
        self.listWidget_14.setObjectName(_fromUtf8("listWidget_14"))
        self.horizontalLayout_7.addWidget(self.listWidget_14)
        self.listWidget_15 = QtGui.QListWidget(self.horizontalLayoutWidget_6)
        self.listWidget_15.setObjectName(_fromUtf8("listWidget_15"))
        self.horizontalLayout_7.addWidget(self.listWidget_15)
        self.horizontalLayoutWidget_7 = QtGui.QWidget(self.tab)
        self.horizontalLayoutWidget_7.setGeometry(QtCore.QRect(10, 410, 871, 341))
        self.horizontalLayoutWidget_7.setObjectName(_fromUtf8("horizontalLayoutWidget_7"))
        self.horizontalLayout_8 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_7)
        self.horizontalLayout_8.setSpacing(1)
        self.horizontalLayout_8.setMargin(0)
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.listWidget_16 = QtGui.QListWidget(self.horizontalLayoutWidget_7)
        self.listWidget_16.setObjectName(_fromUtf8("listWidget_16"))
        self.horizontalLayout_8.addWidget(self.listWidget_16)
        self.listWidget_17 = QtGui.QListWidget(self.horizontalLayoutWidget_7)
        self.listWidget_17.setObjectName(_fromUtf8("listWidget_17"))
        self.horizontalLayout_8.addWidget(self.listWidget_17)
        self.listWidget_18 = QtGui.QListWidget(self.horizontalLayoutWidget_7)
        self.listWidget_18.setObjectName(_fromUtf8("listWidget_18"))
        self.horizontalLayout_8.addWidget(self.listWidget_18)
        self.listWidget_19 = QtGui.QListWidget(self.horizontalLayoutWidget_7)
        self.listWidget_19.setObjectName(_fromUtf8("listWidget_19"))
        self.horizontalLayout_8.addWidget(self.listWidget_19)
        self.listWidget_20 = QtGui.QListWidget(self.horizontalLayoutWidget_7)
        self.listWidget_20.setObjectName(_fromUtf8("listWidget_20"))
        self.horizontalLayout_8.addWidget(self.listWidget_20)
        self.listWidget_21 = QtGui.QListWidget(self.horizontalLayoutWidget_7)
        self.listWidget_21.setObjectName(_fromUtf8("listWidget_21"))
        self.horizontalLayout_8.addWidget(self.listWidget_21)
        self.listWidget_22 = QtGui.QListWidget(self.horizontalLayoutWidget_7)
        self.listWidget_22.setObjectName(_fromUtf8("listWidget_22"))
        self.horizontalLayout_8.addWidget(self.listWidget_22)
        self.calendarWidget = QtGui.QCalendarWidget(self.tab)
        self.calendarWidget.setGeometry(QtCore.QRect(310, 40, 300, 165))
        self.calendarWidget.setGridVisible(False)
        self.calendarWidget.setNavigationBarVisible(True)
        self.calendarWidget.setObjectName(_fromUtf8("calendarWidget"))
        self.calendarWidget.hide()
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.horizontalLayoutWidget_2 = QtGui.QWidget(self.tab_2)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 30, 871, 31))
        self.horizontalLayoutWidget_2.setObjectName(_fromUtf8("horizontalLayoutWidget_2"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_7 = QtGui.QLabel(self.horizontalLayoutWidget_2)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_3.addWidget(self.label_7)
        self.label_6 = QtGui.QLabel(self.horizontalLayoutWidget_2)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_3.addWidget(self.label_6)
        self.label_5 = QtGui.QLabel(self.horizontalLayoutWidget_2)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_3.addWidget(self.label_5)
        self.label_4 = QtGui.QLabel(self.horizontalLayoutWidget_2)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_3.addWidget(self.label_4)
        self.label_3 = QtGui.QLabel(self.horizontalLayoutWidget_2)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_3.addWidget(self.label_3)
        self.label_2 = QtGui.QLabel(self.horizontalLayoutWidget_2)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_3.addWidget(self.label_2)
        self.label = QtGui.QLabel(self.horizontalLayoutWidget_2)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_3.addWidget(self.label)
        self.dateEdit_2 = QtGui.QDateEdit(self.tab_2)
        self.dateEdit_2.setDate(today)
        self.dateEdit_2.setGeometry(QtCore.QRect(310,0,300,30))
        self.dateEdit_2.setObjectName(_fromUtf8("dateEdit_2"))
        self.horizontalLayoutWidget_3 = QtGui.QWidget(self.tab_2)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(10, 60, 871, 691))
        self.horizontalLayoutWidget_3.setObjectName(_fromUtf8("horizontalLayoutWidget_3"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_4.setSpacing(1)
        self.horizontalLayout_4.setMargin(0)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.listWidget_2 = QtGui.QListWidget(self.horizontalLayoutWidget_3)
        self.listWidget_2.setObjectName(_fromUtf8("listWidget_2"))
        self.horizontalLayout_4.addWidget(self.listWidget_2)
        self.listWidget_5 = QtGui.QListWidget(self.horizontalLayoutWidget_3)
        self.listWidget_5.setObjectName(_fromUtf8("listWidget_5"))
        self.horizontalLayout_4.addWidget(self.listWidget_5)
        self.listWidget_6 = QtGui.QListWidget(self.horizontalLayoutWidget_3)
        self.listWidget_6.setObjectName(_fromUtf8("listWidget_6"))
        self.horizontalLayout_4.addWidget(self.listWidget_6)
        self.listWidget_4 = QtGui.QListWidget(self.horizontalLayoutWidget_3)
        self.listWidget_4.setObjectName(_fromUtf8("listWidget_4"))
        self.horizontalLayout_4.addWidget(self.listWidget_4)
        self.listWidget_3 = QtGui.QListWidget(self.horizontalLayoutWidget_3)
        self.listWidget_3.setObjectName(_fromUtf8("listWidget_3"))
        self.horizontalLayout_4.addWidget(self.listWidget_3)
        self.listWidget = QtGui.QListWidget(self.horizontalLayoutWidget_3)
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.horizontalLayout_4.addWidget(self.listWidget)
        self.listWidget_8 = QtGui.QListWidget(self.horizontalLayoutWidget_3)
        self.listWidget_8.setObjectName(_fromUtf8("listWidget_8"))
        self.horizontalLayout_4.addWidget(self.listWidget_8)
        self.calendarWidget_2 = QtGui.QCalendarWidget(self.tab_2)
        self.calendarWidget_2.setGeometry(QtCore.QRect(310, 40, 300, 165))
        self.calendarWidget_2.setObjectName(_fromUtf8("calendarWidget_2"))
        self.calendarWidget_2.hide()
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.horizontalLayoutWidget = QtGui.QWidget(self.tab_3)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 30, 871, 721))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setSpacing(1)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.listWidget_7 = QtGui.QListWidget(self.horizontalLayoutWidget)
        self.listWidget_7.setObjectName(_fromUtf8("listWidget_7"))
        self.horizontalLayout_2.addWidget(self.listWidget_7)
        self.dateEdit = QtGui.QDateEdit(self.tab_3)
        self.dateEdit.setGeometry(QtCore.QRect(310,0,300,30))
        self.dateEdit.setObjectName(_fromUtf8("dateEdit"))
        self.dateEdit.setDate(today)
        self.calendarWidget_3 = QtGui.QCalendarWidget(self.tab_3)
        self.calendarWidget_3.setGeometry(QtCore.QRect(310,40,300,165))
        self.calendarWidget_3.setObjectName(_fromUtf8("calendarWidget_3"))
        self.calendarWidget_3.hide()
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.gridLayout.addWidget(self.tabWidget, 1, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1123, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionRemEmp = QtGui.QAction(MainWindow)
        self.actionRemEmp.setObjectName(_fromUtf8("actionRemEmp"))
        self.actionRemStat = QtGui.QAction(MainWindow)
        self.actionContact = QtGui.QAction(MainWindow)
        self.actionContact.setObjectName(_fromUtf8("actionContact"))
        self.actionRemStat.setObjectName(_fromUtf8("actionRemStat"))
        self.menuFile.addAction(self.actionRemEmp) 
        self.menuFile.addAction(self.actionRemStat)
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuHelp.addAction(self.actionContact)
        self.retranslateUi(MainWindow)
        self.TopFrameLayout.addWidget(self.pushButton_2)
        self.TopFrameLayout.addWidget(self.pushButton_3)
        self.toolBox.setCurrentIndex(1)
        self.populateCheckboxes()
        self.label_22 = QtGui.QLabel(self.frame_2)
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.label_22.setGeometry(QtCore.QRect(40,95,191,101));
        myPixmap = QtGui.QPixmap(_fromUtf8('./data/Clemson_nobg.png'))
        myScaledPixmap = myPixmap.scaled(self.label_22.size(), QtCore.Qt.KeepAspectRatio)
        self.label_22.setPixmap(myScaledPixmap)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.updateRecordsClicked)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.addEmpClicked)
        QtCore.QObject.connect(self.pushButton_3, QtCore.SIGNAL(_fromUtf8("clicked()")), self.addStatClicked)
        QtCore.QObject.connect(self.dateEdit_3, QtCore.SIGNAL(_fromUtf8("dateChanged(QDate)")), self.calendarWidget.show) #right
        QtCore.QObject.connect(self.calendarWidget_2, QtCore.SIGNAL(_fromUtf8("clicked(QDate)")), self.calclicked2  )
        QtCore.QObject.connect(self.dateEdit_2, QtCore.SIGNAL(_fromUtf8("dateChanged(QDate)")), self.calendarWidget_2.show)
        QtCore.QObject.connect(self.calendarWidget, QtCore.SIGNAL(_fromUtf8("clicked(QDate)")), self.calclicked)
        QtCore.QObject.connect(self.dateEdit, QtCore.SIGNAL(_fromUtf8("dateChanged(QDate)")), self.calendarWidget_3.show)
        QtCore.QObject.connect(self.calendarWidget_3, QtCore.SIGNAL(_fromUtf8("clicked(QDate)")), self.calclicked3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        QtCore.QObject.connect(self.actionExit, QtCore.SIGNAL(_fromUtf8("activated()")), sys.exit)
        QtCore.QObject.connect(self.actionRemEmp, QtCore.SIGNAL(_fromUtf8("activated()")), self.remEmpClicked)
        QtCore.QObject.connect(self.actionRemStat, QtCore.SIGNAL(_fromUtf8("activated()")), self.remStatClicked)          
        QtCore.QObject.connect(self.actionContact, QtCore.SIGNAL(_fromUtf8("activated()")), self.contactClicked)

    def retranslateUi(self, MainWindow):
        today = QtCore.QDate.currentDate()
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("MainWindow", "Update", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setMinimumSize(180,27)
        self.pushButton.setMaximumSize(180,27)
        self.pushButton_2.setText(QtGui.QApplication.translate("MainWindow", "Add Employee", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setMinimumSize(180,27)
        self.pushButton_2.setMaximumSize(180,27)
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_3), QtGui.QApplication.translate("MainWindow", "Project Statuses", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setText(QtGui.QApplication.translate("MainWindow", "Add Status", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setMinimumSize(180,27)
        self.pushButton_3.setMaximumSize(180,27)
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_4), QtGui.QApplication.translate("MainWindow", "Employees", None, QtGui.QApplication.UnicodeUTF8))
        self.dateEdit_3.setDisplayFormat(QtGui.QApplication.translate("MainWindow", "d MMMM yyyy", None, QtGui.QApplication.UnicodeUTF8))
        self.fill_labels1(today)
        self.fill_labels2(today)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("MainWindow", "Bi-Weekly", None, QtGui.QApplication.UnicodeUTF8))
        self.dateEdit_2.setDisplayFormat(QtGui.QApplication.translate("MainWindow", "d MMMM yyyy", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("MainWindow", "Weekly", None, QtGui.QApplication.UnicodeUTF8))
        self.dateEdit.setDisplayFormat(QtGui.QApplication.translate("MainWindow", "d MMMM yyyy", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QtGui.QApplication.translate("MainWindow", "Daily", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("MainWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setText(QtGui.QApplication.translate("MainWindow", "Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRemEmp.setText(QtGui.QApplication.translate("MainWindow", "Remove Employee", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRemStat.setText(QtGui.QApplication.translate("MainWindow", "Remove Status", None, QtGui.QApplication.UnicodeUTF8))
        self.actionContact.setText(QtGui.QApplication.translate("MainWindow", "Contact", None, QtGui.QApplication.UnicodeUTF8))
 #self.refreshCheckboxes()

if __name__ == "__main__":
    import sys
    xml = xmlparse.Xmlp()
    hpr = helper.Helper()
    employees = hpr.updateEmployee()
    #print "employees "+str(employees)
    statuses = hpr.updateStatus()
    #print "statuses "+str(statuses)
    records = xml.fetchRecords()
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.employees = employees
    ui.statuses = statuses
    ui.setupUi(MainWindow)
    MainWindow.show()
    atexit.register(ui.goodbye)
    sys.exit(app.exec_())

