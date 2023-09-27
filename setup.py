## responsible for creating my entire machine learning application as a package and even deploy in pypi
## building our application as a package like seaborn 
from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
            
    return requirements
 

#metadata
setup(
name='mlproject_student',
version='0.0.1',
author='Priya',
author_email='gnanapriya40@gmail.com',
packages=find_packages(), # Automatically find all packages in your project
install_requires=get_requirements('requirements.txt')
##['pandas','numpy','seaborn'] ## all the requirements we want, it will automatically install
)


