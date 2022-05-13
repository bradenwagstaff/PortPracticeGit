from re import sub
import socket
import struct
from cmath import pi
import numpy as np
import subprocess
import os
import pygame
from pygame.locals import *
import CircleTest
import sys

pygame.init()
display = pygame.display.set_mode((300, 300))
HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)
cubeX = 0
cubeY = 0
cubeZ = 0
timer = 0
subtract = False
subtractY = True
circleSize = 10
counter = 0

# os.startfile("C:\\Users\\brade\\Documents\\Computing\\UnityProjects\\PortPractice\\PortPractice.exe")
#print((struct.pack('f', 0.01)[3]))
#print((struct.unpack('f', struct.pack('f', 0.01))[0]))

# subprocess.call(r"C:\\Users\\brade\\Documents\\Computing\\UnityProjects\\PortPractice")

def myMap(x, in_min, in_max, out_min, out_max):
    return float((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            FPS = int(str(data, 'UTF=8'))
            #FPS += 1
            #print(type(FPS))
            
            '''#Circle Code
            if counter == FPS:
                 counter == 0
            rad = myMap(counter, 0, FPS, 0, 2*pi)#maps our framerate to tao letting
                                                # this means that our circle makes a cycle every second
                                                # no matter the frame rate
            
            cubeX = np.sin(rad) * circleSize
            cubeY = np.cos(rad) * circleSize
            '''
            for event in pygame.event.get():
                cubeX = 0
                cubeY = 0
                cubeZ = 0
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        cubeX = 1
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        cubeX = -1
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        cubeY = 1
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        cubeY = -1
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_PLUS:
                        cubeZ = 1
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_MINUS:
                        cubeZ = -1
            
            
           
            conn.sendall(struct.pack('fff', cubeX, cubeY, cubeZ))
            
            timer += 1
            counter += 1
            #print(f"received data: {data}")
            # if timer > FPS*10:
            #     break
            if not data:
                break
            #conn.sendall(data)


