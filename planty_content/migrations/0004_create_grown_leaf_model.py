# Generated by Django 3.0.11 on 2021-01-24 13:49

from django.db import migrations, models
import django.db.models.deletion
import solid_backend.content.fields


class Migration(migrations.Migration):

    dependencies = [
        ('planty_content', '0003_create_young_leaf_model'),
    ]

    operations = [
        migrations.CreateModel(
            name='GrownLeaf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=200, verbose_name='Farbe')),
                ('lappung', solid_backend.content.fields.FromToConcatField(blank=True, default='', from_choices=(('ganzrandig', 'ganzrandig'), ('3-', '3-'), ('3-lappig', '3-lappig'), ('5-', '5-'), ('5-lappig', '5-lappig'), ('7-lappig', '7-lappig')), max_length=100, to_choices=(('ganzrandig', 'ganzrandig'), ('3-', '3-'), ('3-lappig', '3-lappig'), ('5-', '5-'), ('5-lappig', '5-lappig'), ('7-lappig', '7-lappig')), verbose_name='Lappung')),
                ('edge_form', models.CharField(choices=[('gesägt', 'gesägt'), ('gezähnt', 'gezähnt')], max_length=7, verbose_name='Randform')),
                ('structure', models.CharField(choices=[('glatt', 'glatt'), ('blasig', 'blasig'), ('gewellt', 'gewellt')], max_length=7, verbose_name='Struktur')),
                ('form_spreite', models.CharField(choices=[('keilförmig', 'keilförmig'), ('herzförmig', 'herzförmig'), ('fünfeckig', 'fünfeckig'), ('kreisförmig', 'kreisförmig'), ('nierenförmig', 'nierenförmig')], max_length=12, verbose_name='Form der Blattspreite')),
                ('shaft_form', solid_backend.content.fields.FromToConcatField(blank=True, default='', from_choices=(('U-', 'U-'), ('U-förmig', 'U-förmig'), ('V-', 'V-'), ('V-förmig', 'V-förmig'), ('lyraförmig', 'lyraförmig')), max_length=100, to_choices=(('U-', 'U-'), ('U-förmig', 'U-förmig'), ('V-', 'V-'), ('V-förmig', 'V-förmig'), ('lyraförmig', 'lyraförmig')), verbose_name='Stielbuchtform')),
                ('shaft_open', models.CharField(choices=[('offen', 'offen'), ('geschlossen', 'geschlossen'), ('überlappend', 'überlappend'), ('weit überlappend', 'weit überlappend')], max_length=16, verbose_name='Stielbuchtöffnungen')),
                ('shaft_notes', models.CharField(blank=True, max_length=200, null=True, verbose_name='Besonderheit der Stielbucht')),
                ('hairy_top', models.CharField(blank=True, max_length=200, null=True, verbose_name='Behaarung Oberseite')),
                ('hairy_bottom', models.CharField(blank=True, max_length=200, null=True, verbose_name='Behaarung Unterseite')),
                ('hairy_nerves', models.CharField(blank=True, max_length=200, null=True, verbose_name='Behaarung Nervenunterseite')),
                ('ant_color', models.CharField(choices=[('fehlend', 'fehlend'), ('gering', 'gering'), ('mittel', 'mittel'), ('stark', 'stark')], max_length=7, verbose_name='Anthocyanfärbung')),
                ('bristle_hairy', models.CharField(blank=True, max_length=200, null=True, verbose_name='Borstenbehaarung')),
                ('shaft', models.CharField(blank=True, max_length=200, null=True, verbose_name='Blattstiel')),
                ('notes', models.TextField(blank=True, max_length=400, null=True, verbose_name='Besonderheiten')),
                ('wine', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='grown_leaf', to='planty_content.Wine', verbose_name='Rebe')),
            ],
            options={
                'verbose_name': 'Ausgewachsenes Blatt',
                'verbose_name_plural': 'Ausgewachsene Blätter',
            },
        ),
    ]
