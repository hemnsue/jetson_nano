
import cv2
window_title = "CSI Camera"
j=0
g=[]
# To flip the image, modify the flip_method parameter (0 and 2 are the most common)
video_capture = cv2.VideoCapture("nvarguscamerasrc sensor-id= 0 ! "
        "video/x-raw(memory:NVMM), width=(int)1640, height=(int)1232, framerate=(fraction)30/1 ! "
        "nvvidconv flip-method=0 ! "
        "video/x-raw, width=(int)1640, height=(int)1232, format=(string)BGRx ! "
        "videoconvert ! "
        "video/x-raw, format=(string)BGR ! appsink", cv2.CAP_GSTREAMER)
while(True):
    ret,frame_camera_input=video_capture.read()
    j+=1
    if j==42:
        g.append(frame_camera_input)  
        j=0

    cv2.imshow("Image",frame_camera_input)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
print(len(g))
video_capture.release()
cv2.destroyAllWindows()
for i in range(0,len(g)):
    x="/home/xlr8wins/xlr8-drone/CSI-Camera/calibdata/"+str(i+10)+".jpg"
    print(x,g[i])
    cv2.imwrite(x,g[i])


