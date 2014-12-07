__author__ = 'sergio'

__all__= ['Fruto', 'Naranja', 'Limon', 'Sandia', 'classes']

from .fruto import Fruto
from .naranja import Naranja
from .limon import Limon
from .sandia import Sandia

classes = [Limon(), Naranja(), Sandia()]