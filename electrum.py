from electrum.keystore import from_bip39_seed, bip39_is_checksum_valid, Wordlist
from electrum import constants
import json


def get_last_word(first_words):
    _, is_wordlist_valid = bip39_is_checksum_valid(first_words)
    if is_wordlist_valid is False:
        raise Exception("Invalid BIP39 Word in first_words: %s" % first_words)

    # Find last word
    for word in Wordlist.from_file("english.txt"):
        challenge = first_words + " " + word
        is_checksum_valid, _ = bip39_is_checksum_valid(challenge)
        if is_checksum_valid:
            return word

    raise Exception("Can't find valid checksum word")


def calculate_seed_and_xpubs(first_words):
    first_words = first_words.strip()
    last_word = get_last_word(first_words=first_words)
    whole_seed = first_words + " " + last_word
    is_checksum_valid, _ = bip39_is_checksum_valid(whole_seed)
    assert is_checksum_valid is True

    if constants.net == constants.BitcoinMainnet:
        derivation_path = "m/48'/0'/0'/2'"
    elif constants.net == constants.BitcoinTestnet:
        derivation_path = "m/48'/1'/0'/2'"
    else:
        raise Exception("Invalid Network: %s" % constants.net)

    ks = from_bip39_seed(seed=whole_seed, passphrase="", derivation=derivation_path)

    return (
        {
            "last_word": last_word,
            "whole_seed": whole_seed,
            "whole_seed_word_count": len(whole_seed.split()),
        },
        {
            "xfp": ks.get_root_fingerprint().upper(),  # uppercase to match others, unsure if that matters
            "p2wsh": ks.get_master_public_key(),
            "p2wsh_deriv": derivation_path,
        },
    )

has_firstwords = False
try:
    first_words
    has_firstwords = True
except NameError:
    print('\n`first_words` not supplied!')
    print('You must first set first_words like this:')
    print('firstwords = "able baby cake ..."')
    print('Substitute your own first 23 words of your seed phrase (without ...) and run this command again', '\n')


if has_firstwords:
    last_word_dict, specter_dict = calculate_seed_and_xpubs(first_words=first_words)
    result = "  [{}/{}]{}".format(
        specter_dict["xfp"], specter_dict["p2wsh_deriv"][2:], specter_dict["p2wsh"]
    )

    print("\n", "*" * 99)
    print("Running on network %s...\n" % constants.net.__name__)

    # Write to coldcard xpub file (not needed, but can be useful to experts in airgap wallet creation)
    f_output = '/tmp/humanrngxp-%s.json' % specter_dict['xfp']
    with open(f_output, 'w') as f:
        f.write(json.dumps(specter_dict, indent=4))

    print("\nPRIVATE SECRET TO WRITE DOWN (%s words total):" % last_word_dict.pop("whole_seed_word_count"), "\n")
    print("  %s" % last_word_dict.pop("whole_seed"))

    print("\n", "PUBLIC KEY INFO TO LOAD INTO SPECTER-DESKTOP (also saved to %s):" % f_output, "\n")
    print(result, "\n")
