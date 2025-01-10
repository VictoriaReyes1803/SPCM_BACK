from rest_framework.generics import ListAPIView
from ..serializers import ActivityLogSerializer

class ActivityLogView(ListAPIView):
    queryset = ActivityLog.objects.all().order_by('-timestamp')
    serializer_class = ActivityLogSerializer
    permission_classes = [IsAuthenticated]
