# ------------------------------------------------------------------------------- #
# IMPORTS
# ------------------------------------------------------------------------------- #

from bpy.types import Object
from bpy.props import PointerProperty
from . import utils
from .props import KRND_PR_001_Controls
from .ops import KRND_OT_001_Setup
from .panel import KRND_PT_001_ViewPanel

# ------------------------------------------------------------------------------- #
# REGISTER
# ------------------------------------------------------------------------------- #

CLASSES = (
    KRND_PR_001_Controls,
    KRND_OT_001_Setup,
    KRND_PT_001_ViewPanel,
)


def register():
    from bpy.utils import register_class
    for cls in CLASSES:
        register_class(cls)

    Object.krnd_001_controls = PointerProperty(type=KRND_PR_001_Controls)


def unregister():
    if hasattr(Object, 'krnd_001_controls'):
        del Object.krnd_001_controls

    from bpy.utils import unregister_class
    for cls in reversed(CLASSES):
        unregister_class(cls)

