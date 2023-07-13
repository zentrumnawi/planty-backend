# Generated by Django 3.2.16 on 2023-07-13 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planty_plant_content', '0017_auto_20230706_1800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bark',
            name='surface',
            field=models.TextField(blank=True, help_text='Jung- und Altzustand', max_length=500, null=True, verbose_name='Oberfläche/Struktur'),
        ),
        migrations.AlterField(
            model_name='blossom',
            name='odor',
            field=models.TextField(blank=True, help_text='Intensität, Aroma', max_length=500, null=True, verbose_name='Geruch'),
        ),
        migrations.AlterField(
            model_name='blossom',
            name='stand',
            field=models.TextField(blank=True, help_text='Formulierungen entspr. Schmeil-Fitschen', max_length=500, null=True, verbose_name='Blütenstand'),
        ),
        migrations.AlterField(
            model_name='diseases',
            name='diseases',
            field=models.TextField(blank=True, max_length=500, null=True, verbose_name='Krankheiten/Schädlinge'),
        ),
        migrations.AlterField(
            model_name='fruit',
            name='form',
            field=models.TextField(blank=True, max_length=500, null=True, verbose_name='Form'),
        ),
        migrations.AlterField(
            model_name='habitus',
            name='grow_form',
            field=models.TextField(max_length=500, verbose_name='Wuchsform'),
        ),
        migrations.AlterField(
            model_name='leaf',
            name='color',
            field=models.TextField(blank=True, max_length=500, null=True, verbose_name='Farbe'),
        ),
        migrations.AlterField(
            model_name='leaf',
            name='form',
            field=models.TextField(help_text='Formulierungen entspr. Schmeil-Fitschen', max_length=500, verbose_name='Form'),
        ),
        migrations.AlterField(
            model_name='root',
            name='type',
            field=models.TextField(blank=True, max_length=500, null=True, verbose_name='Typ'),
        ),
        migrations.AlterField(
            model_name='sprout',
            name='branch_form',
            field=models.TextField(blank=True, max_length=500, null=True, verbose_name='Form Äste/ Triebe/ Verzweigung'),
        ),
    ]
