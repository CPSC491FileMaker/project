import xml.etree.ElementTree as et
from xml.etree.ElementTree import Element
from PyQt4 import QtCore, QtGui


class Helper():

  #initiatlizes the class and prepares an XMLtree for parsing
  def __init__(self):
    self.tree = et.parse('./data/data.xml')
    self.root = self.tree.getroot()

  def write(self, filename):
    return self.tree.write(filename)

  def updateEmployee(self):
    eList = []
    allfound = []

    for employees in self.root:
      for person in employees:
  	for info in person:
  	  eList.append(info.text)
          if(len(eList) == 2):
            allfound.append(eList)
            eList = []

#    for x in allfound:
#      print x
    return allfound
 
  def updateStatus(self):
    sList = []

    for child in self.root:
      if(child.get('MODID') == '2'):
         for stat in child:
            sList.append(stat.text)

#    for x in sList:
#      print x
    return sList


  def removeEmployee(self, toRemove):

    for employees in self.root:
      for person in employees:
        for info in person:
          if (info.text == toRemove):
             employees.remove(person)
    self.write('./data/data.xml')

  def removeStatus(self, toRemove):

    proj_stats = self.root.find('Proj_statuses')
    for status in proj_stats:
      #for status in statuses:
        if (status.text == toRemove):
           proj_stats.remove(status)
    self.write('./data/data.xml')

  def addEmployee(self, eName, eColor):

    emp = Element('Person')
    kid = self.root.find('Employees')
    name = Element('Name')
    color = Element('Color')
    name.text = eName
    color.text = eColor
    emp.append(name)
    emp.append(color)
    kid.append(emp)
    self.write('./data/data.xml')
    
  def addStatus(self, sName):

    st = Element('Stat')
    st.text = sName
    kid = self.root.find('Proj_statuses')
    kid.append(st)
    self.write('./data/data.xml')

if __name__ == "__main__":

  A = Helper()
  A.updateEmployee()
  A.updateStatus()

  A.addEmployee('Walter', '0x0000FF')
  A.addStatus('Eating')
