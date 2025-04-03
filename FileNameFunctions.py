
#!/usr/bin/env streamline
'''
 # @ Author: Aaron Shackelford
 # @ Create Time: 2025-02-25 16:44:41
 # @ Description: 
 
    FileNameFunctions contains helper functions to deal with file names and other path like utilities.
 
 # @ Modified by: Aaron Shackelford
 # @ Modified time: 2025-02-25 16:46:11
 '''

import os


def get_path_components(file_path: str) -> dict[str, str]:
    '''
    get_path_components returns the string components of a dir<br>
    

    Args:
        file_path (str): file path to be processed

    Returns:
        dict\[str,str\]:
            `"dir"`: directory<br>
            `"filename"`: name of the file, no extension<br>
            `"ext"`: the extension of the file<br>
    '''
    # Split the file path into directory, base name, and extension
    directory, base_name = os.path.split(os.path.abspath(file_path))
    name, ext = os.path.splitext(base_name)

    return {"dir": directory, "filename": name, "ext": ext}

def get_file_folder(file_path: str) -> str:
    """
    get_file_folder returns the absolute folder path of the given file.

    Args:
        file (str): file path

    Returns:
        str: folder path
    """
    return get_path_components(file_path=file_path)["ext"]

def get_file_ext(file_path: str) -> str:
    """
    get_file_ext returns the ext of the file if one exists, else returns ""

    Args:
        file (str): file path

    Returns:
        str: file ext
    """
    return get_path_components(file_path=file_path)["ext"]

def get_base_file_name(file_path: str) -> str:
    """
    getBaseName returns the file name of a path, no ext

    Args:
        file (str): file path

    Returns:
        str: file name
    """
    return get_path_components(file_path=file_path)["filename"]


def increment_filename(file_path: str, template: str = "({counter})", is_file_path:bool=True) -> str:
    """
    increment_filename increments given file

    Args:
        file_path (str): path to file. will increment if exists
        template (str): python template. Please use `counter` for the increment argument<br>
            Defaults to " ({counter})".<br>
            ex: `' ({counter:03})'` to pad left with zeros.
        is_file_path (bool): if the file is a file path put True, for folder path put False. Default True.

    Returns:
        str: new file path
    """
    # Split the file path into directory, base name, and extension
    directory, base_name = os.path.split(file_path)
    name, ext = os.path.splitext(base_name)

    # Initialize the counter
    counter: int = 1

    # Generate new file name with increment
    while os.path.exists(file_path):
        increment: str = template.replace("{counter}", str(counter))
        if is_file_path:
            new_name: str = f"{name}{increment}{ext}"
        else:
            # is folder
            new_name: str = f"{name}{ext}{increment}"
        file_path = os.path.normpath(os.path.join(directory, new_name))
        counter += 1
    return file_path

def norm_join_path(lhs_path: str, rhs_path: str) -> str:
    """
    norm_join_path returns the normal **POSIX** joined path for the two string paths

    Args:
        lhs_path (str): left hand side path
        rhs_path (str): right hand side path

    Returns:
        str: normal joined path
    """
    # more variables for debugging purposes
    lhs_dir: str = os.path.normpath(lhs_path)
    rhs_dir: str = os.path.normpath(rhs_path)

    # stupid ass relative edge case.
    # If the following paths start as a relative path, python return the last relative path
    # \\lhs + \\rhs\\... == \\rhs\\...
    # \\lhs + rhs\\... == \\lhs\\rhs\\...
    # What fuckery is this!?
    while rhs_dir.startswith("\\") or rhs_dir.startswith("/"):
        rhs_dir = rhs_dir.removeprefix("/")
        rhs_dir = rhs_dir.removeprefix("\\")
        rhs_dir: str = os.path.normpath(rhs_dir)

    return_dir: str = os.path.normpath(os.path.join(lhs_dir, rhs_dir))
    return return_dir
