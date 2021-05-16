YES_NO_CHOICES = (
    ("ja", "ja"),
    ("nein", "nein"),
)

BLOSSOM_CHOICES = (
    ("männlich", "männlich"),
    ("weiblich", "weiblich"),
    ("zwittrig", "zwittrig"),
)

TIP_HAIRY_CHOICES = (
    ("kahl", "kahl"),
    ("schwachwollig", "schwachwollig"),
    ("wollig", "wollig"),
    ("starkwollig", "starkwollig"),
    ("filzig", "filzig"),
)

TIP_TYPE_CHOICES = (
    ("offen", "offen"),
    ("halb offen bis offen", "halb offen bis offen"),
    ("halb offen", "halb offen"),
    ("geschlossen bis halboffen", "geschlossen bis halboffen"),
    ("geschlossen", "geschlossen"),
)

LAP_CHOICES = (
    (None, "---------"),
    ("ganzrandig", "ganzrandig"),
    ("3-", "3-"),
    ("3-lappig", "3-lappig"),
    ("5-", "5-"),
    ("5-lappig", "5-lappig"),
    ("7-lappig", "7-lappig"),
)


EDGE_FORM_CHOICES = (
    ("gesägt", "gesägt"),
    ("gezähnt", "gezähnt"),
    ("wechselnd gezähnt und gesägt", "wechselnd gezähnt und gesägt"),
)
STRUCTURE_CHOICES = (
    ("glatt", "glatt"),
    ("blasig", "blasig"),
    ("gewellt", "gewellt"),
)
FORM_SPREITE_CHOICES = (
    ("keilförmig", "keilförmig"),
    ("herzförmig", "herzförmig"),
    ("fünfeckig", "fünfeckig"),
    ("kreisförmig", "kreisförmig"),
    ("nierenförmig", "nierenförmig"),
)
SHAFT_FORM_CHOICES = (
    (None, "---------"),
    ("U-", "U-"),
    ("U-förmig", "U-förmig"),
    ("V-", "V-"),
    ("V-förmig", "V-förmig"),
    ("lyraförmig", "lyraförmig"),
)
SHAFT_OPEN_CHOICES = (
    ("offen", "offen"),
    ("geschlossen", "geschlossen"),
    ("überlappend", "überlappend"),
    ("weit überlappend", "weit überlappend"),
)

ANT_COLOR_CHOICES = (
    ("fehlend", "fehlend"),
    ("gering", "gering"),
    ("mittel", "mittel"),
    ("stark", "stark"),
)

DENSITY_CHOICES = (
    ("lockerbeerig", "lockerbeerig"),
    ("mitteldicht", "mitteldicht"),
    ("kompakt", "kompakt"),
)
SIZE_CHOICES = (
    ("sehr klein", "sehr klein"),
    ("klein", "klein"),
    ("mittel", "mittel"),
    ("groß", "groß"),
    ("sehr groß", "sehr groß"),
)
FORM_CHOICES = (
    ("zylindrisch", "zylindrisch"),
    ("konisch", "konisch"),
    ("kegelförmig", "kegelförmig"),
    ("walzenförmig", "walzenförmig"),
)
SHOULDERED_CHOICES = (("ja", "ja"), ("nein", "nein"), ("teilweise", "teilweise"))

BERRY_FORM_CHOICES = (
    ("flach", "flach"),
    ("etwas flach", "etwas flach"),
    ("rundlich", "rundlich"),
    ("kurzoval", "kurzoval"),
    ("eierförmig", "eierförmig"),
    ("eierförmig abgestumpft", "eierförmig abgestumpft"),
    ("verkehrt eierförmig", "verkehrt eierförmig"),
    ("länglich", "länglich"),
    ("langoval", "langoval"),
    ("gebogen", "gebogen"),
)
BERRY_SIZE_CHOICES = (
    ("sehr klein", "sehr klein"),
    ("klein", "klein"),
    ("mittel", "mittel"),
    ("groß", "groß"),
    ("sehr groß", "sehr groß"),
)
BERRY_SURFACE_CHOICES = (
    ("bepunktet", "bepunktet"),
    ("beduftet", "beduftet"),
)
BERRY_COLOR_CHOICES = (
    ("weiß", "weiß"),
    ("rot", "rot"),
    ("gelb", "gelb"),
    ("blau", "blau"),
    ("grüngelb", "grüngelb"),
    ("rosa", "rosa"),
    ("rot", "rot"),
    ("rot-grau", "rot-grau"),
    ("blauschwarz", "blauschwarz"),
    ("rotschwarz", "rotschwarz"),
    ("bernsteinfarben", "bernsteinfarben"),
)
BERRY_FLESH_COLOR_CHOICES = (
    ("ungefärbt", "ungefärbt"),
    ("gefärbt", "gefärbt"),
)
BERRY_ARMOA_CHOICES = (
    ("Muskatgeschmack", "Muskatgeschmack"),
    ("Foxgeschmack", "Foxgeschmack"),
    ("Spezielgeschmack", "Spezielgeschmack"),
)

FORK_CHOICES = (
    ("überwiegend zweigabelig", "überwiegend zweigabelig"),
    ("überwiegend dreigabelig", "überwiegend dreigabelig"),
)
SERIES_CHOICES = (
    ("kontinuierlich", "kontinuierlich"),
    ("diskontinuierlich", "diskontinuierlich"),
)

GOOD_BAD_CHOICES = (
    (None, "---------"),
    ("gering", "gering"),
    ("mittel", "mittel"),
    ("gut", "gut"),
    ("sehr gut", "sehr gut"),
)

WEAK_STRONG_CHOICES = (
    (None, "---------"),
    ("sehr schwach", "sehr schwach"),
    ("schwach", "schwach"),
    ("mittel", "mittel"),
    ("stark", "stark"),
    ("sehr stark", "sehr stark"),
)

EARLY_LATE_CHOICES = (
    (None, "---------"),
    ("sehr früh", "sehr früh"),
    ("früh", "früh"),
    ("mittel", "mittel"),
    ("spät", "spät"),
    ("sehr spät", "sehr spät"),
)

REBLAUS_CHOICES = (
    ("tolerant", "tolerant"),
    ("resistent", "resistent"),
    ("anfällig", "anfällig"),
)
