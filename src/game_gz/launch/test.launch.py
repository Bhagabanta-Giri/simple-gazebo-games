import os

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.conditions import IfCondition, UnlessCondition
from launch_ros.parameter_descriptions import ParameterValue
from launch.substitutions import LaunchConfiguration, Command

from launch_ros.actions import Node

from ament_index_python.packages import get_package_share_directory

from launch.actions import ExecuteProcess, TimerAction


def generate_launch_description():

    package_name = 'game_gz'

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
    
    rviz_config_thief = os.path.join(
        get_package_share_directory(package_name),
        'rviz',
        'thief.rviz'
    )

    rviz_config_police = os.path.join(
        get_package_share_directory(package_name),
        'rviz',
        'police.rviz'
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


        DeclareLaunchArgument(
            'use_gui',
            default_value='true',
            description='Use joint_state_publisher_gui if true, else non-GUI version'
        ),


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
            package='joint_state_publisher_gui',
            executable='joint_state_publisher_gui',
            namespace='thief',
        ),


        Node(
            package='joint_state_publisher_gui',
            executable='joint_state_publisher_gui',
            namespace='police',
        ),


        Node(
            package='rviz2',
            executable='rviz2',
            arguments=['-d', rviz_config_thief],
            output='screen'
        ),


        Node(
            package='rviz2',
            executable='rviz2',
            arguments=['-d', rviz_config_police],
            output='screen'
        ),


        ExecuteProcess(
            cmd=['gz', 'sim', '-r', world_path],
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
                        '-x', '10',
                        '-z', '3',
                    ],
                    output='screen'
                )
            ]
        ),


        TimerAction(
            period=3.0,
            actions=[
                ExecuteProcess(
                    cmd=[
                        'ros2', 'run', 'ros_gz_sim', 'create',
                        '-world', 'duniya_ek',
                        '-topic', 'police/robot_description',
                        '-name', 'chitti',
                        '-x', '-10',
                        '-z', '3',
                    ],
                    output='screen'
                )
            ]
        ),
    ])