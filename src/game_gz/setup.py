from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'game_gz'

setup(
    name=package_name,
    version='1.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'urdf_thief'), glob('urdf_thief/*')),
        (os.path.join('share', package_name, 'urdf_police'), glob('urdf_police/*')),
        (os.path.join('share', package_name, 'launch'), glob('launch/*')),
        (os.path.join('share', package_name, 'worlds'), glob('worlds/*')),
        (os.path.join('share', package_name, 'config'), glob('config/*')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='lenovoi',
    maintainer_email='bhagabantagiri@gmail.com',
    description='A beginner-level ROS 2 Jazzy and Gazebo Harmonic robotics micro-project demonstrating differential-drive control, ROS-Gazebo communication and sensors.',
    license='MIT',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'thief_ai = game_gz.thief_ai:main'
        ],
    },
)
