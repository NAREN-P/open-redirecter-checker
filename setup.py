from setuptools import setup

VERSION = '0.0.1'
DESCRIPTION = 'A Tool to find an open redirect vulnerability'
LONG_DESCRIPTION = 'This tool used all the available open redirect payload to find an application is vulnerable open redirect.'

with open("readme.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="openredirect",
    version=VERSION,
    author="@TENET_B2H",
    author_email="<TENET@gmail.com>",
    long_description=long_description,
    long_description_content_type="text/markdown",
    entry_points={
        'console_scripts': [
            'openredirectcheck = openredirect.main:main',
        ],
    },
    install_requires=['urllib3', 'requests', 'pkg_resources'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)