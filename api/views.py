from rest_framework.generics import get_object_or_404

from .serializers import RoleSerializers
from rest_framework import generics
from .models import Role


class RoleListView(generics.ListCreateAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializers


class RoleDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializers
    # lookup_fields = ['student_no']


class MultipleFieldLookupMixin(object):

    def get_object(self):
        queryset = self.get_queryset()  # Get the base queryset
        queryset = self.filter_queryset(queryset)  # Apply any filter backends
        filter = {}
        for field in self.lookup_fields:
            if self.kwargs[field]:  # Ignore empty fields.
                filter[field] = self.kwargs[field]
        obj = get_object_or_404(queryset, **filter)  # Lookup the object
        self.check_object_permissions(self.request, obj)
        return obj


class RetrieveUserView(MultipleFieldLookupMixin, generics.RetrieveAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializers
    lookup_fields = ['student_no']