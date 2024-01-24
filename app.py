import multiprocessing
from app1 import fetch_data
from main import record

def run_program1():
    fetch_data()

def run_program2():
    record()

if __name__ == '__main__':
    # Create separate processes for each program
    process1 = multiprocessing.Process(target=run_program1)
    process2 = multiprocessing.Process(target=run_program2)

    # Start the processes
    process1.start()
    process2.start()

    # Wait for the processes to finish
    process1.join()
    process2.join()
