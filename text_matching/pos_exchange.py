def pos_exchange_cefr(word, pos):
    cefr_pos = pos

    if pos == 'IN' or pos == 'TO' or pos == 'RP': cefr_pos = 'preposition'
    elif pos == 'VB' or pos == 'VBD' or pos == 'VBG' or pos == 'VBN' or pos == 'VB' or pos == 'VBP' or pos == 'VBZ': cefr_pos = 'verb'
    elif pos == 'DT' or pos == 'WDT': cefr_pos = 'determiner'
    elif pos == 'RB' or pos == 'RBR' or pos == 'RBS': cefr_pos = 'adverb'
    elif pos == 'JJ' or pos == 'JJR' or pos == 'JJS': cefr_pos = 'adjective'
    elif pos == 'NN' or pos == 'NNS' or pos == 'NNP' or pos == 'NNPS': cefr_pos = 'noun'
    elif pos == 'PRP' or pos == 'PRPS' or pos == 'PRP$' or pos == 'WP': cefr_pos = 'pronoun'
    elif pos == 'CC': cefr_pos = 'conjunction'
    elif pos == 'MD': cefr_pos = 'modal auxiliary'
    elif pos == 'UH': cefr_pos = 'interjection'
    elif pos == 'CD': cefr_pos = 'number'
    if cefr_pos == 'verb' and word == 'be': cefr_pos='be-verb'
    if cefr_pos == 'verb' and word == 'have': cefr_pos = 'have-verb'
    if cefr_pos == 'verb' and word == 'do': cefr_pos = 'do-verb'

    return cefr_pos

def pos_exchange_parse(pos):
    if pos == 'S' or pos == 'ROOT' or pos == 'SBAR' or pos == 'SBARQ' or pos == 'SINV':
        parse_pos = 'sentence'

    elif pos == 'NP' or pos == 'NNP' or pos == 'NNS' or pos == 'NN' or pos == 'PRP'\
        or pos == 'NNPS' or pos == 'FRAG' or pos == 'UCP' or pos == 'FW' or pos == 'NP-TMP':
        parse_pos = 'noun'

    elif pos == 'ADJP' or pos == 'JJ' or pos == 'DT' or pos == 'PRP$' or pos == 'QP' or pos == 'CONJP' \
        or pos == 'JJR' or pos == 'JJS' or pos == 'PDT' or pos == 'CD':
        parse_pos = 'adj'

    elif pos == 'RBS' or pos == 'RB' or pos == 'RBR' or pos == 'ADVP':
        parse_pos = 'adv'

    elif pos == 'MD':
        parse_pos = 'aux'

    elif pos == 'WHPP' or pos == 'RP' or pos == 'PRT' or pos == 'WHADVP' or pos == 'SQ' \
        or pos == 'WRB' or pos == 'VBD' or pos == 'VBN' or pos == "''" or pos == "``" or pos == "''" \
        or pos == 'WDT' or pos == 'WHNP' or pos == 'POS' or pos == 'X' or pos == 'VBP' or pos == ':' \
        or pos == 'VBP' or pos == ':' or pos == 'VBZ' or pos == 'VP' or pos == 'IN' or pos == 'PP' \
        or pos == 'VB' or pos == 'TO' or pos == 'CC' or pos == 'VBG' or pos == ',' or pos == '.' \
        or pos == 'WP':
        parse_pos = 'X'

    else:
        parse_pos = '???'

    return parse_pos

def pos_exchange_simple(pos):

    if pos == 'IN' or pos == 'TO' or pos == 'RP':
        simple_pos = 'prep'

    elif pos == 'VB' or pos == 'VBD' or pos == 'VBG' or pos == 'VBN' or pos == 'VB' or \
        pos == 'VBP' or pos == 'VBZ':
        simple_pos = 'verb'

    elif pos == 'DT' or pos == 'WDT':
        simple_pos = 'det'

    elif pos == 'RB' or pos == 'RBR' or pos == 'RBS':
        simple_pos = 'adv'

    elif pos == 'JJ' or pos == 'JJR' or pos == 'JJS' or pos == 'CD':
        simple_pos = 'adj'

    elif pos == 'NN' or pos == 'NNS' or pos == 'NNP' or pos == 'NNPS':
        simple_pos = 'noun'

    elif pos == 'CC':
        simple_pos = 'conj'

    elif pos == 'PRP$':
        simple_pos = 'posPro'

    elif pos == 'PRP':
        simple_pos = 'perPro'

    elif pos == 'UH' or pos == 'MD' or pos == 'PRPS' or pos == 'WP':
        simple_pos = 'other'

    else:
        simple_pos = 'XXXXX'

    return simple_pos