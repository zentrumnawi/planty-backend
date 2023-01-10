from django.contrib import admin
from solid_backend.media_object.admin import AudioVideoMediaObjectInline, ImageMediaObjectInline

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

# Register your models here.


class EcologyAndNatLocationInline(admin.StackedInline):
    model = EcologyAndNatLocation


class TaxonomyInline(admin.StackedInline):
    model = Taxonomy


class AppearanceInline(admin.StackedInline):
    model = Appearance


class ApplicationInline(admin.StackedInline):
    model = Application


class PlantationAndCareInline(admin.StackedInline):
    model = PlantationAndCare


class ReproductionAndProductionInline(admin.StackedInline):
    model = ReproductionAndProduction


class UsabilityInline(admin.StackedInline):
    model = Usability


class DiseasesInline(admin.StackedInline):
    model = Diseases


class GeneralInformationInline(admin.StackedInline):
    model = GeneralInformation


class PlantAdmin(admin.ModelAdmin):
    inlines = [
        TaxonomyInline,
        EcologyAndNatLocationInline,
        AppearanceInline,
        ApplicationInline,
        PlantationAndCareInline,
        ReproductionAndProductionInline,
        UsabilityInline,
        DiseasesInline,
        GeneralInformationInline,
        ImageMediaObjectInline,
        AudioVideoMediaObjectInline
    ]

    class Meta:
        model = Plant


admin.site.register(Taxonomy, admin.ModelAdmin)
admin.site.register(Living, admin.ModelAdmin)
admin.site.register(NatBehavior, admin.ModelAdmin)
admin.site.register(NatOccurence, admin.ModelAdmin)
admin.site.register(ZeigerValues, admin.ModelAdmin)
admin.site.register(EcologyAndNatLocation, admin.ModelAdmin)
admin.site.register(Habitus, admin.ModelAdmin)
admin.site.register(Sprout, admin.ModelAdmin)
admin.site.register(Leaf, admin.ModelAdmin)
admin.site.register(Blossom, admin.ModelAdmin)
admin.site.register(Fruit, admin.ModelAdmin)
admin.site.register(Bark, admin.ModelAdmin)
admin.site.register(Root, admin.ModelAdmin)
admin.site.register(Appearance, admin.ModelAdmin)
admin.site.register(Habitat, admin.ModelAdmin)
admin.site.register(HabitatFactors, admin.ModelAdmin)
admin.site.register(Function, admin.ModelAdmin)
admin.site.register(Application, admin.ModelAdmin)
admin.site.register(PlantationAndCare, admin.ModelAdmin)
admin.site.register(ReproductionAndProduction, admin.ModelAdmin)
admin.site.register(Toxicity, admin.ModelAdmin)
admin.site.register(FaunaUsability, admin.ModelAdmin)
admin.site.register(HumanUsability, admin.ModelAdmin)
admin.site.register(Usability, admin.ModelAdmin)
admin.site.register(Diseases, admin.ModelAdmin)
admin.site.register(GeneralInformation, admin.ModelAdmin)

admin.site.register(Plant, PlantAdmin)
