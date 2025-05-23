import os

if os.name == 'nt':
    from win32com.client import Dispatch
    def create_shortcut(name, target, arguments="", icon=None):
        desktop = os.path.join(os.path.join(os.environ["USERPROFILE"]), "OneDrive\Desktop")
        path = os.path.join(desktop, f"{name}.lnk")

        shell = Dispatch('WScript.Shell')
        shortcut = shell.CreateShortCut(path)
        shortcut.Targetpath = target
        shortcut.Arguments = arguments
        shortcut.WorkingDirectory = os.path.dirname(target)
        if icon:
            shortcut.IconLocation = icon
        shortcut.save()
else:
    def create_shortcut(name, target, arguments="", icon=None):
        peint("Not Implemented for this Operating system")
    

# Shortcut for: skribbl-public
# create_shortcut("Skribble - Public Room", "skribbl-public.exe")
