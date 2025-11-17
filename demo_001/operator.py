# ------------------------------------------------------------------------------- #
# IMPORTS
# ------------------------------------------------------------------------------- #

import bpy
from bpy.types import (
    Context,
    Event,
    Operator,
)
from bpy.props import (
    BoolProperty,
    IntProperty,
    FloatProperty,
)

# ------------------------------------------------------------------------------- #
# OPERATOR
# ------------------------------------------------------------------------------- #

class KRND_OT_RND_Static(Operator):
    '''KRND Demo 001'''
    bl_label = "KRND Demo 001"
    bl_idname = 'krnd.demo_001'
    bl_options = {'REGISTER', 'UNDO'}
    prop_1 : BoolProperty(default=False) # type:ignore
    prop_2 : IntProperty(default=0)      # type:ignore
    prop_3 : FloatProperty(default=0.0)  # type:ignore

    @classmethod
    def poll(cls, context):
        return True


    def invoke(self, context:Context, event:Event):
        return self.execute(context)


    def execute(self, context:Context):
        self.report({'INFO'}, "")
        return {'FINISHED'}


    def draw(self, context:Context):
        pass
