# Generated by Django 4.0.5 on 2022-08-23 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CmsSlider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cms_img', models.ImageField(upload_to='slider_img')),
                ('cms_title', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('cms_text', models.CharField(max_length=200, verbose_name='Текс')),
                ('cms_css', models.CharField(default='-', max_length=200, null=True, verbose_name='CSS class')),
            ],
            options={
                'verbose_name': 'Слайд',
                'verbose_name_plural': 'Слайды',
            },
        ),
    ]
