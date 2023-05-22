from rest_framework.serializers import Serializer

from planty_content.serializers import DisplayNameModelSerializer

from .models import (
    Appearance,
    Bark,
    Blossom,
    EcologyAndNatLocation,
    Fruit,
    Habitus,
    Leaf,
    Living,
    NatBehavior,
    NatOccurence,
    Plant,
    Root,
    Sprout,
    Taxonomy,
    ZeigerValues,
    Application,
    Function,
    HabitatFactors,
    Habitat,
    PlantationAndCare,
    ReproductionAndProduction,
    Usability,
    Toxicity,
    FaunaUsability,
    HumanUsability,
    Diseases,
    GeneralInformation
)


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


class HabitusSerializer(DisplayNameModelSerializer):
    class Meta:
        model = Habitus
        fields = "__all__"
        depth = 1


class SproutSerializer(DisplayNameModelSerializer):
    class Meta:
        model = Sprout
        fields = "__all__"
        depth = 1


class LeafSerializer(DisplayNameModelSerializer):
    class Meta:
        model = Leaf
        fields = "__all__"
        depth = 1


class BlossomSerializer(DisplayNameModelSerializer):
    class Meta:
        model = Blossom
        fields = "__all__"
        depth = 1


class FruitSerializer(DisplayNameModelSerializer):
    class Meta:
        model = Fruit
        fields = "__all__"
        depth = 1


class BarkSerializer(DisplayNameModelSerializer):
    class Meta:
        model = Bark
        fields = "__all__"
        depth = 1


class RootSerializer(DisplayNameModelSerializer):
    class Meta:
        model = Root
        fields = "__all__"
        depth = 1


class AppearanceSerializer(DisplayNameModelSerializer):
    habitus = HabitusSerializer()
    sprout = SproutSerializer()
    leaf = LeafSerializer
    blossom = BlossomSerializer()
    fruit = FruitSerializer()
    bark = BarkSerializer()
    root = RootSerializer()

    class Meta:
        model = Appearance
        exclude = ["plant"]
        depth = 1


class HabitatSerializer(DisplayNameModelSerializer):
    class Meta:
        model = Habitat
        fields = "__all__"
        depth = 1


class HabitatFactorsSerializer(DisplayNameModelSerializer):
    class Meta:
        model = HabitatFactors
        fields = "__all__"
        depth = 1


class FunctionSerializer(DisplayNameModelSerializer):
    class Meta:
        model = Function
        fields = "__all__"
        depth = 1


class ApplicationSerializer(DisplayNameModelSerializer):
    habitat = HabitatSerializer()
    habitat_factors = HabitatFactorsSerializer()
    appl_function = FunctionSerializer()

    class Meta:
        model = Application
        exclude = ["plant"]
        depth = 1


class PlantationAndCareSerializer(DisplayNameModelSerializer):

    class Meta:
        model = PlantationAndCare
        exclude = ["plant"]
        depth = 1


class ReproductionAndProductionSerializer(DisplayNameModelSerializer):

    class Meta:
        model = ReproductionAndProduction
        exclude = ["plant"]
        depth = 1


class ToxicitySerializer(DisplayNameModelSerializer):
    class Meta:
        model = Toxicity
        fields = "__all__"
        depth = 1


class FaunaUsabilitySerializer(DisplayNameModelSerializer):
    class Meta:
        model = FaunaUsability
        fields = "__all__"
        depth = 1


class HumanUsabilitySerializer(DisplayNameModelSerializer):
    class Meta:
        model = HumanUsability
        fields = "__all__"
        depth = 1


class UsabilitySerializer(DisplayNameModelSerializer):
    toxicity = ToxicitySerializer()
    fauna_usability = FaunaUsabilitySerializer()
    human_usability = HumanUsabilitySerializer()

    class Meta:
        model = Usability
        exclude = ["plant"]
        depth = 1


class DiseasesSerializer(DisplayNameModelSerializer):
    class Meta:
        model = Diseases
        exclude = ["plant"]
        depth = 1
        

class GeneralInformationSerializer(DisplayNameModelSerializer):
    class Meta:
        model = GeneralInformation
        exclude = ["plant"]
        depth = 1


class PlantSerializer(DisplayNameModelSerializer):

    living = TaxonomyAndLivingSerializer()
    ecology_and_natlocation = EcologyAndNatLocationSerializer()
    appearance = AppearanceSerializer()
    application = ApplicationSerializer()
    plantation_and_creation = PlantationAndCareSerializer()
    reproduction_and_production = ReproductionAndProductionSerializer()
    usability = UsabilitySerializer()
    disease = DiseasesSerializer()
    general_information = GeneralInformationSerializer()

    class Meta:
        model = Plant
        fields = "__all__"
        depth = 1
