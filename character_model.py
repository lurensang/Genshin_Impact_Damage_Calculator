import tkinter as tk
import tkinter.ttk as ttk
import json

class ch_modle:
    def __init__(self):
        pass


def choose_character_page(top, root, res, monster_label):
    def load_characters():
        with open("character_list.json", 'r', encoding='utf-8') as jsonf:
            character_dict =  json.load(jsonf)
        return character_dict

    def close_window():
        root.attributes('-disabled', 0)
        top.destroy()
    
    def return_and_close():
        selected_line =character_list_listbox.curselection()
        if selected_line:
            x = character_list_listbox.get(selected_line[0])[1:]
        print(x)
        #character_list_listbox.
        
    def update_list(_):
        character_list = []
        weapon_filter_str = weapon_filter.get()
        element_filter_str = element_filter.get()
        star_filter_str = star_filter.get()
        if star_filter_str == '全部':
            star_filter_int = 0
        else:
            star_filter_int = int(star_filter_str)
        area_filter_str = area_filter.get()
        for k, v in character_dict.items():
            if v['武器'] == weapon_filter_str or weapon_filter_str == '全部':
                if element_filter_str in v['元素'] or element_filter_str == '全部':
                    if v['星级'] == star_filter_int or star_filter_int == 0:
                        if v['地区'] == area_filter_str or area_filter_str == '全部':
                            character_list.append(k)

        # 选择栏加入怪物列表
        character_list_listbox.delete(0, tk.END)
        for i in character_list:
            character_list_listbox.insert('end', ' ' + i)
        
    print('\n')
    top.protocol('WM_DELETE_WINDOW',close_window)   # 点击小窗口关闭按钮时
    top.geometry('500x250+300+150')
    top.resizable(False, False)
    top.title('选择角色')

    character_dict = load_characters()
    #character_list = {}
    selected_character_name = ''

    # 筛选
    character_filters_label = ttk.Label(top, text='筛选：')
    character_filters_label.place(x=20, y=10)

    weapon_filter_label = ttk.Label(top, text='武器：')
    weapon_filter_label.place(x=20, y=35)
    weapon_filter = tk.StringVar()
    weapon_filter_OptionMenu = ttk.OptionMenu(top, weapon_filter, '全部', '全部', '单手剑', '双手剑', '弓', '长柄武器', '法器', command=update_list)
    weapon_filter_OptionMenu.place(x=60,y=35)

    element_filter_label = ttk.Label(top, text='元素：')
    element_filter_label.place(x=20, y=60)
    element_filter = tk.StringVar()
    element_filter_OptionMenu = ttk.OptionMenu(top, element_filter, '全部', '全部', '风', '火', '水', '冰', '雷', '岩', '草', command=update_list)
    element_filter_OptionMenu.place(x=60,y=60)

    star_filter_label = ttk.Label(top, text='星级：')
    star_filter_label.place(x=20, y=85)
    star_filter = tk.StringVar()
    star_filter_OptionMenu = ttk.OptionMenu(top, star_filter, '全部', '全部', '4', '5', command=update_list)
    star_filter_OptionMenu.place(x=60,y=85)

    area_filter_label = ttk.Label(top, text='地区：')
    area_filter_label.place(x=20, y=110)
    area_filter = tk.StringVar()
    area_filter_OptionMenu = ttk.OptionMenu(top, area_filter, '全部', '全部', '蒙德', '璃月', '稻妻', '异世界', command=update_list)
    area_filter_OptionMenu.place(x=60,y=110)

    character_list_labelframe  = ttk.LabelFrame(top, text='角色')
    character_list_scrollbar = ttk.Scrollbar(character_list_labelframe)                                             # 定义滚动条
    character_list_listbox = tk.Listbox(character_list_labelframe, height=10, width=20, yscrollcommand=character_list_scrollbar.set, activestyle='none')   # 滚动内容，yscrollcommand设置横向滚动条
    #character_list_listbox.bind('<<ListboxSelect>>', update_display, add='+')
    character_list_scrollbar.config(command=character_list_listbox.yview)                                           # 配置滚动条
    character_list_labelframe.place(x=150,y=10), character_list_scrollbar.pack(side='right', pady=2, fill='y'), character_list_listbox.pack(side='left', pady=2)

    update_list('全部')

    # 确定按钮
    start_calculate = ttk.Button(top, text='确定', command=return_and_close)
    start_calculate.pack(side='bottom')
    
    # # display block
    # display = tk.Text(top, width=20, height=16, state='disabled')
    # display.place(x=320,y=10)   