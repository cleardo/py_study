# coding=utf-8

"""
API测试工具
"""
__author__ = 'Administrator'

from Tkinter import *

root = Tk()

# 界面布局使用frame来布局，类似div
# 设置frame
text_frame = Frame(borderwidth=1, relief="sunken")

api_text = Text(text_frame)

api_text.pack(side=BOTTOM, fill=BOTH, expand=True)


def my_hl(arg, t):
    #print arg
    print arg.keysym
    #print arg.char
    #print arg.state
    #print arg.keycode
    #print arg.x_root

    # t.tag_configure("key_color", foreground="#ff0000")
    # t.tag_configure("val_color", foreground="#cccccc")

    if arg.keysym == 'a':
        print "keyword"
        ins_pos = t.index("insert")
        ins_pos_info = ins_pos.split('.')
        print "插入点", ins_pos
        print ins_pos_info

        ch_pos = int(ins_pos_info[1]) - 1
        color_idx = "%s.%s" % (ins_pos_info[0], ch_pos)
        print "语法加亮", color_idx

        t.mark_set("matchStart2", color_idx)
        t.mark_set("matchEnd2", "%s+1c" % color_idx)

        # t.insert(END, "hello", "val_color")
        t.tag_add("val_color", "matchStart2", "matchEnd2")
    else:
        mark = "1.0-1c"
        print repr(t.get(mark))

        ins_pos = t.index("insert")
        end_pos = t.index("1.end")
        print "end pos", end_pos

        ins_pos_info = ins_pos.split('.')
        print "插入点", ins_pos
        print ins_pos_info

        ch_pos = int(ins_pos_info[1])
        print "ch pos: ", ch_pos

        color_idx = "%s.%s" % (ins_pos_info[0], ch_pos)
        print "语法加亮", color_idx

        if ch_pos == 0:
            print "first"
            mark = "1.0"
            print repr(t.get(mark))
            #t.tag_nextrange
            #t.tag_prevrange
            #t.delete("insert", "insert+1c")
            #t.configure
            #t.insert("insert", "hello")
            next = t.index(mark + "+%d lines linestart" % 1)
            print "next", next
            line = t.get(mark, next)
            print len(line), repr(line)
            print next

            t.mark_set("matchStart", "1.1+1c")
            t.mark_set("matchEnd", "1.1+2c")

            t.tag_add("key_color", "1.0+0c", "1.0+1c")
            t.tag_add("val_color", "1.0+1c", "1.0+2c")
        elif ch_pos == 2:
            t.mark_set("matchStart2", "1.1")
            t.mark_set("matchEnd2", "1.1+1c")
            t.tag_add("val_color", "matchStart2", "matchEnd2")


api_text.tag_configure("key_color", foreground="#ff0000")
api_text.tag_configure("val_color", foreground="#cccccc")

# 绑定键盘事件，根据keysym来判断当前按键
api_text.bind('<KeyPress>', lambda e, t=api_text: my_hl(e, t))

#api_text.bind('<KeyPress>', lambda e, t=api_text: t.insert(END, "I'll bite your legs off!"))

api_text.tag_bind('bite', '<1>', lambda e, t=api_text: t.insert(END, "I'll bite your legs off!"))

text_frame.pack(side=BOTTOM, fill=BOTH, expand=True)

root.mainloop()

