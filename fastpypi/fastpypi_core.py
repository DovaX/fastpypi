import os
import dogui.dogui_core as dg
from keepvariable.keepvariable_core import Var,kept_variables,save_variables,load_variable



def load_setup_py():
    """Checks whether there is already a setup file for given package"""
    with open("setup.py","r") as file:
        rows=file.readlines()
        text_rows="\n".join(rows)
                
        name=text_rows.split("name")[1].split(",")[0].replace("'","").replace("=","").replace('"','')       
        version=text_rows.split("version")[1].split(",")[0].replace("'","").replace("=","").replace('"','') 
        author_email=text_rows.split("author_email")[1].split(",")[0].replace("'","").replace("=","").replace('"','')       
        url=text_rows.split("url")[1].split(",")[0].replace("'","").replace("=","").replace('"','')       
        author=text_rows.split("author")[1].split(",")[0].replace("'","").replace("=","").replace('"','')       
        short_description=text_rows.split("    description")[1].split(",")[0].replace("'","").replace("=","").replace('"','') #its on new line
        try:
            dependencies=text_rows.split("install_requires=[")[1].split("]")[0].replace("'","").replace('"','').replace(" ","").replace("\n","")   
            dependencies="'"+"','".join(dependencies.split(","))+"'"
        except: #if not found, fill nothing
            dependencies=""
        
        
        entry1.text.set(name)
        entry2.text.set(version)
        entry3.text.set(author)
        entry4.text.set(author_email)
        entry5.text.set(url)
        entry8.text.set(short_description)
        entry7.text.set(dependencies)
        



def create_setup_py():
    
    package_name=entry1.text.get()
    version=entry2.text.get()
    author=entry3.text.get()
    author_email=entry4.text.get()
    url=entry5.text.get()
    dependencies=entry7.text.get()
    short_description=entry8.text.get()
    
    
    setup_py_str="""import setuptools
    
with open("README.md", "r") as fh:
    long_description = fh.read()
    
setuptools.setup(
    name='"""+package_name+"""',
    version='"""+version+"""',
    author='"""+author+"""',
    author_email='"""+author_email+"""',
    description='"""+short_description+"""',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='"""+url+"""',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
          """+dependencies+"""
     ],
    python_requires='>=3.6',
)
    """
    
    with open("setup.py","w+") as file:
        file.write(setup_py_str)
        
def create_readme():
    with open("README.md","w+") as file:
        file.write("")

def create_licence():
    
    author=entry3.text.get()
    
    mit_licence_str="""MIT License
        
        Copyright (c) 2020 """+author+"""
        
        Permission is hereby granted, free of charge, to any person obtaining a copy
        of this software and associated documentation files (the "Software"), to deal
        in the Software without restriction, including without limitation the rights
        to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
        copies of the Software, and to permit persons to whom the Software is
        furnished to do so, subject to the following conditions:
        
        The above copyright notice and this permission notice shall be included in all
        copies or substantial portions of the Software.
        
        THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
        IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
        FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
        AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
        LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
        OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
        SOFTWARE.
    """
    
    with open("LICENSE","w+") as file:
        file.write(mit_licence_str)


def create_init_file():
    package_name=entry1.text.get()
    os.mkdir(package_name)
    with open(package_name+"\\__init__.py","w+") as file:
        file.write("")
        
        
def move_files_to_package_folder():
    package_name=entry1.text.get()
    os.system("move *.py "+package_name)


def create_package():
    os.system("python setup.py sdist bdist_wheel")
    
    

def upload_to_pypi():
    
    try:
        with open("fastpypi/credentials.ini", "r") as file:
            rows=file.readlines()
        print(rows)
        PYPI_USERNAME=rows[0].split("=")[1].strip()
        PYPI_PASSWORD=rows[1].split("=")[1].strip()
        
    except:
       PYPI_USERNAME, PYPI_PASSWORD = ("", "") 
    
    print("CRED",PYPI_USERNAME, PYPI_PASSWORD)
    if PYPI_USERNAME == "" and PYPI_PASSWORD == "":
        os.system("python -m twine upload dist/*")
    else:
        os.system("python -m twine upload dist/* -u "+PYPI_USERNAME+" -p "+PYPI_PASSWORD)
   
    
def change_directory():
    new_dir=entry6.text.get()
    os.chdir(new_dir)
    new_dir=label21.text.set(new_dir)
    
    print(os.getcwd())
    
    

current_dir=os.getcwd()
gui1=dg.GUI("Easy PyPI Tool")

label1=dg.Label(gui1.window,"Package name",3,1)
entry1=dg.Entry(gui1.window,3,2)
label2=dg.Label(gui1.window,"Version",4,1)
entry2=dg.Entry(gui1.window,4,2,"0.0.1")
 
btn1=dg.Button(gui1.window,"Create setup.py file",create_setup_py,5,4)
btn2=dg.Button(gui1.window,"Create MIT Licence file",create_licence,5,3)
btn6=dg.Button(gui1.window,"Create __init__.py file",create_init_file,4,3)
btn8=dg.Button(gui1.window,"Create README.md file",create_readme,4,4)
btn7=dg.Button(gui1.window,"Move python files to package folder",move_files_to_package_folder,6,4)


btn4=dg.Button(gui1.window,"Create package distribution",create_package,8,4)
btn5=dg.Button(gui1.window,"Upload package to PyPI",upload_to_pypi,9,4)



label3=dg.Label(gui1.window,"Author",5,1)
entry3=dg.Entry(gui1.window,5,2)
label4=dg.Label(gui1.window,"Author email",6,1)
entry4=dg.Entry(gui1.window,6,2,width=50)
label5=dg.Label(gui1.window,"Url",7,1)
entry5=dg.Entry(gui1.window,7,2,width=50)
label8=dg.Label(gui1.window,"Short Description",8,1)
entry8=dg.Entry(gui1.window,8,2,width=50)
label7=dg.Label(gui1.window,"Dependencies",9,1)
entry7=dg.Entry(gui1.window,9,2,width=50)



label6=dg.Label(gui1.window,"Current directory:",1,1)

label21=dg.Label(gui1.window,current_dir,1,2)

label20=dg.Label(gui1.window,"Change directory to:",2,1)
entry6=dg.Entry(gui1.window,2,2,text_input=current_dir,width=50)
btn3=dg.Button(gui1.window,"Change directory",change_directory,2,3)
btn9=dg.Button(gui1.window,"Load setup.py file",load_setup_py,2,4)


gui1.build_gui()