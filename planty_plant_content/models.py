from enum import Enum
import re

from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.forms import MultipleChoiceField
from django.utils.translation import ugettext_lazy as _
from solid_backend.content.fields import FromToConcatField
from solid_backend.content.models import SolidBaseProfile

from planty_content.choices import YES_NO_CHOICES


class ChoiceArrayField(ArrayField):
    """
    A field that allows us to store an array of choices.

    Uses Django 1.9's postgres ArrayField
    and a MultipleChoiceField for its formfield.
    """

    def formfield(self, **kwargs):
        defaults = {
            "form_class": MultipleChoiceField,
            "choices": self.base_field.choices,
        }
        defaults.update(kwargs)

        return super(ArrayField, self).formfield(**defaults)


class ChoiceEnum(Enum):
    @classmethod
    def choices(cls):
        return tuple((str(i.value), i.name) for i in cls)


class SortedChoiceEnum(Enum):
    """
    Class to use for Enums if people change the Enum which would destroy the original ordered tuple.

    Example:
        Begin with:
        ChoiceEnmu(['A TESTE', 'B TEST', 'C TEST'])
        --> (('1', 'A TESTE'),('2', 'B TEST'),('3', 'C TEST'))

        Changed to:
        ChoiceEnmu(['A TESTE', 'A 2. TEST', 'B TEST', 'C TEST'])
        (('1', 'A TESTE'), ('2', 'A 2. TEST'), ('3', 'B TEST'), ('4', 'C TEST'))

        This would cause a Miss assignment for all Entries that previously had 'B TEST' or 'C TEST' assigned.

    If a requested Changes to an Enum would lead to a messed Up order switch ChoiceEnum with SortedChoiceEnum and add
    new Entries at the end of the List.

    Example:

       ChoiceEnmu(['A TESTE', 'B TEST', 'C TEST'])
       becomes
       SortedChoiceEnmu(['A TESTE', 'B TEST', 'C TEST', 'A 2. TEST'])
    """

    @classmethod
    def choices(cls):
        sorted_list = [(str(i.value), i.name) for i in cls]
        sorted_list.sort(key=lambda tpl: tpl[1])
        return tuple(sorted_list)


class Plant(SolidBaseProfile):

    searchable_fields = [
        "general_information__name",
        "general_information__sub_name",
    ]

    @classmethod
    def get_optimized_queryset(cls):
        return cls.objects.select_related(
            "tree_node",
            "general_information",
            "taxonomy",
            "usability",
            "disease",
            "reproduction_and_production",
            "appearance",
            "application",
            "plantation_and_creation",
            "ecology_and_natlocation",
            # Nested select_related for appearance
            "appearance__habitus",
            "appearance__sprout",
            "appearance__leaf",
            "appearance__blossom",
            "appearance__fruit",
            "appearance__bark",
            "appearance__root",
            # Nested select_related for application
            "application__habitat",
            "application__habitat_factors",
            "application__appl_function",
            # Nested select_related for usability
            "usability__toxicity",
            "usability__fauna_usability",
            "usability__human_usability",
            # Nested select_related for taxonomy
            "taxonomy__living",
            # Nested select_related for ecology_and_natlocation
            "ecology_and_natlocation__nat_occ",
            "ecology_and_natlocation__nat_behavior",
            "ecology_and_natlocation__nat_behavior__zeiger_value",
        ).prefetch_related(
            "media_objects",
        )

    class Meta:
        verbose_name = _("Pflanze")
        verbose_name_plural = _("Pflanzen")
        ordering = ("general_information__name",)


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
            "Vollparasit",
        ),
    ).choices()

    LIFESPAN_CHOICES = ChoiceEnum(
        "LifespanChoices",
        (
            "ausdauernd, sehr kurz überdauernd ( < 50 J)",
            "ausdauernd, kurz überdauernd(50 - 100J)",
            "ausdauernd, mäßig dauerhaft(100 - 300J)",
            "ausdauernd, dauerhaft(300 - 500J)",
            "ausdauernd, sehr dauerhaft(ü 500J)",
        ),
    ).choices()

    living_accord = models.CharField(
        max_length=22,
        choices=LIVING_CHOICES,
        null=True,
        blank=True,
        verbose_name=_("Lebensform nach Raukiær (1919)"),
        help_text=_("Klare Zuweisung einer Kategorie, erweiterbar:"),
    )
    spec_living = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name=_("Besonderes zur Lebensweise"),
    )
    life_span = models.CharField(
        max_length=44,
        null=True,
        blank=True,
        choices=LIFESPAN_CHOICES,
        verbose_name=_("Lebensdauer"),
    )
    extra = models.TextField(
        max_length=500,
        null=True,
        blank=True,
        verbose_name=_("Weiteres zur Lebensdauer"),
        help_text=_("Nur solitär stehend so alt werdend; unter Konkurrenz kurzlebiger"),
    )

    class Meta:
        verbose_name = _("Lebensweise")
        verbose_name_plural = _("Lebensweisen")

    def __str__(self):
        try:
            object_cleared = re.sub("object ", "", super(Living, self).__str__())
            return re.sub(
                r"\d+", self.taxonomy.plant.general_information.name, object_cleared
            )
        except:
            return super(Living, self).__str__()


