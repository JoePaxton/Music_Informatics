import numpy
import math
import matplotlib.pyplot as plt
from echonest.remix import audio

# Track ID for the local audio file that is going to get analyzed

segments = audio.AudioAnalysis('TRLCMRN1485B3F5150').segments

# main()
def main():
    timbre,pitches = matrix()
    plot1= plt.imshow(timbre)
    plot2 = plt.imshow(pitches)
    
    plot1.set_cmap('hot')
    plot2.set_cmap('hot')
    plt.colorbar()
    plt.show()

# This function calculates the Euclidean Distance
# for pitches and timbre between each segment of
# the song.
def matrix():
    dist = 0.0
    seg = (len(segments), len(segments))
    timbreMatrix = numpy.zeros(seg)
    pitchesMatrix = numpy.zeros(seg)

    for i in range(len(segments)):
        for j in range(len(segments)):
            dist = euclid(segments[i].timbre, segments[j].timbre)
            timbreMatrix[i][j] = dist

    for items in range(len(segments)):
        for stuff in range(len(segments)):
            dist = euclid(segments[items].pitches, segments[stuff].pitches)
            pitchesMatrix[items][stuff] = dist

    return timbreMatrix, pitchesMatrix

def euclid(a,b):
    dist = 0.0
    euclid = 0.0

    for i in range(len(a)):
        dist = dist + (a[i] - b[i])**2
    euclid = math.sqrt(dist)
    return euclid

if __name__ == "__main__":
    main()
