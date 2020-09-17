#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/10 15:14
# @Author  : TangHuanqiang
# @File    : 基金最新数据爬取.py
from tkinter import Tk,Frame,Label,Entry,NORMAL,LEFT,RIGHT,Button,StringVar,Scrollbar,Y
from tkinter import ttk  # 导入内部包
from bs4 import BeautifulSoup
from os import remove
from requests import get
from PIL import Image
from lxml import etree
from re import findall
# GUI界面设置
# 基础设置
root = Tk()
root.title('基金数据分析')
root.geometry('1300x800')
shuru_tishi = '还未输入信息'
name = StringVar()
#  提示和输入框部分容器
# 提示
frm = Frame(root)
frm1 = Frame(frm)
label1 = Label(frm1,text='输入序号查看基金数据变化')
label1.pack(side='top')
# 设置为回车
def get_Enter(event):
    name_botton()

# 输入框设置
enter1 = Entry(frm1,state=NORMAL)
enter1.bind('<Key-Return>',get_Enter)
enter1.pack(side='bottom')
frm1.pack(side=LEFT)
frm.pack()
# 基金按钮函数
# 获取数据
def get_date(i):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'}
    # 开放型基金
    total_urls=[
        'http://fund.eastmoney.com/jzzzl.html#os_0;isall_0;ft_;pt_1',
        'http://fund.eastmoney.com/GP_jzzzl.html#os_0;isall_0;ft_;pt_2',
        'http://fund.eastmoney.com/HH_jzzzl.html#os_0;isall_0;ft_;pt_3',
        'http://fund.eastmoney.com/ZQ_jzzzl.html#os_0;isall_0;ft_;pt_13',
        'http://fund.eastmoney.com/ZS_jzzzl.html#os_0;isall_0;ft_;pt_5',
        'http://fund.eastmoney.com/LJ_jzzzl.html#os_0;isall_0;ft_;pt_11',
        'http://fund.eastmoney.com/QDII_jzzzl.html#os_0;isall_0;ft_;pt_6',
        'http://fund.eastmoney.com/LOF_jzzzl.html#os_0;isall_0;ft_;pt_8',
        'http://fund.eastmoney.com/FOF_jzzzl.html#os_0;isall_0;ft_;pt_15'
    ]
    url = total_urls[i]
    response = get(url,headers=headers)
    html_str = response.content.decode('gbk')
    soup = BeautifulSoup(html_str, 'html.parser')
    # whole_code = soup.find_all('div',class_='mainFrame')
    # print(whole_code[8])
    whole_code = soup.find('div',id='tableDiv')
    single_code = whole_code.find_all('td')
    single_code = single_code[19:]
    # print(single_code)
    cycle = 1
    whole_list=[]
    datelist=[]
    for td in single_code:
        if td.get_text() != '':
            datelist.append(td.get_text())
            cycle+=1
            if cycle == 4:
                # print(str(td))
                add_url = findall(r'a href="(.*)">估值图</a>',str(td))
                try:
                    add_url = add_url[0].split('"')[0]
                except: pass
            if cycle == 14:
                cycle=1
                datelist.pop(-1)
                datelist.append(add_url)
                whole_list.append(datelist)
                datelist = []
    for i in whole_list:
        i[2] = i[2][:-6]
    return whole_list[:-1]

def get_date_0():
    x = tree.get_children()
    for item in x:
        tree.delete(item)
    global whole_list
    whole_list = get_date(0)
    sum = 1
    for date in whole_list:
        tree.insert('', sum, values=date)
        sum += 1
def get_date_1():
    x = tree.get_children()
    for item in x:
        tree.delete(item)
    global whole_list
    whole_list = get_date(1)
    sum = 1
    for date in whole_list:
        tree.insert('', sum, values=date)
        sum += 1
def get_date_2():
    x = tree.get_children()
    for item in x:
        tree.delete(item)
    global whole_list
    whole_list = get_date(2)
    sum = 1
    for date in whole_list:
        tree.insert('', sum, values=date)
        sum += 1
def get_date_3():
    x = tree.get_children()
    for item in x:
        tree.delete(item)
    global whole_list
    whole_list = get_date(3)
    sum = 1
    for date in whole_list:
        tree.insert('', sum, values=date)
        sum += 1
def get_date_4():
    x = tree.get_children()
    for item in x:
        tree.delete(item)
    global whole_list
    whole_list = get_date(4)
    sum = 1
    for date in whole_list:
        tree.insert('', sum, values=date)
        sum += 1
