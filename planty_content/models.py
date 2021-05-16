from django.db import models
from django.utils.translation import ugettext_lazy as _
from solid_backend.content.fields import ConcatCharField, FromToConcatField
from solid_backend.content.models import BaseProfile, TreeNode

from .choices import *


class Wine(BaseProfile):
    name = models.CharField(max_length=200, verbose_name=_("Sorte"))
    synonyms = models.CharField(
        max_length=200, blank=True, null=True, verbose_name=_("Synonyme")
    )
    blossom = models.CharField(
        max_length=8,
        choices=BLOSSOM_CHOICES,
        blank=True,
        null=True,
        verbose_name=_("Blüte"),
    )
    cross_parents = models.CharField(
        max_length=200, blank=True, null=True, verbose_name=_("Kreuzungseltern")
    )
    origin = models.CharField(
        max_length=200,
        verbose_name=_("Herkunft"),
        help_text=_('Falss nicht bekannt "unbekannt" als Eingabe'),
    )

    notes = models.TextField(
        max_length=400, blank=True, null=True, verbose_name=_("Anmerkungen")
    )

    class Meta:
        verbose_name = _("Rebe")
        verbose_name_plural = _("Reben")


class Sprout(models.Model):
    tip_hairy = models.CharField(
        max_length=13,
        choices=TIP_HAIRY_CHOICES,
        blank=True,
        null=True,
        verbose_name=_("Behaarung der Triebspitze"),
    )
    tip_type = models.CharField(
        max_length=25,
        blank=True,
        null=True,
        choices=TIP_TYPE_CHOICES,
        verbose_name=_("Typ der Triebspitze"),
    )
    tip_color = models.CharField(
        max_length=200, blank=True, null=True, verbose_name=_("Farbe der Triebspitze")
    )

    hairy = models.CharField(
        max_length=4,
        blank=True,
        null=True,
        choices=YES_NO_CHOICES,
        verbose_name=_("Behaarung des Triebs"),
    )
    color = models.CharField(
        max_length=200, blank=True, null=True, verbose_name=_("Farbe des Triebs")
    )
    notes = models.TextField(
        max_length=400, blank=True, null=True, verbose_name=_("Besonderheiten")
    )

    wine = models.OneToOneField(
        Wine, related_name="sprout", on_delete=models.CASCADE, verbose_name=_("Rebe")
    )

    class Meta:
        verbose_name = _("Trieb")
        verbose_name_plural = _("Triebe")


class YoungLeaf(models.Model):

    color = models.CharField(
        max_length=200, blank=True, null=True, verbose_name=_("Farbe")
    )
    lappung = FromToConcatField(
        max_length=100,
        default="",
        blank=True,
        from_choices=LAP_CHOICES,
        to_choices=LAP_CHOICES,
        verbose_name=_("Lappung"),
    )
    notes = models.TextField(
        max_length=400, blank=True, null=True, verbose_name=_("Besonderheiten")
    )

    wine = models.OneToOneField(
        Wine,
        related_name="young_leaf",
        on_delete=models.CASCADE,
        verbose_name=_("Rebe"),
    )

    class Meta:
        verbose_name = _("Junges Blatt")
        verbose_name_plural = _("Junge Blätter")


class GrownLeaf(models.Model):
    color = models.CharField(
        max_length=200, blank=True, null=True, verbose_name=_("Farbe")
    )
    lappung = FromToConcatField(
        max_length=100,
        default="",
        blank=True,
        from_choices=LAP_CHOICES,
        to_choices=LAP_CHOICES,
        verbose_name=_("Lappung"),
    )
    edge_form = models.CharField(
        max_length=28,
        blank=True,
        null=True,
        choices=EDGE_FORM_CHOICES,
        verbose_name=_("Randform"),
    )
    structure = models.CharField(
        max_length=7,
        choices=STRUCTURE_CHOICES,
        blank=True,
        null=True,
        verbose_name=_("Struktur"),
    )
    form_spreite = models.CharField(
        max_length=12,
        choices=FORM_SPREITE_CHOICES,
        blank=True,
        null=True,
        verbose_name=_("Form der Blattspreite"),
    )

    shaft_form = FromToConcatField(
        max_length=100,
        default="",
        blank=True,
        from_choices=SHAFT_FORM_CHOICES,
        to_choices=SHAFT_FORM_CHOICES,
        verbose_name=_("Stielbuchtform"),
    )
    shaft_open = models.CharField(
        max_length=16,
        choices=SHAFT_OPEN_CHOICES,
        blank=True,
        null=True,
        verbose_name=_("Stielbuchtöffnungen"),
    )
    shaft_notes = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        verbose_name=_("Besonderheit der Stielbucht"),
    )

    hairy_top = models.CharField(
        max_length=200, blank=True, null=True, verbose_name=_("Behaarung Oberseite")
    )
    hairy_bottom = models.CharField(
        max_length=200, blank=True, null=True, verbose_name=_("Behaarung Unterseite")
    )
    hairy_nerves = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        verbose_name=_("Behaarung Nervenunterseite"),
    )

    bristle_hairy = models.CharField(
        max_length=200, blank=True, null=True, verbose_name=_("Borstenbehaarung")
    )

    shaft = models.CharField(
        max_length=200, blank=True, null=True, verbose_name=_("Blattstiel")
    )

    notes = models.TextField(
        max_length=400, blank=True, null=True, verbose_name=_("Besonderheiten")
    )

    wine = models.OneToOneField(
        Wine,
        related_name="grown_leaf",
        on_delete=models.CASCADE,
        verbose_name=_("Rebe"),
    )

    class Meta:
        verbose_name = _("Ausgewachsenes Blatt")
        verbose_name_plural = _("Ausgewachsene Blätter")


