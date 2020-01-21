import os


def formot(str):
    str = str[:-1]
    line = ''
    if str[-3:] == "png":
        line = "<img src='" + str + "'>"
    if str[-3:] == "jpg":
        line = "<img src='" + str + "'>"
    elif str[-3:] == "css":
        line = "<link rel='stylesheet' href='" + str + "'>"
    elif str.endswith("js"):
        line = "<script type='text/javascript' src='" + str + "'></script>"
    return line + '\n'


def gci(filepath):
    files = os.listdir(filepath)
    for fi in files:
        fi_d = os.path.join(filepath, fi)
        if os.path.isdir(fi_d):
            gci(fi_d)
        else:
            # print(filepath,fi_d)
            # str = os.path.join(filepath, fi_d) + '\n'
            s = fi_d[2:]
            str =  eval(repr(s).replace('\\', '/')) + '\n'
            str = str.replace('//', '/')
            vv = formot(str)
            if len(vv) > 2:
                vv = vv.replace("\'", "\"")

                list_txt.writelines(vv)
            print(vv)

list_txt = open('list.html', 'w')
path = r'./'
gci(path)
list_txt.close()