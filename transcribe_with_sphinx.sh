#!/bin/bash

set -eux

FILE=${FILE:-podcast.wav}

pocketsphinx_continuous -dict /usr/share/pocketsphinx/model/en-us/cmudict-en-us.dict -lm /usr/share/pocketsphinx/model/en-us/en-us.lm.bin -infile $FILE 2> sphinx-voice-debug.log | tee sphinx-transcription.log
