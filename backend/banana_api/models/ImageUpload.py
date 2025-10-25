from django.db import models

class ImageUpload(models.Model):
    """
    เก็บข้อมูลเกี่ยวกับรูปภาพที่ผู้ใช้อัปโหลด
    """
    image_id = models.AutoField(primary_key=True)
    # ใช้ ImageField จะจัดการเรื่องการอัปโหลดไฟล์และเส้นทางได้ง่ายกว่า
    file_path = models.ImageField(upload_to='upload/images/')
    # auto_now_add=True จะบันทึกเวลาตอนสร้าง object ครั้งแรกอัตโนมัติ
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image {self.image_id} - {self.file_path.name}"