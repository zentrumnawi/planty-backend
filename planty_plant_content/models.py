from enum import IntEnum, Enum

from django.db import models
from django.utils.translation import ugettext_lazy as _

from planty_content.choices import YES_NO_CHOICES


class ChoiceEnum(Enum):

    @classmethod
    def choices(cls):
        return ((str(i.value), i.name) for i in cls)


class Plant(models.Model):
    class Meta:
        verbose_name = _("Pflanze")
        verbose_name_plural = _("Pflanzen")


class Living(models.Model):

    LIVING_CHOICES = ChoiceEnum(
        "LivingChoices",
        (
            "Hydrophyt",
            "krautiger",
            "Chamaephyt",
            "Geophyt",
            "Hemikryptophyt",
            "Nanophanerophyt",
            "Phanerophyt",
            "Therophyt",
            "holziger Chamaephyt",
            "Liane / Spreitzklimmer",
            "Epiphyt",
            "Halbparasit",
            "Vollparasit"
        )
    ).choices()

    LIFESPAN_CHOICES = ChoiceEnum(
        "LifespanChoices",
        (
            "ausdauernd, sehr kurz überdauernd ( < 50 J)?",
            "ausdauernd, kurz überdauernd(50 - 100J)",
            "ausdauernd, mäßig dauerhaft(100 - 300J)",
            "ausdauernd, dauerhaft(300 - 500J)",
            "ausdauernd, sehr dauerhaft(ü 500J)",
        )
    ).choices()

    living_accord = models.CharField(
        max_length=22,
        choices=LIVING_CHOICES,
        null=True, blank=True,
        verbose_name=_("Lebensform nach Raukiær (1919)"),
        help_text=_("Klare Zuweisung einer Kategorie, erweiterbar:")
    )
    spec_living = models.CharField(max_length=100, null=True, blank=True, verbose_name=_("Besonderes zur Lebensweise"))
    life_span = models.CharField(max_length=44, choices=LIFESPAN_CHOICES, verbose_name=_("Lebensdauer"))
    extra = models.TextField(max_length=500, null=True, blank=True, verbose_name=_("Weiteres zur Lebensdauer"), help_text=_("Nur solitär stehend so alt werdend; unter Konkurrenz kurzlebiger"))

    class Meta:
        verbose_name = _("Lebensweise")
        verbose_name_plural = _("Lebensweisen")


class Taxonomy(models.Model):
    FAMILY_CHOICES = ChoiceEnum(
        "FamilyChoices",
        (
            "Amaryllidaceae(Narzissengewächse)",
            "Apiaceae (Doldenblütler)",
            "Asteraceae(Korbblütler)",
            "Boraginaceae(Raublattgewächse)",
            "Brassicaceae(Kreuzblütengewächse)",
            "Campanulaceae(Glockenblumengewächse)",
            "Caryophyllaceae(Nelkengewächse)",
            "Ericaceae(Heidekrautgewächse)",
            "Euphorbiaceae(Wolfsmilchgewächse)",
            "Fabaceae(Hülsenfrüchtler)",
            "Fagaceae(Buchengewächse)",
            "Gentianaceae(Enziangewächse)",
            "Iridaceae(Schwertliliengewächse)",
            "Lamiaceae(Lippenblütler)",
            "Liliaceae(Liliengewächse)",
            "Magnoliaceae(Magnoliengewächse)",
            "Malvaceae(Malvengewächse)",
            "Nymphaeaceae(Seerosengewächse)",
            "Orchidaceae(Orchideengewächse)",
            "Papaveraceae(Mohngewächse)",
            "Poaceae(Süssgräser)",
            "Primulaceae(Primelgewächse)",
            "Ranunculaceae(Hahnenfussgewächse)",
            "Rosaceae(Rosengewächse)",
            "Scrophulariaceae(Rachenblütler)",
            "Solanaceae(Nachtschattengewächse)",
        )
    ).choices()

    plant = models.OneToOneField(to=Plant, on_delete=models.CASCADE, related_name="living", verbose_name=_("Pflanze"))
    bot_name = models.CharField(max_length=100, verbose_name=_("Botanischer Name"), help_text= _("Gattung und Art, ggf. Unterart/ Variation, ggf. Sorte"))
    de_name = models.CharField(max_length=100, verbose_name=_("Deutscher Name"))
    relevant_cultivar = models.TextField(max_length=500, null=True, blank=True, verbose_name=_("Relevante Sorten"), help_text=_("Name der Sorte' - prägnantes Merkmal"))
    synonyms = models.CharField(max_length=100, null=True, blank=True, verbose_name=_("Synonyme"), help_text=_("Gattung und Art, ggf. Unterart/ Variation, Sorte"))
    family = models.CharField(
        max_length=36,
        choices=FAMILY_CHOICES,
        verbose_name=_("Familie - botanischer Name (deutscher Name)")
    )
    de_domestic = models.CharField(max_length=4, choices=YES_NO_CHOICES, verbose_name=_("In Deutschland heimisch"))
    de_hardy = models.CharField(
        max_length=4,
        choices=YES_NO_CHOICES,
        null=True,
        blank=True,
        verbose_name=_("In Deutschland winterhart"),
        help_text=_("Bitte nur ausfüllen, wenn heimisch = nein")
    )
    living = models.OneToOneField(to=Living, on_delete=models.CASCADE, related_name="living", verbose_name=_("Lebensweise"))


    class Meta:
        verbose_name = _("Taxonomie und Lebensweise")
        verbose_name_plural = _("Taxonomien und Lebensweisen")
