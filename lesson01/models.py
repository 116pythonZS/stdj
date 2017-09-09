#!/usr/local/bin python3
# -*- coding=utf-8 -*-

from django.db import models

class Book(models.Model):
    """ 文档说明 """
    name = models.CharField(max_length=50)
    pub_date = models.DateField()
