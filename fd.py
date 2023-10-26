import cv2
import numpy as np
import matplotlib.pyplot as plt
def persepectivetransform(p):
    trap=np.float32([(0,488),(0,700),(1023,488),(1023,700)]);
    pts=np.float32([(0,0),(0,480),(640,0),(640,480)]);
    matrix=cv2.getPerspectiveTransform(trap,pts);
    mat=cv2.warpPerspective(p,matrix,(640,480));
    return mat;

def edgedetection(frame):
    a=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY);
    cv2.imshow("G",frame);
    cv2.imshow("Mango",a);
    lower=np.array([10,150,240], dtype = "uint8");
    upper=np.array([100,255,255], dtype="uint8");
    frame2=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV);
    cv2.imshow("Bango",frame2);
    maskwhite=cv2.inRange(a,200,255);cv2.imshow("Tango",maskwhite);
    maskyellow=cv2.inRange(frame2,lower,upper);cv2.imshow("Zango",maskyellow);
    maskall=cv2.bitwise_or(maskwhite,maskyellow);cv2.imshow("kango",maskall);
    maskfinal=cv2.bitwise_and(a,maskall);cv2.imshow("Pandgo",maskfinal);
    j=cv2.GaussianBlur(maskfinal,(5,5),0);
    cv2.waitKey(0);
    j1=cv2.Canny(j,50,150);
    return j1;

def regionofinterest(frame):
    return frame;

p=cv2.imread("R.JPG");
j1=edgedetection(p);
j2=persepectivetransform(j1);
cv2.imshow("CAN",j2);
cv2.imshow("MAN",j1);
plt.imshow(p);
plt.show();
#cv2.imshow("nig",mat);
cv2.waitKey(0);
cv2.destroyAllWindows();