# Generated by Django 5.0.4 on 2024-04-17 18:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0004_rename_tipo_usuario_authuser_id_tipo_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authuser',
            name='id_tipo_usuario',
            field=models.ForeignKey(db_column='id_tipo_usuario', default=2, on_delete=django.db.models.deletion.CASCADE, related_name='tipo_usuario', to='application.tipousuario'),
        ),
    ]