# Generated by Django 4.0.3 on 2022-03-24 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipamento', '0006_rename_nome_empresa_anonima_emprestimos_empresa_anonima'),
    ]

    operations = [
        migrations.AddField(
            model_name='empresa',
            name='email',
            field=models.EmailField(blank=True, max_length=60, null=True),
        ),
    ]
