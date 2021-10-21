from setuptools import setup
import os
from glob import glob

package_name = 'gps_visualization'
game_engine ='gps_visualization/game_engine'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name, game_engine],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'assets'), glob('gps_visualization/assets/*'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='apun1',
    maintainer_email='apun1@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'gps_visualizer = gps_visualization.gps_visualizer:main'
        ],
    },
)
