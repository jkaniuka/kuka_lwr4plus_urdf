from setuptools import setup
import os
from glob import glob

package_name = 'lwr_description'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
        (os.path.join('share', package_name, 'model'), glob('model/*.*')),
        (os.path.join('share', package_name, 'rviz') , glob('rviz/*.*')),
        (os.path.join('share', package_name, 'meshes/lwr4plus/visual') , glob('meshes/lwr4plus/visual/*.*')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='jan',
    maintainer_email='kan.jan@wp.pl',
    description='The lwr_description package contains the model of a KUKA LWR 4+ arm.',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
