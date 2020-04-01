#!/usr/bin/env python

import sys
import rospy
from geometry_msgs.msg import Pose, Point
from open_manipulator_msgs.srv import SetJointPosition, SetJointPositionRequest
from open_manipulator_msgs.msg import JointPosition


def moveGripper(topic, gripperPos, time):
    rospy.wait_for_service('/' +topic + '/goal_tool_control')
    try:
        SetJointSpaceGoal = rospy.ServiceProxy('/' +topic+ '/goal_tool_control', SetJointPosition)

        SetJPose=SetJointPositionRequest()
        SetJPose.planning_group = ''

        SetJPose.joint_position.joint_name = ['gripper']
        SetJPose.joint_position.position = [float(gripperPos)]
        SetJPose.path_time = float(time)

        resp = SetJointSpaceGoal(SetJPose)
        
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

def usage():
    return "%s gripperPos(-0.01 ~ +0.01) time"%sys.argv[0]

if __name__=='__main__':
    if len(sys.argv) == 4:
        topic = sys.argv[1]
        gripperPos = sys.argv[2]
        time = sys.argv[3]
    else:
        print usage()
        sys.exit(1)
    print "Gripper Opening : %s m for %s second"%(gripperPos, time)

    try:
        moveGripper(topic, gripperPos, time)
    except rospy.ROSInterruptException:
        pass
