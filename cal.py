import math
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as msg

from choose_monster_page import *
from charater_model import *

class attr():
    def __init__(self, entity, value_type, enable, name):
        self.entity = entity            # entry
        self.value_type = value_type    # 0 for int and 1 for float 
        self.enable = enable
        self.value = 0                  # dafult value
        self.name = name

# attribute blocks
class attr_blocks():
    def __init__(self, txt, isfloat, xpos, ypos,db = False, ch=2):
        self.enable = tk.IntVar(value=1)
        self.Checkbutton = ttk.Checkbutton(home, text=txt + '：', variable=self.enable, command=lambda:entry_status(self.Entry1, self.enable.get(), self.Entry2))
        self.Entry1 = ttk.Entry(home,width=10)
        self.Entry1.insert(tk.END, '0')
        self.Checkbutton.place(x=xpos,y=ypos), self.Entry1.place(x=xpos+40+10*ch,y=ypos)
        self.cls1 = attr(self.Entry1, isfloat, self.enable, txt)
        attributes_list.append(self.cls1)
        if db:
            self.label = ttk.Label(home, text='+')
            self.Entry2 = ttk.Entry(home, width=10)
            self.Entry2.insert(tk.END, '0')
            self.label.place(x=xpos+120+10*ch, y=ypos), self.Entry2.place(x=xpos+140+10*ch,y=ypos)
            self.cls2 = attr(self.Entry2, isfloat, self.enable, '额外' + txt)
            attributes_list.append(self.cls2)
        else:
            self.Entry2 = None

# convert string to int and set to a variable
def int_lv(lv_str, var):
    var.set(math.ceil(float(lv_str)))                   # typr of var: tk.IntVar

# control entry status
def entry_status(entry1, check, entry2=None):
    if check:
        status='normal'
    else:
        status='disabled'
    entry1.config(state=status)
    if entry2:
        entry2.config(state=status)

# update/enable irrelevant block
def change_DMG_attr(DMG_attr_value):
    ATK.Checkbutton.config(state='normal')
    HP.Checkbutton.config(state='normal')
    DEF.Checkbutton.config(state='normal')
    if DMG_attr_value=='攻击力加成':
        ATK.enable.set(1)
        entry_status(ATK.Entry1, 1, ATK.Entry2)
        ATK.Checkbutton.config(state='disabled')
    elif DMG_attr_value=='防御力加成':
        DEF.enable.set(1)
        entry_status(DEF.Entry1, 1, DEF.Entry2)
        DEF.Checkbutton.config(state='disabled')
    elif DMG_attr_value=='生命加成':
        HP.enable.set(1)
        entry_status(HP.Entry1, 1, HP.Entry2)
        HP.Checkbutton.config(state='disabled')
def change_DMG_type(DMG_type_value):
    monster_RES[1] = DMG_type_value
    Pyro_DMG.Checkbutton.config(state='normal')
    Hydro_DMG.Checkbutton.config(state='normal')
    Dendro_DMG.Checkbutton.config(state='normal')
    Electro_DMG.Checkbutton.config(state='normal')
    Anemo_DMG.Checkbutton.config(state='normal')
    Cryo_DMG.Checkbutton.config(state='normal')
    Geo_DMG.Checkbutton.config(state='normal')
    Physical_DMG.Checkbutton.config(state='normal')
    if DMG_type_value=='物伤': 
        Physical_DMG.enable.set(1)
        entry_status(Physical_DMG.Entry1, 1)
        Physical_DMG.Checkbutton.config(state='disabled')
    elif DMG_type_value=='火伤': 
        Pyro_DMG.enable.set(1)
        entry_status(Pyro_DMG.Entry1, 1)
        Pyro_DMG.Checkbutton.config(state='disabled')
    elif DMG_type_value=='水伤': 
        Hydro_DMG.enable.set(1)
        entry_status(Hydro_DMG.Entry1, 1)
        Hydro_DMG.Checkbutton.config(state='disabled')
    elif DMG_type_value=='草伤': 
        Dendro_DMG.enable.set(1)
        entry_status(Dendro_DMG.Entry1, 1)
        Dendro_DMG.Checkbutton.config(state='disabled')
    elif DMG_type_value=='雷伤': 
        Electro_DMG.enable.set(1)
        entry_status(Electro_DMG.Entry1, 1)
        Electro_DMG.Checkbutton.config(state='disabled')
    elif DMG_type_value=='风伤': 
        Anemo_DMG.enable.set(1)
        entry_status(Anemo_DMG.Entry1, 1)
        Anemo_DMG.Checkbutton.config(state='disabled')
    elif DMG_type_value=='冰伤': 
        Cryo_DMG.enable.set(1)
        entry_status(Cryo_DMG.Entry1, 1)
        Cryo_DMG.Checkbutton.config(state='disabled')
    elif DMG_type_value=='岩伤': 
        Geo_DMG.enable.set(1)
        entry_status(Geo_DMG.Entry1, 1)
        Geo_DMG.Checkbutton.config(state='disabled')

