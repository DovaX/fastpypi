import os
import dogui.dogui_core as dg
from keepvariable.keepvariable_core import Var,kept_variables,save_variables,load_variable

def create_setup_py():
    
    package_name=entry1.text.get()
    version=entry2.text.get()
    author=entry3.text.get()
    author_email=entry4.text.get()
    url=entry5.text.get()
    
    setup_py_str="""import setuptools
    
    with open("README.md", "r") as fh:
        long_description = fh.read()
    
    setuptools.setup(
        name='"""+package_name+"""',
        version='"""+version+"""',
        author='"""+author+"""',
        author_email='"""+author_email+"""',
        description="Description",
        long_description=long_description,
        long_description_content_type="text/markdown",
        url='"""+url+"""',
        packages=setuptools.find_packages(),
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
        ],
        python_requires='>=3.6',
    )
    """
    
    with open("test.py","w+") as file:
        file.write(setup_py_str)

gui1=dg.GUI("Easy PyPI Tool")

label1=dg.Label(gui1.window,"Package name",1,1)
entry1=dg.Entry(gui1.window,1,2)
label2=dg.Label(gui1.window,"Version",2,1)
entry2=dg.Entry(gui1.window,2,2,"0.0.1")

btn1=dg.Button(gui1.window,"Create setup.py file",create_setup_py,2,3)

label3=dg.Label(gui1.window,"Author",3,1)
entry3=dg.Entry(gui1.window,3,2)
label4=dg.Label(gui1.window,"Author email",4,1)
entry4=dg.Entry(gui1.window,4,2)
label5=dg.Label(gui1.window,"Url",5,1)
entry5=dg.Entry(gui1.window,5,2)

gui1.build_gui()