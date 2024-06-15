from django.db import models

# Create your models here.

class Teacher(models.Model):    
    full_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    qualification = models.CharField(max_length=20)
    mobile_no = models.CharField(max_length=20)
    address = models.TextField()
    skills = models.TextField(null=True, blank=True) 

    class Meta:
        verbose_name_plural = "1. Teachers"
    
    def __str__(self):
        return self.full_name


class CourseCategory(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = "2. Course Categories"

class Course(models.Model):
    category =  models.ForeignKey(CourseCategory, on_delete=models.CASCADE)
    teacher =  models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    featured_image = models.ImageField(upload_to='course_images/' , null=True, blank=True)
    techs= models.TextField(null=True, blank=True)


    class Meta:
         verbose_name_plural = "3. Courses"
    
    def __str__(self):
        return self.title


class Chapter(models.Model):
    course =  models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    vedio = models.FileField(upload_to='course_vedios/' , null=True, blank=True)
    remarks= models.TextField(null=True, blank=True)

    class Meta:
         verbose_name_plural = "4. Chapters"
    
    def __str__(self):
        return self.title


class Student(models.Model):    
    full_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    qualification = models.CharField(max_length=20)
    mobile_no = models.CharField(max_length=20)
    address = models.TextField()
    interested_categories = models.TextField()

    class Meta:
        verbose_name_plural = "5. Students"
