# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from pydub import AudioSegment
import random
SECONDS_TO_MS_CONSTANT = 1000
END_AUDIO_MIN_LENGTH_SECONDS = 30


audio1 = AudioSegment.from_file("file1.mp3")
audio2 = AudioSegment.from_file("file2.mp3")

audios = [audio1, audio2]

numberOfVariants = 5

for mixNum in range(numberOfVariants):


    numberOfAudios = len(audios)



    audiosLengths = [10 * SECONDS_TO_MS_CONSTANT for _ in range(numberOfAudios)]

    audiosStartStampMs = [(random.randint(0 , len(audios[i]) - audiosLengths[i] - 1)) for i in range(numberOfAudios)]

    segments = [ audios[i][audiosStartStampMs[i]:audiosStartStampMs[i]+audiosLengths[i]] for i in range(numberOfAudios) ]

    combined = segments[0]
    segments[0].export("file" + str(0) + "SEGMENT.mp3", format="mp3")
    for i in range(numberOfAudios - 1):
        segments[i+1].export("file" + str(i+1) + "SEGMENT.mp3", format="mp3")
        combined = combined.overlay(segments[i+1])



    combined.export("mixup" + str(mixNum) + ".mp3", format="mp3")


