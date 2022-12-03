#!/usr/bin/env python3
# Python libs
import sys, time
# numpy and scipy
import numpy as np
from scipy.ndimage import filters

# OpenCV
import cv2

# Ros libraries
import roslib
import rospy

# Ros Messages
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

class image_converter:

  def __init__(self):
    self.image_pub = rospy.Publisher("/image_raw",Image)

    self.bridge = CvBridge()
    self.image_sub = rospy.Subscriber("/image_raw",Image,self.callback)

  def callback(self,data):
    try:
      cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
    except CvBridgeError as e:
      print(e)

    # (rows,cols,channels) = cv_image.shape
    # if cols > 60 and rows > 60 :
    #   cv2.circle(cv_image, (50,50), 10, 255)

    grayImage = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)
    	
    (thresh, blackAndWhiteImage) = cv2.threshold(grayImage, 127, 255, cv2.THRESH_BINARY)
    cv_image = blackAndWhiteImage 

    cv2.imshow("Image window", cv_image)
    cv2.waitKey(3)

    try:
      self.image_pub.publish(self.bridge.cv2_to_imgmsg(cv_image, "bgr8"))
    except CvBridgeError as e:
      print(e)

def main(args):
  ic = image_converter()

  rospy.init_node('image_converter', anonymous=True)
  while not rospy.is_shutdown():
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("Shutting down")
  cv2.destroyAllWindows()

if __name__ == '__main__':
    main(sys.argv)

# cap = cv2.VideoCapture(0)
# bridge = CvBridge()

# def image_publish():
#     img_pub = rospy.Publisher('/image_raw', Image, queue_size=10)
#     rospy.init_node('image', anonymous=False)
#     rate = rospy.Rate(10)
#     while not rospy.is_shutdown():
#         ret, frame = cap.read()
#         if not ret:
#             break

#         msg = bridge.cv2_to_imgmsg(frame, "bgr8")
#         img_pub.publish(msg)

#         if cv2.waitkey(1) & 0xFF == ord('q'):
#             break

#         if rospy.is__shutdown():
#             cap.release()

# if __name__ == '__main__':
#     try:
#         image_publish()
#     except rospy.ROSInterruptException:
#         pass