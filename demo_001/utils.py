# ------------------------------------------------------------------------------- #
# IMPORTS
# ------------------------------------------------------------------------------- #

import bpy
from bpy.types import (
    Context,
    Event,
    Object,
)
from mathutils import (
    Vector,
    Matrix,
    Quaternion,
    geometry
)

# ------------------------------------------------------------------------------- #
# POLLS
# ------------------------------------------------------------------------------- #

def poll_active_object(context:Context):
    if context.active_object:
        if isinstance(context.active_object, Object):
            return True
    return False

# ------------------------------------------------------------------------------- #
# OBJECT
# ------------------------------------------------------------------------------- #

def get_obj_from_ctx(context:Context, prop_name:str=''):
    obj = context.active_object
    if obj and isinstance(context.active_object, Object):
        if hasattr(obj, prop_name):
            return obj
    return None
