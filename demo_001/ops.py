# ------------------------------------------------------------------------------- #
# IMPORTS
# ------------------------------------------------------------------------------- #

import bpy
from bpy.types import (
    Context,
    Event,
    Operator,
    Object,
)
from . import utils

# ------------------------------------------------------------------------------- #
# OPERATOR
# ------------------------------------------------------------------------------- #

class KRND_OT_001_Setup(Operator):
    '''KRND_OT_001_Setup'''
    bl_label = "KRND_OT_001_Setup"
    bl_idname = 'krnd.001_setup'
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context:Context):
        return utils.poll_active_object(context)


    def invoke(self, context:Context, event:Event):
        obj = utils.get_obj_from_ctx(context, 'krnd_001_controls')
        if not obj:
            self.report({'INFO'}, "No Object")
            return {'CANCELLED'}

        props = obj.krnd_001_controls
        self.report({'INFO'}, f"VALUE : {props.prop}")
        return {'FINISHED'}
