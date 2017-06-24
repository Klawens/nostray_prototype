# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import django.utils.timezone as timezone
# Create your models here.


class Animals(models.Model):
	SPECIES_CHOICES = [
		('DOG', 'dog'),
		('CAT', 'cat'),
		('OTHER', 'other'),
	]
	SEX_CHOICES = [
		('MALE', 'male'),
		('FEMALE', 'female'),
	]
	animal_id = models.AutoField(max_length=10, primary_key=True, verbose_name=u"动物编号")
	station_id = models.IntegerField(verbose_name=u"救助站编号")
	name = models.CharField(max_length=10, verbose_name=u"动物名")
	sex = models.CharField(max_length=6, choices=SEX_CHOICES, verbose_name=u"性别")
	age = models.IntegerField(null=True, verbose_name=u"年龄")
	health = models.CharField(max_length=10, null=True, blank=True, verbose_name=u"健康状况")
	price = models.CharField(max_length=10, default='free', verbose_name=u"价格")
	add_time = models.DateTimeField(default=timezone.now, verbose_name=u"入站日期")
	species = models.CharField(max_length=4, choices=SPECIES_CHOICES, verbose_name=u"物种")
	#dog_var = models.CharField(max_length=10, choices=DOG_CHOICES, null=True, verbose_name=u"狗品种")
	#cat_var = models.CharField(max_length=10, choices=CAT_CHOICES, null=True, verbose_name=u"猫品种")
	photo = models.ImageField(upload_to='animal_img', null=True, verbose_name=u"动物图片")
