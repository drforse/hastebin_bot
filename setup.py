import setuptools

setuptools.setup(
    name="hastebin_bot",
    version="0.0.2",
    author="drforse",
    author_email="george.lifeslice@gmail.com",
    description="hastebin_bot",
    long_description="hastebin_bot",
    long_description_content_type="text/markdown",
    url="https://github.com/drforse/hastebin_bot",
    packages=setuptools.find_packages(),
    install_requires=["aiogram==3.0.0b1"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.10',
)
