# ------------------------------------------------------------------------------- #
# ADDON
# ------------------------------------------------------------------------------- #

bl_info = {
    'name'        : "KRND",
    'author'      : "KenzoCG",
    'version'     : (1, 0, 0),
    'blender'     : (5, 0, 0),
    'location'    : "View3D",
    'category'    : "3D View",
    'description' : "KenzoCG Blender R&D",
}

# ------------------------------------------------------------------------------- #
# REGISTER
# ------------------------------------------------------------------------------- #

def register():
    from . import demo_001
    demo_001.register()


def unregister():
    from . import demo_001
    demo_001.unregister()
