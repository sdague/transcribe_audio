#!/usr/bin/env python
#
# Copyright 2017 IBM
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import argparse
import ConfigParser
import json
from os.path import join, dirname
from watson_developer_cloud import SpeechToTextV1


def get_auth():
    config = ConfigParser.RawConfigParser()
    config.read('auth.cfg')
    user = config.get('watson', 'username')
    password = config.get('watson', 'password')
    return (user, password)


def parse_args():
    parser = argparse.ArgumentParser(
        description='Transcribe audio with watson')
    parser.add_argument('file')
    parser.add_argument('--customization', help="Process using a customized model id")
    args = parser.parse_args()
    return args

def main():
    args = parse_args()
    (user, passwd) = get_auth()
    speech_to_text = SpeechToTextV1(
        username=user,
        password=passwd,
        x_watson_learning_opt_out=False
    )

    speech_to_text.get_model('en-US_BroadbandModel')

    with open(args.file, 'rb') as audio_file:
        print("Sending audio to watson to recognize, this will take 30+ minutes")
        if args.customization is not None:
            print("Using custom model {0}".format(args.customization))
        print("Please be patient and don't kill this process while running")
        output = speech_to_text.recognize(
            audio_file, content_type='audio/flac', timestamps=True,
            customization_id=args.customization,
            word_confidence=True)
        with open("watson-transcript.json", "w") as out:
            print("Transcription done, written to watson-transcription.json")
            out.write(json.dumps(output, indent=2))

if __name__ == "__main__":
    main()
