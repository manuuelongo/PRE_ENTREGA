# Generated by Django 4.2.7 on 2023-11-27 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_opinion_opinion_alter_comentario_comentario'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='console',
            field=models.CharField(choices=[('Xbox', 'Xbox'), ('PC', 'PC'), ('Nintendo Switch', 'Nintendo Switch'), ('PS5', 'PS5'), ('Sin Información', 'Sin Información')], default='Sin Información', max_length=20),
            preserve_default=False,
        ),
    ]
