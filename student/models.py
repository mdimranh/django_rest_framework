from django.db import models
from django.utils.timezone import now

class Student(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=17)
    profile = models.ImageField(upload_to = 'stu_img', blank=True, null=True)
    department = models.CharField(max_length=200)
    term = models.IntegerField()
    level = models.IntegerField()
    student_id = models.CharField(max_length=50)
    admission = models.DateTimeField(default=now)

    def __str__(self):
        return self.name

class ProfileUpload(models.Model):
    profile = models.ImageField(upload_to = 'stu_img')
    student = models.ForeignKey(Student, on_delete = models.CASCADE, related_name='images')
    def save(self, *args, **kwargs):
        super(self, ProfileUpload).save(*args, **kwargs)
        img = Image.open(self.profile.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.profile.path)