import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.conditions import IfCondition, UnlessCondition
from launch.substitutions import Command, LaunchConfiguration
from launch.actions import DeclareLaunchArgument, ExecuteProcess
from launch_ros.parameter_descriptions import ParameterValue
from launch_ros.actions import Node

def generate_launch_description():

    use_gui_arg = DeclareLaunchArgument(name='use_gui', default_value='true', choices=['true', 'false'],
                                    description='Whether to run joint_state_publisher_gui or not.')

    display_model = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        parameters=[{
            'robot_description': ParameterValue(
                                    Command(['xacro ', os.path.join(get_package_share_directory('lwr_description'), 'model', 'kuka_lwr.urdf.xacro') ]),
                                      value_type=str)
        }]
        )

    run_rviz = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='screen',
        arguments=['-d', os.path.join(get_package_share_directory('lwr_description'), 'rviz', 'lwr_config.rviz')]
        )

    joint_state_publisher_gui = Node(
        package='joint_state_publisher_gui',
        executable='joint_state_publisher_gui',
        name='joint_state_publisher_gui',
        condition = IfCondition(LaunchConfiguration('use_gui'))
        )
    
    # If we don't use joint_state_publisher_gui, we need to publish sensor_msgs/msg/JointState message at least once so that the manipulator model shows up in RViz. 
    joint_states_cmd = ExecuteProcess(
        cmd=[[
            'ros2 topic pub ',
            '/joint_states ',
            'sensor_msgs/msg/JointState ',
            '"{header: auto, name: ["Joint_1", "Joint_2", "Joint_3", "Joint_4", "Joint_5", "Joint_6", "Joint_7"],'
            ' position: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]}" ',
            '--once'
            ]],
        shell=True,
        condition=UnlessCondition(LaunchConfiguration('use_gui'))
        )

    return LaunchDescription([
        use_gui_arg,
        display_model,
        run_rviz,
        joint_state_publisher_gui,
        joint_states_cmd
    ])