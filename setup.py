from setuptools import setup, find_packages

setup(
    name='python-daemon',
    version='0.1',
    packages=find_packages(),  # <== this is key
    entry_points={
        'console_scripts': [
            'mydaemon = mydaemon.main:main',  # optional if you want /usr/bin/mydaemon
        ]
    },
)
