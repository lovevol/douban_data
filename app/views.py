import json

from django.shortcuts import render

# Create your views here.
from rest_framework import serializers, mixins, viewsets, status
from rest_framework.response import Response

from app.models import DouBanBook


class DouBanBookSerializer(serializers.ModelSerializer):

    class Meta:
        model = DouBanBook
        fields = ['id', 'name', 'pub', 'star', 'desc', 'category']


class DouBanBookViewSet(mixins.ListModelMixin,
                       mixins.RetrieveModelMixin,
                       mixins.UpdateModelMixin,
                       mixins.DestroyModelMixin,
                       viewsets.GenericViewSet):
    queryset = DouBanBook.objects.all()
    serializer_class = DouBanBookSerializer

    def get_queryset(self):
        queryset = DouBanBook.objects.all()

        name = self.request.query_params.get('name', None)
        if name is not None:
            name_list = list(map(lambda x: x.strip(), name.split(',')))
            queryset = queryset.filter(name__in=name_list)

        return queryset

    def create(self, request):
        data = request.data
        name = data['name']
        defaults = {
            'pub': data['pub'],
            'star': data['star'],
            'desc': data['desc'],
            'category': data['category'],
        }
        server_info, created = DouBanBook.objects.update_or_create(name=name, defaults=defaults)
        if created:
            status_code = status.HTTP_201_CREATED
        else:
            status_code = status.HTTP_200_OK
        return Response(json.dumps(defaults), status=status_code)