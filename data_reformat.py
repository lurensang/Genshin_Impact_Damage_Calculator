import json

def del_space(old_str,start_index, end_index):
    temp_str = old_str[start_index:end_index]
    temp_str = temp_str.replace('\n', '')
    temp_str = temp_str.replace(' ', '')
    temp_str = temp_str.replace(',', ', ')
    new_str_seg = temp_str
    return new_str_seg

def reformat(attr_dict):
    attr_str = json.dumps(attr_dict, indent=4, ensure_ascii=False)

    ind = []
    unchange_seg_start = 0
    unchange_seg_end = 0
    new_str = ''
    for i, j in enumerate(attr_str):
        if j == '[':
            ind.append(i)
            if len(ind) == 2:
                unchange_seg_end = i
                new_str += attr_str[unchange_seg_start:unchange_seg_end]
        elif j == ']':
            if len(ind) == 2:
                new_str_seg = del_space(attr_str, ind[-1], i+1)
                unchange_seg_start = i+1
                new_str += new_str_seg
            del(ind[-1])
    new_str += attr_str[unchange_seg_start:]
    return new_str