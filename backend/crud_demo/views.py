from django.shortcuts import render

# Create your views here.
from crud_demo.models import CrudDemoModel
from crud_demo.serializers import CrudDemoModelSerializer, CrudDemoModelCreateUpdateSerializer
from dvadmin.utils.viewset import CustomModelViewSet


class CrudDemoModelViewSet(CustomModelViewSet):
    """
    list:Inquire
    create:new
    update:Revise
    retrieve:read
    destroy:delete
    """
    queryset = CrudDemoModel.objects.all()
    serializer_class = CrudDemoModelSerializer
    create_serializer_class = CrudDemoModelCreateUpdateSerializer
    update_serializer_class = CrudDemoModelCreateUpdateSerializer
    filter_fields = ['goods', 'goods_price']
    search_fields = ['goods']