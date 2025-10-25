from django.db import models

class ModelFile(models.Model):
    """
    เก็บข้อมูลเกี่ยวกับไฟล์โมเดลที่ใช้ในการทำนาย
    """
    model_id = models.AutoField(primary_key=True)
    file_name = models.CharField(max_length=255)
    # ใช้ FileField 
    file_path = models.FileField(upload_to='model_files/')
    version = models.CharField(max_length=50)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.file_name} (v{self.version})"