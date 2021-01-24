from rest_framework.serializers import ModelSerializer


class WineSerializer(ModelSerializer):

    class Meta:
        model = None
        fields = "__all__"
        depth = 1
