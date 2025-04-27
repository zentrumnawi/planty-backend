from django.contrib import admin
from solid_backend.media_object.admin import (
    AudioVideoMediaObjectInline,
    ImageMediaObjectInline,
)
from solid_backend.photograph.admin import PhotographInline

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

# Register your models here.


class SproutInline(admin.StackedInline):
    model = Sprout
    raw_id_fields = ["wine"]


class YoungLeafInline(admin.StackedInline):
    model = YoungLeaf
    raw_id_fields = ["wine"]


class GrownLeafInline(admin.StackedInline):
    model = GrownLeaf
    raw_id_fields = ["wine"]


class GrapeInline(admin.StackedInline):
    model = Grape
    raw_id_fields = ["wine"]


class BerryInline(admin.StackedInline):
    model = Berry
    raw_id_fields = ["wine"]


class TwineInline(admin.StackedInline):
    model = Twine
    raw_id_fields = ["wine"]


class PropertiesInline(admin.StackedInline):
    model = Properties
    raw_id_fields = ["wine"]


class PhenologyInline(admin.StackedInline):
    model = Phenology
    raw_id_fields = ["wine"]


class DiseaseInline(admin.StackedInline):
    model = Disease
    raw_id_fields = ["wine"]


class GeneralInformationInline(admin.StackedInline):
    model = GeneralInformation
    raw_id_fields = ["wine"]


class WineModelAdmin(admin.ModelAdmin):
    list_display = ["id", "get_name", "get_synonyms"]
    inlines = [
        GeneralInformationInline,
        SproutInline,
        YoungLeafInline,
        GrownLeafInline,
        GrapeInline,
        BerryInline,
        TwineInline,
        PropertiesInline,
        PhenologyInline,
        DiseaseInline,
        ImageMediaObjectInline,
        AudioVideoMediaObjectInline,
    ]
    raw_id_fields = ["tree_node"]

    def get_name(self, obj):
        return obj.general_information.name

    def get_synonyms(self, obj):
        return obj.general_information.synonyms


class DiseaseModelAdmin(admin.ModelAdmin):
    raw_id_fields = ["wine"]


class GrapeModelAdmin(admin.ModelAdmin):
    raw_id_fields = ["wine"]


class BerryModelAdmin(admin.ModelAdmin):
    raw_id_fields = ["wine"]


class PhenologyModelAdmin(admin.ModelAdmin):
    raw_id_fields = ["wine"]


class PropertiesModelAdmin(admin.ModelAdmin):
    raw_id_fields = ["wine"]


class YoungLeafModelAdmin(admin.ModelAdmin):
    raw_id_fields = ["wine"]


class GrownLeafModelAdmin(admin.ModelAdmin):
    raw_id_fields = ["wine"]


class TwineModelAdmin(admin.ModelAdmin):
    raw_id_fields = ["wine"]


class GeneralInformationModelAdmin(admin.ModelAdmin):
    raw_id_fields = ["wine"]


class SproutModelAdmin(admin.ModelAdmin):
    raw_id_fields = ["wine"]


admin.site.register(GeneralInformation, GeneralInformationModelAdmin)
admin.site.register(Sprout, SproutModelAdmin)
admin.site.register(YoungLeaf, YoungLeafModelAdmin)
admin.site.register(GrownLeaf, GrownLeafModelAdmin)
admin.site.register(Grape, GrapeModelAdmin)
admin.site.register(Berry, BerryModelAdmin)
admin.site.register(Twine, TwineModelAdmin)
admin.site.register(Properties, PropertiesModelAdmin)
admin.site.register(Phenology, PhenologyModelAdmin)
admin.site.register(Disease, DiseaseModelAdmin)

admin.site.register(Wine, WineModelAdmin)
