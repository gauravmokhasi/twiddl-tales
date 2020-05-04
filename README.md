# twiddl-tales
Twiddl Tales allows users to create stories that unfold in quasi-real time on slack through pre-created bots.

## To run twiddle tales
- install python 3 (https://www.python.org/downloads/)
- download https://github.com/gauravmokhasi/twiddl-tales/blob/master/twiddl-tales.py.
- add a dialogue file like https://github.com/gauravmokhasi/twiddl-tales/blob/master/example-text.txt to the same folder as twiddl-tales.py. the format of the file is (character name) ~ (line) ~ (delay after line in seconds)
- add a bindings file containing character names and the incoming webhook url of the slack bot associated with the character: similar to https://github.com/gauravmokhasi/twiddl-tales/blob/master/bindings.txt
- run https://github.com/gauravmokhasi/twiddl-tales/blob/master/twiddl-tales.py
- open the slack channel with your bots 

## prework
- setup slack bots in your workspace
- give slack bots oauth permissions for incoming webhooks and chat write; install them to the appropriate channel
- add the incoming webhook url to bindings.txt
