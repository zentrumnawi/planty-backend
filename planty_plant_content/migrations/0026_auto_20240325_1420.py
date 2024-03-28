# Generated by Django 3.2.16 on 2024-03-25 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planty_plant_content', '0025_auto_20230713_1615'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='generalinformation',
            options={'verbose_name': 'Allgemein', 'verbose_name_plural': 'Allgemein'},
        ),
        migrations.AlterField(
            model_name='blossom',
            name='age_at_frist_bloom',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Alter bei erster Blüte'),
        ),
        migrations.AlterField(
            model_name='blossom',
            name='color',
            field=models.CharField(blank=True, help_text='Grundfarbe und besondere Farbnuancen', max_length=250, null=True, verbose_name='Farbe'),
        ),
        migrations.AlterField(
            model_name='blossom',
            name='form_single_blossom',
            field=models.CharField(blank=True, help_text='Formulierungen entspr. Schmeil-Fitschen', max_length=250, null=True, verbose_name='Form der Einzelblüte'),
        ),
        migrations.AlterField(
            model_name='leaf',
            name='budding_time',
            field=models.CharField(blank=True, help_text='Wenn Besonderheit im Zeitpunkt des Neuaustriebs', max_length=250, null=True, verbose_name='Zeitpunkt des Austriebs'),
        ),
        migrations.AlterField(
            model_name='leaf',
            name='edge_form',
            field=models.CharField(blank=True, help_text='Formulierungen entspr. Schmeil-Fitschen', max_length=250, null=True, verbose_name='Randform'),
        ),
        migrations.AlterField(
            model_name='leaf',
            name='position',
            field=models.CharField(help_text='Formulierungen entspr. Schmeil-Fitschen', max_length=250, verbose_name='Stellung'),
        ),
        migrations.AlterField(
            model_name='root',
            name='sensitivity',
            field=models.CharField(blank=True, help_text='Empfindlichkeiten/Fähigkeiten', max_length=250, null=True, verbose_name='Empfindlichkeit'),
        ),
        migrations.AlterField(
            model_name='sprout',
            name='leaf_scar',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Blattnarbe'),
        ),
    ]
