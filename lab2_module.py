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

#%% PART 2: Build a Convolution Function
# convolve input signals with system impulse
def get_convolved_signal(input_signal, system_impulse):
    """ This function takes two inputs input_signal and system_impulse. It generates a 1D array of zeros of length 
    input_signal + system_impulse - 1, then convolves the signals by iterating through a for loop.

    Parameters
    __________
    input_signal : Array of float, size: (,)
        Input signal at each time point.
    system_impulse : Array of int, size: (,)
        A rectangular pulse function displayed as an array of ints.

    Returns
    _______
    my_convolved_signal : Array of float, size: (,)
        Convolution of input_signal and system_impulse.
    
    """
    # array of zeros
    my_convolved_signal = np.zeros(len(input_signal) + len(system_impulse) - 1)
    # loop through convolutions
    for in_sig_idx in range(len(input_signal)):
        for sys_imp_idx in range(len(system_impulse)):
            my_convolved_signal[in_sig_idx + sys_imp_idx] += input_signal[in_sig_idx] * system_impulse[sys_imp_idx]
    return my_convolved_signal

#%% PART 3: Simplify a Cascade System
# calculate system output
def run_drug_simulations(input_signal, system_impulse, dt, label):
    """ This function uses NumPy's convolve command to convolve input_signal and system_impulse, then plots the resultant
    system output. 

    Parameters
    __________
    input_signal : Array of float, size: (,)
          Input signal at each time point dt.
    system_impulse : Array of int, size: (,)
        A rectangular pulse function displayed as an array of ints.
    dt : Array of float, size: (,)
        Time vector from 0 to 50 seconds inclusive with a step size of 0.01 seconds.
    label : str
        Label describing line that is being plotted

    Returns
    _______
    None. 
    
    """
    # convolve signals
    system_output = np.convolve(input_signal, system_impulse)
    times = np.arange(0, len(y_t))/(1/dt)
    # plot system output
    plt.figure(3)
    plt.plot(times, system_output, label=label)
    
