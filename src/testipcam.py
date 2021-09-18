import cv2

print("Before URL")
# rtsp://admin:123456@192.168.226.202:60002
url = 'rtsp://admin:123456@192.168.226.202:550/mode=real&idc=1&ids=1'
cap = cv2.VideoCapture('http://192.168.1.5:8080/video')
# print("After URL")

while True:

    # print('About to start the Read command')
    ret, frame = cap.read()
    # print('About to show frame of Video.')
    cv2.imshow("Capturing", frame)
    # print('Running..')

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
