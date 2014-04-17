import os, time
import threading,ctypes

#this class is responsible for monitoring the remote data file in order to provide the user with a timely
#notification when a change has been made to the remote data file.
#it is called via a thread from pycalendar and runs until it receives sigterm.
#still some vestiges of previous QThread solution in this class.

class CalTimer(threading.Thread):
 
  xml_file = './data/data.xml'
  fileSize = os.stat(xml_file)

  def __init__(self,ui):
    threading.Thread.__init__(self)
    self.view = ui
    self.initFileSize()
    self.updateTimer()

  def initFileSize(self):
    fileToCheck = os.stat(self.xml_file)
    self.fileSize = fileToCheck.st_size

  def stop(self):
    self.join()
    sys.exit()

  def checkFileSize(self, filename, oldSize):
    needsUpdate = False
    checkedFile = os.stat(filename)
    checkSize = checkedFile.st_size
    if not(checkSize == oldSize):
        #print "returns true - update needed"
        needsUpdate = True
        self.view.pushButton.setText("UPDATE NEEDED")  #pushbutton text that is modified.
        self.initFileSize()
    #else:
    #    print "returns false - no update needed"
    return needsUpdate

  def updateTimer(self):
    t0 = time.time()
    while not (time.time() - t0 >= 5):
      time.sleep(1)
    else:
      self.checkFileSize(self.xml_file, self.fileSize)
      self.updateTimer()

  def test(self):
    print 'blah'


if __name__ == "__main__":

  A = CalTimer()

  A.updateTimer()
