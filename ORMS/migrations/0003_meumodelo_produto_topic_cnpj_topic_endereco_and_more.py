# Generated by Django 4.2.10 on 2024-11-16 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ORMS', '0002_entry'),
    ]

    operations = [
        migrations.CreateModel(
            name='MeuModelo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
                ('imagem', models.ImageField(upload_to='imagens/')),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagem', models.ImageField(blank=True, null=True, upload_to='produtos/')),
                ('categoria', models.CharField(max_length=255)),
                ('nome', models.CharField(max_length=255)),
                ('modelo', models.CharField(blank=True, max_length=255, null=True)),
                ('marca', models.CharField(default='Sem Marca', max_length=255)),
                ('codigo', models.CharField(max_length=20, unique=True)),
                ('existente', models.IntegerField(default=0)),
                ('sku', models.CharField(max_length=20, unique=True)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantidade', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='topic',
            name='cnpj',
            field=models.CharField(default='00.000.000/0000-00', max_length=14),
        ),
        migrations.AddField(
            model_name='topic',
            name='endereco',
            field=models.CharField(default='Endereço Padrão', max_length=255),
        ),
        migrations.AddField(
            model_name='topic',
            name='telefone',
            field=models.CharField(default='(00) 0000-0000', max_length=15),
        ),
    ]
