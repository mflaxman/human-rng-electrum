from electrum.keystore import from_bip39_seed, bip39_is_checksum_valid, Wordlist
import json, textwrap


def get_last_word(first_words):
    _, is_wordlist_valid = bip39_is_checksum_valid(first_words)
    if is_wordlist_valid is False:
        raise Exception("Bad Word in First Words: %s" % first_words)

    # Find last word
    for word in Wordlist.from_file("english.txt"):
        challenge = first_words + " " + word
        is_checksum_valid, _ = bip39_is_checksum_valid(challenge)
        if is_checksum_valid:
            return word

    raise Exception("Can't find valid checksum word")


def calculate_seed_and_xpubs(first_words):
    last_word = get_last_word(first_words=first_words)
    whole_seed = first_words + " " + last_word
    is_checksum_valid, _ = bip39_is_checksum_valid(whole_seed)
    assert is_checksum_valid is True

    derivation_path = "m/48'/0'/0'/2'"
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


last_word_dict, specter_dict = calculate_seed_and_xpubs(first_words=first_words)
result = "  [{}/{}]{}".format(
    specter_dict["xfp"], specter_dict["p2wsh_deriv"][2:], specter_dict["p2wsh"]
)

# print(json.dumps(specter_dict, indent=4))  ## Can be used for ccxp-*.json file, but relying on Specter for this instead
print("\n", "*" * 99, "\n")
print("PRIVATE SECRET TO WRITE DOWN:", "\n")
print(textwrap.indent(text=json.dumps(last_word_dict, indent=2), prefix="  "))

print("\n", "PUBLIC KEY INFO TO LOAD INTO SPECTER-DESKTOP:", "\n")
print(result, "\n")
