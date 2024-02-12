import os
from box.exceptions import BoxValueError
import yaml
from textSummarizer.logging import logger
from box import ConfigBox
from pathlib import Path
from typing import Any
from ensure import ensure_annotations


def read_yaml(path_to_yaml:Path)->ConfigBox:
    """reads yaml file and returns ConfigBox
    
    Args:
        path_to_yaml (str): path to yaml file

    Raises:
        ValueError: if yaml file is empty
        e:empty file

    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file :{path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    

def create_directories(path_to_directories:list,verbose=True):
    """creates list of directories
        
        Args:
            path_to_directories (list): list of directories
            verbose (bool, optional): [description]. Defaults to True.

        Raises:
            ValueError: [description]

        Returns:
            [type]: [description]
    """
    for directory in path_to_directories:
        if not os.path.exists(directory):
            os.makedirs(directory)
            if verbose:
                logger.info(f"creating directory : {directory}")
        else:
            if verbose:
                logger.info(f"directory : {directory} already exists")
    return path_to_directories


def get_size(path:Path)->str:
    """ Get the size in KB
    
    Args:
        path (str): path to file

    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f" ~ {size_in_kb}"



