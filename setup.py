from setuptools import setup, find_packages

setup(
    name='thobanipackage',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA python package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/Thobani96/thobanipackage',
    author='Thobani',
    author_email='thobanimthimkhulu@gmail.com'
    )
