from rest_framework import serializers
from .models import Student, Subject, SubjectEntry


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = "__all__"


class SubjectEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubjectEntry
        fields = "__all__"



class StudentResultSerializer(serializers.Serializer):
    student_id = serializers.IntegerField()
    total_marks = serializers.IntegerField()
    percentage = serializers.FloatField()
    grade = serializers.CharField()
