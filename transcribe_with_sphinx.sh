#!/bin/bash

FILE=${FILE:-podcast.wav}

pocketsphinx_continuous -dict /usr/share/pocketsphinx/model/en-us/cmudict-en-us.dict -lm /usr/share/pocketsphinx/model/en-us/en-us.lm.bin -infile input.wav 2> sphinx-voice-debug.log | tee sphinx-transcription.log
