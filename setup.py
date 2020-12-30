import setuptools
    
with open("README.md", "r") as fh:
    long_description = fh.read()
    
setuptools.setup(
    name='fastpypi',
    version='0.1.0',
    author='DovaX',
    author_email='dovax.ai@gmail.com',
    description='A package enabling user to create and update existing pypi packages in an easy-to-use gui',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/DovaX/easypypi',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
          'dogui','keepvariable'
     ],
    python_requires='>=3.6',
)
    