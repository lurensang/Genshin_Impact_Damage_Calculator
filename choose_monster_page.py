import tkinter as tk
import tkinter.ttk as ttk
import json

def choose_monster_page(top, root, res, monster_label):
    def load_monsters_res():
        with open("monster_res_file.json", 'r', encoding='utf-8') as jsonf:
            monster_res_dict =  json.load(jsonf)
        return monster_res_dict

    def update_list(filter):
        monster_list = []
        if filter=='全部':
            for key in monster_res_dict:
                for k, v in monster_res_dict[key].items():
                    monster_list.append(k)
                    monster_res_list[k] = v
        else:
            for i in monster_res_dict[filter]:
                monster_list.append(i)

        # 选择栏加入怪物列表
        monster_list_listbox.delete(0, tk.END)
        for i in monster_list:
            monster_list_listbox.insert('end', ' ' + i)

    def update_display(_):
        nonlocal selected_monster_name
        dsp = '怪物抗性预览：(%)\n'
        typr_dsp = ''
        selected_line =monster_list_listbox.curselection()
        if selected_line:
            start_calculate.config(state='enabled')
            monster_name = monster_list_listbox.get(selected_line[0])[1:]
            dsp += monster_name + '\n'
            selected_monster_name = monster_name
            monster_res = monster_res_list[monster_name]
            # print(monster_res)
            for k, v in monster_res.items():
                if k != '对应属性':
                    dsp += k + '抗性：' + str(v) + '\n'
                else:
                    if v == '0':
                        dsp += '暂无该敌人数据！'
                        start_calculate.config(state='disabled')
                        break
                    elif v != 0:
                        typr_dsp = '对应属性抗性：' + str(v) + '\n'
                    else:
                        typr_dsp = '无特殊抗性\n'
            dsp += typr_dsp
            display.config(state='normal')
            display.delete('1.0', tk.END)                    # clear from line 1 position 0 to the end
            display.insert(tk.END, dsp)
            display.config(state='disabled')

    def close_window():
        root.attributes('-disabled', 0)
        top.destroy()

    def return_and_close():
        if selected_monster_name:
            res[0] = monster_res_list[selected_monster_name]
            monster_label.config(text=selected_monster_name)
            close_window()
        else:
            res[0] = {'对应属性': 0, '物伤': 0, '火伤': 0, '水伤': 0, '草伤': 0, '雷伤': 0, '风伤': 0, '冰伤': 0, '岩伤': 0}
            monster_label.config(text='未选择，默认无抗性')
            close_window()

    top.protocol('WM_DELETE_WINDOW',close_window)   # 点击小窗口关闭按钮时
    top.geometry('500x250+300+150')
    top.resizable(False, False)
    top.title('选择敌人')

    monster_res_dict = load_monsters_res()
    monster_res_list = {}
    selected_monster_name = ''

    # 筛选
    monster_filter_label = ttk.Label(top, text='筛选：')
    monster_filter_label.place(x=20, y=10)
    monster_filter = tk.StringVar()
    monster_filter_OptionMenu = ttk.OptionMenu(top, monster_filter, '全部', '全部', '普通', '精英', '首领', '周本', '其他', command=update_list)
    monster_filter_OptionMenu.place(x=20,y=35)

    monster_list_labelframe  = ttk.LabelFrame(top, text='敌人')
    monster_list_scrollbar = ttk.Scrollbar(monster_list_labelframe)                                               # 定义滚动条
    monster_list_listbox = tk.Listbox(monster_list_labelframe, height=10, width=20, yscrollcommand=monster_list_scrollbar.set, activestyle='none')   # 滚动内容，yscrollcommand设置横向滚动条
    monster_list_listbox.bind('<<ListboxSelect>>', update_display, add='+')
    monster_list_scrollbar.config(command=monster_list_listbox.yview)                                             # 配置滚动条
    monster_list_labelframe.place(x=120,y=10), monster_list_scrollbar.pack(side='right', pady=2, fill='y'), monster_list_listbox.pack(side='left', pady=2)

    update_list('全部')

    # 确定按钮
    start_calculate = ttk.Button(top, text='确定', command=return_and_close)
    start_calculate.pack(side='bottom')
    
    # display block
    display = tk.Text(top, width=20, height=16, state='disabled')
    display.place(x=320,y=10)
