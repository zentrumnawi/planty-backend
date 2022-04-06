from django.contrib import admin

from .models import Plant, Taxonomy, Living, NatBehavior, NatOccurence, ZeigerValues, EcologyAndNatLocation
# Register your models here.


class EcologyAndNatLocationInline(admin.StackedInline):
    model = EcologyAndNatLocation


class TaxonomyInline(admin.StackedInline):
    model = Taxonomy


class PlantAdmin(admin.ModelAdmin):
    inlines = [TaxonomyInline, EcologyAndNatLocationInline]

    class Meta:
        model = Plant


admin.site.register(Taxonomy, admin.ModelAdmin)
admin.site.register(Living, admin.ModelAdmin)
admin.site.register(NatBehavior, admin.ModelAdmin)
admin.site.register(NatOccurence, admin.ModelAdmin)
admin.site.register(ZeigerValues, admin.ModelAdmin)
admin.site.register(EcologyAndNatLocation, admin.ModelAdmin)

admin.site.register(Plant, PlantAdmin)

