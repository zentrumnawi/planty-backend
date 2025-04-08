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
    YoungLeaf, GeneralInformation,
)

# Register your models here.


class SproutInline(admin.StackedInline):
    model = Sprout


class YoungLeafInline(admin.StackedInline):
    model = YoungLeaf


class GrownLeafInline(admin.StackedInline):
    model = GrownLeaf


class GrapeInline(admin.StackedInline):
    model = Grape


class BerryInline(admin.StackedInline):
    model = Berry


class TwineInline(admin.StackedInline):
    model = Twine


class PropertiesInline(admin.StackedInline):
    model = Properties


class PhenologyInline(admin.StackedInline):
    model = Phenology


class DiseaseInline(admin.StackedInline):
    model = Disease


class GeneralInformationInline(admin.StackedInline):
    model = GeneralInformation


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

    def get_name(self, obj):
        return obj.general_information.name

    def get_synonyms(self, obj):
        return obj.general_information.synonyms


admin.site.register(GeneralInformation, admin.ModelAdmin)
admin.site.register(Sprout, admin.ModelAdmin)
admin.site.register(YoungLeaf, admin.ModelAdmin)
admin.site.register(GrownLeaf, admin.ModelAdmin)
admin.site.register(Grape, admin.ModelAdmin)
admin.site.register(Berry, admin.ModelAdmin)
admin.site.register(Twine, admin.ModelAdmin)
admin.site.register(Properties, admin.ModelAdmin)
admin.site.register(Phenology, admin.ModelAdmin)
admin.site.register(Disease, admin.ModelAdmin)

admin.site.register(Wine, WineModelAdmin)
