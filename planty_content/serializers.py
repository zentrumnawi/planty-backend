from rest_framework import serializers
from solid_backend.media_object.serializers import MediaObjectSerializer
from solid_backend.photograph.serializers import PhotographSerializer

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
)


class DisplayNameModelSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        ret = super(DisplayNameModelSerializer, self).to_representation(instance)

        return serializers.OrderedDict(filter(lambda x: not x[1] is None, ret.items()))


class SproutSerializer(DisplayNameModelSerializer):
    class Meta:
        model = Sprout
        exclude = ["wine"]
        swagger_schema_fields = {"title": str(model._meta.verbose_name)}


class YoungLeafSerializer(DisplayNameModelSerializer):
    class Meta:
        model = YoungLeaf
        exclude = ["wine"]
        swagger_schema_fields = {"title": str(model._meta.verbose_name)}


class GrownLeafSerializer(DisplayNameModelSerializer):
    class Meta:
        model = GrownLeaf
        exclude = ["wine"]
        swagger_schema_fields = {"title": str(model._meta.verbose_name)}


class GrapeSerializer(DisplayNameModelSerializer):
    class Meta:
        model = Grape
        exclude = ["wine"]
        swagger_schema_fields = {"title": str(model._meta.verbose_name)}


class BerrySerializer(DisplayNameModelSerializer):
    class Meta:
        model = Berry
        exclude = ["wine"]
        swagger_schema_fields = {"title": str(model._meta.verbose_name)}


class TwineSerializer(DisplayNameModelSerializer):
    class Meta:
        model = Twine
        exclude = ["wine"]
        swagger_schema_fields = {"title": str(model._meta.verbose_name)}


class PropertiesSerializer(DisplayNameModelSerializer):
    class Meta:
        model = Properties
        exclude = ["wine"]
        swagger_schema_fields = {"title": str(model._meta.verbose_name)}


class PhenologySerializer(DisplayNameModelSerializer):
    class Meta:
        model = Phenology
        exclude = ["wine"]
        swagger_schema_fields = {"title": str(model._meta.verbose_name)}


class DiseaseSerializer(DisplayNameModelSerializer):
    class Meta:
        model = Disease
        exclude = ["wine"]
        swagger_schema_fields = {"title": str(model._meta.verbose_name)}


class WineSerializer(DisplayNameModelSerializer):
    sprout = SproutSerializer()
    young_leaf = YoungLeafSerializer()
    grown_leaf = GrownLeafSerializer()
    grape = GrapeSerializer(required=False)
    berry = BerrySerializer(required=False)
    twine = TwineSerializer(required=False)
    properties = PropertiesSerializer()
    phenology = PhenologySerializer(required=False)
    disease = DiseaseSerializer()
    media_objects = MediaObjectSerializer(many=True)

    class Meta:
        model = Wine
        fields = "__all__"
        depth = 1
