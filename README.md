watch a directory, sending new files to your dropbox

## dependencies

if you're on a system with python and pip available, but no root access, setup like so:

```
pip install --user watchdog dropbox
```

## usage

* run `app.py path/to/watch`
* confirm that the path is correct
* follow the instructions to auth with Dropbox
* move (or have some other script move) files into the path

directories are OK, Dropbox handles them nicely

this script does not delete anything, consider it a one-way sync out to dropbox
