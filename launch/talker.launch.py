from launch import LaunchDescription
from launch_ros.actions import Node

def generate_Launch_description():
    return LaunchDescription([
        Node(
            package='demo_nodes_cpp',
            executable='talker'
        )
    ])