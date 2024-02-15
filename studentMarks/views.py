from django.shortcuts import render
from rest_framework import viewsets
from .models import Student, Subject, SubjectEntry
from .serializers import StudentSerializer, SubjectSerializer, SubjectEntrySerializer
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from django.db.models import Aggregate, Avg, Sum, Max, Min


# Create your views here.

class StudentView(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class SubjectView(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = (IsAuthenticated,)


class SubjectEntryView(viewsets.ModelViewSet):
    queryset = SubjectEntry.objects.all()
    serializer_class = SubjectEntrySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = "__all__"


def student_result_view(request, student_id):
    student = Student.objects.get(pk=student_id)
    subject_entries = SubjectEntry.objects.filter(student=student)

    total_marks = sum(entry.marks for entry in subject_entries)
    out_of_marks = Subject.objects.all().aggregate(Sum("total_marks"))['total_marks__sum']
    print(out_of_marks)
    percentage = (total_marks / out_of_marks) * 100

    if percentage >= 66:
        grade = 'First Class with Distinction'
    elif 60 <= percentage < 66:
        grade = 'First Class'
    else:
        grade = 'Pass Class'

    context = {
        'student': student,
        'entries': subject_entries,
        'total_marks': total_marks,
        'percentage': round(percentage, 2),
        'grade': grade,
    }

    return render(request, 'studentMarks/student_result.html', context)


