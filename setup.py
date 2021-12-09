import os, shutil


def copytree(src, dst, symlinks=False, ignore=None):
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, symlinks, ignore)
        else:
            shutil.copy2(s, d)


def move_scripts():
    print("copying scripts to parent folder")
    copytree('scripts', '../')


def create_lcd_enabled():
    print("creating LCD enabled file")
    f = open("lcdenabled", "a")
    f.close()


move_scripts()
create_lcd_enabled()
