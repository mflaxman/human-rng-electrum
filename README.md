# Last word checksum and XFP calculator

1. Open Electrum Console
2. Enter the following (replace with your seed's first words):
first_words = "abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon"
3. Paste the code from `oneline.py` into the console
4. Results will be printed to the screen and saved to a file.

## Build Steps
Yes, this is sketchy.
Electrum console has poor copy-paste support. We need our whole code in one-line.

## Convert to One-Liner

Take the code from this repo (see `electrum.py`) and load it into your clipboard.

On MacOS, you can run:
```bash
$ cat electrum.py | pbcopy
```

Then convert it to one liner on this website:
https://jagt.github.io/python-single-line-convert/

Select `Python 3`, paste your code, and  hit `Convert`.

Save the resulting file to `oneline.py`

On MacOS, you can run:
```bash
$ pbpaste > oneline.py
```
