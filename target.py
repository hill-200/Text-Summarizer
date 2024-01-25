import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format= '[%(asctime)s]: %(message)s:')

projectName = "textSummarizer"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{projectName}/__init.py__",
    f"src/{projectName}/components/__init.py",
    f"src/{projectName}/utils/__init.py__",
    f"src/{projectName}/utils/common.py",
    f"src/{projectName}/logging//__init.py__",
    f"src/{projectName}/logging/__init.py__",
    f"src/{projectName}/config/__init__.py",
    f"src/{projectName}/config/configuration.py",
    f"src/{projectName}/pipeline/__init.py__",
    f"src/{projectName}/entity/__init__.py",
    f"src/{projectName}/constants/__init__.py",
    "config/config.yml",
    "params.yml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    fileDirectory, filename = os.path.split(filepath)

    if fileDirectory != "":
        os.makedirs(fileDirectory, exist_ok=True)
        logging.info(f"Creating directory:{fileDirectory} for file:{filename}")

    if(not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,'w') as f:
            pass
            logging.info(f"Creating empty file:{filepath}")
        
    else:
        logging.info(f"{filename} already exists")
