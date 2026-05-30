#!/usr/bin/env python

import rospy
import sys
import tty
import termios
from geometry_msgs.msg import Twist
import select

KEY_BINDINGS = {
    'w': ( 1.0,  0.0),
    's': (-1.0,  0.0),
    'a': ( 0.0,  1.0),
    'd': ( 0.0, -1.0),
    'q': ( 1.0,  1.0),
    'e': ( 1.0, -1.0),
    'z': (-1.0,  1.0),
    'c': (-1.0, -1.0),
}

SPEED_LINEAR  = 2.0 
SPEED_ANGULAR = 2.0

def get_key():
    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        ready, _, _ = select.select([sys.stdin], [], [], 0.1)
        key = sys.stdin.read(1) if ready else ''
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old)
    return key

def main():
    # Get turtle name
    if len(sys.argv) < 2:
        print("Usage: controller.py <turtle_name>")
        sys.exit(1)

    turtle_name = sys.argv[1]

    # topic name
    topic = '/{}/cmd_vel'.format(turtle_name)

    #  ROS node and publisher
    rospy.init_node('controller_{}'.format(turtle_name), anonymous=True)
    pub = rospy.Publisher(topic, Twist, queue_size=10)
    rate = rospy.Rate(10)

    rospy.loginfo("Controlling: {}  |  topic: {}".format(turtle_name, topic))
    print("\nControls:  w/s = forward/back   a/d = turn   q/e/z/c = diagonal")
    print("Press  Ctrl+C  to quit\n")

    # Main loop
    while not rospy.is_shutdown():
        key = get_key()

        # Ctrl+C exits
        if key == '\x03':
            break

        twist = Twist()

        if key in KEY_BINDINGS:
            linear, angular = KEY_BINDINGS[key]
            twist.linear.x  = linear  * SPEED_LINEAR
            twist.angular.z = angular * SPEED_ANGULAR

        pub.publish(twist)
        rate.sleep()

    # Stop the turtle
    pub.publish(Twist())
    rospy.loginfo("Controller stopped.")

if __name__ == '__main__':
    main()
