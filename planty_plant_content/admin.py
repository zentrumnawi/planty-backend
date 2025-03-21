from django.contrib import admin
from solid_backend.media_object.admin import (
    AudioVideoMediaObjectInline,
    ImageMediaObjectInline,
)

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
    raw_id_fields=["plant", "nat_occ", "nat_behavior"]


class TaxonomyInline(admin.StackedInline):
    model = Taxonomy
    raw_id_fields=["plant", "living"]


class AppearanceInline(admin.StackedInline):
    model = Appearance
    raw_id_fields=["plant", "habitus", "sprout", "leaf", "blossom", "fruit", "bark", "root"]


class ApplicationInline(admin.StackedInline):
    model = Application
    raw_id_fields=["plant", "habitat", "habitat_factors", "appl_function"]


class PlantationAndCareInline(admin.StackedInline):
    model = PlantationAndCare


class ReproductionAndProductionInline(admin.StackedInline):
    model = ReproductionAndProduction


class UsabilityInline(admin.StackedInline):
    model = Usability
    raw_id_fields=["plant", "toxicity", "fauna_usability", "human_usability"]

class DiseasesInline(admin.StackedInline):
    model = Diseases


class GeneralInformationInline(admin.StackedInline):
    model = GeneralInformation
    fields = (
        "info",
        "geo_data",
        "name",
        "sub_name",
        "literature"
    )


class PlantAdmin(admin.ModelAdmin):

    inlines = [
        GeneralInformationInline,
        TaxonomyInline,
        EcologyAndNatLocationInline,
        AppearanceInline,
        ApplicationInline,
        PlantationAndCareInline,
        ReproductionAndProductionInline,
        UsabilityInline,
        DiseasesInline,
        ImageMediaObjectInline,
        AudioVideoMediaObjectInline,
    ]

    list_display = ["id", "get_bot_name", "get_name"]
    ordering = ("general_information__name",)
    raw_id_fields = ['tree_node']

    @admin.decorators.display(description="Bot. Name")
    def get_bot_name(self, obj):
        return obj.general_information.name

    @admin.decorators.display(description="Name")
    def get_name(self, obj):
        return obj.general_information.sub_name

    class Meta:
        model = Plant

class AppearanceModelAdmin(admin.ModelAdmin):
    raw_id_fields=["plant", "habitus", "sprout", "leaf", "blossom", "fruit", "bark", "root"]

class UsabilityModelAdmin(admin.ModelAdmin):
    raw_id_fields=["plant", "toxicity", "fauna_usability", "human_usability"]

class ApplicationModelAdmin(admin.ModelAdmin):
    raw_id_fields=["plant", "habitat", "habitat_factors", "appl_function"]

class EcologyAndNatLocationModelAdmin(admin.ModelAdmin):
    raw_id_fields=["plant", "nat_occ", "nat_behavior"]

class TaxonomyModelAdmin(admin.ModelAdmin):
    raw_id_fields=["plant", "living"]

class ReproductionAndProductionModelAdmin(admin.ModelAdmin):
    raw_id_fields=["plant"]

class DiseasesModelAdmin(admin.ModelAdmin):
    raw_id_fields=["plant"]

class PlantationAndCareModelAdmin(admin.ModelAdmin):
    raw_id_fields=["plant"]

class GeneralInformationModelAdmin(admin.ModelAdmin):
    raw_id_fields=["plant"]

class NatBehaviorModelAdmin(admin.ModelAdmin):
    raw_id_fields=["zeiger_value"]

admin.site.register(Taxonomy, TaxonomyModelAdmin)
admin.site.register(Living, admin.ModelAdmin)
admin.site.register(NatBehavior, NatBehaviorModelAdmin)
admin.site.register(NatOccurence, admin.ModelAdmin)
admin.site.register(ZeigerValues, admin.ModelAdmin)
admin.site.register(EcologyAndNatLocation, EcologyAndNatLocationModelAdmin)
admin.site.register(Habitus, admin.ModelAdmin)
admin.site.register(Sprout, admin.ModelAdmin)
admin.site.register(Leaf, admin.ModelAdmin)
admin.site.register(Blossom, admin.ModelAdmin)
admin.site.register(Fruit, admin.ModelAdmin)
admin.site.register(Bark, admin.ModelAdmin)
admin.site.register(Root, admin.ModelAdmin)
admin.site.register(Appearance, AppearanceModelAdmin)
admin.site.register(Habitat, admin.ModelAdmin)
admin.site.register(HabitatFactors, admin.ModelAdmin)
admin.site.register(Function, admin.ModelAdmin)
admin.site.register(Application, ApplicationModelAdmin)
admin.site.register(PlantationAndCare, PlantationAndCareModelAdmin)
admin.site.register(ReproductionAndProduction, ReproductionAndProductionModelAdmin)
admin.site.register(Toxicity, admin.ModelAdmin)
admin.site.register(FaunaUsability, admin.ModelAdmin)
admin.site.register(HumanUsability, admin.ModelAdmin)
admin.site.register(Usability, UsabilityModelAdmin)
admin.site.register(Diseases, DiseasesModelAdmin)
admin.site.register(GeneralInformation, GeneralInformationModelAdmin)

admin.site.register(Plant, PlantAdmin)
