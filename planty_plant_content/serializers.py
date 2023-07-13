from solid_backend.media_object.serializers import MediaObjectSerializer
from solid_backend.utils.serializers import SolidModelSerializer

from .models import (
    Appearance,
    Application,
    Bark,
    Blossom,
    Diseases,
    EcologyAndNatLocation,
    FaunaUsability,
    Fruit,
    Function,
    GeneralInformation,
    Habitat,
    HabitatFactors,
    Habitus,
    HumanUsability,
    Leaf,
    Living,
    NatBehavior,
    NatOccurence,
    Plant,
    PlantationAndCare,
    ReproductionAndProduction,
    Root,
    Sprout,
    Taxonomy,
    Toxicity,
    Usability,
    ZeigerValues,
)


class LivingSerializer(SolidModelSerializer):
    class Meta:
        model = Living
        fields = "__all__"
        depth = 1


class TaxonomyAndLivingSerializer(SolidModelSerializer):
    living = LivingSerializer()

    class Meta:
        model = Taxonomy
        exclude = ["plant"]
        depth = 1


class NatOccurenceSerializer(SolidModelSerializer):
    class Meta:
        model = NatOccurence
        fields = "__all__"
        depth = 1


class ZeigerValuesSerializer(SolidModelSerializer):
    class Meta:
        model = ZeigerValues
        fields = "__all__"
        depth = 1


class NatBehaviorSerializer(SolidModelSerializer):
    zeiger_value = ZeigerValuesSerializer()

    class Meta:
        model = NatBehavior
        fields = "__all__"
        depth = 1


class EcologyAndNatLocationSerializer(SolidModelSerializer):
    nat_occ = NatOccurenceSerializer()
    nat_behavior = NatBehaviorSerializer()

    class Meta:
        model = EcologyAndNatLocation
        exclude = ["plant"]
        depth = 1


class HabitusSerializer(SolidModelSerializer):
    class Meta:
        model = Habitus
        fields = "__all__"
        depth = 1


class SproutSerializer(SolidModelSerializer):
    class Meta:
        model = Sprout
        fields = "__all__"
        depth = 1


class LeafSerializer(SolidModelSerializer):
    class Meta:
        model = Leaf
        fields = "__all__"
        depth = 1


class BlossomSerializer(SolidModelSerializer):
    class Meta:
        model = Blossom
        fields = "__all__"
        depth = 1


class FruitSerializer(SolidModelSerializer):
    class Meta:
        model = Fruit
        fields = "__all__"
        depth = 1


class BarkSerializer(SolidModelSerializer):
    class Meta:
        model = Bark
        fields = "__all__"
        depth = 1


class RootSerializer(SolidModelSerializer):
    class Meta:
        model = Root
        fields = "__all__"
        depth = 1


class AppearanceSerializer(SolidModelSerializer):
    habitus = HabitusSerializer()
    sprout = SproutSerializer()
    leaf = LeafSerializer()
    blossom = BlossomSerializer()
    fruit = FruitSerializer()
    bark = BarkSerializer()
    root = RootSerializer()

    class Meta:
        model = Appearance
        exclude = ["plant"]
        depth = 1


class HabitatSerializer(SolidModelSerializer):
    class Meta:
        model = Habitat
        fields = "__all__"
        depth = 1


class HabitatFactorsSerializer(SolidModelSerializer):
    class Meta:
        model = HabitatFactors
        fields = "__all__"
        depth = 1


class FunctionSerializer(SolidModelSerializer):
    class Meta:
        model = Function
        fields = "__all__"
        depth = 1


class ApplicationSerializer(SolidModelSerializer):
    habitat = HabitatSerializer()
    habitat_factors = HabitatFactorsSerializer()
    appl_function = FunctionSerializer()

    class Meta:
        model = Application
        exclude = ["plant"]
        depth = 1


class PlantationAndCareSerializer(SolidModelSerializer):
    class Meta:
        model = PlantationAndCare
        exclude = ["plant"]
        depth = 1


class ReproductionAndProductionSerializer(SolidModelSerializer):
    class Meta:
        model = ReproductionAndProduction
        exclude = ["plant"]
        depth = 1


class ToxicitySerializer(SolidModelSerializer):
    class Meta:
        model = Toxicity
        fields = "__all__"
        depth = 1


class FaunaUsabilitySerializer(SolidModelSerializer):
    class Meta:
        model = FaunaUsability
        fields = "__all__"
        depth = 1


class HumanUsabilitySerializer(SolidModelSerializer):
    class Meta:
        model = HumanUsability
        fields = "__all__"
        depth = 1


class UsabilitySerializer(SolidModelSerializer):
    toxicity = ToxicitySerializer()
    fauna_usability = FaunaUsabilitySerializer()
    human_usability = HumanUsabilitySerializer()

    class Meta:
        model = Usability
        exclude = ["plant"]
        depth = 1


class DiseasesSerializer(SolidModelSerializer):
    class Meta:
        model = Diseases
        exclude = ["plant"]
        depth = 1


class PlantGeneralInformationSerializer(SolidModelSerializer):
    class Meta:
        model = GeneralInformation
        exclude = ["plant"]
        depth = 1


class PlantSerializer(SolidModelSerializer):

    taxonomy = TaxonomyAndLivingSerializer(required=False)
    ecology_and_natlocation = EcologyAndNatLocationSerializer(required=False)
    appearance = AppearanceSerializer(required=False)
    application = ApplicationSerializer(required=False)
    plantation_and_creation = PlantationAndCareSerializer(required=False)
    reproduction_and_production = ReproductionAndProductionSerializer(required=False)
    usability = UsabilitySerializer(required=False)
    disease = DiseasesSerializer(required=False)
    general_information = PlantGeneralInformationSerializer(required=False)
    media_objects = MediaObjectSerializer(many=True)

    class Meta:
        model = Plant
        fields = "__all__"
        depth = 1
