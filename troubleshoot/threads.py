#!/usr/bin/env python3

from concurrent import futures

def progress_bar():
    pass

def process_file():
    pass

def main():
    
    # Thread executor
    executor = futures.ThreadPoolExecutor()

    # Processes executor
    #executor = futures.ProcessPoolExecutor()
    
    for root, _, files in os.walk('images'):
        for basename in progress_bar(files):
            if not basename.endswith('.jpg'):
                continue
            executor.submit(process_file, root, basename)
    print('Waiting for all threads to finish.')
    executor.shutdown()
    return 0

