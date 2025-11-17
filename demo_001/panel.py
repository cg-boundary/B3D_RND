# ------------------------------------------------------------------------------- #
# IMPORTS
# ------------------------------------------------------------------------------- #

import bpy
from bpy.types import (
    Context,
    Panel,
)
from . import utils

# ------------------------------------------------------------------------------- #
# PANEL
# ------------------------------------------------------------------------------- #

class KRND_PT_001_ViewPanel(Panel):
    bl_category = "KRND"
    bl_label = "Demo 001"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_options = {'DEFAULT_CLOSED'}


    @classmethod
    def poll(cls, context:Context):
        return utils.poll_active_object(context)


    def draw(self, context:Context):
        box = self.layout.box()
        row = box.row()
        row.operator('krnd.001_setup', text="Setup")
