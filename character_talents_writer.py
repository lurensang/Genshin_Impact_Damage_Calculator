import json
from attr_fatcher import fatch_character_data
from traveler_attr_fatcher import fatch_traveler_data
from data_reformat import reformat

character_list = {'久岐忍':{'页面ID': 4148},
                  '夜兰':{'页面ID': 4081},
                  '旅行者(空)':{'页面ID': 4074},
                  '旅行者(荧)':{'页面ID': 4073},
                  '神里绫人':{'页面ID': 3875},
                  '八重神子':{'页面ID': 3564},
                  '云堇':{'页面ID': 3387},
                  '申鹤':{'页面ID': 3386},
                  '荒泷一斗':{'页面ID': 3276},
                  '五郎':{'页面ID': 3275},
                  '优菈':{'页面ID': 2040},
                  '阿贝多':{'页面ID': 1360},
                  '托马':{'页面ID': 2606},
                  '胡桃':{'页面ID': 1627},
                  '达达利亚':{'页面ID': 1220},
                  '雷电将军':{'页面ID': 2404},
                  '珊瑚宫心海':{'页面ID': 2403},
                  '埃洛伊':{'页面ID': 2415},
                  '宵宫':{'页面ID': 2124},
                  '神里绫华':{'页面ID': 2123},
                  '枫原万叶':{'页面ID': 2142},
                  '温迪':{'页面ID': 57},
                  '刻晴':{'页面ID': 1058},
                  '莫娜':{'页面ID': 1057},
                  '可莉':{'页面ID': 55},
                  '琴':{'页面ID': 59},
                  '迪卢克':{'页面ID': 75},
                  '七七':{'页面ID': 1056},
                  '魈':{'页面ID': 1498},
                  '钟离':{'页面ID': 1290},
                  '甘雨':{'页面ID': 1433},
                  '早柚':{'页面ID': 2125},
                  '九条裟罗':{'页面ID': 2402},
                  '凝光':{'页面ID': 78},
                  '菲谢尔':{'页面ID': 382},
                  '班尼特':{'页面ID': 105},
                  '丽莎':{'页面ID': 92},
                  '行秋':{'页面ID': 241},
                  '迪奥娜':{'页面ID': 1221},
                  '安柏':{'页面ID': 54},
                  '重云':{'页面ID': 644},
                  '雷泽':{'页面ID': 56},
                  '芭芭拉':{'页面ID': 61},
                  '罗莎莉亚':{'页面ID': 1744},
                  '香菱':{'页面ID': 112},
                  '北斗':{'页面ID': 79},
                  '诺艾尔':{'页面ID': 111},
                  '砂糖':{'页面ID': 1055},
                  '辛焱':{'页面ID': 1291},
                  '烟绯':{'页面ID': 1795}}

for k, v in character_list.items():
    if '旅行者' not in k:
        all_rates_temp = fatch_character_data(v['页面ID'])
        v['普通攻击'] = all_rates_temp[0]
        v['元素战技'] = all_rates_temp[1]
        v['元素爆发'] = all_rates_temp[2]
        if len(k) < 4:
            print(k, '\t\t信息已记录')
        else:
            print(k, '\t信息已记录')
    else:
        traveler_rates_temp = fatch_traveler_data(v['页面ID'])
        v['普通攻击'] = traveler_rates_temp[0]

        l = len(traveler_rates_temp)
        l -= 1
        traveler_type = ['风','岩','雷']
        for t in traveler_type:
            traveler_type_temp = {}
            traveler_type_temp['元素战技'] = traveler_rates_temp[l-1]
            traveler_type_temp['元素爆发'] = traveler_rates_temp[l]
            v[t] = traveler_type_temp
            l -= 2
        print(k, '\t信息已记录')

character_list_str = reformat(character_list)

with open("character_talents_temp.json", 'w', encoding='utf-8') as fw:
    fw.write(character_list_str)

print('全部角色信息已写入文件')
