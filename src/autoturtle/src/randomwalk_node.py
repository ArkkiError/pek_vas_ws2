#! /usr/bin/python3

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import random

def callback(data):
    vel_msg = Twist()
    pose = data

    if pose.x > 10:
        vel_msg.angular.z = -5
        vel_msg.linear.x = 3
        print("Wall")

    elif pose.x < 1:
        vel_msg.angular.z = -5
        vel_msg.linear.x = 2
        print("Wall")

    elif pose.y > 10:
        vel_msg.angular.z = -5
        vel_msg.linear.x = 3
        print("Wall")

    elif pose.y < 1:
        vel_msg.angular.z = -5
        vel_msg.linear.x = 2
        print("Wall")

    else:
        # vel_msg.angular.z = 5
        # vel_msg.linear.x = 2
        vel_msg.angular.z = random.randint(-2,2)
        vel_msg.linear.x = random.randint(0,2)

    # Make so that the turtle is moving with theta direction also
    # theta: angle of the turtle
    velocity_publisher.publish(vel_msg)
    print(pose.theta)


rospy.init_node('turtlebot_auto', anonymous=True)
velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
pose_subscriber = rospy.Subscriber('/turtle1/pose', Pose, callback)

while not rospy.is_shutdown():
    rospy.spin()