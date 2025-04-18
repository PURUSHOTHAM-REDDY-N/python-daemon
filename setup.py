from setuptools import setup, find_packages

setup(
    name='mydaemon',
    version='1.0',
    description='Simple background Python daemon',
    author='Your Name',
    author_email='you@example.com',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'mydaemon = mydaemon.main:main',
        ],
    }
)
