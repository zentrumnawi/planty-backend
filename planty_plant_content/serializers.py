
from .models import Plant, Taxonomy, Living
from planty_content.serializers import DisplayNameModelSerializer
from rest_framework.serializers import Serializer


class LivingSerializer(DisplayNameModelSerializer):
    class Meta:
        model = Living
        fields = "__all__"
        depth = 1


class TaxonomyAndLivingSerializer(DisplayNameModelSerializer):
    living = LivingSerializer()

    class Meta:
        model = Taxonomy
        exclude = ["plant"]
        depth = 1


class PlantSerializer(DisplayNameModelSerializer):

    living = TaxonomyAndLivingSerializer()
    ecology_and_natlocation = Serializer()
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
