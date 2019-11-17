import Quartz, subprocess


was_locked = False
while True:
    d = Quartz.CGSessionCopyCurrentDictionary()
    if not 'CGSSessionScreenIsLocked' in d.keys():
        if was_locked:
            subprocess.call(["afplay", "jingle.mp3"])
            was_locked = False
    else:
        was_locked = True
