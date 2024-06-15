from  rest_framework import serializers
from . import models

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Teacher
        fields = ['id', 'full_name', 'email', 'password', 'qualification', 'mobile_no', 'address','skills']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CourseCategory
        fields = ['id', 'title', 'description',]


class CourseSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Course
        fields = ['id', 'category', 'teacher', 'title', 'description', 'featured_image', 'techs']

class ChapterSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Chapter
        fields = ['id','course',  'title', 'description', 'vedio', 'remarks']