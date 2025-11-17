# ------------------------------------------------------------------------------- #
# IMPORTS
# ------------------------------------------------------------------------------- #

import bpy
from bpy.types import (
    Object,
    Mesh,
    Curve,
    PropertyGroup,
)
from bpy.props import (
    BoolProperty,
    IntProperty,
    FloatProperty,
    StringProperty,
    EnumProperty,
    BoolVectorProperty,
    IntVectorProperty,
    FloatVectorProperty,
    CollectionProperty,
    PointerProperty,
)

# ------------------------------------------------------------------------------- #
# PROPS
# ------------------------------------------------------------------------------- #

class KRND_PR_001_Controls(PropertyGroup):
    prop : BoolProperty(name="Prop", default=False) # type:ignore




