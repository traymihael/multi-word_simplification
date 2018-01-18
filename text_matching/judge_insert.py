import pos_exchange as pos_ex
import copy

def check_in(pos_left, pos_right, inserted_pos):

    if pos_left == 'noun' and pos_right == 'noun':
        for pos in inserted_pos:
            if pos != 'noun' and pos != 'adj':
                return 0

    elif pos_left == 'noun' and pos_right == 'prep':
        for pos in inserted_pos:
            if pos != 'noun' and pos != 'adj' and pos != 'adv':
                return 0

    elif pos_left == 'noun' and pos_right == 'adj':
        for pos in inserted_pos:
            if pos != 'adj' and pos != 'adv':
                return 0

    elif pos_left == 'noun' and pos_right == 'verb':
        for pos in inserted_pos:
            if pos != 'adv' and pos != 'aux':
                return 0

    elif pos_left == 'adj' and pos_right == 'noun':
        for pos in inserted_pos:
            if pos != 'noun' and pos != 'adj' and pos != 'adv':
                return 0

    elif pos_left == 'adj' and pos_right == 'prep':
        for pos in inserted_pos:
            if pos != 'noun':
                return 0

    elif pos_left == 'adv' and pos_right == 'adj':
        for pos in inserted_pos:
            if pos != 'adv':
                return 0

    elif pos_left == 'adv' and pos_right == 'adv':
        for pos in inserted_pos:
            if pos != 'adv':
                return 0

    elif pos_left == 'adv' and pos_right == 'prep':
        for pos in inserted_pos:
            if pos != 'adv':
                return 0

    elif pos_left == 'adv' and pos_right == 'verb':
        for pos in inserted_pos:
            if pos != 'adv':
                return 0

    elif pos_left == 'conj' and pos_right == 'verb':
        for pos in inserted_pos:
            if pos != 'adv':
                return 0

    elif pos_left == 'conj' and pos_right == 'prep':
        for pos in inserted_pos:
            if pos != 'adv':
                return 0

    elif pos_left == 'conj' and pos_right == 'noun':
        for pos in inserted_pos:
            if pos != 'adj':
                return 0

    elif pos_left == 'verb' and pos_right == 'adv':
        for pos in inserted_pos:
            if pos != 'adv' and pos != 'adj':
                return 0

    elif pos_left == 'verb' and pos_right == 'noun':
        for pos in inserted_pos:
            if pos != 'noun' and pos != 'adj':
                return 0

    elif pos_left == 'verb' and pos_right == 'adj':
        for pos in inserted_pos:
            if pos != 'adv' and pos != 'adj':
                return 0

    elif pos_left == 'verb' and pos_right == 'prep':
        for pos in inserted_pos:
            if pos != 'adv' and pos != 'adj':
                return 0

    elif pos_left == 'prep' and pos_right == 'noun':
        for pos in inserted_pos:
            if pos != 'noun' and pos != 'adj':
                return 0

    elif pos_left == 'prep' and pos_right == 'adj':
        for pos in inserted_pos:
            if pos != 'adv' and pos != 'adj' and pos != 'noun':
                return 0

    elif pos_left == 'det' and pos_right == 'adj':
        for pos in inserted_pos:
            if pos != 'adj' and pos != 'adv' and pos != 'noun':
                return 0

    elif pos_left == 'det' and pos_right == 'noun':
        for pos in inserted_pos:
            if pos != 'adv' and pos != 'adj' and pos != 'noun':
                return 0

    elif pos_left == 'pospro' and pos_right == 'noun':
        for pos in inserted_pos:
            if pos != 'adj' and pos != 'noun':
                return 0

    elif pos_left == 'perpro' and pos_right == 'noun':
        for pos in inserted_pos:
            if pos != 'adj':
                return 0

    elif pos_left == 'perpro' and pos_right == 'adv':
        for pos in inserted_pos:
            if pos != 'adv':
                return 0

    elif pos_left == 'perpro' and pos_right == 'prep':
        for pos in inserted_pos:
            if pos != 'adj' and pos != 'adv':
                return 0
    else:
        return 0

    return 1

def inserte_check(word_pos, insert):
    candidate = []
    inserted = copy.deepcopy(insert)
    insert = inserted.copy()
    for i in range(len(insert)):
        for j in range(len(insert[i])):
            for k in range(len(insert[i][j])):
                insert[i][j][k] = pos_ex.pos_exchange_parse(insert[i][j][k])

    #return 候補の番号　0:複合語でない、1:複合語である
    for i in range(len(insert)):
        flag = 1
        for j in range(len(insert[i])):
            if 'X' in insert[i][j]:
                flag = 0
                break
        if flag == 1:
            candidate.append(i)

    for i in candidate:
        flag2 = 1
        for j in range(len(word_pos)-1):

            if len(insert[i][j]) == 0:
                continue
            #2つ以上の挿入がある場合は除去
            if len(insert[i][j]) >= 2:
                #print(insert[i][j])
                flag2 = 0
                break
            left = word_pos[j]
            
            for k in range(len(insert[i][j])-1):
                right = insert[i][j][k+1]
                if not check_in(left, right, [insert[i][j][k]]):
                    flag2 = 0
                    break
                left = insert[i][j][k]

            if flag2 == 0:
                break
            
            if not check_in(left, word_pos[j+1], [insert[i][j][-1]]):
                flag2 = 0
                break
        if flag2:
            return i, 1

    return 0, 0