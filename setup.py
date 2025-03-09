from setuptools import find_packages, setup
from typing import List

def get_requirments(file_path:str)->List[str]:
    requirments = []
    with open(file_path) as file_obj:
        requirments = file_obj.readlines()
        requirments = [req.replace("\n", "") for req in requirments]

        if '-e .' in requirments:
            requirments.remove('-e .')
    return requirments
    
setup(name="diabetes predict",
        version= "0.1",
        author="akshay",
        author_email="akshaykumar249@gmail.com",
        packages= find_packages(),
        install_requires= get_requirments("requirements.txt")
)