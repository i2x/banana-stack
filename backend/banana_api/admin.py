from django.contrib import admin
from .models import Disease, ImageUpload, ModelFile, Prediction, Treatment

admin.site.register(Disease)
admin.site.register(ImageUpload)
admin.site.register(ModelFile)
admin.site.register(Prediction)
admin.site.register(Treatment)
