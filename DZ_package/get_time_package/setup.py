from setuptools import setup

setup(
    name='get_time_package',
    version='0.1',
    description='description',
    url='http://github.com/name/package_name',
    author='Team_9',
    author_email='email@example.com',
    license='MIT',
    packages=['get_time_package'],
    install_requires=[
    'requests==2.26.0',
    ],
    entry_points={
    'console_scripts': [
    'get_time=get_time_package.get_time:main',
    ]
    }
)
