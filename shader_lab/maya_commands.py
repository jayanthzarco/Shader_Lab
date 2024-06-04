try:
    import maya.cmds as cmds
except:
    pass

class MayaCmds:
    @staticmethod
    def return_shaders(hi=False, scene=False):
        mesh_and_shaders = {}
        selection = cmds.ls(sl=True)
        for each in selection:
            mesh_and_shaders[each] = None

        return mesh_and_shaders

    @staticmethod
    def export_shaders(group=False):
        if group:
            print("exporting every shaders")
        else:
            print("exporting  as single shaders")

    @staticmethod
    def return_selection(hierarchy=True):
        mesh = []
        # TODO: NEED TO FIND BETTER WAY ITS CURRENTLY NOT WORKING AS EXPECTED
        if hierarchy:
            selection = cmds.ls(sl=True)
            for each in selection:
                cmds.select(each, replace=True, hi=True)
                sel2 = cmds.ls(sl=True)
                for obj in sel2:
                    if obj not in mesh:
                        if cmds.nodeType == "mesh":
                            mesh.append(obj)
        else:
            selection = cmds.ls(sl=True)
            for each in selection:
                if cmds.nodeType(each) == "transform":
                    shapes = cmds.listRelatives(each, shapes=True)
                    if shapes:
                        for shape in shapes:
                            if cmds.nodeType(shape) == "mesh":
                                mesh.append(selection)
                elif cmds.nodeType(each) == "mesh":
                    if each not in mesh:
                        mesh.append(each)
        print(mesh)
        return mesh

