"""Functions for creating, transforming, and adding prefixes to strings."""


def add_prefix_un(word):
    un_word = 'un' + word
    return un_word

def make_word_groups(vocab_words):
    prefix = vocab_words[0]
    vocab_words_no_prefix = vocab_words[1:]
    prefix_words=prefix+ (' :: '+prefix).join(vocab_words_no_prefix)
    return prefix+' :: '+prefix_words


def remove_suffix_ness(word):
    word_no_suffix = word[:-4]
    if word_no_suffix[-1] == 'i':
        return word_no_suffix[:-1]+'y'
    return word_no_suffix

def adjective_to_verb(sentence, index):
    """Change the adjective within the sentence to a verb.

    :param sentence: str - that uses the word in sentence.
    :param index: int - index of the word to remove and transform.
    :return: str - word that changes the extracted adjective to a verb.

    For example, ("It got dark as the sun set.", 2) becomes "darken".
    """
    words = sentence.split()
    words[-1]=words[-1][:-1]#removes the "."
    adj = words[index]
    return adj+'en'
