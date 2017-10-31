from PIL import Image
import os
import sys
from PIL import ImageGrab
import time
import numpy as np
import cv2

from PyQt4.QtGui import QPixmap, QApplication
app = QApplication(sys.argv)

fps = 15
time_to_record = 25
time_start = time.clock()
fourcc = cv2.VideoWriter_fourcc('i','Y','U', 'V')
writer = cv2.VideoWriter('output.avi',fourcc, fps, (1366,768),1)

def convertQImageToMat(incomingImage):
    '''  Converts a QImage into an opencv MAT format  '''

    incomingImage = incomingImage.convertToFormat(4)

    width = incomingImage.width()
    height = incomingImage.height()

    ptr = incomingImage.bits()
    ptr.setsize(incomingImage.byteCount())
    arr = np.array(ptr).reshape(height, width, 4)  #  Copies the data
    return arr

print (time.clock()-time_start)
print time_to_record
i =1
img=[]
while (time.clock()-time_start)<time_to_record*1.5+1:
    directory = "C:\Users\Madhavan Seshadri\Desktop"
    #img = ImageGrab.grab()
    img.append(QPixmap.grabWindow(QApplication.desktop().winId()))
    time.sleep(1.0/fps-0.01)
    i+=1

print img
for j in range(1,i):
    qimg = img.pop(j-i).toImage()
    imgarr = convertQImageToMat(qimg)#np.array(qimg.getdata(),dtype="uint8").reshape((qimg.size[1],qimg.size[0],3))#np.ndarray(shape=qimg.size(), dtype="uint8", buffer=qimg.bits())
    #printscreen_numpy =   np.array(img.getdata(),dtype="uint8").reshape((img.size[1],img.size[0],3))
    #save_name = os.path.join(directory,"Screenshot.jpg")
    #img.save(save_name)
    #print time.clock()-time_start
    writer.write(imgarr)
