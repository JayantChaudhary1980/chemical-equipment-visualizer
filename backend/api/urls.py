from django.urls import path
from .views import upload_csv, latest_summary, upload_history, download_latest_pdf

urlpatterns = [
    path('upload/', upload_csv),
    path('latest/', latest_summary),
    path('history/', upload_history),
    path("report/", download_latest_pdf),
]
