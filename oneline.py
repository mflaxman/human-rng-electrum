exec("""\nfrom electrum.keystore import from_bip39_seed, bip39_is_checksum_valid, Wordlist\nimport json\n\ndef get_last_word(first_words):\n    _, is_wordlist_valid = bip39_is_checksum_valid(first_words)\n    if is_wordlist_valid is False:\n        raise Exception("Bad Word in First Words: %s" % first_words)\n\n    # Find last word\n    for word in Wordlist.from_file("english.txt"):\n        challenge = first_words + " " + word\n        is_checksum_valid, _ = bip39_is_checksum_valid(challenge)\n        if is_checksum_valid:\n            return word\n\n    raise Exception("Can't find valid checksum word")\n\ndef calculate_seed_and_xpubs(first_words):\n    last_word = get_last_word(first_words=first_words)\n    whole_seed = first_words + " " + last_word\n    is_checksum_valid, _ = bip39_is_checksum_valid(whole_seed)\n    assert is_checksum_valid is True\n\n    derivation_path="m/48'/0'/0'/2'"\n    ks = from_bip39_seed(seed=whole_seed, passphrase="", derivation=derivation_path)\n\n    return ({\n        'last_word': last_word,\n        'whole_seed': whole_seed,\n        'whole_seed_len': len(whole_seed.split()),\n    }, {\n      'xfp': ks.get_root_fingerprint().upper(),  # uppercase to match others, unsure if that matters\n      'p2wsh': ks.get_master_public_key(),\n      'p2wsh_deriv': derivation_path,\n    })\n\nlast_word_dict, cc_export_dict = calculate_seed_and_xpubs(first_words=first_words)\nprint(json.dumps(last_word_dict, indent=4))\nprint(json.dumps(cc_export_dict, indent=4))\n\nf_output = '/tmp/ccxp-%s.json' % cc_export_dict['xfp']\nwith open(f_output, 'w') as f: f.write(json.dumps(cc_export_dict, indent=4))\nprint("Saved to: %s" % f_output)\n""")