class Taxonomy(models.Model):
    FAMILY_CHOICES = SortedChoiceEnum(
        "FamilyChoices",
        (
            "Acanthaceae (Akanthusgewächse)",
            "Adoxaceae (Moschuskrautgewächse)",
            "Amaryllidaceae (Narzissengewächse)",
            "Anacardiaceae (Sumachgewächse)",
            "Anthericaceae (Grasliliengewächse)",
            "Apiaceae (Doldenblütler)",
            "Aquifoliaceae (Stechpalmengewächse)",
            "Araliaceae (Efeugewächse)",
            "Aristolochiaceae (Osterluzeigewächse)",
            "Asparagaceae (Spargelgewächse)",
            "Asphodelaceae (Affodillgewächse)",
            "Asteraceae (Korbblütler)",
            "Berberidaceae (Berberitzengewächse)",
            "Betulaceae (Birkengewächse)",
            "Bignoniaceae (Trompetenbaumgewächse)",
            "Boraginaceae (Raublattgewächse)",
            "Brassicaceae (Kreuzblütengewächse)",
            "Buddlejaceae (Schmetterlingsfliedergewächse)",
            "Buxaceae (Buchsbaumgewächse)",
            "Campanulaceae (Glockenblumengewächse)",
            "Caprifoliaceae (Geißblattgewächse)",
            "Caryophyllaceae (Nelkengewächse)",
            "Celastraceae (Spindelbaumgewächse)",
            "Cercidiphyllaceae (Kuchenbaumgewächse)",
            "Cistaceae (Zistrosengewächse)",
            "Clusiaceae (Johanniskrautgewächse)",
            "Cornaceae (Hartriegelgewächse)",
            "Crassulaceae (Dickblattgewächse)",
            "Cupressaceae (Zypressengewächse)",
            "Dipsacaceae (Kardengewächse)",
            "Ebenaceae (Ebenholzgewächse)",
            "Elaeagnaceae (Ölweidengewächse)",
            "Ericaceae (Heidekrautgewächse)",
            "Euphorbiaceae (Wolfsmilchgewächse)",
            "Fabaceae (Hülsenfrüchtler)",
            "Fagaceae (Buchengewächse)",
            "Gentianaceae (Enziangewächse)",
            "Geraniaceae (Storchschnabelgewächse)",
            "Ginkgoaceae (Ginkgogewächse)",
            "Hamamelidaceae (Zaubernussgewächse)",
            "Hemerocallidaceae (Tagliliengewächse)",
            "Hydrangeaceae (Hortensiengewächse)",
            "Iridaceae (Schwertliliengewächse)",
            "Juglandaceae (Walnussgewächse)",
            "Lamiaceae (Lippenblütler)",
            "Liliaceae (Liliengewächse)",
            "Lythraceae (Weiderichgewächse)",
            "Magnoliaceae (Magnoliengewächse)",
            "Malvaceae (Malvengewächse)",
            "Moraceae (Maulbeergewächse)",
            "Nymphaeaceae (Seerosengewächse)",
            "Nyssaceae (Tupelogewächse)",
            "Oleaceae (Ölbaumgewächse)",
            "Onagraceae (Nachtkerzengewächse)",
            "Orchidaceae (Orchideengewächse)",
            "Paeoniaceae (Pfingstrosengewächse)",
            "Papaveraceae (Mohngewächse)",
            "Pinaceae (Kieferngewächse)",
            "Plantaginaceae (Wegerichgewächse)",
            "Platanaceae (Platanengewächse)",
            "Poaceae (Süßgräser)",
            "Polemoniaceae (Himmelsleitergewächse)",
            "Polygonaceae (Knöterichgewächse)",
            "Primulaceae (Primelgewächse)",
            "Ranunculaceae (Hahnenfußgewächse)",
            "Rhamnaceae (Kreuzdorngewächse)",
            "Rosaceae (Rosengewächse)",
            "Rubiaceae (Krappgewächse)",
            "Rutaceae (Rautengewächse)",
            "Salicaceae (Weidengewächse)",
            "Sapindaceae (Seifenbaumgewächse)",
            "Sapotaceae (Sapotengewächse)",
            "Saxifragaceae (Steinbrechgewächse)",
            "Scrophulariaceae (Braunwurzgewächse)",
            "Simaroubaceae (Bittereschengewächse)",
            "Solanaceae (Nachtschattengewächse)",
            "Styracaceae (Storaxbaumgewächse)",
            "Taxaceae (Eibengewächse)",
            "Taxodiaceae (Sumpfzypressengewächse)",
            "Thymelaeaceae (Seidelbastgewächse)",
            "Ulmaceae (Ulmengewächse)",
            "Valerianaceae (Baldriangewächse)",
            "Verbenaceae (Eisenkrautgewächse)",
            "Violaceae (Veilchengewächse)",
            "Vitaceae (Rebengewächse)",
        ),
    ).choices()

    plant = models.OneToOneField(
        to=Plant,
        on_delete=models.CASCADE,
        related_name="taxonomy",
        verbose_name=_("Pflanze"),
    )
    relevant_cultivar = models.TextField(
        max_length=500,
        null=True,
        blank=True,
        verbose_name=_("Relevante Sorten"),
        help_text=_("Name der Sorte' - prägnantes Merkmal"),
    )
    synonyms = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name=_("Synonyme"),
        help_text=_("Gattung und Art, ggf. Unterart/ Variation, Sorte"),
    )
    family = models.CharField(
        max_length=36,
        choices=FAMILY_CHOICES,
        verbose_name=_("Familie - botanischer Name (deutscher Name)"),
    )
    de_domestic = models.CharField(
        max_length=4, choices=YES_NO_CHOICES, verbose_name=_("In Deutschland heimisch")
    )
    de_hardy = models.CharField(
        max_length=4,
        choices=YES_NO_CHOICES,
        null=True,
        blank=True,
        verbose_name=_("In Deutschland winterhart"),
        help_text=_("Bitte nur ausfüllen, wenn heimisch = nein"),
    )
    living = models.OneToOneField(
        to=Living,
        on_delete=models.CASCADE,
        related_name="taxonomy",
        verbose_name=_("Lebensweise"),
    )

    class Meta:
        verbose_name = _("Taxonomie und Lebensweise")
        verbose_name_plural = _("Taxonomien und Lebensweisen")

    def __str__(self):
        object_cleared = re.sub("object ", "", super(Taxonomy, self).__str__())
        return re.sub(r"\d+", self.plant.general_information.name, object_cleared)


class NatOccurence(models.Model):
    ENDANGERMENT_CHOICES = ChoiceEnum(
        "EndangermentChoices",
        (
            "0: ausgestorben oder verschollen",
            "1: vom Aussterben bedroht",
            "2: stark gefährdet",
            "3: gefährdet",
            "4: potentiell gefährdet (nur bei Roten Listen der Länder; soll künftig durch R ersetzt werden)",
            "V: Vorwarnliste, Bestände zurückgehend",
            "R: extrem selten (entspricht 4 bei den Roten Listen der Länder; s.o.)",
            "G: Gefährdung anzunehmen",
            "D: Daten mangelhaft",
            "*: ungefährdet",
        ),
    ).choices()

    origin = models.TextField(max_length=500, verbose_name=_("Herkunft | Vorkommen"))
    occurrence = models.TextField(
        max_length=500,
        null=True,
        blank=True,
        verbose_name=_("Vorkommen in Pflanzengesellschaften"),
        help_text=_("Vegetationsökologische Systeme"),
    )
    endangerment = models.CharField(
        max_length=2,
        choices=ENDANGERMENT_CHOICES,
        null=True,
        blank=True,
        verbose_name=_("Gefährdung "),
        help_text=_("Gefährdung nach Rote Liste"),
    )
    de_protected = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name=_("Geschützt in Deutschland"),
        help_text=_(
            "Schutz durch verschiedene Gesetze, Schutz kann in Bundesländern variieren (https://www.wisia.de/prod/index.html)"
        ),
    )
    de_he_protected = models.TextField(
        max_length=500,
        null=True,
        blank=True,
        verbose_name=_("Gefährdung/Geschützt in Hessen"),
    )
    neobiota = models.TextField(
        max_length=500,
        null=True,
        blank=True,
        verbose_name=_("Neobiota | Invasivitätsbewertung"),
    )

    class Meta:
        verbose_name = _("Ökologie und Naturstandort")
        verbose_name_plural = _("Ökologien und Naturstandorte")

    def __str__(self):
        try:
            object_cleared = re.sub("object ", "", super(NatOccurence, self).__str__())
            return re.sub(
                r"\d+",
                self.eco_and_natlocation.plant.general_information.name,
                object_cleared,
            )
        except:
            return super(NatOccurence, self).__str__()


