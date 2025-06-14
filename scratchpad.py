import os
import sys



def get_files_info(working_directory, directory=None):
    if not directory:
        return ("Error: No directory parameter was provided.")
    abs_directory = directory
    abs_wkdir = os.path.abspath(working_directory)
    is_wkdir_valid_path = os.path.isdir(working_directory)
    is_dir_valid_path = os.path.isdir(directory)
    # Convert the directory to an absolute path
    if is_dir_valid_path:
        abs_directory = os.path.abspath(directory)
    
    # Basic error checks
    if not is_wkdir_valid_path:
        return f'Error: "{working_directory}" is not a directory'
    if not is_dir_valid_path:
        return f'Error: "{abs_directory}" is not a directory'
    
    # get list of working directory contents
    workingdir_contents = os.listdir(working_directory)
    directory_contents = os.listdir(abs_directory)
    end_of_path_in_dir = abs_directory.split("/")[-1]
    print(f"child: {end_of_path_in_dir}")
    # Both the working directory and directory inputs are valid paths,
    # we can continue
    if end_of_path_in_dir in workingdir_contents:
        for item in directory_contents:
            item_path = os.path.join(abs_directory, item)
            isFile = os.path.isfile(item_path)
            file_size = os.path.getsize(item_path)
            print(f"- {item}: file_size={file_size} bytes, is_dir={isFile}")
    else:
        return f'Error: Cannot list "{abs_directory}" as it is outside the permitted working directory'


get_files_info(sys.argv[1], sys.argv[2])
