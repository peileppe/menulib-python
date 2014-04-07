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

Monday, April 07, 2014
"""

import curses
from curses import panel

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

def longest_in_the_list(list2):
	# return the size of the longest string in the list
	return len(max(list2,key=len))

def display_box(list1):
	# display the list in a box / not a menu
	maxx = longest_in_the_list(list1) + 4
	w1=curses.newwin(len(list1)+2,maxx,curses.LINES/2-len(list1)/2,curses.COLS/2-maxx/2)
	w1panel=panel.new_panel(w1)
	w1.box()
	yy, xx=w1.getmaxyx()
	line=1
	for item in list1:
		w1.addstr(line,2,str(item))
		line+=1
	w1.move(0,0)
	w1.addstr("[X]")
	w1.refresh()
	w1.getch()
	del w1panel

def main(self):
	win=curses.initscr()
	# filling the screen with numbers - to see how panels are working 
	for y in range(0, curses.LINES - 1):
			for x in range(0, curses.COLS):
				win.addch(".")
	win.refresh()
	max_option=len(menu_main)
	max_length = longest_in_the_list(menu_main) + 4
	returned_option=-1
	while returned_option != (max_option-1):
		y,x = 0, 0 
		returned_option=run_menu(menu_main)
		if returned_option==2:
			y, x =returned_option, max_length
			returned_option=run_menu(menu_1[1:],x,y, True)
		elif returned_option==3:
			y, x =returned_option, max_length
			returned_option=run_menu(menu_2[1:],x,y, True)
	curses.endwin()

def display_menu(ws,x1,y1,menu1,attribut1):
	"""
	display each item in the list as an optin in the menu
	if the item is a list (or a tuple) then it only print the first item of that list/tuple
	"""
	current_option=0
	for o in menu1:
		if type(o)  == str:
			o=str(current_option)+". "+o
		elif type(o) == tuple or type(o) == list:
			o=str(current_option)+". "+o[0]
		ws.addstr(y1,x1,o,attribut1[current_option])
		ws.clrtoeol()
		y1+=1
		current_option+=1
	ws.move(0,0)
	ws.refresh()

def run_menu(menu1,x=0,y=0, subMenu=False):
	"""
	will display the menu at x, y on a newly created window
	then display menu to relative coordinates in that new window called wmenu
	see display_menu above
	"""
	max_length = longest_in_the_list(menu1)+4
	max_option = len(menu1)
	current_option=0
	option_selected=-1
	wmenu=curses.newwin(max_option ,max_length ,y ,x )
	menupanel = panel.new_panel(wmenu)
	color=curses.COLOR_RED
	curses.init_pair(color, curses.COLOR_WHITE, curses.COLOR_BLUE)
	wmenu.bkgdset(ord(' '), curses.color_pair(color))
	wmenu.keypad(1)
	wmenu.refresh()
	while option_selected == -1:
		attribut=[curses.A_NORMAL]*max_option
		attribut[current_option]=curses.A_REVERSE+curses.A_BOLD
		display_menu(wmenu,0,0,menu1,attribut)
		a=wmenu.getch()
		if   a==curses.KEY_DOWN:
			current_option+=1
		elif a==curses.KEY_UP:
			current_option-=1
		elif a==ord('\n') or a == 32 :
			option_selected=current_option
			if subMenu:
				del menupanel
				panel.update_panels()
		if current_option>max_option-1:
			current_option=max_option-1
		elif current_option <0:
			current_option=0
	return option_selected

if __name__ == '__main__':
    curses.wrapper(main)
