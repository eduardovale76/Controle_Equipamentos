# Generated by Django 4.0.3 on 2022-03-24 00:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('equipamento', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='emprestimos',
            name='categoria',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='equipamento.categoria'),
            preserve_default=False,
        ),
    ]
