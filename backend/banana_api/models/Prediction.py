from django.db import models
from .ImageUpload import ImageUpload
from .Disease import Disease

class Prediction(models.Model):
    """
    เก็บผลลัพธ์การทำนายจากรูปภาพที่อัปโหลด
    """
    prediction_id = models.AutoField(primary_key=True)
    image = models.ForeignKey(ImageUpload, on_delete=models.CASCADE, related_name='predictions')
    disease = models.ForeignKey(Disease, on_delete=models.CASCADE, related_name='predictions')
    confidence = models.FloatField()
    predicted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Prediction for {self.image.file_path.name} -> {self.disease.name} ({self.confidence:.2%})"
    