class ZeigerValues(models.Model):
    ZEIGER_CHOICES = ChoiceEnum(
        "ZeigerChoices",
        (
            "0",
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "10",
            "11",
            "12",
            "x",
            "?",
            "~",
            "=",
        ),
    ).choices()
    DISSEMINATION_CHOCIES = ChoiceEnum(
        "DisseminationChoices",
        (
            "Selbstausbreitung (Autochorie)",
            "Windausbreitung (Anemochorie)",
            "Wasserausbreitung (Hydrochorie)",
            "Klettausbreitung (Epizoochorie)",
            "Verdauungsausbreitung (Endozoochorie)",
            "Ameisenausbreitung (Myrmeochorie)",
            "unspezifische Verschleppung durch Tiere (Zoochorie)",
            "Menschenausbreitung (Anthropochorie)",
        ),
    )

    light_value = models.CharField(
        max_length=2,
        choices=ZEIGER_CHOICES,
        null=True,
        blank=True,
        verbose_name=_("Licht"),
    )
    temp_value = models.CharField(
        max_length=2,
        choices=ZEIGER_CHOICES,
        null=True,
        blank=True,
        verbose_name=_("Temperatur"),
    )
    continent_value = models.CharField(
        max_length=2,
        choices=ZEIGER_CHOICES,
        null=True,
        blank=True,
        verbose_name=_("Kontinentalität"),
    )
    humidity_value = models.CharField(
        max_length=2,
        choices=ZEIGER_CHOICES,
        null=True,
        blank=True,
        verbose_name=_("Feuchte"),
    )
    reaction_value = models.CharField(
        max_length=2,
        choices=ZEIGER_CHOICES,
        null=True,
        blank=True,
        verbose_name=_("Reaktion"),
    )
    nitrogen_value = models.CharField(
        max_length=2,
        choices=ZEIGER_CHOICES,
        null=True,
        blank=True,
        verbose_name=_("Stickstoff"),
    )
    salt_value = models.CharField(
        max_length=2,
        choices=ZEIGER_CHOICES,
        null=True,
        blank=True,
        verbose_name=_("Salz"),
    )
    metal_value = models.CharField(
        max_length=2,
        choices=(("b", "b"), ("B", "B")),
        null=True,
        blank=True,
        verbose_name=_("Schwermetallresistenz"),
    )
    dominance = models.CharField(
        max_length=2,
        choices=ZEIGER_CHOICES,
        null=True,
        blank=True,
        verbose_name=_("Dominanz nach Ellenberg"),
    )
    dissemination = ChoiceArrayField(
        models.CharField(
            choices=DISSEMINATION_CHOCIES.choices(), max_length=2, blank=True
        ),
        null=True,
        blank=True,
        verbose_name=_("Verbreitungsstrategie (großräumig)"),
    )
    extraord_ability = models.TextField(
        max_length=500,
        null=True,
        blank=True,
        verbose_name=_("Besondere Fähigkeiten am Naturstandort"),
    )

    class Meta:
        verbose_name = _("Zeigerwerte nach Ellenberg")
        verbose_name_plural = _("Zeigerwerte nach Ellenberg")

    def __str__(self):
        try:
            object_cleared = re.sub("object ", "", super(ZeigerValues, self).__str__())
            return re.sub(
                r"\d+",
                self.nat_behavior.eco_and_natlocation.plant.general_information.name,
                object_cleared,
            )
        except:
            return super(ZeigerValues, self).__str__()


class NatBehavior(models.Model):
    STRATEGY_TYPE_CHOICES = ChoiceEnum(
        "StrategyTypeChoices", ("C", "S", "R", "CR", "SR", "CS", "CSR")
    ).choices()

    strategy_type = models.CharField(
        max_length=2,
        choices=STRATEGY_TYPE_CHOICES,
        null=True,
        blank=True,
        verbose_name=_("Strategietypen nach Grime"),
        help_text=_("Gefährdung nach Rote Liste"),
    )
    zeiger_value = models.OneToOneField(
        to=ZeigerValues,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="nat_behavior",
        verbose_name=_("Zeigerwerte nach Ellenberg"),
    )

    class Meta:
        verbose_name = _("Natürliche Verhaltensweisen und Fähigkeiten am Standort")
        verbose_name_plural = _(
            "Natürliche Verhaltensweisen und Fähigkeiten am Standort"
        )

    def __str__(self):
        try:
            object_cleared = re.sub("object ", "", super(NatBehavior, self).__str__())
            return re.sub(
                r"\d+",
                self.eco_and_natlocation.plant.general_information.name,
                object_cleared,
            )
        except:
            return super(NatBehavior, self).__str__()


class EcologyAndNatLocation(models.Model):
    plant = models.OneToOneField(
        to=Plant,
        on_delete=models.CASCADE,
        related_name="ecology_and_natlocation",
        verbose_name=_("Pflanze"),
    )
    nat_occ = models.OneToOneField(
        to=NatOccurence,
        on_delete=models.CASCADE,
        related_name="eco_and_natlocation",
        verbose_name=_("Natürliches Vorkommen"),
    )
    nat_behavior = models.OneToOneField(
        to=NatBehavior,
        on_delete=models.CASCADE,
        related_name="eco_and_natlocation",
        verbose_name=_("Natürliche Verhaltensweisen und Fähigkeiten am Standort"),
    )

    class Meta:
        verbose_name = _("Ökologie und Naturstandort")
        verbose_name_plural = _("Ökologie und Naturstandort")

    def __str__(self):
        object_cleared = re.sub(
            "object ", "", super(EcologyAndNatLocation, self).__str__()
        )
        return re.sub(r"\d+", self.plant.general_information.name, object_cleared)


class Habitus(models.Model):
    height = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name=_("Wuchshöhe"),
        help_text=_("in m, Engabe der Einheut"),
    )
    width = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name=_("Wuchsbreite"),
        help_text=_("in m, Engabe der Einheut"),
    )
    grow_style = models.CharField(
        max_length=100, null=True, blank=True, verbose_name=_("Wüchsigkeit")
    )
    dimension_extra = models.TextField(
        max_length=500,
        null=True,
        blank=True,
        verbose_name=_("Weiteres zur Dimension"),
        help_text=_("Veränderte Größen bei speziellen Bedingungen"),
    )
    grow_form = models.TextField(max_length=500, verbose_name=_("Wuchsform"))
    grow_extra = models.TextField(
        max_length=500, null=True, blank=True, verbose_name=_("Weiteres zum Wuchs")
    )
    similar_kinds = models.TextField(
        max_length=500,
        null=True,
        blank=True,
        verbose_name=_("Ähnliche Arten / Differenzialmerkmale"),
        help_text=_("('leicht zu verwechseln mit', Merkmal)"),
    )

    class Meta:
        verbose_name = _("Habitus")
        verbose_name_plural = _("Habita")

    def __str__(self):
        try:
            object_cleared = re.sub("object ", "", super(Habitus, self).__str__())
            return re.sub(
                r"\d+", self.appearance.plant.general_information.name, object_cleared
            )
        except:
            return super(Habitus, self).__str__()


class PlantSprout(models.Model):
    branch_form = models.TextField(
        max_length=500,
        null=True,
        blank=True,
        verbose_name=_("Form Äste/ Triebe/ Verzweigung"),
    )
    buds = models.TextField(
        max_length=500, verbose_name=_("Knospen"), help_text=_("Form und Farbe")
    )
    leaf_scar = models.CharField(
        max_length=250, null=True, blank=True, verbose_name=_("Blattnarbe")
    )
    odor = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name=_("Geruch"),
        help_text=_("Intensität, Aroma"),
    )
    extras = models.TextField(
        max_length=500, null=True, blank=True, verbose_name=_("Weitere Merkmale ")
    )

    class Meta:
        verbose_name = _("Trieb")
        verbose_name_plural = _("Triebe")

    def __str__(self):
        try:
            object_cleared = re.sub("object ", "", super(PlantSprout, self).__str__())
            return re.sub(
                r"\d+", self.appearance.plant.general_information.name, object_cleared
            )
        except:
            return super(PlantSprout, self).__str__()


