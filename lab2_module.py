#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 14:37:23 2024
lab2_module.py

@author: coledlocks
"""
# importing related packages
import numpy as np
from matplotlib import pyplot as plt

#%% PART 2

def get_convolved_signal(input_signal, system_impulse):
    # initiating the array
    my_convolved_signal = np.zeros(len(input_signal) + len(system_impulse) - 1)
    
    # nested for loops
    for in_sig_idx in range(len(input_signal)):
        for sys_imp_idx in range(len(system_impulse)):
            my_convolved_signal[in_sig_idx + sys_imp_idx] += input_signal[in_sig_idx] * system_impulse[sys_imp_idx]
    return my_convolved_signal

#%% PART 3

def run_drug_simulations(input_signal, system_impulse, dt, label):
    y_t = np.convolve(input_signal, system_impulse)
    times = np.arange(0, len(y_t))/(1/dt)
    plt.figure(3)
    plt.plot(times, y_t, label=label)

