# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from pydub import AudioSegment
import os
import random
from datetime import datetime


#
# EDITABLE VARIABLES
# \/ \/ \/ \/ \/ \/ \/
AUDIO_SEGMENT_MIN_LENGTH_SECONDS = 2
AUDIO_SEGMENT_MAX_LENGTH_SECONDS = 10
NUMBER_OF_VARIANTS = 5
# /\ /\ /\ /\ /\ /\ /\
# EDITABLE VARIABLES
#


SECONDS_TO_MS_CONSTANT = 1000
END_AUDIO_MIN_LENGTH_SECONDS = 30

#DEFAULT_DIRECTORY = "testing/"
DEFAULT_DIRECTORY = "./"
DEFAULT_INPUTS_DIRECTORY = DEFAULT_DIRECTORY + "inputs/"
CURRENT_PROGRAM_DIRECTORY = DEFAULT_DIRECTORY + datetime.now().strftime('%Y-%m-%d_%H-%M-%S') + "/"

if not os.path.exists(DEFAULT_DIRECTORY):
    os.makedirs(DEFAULT_DIRECTORY)

if not os.path.exists(DEFAULT_INPUTS_DIRECTORY):
    os.makedirs(DEFAULT_DIRECTORY)

if not os.path.exists(CURRENT_PROGRAM_DIRECTORY):
    os.makedirs(CURRENT_PROGRAM_DIRECTORY)



audios = []
print("finding audio files...")
for filename in os.listdir(DEFAULT_INPUTS_DIRECTORY):
    if filename.endswith('.mp3'):
        audios.append(AudioSegment.from_file(DEFAULT_INPUTS_DIRECTORY + filename))
        print("audio file " + filename + " found")
print("finished finding audio files")

numberOfAudios = len(audios)



finalsDirectory = CURRENT_PROGRAM_DIRECTORY + "finals/"
inputsDirectory = CURRENT_PROGRAM_DIRECTORY + "inputs/"

if not os.path.exists(finalsDirectory):
    os.makedirs(finalsDirectory)
if not os.path.exists(inputsDirectory):
    os.makedirs(inputsDirectory)

print("copying audio files...")
for i in range(numberOfAudios):
    audios[i].export(inputsDirectory + "input" + str(i) + ".mp3", format="mp3")
    print("audio file " + str(i+1) + " of " + str(numberOfAudios) + " copied...")
print("audio files copied")

for mixNum in range(NUMBER_OF_VARIANTS):
    print("starting mix " + str(mixNum+1) + " of " + str(NUMBER_OF_VARIANTS) + "...")



    currentDirectory = CURRENT_PROGRAM_DIRECTORY + str(mixNum) + "/"

    if not os.path.exists(currentDirectory):
        os.makedirs(currentDirectory)






    audiosLengths = [random.randint(AUDIO_SEGMENT_MIN_LENGTH_SECONDS * SECONDS_TO_MS_CONSTANT, AUDIO_SEGMENT_MAX_LENGTH_SECONDS * SECONDS_TO_MS_CONSTANT) for _ in range(numberOfAudios)]

    audiosStartStampMs = [(random.randint(0 , len(audios[i]) - audiosLengths[i] - 1)) for i in range(numberOfAudios)]

    segments = [ audios[i][audiosStartStampMs[i]:audiosStartStampMs[i]+audiosLengths[i]] for i in range(numberOfAudios) ]

    sorted_indexes = sorted(range(len(segments)), key=lambda i: len(segments[i]), reverse=True)

    combined = segments[sorted_indexes[0]]
    segments[sorted_indexes[0]].export(currentDirectory + "file" + str(0) + "SEGMENT_VER_" + str(mixNum) + ".mp3", format="mp3")
    for i in range(numberOfAudios - 1):
        segments[sorted_indexes[i+1]].export(currentDirectory + "file" + str(i+1) + "SEGMENT_VER_" + str(mixNum) + ".mp3", format="mp3")
        combined = combined.overlay(segments[sorted_indexes[i+1]], loop=True)



    combined.export(finalsDirectory + str(mixNum) + ".mp3", format="mp3")
    combined.export(currentDirectory + "mixup_VER_" + str(mixNum) + ".mp3", format="mp3")


