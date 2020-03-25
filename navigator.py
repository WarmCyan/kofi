import argparse
import libtmux
import urwid

import util

parser = argparse.ArgumentParser()
parser.add_argument("--tmux-server-name", dest="tmux_server_name", default=None)
args = parser.parse_args()

tmux_server = libtmux.Server()
tmux_session = tmux_server.find_where({"session_name": args.tmux_server_name})

tmux_nav_pane = tmux_session.attached_window.attached_pane
nav_pane_id = ""
tmux_vim_pane = None
vim_pane_id = ""
 

current_editing_object = None


def ensure_vim_pane():
    global tmux_vim_pane
    global vim_pane_id
    global nav_pane_id
    if tmux_vim_pane is None:
        tmux_vim_pane = tmux_nav_pane.split_window(vertical=False)
        nav_pane_id = tmux_nav_pane.get("pane_id")
        vim_pane_id = tmux_vim_pane.get("pane_id")
        tmux_session.cmd("swap-pane", "-s", vim_pane_id, "-t", nav_pane_id)

    return tmux_vim_pane


def create():
    """ Create a new object and open it for editing """
    global current_editing_object
    ensure_vim_pane()

    new_obj_uuid = util.get_uuid()
    current_editing_object = new_obj_uuid
    #tmux_vim_pane.send_keys(f"nvim ./cache/{new_obj_uuid}; tmux send-keys -t {nav_pane_id} Enter")
    tmux_vim_pane.send_keys(f"nvim ./cache/{new_obj_uuid}; tmux send-keys -t {nav_pane_id} w")
    tmux_vim_pane.select_pane()


def key_handler(key):
    global mainloop
    global message
    if key in ('q', 'Q'):
        raise urwid.ExitMainLoop()
    if key == 'c':
        create()
        message.set_text(message.text + "\nSTUFF NOW")
        mainloop.screen.register_palette_entry('banner_text', 'black', 'light red')
    if key == 'w':
        message.set_text(message.text + "\nokay done now")
        mainloop.screen.register_palette_entry('banner_text', 'black', 'light blue')
        mainloop.screen.clear()
        tmux_nav_pane.select_pane()

class ConsoleBox(urwid.Text):
    def keypress(self, size, key):
        self.text += key

palette = [
    ('banner_text', "black", "light blue"),
]


banner = urwid.Text(("banner_text", "KOFI"), align='center')
map1 = urwid.AttrMap(banner, 'banner_text')
banner_fill = urwid.Filler(map1, 'top')
 
#console = ConsoleBox("hello?")
# 
message = urwid.Text("hello there")
# 
pile = urwid.Filler(urwid.Pile([(1, banner_fill), message]), valign='top')
# what = urwid.AttrMap(pile, 'bg')
        

#lb = urwid.ListBox(urwid.SimpleFocusListWalker([banner_fill, message]))

#mainloop = urwid.MainLoop(what, palette, unhandled_input=key_handler)





# thing1 = urwid.Text("hello?")
# thing2 = urwid.Text("uhhhh?")
# pile = urwid.Filler(urwid.Pile([thing1, thing2]))


mainloop = urwid.MainLoop(pile, palette, unhandled_input=key_handler)
mainloop.run()
