import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

from sys import argv, exit

exit_code = 1

class MainWindow(Gtk.Window):
	def __init__(self):
		Gtk.Window.__init__(self, title='SSH Askpass Utility')
		self.set_default_size(400,100)

		self.base = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
		self.base.set_spacing(5)

		self.title = Gtk.Label()
		self.title.set_text('Password:' if len(argv) < 2 else argv[1])
		self.title.set_hexpand(True)

		self.base.pack_start(self.title,False,False,5)

		def exit_with_password():
			global exit_code
			exit_code = 0
			print(self.input.get_text())
			Gtk.main_quit()

		self.input = Gtk.Entry()
		self.input.set_visibility(False)
		self.input.connect('activate', lambda *_: exit_with_password())

		self.base.pack_start(self.input,False,False,0)

		self.buttons = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)

		self.submit = Gtk.Button(label='Submit')
		self.submit.connect('clicked', lambda *_: exit_with_password())

		self.cancel = Gtk.Button(label='Cancel')
		self.cancel.connect('clicked', lambda *_: Gtk.main_quit())

		self.buttons.pack_start(self.submit,True,True,3)
		self.buttons.pack_end(self.cancel,True,True,3)
		self.buttons.set_hexpand(True)
		self.base.pack_start(self.buttons,False,False,5)

		self.add(self.base)

win = MainWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
exit(exit_code)