class Leaf(models.Model):
    ENDURANCE_CHOICES = ChoiceEnum(
        "EnduranceChoices",
        (
            "immergrün",
            "überwinternd grün / wintergrün",
            "sommergrün",
            "vorsommergrün",
        ),
    ).choices()
    ANATOMY_CHOICES = ChoiceEnum(
        "AnatomyChoices",
        (
            "hydromorph",
            "blattsukkulent",
            "helomorph",
            "mesomorph",
            "skleromorph / xeromorph",
            "hygromorph",
        ),
    ).choices()
    BUDDING_CHOICES = ChoiceEnum(
        "BuddingChoices",
        (
            "Vorfrühling",
            "Beginn Erstfrühling",
            "Ende Erstfrühling",
            "Beginn Vollfrühling",
            "Ende Vollfrühling",
            "Beginn Frühsommer",
            "Ende Frühsommer",
            "Hochsommer",
            "Frühherbst",
            "Herbst",
            "Winter",
        ),
    ).choices()

    form = models.TextField(
        max_length=500,
        verbose_name=_("Form"),
        help_text=_("Formulierungen entspr. Schmeil-Fitschen"),
    )
    edge_form = models.CharField(
        max_length=250,
        null=True,
        blank=True,
        verbose_name=_("Randform"),
        help_text=_("Formulierungen entspr. Schmeil-Fitschen"),
    )
    size = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name=_("Größe"),
        help_text=_("in mm/cm, Eingabe der Einheit"),
    )
    color = models.TextField(
        max_length=500, null=True, blank=True, verbose_name=_("Farbe")
    )
    panasch = models.CharField(
        max_length=100, null=True, blank=True, verbose_name=_("Panschierung")
    )
    color_winter = models.CharField(
        max_length=100, null=True, blank=True, verbose_name=_("Farbe in Herbst/Winter")
    )
    position = models.CharField(
        max_length=250,
        verbose_name=_("Stellung"),
        help_text=_("Formulierungen entspr. Schmeil-Fitschen"),
    )
    nerves = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name=_("Nervatur"),
        help_text=_("Formulierungen entspr. Schmeil-Fitschen"),
    )
    endurance = ChoiceArrayField(
        models.CharField(choices=ENDURANCE_CHOICES, max_length=2, blank=True),
        null=True,
        blank=True,
        verbose_name=_("Ausdauer"),
    )
    anatomy = ChoiceArrayField(
        models.CharField(choices=ANATOMY_CHOICES, max_length=2, blank=True),
        null=True,
        blank=True,
        verbose_name=_("Anatomie"),
    )
    budding = models.CharField(
        max_length=2,
        choices=BUDDING_CHOICES,
        null=True,
        blank=True,
        verbose_name=_("Blattaustrieb (phänologisch)"),
    )
    budding_time = models.CharField(
        max_length=250,
        null=True,
        blank=True,
        verbose_name=_("Zeitpunkt des Austriebs"),
        help_text=_("Wenn Besonderheit im Zeitpunkt des Neuaustriebs"),
    )
    odor = models.TextField(
        max_length=500,
        null=True,
        blank=True,
        verbose_name=_("Geruch"),
        help_text=_("Intensität, Aroma"),
    )
    extras = models.TextField(
        max_length=500, null=True, blank=True, verbose_name=_("Weitere Merkmale ")
    )

    class Meta:
        verbose_name = _("Blatt")
        verbose_name_plural = _("Blätter")

    def __str__(self):
        try:
            object_cleared = re.sub("object ", "", super(Leaf, self).__str__())
            return re.sub(
                r"\d+", self.appearance.plant.general_information.name, object_cleared
            )
        except:
            return super(Leaf, self).__str__()


class Blossom(models.Model):
    POLLINATION_CHOICES = ChoiceEnum(
        "PollinationChoices",
        (
            "abiotische Bestäubung",
            "Fledermausbestäubung",
            "Geitonogamie",
            "Insektenbestäubung",
            "Kleistogamie",
            "Pseudokleistogamie",
            "Selbstbestäubung",
            "Schneckenbestäubung",
            "Vogelbestäubung",
            "Wasserbestäubung",
            "Windbestäubung",
            "Tierbestäubung",
        ),
    ).choices()

    MAIN_BLOOMING_CHOICES = (
        ("I", "I"),
        ("II", "II"),
        ("III", "III"),
        ("IV", "IV"),
        ("V", "V"),
        ("VI", "VI"),
        ("VII", "VII"),
        ("VIII", "VIII"),
        ("IX", "IX"),
        ("X", "X"),
        ("XI", "XI"),
        ("XII", "XII"),
    )

    stand = models.TextField(
        max_length=500,
        null=True,
        blank=True,
        verbose_name=_("Blütenstand"),
        help_text=_("Formulierungen entspr. Schmeil-Fitschen"),
    )
    form_single_blossom = models.CharField(
        max_length=250,
        null=True,
        blank=True,
        verbose_name=_("Form der Einzelblüte"),
        help_text=_("Formulierungen entspr. Schmeil-Fitschen"),
    )
    size = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name=_("Größe"),
        help_text=(
            "Einzelblüte/Blütenbestandteile/Blütenstand in mm bis cm, Eingabe der Einheit"
        ),
    )
    color = models.CharField(
        max_length=250,
        null=True,
        blank=True,
        verbose_name=_("Farbe"),
        help_text=_("Grundfarbe und besondere Farbnuancen"),
    )
    sexus = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name=_("Geschlechtlichkeit"),
    )
    housing = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name=_("Häusigkeit"),
    )
    pollination = ChoiceArrayField(
        models.CharField(
            max_length=2,
            choices=POLLINATION_CHOICES,
            blank=True,
        ),
        null=True,
        blank=True,
        verbose_name=_("Bestäubungsfaktoren "),
        help_text=_("für generative Vermehrung"),
    )
    extras = models.TextField(
        max_length=500, null=True, blank=True, verbose_name=_("Weitere Merkmale ")
    )
    main_blooming_period = FromToConcatField(
        max_length=100,
        default="",
        blank=True,
        from_choices=MAIN_BLOOMING_CHOICES,
        to_choices=MAIN_BLOOMING_CHOICES,
        verbose_name=_("Hauptblütezeit"),
    )
    after_blooming_period = models.CharField(
        max_length=100, null=True, blank=True, verbose_name=_("Nachblüte, Nebenblüte")
    )
    phenology_blooming_period = models.CharField(
        max_length=2,
        choices=Leaf.BUDDING_CHOICES,
        null=True,
        blank=True,
        verbose_name=_("Phänologische Blühphasen "),
    )
    age_at_frist_bloom = models.CharField(
        max_length=250, null=True, blank=True, verbose_name=_("Alter bei erster Blüte")
    )
    note_to_bloom = models.TextField(
        max_length=500, null=True, blank=True, verbose_name=_("Hinweise zur Blütezeit")
    )
    odor = models.TextField(
        max_length=500,
        null=True,
        blank=True,
        verbose_name=_("Geruch"),
        help_text=_("Intensität, Aroma"),
    )

    class Meta:
        verbose_name = _("Blüte")
        verbose_name_plural = _("Blüten")

    def __str__(self):
        try:
            object_cleared = re.sub("object ", "", super(Blossom, self).__str__())
            return re.sub(
                r"\d+", self.appearance.plant.general_information.name, object_cleared
            )
        except:
            return super(Blossom, self).__str__()


