# Last Word Checksum and XFP Calculator

## THIS REPOSITORY COMES WITH ZERO GUARANTEES. USE AT YOUR OWN RISK!

## Instructions:
1. Open Electrum Console tab
2. Enter the following (replace with your seed's first words):
```python
first_words = "abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon"
```
3. Paste the code from [oneline.py](https://raw.githubusercontent.com/mflaxman/human-rng-electrum/master/oneline.py) into the console (it will use whatever you set `first_words` to in the previous step).
4. Private results (last word checksum) will be printed to the screen
5. Public results (extended public key, root fingerprint, and derivation path) are printed to the screen and saved to a file (for export to your multisig setup) in your `/tmp` directory

**Note: it is strongly recommended to perform all these steps (including below) offline on an airgapped machine, preferably using [Tails](https://tails.boum.org/).**

#### Example
Using the following **INSECURE** `first_words`:  
`first_words = "zoo zoo zoo zoo zoo zoo zoo zoo zoo zoo zoo zoo zoo zoo zoo zoo zoo zoo zoo zoo zoo zoo zoo"`

Which generates the following output:
```
***************************************************************************************************
Running on network BitcoinMainnet...

PRIVATE SECRET TO WRITE DOWN (24 words total):

  zoo zoo zoo zoo zoo zoo zoo zoo zoo zoo zoo zoo zoo zoo zoo zoo zoo zoo zoo zoo zoo zoo zoo buddy

PUBLIC KEY INFO TO LOAD INTO SPECTER-DESKTOP (also saved to /tmp/humanrngxp-669DCE62.json):

  [669DCE62/48'/0'/0'/2']Zpub74sb5KB3Ak1RwabGr8SHQnMTkd2mC3boVDgPf1jBFNxcXh7Nx4KV3XakPDtWLN5RpszdM7qcBN4wm7xreh8Ys2xYUBqQ9GtkTN8h5kRVecc
```

![](example.png)

You can confirm this matches SeedPicker:  
<http://seedpicker.net/calculator/last-word.html>

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

Select `Python 3` radio button, paste your code, and  hit `Convert`.

#### Save the Resulting File
This is how [oneline.py](oneline.py) was created.

On MacOS, you can run:
```bash
$ pbpaste > oneline.py
```

Now you can use the steps at the top to calculate your last word checksum and root fingerpint.
