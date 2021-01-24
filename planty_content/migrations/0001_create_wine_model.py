# Generated by Django 3.0.11 on 2021-01-24 12:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('content', '0001_create_tree_node_model'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Sorte')),
                ('ger_name', models.CharField(max_length=200, verbose_name='Sorte')),
                ('synonyms', models.CharField(blank=True, max_length=200, null=True, verbose_name='Synonyme')),
                ('blossom', models.CharField(choices=[('männlich', 'männlich'), ('weiblich', 'weiblich'), ('zwittrig', 'zwittrig')], default='', max_length=8, verbose_name='Blüte')),
                ('cross_parents', models.CharField(max_length=200, verbose_name='Kreuzungseltern')),
                ('origin', models.CharField(help_text='Falss nicht bekannt "unbekannt" als Eingabe', max_length=200, verbose_name='Herkunft')),
                ('notes', models.TextField(blank=True, max_length=400, null=True, verbose_name='Anmerkungen')),
                ('systematics', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='profiles', to='content.TreeNode', verbose_name='Steckbrief-Ebene')),
            ],
            options={
                'verbose_name': 'Rebe',
                'verbose_name_plural': 'Reben',
            },
        ),
    ]
