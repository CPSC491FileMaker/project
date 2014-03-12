# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'updated_layout_with_stretch_and_scrollareas_drawn_in.ui'
#
# Created: Sat Mar  8 13:33:19 2014
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import QDateTime
import atexit,os,signal,subprocess,helper, xmlparse, addEmployee, addStatus, removeEmployee, removeStatus, re
from datetime import date
import datetime

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)
    


class Ui_MainWindow(object):

    
    employees = []
    statuses = []
    #empCheckBoxes = []
    #statCheckBoxes = []    
    empStatus = False
    statStatus = False

    def openMenu(self,position):
        menu = QtGui.QMenu()
        clearAll= menu.addAction("Clear All")
        action = menu.exec_(self.listWidget_7.mapToGlobal(position))
        if action == clearAll:
            self.listWidget_7.clear()

    def contactClicked(self):
        print "stub"
    
    def aboutClicked(self):
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

    def goodbye(self,proc):
      os.killpg(proc.pid,signal.SIGTERM)
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

    def updateRecordsClicked(self):
      records = xml.fetchRecords()  
    
    def populateCheckboxes(self):
      #self.empCheckBoxes = []
      #self.statCheckBoxes = []
      ind =2
      #self.formLayout_6.addWidget(self.pushButton_2)
      for person in self.employees:
        ind += 1
        self.checkBox = QtGui.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.formLayout_3.addWidget(self.checkBox)    #formlayout3 contains employee checkboxes 
        #self.empCheckBoxes.append(self.checkBox)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.formLayout.setWidget(0,QtGui.QFormLayout.LabelRole,self.scrollArea)
        self.checkBox.setText(QtGui.QApplication.translate("MainWindow", person[0], None, QtGui.QApplication.UnicodeUTF8))
      ind =2 
      #self.formLayout_7.addWidget(self.pushButton_3)
      for status in self.statuses:
        ind += 1
        self.checkBox_3 = QtGui.QCheckBox(self.scrollAreaWidgetContents_2)
        self.checkBox_3.setObjectName(_fromUtf8("checkBox3"))
        self.formLayout_4.addWidget(self.checkBox_3) #formlayout4 containts status checkboxes
        #self.statCheckBoxes.append(self.checkBox_3)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.formLayout_2.setWidget(0,QtGui.QFormLayout.LabelRole,self.scrollArea_2)
        self.checkBox_3.setText(QtGui.QApplication.translate("MainWindow", status, None, QtGui.QApplication.UnicodeUTF8))
    
    def refreshCheckboxes(self):
        for i in reversed(range(self.formLayout_3.count())):
            item = self.formLayout_3.itemAt(i)
            if isinstance(item, QtGui.QWidgetItem):
                item.widget().close()
            self.formLayout_3.removeItem(item)

        for i in reversed(range(self.formLayout_4.count())): 
            item = self.formLayout_4.itemAt(i)
            if isinstance(item, QtGui.QWidgetItem):
                item.widget().close()
            self.formLayout_4.removeItem(item) 
        self.populateCheckboxes()
    
    #formLayout_6 == employee checkBoxes
   
    def checkEmp(self,employeeName):
      count = 0
      #print "in checkEmp "
      #for checkBox in self.empCheckBoxes:
      for i in range(self.formLayout_3.count()):
        #print "cb.text "+str(i)+' '+self.formLayout_6.itemAt(i).widget().text()
        if (self.formLayout_3.itemAt(i).widget().text() == employeeName):
          self.empStatus = self.formLayout_3.itemAt(i).widget().isChecked()
          #print "empStatus "+str(self.empStatus)
          return
        else:
          self.empStatus = False

    def checkStat(self,status):
      #print "in checkStat "
      #for checkBox in self.statCheckBoxes:
      for i in range(self.formLayout_4.count()):
        #print "cb.text "+self.formLayout_7.itemAt(i).widget().text()
        if(self.formLayout_4.itemAt(i).widget().text() == status):
          self.statStatus = self.formLayout_4.itemAt(i).widget().isChecked()
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

    def calclicked(self):
        self.dateEdit_3.setDate(self.calendarWidget.selectedDate())
        self.fill_labels1((self.calendarWidget.selectedDate()))
        self.calendarWidget.hide() 
    
    def calclicked2(self):
        #print "about to clear lists"

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
          #print "rangeForSelectedDate"
          #for date in rangeForSelectedDate:
            #print date
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
          #print "rangeForSelectedDate"
          #for date in rangeForSelectedDate:
            #print date
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
          #print "rangeForSelectedDate"
          #for date in rangeForSelectedDate:
            #print date
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
          #print "rangeForSelectedDate"
          #for date in rangeForSelectedDate:
            #print date
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
          #print "rangeForSelectedDate"
          #for date in rangeForSelectedDate:
            #print date
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
          #print "rangeForSelectedDate"
          #for date in rangeForSelectedDate:
            #print date
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
          #print "rangeForSelectedDate"
          #for date in rangeForSelectedDate:
            #print date

        for date in rangeForSelectedDate:
          #print "date "+str(date)
          dow = date.weekday()
          #print "day of the week"+str(date.weekday())
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
                  putMeInList.setBackgroundColor(QtGui.QColor(int(color[1]),int(color[2]),int(color[3]),255-(alphaValue*255)))
                  self.listWidget_5.addItem(putMeInList)
              elif(dayOfWeek == 1):#listWidget_6 tuesday
                if (date <= endDate and date >= startDate ):
                  #print "startDate: "+ startDate.__repr__()
                  #print "date: "+selectedDate.__repr__()
                  #print "endDate: "+endDate.__repr__()
                  putMeInList = QtGui.QListWidgetItem(self.listWidget_6)
                  #putMeInList.setWordWrap(True)
                  putMeInList.setText(record[0].isoformat()+"\n"+record[1].isoformat()+"\n"+record[2]+"\n"+record[3]+"\n"+record[4]+"\n"+record[5])
                  putMeInList.setBackgroundColor(QtGui.QColor(int(color[1]),int(color[2]),int(color[3]),255-(alphaValue*255)))
                  self.listWidget_6.addItem(putMeInList)
              elif(dayOfWeek == 2):#listWidget_4 wednesday
                if (date <= endDate and date >= startDate ):
                  #print "startDate: "+ startDate.__repr__()
                  #print "date: "+selectedDate.__repr__()
                  #print "endDate: "+endDate.__repr__()
                  putMeInList = QtGui.QListWidgetItem(self.listWidget_4)
                  #putMeInList.setWordWrap(True)
                  putMeInList.setText(record[0].isoformat()+"\n"+record[1].isoformat()+"\n"+record[2]+"\n"+record[3]+"\n"+record[4]+"\n"+record[5])
                  putMeInList.setBackgroundColor(QtGui.QColor(int(color[1]),int(color[2]),int(color[3]),255-(alphaValue*255)))
                  self.listWidget_4.addItem(putMeInList)
              elif(dayOfWeek == 3):#listWidget_3 thursday
                if (date <= endDate and date >= startDate ):
                  #print "startDate: "+ startDate.__repr__()
                  #print "date: "+selectedDate.__repr__()
                  #print "endDate: "+endDate.__repr__()
                  putMeInList = QtGui.QListWidgetItem(self.listWidget_3)
                  #putMeInList.setWordWrap(True)
                  putMeInList.setText(record[0].isoformat()+"\n"+record[1].isoformat()+"\n"+record[2]+"\n"+record[3]+"\n"+record[4]+"\n"+record[5])
                  putMeInList.setBackgroundColor(QtGui.QColor(int(color[1]),int(color[2]),int(color[3]),255-(alphaValue*255)))
                  self.listWidget_3.addItem(putMeInList)
              elif(dayOfWeek == 4):#listWidget friday
                if (date <= endDate and date >= startDate ):
                  #print "startDate: "+ startDate.__repr__()
                  #print "date: "+selectedDate.__repr__()
                  #print "endDate: "+endDate.__repr__()
                  putMeInList = QtGui.QListWidgetItem(self.listWidget)
                  #putMeInList.setWordWrap(True)
                  putMeInList.setText(record[0].isoformat()+"\n"+record[1].isoformat()+"\n"+record[2]+"\n"+record[3]+"\n"+record[4]+"\n"+record[5])
                  putMeInList.setBackgroundColor(QtGui.QColor(int(color[1]),int(color[2]),int(color[3]),255-(alphaValue*255)))
                  self.listWidget.addItem(putMeInList)
              elif(dayOfWeek == 5):#listWidget_8 saturday
                if (date <= endDate and date >= startDate ):
                  #print "startDate: "+ startDate.__repr__()
                  #print "date: "+selectedDate.__repr__()
                  #print "endDate: "+endDate.__repr__()
                  putMeInList = QtGui.QListWidgetItem(self.listWidget_8)
                  #putMeInList.setWordWrap(True)                  
                  putMeInList.setText(record[0].isoformat()+"\n"+record[1].isoformat()+"\n"+record[2]+"\n"+record[3]+"\n"+record[4]+"\n"+record[5])
                  putMeInList.setBackgroundColor(QtGui.QColor(int(color[1]),int(color[2]),int(color[3]),255-(alphaValue*255)))
                  self.listWidget_8.addItem(putMeInList)
              elif(dayOfWeek == 6):#listWidget_2 sunday
                if (date <= endDate and date >= startDate ):
                  #print "startDate: "+ startDate.__repr__()
                  #print "date: "+selectedDate.__repr__()
                  #print "endDate: "+endDate.__repr__()
                  putMeInList = QtGui.QListWidgetItem(self.listWidget_2)
                  #putMeInList.setWordWrap(True)
                  putMeInList.setText(record[0].isoformat()+"\n"+record[1].isoformat()+"\n"+record[2]+"\n"+record[3]+"\n"+record[4]+"\n"+record[5])
                  putMeInList.setBackgroundColor(QtGui.QColor(int(color[1]),int(color[2]),int(color[3]),255-(alphaValue*255)))
                  self.listWidget_2.addItem(putMeInList)
            #listWidget_2 == Sunday
    #listWidget_5 == Monday
    #listWidget_6 == Tuesday
    #listWidget_4 == Wednesday
    #listWidget_3 == Thursday
    #listWidget == Friday
    #listWidget_8 == Saturday
   
    def calclicked3(self):
        self.listWidget_4.clear()
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
#<<<<<<< HEAD:testing/Noah/pycalendar.py
                #print "MADE IT PAST CHECKEMP"
                #print "color "+str(color)
