import os
from PIL import Image
import matplotlib.pyplot as plt

NewImg=[]
lines = [line.rstrip('\n') for line in open('/home/wynmew/Documents/frame/output.txt')]
for count, line in enumerate(lines, start=1):
    #print(count, line)
    if line=='++++++++++':
        NewImg.append(count)

for count, idx in enumerate(NewImg, start=1):
    print(count, idx)
    filename = lines[idx][29:]
    print(filename)
    nameroot = filename.split(".")[0]
    inImgCounter=0
    idxNow=idx
    img = Image.open(lines[idx])
    while lines[idxNow+1] != '++++++++++':
        print(lines[idxNow+1][0:15])
        if lines[idxNow+1][1:14] == 'startposition':
            inImgCounter+=1
            coor = lines[idxNow+1][18:-1]
            coorUL=coor.split(", ")
            ULX=int(float(coorUL[0]))
            ULY=int(float(coorUL[1]))
            coor = lines[idxNow + 2][18:-1]
            coorDR = coor.split(", ")
            DRX = int(float(coorDR[0]))
            DRY = int(float(coorDR[1]))
            if DRX - ULX > 5:
                ROI = img.crop((ULX, ULY, DRX, DRY))
                ROI = ROI.resize((64, 64), Image.ANTIALIAS)
                print(ULX, ULY, DRX, DRY)
                #plt.imshow(img)
                #plt.show()
                ROI.save(os.path.join('/home/wynmew/Documents/crop', nameroot+'_'+str(inImgCounter)+'.png'))
        idxNow += 3


