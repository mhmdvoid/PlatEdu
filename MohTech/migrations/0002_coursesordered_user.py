# Generated by Django 3.0.5 on 2020-05-03 02:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MohTech', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursesordered',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='MohTech.Student'),
        ),
    ]