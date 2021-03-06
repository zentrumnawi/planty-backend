from django.contrib import admin
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


class WineModelAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "ger_name", "synonyms"]
    inlines = [
        SproutInline,
        YoungLeafInline,
        GrownLeafInline,
        GrapeInline,
        BerryInline,
        TwineInline,
        PropertiesInline,
        PhenologyInline,
        DiseaseInline,
        PhotographInline,
    ]


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