class Grape(models.Model):

    density = FromToConcatField(
        max_length=30,
        from_choices=DENSITY_CHOICES,
        to_choices=DENSITY_CHOICES,
        default="",
        blank=True,
        verbose_name=_("Dichte")
    )
    size = models.CharField(
        max_length=10, choices=SIZE_CHOICES, blank=True, null=True, verbose_name=_("Größe ohne Stiel")
    )
    form = FromToConcatField(
        max_length=55,
        from_choices=FORM_CHOICES,
        to_choices=FORM_CHOICES,
        default="",
        blank=True,
        verbose_name=_("Form")
    )
    shouldered = models.CharField(
        max_length=9, choices=SHOULDERED_CHOICES, blank=True, null=True, verbose_name=_("Geschultert")
    )
    notes = models.TextField(
        max_length=400, blank=True, null=True, verbose_name=_("Besonderheiten")
    )

    wine = models.OneToOneField(
        Wine, related_name="grape", on_delete=models.CASCADE, verbose_name=_("Rebe")
    )

    class Meta:
        verbose_name = _("Traube")
        verbose_name_plural = _("Trauben")


class Berry(models.Model):

    form = models.CharField(
        max_length=22, choices=BERRY_FORM_CHOICES, verbose_name=_("Form")
    )
    size = models.CharField(
        max_length=10, choices=BERRY_SIZE_CHOICES, verbose_name=_("Größe")
    )
    surface = models.CharField(
        max_length=9,
        null=True,
        blank=True,
        choices=BERRY_SURFACE_CHOICES,
        verbose_name=_("Oberfläche"),
    )
    color = models.CharField(
        max_length=15, choices=BERRY_COLOR_CHOICES, verbose_name=_("Farbe")
    )
    flesh_color = models.CharField(
        max_length=9,
        choices=BERRY_FLESH_COLOR_CHOICES,
        verbose_name=_("Farbe des Fruchtfleischs"),
    )
    aroma = models.CharField(
        max_length=16,
        null=True,
        blank=True,
        choices=BERRY_ARMOA_CHOICES,
        verbose_name=_("Aroma"),
    )

    notes = models.TextField(
        max_length=400, blank=True, null=True, verbose_name=_("Besonderheiten")
    )

    wine = models.OneToOneField(
        Wine, related_name="berry", on_delete=models.CASCADE, verbose_name=_("Rebe")
    )

    class Meta:
        verbose_name = _("Beere")
        verbose_name_plural = _("Beeren")


class Twine(models.Model):

    fork = models.CharField(
        max_length=23,
        null=True,
        blank=True,
        choices=FORK_CHOICES,
        verbose_name=_("Gabelung"),
    )
    series = models.CharField(
        max_length=17,
        null=True,
        blank=True,
        choices=SERIES_CHOICES,
        verbose_name=_("Rankenfolge"),
    )
    color = models.CharField(
        max_length=200, blank=True, null=True, verbose_name=_("Farbe")
    )
    hairy = models.CharField(
        max_length=200, blank=True, null=True, verbose_name=_("Behaarung")
    )

    notes = models.TextField(
        max_length=400, blank=True, null=True, verbose_name=_("Besonderheiten")
    )

    wine = models.OneToOneField(
        Wine, related_name="twine", on_delete=models.CASCADE, verbose_name=_("Rebe")
    )

    class Meta:
        verbose_name = _("Ranke")
        verbose_name_plural = _("Ranken")


