import os

def search_dir_return_path(bottom_directory, string_to_search, file_type):
    files_to_return = []
    for root, dirs, files in os.walk(bottom_directory, topdown=False):        
        for name in files:
            if (string_to_search in name) and (name.endswith(file_type)):
                files_to_return.append(str(os.path.join(root, name)))
    return(files_to_return)

def search_dir_return_path_two_strings(bottom_directory, list_of_strings_to_search, file_type):
    
    files_to_return = []
    for root, dirs, files in os.walk(bottom_directory, topdown=False):        
        for name in files:
        	if (list_of_strings_to_search[0] and list_of_strings_to_search[1] in name) and (name.endswith(file_type)):
        		files_to_return.append(str(os.path.join(root, name)))
        		
    return(files_to_return)
   
def search_dir_return_path_multiple_strings(bottom_directory, list_of_strings_to_search, file_type):
    ##modify this to search for combination of an arbitrary list of strings in a filename
    files_to_return = []
    for root, dirs, files in os.walk(bottom_directory, topdown=False):        
        for name in files:
            for string in list_of_strings_to_search:
            	if (string_to_search in name) and (name.endswith(file_type)):
                	files_to_return.append(str(os.path.join(root, name)))
                	
    return(files_to_return)
    
def search_dir_for_file_return_path(bottom_directory, file_name):
    file_path = 'not found'
    for root, dirs, files in os.walk(bottom_directory, topdown=False):        
        for name in files:
            if name == file_name:
				file_path = str(root) + '/' + str(name)
    return(file_path)
    
def search_dir_for_list_of_files_return_path(bottom_directory, files_list, file_type):
	file_names = []
	found_paths = []
	for root, dirs, files in os.walk(bottom_directory, topdown=False):
		for name in files:
			for item in files_list:
				if (item in name) and (name.endswith(file_type)):
					found_paths.append(os.path.join(root, name))
					file_names.append(name)
	return(file_names, found_paths)

def search_dir_for_file_return_path(bottom_directory, name):
    list_of_experiments = []
    for root, dirs, files in os.walk(bottom_directory, topdown=False):        
        for dir_name in dirs:
            if name in dir_name:
                list_of_experiments.append(str(root) + str(dir_name))
    return(list_of_experiments)