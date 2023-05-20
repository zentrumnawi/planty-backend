
from .models import Plant, Taxonomy, Living, EcologyAndNatLocation, NatOccurence, ZeigerValues, NatBehavior
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


class NatOccurenceSerializer(DisplayNameModelSerializer):
    
    class Meta:
        model = NatOccurence
        fields = "__all__"
        depth = 1


class ZeigerValuesSerializer(DisplayNameModelSerializer):
    
    class Meta:
        model = ZeigerValues
        fields = "__all__"
        depth = 1


class NatBehaviorSerializer(DisplayNameModelSerializer):
    zeiger_value = ZeigerValuesSerializer()

    class Meta:
        model = NatBehavior
        fields = "__all__"
        depth = 1


class EcologyAndNatLocationSerializer(DisplayNameModelSerializer):
    nat_occ = NatOccurenceSerializer()
    nat_behavior = NatBehaviorSerializer()

    class Meta:
        model = EcologyAndNatLocation
        exclude = ["plant"]
        depth = 1


class PlantSerializer(DisplayNameModelSerializer):

    living = TaxonomyAndLivingSerializer()
    ecology_and_natlocation = EcologyAndNatLocationSerializer()
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
