import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="HowLongToBeat-Python-API", # Replace with your own username
    version="0.1.14",
    author="KimWithGlasses",
    author_email="kimwithglasses@kakao.com",
    description="This package helps to get data from howlongtobeat.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/JaeguKim/HowLongToBeat-Python-API",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'urllib3',
        'bs4>=0.0.1',
        #bs4 installing is failed because bs4 doesn't exist in testPyPI
    ],
    python_requires='>=3.6',
)