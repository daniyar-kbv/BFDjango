from rest_framework import generics

from api2.serializers import StudentModelSerializer
from main2.models import Student
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class IsSuperAdmin(IsAuthenticated):
    def has_permission(self, request, view):
        return request.user and request.user.is_superuser


class IsStaff(IsAuthenticated):
    def has_permission(self, request, view):
        return request.user and request.user.is_staff


class GenericStudentList(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return Student.objects.for_user(self.request.user)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class GenericStudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )
    lookup_field = 'student_id'

    def get_object(self):
        return Student.objects.get(id=self.kwargs[self.lookup_field])

    def get_queryset(self):
        return Student.objects.for_user(self.request.user)
