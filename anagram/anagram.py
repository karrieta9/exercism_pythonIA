def find_anagrams(word, candidates):
    response = []
    word = word.lower()

    for candidate in candidates:
        if sorted(word) == sorted(candidate.lower()) and candidate.lower() != word:
            response.append(candidate)
    return response
