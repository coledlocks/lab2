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
# create time vector
dt = 0.01
time = np.arange(0, 5.01, dt)

input_signal = np.sin(6 * np.pi * time)

system_impulse = np.zeros_like(time)
system_impulse[time>=0.5] = 1
system_impulse[time>=2] = 0

input_signal_scaled = 2 * input_signal

# convolving statements
x_conv_h = np.convolve(input_signal, system_impulse)
h_conv_x = np.convolve(system_impulse, input_signal)
x_scaled_conv_h = np.convolve(input_signal_scaled, system_impulse)

convolve_times = np.arange(0, len(x_conv_h))/(1/dt)

# plotting the 3x3 subplots
plt.figure(1, clear=True)
plt.subplot(3, 3, 1)
plt.plot(time, input_signal)
plt.xlabel('time (secs)')
plt.ylabel('amplitude (a.u.)')
plt.subplot(3, 3, 2)
plt.plot(time, system_impulse)
plt.xlabel('time (secs)')
plt.ylabel('amplitude (a.u.)')
plt.subplot(3, 3, 3)
plt.plot(convolve_times, x_conv_h)
plt.xlabel('time (secs)')
plt.ylabel('amplitude (a.u.)')
plt.subplot(3, 3, 4)
plt.plot(time, system_impulse)
plt.xlabel('time (secs)')
plt.ylabel('amplitude (a.u.)')
plt.subplot(3, 3, 5)
plt.plot(time, input_signal)
plt.xlabel('time (secs)')
plt.ylabel('amplitude (a.u.)')
plt.subplot(3, 3, 6)
plt.plot(convolve_times, h_conv_x)
plt.xlabel('time (secs)')
plt.ylabel('amplitude (a.u.)')
plt.subplot(3, 3, 7)
plt.plot(time, input_signal_scaled)
plt.xlabel('time (secs)')
plt.ylabel('amplitude (a.u.)')
plt.subplot(3, 3, 8)
plt.plot(time, system_impulse)
plt.xlabel('time (secs)')
plt.ylabel('amplitude (a.u.)')
plt.subplot(3, 3, 9)
plt.plot(convolve_times, x_scaled_conv_h)
plt.xlabel('time (secs)')
plt.ylabel('amplitude (a.u.)')
plt.tight_layout()

#%% PART 2

# defining signal
def get_convolved_signal(input_signal, system_impulse):
    # initiating the array
    my_convolved_signal = np.zeros(len(input_signal) + len(system_impulse) - 1)
    
    # nesting for loops
    for in_sig_idx in range(len(input_signal)):
        for sys_imp_idx in range(len(system_impulse)):
            my_convolved_signal[in_sig_idx + sys_imp_idx] += input_signal[in_sig_idx] * system_impulse[sys_imp_idx]
    return my_convolved_signal

my_convolved_signal = get_convolved_signal(input_signal, system_impulse)

# plotting the manually made convolved signal
plt.figure(2, clear=True)
plt.plot(convolve_times, my_convolved_signal)

# annotating the plot
plt.xlabel('time (secs)')
plt.ylabel('amplitude (a.u.)')

#%% PART 3
# create time vector
dt = 0.01
drug_time = np.arange(0, 50.01, dt)

drug_dosage = 1 - (np.cos(0.25 * np.pi * drug_time))

# simplify body impulse 
gut_impulse = 0.25 * np.exp(drug_time/0.25) * drug_dosage
blood_impulse = 
kidney_impulse = np.exp(-2 * (drug_time - 1)**2
body_impulse =

# plot y(t) body response

#%% PART 4

