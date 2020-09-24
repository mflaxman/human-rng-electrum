exec("""\nfrom electrum.keystore import from_bip39_seed, bip39_is_checksum_valid, Wordlist\nfrom electrum import constants\nimport json\n\n\ndef get_last_word(first_words):\n    _, is_wordlist_valid = bip39_is_checksum_valid(first_words)\n    if is_wordlist_valid is False:\n        raise Exception("Invalid BIP39 Word in first_words: %s" % first_words)\n\n    # Find last word\n    for word in Wordlist.from_file("english.txt"):\n        challenge = first_words + " " + word\n        is_checksum_valid, _ = bip39_is_checksum_valid(challenge)\n        if is_checksum_valid:\n            return word\n\n    raise Exception("Can't find valid checksum word")\n\n\ndef calculate_seed_and_xpubs(first_words):\n    first_words = first_words.strip()\n    last_word = get_last_word(first_words=first_words)\n    whole_seed = first_words + " " + last_word\n    is_checksum_valid, _ = bip39_is_checksum_valid(whole_seed)\n    assert is_checksum_valid is True\n\n    if constants.net == constants.BitcoinMainnet:\n        derivation_path = "m/48'/0'/0'/2'"\n    elif constants.net == constants.BitcoinTestnet:\n        derivation_path = "m/48'/1'/0'/2'"\n    else:\n        raise Exception("Invalid Network: %s" % constants.net)\n\n    ks = from_bip39_seed(seed=whole_seed, passphrase="", derivation=derivation_path)\n\n    return (\n        {\n            "last_word": last_word,\n            "whole_seed": whole_seed,\n            "whole_seed_word_count": len(whole_seed.split()),\n        },\n        {\n            "xfp": ks.get_root_fingerprint().upper(),  # uppercase to match others, unsure if that matters\n            "p2wsh": ks.get_master_public_key(),\n            "p2wsh_deriv": derivation_path,\n        },\n    )\n\n\nhas_firstwords = False\ntry:\n    first_words\n    has_firstwords = True\nexcept NameError:\n    print("\\n`first_words` not supplied!")\n    print("You must first set first_words like this:")\n    print('firstwords = "able baby cake ..."')\n    print(\n        "Substitute your own first 23 words of your seed phrase (without ...) and run this command again",\n        "\\n",\n    )\n\n\nif has_firstwords:\n    last_word_dict, specter_dict = calculate_seed_and_xpubs(first_words=first_words)\n    result = "  [{}/{}]{}".format(\n        specter_dict["xfp"], specter_dict["p2wsh_deriv"][2:], specter_dict["p2wsh"]\n    )\n\n    print("\\n", "*" * 99)\n    print("Running on network %s...\\n" % constants.net.__name__)\n\n    # Write to coldcard xpub file (not needed, but can be useful to experts in airgap wallet creation)\n    f_output = "/tmp/humanrngxp-%s.json" % specter_dict["xfp"]\n    with open(f_output, "w") as f:\n        f.write(json.dumps(specter_dict, indent=4))\n\n    print(\n        "\\nPRIVATE SECRET TO WRITE DOWN (%s words total):"\n        % last_word_dict.pop("whole_seed_word_count"),\n        "\\n",\n    )\n    print("  %s" % last_word_dict.pop("whole_seed"))\n\n    print(\n        "\\n",\n        "PUBLIC KEY INFO TO LOAD INTO SPECTER-DESKTOP (also saved to %s):" % f_output,\n        "\\n",\n    )\n    print(result, "\\n")\n""")
