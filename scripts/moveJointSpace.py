#!/usr/bin/env python

import sys
import rospy
from geometry_msgs.msg import Pose, Point
from open_manipulator_msgs.srv import SetJointPosition, SetJointPositionRequest
from open_manipulator_msgs.msg import JointPosition


def moveJointSpace(topic, joint1, joint2, joint3, joint4, time):
    rospy.wait_for_service('/' + topic + '/goal_joint_space_path')
    try:
        SetJointSpaceGoal = rospy.ServiceProxy('/' + topic + '/goal_joint_space_path', SetJointPosition)

        SetJPose=SetJointPositionRequest()
        SetJPose.planning_group = ''

        SetJPose.joint_position.joint_name = ['joint1','joint2','joint3','joint4']
        SetJPose.joint_position.position = [float(joint1), float(joint2), float(joint3), float(joint4)]
        SetJPose.path_time = float(time)

        resp = SetJointSpaceGoal(SetJPose)
        
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

def usage():
    return "%s Joint1 Joint2 Joint3 Joint4 time"%sys.argv[0]

if __name__=='__main__':
    if len(sys.argv) == 7:
        topic = sys.argv[1]
        joint1 = sys.argv[2]
        joint2 = sys.argv[3]
        joint3 = sys.argv[4]
        joint4 = sys.argv[5]
        time = sys.argv[6]
    else:
        print usage()
        sys.exit(1)
    print "Joint Space J1: %s, J2: %s, J3: %s, J4: %s, for %s second"%(joint1, joint2, joint3, joint4, time)

    try:
        moveJointSpace(topic, joint1, joint2, joint3, joint4, time)
    except rospy.ROSInterruptException:
        pass
