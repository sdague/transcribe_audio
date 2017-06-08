==========================
 Transcribe Podcast Audio Testing
==========================

This is a repository demonstrating transcribing podcast audio with a
few different services: IBM Watson Speech to Text, Google Cloud
Speech, and CMU Sphinx.

Getting Started
===============

First run ``fetch_podcast.sh`` to pull some content down for
converting. The example from my blog post is used, though you can
replace the URL if you like to try with other content.

Running CMU Sphinx
==================

Ensure that sphinx is installed. On Ubuntu this is done with

::
   sudo apt-get install pocketsphinx pocketsphinx-en-us

Then run ``transcribe_with_sphinx.sh``. It will produce
``sphinx-transcription.log`` as output.

Running Watson
==============

Sign up for IBM Bluemix and create a Watson Speech to Text instance.

Install python prereqs

::
   pip install watson-developer-cloud
