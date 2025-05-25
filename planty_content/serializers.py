from solid_backend.media_object.serializers import MediaObjectSerializer
from solid_backend.utils.serializers import SolidModelSerializer
from .models import (
    Berry,
    Disease,
    Grape,
    GrownLeaf,
    Phenology,
    Properties,
    Sprout,
    Twine,
    Wine,
    YoungLeaf,
    GeneralInformation,
)


class SproutSerializer(SolidModelSerializer):
    class Meta:
        model = Sprout
        exclude = ["wine"]
        swagger_schema_fields = {"title": str(model._meta.verbose_name)}


class YoungLeafSerializer(SolidModelSerializer):
    class Meta:
        model = YoungLeaf
        exclude = ["wine"]
        swagger_schema_fields = {"title": str(model._meta.verbose_name)}


class GrownLeafSerializer(SolidModelSerializer):
    class Meta:
        model = GrownLeaf
        exclude = ["wine"]
        swagger_schema_fields = {"title": str(model._meta.verbose_name)}


class GrapeSerializer(SolidModelSerializer):
    class Meta:
        model = Grape
        exclude = ["wine"]
        swagger_schema_fields = {"title": str(model._meta.verbose_name)}


class BerrySerializer(SolidModelSerializer):
    class Meta:
        model = Berry
        exclude = ["wine"]
        swagger_schema_fields = {"title": str(model._meta.verbose_name)}


class TwineSerializer(SolidModelSerializer):
    class Meta:
        model = Twine
        exclude = ["wine"]
        swagger_schema_fields = {"title": str(model._meta.verbose_name)}


class PropertiesSerializer(SolidModelSerializer):
    class Meta:
        model = Properties
        exclude = ["wine"]
        swagger_schema_fields = {"title": str(model._meta.verbose_name)}


class PhenologySerializer(SolidModelSerializer):
    class Meta:
        model = Phenology
        exclude = ["wine"]
        swagger_schema_fields = {"title": str(model._meta.verbose_name)}


class DiseaseSerializer(SolidModelSerializer):
    class Meta:
        model = Disease
        exclude = ["wine"]
        swagger_schema_fields = {"title": str(model._meta.verbose_name)}


class WineGeneralInformationSerializer(SolidModelSerializer):
    class Meta:
        model = GeneralInformation
        exclude = ["wine"]
        swagger_schema_fields = {"title": str(model._meta.verbose_name)}


class WineSerializer(SolidModelSerializer):
    sprout = SproutSerializer()
    young_leaf = YoungLeafSerializer()
    grown_leaf = GrownLeafSerializer()
    grape = GrapeSerializer(required=False)
    berry = BerrySerializer(required=False)
    twine = TwineSerializer(required=False)
    properties = PropertiesSerializer()
    phenology = PhenologySerializer(required=False)
    disease = DiseaseSerializer()
    general_information = WineGeneralInformationSerializer()
    media_objects = MediaObjectSerializer(many=True)

    class Meta:
        model = Wine
        fields = "__all__"
        depth = 1