def get_date_5():
    x = tree.get_children()
    for item in x:
        tree.delete(item)
    global whole_list
    whole_list = get_date(5)
    sum = 1
    for date in whole_list:
        tree.insert('', sum, values=date)
        sum += 1
def get_date_6():
    x = tree.get_children()
    for item in x:
        tree.delete(item)
    global whole_list
    whole_list = get_date(6)
    sum = 1
    for date in whole_list:
        tree.insert('', sum, values=date)
        sum += 1
def get_date_7():
    x = tree.get_children()
    for item in x:
        tree.delete(item)
    global whole_list
    whole_list = get_date(7)
    sum = 1
    for date in whole_list:
        tree.insert('', sum, values=date)
        sum += 1
def get_date_8():
    x = tree.get_children()
    for item in x:
        tree.delete(item)
    global whole_list
    whole_list = get_date(8)
    sum = 1
    for date in whole_list:
        tree.insert('', sum, values=date)
        sum += 1
# 获取估值图并弹窗提示
def get_change_date(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'}
    response = get(url,headers=headers)
    html_str = response.content.decode()
    html = etree.HTML(html_str)
    last_url = html.xpath('//*[@id="Li1"]/div[2]/a')
    for a in last_url:
        href = a.xpath('./@href')
    last_url = href[0]
    response = get(last_url,headers=headers)
    html_str = response.content.decode()
    html = etree.HTML(html_str)
    picture_url =html.xpath('//*[@id="jzpng"]')
    for i in picture_url:
        picture_content = i.xpath('./@src')
    picture_content = 'http:' + picture_content[0]
    content = get(picture_content,headers=headers)
    with open('Temp_png.png','wb')as f:
        f.write(content.content)
    # 打开子弹窗显示数据
    image = Image.open('Temp_png.png')
    image.show()
    remove('Temp_png.png')
# 查询估值表按钮函数
def name_botton():
    if enter1.get():
        # 输入名字之后
        shuru_tishi = ''
        for find in whole_list:
            if find[0] == enter1.get():
                add_url = find[12]
                new_url = 'http://fund.eastmoney.com/' + add_url
                get_change_date(new_url)


    else:
        shuru_tishi = '你没输入序号呢'
    label2.config(text=shuru_tishi)
# 未输入提示
label2 = Label(root,text=shuru_tishi)
label2.pack()

# 按钮
button_frm = Frame(root)
name.set('↑基金名字↑')
button1 = Button(button_frm,textvariable=name,command=name_botton)
button1.pack(side=LEFT)
button_frm.pack()
# 基金类型选择
button_frms = Frame(root)
b1 = Button(button_frms,text='全部',width=10,command=get_date_0)
b2 = Button(button_frms,text='股票型',width=10,command=get_date_1)
b3 = Button(button_frms,text='混合型',width=10,command=get_date_2)
b4 = Button(button_frms,text='债券型',width=10,command=get_date_3)
b5 = Button(button_frms,text='指数型',width=10,command=get_date_4)
b6 = Button(button_frms,text='ETF联接',width=10,command=get_date_5)
b7 = Button(button_frms,text='QDⅡ',width=10,command=get_date_6)
b8 = Button(button_frms,text='LOF',width=10,command=get_date_7)
b9 = Button(button_frms,text='FOF',width=10,command=get_date_8)
b1.grid(row=0,column=0)
b2.grid(row=0,column=1)
b3.grid(row=0,column=2)
b4.grid(row=0,column=3)
b5.grid(row=0,column=4)
b6.grid(row=0,column=5)
b7.grid(row=0,column=6)
b8.grid(row=0,column=7)
b9.grid(row=0,column=8)
button_frms.pack()

# 表格内容，设置表头
frm3 = Frame(root)
scrollBar = Scrollbar(frm3)
scrollBar.pack(side=RIGHT, fill=Y)
title = ("序号","基金代码","基金简称","基金净值-最新","累计净值-最新","基金净值-前日","累计净值-前日","日增长值","日增长率","申购状态","赎回状态","手续费")
tree = ttk.Treeview(frm3,columns=title,show='headings',yscrollcommand=scrollBar.set,height=40)
scrollBar.config(command=tree.yview)
frm3.pack()
# GUI设置结束
# 开始输入内容
for i in title:
    # 输入表头
    if i =='基金简称':
        tree.column(i,width=200,anchor='center')
    else:
        tree.column(i,width=100,anchor='center')
    tree.heading(i,text=i)
global whole_list
whole_list = get_date(0)
sum = 1
for date in whole_list:
    tree.insert('', sum, values=date)
    sum += 1
tree.pack()
root.mainloop()