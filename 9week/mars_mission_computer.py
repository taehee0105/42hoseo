# mars_mission_computer.py

import threading
import multiprocessing
import time
import sys

class MissionComputer:
    def __init__(self, name='MissionComputer'):
        self.name = name

    def get_mission_computer_info(self, stop_event=None):
        while not (stop_event and stop_event.is_set()):
            print(f'[{self.name}] Mission Computer Info: Status OK')
            time.sleep(20)

    def get_mission_computer_load(self, stop_event=None):
        while not (stop_event and stop_event.is_set()):
            print(f'[{self.name}] Mission Computer Load: CPU Load at 45%')
            time.sleep(20)

    def get_sensor_data(self, stop_event=None):
        while not (stop_event and stop_event.is_set()):
            print(f'[{self.name}] Sensor Data: Temperature 36.5°C')
            time.sleep(5)

def run_threads():
    runComputer = MissionComputer('runComputer')
    stop_event = threading.Event()

    threads = [
        threading.Thread(target=runComputer.get_mission_computer_info, args=(stop_event,)),
        threading.Thread(target=runComputer.get_mission_computer_load, args=(stop_event,)),
        threading.Thread(target=runComputer.get_sensor_data, args=(stop_event,))
    ]

    for t in threads:
        t.start()

    try:
        while True:
            user_input = input()
            if user_input.strip().lower() == 'q':
                print('Stopping threads...')
                stop_event.set()
                break
    except KeyboardInterrupt:
        stop_event.set()

    for t in threads:
        t.join()

def run_instance(name):
    comp = MissionComputer(name)
    stop_event = multiprocessing.Event()

    info_proc = multiprocessing.Process(target=comp.get_mission_computer_info, args=(stop_event,))
    load_proc = multiprocessing.Process(target=comp.get_mission_computer_load, args=(stop_event,))
    sensor_proc = multiprocessing.Process(target=comp.get_sensor_data, args=(stop_event,))

    info_proc.start()
    load_proc.start()
    sensor_proc.start()

    try:
        while True:
            user_input = input()
            if user_input.strip().lower() == 'q':
                print(f'Stopping processes for {name}...')
                stop_event.set()
                break
    except KeyboardInterrupt:
        stop_event.set()

    info_proc.terminate()
    load_proc.terminate()
    sensor_proc.terminate()

    info_proc.join()
    load_proc.join()
    sensor_proc.join()

def run_processes():
    processes = [
        multiprocessing.Process(target=run_instance, args=('runComputer1',)),
        multiprocessing.Process(target=run_instance, args=('runComputer2',)),
        multiprocessing.Process(target=run_instance, args=('runComputer3',))
    ]

    for p in processes:
        p.start()

    try:
        while True:
            user_input = input()
            if user_input.strip().lower() == 'q':
                print('Stopping all computer instances...')
                for p in processes:
                    p.terminate()
                break
    except KeyboardInterrupt:
        for p in processes:
            p.terminate()

    for p in processes:
        p.join()

if __name__ == '__main__':
    print('Select Mode:')
    print('1. Run multithreaded (enter "1")')
    print('2. Run multiprocess (enter "2")')
    print('Enter "q" anytime to stop.')

    mode = input('Mode: ').strip()

    if mode == '1':
        run_threads()
    elif mode == '2':
        run_processes()
    else:
        print('Exiting.')
