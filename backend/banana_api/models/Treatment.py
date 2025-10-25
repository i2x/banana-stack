from django.db import models
from .Disease import Disease

class Treatment(models.Model):
    """
    เก็บข้อมูลวิธีการรักษาของแต่ละโรค
    """
    treatment_id = models.AutoField(primary_key=True)
    # related_name='treatments'
    disease = models.ForeignKey(Disease, on_delete=models.CASCADE, related_name='treatments')
    method = models.TextField()
    # ใช้ URLField ถ้า source 
    source = models.URLField(max_length=500, null=True, blank=True)

    def __str__(self):
        return f"Treatment for {self.disease.name}"