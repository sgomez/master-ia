__author__ = 'jmoyano'

__all__= ['Vino', 'Muy malo', 'Malo', 'Regular', 'Bueno', 'Muy bueno', 'classes']

from .vino import Vino
from .muymalo import MuyMalo
from .malo import Malo
from .regular import Regular
from .bueno import Bueno
from .muybueno import MuyBueno

classes = [MuyMalo(), Malo(), Regular(), Bueno(), MuyBueno()]