class Properties(models.Model):

    claims = models.CharField(
        max_length=200, blank=True, null=True, verbose_name=_("Lageansprüche")
    )
    dry_tolerant = FromToConcatField(
        max_length=100,
        from_choices=GOOD_BAD_CHOICES,
        to_choices=GOOD_BAD_CHOICES,
        default="",
        blank=True,
        verbose_name=_("Trockentoleranz"),
    )
    chlorose = FromToConcatField(
        max_length=100,
        from_choices=GOOD_BAD_CHOICES,
        to_choices=GOOD_BAD_CHOICES,
        default="",
        blank=True,
        verbose_name=_("Chlorosefestigkeit"),
    )
    aktive_chalk = models.CharField(
        max_length=200, blank=True, null=True, verbose_name=_("Aktivkalktoleranz")
    )
    grow_pwr = FromToConcatField(
        max_length=100,
        from_choices=WEAK_STRONG_CHOICES,
        to_choices=WEAK_STRONG_CHOICES,
        default="",
        blank=True,
        verbose_name=_("Wuchskraft"),
    )
    roots = FromToConcatField(
        max_length=100,
        from_choices=GOOD_BAD_CHOICES,
        to_choices=GOOD_BAD_CHOICES,
        default="",
        blank=True,
        verbose_name=_("Bewurzelung"),
    )
    vegetation = FromToConcatField(
        max_length=100,
        from_choices=EARLY_LATE_CHOICES,
        to_choices=EARLY_LATE_CHOICES,
        default="",
        blank=True,
        verbose_name=_("Vegetationsabschluss"),
    )
    pfropf = FromToConcatField(
        max_length=100,
        from_choices=GOOD_BAD_CHOICES,
        to_choices=GOOD_BAD_CHOICES,
        default="",
        blank=True,
        verbose_name=_("Pfropfaffinität"),
    )

    notes = models.TextField(
        max_length=400, blank=True, null=True, verbose_name=_("Besonderheiten")
    )

    wine = models.OneToOneField(
        Wine,
        related_name="properties",
        on_delete=models.CASCADE,
        verbose_name=_("Rebe"),
    )

    class Meta:
        verbose_name = _("Eigenschaften")
        verbose_name_plural = verbose_name


class Phenology(models.Model):

    budding = FromToConcatField(
        max_length=100,
        from_choices=EARLY_LATE_CHOICES,
        to_choices=EARLY_LATE_CHOICES,
        default="",
        blank=True,
        verbose_name=_("Austrieb"),
    )
    bloom = FromToConcatField(
        max_length=100,
        from_choices=EARLY_LATE_CHOICES,
        to_choices=EARLY_LATE_CHOICES,
        default="",
        blank=True,
        verbose_name=_("Blütezeitpunkt"),
    )
    ripening = FromToConcatField(
        max_length=100,
        from_choices=EARLY_LATE_CHOICES,
        to_choices=EARLY_LATE_CHOICES,
        default="",
        blank=True,
        verbose_name=_("Reifezeit"),
    )

    wine = models.OneToOneField(
        Wine, related_name="phenology", on_delete=models.CASCADE, verbose_name=_("Rebe")
    )

    class Meta:
        verbose_name = _("Phänologie")
        verbose_name_plural = _("Phänologien")


class Disease(models.Model):

    oidium = models.CharField(
        max_length=4,
        null=True,
        blank=True,
        choices=YES_NO_CHOICES,
        verbose_name=_("Anfälligkeit für Oidium"),
    )
    peronospora = models.CharField(
        max_length=4,
        choices=YES_NO_CHOICES,
        null=True,
        blank=True,
        verbose_name=_("Anfälligkeit für Peronospora"),
    )
    botrytis = models.CharField(
        max_length=4,
        choices=YES_NO_CHOICES,
        null=True,
        blank=True,
        verbose_name=_("Anfälligkeit für Botrytis"),
    )

    reblaus = models.CharField(
        max_length=9,
        choices=REBLAUS_CHOICES,
        null=True,
        blank=True,
        verbose_name=_("Verhalten gegenüber Reblaus"),
    )

    wine = models.OneToOneField(
        Wine, related_name="disease", on_delete=models.CASCADE, verbose_name=_("Rebe")
    )

    class Meta:
        verbose_name = _("Krankheiten")
        verbose_name_plural = verbose_name
