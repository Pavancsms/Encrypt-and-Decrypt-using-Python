import os, time,subprocess
path_to_watch = "C:\synchfiles"
before = dict ([(f, None) for f in os.listdir (path_to_watch)])
while 1:
  time.sleep (10)
  after = dict ([(f, None) for f in os.listdir (path_to_watch)])
  added = [f for f in after if not f in before]
  removed = [f for f in before if not f in after]
  if added: subprocess.call("python assignment1.py C:/synchfiles/" + ''.join(added), shell=True)
  if removed: print "Removed: ", ", ".join (removed)
  before = after