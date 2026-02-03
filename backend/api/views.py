from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Dataset
from .utils import analyze_csv


@api_view(['POST'])
def upload_csv(request):
    if 'file' not in request.FILES:
        return Response(
            {"error": "No file uploaded"},
            status=status.HTTP_400_BAD_REQUEST
        )

    file = request.FILES['file']

    try:
        summary = analyze_csv(file)
    except Exception as e:
        return Response(
            {"error": str(e)},
            status=status.HTTP_400_BAD_REQUEST
        )

    Dataset.objects.create(
        filename=file.name,
        summary=summary
    )

    if Dataset.objects.count() > 5:
        Dataset.objects.order_by('uploaded_at').first().delete()

    return Response(
        {
            "message": "CSV processed successfully",
            "summary": summary
        },
        status=status.HTTP_201_CREATED
    )


@api_view(['GET'])
def latest_summary(request):
    dataset = Dataset.objects.order_by('-uploaded_at').first()

    if not dataset:
        return Response({"message": "No data available"}, status=status.HTTP_404_NOT_FOUND)

    return Response(dataset.summary, status=status.HTTP_200_OK)


@api_view(['GET'])
def upload_history(request):
    datasets = Dataset.objects.order_by('-uploaded_at')[:5]

    history = [
        {
            "filename": d.filename,
            "uploaded_at": d.uploaded_at,
            "summary": d.summary
        }
        for d in datasets
    ]

    return Response(history, status=status.HTTP_200_OK)
