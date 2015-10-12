# coding=utf-8
__author__ = 'linzh'

import os
import Tkinter as tk
import cof.file as CoFile

def svn_co(t):
    print "迁出svn代码"
    usr_home = os.path.expanduser('~')
    dir_path = path_entry.get()
    dir_path_list = dir_path.split(os.sep)
    dir_path_list.insert(0, usr_home)
    print dir_path_list
    dir_o = CoFile.CoFile()
    dir_o.set_path(dir_path)
    dir_o.create_dir(dir_path_list)
    fullpath = dir_o.get_full_path()
    api_svn = "http://svn.sdp.nd/svn/qa-linzh/branch/cof/"
    cmd = "svn co " + api_svn + ' ' + fullpath + os.sep + "cof" + " --username=10003732 --password=lm213215"
    co_info = os.popen(cmd).read()
    t.delete("1.0", tk.END)
    t.insert(tk.END, co_info)

    # 初始化测试文件

    init_content = """
# coding=utf-8

# 引入库
from pprint import pprint
import cof.http as cofHttp

# 设置域名
url = "plot.qa.sdp.nd"

# 初始化http请求对象
http_o = cofHttp.Http(url, 80)

# 对接口执行GET请求
res = http_o.get("/api_get.json")

# 打印接口响应
pprint(res)

    """

    fp = open(fullpath + os.sep + "test.py", "w")
    fp.write(init_content)
    fp.close()

    print cmd
    t.insert(tk.END, "测试文件创建(test.py)...成功\n")
    t.insert(tk.END, "进入目录" + fullpath + "\n运行python test.py")
    t.yview_moveto(1.0)

root = tk.Tk()

root.geometry("380x200+500+100")

co_frame = tk.Frame(root)
co_frame.pack(side=tk.TOP)

path_label = tk.Label(co_frame, text="代码迁出目录：")
path_label.pack(side=tk.LEFT, padx=10)

path_entry = tk.Entry(co_frame)
path_entry.pack(side=tk.LEFT, padx=10)

co_text = tk.Text(root)
co_text.pack(side=tk.TOP)

init_btn = tk.Button(co_frame, text="初始化项目", command=lambda t=co_text: svn_co(t))
init_btn.pack(side=tk.TOP, expand=tk.YES)


root.mainloop()
