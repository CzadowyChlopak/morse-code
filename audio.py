import wave
import numpy as np
import matplotlib.pyplot as plt
import sys
import scipy.signal.signaltools as sigtool
from scipy.signal import find_peaks


def normalization(sig):
    env = (sigtool.hilbert(sig)) #przeksztalcenie hilberata
    threshold = 200
    square_sig = (env > threshold)
    return square_sig


def wav2morse(filename):
    wav = wave.open(filename, 'r')


    raw = wav.readframes(-1)
    raw = list(np.frombuffer(raw, "Int16"))
    plt.figure('raw')
    plt.title("raw")
    plt.plot(raw)
    # plt.show()

    if wav.getnchannels()==2:
        print("Stereo files are not supported!")
        sys.exit(0)

    thresh = normalization(raw)
    # print(thresh)

    plt.figure('thresh')
    plt.title('thresh')
    plt.plot(thresh)
    # plt.show()

    peaks, _ = find_peaks(thresh)
    print(peaks)


    plt.figure('peaks')
    plt.title('peaks')
    plt.plot(peaks, thresh[peaks], '.')
    # plt.show()

    #####################################
    delta = 0
    start_value = peaks[0]
    prev_value = 0
    spaces = []
    characters = []

    for i in range(len(peaks)):
        delta = peaks[i] - prev_value#peaks[i-1]
        # print(delta)
        if delta > 20:
            spaces.append(delta)
            characters.append(prev_value-start_value)
            start_value=peaks[i]
        prev_value = peaks[i]


    rew_peaks = peaks[::-1]
    start_value = rew_peaks[0]
    prev_value = rew_peaks[0]

    for i in range(len(rew_peaks)):
        delta = abs(rew_peaks[i] - prev_value)
        if delta > 20:
            spaces.append(delta)
            characters.append(abs(prev_value-start_value))
            start_value=peaks[i]
            break
        prev_value = rew_peaks[i]




    print(spaces)
    print(characters)
    print(len(spaces)-len(characters))

    returned_vals = []
    for i in range(len(characters)):
        returned_vals.append(characters[i])
        if spaces[i] > 5000:
            returned_vals.append(0)

    print(returned_vals)

    returned = ''
    for i in range(len(returned_vals)):
        if returned_vals[i] == 0:
            returned +=' '
        elif returned_vals[i] < 500:
            returned +='.'
        else:
            returned += '-'

    print(returned)
    plt.show()
    return returned
