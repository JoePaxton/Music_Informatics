#!/usr/bin/env python
# encoding: utf=8
"""
one_segment.py

Appends each item in the children of each section into a new list, creating a new audio file.

Joe Paxton

10 February 2015
"""
import echonest.remix.audio as audio

usage = """
Usage: 
    python one_segment.py <input_filename> <output_filename>

Example:
    python one_segment.py lateralus.mp3 output.mp3
"""

def main(input_filename, output_filename):
    # Returns results of the input track.
    audiofile = audio.LocalAudioFile(input_filename)
    # Gets a list of every section in the track.
    sections = audiofile.analysis.sections
    # New list for AudioQuantums.
    collect = audio.AudioQuantumList()
    # Loops through the first item in the children of each section into the new list.
    for sec in sections:
        collect.append(sec.children()[0])
    # Audio defined in collect from analyzed audio file.
    out = audio.getpieces(audiofile, collect)
    # Writes the new audio.
    out.encode(output_filename)

if __name__ == '__main__':
    import sys
    try:
        input_filename = sys.argv[1]
        output_filename = sys.argv[2]
    except:
        print usage
        sys.exit(-1)
    main(input_filename, output_filename)
