#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from open_manipulator_msgs.msg import OpenManipulatorState

def callback(data):
    print "open_manipulator_moving_state = %s"%data.open_manipulator_moving_state

def readMovingStat(topic):
    rospy.init_node('readMovingStat', anonymous=True)
    rospy.Subscriber("/" + topic + "/states", OpenManipulatorState, callback)
    rospy.spin()

if __name__=='__main__':

    if (len(sys.argv) == 2):
        topic = sys.argv[1]
    else:
        print usage()
        sys.exit(1)

    readMovingStat(topic)
