#!/usr/bin/env python
#
# This is a simple script to convert the watson transcript to
# something a little easier to skim. It color codes the words based on
# individual confidences, and puts delay markers in for every 100 ms
# of speech delay. This makes it a bit easier to parse than the run on
# blocks.

import json

data = json.load(open('watson-transcript.json'))

# print(data)

words = []

for r in data["results"]:
    conf = r["alternatives"][0]["word_confidence"]
    times = r["alternatives"][0]["timestamps"]
    for i in range(len(conf)):
        conf[i].extend((times[i][1], times[i][2]))
    words.extend(conf)

print """
<html>
<header>
<style>
.confidence_10 { color: #000000 }
.confidence_9 { color: #220000 }
.confidence_8 { color: #440000}
.confidence_7 { color: #660000 }
.confidence_6 { color: #880000 }
.confidence_5 { color: #aa0000}
.confidence_4 { color: #cc0000 }
.confidence_3 { color: #ee0000 }
.confidence_2 { color: #ff2200 }
.confidence_1 { color: #ff4400 }
.confidence_0 { color: #ff6600 }
.main {width: 480px; margin:0 auto;}
</style>
</header>
<body>
<div class="main">
"""

lastend = 0

for word in words:
    w, score, start, end = word
    space = start - lastend
    if 0.1 < space <= 0.3:
        print ", "
    elif 0.3 < space:
        num = int(space * 10)
        print "." * num

    print '<span title="Confidence %f; Timestamp %.2fs-%.2fs" class="confidence_%d">%s</span> ' % (score, start, end, score * 10, w)
    lastend = end

print """
</div>
</body>
</html>
"""
