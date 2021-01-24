from rest_framework import serializers
from .models import Wine, Sprout, YoungLeaf, GrownLeaf, Grape, Berry, Twine, Properties, Phenology, Disease



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
    grape = GrapeSerializer()
    berry = BerrySerializer()
    twine = TwineSerializer()
    properties = PropertiesSerializer()
    phenology = PhenologySerializer()
    disease = DiseaseSerializer()

    class Meta:
        model = Wine
        fields = "__all__"
        depth = 1
