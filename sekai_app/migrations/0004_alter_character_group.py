# Generated by Django 4.2.16 on 2024-10-30 20:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sekai_app', '0003_alter_card_stats'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='characters', to='sekai_app.group'),
        ),
    ]
