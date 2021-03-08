import bpy, bmesh


def deselect_all(bm):
    for f in bm.faces:
        f.select = False
    for v in bm.verts:
        v.select = False
    for e in bm.edges:
        e.select = False
        
def select_faces(faces):
    for f in faces:
        f.select = True
