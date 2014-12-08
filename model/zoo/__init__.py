__author__ = 'jmoyano'

__all__= ['Animal', 'Anfibio', 'Ave', 'Insecto', 'Invertebrado', 'Mamifero', 'Pez', 'Reptil', 'classes']

from .animal import Animal
from .anfibio import Anfibio
from .ave import Ave
from .insecto import Insecto
from .invertebrado import Invertebrado
from .mamifero import Mamifero
from .pez import Pez
from .reptil import Reptil

classes = [Anfibio(), Ave(), Insecto(), Invertebrado(), Mamifero(), Pez(), Reptil()]