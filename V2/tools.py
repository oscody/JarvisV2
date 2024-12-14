import importlib.util
import os
import sys

def import_module_from_path(module_name, file_path):
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    if spec is None:
        raise ImportError(f"Cannot find spec for '{module_name}' at '{file_path}'")
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module

# Determine the base path relative to this script
base_path = os.path.dirname(os.path.abspath(__file__))

# Paths to your modules
getTime_path = os.path.join(base_path, '..', 'tests', '3.ai', 'tools', 'getTime.py')
langchain_gmail_path = os.path.join(base_path, '..', 'tests', '3.ai', 'tools', 'langchain_gmail.py')

# Import the modules
getTime = import_module_from_path('getTime', getTime_path)
langchain_gmail = import_module_from_path('langchain_gmail', langchain_gmail_path)


# Expose the functions directly from tools.py
fetch_mails = langchain_gmail.fetch_mails
get_current_time = getTime.get_current_time

# Now you can use the imported modules
if __name__ == "__main__":
    print(fetch_mails())
    print(get_current_time())