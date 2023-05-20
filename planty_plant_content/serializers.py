
from .models import Plant
from planty_content.serializers import DisplayNameModelSerializer


class PlantSerializer(DisplayNameModelSerializer):

    class Meta:
        model = Plant
        fields = "__all__"
        depth = 1