class Fruit(models.Model):
    form = models.TextField(
        max_length=500, null=True, blank=True, verbose_name=_("Form")
    )
    size = models.CharField(
        max_length=100, null=True, blank=True, verbose_name=_("Größe")
    )
    color = models.CharField(
        max_length=100, null=True, blank=True, verbose_name=_("Farbe")
    )
    ripeness = FromToConcatField(
        max_length=100,
        default="",
        blank=True,
        from_choices=Blossom.MAIN_BLOOMING_CHOICES,
        to_choices=Blossom.MAIN_BLOOMING_CHOICES,
        verbose_name=_("Reife"),
    )
    seed_intensity = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name=_("Intensität der Versamung "),
        help_text=_("generative Vermehrung"),
    )
    extras = models.TextField(
        max_length=500, null=True, blank=True, verbose_name=_("Weitere Merkmale ")
    )

    class Meta:
        verbose_name = _("Frucht")
        verbose_name_plural = _("Früchte")

    def __str__(self):
        try:
            object_cleared = re.sub("object ", "", super(Fruit, self).__str__())
            return re.sub(
                r"\d+", self.appearance.plant.general_information.name, object_cleared
            )
        except:
            return super(Fruit, self).__str__()


class Bark(models.Model):
    color = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name=_("Farbe"),
        help_text=_("Jung- und Altzustand"),
    )
    surface = models.TextField(
        max_length=500,
        null=True,
        blank=True,
        verbose_name=_("Oberfläche/Struktur"),
        help_text=_("Jung- und Altzustand"),
    )
    extras = models.TextField(
        max_length=500, null=True, blank=True, verbose_name=_("Weitere Merkmale")
    )

    class Meta:
        verbose_name = _("Rinde")
        verbose_name_plural = _("Rinden")

    def __str__(self):
        try:
            object_cleared = re.sub("object ", "", super(Bark, self).__str__())
            return re.sub(
                r"\d+", self.appearance.plant.general_information.name, object_cleared
            )
        except:
            return super(Bark, self).__str__()


class Root(models.Model):
    type = models.TextField(
        max_length=500, null=True, blank=True, verbose_name=_("Typ")
    )
    depth = models.CharField(
        max_length=100, null=True, blank=True, verbose_name=_("Tiefe, konkret")
    )
    spread = models.TextField(
        max_length=500,
        null=True,
        blank=True,
        verbose_name=_("Vegetative Ausbreitung und Speicherorgane"),
        help_text=_("Vegetative Ausbreitung und Speicherorgane"),
    )
    sensitivity = models.CharField(
        max_length=250,
        null=True,
        blank=True,
        verbose_name=_("Empfindlichkeit"),
        help_text=_("Empfindlichkeiten/Fähigkeiten"),
    )
    extras = models.TextField(
        max_length=500,
        null=True,
        blank=True,
        verbose_name=_("Weitere Merkmale"),
        help_text=_("Besonderes Verhalten"),
    )

    class Meta:
        verbose_name = _("Wurzel")
        verbose_name_plural = _("Wurzeln")

    def __str__(self):
        try:
            object_cleared = re.sub("object ", "", super(Root, self).__str__())
            return re.sub(
                r"\d+", self.appearance.plant.general_information.name, object_cleared
            )
        except:
            return super(Root, self).__str__()


class Appearance(models.Model):
    plant = models.OneToOneField(
        to=Plant,
        on_delete=models.CASCADE,
        related_name="appearance",
        verbose_name=_("Pflanze"),
    )

    habitus = models.OneToOneField(
        to=Habitus,
        on_delete=models.CASCADE,
        related_name="appearance",
        verbose_name=_("Habitus"),
    )
    sprout = models.OneToOneField(
        to=PlantSprout,
        on_delete=models.CASCADE,
        related_name="appearance",
        verbose_name=_("Trieb"),
    )
    leaf = models.OneToOneField(
        to=Leaf,
        on_delete=models.CASCADE,
        related_name="appearance",
        verbose_name=_("Blatt"),
    )
    blossom = models.OneToOneField(
        to=Blossom,
        on_delete=models.CASCADE,
        related_name="appearance",
        verbose_name=_("Blüte"),
    )
    fruit = models.OneToOneField(
        to=Fruit,
        on_delete=models.CASCADE,
        related_name="appearance",
        verbose_name=_("Frucht"),
    )
    bark = models.OneToOneField(
        to=Bark,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="appearance",
        verbose_name=_("Rinde"),
    )
    root = models.OneToOneField(
        to=Root,
        on_delete=models.CASCADE,
        related_name="appearance",
        verbose_name=_("Wurzel"),
    )

    class Meta:
        verbose_name = _("Habitus und Erscheinung")
        verbose_name_plural = _("Habitus und Erscheinungen")

    def __str__(self):
        object_cleared = re.sub("object ", "", super(Appearance, self).__str__())
        return re.sub(r"\d+", self.plant.general_information.name, object_cleared)


class Habitat(models.Model):
    area_of_life = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name=_("Lebensbereiche"),
        help_text=_(
            "Lebensbereich (ggf. Sekundärlebensbereiche) nach Kiermeier oder Hansen und Stahl (2006)"
        ),
    )
    extra_areas = models.TextField(
        max_length=500, null=True, blank=True, verbose_name=_("Weitere Standorte")
    )
    special_abilities = models.TextField(
        max_length=500,
        null=True,
        blank=True,
        verbose_name=_("Besondere Fähigkeiten am Standort"),
    )

    class Meta:
        verbose_name = _("Standorte")
        verbose_name_plural = _("Standorte")

    def __str__(self):
        try:
            object_cleared = re.sub("object ", "", super(Habitat, self).__str__())
            return re.sub(
                r"\d+", self.application.plant.general_information.name, object_cleared
            )
        except:
            return super(Habitat, self).__str__()


