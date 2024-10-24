# Generated by Django 4.2.5 on 2024-10-22 12:50

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('animais', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='descricao',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='animal',
            name='detalhes_medicos',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('VACINADO', 'Vacinado'), ('VERMIFUGADO', 'Vermifugado'), ('CASTRADO', 'Castrado')], default=['Vacinado'], max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='animal',
            name='porte',
            field=models.CharField(choices=[('PEQUENO', 'Pequeno'), ('MÉDIO', 'Médio'), ('GRANDE', 'Grande')], default='Desconhecido', max_length=10),
        ),
        migrations.AddField(
            model_name='animal',
            name='raca',
            field=models.CharField(default='SRD', max_length=20),
        ),
        migrations.AddField(
            model_name='animal',
            name='sexo',
            field=models.CharField(choices=[('Macho', 'Macho'), ('Fêmea', 'Fêmea')], default='Desconhecido', max_length=10),
        ),
    ]