# check if all values are numbers(int or float)
# return True/False
def check_attributes():
    warn_list = []
    # value check
    for i in attributes_list:
        if i.enable.get():
            try:
                if i.value_type:
                    i.value = float(i.entity.get())     # float
                else:
                    i.value = int(i.entity.get())       # int
                if i.name in type_DMG:
                    type_DMG[i.name] = i.value
            except:
                # wrong type
                warn_list.append([i.name, i.value_type])

    # value warning
    if warn_list:
        warn_msg = ''
        warn_msg_float = []
        warn_msg_int = []
        for i in warn_list:                             # stick warning massage
            if i[1]:
                warn_msg_float.append(i[0])
            else:
                warn_msg_int.append(i[0])
        if warn_msg_int:
            warn_msg += '，'.join(warn_msg_int) + '处必须为整数\n'
        if warn_msg_float:
            warn_msg += '，'.join(warn_msg_float) + '处必须为数字\n'
        msg.showwarning('警告',warn_msg)
        return False
    return True

# run calcutatioin
def run_calculate(is_CRIT, is_same_tpye = False):
    # 七大乘区
    atk = 0
    talents_percentage_percentage = 100
    buff_percentage = 0
    crit_percentage = 50
    react = 1
    defense = 0
    res_percentage = 0

    # 攻击力乘区
    atk_extra = ATK.cls2.value
    atk_raw = ATK.cls1.value
    atk_buff = 0
    atk_buff_percentage = buff_ATK.cls1.value/100
    atk_buff_raw = buff_ATK.cls2.value
    if buff_ATK.enable.get():
        atk_buff = atk_raw * atk_buff_percentage + atk_buff_raw
    atk = atk_raw + atk_extra + atk_buff

    # 倍率乘区
    talents_percentage_percentage = DMG_attr_percentage.value
    talents_raw = DMG_attr_raw.value
    talents_percentage = talents_percentage_percentage/100

    # 增伤乘区
    DMG_type_value = DMG_tpye.get()
    buff_raw = 0
    buff_percentage = type_DMG[DMG_type_value]
    if buff_DMG.enable.get():
        buff_percentage += buff_DMG.cls1.value
        buff_raw = buff_DMG.cls2.value
    buff = 1 + buff_percentage/100

    # 双爆乘区
    crit_percentage = CRIT_DMG.cls1.value
    if CRIT_DMG_inc.enable.get():
        crit_percentage += CRIT_DMG_inc.cls1.value
    if is_CRIT:
        crit = 1 + crit_percentage/100
    else:
        crit = 1

    # 反应乘区


    # 防御力乘区
    def_dec_percentage = 0                  # 减防百分比
    def_ingore_percentage = 0               # 无视防御百分比
    if DEF_dec.enable.get():
        def_dec_percentage = DEF_dec.cls1.value
    if DEF_ignore.enable.get():
        def_ingore_percentage = DEF_ignore.cls1.value
    player_lv_ = player_lv_value.get() + 100
    monster_lv_ = monster_lv_value.get() + 100
    def_dec = def_dec_percentage/100
    def_ingore = def_ingore_percentage/100
    defense = player_lv_ / (player_lv_ + (1 - def_dec)*(1 - def_ingore)*monster_lv_)

    # 抗性乘区
    if is_same_tpye:
        res_percentage = monster_RES[0]['对应属性']
    else:
        res_percentage = monster_RES[0][monster_RES[1]]
    if RES_dec.enable.get():
        res_percentage -= RES_dec.cls1.value
    if res_percentage < 0:
        res = 1 - res_percentage/100/2
    elif res_percentage <= 75:
        res = 1 - res_percentage/100
    else:
        res = 1 / (1 + 4 * res_percentage/100)
    
    # 总伤害
    dmg = (atk * talents_percentage + talents_raw + buff_raw) * buff * crit * react * defense * res

    return math.floor(dmg)

def generate_dmg_string(dmg1, dmg2):
    dmg_str = ''
    dmg_str = '伤害：' + str(dmg1) + '\n'
    if CRIT_DMG.enable.get():
        dmg_str += '暴击伤害：' + str(dmg2) + '\n'
    return dmg_str

