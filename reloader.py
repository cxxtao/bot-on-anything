
# encoding:utf-8

import importlib
import os
import threading
import time

def reload_module():
    module_name = 'model.google.bard_bot'  # Replace with the name of your module
    module = importlib.import_module(module_name)

    # Get the initial modified time of the source file
    initial_modified_time = os.path.getmtime(module.__file__)
    print(f'watching {module.__file__} ...')
    while True:
        try:
            modified_time = os.path.getmtime(module.__file__)
            if modified_time > initial_modified_time:
                print(f'Reloading module: [{module.__file__}]...')
                module = importlib.reload(module)
                initial_modified_time = modified_time
        except Exception as e:
            print('Error occurred while reloading module:', str(e))
            # Handle the exception as desired

        time.sleep(1)  # Wait for 1 second before the next check

def main():
    # Your main process logic here
    while True:
        # Your main process code
        time.sleep(1)  # Example: Wait for 1 second before the next iteration

if __name__ == '__main__':
    # Start the module reloading thread
    reload_thread = threading.Thread(target=reload_module, daemon=True)
    reload_thread.start()

    # Start your main process
    main()
