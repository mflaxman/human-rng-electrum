# Last Word Checksum and XFP Calculator

## THIS REPOSITORY COMES WITH ZERO GUARANTEES. USE AT YOUR OWN RISK!

## Instructions:
1. Open Electrum Console tab
2. Enter the following (replace with your seed's first words):
```python
first_words = "abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon"
```
3. Paste the code from [oneline.py](oneline.py) into the console (it will use whatever you set `first_words` to in the previous step).
4. Private results (last word checksum) will be printed to the screen
5. Public results (extended public key, root fingerprint, and derivation path) are printed to the screen and saved to a file (for export to your multisig setup) in your `/tmp` directory

**Note: it is strongly recommended to perform all these steps (including below) offline on an airgapped machine, preferably using [Tails](https://tails.boum.org/).**

---

## Build Steps For Trust Minimization
Yes, this is sketchy!
Electrum console has poor copy-paste support. We need our whole code in one-line.

#### Copy Code to Clipboard
Take the code from this repo (see `electrum.py`) and load it into your clipboard.

On MacOS, you can run:
```bash
$ cat electrum.py | pbcopy
```

#### Convert to One-Line
Convert code in your clipboard to one-liner on this website:
https://jagt.github.io/python-single-line-convert/

Select `Python 3`, paste your code, and  hit `Convert`.

#### Save the Resulting File
This is how [oneline.py](oneline.py) was created.

On MacOS, you can run:
```bash
$ pbpaste > oneline.py
```

Now you can use the steps at the top to calculate your last word checksum and root fingerpint.
