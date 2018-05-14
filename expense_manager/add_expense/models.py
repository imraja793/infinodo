from __future__ import unicode_literals

from django.db import models


class AddExpense(models.Model):
    expense_title = models.CharField('Expense Title', max_length=20)
    amount = models.DecimalField('Amount', decimal_places=2, max_digits=10)
    currency = models.CharField('Currency', max_length=23)
    payment_type = models.CharField('Payment Type', max_length=30)
    expense_type = models.CharField('Expense Type', max_length=200, blank=True)
    vendor_name = models.CharField('Vendor Name', max_length=200, blank=True)
