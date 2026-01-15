#!/usr/bin/env python3

#interpreter line used to tell the interpreter that its using the python interpreter


import rclpy #python library for ROS2 Communication
from rclpy.node import Node

class MyNode(Node): #defined a class called my node that inherits the functionalities of the Node class from the rclpy library
    def __init__ (self):
        super().__init__("first_node") # here we provide the node name that we will use in the graph
        self.create_timer(1.0,self.timer_callback)

    def timer_callback(self):
        self.get_logger().info("Hello")
def main(args=None):
    rclpy.init(args=args) # initializing ros2 communication  args= the args from the main function 
    node=MyNode() #creating an instance of the node
    rclpy.spin(node) #spin make the node continue to run until i kill it manually in the terminal


    rclpy.shutdown() # stop the ROS2 communication



if __name__=='__main__':

    main()





# In the main function we
# first initialiW ROS2 communication    
# everything we should write anout the node behaviour should be between the rclpy.init and rclpy.shutdown commands
# to create a node we use oop by creating a class for the node that inherits the nodes behaviour