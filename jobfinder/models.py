from django.db import models
from django.db import models

class JobListing(models.Model):
    job_title = models.CharField(max_length=255)
    job_type=models.CharField(max_length=255 , default="Nothing Here")
    company_name = models.CharField(max_length=255)
    job_details = models.TextField()

    def __str__(self):
        return self.job_title