# Generated by Django 3.2.12 on 2022-03-25 13:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('slug', models.SlugField(null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='İsim')),
                ('email', models.CharField(max_length=50, verbose_name='Email')),
                ('message', models.TextField(verbose_name='Mesaj')),
            ],
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('slug', models.SlugField(null=True, unique=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogapp.category', verbose_name='Alt kategori')),
            ],
        ),
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Post başlığı')),
                ('body', models.TextField(verbose_name='İçeriği')),
                ('code', models.TextField(blank=True, verbose_name='Örnek kod')),
                ('views', models.IntegerField(default=0, verbose_name='Görüntülenme sayısı')),
                ('imageurl', models.ImageField(default='static/img/default.png', upload_to='static/upload/%Y/%m/%d/', verbose_name='Fotoğraf seç')),
                ('created_datetime', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Yazar')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='blogapp.category', verbose_name='Kategori')),
                ('sub_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='blogapp.subcategory', verbose_name='Alt kategori')),
            ],
        ),
    ]