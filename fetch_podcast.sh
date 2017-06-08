#!/bin/bash

set -eux

PODCAST_URL=${PODCAST_URL:-http://audio.commonwealthclub.org/audio/podcast/cc_20170323_Zip_Code_Not_Genetic_Code_Podcast.mp3}
FILE=$(basename $PODCAST_URL)

wget -O $FILE $PODCAST_URL

echo "Converting to flac for cloud services"
ffmpeg -i $FILE -ar 16000 podcast.flac

echo "Converting to wav for CMU Sphinx"
ffmpeg -i $FILE -ar 16000 podcast.wav