# def generate_output_string(output_str, addstr = ''):
#     output_str += addstr
#     return output_str

# write output block(text)
def wirte_output(output_str):
    output.config(state='normal')
    output.delete('1.0', tk.END)                    # clear from line 1 position 0 to the end
    output.insert(tk.END, output_str)
    output.config(state='disabled')

# show the damage 
def show_dmg():
    if check_attributes():
        output_str = ''
        base_dmg_not_CRIT = run_calculate(0)
        base_dmg_CRIT = run_calculate(1)
        output_str += generate_dmg_string(base_dmg_not_CRIT, base_dmg_CRIT)
        same_type_res = monster_RES[0]['对应属性']
        if same_type_res and monster_RES[1] != '物伤':
            output_str += '对应属性伤害：\n'
            if same_type_res == '免疫':
                output_str += '免疫'
            elif type(same_type_res) == int:
                same_type_dmg_not_CRIT = run_calculate(0, True)
                same_type_dmg_CRIT = run_calculate(1, True)
                output_str += generate_dmg_string(same_type_dmg_not_CRIT, same_type_dmg_CRIT)
        wirte_output(output_str)
        #print(type(player_lv_value))
        #print(monster_RES)

def choose_monster():
    choose_monster_page_top = tk.Toplevel()
    root.attributes('-disabled', 1)             # 打开小窗口时禁用主窗口
    #choose_monster_page_top.overrideredirect(1)    # 无关闭等操作栏
    choose_monster_page(choose_monster_page_top, root, monster_RES, choose_monster_label)

def load_charater():
    print('load')
    choose_character_page_top = tk.Toplevel()
    #root.attributes('-disabled', 1)             # 打开小窗口时禁用主窗口
    choose_character_page(choose_character_page_top, root, monster_RES, choose_monster_label)
    print(type(root.winfo_children()[0]))
    print(home.winfo_children()[0])
    home.nametowidget('.!frame.!spinbox').config(from_=50)
    '''角色：
    等级：40已突破，50未突破
    普通攻击等级：！
    元素战技等级：1
    元素爆发等级：1
    命坐：1命
    '''

# page settings
root = tk.Tk()
root.title('原神伤害计算器') 
root.geometry('700x500')
root.resizable(False, False)
#root.attributes('-topmost', 1)     # 置顶窗口

# add a frame
home = ttk.Frame(root)
home.pack(fill='both',expand=1)

attributes_list = []
type_DMG = {'物伤': 0, '火伤': 0, '水伤': 0, '草伤': 0, '雷伤': 0, '风伤': 0, '冰伤': 0, '岩伤': 0}
type_RES = {'对应属性': 0, '物伤': 0, '火伤': 0, '水伤': 0, '草伤': 0, '雷伤': 0, '风伤': 0, '冰伤': 0, '岩伤': 0}
monster_RES = [type_RES, '物伤']
player_lv_value = tk.IntVar(value=1)
monster_lv_value = tk.IntVar(value=1)

# player lv
player_lv_label = ttk.Label(home, text='角色等级：')
player_lv_Spinbox = ttk.Spinbox(home, from_=1, to=90, width=10, textvariable=player_lv_value)
player_lv_Scale = ttk.Scale(home, from_=1, to=90, length=90, orient='horizontal', variable=player_lv_value, command=lambda s:int_lv(s, player_lv_value))
player_lv_label.place(x=360,y=20), player_lv_Spinbox.place(x=420,y=20), player_lv_Scale.place(x=420,y=45)
# monster lv
monster_lv_label = ttk.Label(home, text='怪物等级：')
monster_lv_Spinbox = ttk.Spinbox(home, from_=1, to=120, width=10, textvariable=monster_lv_value)
monster_lv_Scale = ttk.Scale(home, from_=1, to=120, length=90, orient='horizontal', variable=monster_lv_value, command=lambda s:int_lv(s, monster_lv_value))
monster_lv_label.place(x=360,y=95), monster_lv_Spinbox.place(x=420,y=95), monster_lv_Scale.place(x=420,y=120)

