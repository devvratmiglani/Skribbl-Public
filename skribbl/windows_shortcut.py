import os

def create_shortcut(name, target, arguments="", icon=None):
    if os.name != 'nt':
        print("Shortcut creation is not supported on this OS.")
        return
    try:
        from win32com.client import Dispatch
        desktop = os.path.join(os.path.join(os.environ["USERPROFILE"]), "OneDrive","Desktop")
        path = os.path.join(desktop, f"{name}.lnk")
        
        shell = Dispatch('WScript.Shell')
        shortcut = shell.CreateShortCut(path)
        shortcut.Targetpath = target
        shortcut.Arguments = arguments
        shortcut.WorkingDirectory = os.path.dirname(target)
        if icon:
            shortcut.IconLocation = icon
        shortcut.save()
    except Exception as e:
        print(f"❌ Shortcut creation failed with exception {e}")


# Shortcut for: skribbl-public
# create_shortcut("Skribble - Public Room", "skribbl-public.exe")
