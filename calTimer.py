import os, time
import threading,ctypes

class CalTimer(threading.Thread):
 
  xml_file = './data/data.xml'
  fileSize = os.stat(xml_file)

  def __init__(self,ui):
    threading.Thread.__init__(self)
    #print "Started calTimer thread"
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
        self.view.pushButton.setText("UPDATE NEEDED")
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
