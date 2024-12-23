from setuptools import find_packages, setup

package_name = 'mypkgsec'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Koki Iwai',
    maintainer_email='koki4302000@gmail.com',
    description='practice second time',
    license='BSD-3-Clause',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'talker = mypkgsec.talker:main',
            'listener = mypkgsec.listener:main',
        ],
    },
)
