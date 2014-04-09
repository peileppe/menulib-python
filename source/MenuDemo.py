#!/usr/bin/env python

"""
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
For a copy of the license see .
=====================================================================
www.peileppe.com

A library to use for displaying vertical menu with submenu
Just call run_menu with a list (or tuple) of a menu
display_box is given as extra for displaying a list outside of a menu

Wednesday 09 April 2014 [10:55]

"""

import curses
import menulib as m

menu_1=(
	"Demo->",
	"Color",
	"Audio",
	"Window")

menu_2=(
	"Window->",
	"Minimize",
	"Maximize",
	"Arrange",
	"Get Info")

menu_main=(
	"New File",
	"Edit",
	menu_1,
	menu_2,
	"Help",
	"Exit")

def main(self):
	win=curses.initscr()
	# filling the screen with numbers - to see how panels are working 
	for y in range(0, curses.LINES - 1):
			for x in range(0, curses.COLS):
				win.addch(".")
	win.refresh()
	max_option=len(menu_main)
	max_length = m.longest_in_the_list(menu_main) + 4
	returned_option=-1
	while returned_option != (max_option-1):
		y,x = 0, 0 
		returned_option=m.run_menu(menu_main)
		if returned_option==0:
			listF=["New File","created"]
			m.display_box(listF)		
		elif returned_option==1:
			listF=["File","Edited"]
			m.display_box(listF)
		elif returned_option==2:
			y, x =returned_option, max_length
			returned_option=m.run_menu(menu_1[1:],x,y, True)
			if returned_option==0:
				listF=["Color","activated"]
				m.display_box(listF)
			elif returned_option==1:
				listF=["Audio","activated"]
				m.display_box(listF)			
		elif returned_option==3:
			y, x =returned_option, max_length
			returned_option=m.run_menu(menu_2[1:],x,y, True)
		elif returned_option==4:
			listF=["Help","use arrow key or number"]
			m.display_box(listF)			
	curses.endwin()

if __name__ == '__main__':
    curses.wrapper(main)
