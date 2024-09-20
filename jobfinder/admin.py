# jobfinder/admin.py
from django.contrib import admin
from .models import JobListing

@admin.register(JobListing)
class JobListingAdmin(admin.ModelAdmin):
    list_display = ('job_title', 'company_name', 'job_type', 'job_link','job_origin')  # Columns to display
    search_fields = ('job_title', 'company_name')  # Enable search on job title and company name
    list_filter = ('job_type','job_origin')  # Add filter by job type
    ordering = ('-job_title',)  # Order by job title