class HabitatFactors(models.Model):
    MICROCLIMATE_CHOICES = ChoiceEnum(
        "MicroClimateChoices",
        (
            "anspruchslos",
            "bevorzugt Kühle",
            "hitzeempfindlich",
            "exponierte Lage",
            "geschützte Lage",
            "windgeschützte Lage",
            "windexponierte Lage",
            "Laubmull",
            "empfindlich auf Laubmull",
            "luftfeuchte Lage",
            "lufttrockene Lage",
            "wärmeliebend",
            "hitzeverträglich",
            "trockenwarm",
        ),
    ).choices()

    HARDY_CHOICES = ChoiceEnum(
        "HardyChoices",
        (
            "Z1 unter -45,5",
            "Z2 -45, 5 bis -40, 1",
            "Z3 -40, 1 bis -34, 5",
            "Z4 -34, 5 bis -28, 9",
            "Z5 -28, 8 bis -23, 4",
            "Z6 -23, 4 bis -17, 8",
            "Z7 -17, 8 bis -12, 3",
            "Z8 -12, 3 bis -6, 7",
            "Z9 -6, 7 bis -1, 2",
            "Z10 -1, 2 bis +4, 4",
            "Z11 über +4, 4",
        ),
    ).choices()

    LIGHT_CHOICES = ChoiceEnum(
        "LightChoices",
        (
            "sonnig",
            "absonnig",
            "halbschattig",
            "schattig",
            "lichtschattig",
            "vollsonnig",
        ),
    ).choices()

    SOIL_CHOCIES = ChoiceEnum(
        "SoilChoices",
        (
            "sauer",
            "leicht sauer",
            "neutral",
            "leicht alkalisch",
            "alkalisch",
            "kalkreich",
            "basenreich",
            "kalkempfindlich",
            "kalkmeidend",
            "kalkfliehend",
        ),
    ).choices()

    NUTRIENTS_CHOICES = ChoiceEnum(
        "NutrientsChoices",
        (
            "mager",
            "geringe Nährstoffansprüche",
            "mittlere Nährstoffansprüche",
            "hohe Nährstoffansprüche",
            "regelmäßige Nährstoffeinträge",
            "nitrophytisch",
        ),
    ).choices()

    micro_climate = ChoiceArrayField(
        models.CharField(choices=MICROCLIMATE_CHOICES, max_length=2, blank=True),
        null=True,
        blank=True,
        verbose_name=_("Mikroklima"),
        help_text=_("Fähigkeiten, Ansprüche"),
    )
    room_climate = models.TextField(
        max_length=500,
        null=True,
        blank=True,
        verbose_name=_("Raumklimatische Faktoren "),
        help_text=_("Für Innenräume"),
    )
    frost_sensitivity = models.TextField(
        max_length=500,
        null=True,
        blank=True,
        verbose_name=_("Frostempfindlichkeit"),
    )
    hardy_zone = models.CharField(
        max_length=100,
        choices=HARDY_CHOICES,
        null=True,
        blank=True,
        verbose_name=_("Winterhärtezone"),
    )
    light = ChoiceArrayField(
        models.CharField(choices=LIGHT_CHOICES, max_length=2, blank=True),
        null=True,
        blank=True,
        verbose_name=_("Licht"),
    )
    extra_light = models.TextField(
        max_length=500,
        null=True,
        blank=True,
        verbose_name=_("Weitere Lichtfaktoren/ Besondere Fähigkeiten"),
    )
    soil_humidity = models.CharField(
        max_length=100, null=True, blank=True, verbose_name=_("Bodenfeuchte")
    )
    extra_humidity = models.TextField(
        max_length=500,
        null=True,
        blank=True,
        verbose_name=_("Weitere Feuchtefaktoren/ Besondere Fähigkeiten"),
        help_text=_("Beschreibung der Ansprüche an Feuchtigkeit"),
    )
    soil_reaction = ChoiceArrayField(
        models.CharField(choices=SOIL_CHOCIES, max_length=2, blank=True),
        null=True,
        blank=True,
        verbose_name=_("Bodenreaktion"),
    )
    nutrients = ChoiceArrayField(
        models.CharField(choices=NUTRIENTS_CHOICES, max_length=2, blank=True),
        null=True,
        blank=True,
        verbose_name=_("Nährstoffe"),
    )
    extra_nutrients = models.TextField(
        max_length=500,
        null=True,
        blank=True,
        verbose_name=_(
            "Weiteres zu Bodenreaktion und Nährstoffen/ Besondere Fähigkeiten "
        ),
    )
    soil = models.TextField(
        max_length=500, null=True, blank=True, verbose_name=_("Bodeneigenschaften")
    )
    extra_soil = models.TextField(
        max_length=500,
        null=True,
        blank=True,
        verbose_name=_("Weitere Bodenfaktoren/ Besondere Fähigkeiten "),
        help_text=_(
            "Bisher bekannte, geeignete Bodeneigenschaften aus Natur und Kultur"
        ),
    )

    class Meta:
        verbose_name = _("Standortfaktoren und Ansprüche")
        verbose_name_plural = _("Standortfaktoren und Ansprüche")

    def __str__(self):
        try:
            object_cleared = re.sub(
                "object ", "", super(HabitatFactors, self).__str__()
            )
            return re.sub(
                r"\d+", self.application.plant.general_information.name, object_cleared
            )
        except:
            return super(HabitatFactors, self).__str__()


class Function(models.Model):
    sightings = models.TextField(
        max_length=500, null=True, blank=True, verbose_name=_("Sichtungsergebnisse")
    )
    eco_net = models.TextField(
        max_length=500,
        null=True,
        blank=True,
        verbose_name=_("Eignung für die ökologische Vernetzung"),
    )
    roof_plant = models.TextField(
        max_length=500,
        null=True,
        blank=True,
        verbose_name=_("Eignung für Dach- und Kübelbepflanzung"),
    )
    breeding_prodcution = models.TextField(
        max_length=500,
        null=True,
        blank=True,
        verbose_name=_("Eignung für Zucht und Produktion"),
    )
    city_tree = models.TextField(
        max_length=500, null=True, blank=True, verbose_name=_("Eignung als Stadtbaum")
    )
    city_application = models.TextField(
        max_length=500,
        null=True,
        blank=True,
        verbose_name=_("Eignung für die Verwendung in Städten"),
        help_text=_("Thema Klimabaum, Forst"),
    )
    climate_suitability = models.TextField(
        max_length=500,
        null=True,
        blank=True,
        verbose_name=_("Einschätzung Klimawandeltauglichkeit"),
    )
    extra_notes = models.TextField(
        max_length=500,
        null=True,
        blank=True,
        verbose_name=_("Weitere Verwendungshinweise"),
    )
    extra_functions = models.TextField(
        max_length=500, null=True, blank=True, verbose_name=_("Weitere Funktionen")
    )

    class Meta:
        verbose_name = _("Funktion")
        verbose_name_plural = _("Funktionen")

    def __str__(self):
        try:
            object_cleared = re.sub("object ", "", super(Function, self).__str__())
            return re.sub(
                r"\d+", self.application.plant.general_information.name, object_cleared
            )
        except:
            return super(Function, self).__str__()


class Application(models.Model):
    plant = models.OneToOneField(
        to=Plant,
        on_delete=models.CASCADE,
        related_name="application",
        verbose_name=_("Pflanze"),
    )
    habitat = models.OneToOneField(
        to=Habitat,
        on_delete=models.CASCADE,
        related_name="application",
        verbose_name=_("Standort"),
    )
    habitat_factors = models.OneToOneField(
        to=HabitatFactors,
        on_delete=models.CASCADE,
        related_name="application",
        verbose_name=_("Standortfaktoren und Ansprüche"),
    )
    appl_function = models.OneToOneField(
        to=Function,
        on_delete=models.CASCADE,
        related_name="application",
        verbose_name=_("Funktion"),
    )

    class Meta:
        verbose_name = _("Verwendung")
        verbose_name_plural = _("Verwendungen")

    def __str__(self):
        object_cleared = re.sub("object ", "", super(Application, self).__str__())
        return re.sub(r"\d+", self.plant.general_information.name, object_cleared)


