from setuptools import setup, find_packages

setup(
    name="skribbl-public",
    version="0.2.0",
    packages=find_packages(),
    install_requires=[
        "websockets",
        "pyperclip",
        "argparse"
    ],
    entry_points={
        "console_scripts": [
            "skribbl-public=skribbl.autojoin:run",
        ],
    },
    author="Devvrat Miglani",
    description="A package to generate public session url for Skribbl.io game",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/devvratmiglani/SkribblePublicRoomLink",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
