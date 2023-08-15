import json
character_list = {'久岐忍':{'地区':'稻妻', '星级':4, '元素':'雷', '武器':'单手剑'},
                  '夜兰':{'地区':'璃月', '星级':5, '元素':'水', '武器':'弓'},
                  '旅行者(空)':{'地区':'异世界', '星级':5, '元素':'风岩雷', '武器':'单手剑'},
                  '旅行者(荧)':{'地区':'异世界', '星级':5, '元素':'风岩雷', '武器':'单手剑'},
                  '神里绫人':{'地区':'稻妻', '星级':5, '元素':'水', '武器':'单手剑'},
                  '八重神子':{'地区':'稻妻', '星级':5, '元素':'雷', '武器':'法器'},
                  '云堇':{'地区':'璃月', '星级':4, '元素':'岩', '武器':'长柄武器'},
                  '申鹤':{'地区':'璃月', '星级':5, '元素':'冰', '武器':'长柄武器'},
                  '荒泷一斗':{'地区':'稻妻', '星级':5, '元素':'岩', '武器':'双手剑'},
                  '五郎':{'地区':'稻妻', '星级':4, '元素':'岩', '武器':'弓'},
                  '优菈':{'地区':'蒙德', '星级':5, '元素':'冰', '武器':'双手剑'},
                  '阿贝多':{'地区':'蒙德', '星级':5, '元素':'岩', '武器':'单手剑'},
                  '托马':{'地区':'稻妻', '星级':4, '元素':'火', '武器':'长柄武器'},
                  '胡桃':{'地区':'璃月', '星级':5, '元素':'火', '武器':'长柄武器'},
                  '达达利亚':{'地区':'璃月', '星级':5, '元素':'水', '武器':'弓'},
                  '雷电将军':{'地区':'稻妻', '星级':5, '元素':'雷', '武器':'长柄武器'},
                  '珊瑚宫心海':{'地区':'稻妻', '星级':5, '元素':'水', '武器':'法器'},
                  '埃洛伊':{'地区':'异世界', '星级':5, '元素':'冰', '武器':'弓'},
                  '宵宫':{'地区':'稻妻', '星级':5, '元素':'火', '武器':'弓'},
                  '神里绫华':{'地区':'稻妻', '星级':5, '元素':'冰', '武器':'单手剑'},
                  '枫原万叶':{'地区':'稻妻', '星级':5, '元素':'风', '武器':'单手剑'},
                  '温迪':{'地区':'蒙德', '星级':5, '元素':'风', '武器':'弓'},
                  '刻晴':{'地区':'璃月', '星级':5, '元素':'雷', '武器':'单手剑'},
                  '莫娜':{'地区':'蒙德', '星级':5, '元素':'水', '武器':'法器'},
                  '可莉':{'地区':'蒙德', '星级':5, '元素':'火', '武器':'法器'},
                  '琴':{'地区':'蒙德', '星级':5, '元素':'风', '武器':'单手剑'},
                  '迪卢克':{'地区':'蒙德', '星级':5, '元素':'火', '武器':'双手剑'},
                  '七七':{'地区':'璃月', '星级':5, '元素':'冰', '武器':'单手剑'},
                  '魈':{'地区':'璃月', '星级':5, '元素':'风', '武器':'长柄武器'},
                  '钟离':{'地区':'璃月', '星级':5, '元素':'岩', '武器':'长柄武器'},
                  '甘雨':{'地区':'璃月', '星级':5, '元素':'冰', '武器':'弓'},
                  '早柚':{'地区':'稻妻', '星级':4, '元素':'风', '武器':'双手剑'},
                  '九条裟罗':{'地区':'稻妻', '星级':4, '元素':'雷', '武器':'弓'},
                  '凝光':{'地区':'璃月', '星级':4, '元素':'岩', '武器':'法器'},
                  '菲谢尔':{'地区':'蒙德', '星级':4, '元素':'雷', '武器':'弓'},
                  '班尼特':{'地区':'蒙德', '星级':4, '元素':'火', '武器':'单手剑'},
                  '丽莎':{'地区':'蒙德', '星级':4, '元素':'雷', '武器':'法器'},
                  '行秋':{'地区':'璃月', '星级':4, '元素':'水', '武器':'单手剑'},
                  '迪奥娜':{'地区':'蒙德', '星级':4, '元素':'冰', '武器':'弓'},
                  '安柏':{'地区':'蒙德', '星级':4, '元素':'火', '武器':'弓'},
                  '重云':{'地区':'璃月', '星级':4, '元素':'冰', '武器':'双手剑'},
                  '雷泽':{'地区':'蒙德', '星级':4, '元素':'雷', '武器':'双手剑'},
                  '芭芭拉':{'地区':'蒙德', '星级':4, '元素':'水', '武器':'法器'},
                  '罗莎莉亚':{'地区':'蒙德', '星级':4, '元素':'冰', '武器':'长柄武器'},
                  '香菱':{'地区':'璃月', '星级':4, '元素':'火冰雷', '武器':'长柄武器'},
                  '北斗':{'地区':'璃月', '星级':4, '元素':'雷', '武器':'双手剑'},
                  '诺艾尔':{'地区':'蒙德', '星级':4, '元素':'岩', '武器':'双手剑'},
                  '砂糖':{'地区':'蒙德', '星级':4, '元素':'风', '武器':'法器'},
                  '辛焱':{'地区':'璃月', '星级':4, '元素':'火', '武器':'双手剑'},
                  '烟绯':{'地区':'璃月', '星级':4, '元素':'火', '武器':'法器'}}
with open("character_list_temp.json", 'w', encoding='utf-8') as fw:
    json.dump(character_list, fw, indent=4, ensure_ascii=False)