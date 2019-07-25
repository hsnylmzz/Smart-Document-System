import hashlib

def Kodlar(xtable, type):
    qry = xtable.objects.all().filter(type=type)
    xlist = []
    for i in qry.values_list('id', 'title'):
        xlist.append(i)
    return xlist

# hasher = hashlib.md5()
# # with open('/home/engin/PycharmProjects/smart-document-system/src/uploads/Untitled_Diagram.png', 'rb') as afile:
# with open('/home/engin/PycharmProjects/smart-document-system/src/uploads/Untitled_Diagram_mtwyrPY.png', 'rb') as afile:
#     buf = afile.read()
#     hasher.update(buf)
#
# print(hasher.hexdigest())

def generate_sha(file):
    sha = hashlib.sha1()
    file.seek(0)
    while True:
        buf = file.read(104857600)
        if not buf:
            break
        sha.update(buf)
    sha1 = sha.hexdigest()
    file.seek(0)
    return sha1