#=======
              #print "MADE IT PAST CHECKEMP"
              #print "color "+str(color)
#>>>>>>> 59a5cea1287bb21d6dea58be210c384e80fa0a7a:testing/calendar_nowstretches.py
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
                putMeInList.setBackgroundColor(QtGui.QColor(int(color[1]),int(color[2]),int(color[3]),255-(alphaValue*255)))
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
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(500, 500))
        MainWindow.setMaximumSize(QtCore.QSize(5000, 5000))
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
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.pushButton_2 = QtGui.QPushButton(self.frame_2)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.verticalLayout_2.addWidget(self.pushButton_2)
        self.pushButton_3 = QtGui.QPushButton(self.frame_2)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.verticalLayout_2.addWidget(self.pushButton_3)
        self.pushButton = QtGui.QPushButton(self.frame_2)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.verticalLayout_2.addWidget(self.pushButton)
        self.label_22 = QtGui.QLabel(self.frame_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_22.sizePolicy().hasHeightForWidth())
        self.label_22.setSizePolicy(sizePolicy)
        self.label_22.setMinimumSize(QtCore.QSize(171, 91))
        self.label_22.setMaximumSize(QtCore.QSize(171, 91))
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.verticalLayout_2.addWidget(self.label_22)
        self.verticalLayout.addWidget(self.frame_2)
        self.toolBox = QtGui.QToolBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolBox.sizePolicy().hasHeightForWidth())
        self.toolBox.setSizePolicy(sizePolicy)
        self.toolBox.setMinimumSize(QtCore.QSize(200, 600))
        self.toolBox.setAutoFillBackground(False)
        self.toolBox.setObjectName(_fromUtf8("toolBox"))
        self.page_3 = QtGui.QWidget()
        self.page_3.setGeometry(QtCore.QRect(0, 0, 190, 552))
        self.page_3.setObjectName(_fromUtf8("page_3"))
        self.formLayoutWidget = QtGui.QWidget(self.page_3)
        self.formLayoutWidget.setGeometry(QtCore.QRect(0, 0, 185, 512))
        self.formLayoutWidget.setObjectName(_fromUtf8("formLayoutWidget"))
        self.formLayout = QtGui.QFormLayout(self.formLayoutWidget)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.ExpandingFieldsGrow)
        self.formLayout.setMargin(0)
        self.formLayout.setVerticalSpacing(2)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.scrollArea = QtGui.QScrollArea(self.formLayoutWidget)
        self.scrollArea.setMinimumSize(QtCore.QSize(183, 510))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 177, 504))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.formLayout_3 = QtGui.QFormLayout(self.scrollAreaWidgetContents)
        self.formLayout_3.setObjectName(_fromUtf8("formLayout_3"))
        #self.checkBox_2 = QtGui.QCheckBox(self.scrollAreaWidgetContents)
        #self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        #self.formLayout_3.setWidget(0, QtGui.QFormLayout.LabelRole, self.checkBox_2)
        #self.checkBox = QtGui.QCheckBox(self.scrollAreaWidgetContents)
        #self.checkBox.setObjectName(_fromUtf8("checkBox"))
        #self.formLayout_3.setWidget(1, QtGui.QFormLayout.LabelRole, self.checkBox)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.formLayout.setWidget(0, QtGui.QFormLayout.SpanningRole, self.scrollArea)
        self.toolBox.addItem(self.page_3, _fromUtf8(""))
        self.page_4 = QtGui.QWidget()
        self.page_4.setGeometry(QtCore.QRect(0, 0, 190, 552))
        self.page_4.setObjectName(_fromUtf8("page_4"))
        self.formLayoutWidget_2 = QtGui.QWidget(self.page_4)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 189, 510))
        self.formLayoutWidget_2.setObjectName(_fromUtf8("formLayoutWidget_2"))
        self.formLayout_2 = QtGui.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setMargin(0)
        self.formLayout_2.setVerticalSpacing(2)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.scrollArea_2 = QtGui.QScrollArea(self.formLayoutWidget_2)
        self.scrollArea_2.setMinimumSize(QtCore.QSize(183, 515))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName(_fromUtf8("scrollArea_2"))
        self.scrollAreaWidgetContents_2 = QtGui.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 177, 510))
        self.scrollAreaWidgetContents_2.setObjectName(_fromUtf8("scrollAreaWidgetContents_2"))
        self.formLayout_4 = QtGui.QFormLayout(self.scrollAreaWidgetContents_2)
        self.formLayout_4.setObjectName(_fromUtf8("formLayout_4"))
        #self.checkBox_4 = QtGui.QCheckBox(self.scrollAreaWidgetContents_2)
        #self.checkBox_4.setObjectName(_fromUtf8("checkBox_4"))
        #self.formLayout_4.setWidget(0, QtGui.QFormLayout.LabelRole, self.checkBox_4)
        #self.checkBox_3 = QtGui.QCheckBox(self.scrollAreaWidgetContents_2)
        #self.checkBox_3.setObjectName(_fromUtf8("checkBox_3"))
        #self.formLayout_4.setWidget(1, QtGui.QFormLayout.LabelRole, self.checkBox_3)
        #self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.scrollArea_2)
        self.toolBox.addItem(self.page_4, _fromUtf8(""))
        self.verticalLayout.addWidget(self.toolBox)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.gridLayout_2 = QtGui.QGridLayout(self.tab)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setSpacing(1)
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.listWidget_16 = QtGui.QListWidget(self.tab)
        self.listWidget_16.setObjectName(_fromUtf8("listWidget_16"))
        self.horizontalLayout_8.addWidget(self.listWidget_16)
        self.listWidget_17 = QtGui.QListWidget(self.tab)
        self.listWidget_17.setObjectName(_fromUtf8("listWidget_17"))
        self.horizontalLayout_8.addWidget(self.listWidget_17)
        self.listWidget_18 = QtGui.QListWidget(self.tab)
        self.listWidget_18.setObjectName(_fromUtf8("listWidget_18"))
        self.horizontalLayout_8.addWidget(self.listWidget_18)
        self.listWidget_19 = QtGui.QListWidget(self.tab)
        self.listWidget_19.setObjectName(_fromUtf8("listWidget_19"))
        self.horizontalLayout_8.addWidget(self.listWidget_19)
        self.listWidget_20 = QtGui.QListWidget(self.tab)
        self.listWidget_20.setObjectName(_fromUtf8("listWidget_20"))
        self.horizontalLayout_8.addWidget(self.listWidget_20)
        self.listWidget_21 = QtGui.QListWidget(self.tab)
        self.listWidget_21.setObjectName(_fromUtf8("listWidget_21"))
        self.horizontalLayout_8.addWidget(self.listWidget_21)
        self.listWidget_22 = QtGui.QListWidget(self.tab)
        self.listWidget_22.setObjectName(_fromUtf8("listWidget_22"))
        self.horizontalLayout_8.addWidget(self.listWidget_22)
        self.gridLayout_2.addLayout(self.horizontalLayout_8, 8, 0, 1, 3)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_8 = QtGui.QLabel(self.tab)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.horizontalLayout_5.addWidget(self.label_8)
        self.label_9 = QtGui.QLabel(self.tab)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.horizontalLayout_5.addWidget(self.label_9)
        self.label_10 = QtGui.QLabel(self.tab)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.horizontalLayout_5.addWidget(self.label_10)
        self.label_11 = QtGui.QLabel(self.tab)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.horizontalLayout_5.addWidget(self.label_11)
        self.label_12 = QtGui.QLabel(self.tab)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.horizontalLayout_5.addWidget(self.label_12)
        self.label_13 = QtGui.QLabel(self.tab)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.horizontalLayout_5.addWidget(self.label_13)
        self.label_14 = QtGui.QLabel(self.tab)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.horizontalLayout_5.addWidget(self.label_14)
        self.gridLayout_2.addLayout(self.horizontalLayout_5, 5, 0, 1, 3)
        spacerItem = QtGui.QSpacerItem(380, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 4, 0, 1, 1)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_15 = QtGui.QLabel(self.tab)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.horizontalLayout_6.addWidget(self.label_15)
        self.label_16 = QtGui.QLabel(self.tab)
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.horizontalLayout_6.addWidget(self.label_16)
        self.label_17 = QtGui.QLabel(self.tab)
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.horizontalLayout_6.addWidget(self.label_17)
        self.label_18 = QtGui.QLabel(self.tab)
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.horizontalLayout_6.addWidget(self.label_18)
        self.label_19 = QtGui.QLabel(self.tab)
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.horizontalLayout_6.addWidget(self.label_19)
        self.label_20 = QtGui.QLabel(self.tab)
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.horizontalLayout_6.addWidget(self.label_20)
        self.label_21 = QtGui.QLabel(self.tab)
        self.label_21.setAlignment(QtCore.Qt.AlignCenter)
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.horizontalLayout_6.addWidget(self.label_21)
        self.gridLayout_2.addLayout(self.horizontalLayout_6, 7, 0, 1, 3)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setSpacing(1)
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.listWidget_9 = QtGui.QListWidget(self.tab)
        self.listWidget_9.setObjectName(_fromUtf8("listWidget_9"))
        self.horizontalLayout_7.addWidget(self.listWidget_9)
        self.listWidget_10 = QtGui.QListWidget(self.tab)
        self.listWidget_10.setObjectName(_fromUtf8("listWidget_10"))
        self.horizontalLayout_7.addWidget(self.listWidget_10)
        self.listWidget_11 = QtGui.QListWidget(self.tab)
        self.listWidget_11.setObjectName(_fromUtf8("listWidget_11"))
        self.horizontalLayout_7.addWidget(self.listWidget_11)
        self.listWidget_12 = QtGui.QListWidget(self.tab)
        self.listWidget_12.setObjectName(_fromUtf8("listWidget_12"))
        self.horizontalLayout_7.addWidget(self.listWidget_12)
        self.listWidget_13 = QtGui.QListWidget(self.tab)
        self.listWidget_13.setObjectName(_fromUtf8("listWidget_13"))
        self.horizontalLayout_7.addWidget(self.listWidget_13)
        self.listWidget_14 = QtGui.QListWidget(self.tab)
        self.listWidget_14.setObjectName(_fromUtf8("listWidget_14"))
        self.horizontalLayout_7.addWidget(self.listWidget_14)
        self.listWidget_15 = QtGui.QListWidget(self.tab)
        self.listWidget_15.setObjectName(_fromUtf8("listWidget_15"))
        self.horizontalLayout_7.addWidget(self.listWidget_15)
        self.gridLayout_2.addLayout(self.horizontalLayout_7, 6, 0, 1, 3)
        self.dateEdit_3 = QtGui.QDateEdit(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dateEdit_3.sizePolicy().hasHeightForWidth())
        self.dateEdit_3.setSizePolicy(sizePolicy)
        self.dateEdit_3.setMinimumSize(QtCore.QSize(140, 25))
        self.dateEdit_3.setMaximumSize(QtCore.QSize(100, 20))
        self.dateEdit_3.setObjectName(_fromUtf8("dateEdit_3"))
        self.gridLayout_2.addWidget(self.dateEdit_3, 4, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 4, 2, 1, 1)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.gridLayout_3 = QtGui.QGridLayout(self.tab_2)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        spacerItem2 = QtGui.QSpacerItem(399, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem2, 0, 0, 1, 1)
        self.dateEdit_2 = QtGui.QDateEdit(self.tab_2)
        self.dateEdit_2.setObjectName(_fromUtf8("dateEdit_2"))
        self.gridLayout_3.addWidget(self.dateEdit_2, 0, 1, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(400, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem3, 0, 2, 1, 1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_7 = QtGui.QLabel(self.tab_2)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_3.addWidget(self.label_7)
        self.label_6 = QtGui.QLabel(self.tab_2)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_3.addWidget(self.label_6)
        self.label_5 = QtGui.QLabel(self.tab_2)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_3.addWidget(self.label_5)
        self.label_4 = QtGui.QLabel(self.tab_2)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_3.addWidget(self.label_4)
        self.label_3 = QtGui.QLabel(self.tab_2)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_3.addWidget(self.label_3)
        self.label_2 = QtGui.QLabel(self.tab_2)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_3.addWidget(self.label_2)
        self.label = QtGui.QLabel(self.tab_2)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_3.addWidget(self.label)
        self.gridLayout_3.addLayout(self.horizontalLayout_3, 1, 0, 1, 3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(1)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.listWidget_2 = QtGui.QListWidget(self.tab_2)
        self.listWidget_2.setObjectName(_fromUtf8("listWidget_2"))
        self.horizontalLayout_4.addWidget(self.listWidget_2)
        self.listWidget_5 = QtGui.QListWidget(self.tab_2)
        self.listWidget_5.setObjectName(_fromUtf8("listWidget_5"))
        self.horizontalLayout_4.addWidget(self.listWidget_5)
        self.listWidget_6 = QtGui.QListWidget(self.tab_2)
        self.listWidget_6.setObjectName(_fromUtf8("listWidget_6"))
        self.horizontalLayout_4.addWidget(self.listWidget_6)
        self.listWidget_4 = QtGui.QListWidget(self.tab_2)
        self.listWidget_4.setObjectName(_fromUtf8("listWidget_4"))
        self.horizontalLayout_4.addWidget(self.listWidget_4)
        self.listWidget_3 = QtGui.QListWidget(self.tab_2)
        self.listWidget_3.setObjectName(_fromUtf8("listWidget_3"))
        self.horizontalLayout_4.addWidget(self.listWidget_3)
        self.listWidget = QtGui.QListWidget(self.tab_2)
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.horizontalLayout_4.addWidget(self.listWidget)
        self.listWidget_8 = QtGui.QListWidget(self.tab_2)
        self.listWidget_8.setObjectName(_fromUtf8("listWidget_8"))
        self.horizontalLayout_4.addWidget(self.listWidget_8)
        self.gridLayout_3.addLayout(self.horizontalLayout_4, 2, 0, 1, 3)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.gridLayout_4 = QtGui.QGridLayout(self.tab_3)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        spacerItem4 = QtGui.QSpacerItem(404, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem4, 0, 0, 1, 1)
        self.dateEdit = QtGui.QDateEdit(self.tab_3)
        self.dateEdit.setObjectName(_fromUtf8("dateEdit"))
        self.gridLayout_4.addWidget(self.dateEdit, 0, 1, 1, 1)
        spacerItem5 = QtGui.QSpacerItem(395, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem5, 0, 2, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(1)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.listWidget_7 = QtGui.QListWidget(self.tab_3)
        self.listWidget_7.setObjectName(_fromUtf8("listWidget_7"))
        self.listWidget_7.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.listWidget_7.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.horizontalLayout_2.addWidget(self.listWidget_7)
        self.gridLayout_4.addLayout(self.horizontalLayout_2, 1, 0, 1, 3)
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.gridLayout.addWidget(self.tabWidget, 1, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1123, 21))
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
        self.actionRemStat = QtGui.QAction(MainWindow)
        self.actionContact = QtGui.QAction(MainWindow)
        self.actionContact.setObjectName(_fromUtf8("actionContact"))
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.menuFile.addAction(self.actionRemEmp)
        self.menuFile.addAction(self.actionRemStat)
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionContact)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.calendarWidget = QtGui.QCalendarWidget(self.tab)
        self.calendarWidget.setGeometry(QtCore.QRect(310, 40, 300, 165))
        self.calendarWidget.setGridVisible(False)
        self.calendarWidget.setNavigationBarVisible(True)
        self.calendarWidget.setObjectName(_fromUtf8("calendarWidget"))
        self.calendarWidget.hide()
        self.calendarWidget_2 = QtGui.QCalendarWidget(self.tab_2)
        self.calendarWidget_2.setGeometry(QtCore.QRect(310, 40, 300, 165))
        self.calendarWidget_2.setObjectName(_fromUtf8("calendarWidget_2"))
        self.calendarWidget_2.hide()
        self.calendarWidget_3 = QtGui.QCalendarWidget(self.tab_3)
        self.calendarWidget_3.setGeometry(QtCore.QRect(310,40,300,165))
        self.calendarWidget_3.setObjectName(_fromUtf8("calendarWidget_3"))
        self.calendarWidget_3.hide()
        self.retranslateUi(MainWindow)
        self.toolBox.setCurrentIndex(1)
        self.tabWidget.setCurrentIndex(0)
        self.label_22.setAlignment(QtCore.Qt.AlignCenter)
        self.populateCheckboxes()
        myPixmap = QtGui.QPixmap(_fromUtf8('./data/Clemson_nobg.png'))
        myScaledPixmap = myPixmap.scaled(self.label_22.size(), QtCore.Qt.KeepAspectRatio)
        self.label_22.setPixmap(myScaledPixmap)
        self.listWidget_7.customContextMenuRequested.connect(self.openMenu)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.updateRecordsClicked)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.addEmpClicked)
        QtCore.QObject.connect(self.pushButton_3, QtCore.SIGNAL(_fromUtf8("clicked()")), self.addStatClicked)
        QtCore.QObject.connect(self.dateEdit_3, QtCore.SIGNAL(_fromUtf8("dateChanged(QDate)")), self.calendarWidget.show) #right
        QtCore.QObject.connect(self.dateEdit_2, QtCore.SIGNAL(_fromUtf8("dateChanged(QDate)")), self.calendarWidget_2.show)
        QtCore.QObject.connect(self.dateEdit, QtCore.SIGNAL(_fromUtf8("dateChanged(QDate)")), self.calendarWidget_3.show)
        QtCore.QObject.connect(self.calendarWidget, QtCore.SIGNAL(_fromUtf8("clicked(QDate)")), self.calclicked)
        QtCore.QObject.connect(self.calendarWidget_2, QtCore.SIGNAL(_fromUtf8("clicked(QDate)")), self.calclicked2  )
        QtCore.QObject.connect(self.calendarWidget_3, QtCore.SIGNAL(_fromUtf8("clicked(QDate)")), self.calclicked3)
        QtCore.QObject.connect(self.actionExit, QtCore.SIGNAL(_fromUtf8("activated()")), sys.exit)
        QtCore.QObject.connect(self.actionRemEmp, QtCore.SIGNAL(_fromUtf8("activated()")), self.remEmpClicked)
        QtCore.QObject.connect(self.actionRemStat, QtCore.SIGNAL(_fromUtf8("activated()")), self.remStatClicked)          
        QtCore.QObject.connect(self.actionContact, QtCore.SIGNAL(_fromUtf8("activated()")), self.contactClicked)
        QtCore.QObject.connect(self.actionAbout, QtCore.SIGNAL(_fromUtf8("activated()")), self.aboutClicked) 
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        today = QtCore.QDate.currentDate()
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.pushButton_2.setText(_translate("MainWindow", "Add Employee", None))
        self.pushButton_3.setText(_translate("MainWindow", "Add Status", None))
        self.pushButton.setText(_translate("MainWindow", "Update", None))
        #self.label_22.setText(_translate("MainWindow", "Banner Goes Here", None))
        #self.checkBox_2.setText(_translate("MainWindow", "CheckBox", None))
        #self.checkBox.setText(_translate("MainWindow", "CheckBox", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_3), _translate("MainWindow", "Employees", None))
        #self.checkBox_4.setText(_translate("MainWindow", "CheckBox", None))
        #self.checkBox_3.setText(_translate("MainWindow", "CheckBox", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_4), _translate("MainWindow", "Project Statuses", None))
        self.dateEdit.setDate(today)
        self.dateEdit_2.setDate(today)
        self.dateEdit_3.setDate(today)
        self.fill_labels1(today)
        self.fill_labels2(today)
        self.dateEdit_3.setDisplayFormat(_translate("MainWindow", "d MMMM yyyy", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Bi-Weekly", None))
        self.dateEdit_2.setDisplayFormat(_translate("MainWindow", "d MMMM yyyy", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Weekly", None))
        self.dateEdit.setDisplayFormat(_translate("MainWindow", "d MMMM yyyy", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Daily", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))
        self.actionRemEmp.setText(_translate("MainWindow", "Remove Employee", None))
        self.actionRemStat.setText(_translate("MainWindow", "Remove Status", None))
        self.actionContact.setText(_translate("MainWindow", "Contact", None))
        self.actionAbout.setText(_translate("MainWindow", "About", None))


if __name__ == "__main__":
    import sys
    timerProc = subprocess.Popen(["python","timer.py"],stdout=subprocess.PIPE,shell=False,preexec_fn=os.setsid)
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
    atexit.register(ui.goodbye,timerProc)
    sys.exit(app.exec_())
