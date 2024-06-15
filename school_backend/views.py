from django.shortcuts import render
from .import models
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, permissions
from .serializers import TeacherSerializer, CategorySerializer,CourseSerializers,ChapterSerializers
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
# Create your views here.


# class TeacherList(generics.ListCreateAPIView):
#     def get(self, request):
#         teachers = models.Teacher.objects.all()
#         serializer = TeacherSerializer(teachers, many=True)
#         return Response(serializer.data)



class TeacherList(generics.ListCreateAPIView):
    queryset = models.Teacher.objects.all()
    serializer_class = TeacherSerializer
    # permission_classes = [permissions.IsAuthenticated]

class TeacherDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [permissions.IsAuthenticated]


@csrf_exempt
def teacher_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            teacher = models.Teacher.objects.get(email=email,password=password)
        except model.Teacher.DoesNotExist:
            teacher= None
        if teacher:
            return JsonResponse({'bool':True,'teacher_id':teacher.id})
        else:
            return JsonResponse({'bool':False})



class CategoryList(generics.ListCreateAPIView):
    queryset = models.CourseCategory.objects.all()
    serializer_class = CategorySerializer


class CourseList(generics.ListCreateAPIView):
    queryset = models.Course.objects.all()
    serializer_class = CourseSerializers


    
class ChapterList(generics.ListCreateAPIView):
    queryset = models.Chapter.objects.all()
    serializer_class = ChapterSerializers

    # single teacher courses
class TeacherCourseList(generics.ListCreateAPIView):
    serializer_class = CourseSerializers

    def get_queryset(self):
        teacher_id = self.kwargs['teacher_id']
        return models.Course.objects.filter(teacher=teacher_id)
         