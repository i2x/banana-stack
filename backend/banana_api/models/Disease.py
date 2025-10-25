from django.db import models

class Disease(models.Model):
    """
    เก็บข้อมูลของโรคแต่ละชนิด
    """
    disease_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    symptoms = models.TextField()
    # อาจใช้เป็น ImageField ถ้าต้องการอัปโหลดรูปตัวอย่างเก็บไว้ในระบบ
    image_example = models.ImageField(upload_to='disease_examples/', null=True, blank=True)

    def __str__(self):
        return self.name