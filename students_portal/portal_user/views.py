from rest_framework.permissions import AllowAny
from rest_framework.generics import (ListAPIView,
                                     CreateAPIView, DestroyAPIView,
                                     UpdateAPIView)
from rest_framework.response import Response
from .models import Student, MarkList
from .serializers import StudentSerializer, MarkSerializer
from django.db.models import Q


# Api to Create Student
class CreateStudentAPI(CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = (AllowAny,)

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": 200, "data": serializer.data,
                             "message": "Student record created"})
        else:
            return Response({"status": 400, "errors": serializer.errors,
                             "message": "Invalid input data"})


# CRUD Operations of Student Model
class StudentListAPI(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = (AllowAny,)

    def list(self, request):
        serializer = StudentSerializer(self.get_queryset(), many=True)
        return Response({"status": 200, "data": serializer.data,
                         "message": "Student list"})


class StudentDetailsUpdateAPI(UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = (AllowAny,)
    lookup_field = 'id'

    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data,
                                         instance=self.get_object())
        if serializer.is_valid():
            serializer.save()
            return Response({"status": 200, "data": serializer.data,
                             "message": "Student record updated"})
        else:
            return Response({"status": 400, "errors": serializer.errors,
                            "message": "Invalid input data"})


class DeleteStudentAPI(DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = (AllowAny,)
    lookup_field = 'id'

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
        except Exception:
            return Response({"status": 400, "errors": {},
                             "message": "Record not found"})
        self.perform_destroy(instance)
        return Response({"status": 200, "data": {},
                         "message": "Student record deleted"})


# Api to create Marks
class CreateMarksAPI(CreateAPIView):
    permission_classes = (AllowAny,)
    queryset = MarkList.objects.all()
    serializer_class = MarkSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        record = MarkList.objects.filter(Q(student=request.data["student"]) &
                                         Q(term=request.data["term"]))
        if serializer.is_valid() and not record:
            serializer.save()
            return Response({"status": 200, "data": serializer.data,
                             "message": "Mark list generated"})
        else:
            return Response({"status": 400, "errors": serializer.errors,
                             "message": "Invalid input data"})


# CRUD operations of Marks
class MarkListAPI(ListAPIView):
    queryset = MarkList.objects.all()
    serializer_class = MarkSerializer
    permission_classes = (AllowAny,)

    def list(self, request):
        serializer = MarkSerializer(self.get_queryset(), many=True)

        return Response({"status": 200, "data": serializer.data,
                         "message": "Mark list"})


class MarkDetailsUpdateAPI(UpdateAPIView):
    queryset = MarkList.objects.all()
    serializer_class = MarkSerializer
    permission_classes = (AllowAny,)
    lookup_field = 'id'

    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data,
                                         instance=self.get_object())
        if serializer.is_valid():
            serializer.save()
            return Response({"status": 200, "data": serializer.data,
                             "message": "Mark list updated"})
        else:
            return Response({"status": 400, "errors": serializer.errors,
                            "message": "Invalid input data"})


class DeleteMarkListAPI(DestroyAPIView):
    queryset = MarkList.objects.all()
    serializer_class = MarkSerializer
    permission_classes = (AllowAny,)
    lookup_field = 'id'

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
        except Exception:
            return Response({"status": 400, "errors": {},
                             "message": "Record not found"})
        self.perform_destroy(instance)
        return Response({"status": 200, "data": {},
                         "message": "Mark list deleted"})