class PlantationAndCare(models.Model):
    ERUPTION_CHOICES = ChoiceEnum(
        "EruptionChoices",
        (
            "frostfrei",
            "kühl",
            "warm",
            "Kalthaus",
            "Warmhaus",
            "hell",
            "dunkel",
            "Freiland",
            "Winterschutz",
            "beheizter" "Winterschutz",
            "Nässeschutz",
        ),
    ).choices()

    plant = models.OneToOneField(
        to=Plant,
        on_delete=models.CASCADE,
        related_name="plantation_and_creation",
        verbose_name=_("Pflanze"),
    )
    plantation_time = models.TextField(
        max_length=500,
        null=True,
        blank=True,
        verbose_name=_("Empfohlener Pflanzzeitpunkt "),
    )
    eruption = models.CharField(
        max_length=4,
        choices=YES_NO_CHOICES,
        null=True,
        blank=True,
        verbose_name=_("Stockausschlagsfähigkeit"),
    )
    cutting = models.TextField(
        max_length=500,
        null=True,
        blank=True,
        verbose_name=_("Schnitt"),
        help_text=_("Verträglichkeit, Zeitpunkt"),
    )
    preservation = models.TextField(
        max_length=500, null=True, blank=True, verbose_name=_("Verjüngung/Erhaltung ")
    )
    fertilization = models.TextField(
        max_length=500,
        null=True,
        blank=True,
        verbose_name=_("Düngung/Wachstumsförderung "),
        help_text=_("in Verwendung"),
    )
    soil_treatment = models.TextField(
        max_length=500, null=True, blank=True, verbose_name=_("Bodenbearbeitung")
    )
    hibernation = ChoiceArrayField(
        models.CharField(choices=ERUPTION_CHOICES, max_length=2, blank=True),
        null=True,
        blank=True,
        verbose_name=_("Überwinterung"),
    )
    extra = models.TextField(
        max_length=500,
        null=True,
        blank=True,
        verbose_name=_("Weiteres zur Pflanzung und Pflege"),
    )

    class Meta:
        verbose_name = _("Pflanzung und Pflege")
        verbose_name_plural = _("Pflanzungen und Pflege")

    def __str__(self):
        object_cleared = re.sub("object ", "", super(PlantationAndCare, self).__str__())
        return re.sub(r"\d+", self.plant.general_information.name, object_cleared)


class ReproductionAndProduction(models.Model):
    REPRODUCTION_CHOICES = ChoiceEnum(
        "ReproductionChoices",
        ("Aussaat", "Stecklingsvermehrung", "Brutknöllchen", "Ableger", "Veredlung"),
    ).choices()
    SPROUT_BEHAVIOR_CHOICES = ChoiceEnum(
        "SproutBehaviorChoices",
        ("Kaltkeimer", "Warmkeimer", "Lichtkeimer", "Normalkeimer"),
    ).choices()

    plant = models.OneToOneField(
        to=Plant,
        on_delete=models.CASCADE,
        related_name="reproduction_and_production",
        verbose_name=_("Pflanze"),
    )
    reproduction_type = ChoiceArrayField(
        models.CharField(choices=REPRODUCTION_CHOICES, max_length=2, blank=True),
        null=True,
        blank=True,
        verbose_name=_("Art der Vermehrung"),
    )
    sprout_behavior = ChoiceArrayField(
        models.CharField(choices=SPROUT_BEHAVIOR_CHOICES, max_length=2, blank=True),
        null=True,
        blank=True,
        verbose_name=_("Keimverhalten"),
    )
    refinement = models.TextField(
        max_length=500, null=True, blank=True, verbose_name=_("Veredelungsfaktoren")
    )
    extra_reproducttion = models.TextField(
        max_length=500,
        null=True,
        blank=True,
        verbose_name=_("Weiteres zur Vermehrung "),
    )
    cultivation_req = models.TextField(
        max_length=500,
        null=True,
        blank=True,
        verbose_name=_("Anzuchtbedingungen "),
        help_text=_("Saattiefe, Keimtemperatur, Substrate, Wundverschluss, etc."),
    )
    culture_req = models.TextField(
        max_length=500,
        null=True,
        blank=True,
        verbose_name=_("Kulturbedingungen (Outdoor)"),
        help_text=_("nur bei dauerhafter Kultur, z.B. Baumschule"),
    )
    lighting_criteria = models.TextField(
        max_length=500, null=True, blank=True, verbose_name=_("Beleuchtungskriterien")
    )
    tempertaure_criteria = models.TextField(
        max_length=500, null=True, blank=True, verbose_name=_("Temperaturkriterien")
    )
    cilture_substrates = models.TextField(
        max_length=500, null=True, blank=True, verbose_name=_("Kultursubstrate")
    )
    fertilization = models.TextField(
        max_length=500,
        null=True,
        blank=True,
        verbose_name=_("Düngung/Wachstumsförderung "),
        help_text=_("in Kultur"),
    )
    extra_culture = models.TextField(
        max_length=500,
        null=True,
        blank=True,
        verbose_name=_("Weitere Kulturbedingungen (Indoor)"),
        help_text=_("nur bei dauerhafter Kultur, z.B. Gewächshaus"),
    )
    extra_production = models.TextField(
        max_length=500, null=True, blank=True, verbose_name=_("Weiteres zu Produktion")
    )

    class Meta:
        verbose_name = _("Vermehrung / Produktion")
        verbose_name_plural = _("Vermehrungen / Produktionen")

    def __str__(self):
        object_cleared = re.sub(
            "object ", "", super(ReproductionAndProduction, self).__str__()
        )
        return re.sub(r"\d+", self.plant.general_information.name, object_cleared)


class Toxicity(models.Model):
    TOXICITY_CHOICES = ChoiceEnum(
        "ToxicityChoices",
        (
            "Blüte giftig",
            "Blüte leicht giftig",
            "Blüte stark giftig",
            "Frucht giftig",
            "Frucht leicht giftig",
            "Frucht stark giftig",
            "gesamte Pflanze leicht giftig",
            "gesamte Pflanze giftig",
            "gesamte Pflanze stark giftig",
            "Laub giftig",
            "Laub leicht giftig",
            "Laub stark giftig",
            "Rinde giftig",
            "Samen giftig",
            "Samen leicht giftig",
            "Samen stark giftig",
            "Wurzel giftig",
            "Wurzel leicht giftig",
            "Wurzel stark giftig",
            "kontaktgiftig",
            "phototoxisch",
            "ungiftig",
            "Nadeln giftig",
            "Nadeln leicht giftig",
            "Nadeln stark giftig",
        ),
    ).choices()

    toxicity = ChoiceArrayField(
        models.CharField(choices=TOXICITY_CHOICES, max_length=2, blank=True),
        null=True,
        blank=True,
        verbose_name=_("Giftigkeit"),
    )
    extra_toxicity = models.TextField(
        max_length=500, null=True, blank=True, verbose_name=_("Hinweise zur Giftigkeit")
    )

    class Meta:
        verbose_name = _("Giftigkeit")
        verbose_name_plural = _("Giftigkeiten")

    def __str__(self):
        try:
            object_cleared = re.sub("object ", "", super(Toxicity, self).__str__())
            return re.sub(
                r"\d+", self.usability.plant.general_information.name, object_cleared
            )
        except:
            return super(Toxicity, self).__str__()


