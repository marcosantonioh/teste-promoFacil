# Generated by Django 5.1.3 on 2024-12-07 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promocoes', '0007_alter_promocao_unique_together_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
    ]
