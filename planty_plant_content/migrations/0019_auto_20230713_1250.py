# Generated by Django 3.2.16 on 2023-07-13 10:50

from django.db import migrations, models
import planty_plant_content.models


class Migration(migrations.Migration):

    dependencies = [
        ('planty_plant_content', '0018_auto_20230713_1239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='living',
            name='life_span',
            field=models.CharField(blank=True, choices=[('1', 'ausdauernd, sehr kurz überdauernd ( < 50 J)'), ('2', 'ausdauernd, kurz überdauernd(50 - 100J)'), ('3', 'ausdauernd, mäßig dauerhaft(100 - 300J)'), ('4', 'ausdauernd, dauerhaft(300 - 500J)'), ('5', 'ausdauernd, sehr dauerhaft(ü 500J)')], max_length=44, null=True, verbose_name='Lebensdauer'),
        ),
        migrations.AlterField(
            model_name='toxicity',
            name='toxicity',
            field=planty_plant_content.models.ChoiceArrayField(base_field=models.CharField(blank=True, choices=[('1', 'Blüte giftig'), ('2', 'Blüte leicht giftig'), ('3', 'Blüte stark giftig'), ('4', 'Frucht giftig'), ('5', 'Frucht leicht giftig'), ('6', 'Frucht stark giftig'), ('7', 'gesamte Pflanze leicht giftig'), ('8', 'gesamte Pflanze giftig'), ('9', 'gesamte Pflanze stark giftig'), ('10', 'Laub giftig'), ('11', 'Laub leicht giftig'), ('12', 'Laub stark giftig'), ('13', 'Rinde giftig'), ('14', 'Samen giftig'), ('15', 'Samen leicht giftig'), ('16', 'Samen stark giftig'), ('17', 'Wurzel giftig'), ('18', 'Wurzel leicht giftig'), ('19', 'Wurzel stark giftig'), ('20', 'kontaktgiftig'), ('21', 'phototoxisch'), ('22', 'ungiftig'), ('23', 'Nadeln giftig'), ('24', 'Nadeln leicht giftig'), ('25', 'Nadeln stark giftig')], max_length=2), blank=True, null=True, size=None, verbose_name='Giftigkeit'),
        ),
    ]
