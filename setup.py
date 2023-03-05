from  setuptools import find_packages , setup 
from typing import List

Hypen_dot = "-e ."

def get_requirements(filepath = "requirements.txt")-> List[str]:
    requiremets = []
    with open(filepath) as f:
        requiremets = f.readlines()
        requiremets= [req.replace("\n" , "") for req in requiremets]

        if Hypen_dot in requiremets:
            requiremets.remove(Hypen_dot)

    return requiremets


setup(
name="MLProject",
description="End To End Machine Learning Pipeline",
version="0.0.1",
author="Karthik Saran",
author_email="mailmekarthik001@gmail.com",
packages = find_packages(),
install_requires = get_requirements("requirements.txt")
)

    