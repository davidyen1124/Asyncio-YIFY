from setuptools import setup

setup(
    name='asyncio-yify',
    version='0.0.8',
    author='davidyen1124',
    author_email='davidyen1124@gmail.com',
    description='Damned fast YIFY parser using Asyncio',
    lincense='Apache',
    keywords='yify parser movies asyncio',
    url='https://github.com/davidyen1124/Asyncio-YIFY',
    packages=['yify'],
    install_requires=[
        'aiohttp==0.11.0',
        'lxml==4.6.3',
    ],
)
