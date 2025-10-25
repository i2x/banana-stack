# __init__.py
from .Disease import Disease
from .ImageUpload import ImageUpload
from .ModelFile import ModelFile
from .Prediction import Prediction
from .Treatment import Treatment

#  __all__ เพื่อควบคุมการ import ด้วยเครื่องหมาย *
__all__ = [
    'Disease',
    'ImageUpload',
    'ModelFile',
    'Prediction',
    'Treatment',
]