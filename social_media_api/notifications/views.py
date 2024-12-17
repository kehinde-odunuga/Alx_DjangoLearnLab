from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from notifications.models import Notification
from notifications.serializers import NotificationSerializer

class NotificationListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Fetch notifications for the current user
        notifications = Notification.objects.filter(recipient=request.user).order_by('-timestamp')
        
        # Serialize the notifications (adjust fields as needed)
        data = [
            {
                "id": notification.id,
                "actor": notification.actor.username,
                "verb": notification.verb,
                "timestamp": notification.timestamp,
                "is_read": notification.is_read,
                "target": str(notification.target),
            }
            for notification in notifications
        ]

        return Response(data, status=200)

    # def get(self, request):
    #     user = request.user
    #     notifications = user.notifications.filter(read=False).order_by('-timestamp')
    #     serializer = NotificationSerializer(notifications, many=True)
    #     return Response(serializer.data)
