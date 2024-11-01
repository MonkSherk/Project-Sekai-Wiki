# Generated by Django 4.2.16 on 2024-10-30 20:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sekai_app', '0004_alter_character_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='character',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cards', to='sekai_app.character'),
        ),
        migrations.AlterField(
            model_name='event',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='events', to='sekai_app.group'),
        ),
        migrations.AlterField(
            model_name='group',
            name='sekai',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='groups', to='sekai_app.sekaiworld'),
        ),
        migrations.AlterField(
            model_name='song',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='songs', to='sekai_app.group'),
        ),
    ]
