# make src package usable locally

from setuptools import find_packages, setup

setup(
    name='Medical Chatbot',  # name fo the package
    version='0.0.0',
    author='Jack Chen',
    author_email='chenhongzhi90@gmail.com',
    packages=find_packages(),
    install_requires=[]

)
