# summary: Menulib-python Project FAQ

# Introduction #

**[menulib.py ](https://code.google.com/p/menulib-python/source/browse/source/menulib.py)** is a library to use for displaying vertical menu with submenu
Just call run\_menu with a list (or tuple) of a menu
display\_box is given as extra for displaying a list outside of a menu

**[menudemo.py ](https://code.google.com/p/menulib-python/source/browse/source/MenuDemo.py)** is a demo file to show the use of the library - it declares a main\_menu and 2 submenu (menu\_1 and menu\_2) and check all the returned option - this could be used as a template for your project.

# Details #

_Latest change_ :

Since there is a number added at the beginning of each option displayed on the menu
pressing a number is also sending an event from the run\_menu()
The limits is 0 to 9 (number above will not be reachable).