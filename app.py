#!/usr/bin/env python

import os
import sys
args = sys.argv[1:]
relpath = args[0] if args else '.'
path = os.path.abspath(relpath)
print "Watching "+path

import dropbox
app_key = 'iejck3u2kmmm65e'
app_secret = 'damh69bugl5zgii'
flow = dropbox.client.DropboxOAuth2FlowNoRedirect(app_key, app_secret)

authorize_url = flow.start()
print '1. Go to: ' + authorize_url
print '2. Click "Allow" (you might have to log in first)'
print '3. Copy the authorization code.'
code = raw_input("Enter the authorization code here: ").strip()
access_token, user_id = flow.finish(code)

client = dropbox.client.DropboxClient(access_token)
print 'linked account: ', client.account_info()

import time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

class MyHandler(PatternMatchingEventHandler):
  patterns = ["*"]

  """
  event.event_type
      'modified' | 'created' | 'moved' | 'deleted'
  event.is_directory
      True | False
  event.src_path
      path/to/observed/file
  """
  def on_created(self, event):
    print event.src_path
    if event.is_directory:
      print "skipping dir"
    else:
      f = open(event.src_path)
      response = client.put_file(event.src_path, f)
      print 'uploaded: ', response

if __name__ == '__main__':
  observer = Observer()
  observer.schedule(MyHandler(), path=path, recursive=True)
  observer.start()

  try:
    while True:
        time.sleep(1)
  except KeyboardInterrupt:
    observer.stop()

  observer.join()
