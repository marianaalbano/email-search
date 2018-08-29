from setuptools import setup
from setuptools.command.develop import develop
from setuptools.command.install import install
from subprocess import check_call


setup(
    name='pymail',
    version='1.0.0',
    url='https://github.com/marianaalbano/pymail',
    license='MIT',
    author='Mariana Albano',
    author_email='mariana.albano@outlook.com',
    description='Email management module',
    py_modules=['python-mail'],
    install_requires=['imaplib','email']
)