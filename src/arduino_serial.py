# Written by Aaron Barge
# Copyright 2021


import serial # serial.Serial()
import struct # struct.pack()
import sys # sys.exit()
import time # time.sleep()


def handshake(arduino):
    """
    Performs a simple handshake with the arduino to ensure a stable connection.
    """
    arduino.write(bytes('a'.encode("utf-8"))) # Send a dummy byte
    wait_for_n_bytes(arduino, 5)
    data = arduino.read(5)             # Grab response
    if data != b'begin':               # Check for good response
        return False
    return True


def wait_for_n_bytes(arduino, n):
    while arduino.in_waiting < n:
        continue


def write_int_n_bytes(arduino, msg, n):
    arduino.write(struct.pack('>' + ('B' * n), msg))


def run(animation):
    arduino = serial.Serial('/dev/ttyUSB0', 115200, timeout=0.1)
    time.sleep(2)                       # Wait for the arduino to be ready
    success = handshake(arduino)
    if not success:
        sys.exit("Handshake with Arduino failed.")
    wait_for_n_bytes(arduino, 1)
    arduino.read(1)
    while True:
        for frame in animation.frames:
            start_ms = round(time.time() * 1000)
            write_int_n_bytes(arduino, len(frame), 1)
            for index, color in frame.items():
                write_int_n_bytes(arduino, index, 1)
                write_int_n_bytes(arduino, color.r, 1)
                write_int_n_bytes(arduino, color.g, 1)
                write_int_n_bytes(arduino, color.b, 1)
            wait_for_n_bytes(arduino, 1)
            arduino.read(1)
            end_ms = round(time.time() * 1000)
            frame_display_delay_ms = end_ms - start_ms
            sleep_time_s = (animation.hold_ms - frame_display_delay_ms) / 1000
            time.sleep(sleep_time_s if sleep_time_s > 0 else 0)





