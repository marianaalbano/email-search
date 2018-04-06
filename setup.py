from setuptools import setup
from setuptools.command.develop import develop
from setuptools.command.install import install
from subprocess import check_call


setup(
    name='email-search',
    version='1.0.0',
    url='https://github.com/marianaalbano/email-search.git',
    license='MIT',
    author='Mariana Albano',
    author_email='mariana.albano@outlook.com',
    description='Module to search email',
    py_modules=['email-search'],
    install_requires=['imaplib','email']
)