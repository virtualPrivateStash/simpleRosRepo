#!/usr/bin/python
import os
import rospy

def main():
	global pub
	print("this is node argpack (argNode.py)")
    #rospy.init_node('Image_Processing', anonymous=True)
    #camtopic = 'Camera/Cam_Frame'

	
	
	
	if rospy.has_param('Image_processing/Cam_topic') :
		camtopic = rospy.get_param('Image_processing/Cam_topic')
    
    
	if rospy.has_param('ArgNode/cam_image_topic'):
		camtopic = rospy.get_param('ArgNode/cam_image_topic')
		print(camtopic)
		print("camtopic ist vorhanden")
    
		rospy.Service('ArgNode/GetState', GetState, get_state)
		rospy.Service('ArgNode/SetState', SetState, set_state)
		rospy.Service('ArgNode/GetWorkspace', GetWorkspace, get_workspace)

    #image_sub = rospy.Subscriber(camtopic, Image, cam_callback)

    #pub = rospy.Publisher('Image_Processing/raw_coord',String,queue_size=10)
    #rospy.spin()


if __name__ == "__main__":
    main()