# Attributes
HP = attr_blocks('生命', 0, 40, 20, db=True)
ATK = attr_blocks('攻击', 0, 40, 45, db=True)
ATK.Checkbutton.config(state='disabled')
DEF = attr_blocks('防御', 0, 40, 70, db=True)
EM = attr_blocks('精通', 0, 40, 95)             # 元素精通
CRIT_RATE = attr_blocks('暴击', 1, 40, 120)
CRIT_RATE.Entry1.delete('0', tk.END)
CRIT_RATE.Entry1.insert(tk.END, '5')
CRIT_DMG = attr_blocks('爆伤', 1, 40, 145)
CRIT_DMG.Entry1.delete('0', tk.END)
CRIT_DMG.Entry1.insert(tk.END, '50')
ER = attr_blocks('充能', 1, 40, 170)            # 元素充能
ER.Entry1.delete('0', tk.END)
ER.Entry1.insert(tk.END, '100')
Pyro_DMG = attr_blocks('火伤', 1, 40, 195)      # 火伤
Hydro_DMG = attr_blocks('水伤', 1, 40, 220)     # 水伤
Dendro_DMG = attr_blocks('草伤', 1, 40, 270)    # 草伤
Electro_DMG = attr_blocks('雷伤', 1, 40, 245)   # 雷伤
Anemo_DMG = attr_blocks('风伤', 1, 40, 270)     # 风伤
Cryo_DMG = attr_blocks('冰伤', 1, 40, 295)      # 冰伤
Geo_DMG = attr_blocks('岩伤', 1, 40, 320)       # 岩伤
Physical_DMG = attr_blocks('物伤', 1, 40, 345)  # 物伤
Physical_DMG.Checkbutton.config(state='disabled')

# choose monster buttom
choose_monster_button = ttk.Button(home, text='选择敌人', width=9, command=choose_monster)
choose_monster_button.place(x=200, y=95)
# choose monster result
choose_monster_label = ttk.Label(home, text='未选择，默认无抗性')
choose_monster_label.place(x=280, y=125)

# DMG Attributes
DMG_attr_label = ttk.Label(home, text='加成类型，倍率(%)+固定值，伤害类型：')
DMG_attr_label.place(x=200, y=145)
DMG_attr = tk.StringVar()
DMG_attr_OptionMenu = ttk.OptionMenu(home, DMG_attr, '攻击力加成', '生命加成', '攻击力加成', '防御力加成', command=change_DMG_attr)
DMG_attr_OptionMenu.place(x=200,y=170)
# 百分比加成
DMG_attr_percentage_Entry = ttk.Entry(home,width=6)
DMG_attr_percentage_Entry.insert(tk.END, '0')
DMG_attr_percentage_Entry.place(x=300, y=170)
DMG_attr_percentage = attr(DMG_attr_percentage_Entry, 1, tk.IntVar(value=1), '加成倍率')
attributes_list.append(DMG_attr_percentage)
# 固定值加成
DMG_attr_raw_Entry = ttk.Entry(home,width=6)
DMG_attr_raw_Entry.insert(tk.END, '0')
DMG_attr_raw_Entry.place(x=355, y=170)
DMG_attr_raw = attr(DMG_attr_raw_Entry, 1, tk.IntVar(value=1), '加成数值')
attributes_list.append(DMG_attr_raw)
# 伤害类型
DMG_tpye = tk.StringVar()
DMG_tpye_OptionMenu = ttk.OptionMenu(home, DMG_tpye, '物伤', '物伤', '火伤', '水伤', '草伤', '雷伤', '风伤', '冰伤', '岩伤', command=change_DMG_type)
DMG_tpye_OptionMenu.place(x=420,y=170)

# buffs
buff_attr_label = ttk.Label(home, text='增益类型，百分比(%)+固定值：')
buff_attr_label.place(x=200, y=195)
buff_DMG = attr_blocks('增加伤害', 1, 200, 220, db=True, ch=4)
buff_ATK = attr_blocks('增加面板', 1, 200, 245, db=True, ch=4)
DEF_ignore = attr_blocks('无视防御', 1, 200, 270, ch=4)
DEF_dec = attr_blocks('降低防御', 1, 200, 295, ch=4)
RES_dec = attr_blocks('降低抗性', 1, 200, 320, ch=4)
CRIT_DMG_inc = attr_blocks('增加暴伤', 1, 200, 345, ch=4)

# load character
load_charater_button = ttk.Button(home, text='导入角色', command=load_charater)
load_charater_button.place(x=40,y=370)

# character attribute display
character_attr = tk.Text(home, width=24, height=6, state='normal')
character_attr.place(x=150,y=370)

# calculation button
start_calculate = ttk.Button(home, text='计算伤害', command=show_dmg)
start_calculate.pack(side='bottom')

# output block
output = tk.Text(home, width=20, height=30, state='disabled')
#output.insert(tk.END, "Hello.....")
#output.config(state='disabled')
output.place(x=520,y=10)

root.mainloop()
