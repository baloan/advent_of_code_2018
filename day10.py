#!python3
# encoding: utf8
# Copyright (c) 2018 Andreas Balogh
# See LICENSE for details.

""" advent of code - day 10 """

from collections import defaultdict
import logging
import operator
from pathlib import Path
from pprint import pprint
import sys
from tkinter import ttk

import tkinter as tk

LOG = logging.getLogger()


class App(tk.Tk):

    def __init__(self):
        super().__init__()
        self.option_add('*tearOff', False)
        self.title("Advent of Code - Day 10")
        self.protocol('WM_DELETE_WINDOW', self.file_exit)
        self.__create_menubar()
        self.__create_widgets()
        self.update_idletasks()
        self.after_idle(self.setup)

    def __create_menubar(self):
        self.mb = tk.Menu(self)
        self.menu_file = tk.Menu(self.mb)
        self.menu_about = tk.Menu(self.mb)
        self.mb.add_cascade(menu=self.menu_file, label='File')
        self.mb.add_cascade(menu=self.menu_about, label='About')
        self.menu_file.add_command(label='Exit', command=self.file_exit)
        self.menu_about.add_command(label='About...', command=self.help_about)
        self['menu'] = self.mb

    def __create_widgets(self):
        # feed selection list
        self.fr0 = ttk.LabelFrame(self, padding=2, borderwidth="2p", text="Stats")
        self.fr0.pack(side=tk.LEFT, anchor=tk.N, fill=tk.Y)
        # feed select and filter
        self.fr1 = ttk.Frame(self, padding=5)
        self.fr1.pack(side=tk.LEFT, fill=tk.X)
        self.cv1 = tk.Canvas(self.fr1, width="520", height="520")
        self.cv1.pack()

    def file_exit(self):
        self.after(100, self.quit)
        
    def help_about(self):
        LOG.info("about")

    def setup(self):
        inp = Path(r"day10_input.txt")
        self.posx = list()
        self.posy = list()
        self.velx = list()
        self.vely = list()
        with inp.open() as fh:
            for raw_line in fh:
                line = raw_line.rstrip()
                # 01234567890123456789012345678901234567890123456789
                # position=<-52592,  31869> velocity=< 5, -3>
                px = int(line[10:16])
                py = int(line[17:24])
                vx = int(line[36:38])
                vy = int(line[39:42])
                self.posx.append(px)
                self.posy.append(py)
                self.velx.append(vx)
                self.vely.append(vy)
        self.count = 0
        self.cv1.create_text(50, 10, text="Advent of Code")
        self.after_idle(self.advance)

    def advance(self):
        x0 = min(self.posx)
        if x0 < 10000:
            f = 10000
        if x0 < 1000:
            f = 1000
        if x0 < 0:
            f = 10
        if x0 > 0:
            f = 1
        if x0 > 100:
            f = 0.01
        self.count += f
        self.posx = list(map(lambda x, v: x + v*f, self.posx, self.velx))
        self.posy = list(map(lambda x, v: x + v*f, self.posy, self.vely))
        dx = max(self.posx) - min(self.posx)
        dy = max(self.posy) - min(self.posy)
        x0 = min(self.posx)
        y0 = min(self.posy)
        print(self.count, x0, y0, dx, dy)
        self.cv1.delete("stars")
        self.cv1.create_text(300, 10, text=f"{self.count}", tags="stars")
        # self.cv1.scale("stars", min(self.posx), min(self.posy), 500 / dx, 500 / dy)
        for x, y in zip(self.posx, self.posy):
            sx = (x - x0) / dx * 500 + 5
            sy = (y - y0) / dy * 500 + 5
            # print(x,y, sx, sy)
            self.cv1.create_oval(sx, sy, sx + 5, sy + 5, fill="black", tags="stars")
        self.update_idletasks()
        if f >= 1:
            self.after_idle(self.advance)
        else:
            self.after(500, self.advance)



def gui():
    # setup tk.Tk() and toplevel window
    root = App()
    # tk GUI loop in main thread
    root.mainloop()
    # destructor for tk resources
    root.destroy()
        

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s.%(msecs)03i [%(thread)i] %(levelname).4s %(funcName)10s: %(message)s',
                        datefmt='%H:%M:%S')
    sys.exit(gui())
