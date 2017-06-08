#!/usr/bin/env python

import os
import time

from google.cloud import storage
from google.cloud import exceptions as gex
from google.cloud.gapic.speech.v1 import speech_client
from google.cloud.gapic.speech.v1 import enums
from google.cloud.proto.speech.v1 import cloud_speech_pb2
from google.protobuf import json_format

BUCKET="transcribe-test"
FILE="podcast.flac"

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "auth.json"

print("Creating bucket")

client = storage.Client()
bucket = client.lookup_bucket(BUCKET)
if not bucket:
    bucket = client.create_bucket(BUCKET)

print("Uploading Podcast")
blob = storage.Blob(FILE, bucket)
blob.upload_from_filename(FILE)

sclient = speech_client.SpeechClient()
encoding = enums.RecognitionConfig.AudioEncoding.FLAC
sample_rate_hertz = 16000
language_code = 'en-US'
config = cloud_speech_pb2.RecognitionConfig(
    encoding=encoding,
    sample_rate_hertz=sample_rate_hertz,
    language_code=language_code)
uri = 'gs://%s/%s' % (BUCKET, FILE)
audio = cloud_speech_pb2.RecognitionAudio(uri=uri)
response = sclient.long_running_recognize(config, audio)

def callback(operation_future):
    # Handle result.
    result = operation_future.result()
    with open("google-transcript.json", "w") as f:
        f.write(json_format.MessageToJson(result))
    print("Done!")

response.add_done_callback(callback)
print("Running speech recognition")
