import os

def get_test_resource_path(resource_name):
    return os.path.join(os.getcwd(), "TestResources", resource_name)

def check_elimination(seq, patterns):
    for p in patterns:
        if p in seq:
            return False
    return True