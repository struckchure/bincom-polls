from django.db import models


class LGA(models.Model):
    lga_id = models.PositiveBigIntegerField(blank=False)
    lga_name = models.CharField(max_length=50, blank=False)
    state_id = models.PositiveBigIntegerField(blank=False)
    lga_description = models.TextField(blank=True)
    entered_by_user = models.CharField(max_length=50, null=True)
    date_entered = models.DateTimeField(auto_now_add=True, null=True)
    user_ip_address = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.lga_name


class PollUnit(models.Model):
    polling_unit_id = models.PositiveBigIntegerField(blank=False)
    ward_id = models.PositiveBigIntegerField(blank=False)
    lga_id = models.ForeignKey(LGA, on_delete=models.CASCADE)
    uniquewardid = models.PositiveBigIntegerField(blank=False)
    polling_unit_number = models.CharField(max_length=50, blank=True)
    polling_unit_name = models.CharField(max_length=50, blank=True)
    polling_unit_description = models.TextField(blank=True, null=True)
    lat = models.CharField(max_length=255, blank=True)
    long = models.CharField(max_length=255, blank=True)
    entered_by_user = models.CharField(max_length=50, null=True)
    date_entered = models.DateTimeField(auto_now_add=True, null=True)
    user_ip_address = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.polling_unit_name