class FaunaUsability(models.Model):
    BEE_CHOICES = ChoiceEnum(
        "BeeChoices", ("Nektar", "Pollen", "Aufenthalt", "Nistmaterial")
    ).choices()

    MOTH_CHOICES = ChoiceEnum(
        "MothChoices",
        (
            "Raupenfutterpflanze(Schmetterling)",
            "Raupenfutterpflanze (Nachtfalter)",
            "Nektarpflanze(Schmetterling)",
            "Nektarpflanze(Nachtfalter)",
            "Nutzung von Schmetterlingen",
            "Nutzung von Nachtfaltern",
        ),
    ).choices()

    BIRD_CHOICES = ChoiceEnum(
        "BirdChoices", ("Futter", "Nistplatz", "Nistmaterial")
    ).choices()

    bee_plant = ChoiceArrayField(
        models.CharField(choices=BEE_CHOICES, max_length=2, blank=True),
        null=True,
        blank=True,
        verbose_name=_("Bienenpflanze"),
    )
    extra_bee = models.TextField(
        max_length=500,
        null=True,
        blank=True,
        verbose_name=_("Hinweise zur Bienenpflanze"),
    )
    moth_plant = ChoiceArrayField(
        models.CharField(choices=MOTH_CHOICES, max_length=2, blank=True),
        null=True,
        blank=True,
        verbose_name=_("Falterpflanze"),
    )
    extra_moth = models.TextField(
        max_length=500,
        null=True,
        blank=True,
        verbose_name=_("Hinweise zur Falterpflanze"),
    )
    bird_plant = ChoiceArrayField(
        models.CharField(choices=BIRD_CHOICES, max_length=2, blank=True),
        null=True,
        blank=True,
        verbose_name=_("Vogelnutzpflanze"),
    )
    extra_bird = models.TextField(
        max_length=500,
        null=True,
        blank=True,
        verbose_name=_("Hinweise zur Vogelnutzpflanze"),
    )
    extra_animal = models.TextField(
        max_length=500,
        null=True,
        blank=True,
        verbose_name=_("Weitere Nutzungen durch Tiere"),
    )

    class Meta:
        verbose_name = _("Nutzbarkeit Fauna")
        verbose_name_plural = _("Nutzbarkeiten Fauna")

    def __str__(self):
        try:
            object_cleared = re.sub(
                "object ", "", super(FaunaUsability, self).__str__()
            )
            return re.sub(
                r"\d+", self.usability.plant.general_information.name, object_cleared
            )
        except:
            return super(FaunaUsability, self).__str__()


class HumanUsability(models.Model):
    medical_use = models.TextField(
        max_length=500, null=True, blank=True, verbose_name=_("Medizinischer Nutzen")
    )
    edible = models.TextField(
        max_length=500,
        null=True,
        blank=True,
        verbose_name=_("Essbarkeit der Bestandteile"),
    )
    use_of_parts = models.TextField(
        max_length=500,
        null=True,
        blank=True,
        verbose_name=_("Nutzung und Verarbeitung der Bestandteile"),
    )
    wood_use = models.TextField(
        max_length=500, null=True, blank=True, verbose_name=_("Holznutzung")
    )
    wood_properties = models.TextField(
        max_length=500, null=True, blank=True, verbose_name=_("Holzeigenschaften ")
    )
    religious_meaning = models.TextField(
        max_length=500,
        null=True,
        blank=True,
        verbose_name=_("Etymologie und kulturelle Bedeutung"),
    )

    class Meta:
        verbose_name = _("Nutzbarkeit Mensch ")
        verbose_name_plural = _("Nutzbarkeiten Mensch ")

    def __str__(self):
        try:
            object_cleared = re.sub(
                "object ", "", super(HumanUsability, self).__str__()
            )
            return re.sub(
                r"\d+", self.usability.plant.general_information.name, object_cleared
            )
        except:
            return super(HumanUsability, self).__str__()


class Usability(models.Model):
    plant = models.OneToOneField(
        to=Plant,
        on_delete=models.CASCADE,
        related_name="usability",
        verbose_name=_("Pflanze"),
    )
    toxicity = models.OneToOneField(
        to=Toxicity,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="usability",
        verbose_name=_("Giftigkeit"),
    )
    fauna_usability = models.OneToOneField(
        to=FaunaUsability,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="usability",
        verbose_name=_("Nutzbarkeit Fauna"),
    )
    human_usability = models.OneToOneField(
        to=HumanUsability,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="usability",
        verbose_name=_("Nutzbarkeit Mensch "),
    )

    class Meta:
        verbose_name = _("Nutzbarkeit")
        verbose_name_plural = _("Nutzbarkeiten")

    def __str__(self):
        object_cleared = re.sub("object ", "", super(Usability, self).__str__())
        return re.sub(r"\d+", self.plant.general_information.name, object_cleared)


class Diseases(models.Model):
    plant = models.OneToOneField(
        to=Plant,
        on_delete=models.CASCADE,
        related_name="disease",
        verbose_name=_("Pflanze"),
    )
    diseases = models.TextField(
        max_length=500, null=True, blank=True, verbose_name=_("Krankheiten/Schädlinge")
    )
    physiology_damage = models.CharField(
        max_length=100, null=True, blank=True, verbose_name=_("Physiologische Schäden")
    )
    resistances = models.TextField(
        max_length=500,
        null=True,
        blank=True,
        verbose_name=_("Resistenzen/ Immunitäten/ Geringe Anfälligkeiten"),
    )
    culture_protection = models.TextField(
        max_length=500, null=True, blank=True, verbose_name=_("Kulturschutzmaßnahmen")
    )
    biological_protection = models.TextField(
        max_length=500,
        null=True,
        blank=True,
        verbose_name=_("Biologische Kulturschutzmaßnahmen"),
    )

    class Meta:
        verbose_name = _("Krankheiten / Schädlinge / Resistenzen")
        verbose_name_plural = _("Krankheiten / Schädlinge / Resistenzen")

    def __str__(self):
        object_cleared = re.sub("object ", "", super(Diseases, self).__str__())
        return re.sub(r"\d+", self.plant.general_information.name, object_cleared)


class GeneralInformation(models.Model):
    plant = models.OneToOneField(
        to=Plant,
        on_delete=models.CASCADE,
        related_name="general_information",
        verbose_name=_("Pflanze"),
    )
    info = models.TextField(
        max_length=500, null=True, blank=True, verbose_name=_("Informatives")
    )
    literature = models.TextField(
        max_length=500, null=True, blank=True, verbose_name=_("Literatur")
    )
    geo_data = models.TextField(
        max_length=500,
        null=True,
        blank=True,
        verbose_name=_("Verortung am Hochschulstandort"),
    )
    name = models.CharField(
        max_length=100,
        verbose_name=_("Botanischer Name"),
        help_text=_("Gattung und Art, ggf. Unterart/ Variation, ggf. Sorte"),
    )
    sub_name = models.CharField(
        max_length=100, blank=True, verbose_name=_("Deutscher Name")
    )

    class Meta:
        verbose_name = _("Allgemein")
        verbose_name_plural = _("Allgemein")

    def __str__(self):
        object_cleared = re.sub(
            "object ", "", super(GeneralInformation, self).__str__()
        )
        return re.sub(r"\d+", self.plant.general_information.name, object_cleared)
