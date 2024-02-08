import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,
                    format='[%(asctime)s]: %(message)s')

project_name = "textSummarizer"


list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trais.ipynb"
]

for filePath in list_of_files:
    filePath = Path(filePath)
    filedir,filename = os.path.split(filePath)
    
    if filedir != "":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"creating directory : {filedir} for the file {filename}")
    
    if (not os.path.exists(filePath)) or (os.path.getsize(filePath)):
        with open(filePath,"w") as f:
            pass
        logging.info(f"creating empty file : {filePath}")
    else:
        logging.info(f"file already exists : {filePath}")