from crud_demo.models import CrudDemoModel
from dvadmin.utils.serializers import CustomModelSerializer


class CrudDemoModelSerializer(CustomModelSerializer):
    """
    serializer
    """

    class Meta:
        model = CrudDemoModel
        fields = "__all__"


class CrudDemoModelCreateUpdateSerializer(CustomModelSerializer):
    """
    Serializer on create/update
    """

    class Meta:
        model = CrudDemoModel
        fields = '__all__'