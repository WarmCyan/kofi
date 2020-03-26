import argparse
import libtmux
import urwid

import util


class KofiTUI:

    def __init__(self, navigator):
        self.navigator = navigator
    
    def key_handler(self, key):
        if key in ('q', 'Q'):
            raise urwid.ExitMainLoop()
        if key == 'c':
            self.navigator.create_object()
            self.message.set_text(self.message.text + "\nSTUFF NOW")
            self.main_loop.screen.register_palette_entry('banner_text', 'black', 'light red')
        if key == 'w':
            self.message.set_text(self.message.text + "\nokay done now")
            self.main_loop.screen.register_palette_entry('banner_text', 'black', 'light blue')
            self.main_loop.screen.clear()
            self.navigator.tmux_nav_pane.select_pane()

    def init_tui(self):
        self.palette = [
            ('banner_text', "black", "light blue"),
        ]
        
        # titlebar
        self.banner = urwid.Text(("banner_text", "KOFI"), align='center')
        self.map1 = urwid.AttrMap(self.banner, 'banner_text')
        self.titlebar = urwid.Filler(self.map1, 'top')
        
        self.message = urwid.Text("hello there")
        
        self.pile = urwid.Filler(urwid.Pile([(1, self.titlebar), self.message]), valign='top')

        self.main_loop = urwid.MainLoop(self.pile, self.palette, unhandled_input=self.key_handler)
    
    def start(self):
        self.init_tui()
        self.main_loop.run()


class KofiTerminalNavigator:

    def __init__(self, args):
        self.tmux_server = libtmux.Server()
        self.tmux_session = self.tmux_server.find_where({"session_name": args.tmux_server_name})

        self.tmux_nav_pane = self.tmux_session.attached_window.attached_pane
        self.nav_pane_id = ""
        self.tmux_vim_pane = None
        self.vim_pane_id = ""

        self.current_editing_object = None

        self.tui = KofiTUI(self)

    def ensure_vim_pane(self):
        """ Make sure a pane for the editor exists """
        if self.tmux_vim_pane is None:
            self.tmux_vim_pane = self.tmux_nav_pane.split_window(vertical=False)
            self.nav_pane_id = self.tmux_nav_pane.get("pane_id")
            self.vim_pane_id = self.tmux_vim_pane.get("pane_id")
            self.tmux_session.cmd("swap-pane", "-s", self.vim_pane_id, "-t", self.nav_pane_id)

    def create_object(self):
        """ Create a new object and open it for editing """
        self.ensure_vim_pane()

        new_obj_uuid = util.get_uuid()
        self.current_editing_object = new_obj_uuid
        self.tmux_vim_pane.send_keys(f"nvim ./cache/{new_obj_uuid}; tmux send-keys -t {self.nav_pane_id} w")
        self.tmux_vim_pane.select_pane()

    def start(self):
        self.tui.start()
        

# class ConsoleBox(urwid.Text):
#     def keypress(self, size, key):
#         self.text += key

# palette = [
#     ('banner_text', "black", "light blue"),
# ]


 
#console = ConsoleBox("hello?")
# 
# what = urwid.AttrMap(pile, 'bg')
        

#lb = urwid.ListBox(urwid.SimpleFocusListWalker([banner_fill, message]))

#mainloop = urwid.MainLoop(what, palette, unhandled_input=key_handler)





# thing1 = urwid.Text("hello?")
# thing2 = urwid.Text("uhhhh?")
# pile = urwid.Filler(urwid.Pile([thing1, thing2]))


# mainloop = urwid.MainLoop(pile, palette, unhandled_input=key_handler)
# mainloop.run()


parser = argparse.ArgumentParser()
parser.add_argument("--tmux-server-name", dest="tmux_server_name", default=None)
args = parser.parse_args()

nav = KofiTerminalNavigator(args)
nav.start()
