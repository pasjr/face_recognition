###############################################################################
# file: facerec_ltk.py                                                        #
# author: Pedro Adolfo de Souza Junior                                        #
# brief: This file include the source code to handle the frames captures from #
#        device camera and send it to face manager module when the frame has  #
#        a face present.                                                      #
###############################################################################
import face_recognition
import cv2
import datetime
import time
from interfaces.QueueLtk import QueueLtk

# Start capture from webcam (dev/video0)
video_capture = cv2.VideoCapture(0)
if (video_capture.isOpened()):
    print("Video capture start")

# Start Queue
q = QueueLtk()

while True:
    # Get frame from capture
    ret, frame = video_capture.read()

    # Find all the faces in frame
    # [TODO-JR] - Test model "cnn" --> face_locations(face, 1, model="cnn")
    face_locations = face_recognition.face_locations(frame)

    # [TODO-JR] Move 'prints' to a log class
    ts = datetime.datetime.now().timestamp()
    ts_h = datetime.datetime.fromtimestamp(ts).isoformat()

    if(len(face_locations) == 1):
        print("{}: I found 1 face in this frame and send it to queue.".format(ts_h))
        q.enqueue(frame)
    else:
        print("{}: I found {} face(s) in this photograph.".format(ts_h,
        len(face_locations)))

    # Check frame queue
    if(q.isEmpty() == False):
        print(q.dequeue())

    # time.sleep(0.1)
    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release webcam
video_capture.release()
