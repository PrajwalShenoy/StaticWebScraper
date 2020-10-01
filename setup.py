import os
from setuptools import setup, find_packages

dir_path = os.getcwd()
with open(os.path.join(dir_path, 'requirements.txt'), 'r') as f:
    dependencies_string = f.read()

dependencies = [dependency.strip() for dependency in dependencies_string.strip().split("\n")]

setup(
    name='scraper',
    version=0.1,
    url='https://github.com/PrajwalShenoy/StaticWebScraper',
    author="Prajwal Shenoy",
    author_email='prajwalkpshenoy@gmail.com',
    description='Downloads all the account information from the DPO website',
    packages=['scraper'],
    install_requires=dependencies,
    entry_points={
        'console_scripts':[
            'scraper = '
            'scraper.scraper:main',
        ],
    },
    classifiers=[
        'Programming language :: Python :: 3',
        'Operating System :: Ubuntu :: 20.04'
    ],
    python_requires='>=3.6',
)