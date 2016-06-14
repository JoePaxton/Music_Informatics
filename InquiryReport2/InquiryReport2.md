#Problem

We want to slow down or speed up beats to produce different tempos (the pace of a musical composition) of a track 
in order to output an altered tempo audio file. Does [EchoNest] provide us with any answers?

# Questions
1. Does [EchoNest] provide us with the tools/attributes to get tempo and the time signature?
2. Does compressing or expanding beats help us change tempo?

# Resources
1. [EchoNest]
2. [stretch.py]

### 1. [EchoNest] tempo attribute:

The [EchoNest] provides us with infromation about the track's attributes. You can find the tempo and the
time signature of a track. When you print track.tempo a floating-point decimal value appears on the console,
which corresponds to the tempo. Can we use these specific tempo values in order to manipulate the original audio?

```python
import pyechonest.track as track

track = track.track_from_filename('C:\users\joe\desktop\lateralus.mp3')
track.tempo
print track.tempo
```

### 2. The relevance of [stretch.py]:

This example can be found on the [EchoNest Remix] API and it comes in a compressed zip folder of 
echo-nest-remix-examples. This expands or shrinks the entire track, beat by beat. You can manipulate
the timeScale function to change the time of a beat and you can create a new track from these modified
beats. When you import dirac, it only works on raw data for the first parameter and a floating-point 
ratio. If the ratio is greater than 0.5 than you can notice a difference in the pace of the track. The
higher the number you make the ratio the longer the time signature and expands the beats. This alters the
tempo dramatically if you are familiar with the particular audio file you have uploaded.

```python
import math
import os
import sys
import dirac
from echonest.remix import audio

audiofile = audio.LocalAudioFile(input_filename)
beats = audiofile.analysis.beats
collect = []

for beat in beats:
  beat_audio = beat.render()
  scaled_beat = dirac.timeScale(beat_audio.data, ratio)
  ts = audio.AudioData(ndarray=scaled_beat, shape=scaled_beat.shape,
      sampleRate=audiofile.sampleRate, numChannels=scaled_beat.shape[1])
  collect.append(ts)
  
out = audio.assemble(collect, numChannels=2)
out.encode(output_filename)
``` 
The render function gets the raw audio data from the beat and then is scaled by calling the
dirac.timeScale() function. After this we create a new AudioData object and append it to
an output list and write the output data. 

[EchoNest]: http://developer.echonest.com/docs/v4/
[EchoNest Remix]: http://echonest.github.io/remix/apidocs/  
[stretch.py]:https://github.com/echonest/remix/blob/master/examples/stretch/simple_stretch.py
