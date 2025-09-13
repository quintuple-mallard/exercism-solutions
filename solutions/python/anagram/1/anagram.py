def find_anagrams(word, candidates):
    sorted_word = "".join(sorted(word.lower()))
    anagrams = []
    sorted_candidates = list(
        map(
            lambda item: "".join(sorted(item)), 
            map(lambda item: item.lower(), candidates)
        )
    )
    for i, item in enumerate(sorted_candidates):
        if item == sorted_word and word.lower() != candidates[i].lower():
            anagrams.append(candidates[i])

    return anagrams
