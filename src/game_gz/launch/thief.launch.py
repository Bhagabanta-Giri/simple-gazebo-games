import os

from launch import LaunchDescription
from launch_ros.parameter_descriptions import ParameterValue
from launch.substitutions import Command

from launch_ros.actions import Node

from ament_index_python.packages import get_package_share_directory

from launch.actions import ExecuteProcess, TimerAction


def generate_launch_description():

    package_name = 'game_gz'

    config_path = os.path.join(
        get_package_share_directory(package_name),
        'config',
        'duniya_ek.config'
    )

    thief_path = os.path.join(
        get_package_share_directory(package_name),
        'urdf_thief',
        'tuktuk.xacro' 
    )

    police_path = os.path.join(
        get_package_share_directory(package_name),
        'urdf_police',
        'robot_vtwo.xacro' 
    )

    thief_description = ParameterValue(
        Command(['xacro ', thief_path]), 
        value_type=str
    )

    police_description = ParameterValue(
        Command(['xacro ', police_path]), 
        value_type=str
    )

    world_path = os.path.join(
    get_package_share_directory(package_name),
    'worlds',
    'duniya_ek.sdf'
)

    return LaunchDescription([


        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            namespace='thief',
            parameters=[{'robot_description': thief_description}],
        ),


        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            namespace='police',
            parameters=[{'robot_description': police_description}],
        ),


        Node(
            package='ros_gz_bridge',
            executable='parameter_bridge',
            arguments=[
                '/thief/cmd_vel@geometry_msgs/msg/Twist@gz.msgs.Twist',
                '/thief/camera/image@sensor_msgs/msg/Image@gz.msgs.Image',
            ],
            output='screen'
        ),


        ExecuteProcess(
            cmd=['gz', 'sim', '-r', world_path, '--gui-config', config_path],
            output='screen'
            ),


        TimerAction(
            period=3.0,
            actions=[
                ExecuteProcess(
                    cmd=[
                        'ros2', 'run', 'ros_gz_sim', 'create',
                        '-world', 'duniya_ek',
                        '-topic', '/thief/robot_description',
                        '-name', 'tuktuk',
                        '-y', '5',
                        '-z', '3',
                        '-Y', '-1.57079632679'
                    ],
                    output='screen'
                ),
                ExecuteProcess(
                    cmd=[
                        'ros2', 'run', 'ros_gz_sim', 'create',
                        '-world', 'duniya_ek',
                        '-topic', '/police/robot_description',
                        '-name', 'chitti',
                        '-y', '-5',
                        '-z', '3',
                        '-Y', '1.57079632679'
                    ],
                    output='screen'
                )
            ]
        ),
    ])