def _check_(temp, ind, pos_res):
    if len(temp) == ind:
        return pos_res
    else:
        return -1

def check_fin(res):
    return res != -1

def pattern_find():
    s = str(input())
    template = str(input())
    is_started = False
    result = -1
    ind_s = 0
    ind_t = 0
    possible_res = -1
    for ind_s in range(len(s)):
        if s[ind_s] == template[ind_t] and is_started:
            ind_t += 1
            result = _check_(template, ind_t, possible_res)
            if check_fin(result):
                break
        elif s[ind_s] == template[ind_t] and not is_started:
            is_started = True
            possible_res = ind_s
            ind_t += 1
            result = _check_(template, ind_t, possible_res)
            if check_fin(result):
                break
        elif is_started and template[ind_t] == "@":
            ind_t += 1
            result = _check_(template, ind_t, possible_res)
            if check_fin(result):
                break
            continue
        elif template[ind_t] == "@" and not is_started:
            is_started = True
            possible_res = ind_s
            ind_t += 1
            result = _check_(template, ind_t, possible_res)
            if check_fin(result):
                break
        elif s[ind_s] != template[ind_t]:
            ind_t = 0
            possible_res = -1
            is_started = False if s[ind_s] != template[ind_t] and template[ind_t] != "@" else True
            if is_started:
                possible_res = ind_s
                ind_t += 1
                result = _check_(template, ind_t, possible_res)
                if check_fin(result):
                    break

    if len(template) == ind_t:
        result = possible_res
    return result

print(pattern_find())