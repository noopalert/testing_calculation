from django.db import models


class ContractClient(models.Model):
    contract_number = models.CharField(max_length=100, db_column='contract_number', null=True, blank=True)
    client_name = models.CharField(max_length=100, db_column='client_name', null=True, blank=True)
    otr = models.IntegerField(db_column='otr', null=True, blank=True)
    monthly_installment = models.IntegerField(db_column='monthly_installment', default=None, null=True, blank=True)
    range_date = models.IntegerField(db_column='range_date', null=True, blank=True)
    dp = models.IntegerField(db_column='dp', null=True, blank=True)

    class Meta:
        db_table = 'contract_client'

    def __str__(self):
        return f'{self.client_name} - {self.contract_number}'

class Installment(models.Model):
    contract_number = models.ForeignKey(
        ContractClient,
        on_delete=models.CASCADE,
        db_column='contract_number',
        null=True, 
        blank=True
    )
    number_installment = models.IntegerField(db_column='number_installment', null=True, blank=True)
    total_installment = models.IntegerField(db_column='total_installment', null=True, blank=True)
    due_date = models.DateField(db_column='due_date', null=True, blank=True)

    class Meta:
        db_table = 'installment'

    def __str__(self):
        return f'{self.contract_number} - {self.number_installment}'