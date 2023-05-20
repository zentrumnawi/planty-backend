
from .models import Plant
from planty_content.serializers import DisplayNameModelSerializer
from rest_framework.serializers import Serializer


class PlantSerializer(DisplayNameModelSerializer):

    living = Serializer()
    ecology_andd_natlocation = Serializer()
    appearance = Serializer()
    application = Serializer()
    plantation_and_creation = Serializer()
    reproduction_and_production = Serializer()
    usability = Serializer()
    disease = Serializer()
    general_information = Serializer()

    class Meta:
        model = Plant
        fields = "__all__"
        depth = 1
