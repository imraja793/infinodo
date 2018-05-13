# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class AddExpense(models.Model):

    expensetitle = models.CharField(max_length=20)
    amount = models.DecimalField(decimal_places=2, max_digits=10)
    currency = models.CharField(max_length=23)
    paymenttype = models.CharField(max_length=30)
    expensetype = models.CharField(max_length=200)
    vendorname = models.CharField(max_length=200)

    def __str__(self):
        return self.expensetitle