from rest_framework import serializers
from .models import Student, MarkList, Teacher


class TeacherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Teacher
        fields = ['name']


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ['id', 'name', 'age', 'gender', 'reporting_teacher']

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['reporting_teacher'] = TeacherSerializer(
                                        instance.reporting_teacher).data
        return response


class SimpleStudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ['name']


class MarkSerializer(serializers.ModelSerializer):
    total_marks = serializers.SerializerMethodField()
    created_time = serializers.SerializerMethodField()

    class Meta:
        model = MarkList
        fields = ['id', 'student', 'term', 'maths', 'science', 'history',
                  'total_marks', 'created_time']

    def get_total_marks(self, obj):
        return obj.maths + obj.science + obj.history

    def get_created_time(self, obj):
        return obj.created_time.strftime("%b %d, %Y, %-I:%M %P")

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['student'] = SimpleStudentSerializer(
                                        instance.student).data
        return response
