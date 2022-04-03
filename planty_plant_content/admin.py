from django.contrib import admin

from .models import Plant, Taxonomy, Living
# Register your models here.


class TaxonomyInline(admin.StackedInline):
    model = Taxonomy


class PlantAdmin(admin.ModelAdmin):
    inlines = [TaxonomyInline, ]

    class Meta:
        model = Plant


admin.site.register(Plant, PlantAdmin)
admin.site.register(Taxonomy, admin.ModelAdmin)
admin.site.register(Living, admin.ModelAdmin)
