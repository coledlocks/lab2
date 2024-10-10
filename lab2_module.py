#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 11:00:36 2024
lab2_module.py


Cole Drozdek and Kaelen Kenna
"""
# importing related packages
import sounddevice as sd
import numpy as np
from matplotlib import pyplot as plt
from scipy.io.wavfile import read

#%% PART 1
dt = 0.01
time = np.arange(0, 5.01, dt)

input_signal = np.sin(2 * np.pi * SOMETHING * time)

# NOT QUITE THIS
# rect = np.zeros(len(time))
# rect[time>=-0.5] = 1
# rect[time>=0.5] = 0

system_impulse = np.zeros_like(time)
system_impulse[time>=0.5] = 1
system_impulse[time>=2] = 0

#%% PART 2

#%% PART 3

#%% PART 4

