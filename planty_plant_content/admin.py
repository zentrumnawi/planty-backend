from django.contrib import admin

from .models import (
    Plant, Taxonomy, Living, NatBehavior, NatOccurence, ZeigerValues, EcologyAndNatLocation, Habitus, Sprout, Leaf,
    Blossom, Fruit, Bark, Root, Appearance
                     )
# Register your models here.


class EcologyAndNatLocationInline(admin.StackedInline):
    model = EcologyAndNatLocation


class TaxonomyInline(admin.StackedInline):
    model = Taxonomy


class AppearanceInline(admin.StackedInline):
    model = Appearance


class PlantAdmin(admin.ModelAdmin):
    inlines = [TaxonomyInline, EcologyAndNatLocationInline, AppearanceInline]

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

admin.site.register(Plant, PlantAdmin)

