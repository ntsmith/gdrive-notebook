def printFiles(d):
    for f in d.values():
        print(f"{f['name']} ({f['id']})")

def getPath(fid,fileById):
    f = fileById[fid]
    out = ''
    if 'parents' in f:
        [pid] = f['parents']
        out = getPath(pid,fileById)
    out += '/' + f['name']
    return out

def depthFirstPrint(fid,fileById):
    f = fileById[fid]
    print(f'{getPath(fid,fileById)} ({f["id"]})')
    for childid in fileById[f['id']]['children']:
        depthFirstPrint(childid, fileById)