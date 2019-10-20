import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="home_temp_sensor",
    version='0.0.2',
    author="LeadTheSalt",
    author_email="leadthesalt.soc@gmail.com",
    description="My home tempearture sensore on a RaspberryPi",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/leadthesalt/home_temp_sensor",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)