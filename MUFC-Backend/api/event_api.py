from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

import MUFC2.services
from MUFC2.serializers import EventSerializer
from MUFC2.services import event_service
from MUFC2.services.event_service import read_event_details


@api_view(['POST'])
def create_event_endpoint(request, user_id, friend_id):
    event = event_service.create_event(
        name = request.data['name'],
        date = request.data['date'],
        user_id = user_id,
        friend_id = friend_id,
        classification = request.data['classification'],
        details = request.data['details'],
    )

    if event:
        return Response(EventSerializer(event).data, status=status.HTTP_201_CREATED)
    return Response({"error" : "Error occurred when creating event"},status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_user_event_list_endpoint(request, user_id):
    event_list = event_service.get_user_event_list(user_id)
    if event_list:
        return Response(EventSerializer(event_list, many=True).data, status=status.HTTP_200_OK)
    return Response({"error": "Error when getting user event"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_friend_event_list_endpoint(request, friend_id):
    event_list = event_service.get_friend_event_list(friend_id)
    if event_list:
        return Response(EventSerializer(event_list, many=True).data, status=status.HTTP_200_OK)
    return Response({"error": "Error when getting friend event"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_event_details_endpoint(request, event_id):
    event = event_service.read_event_details(event_id)
    if event:
        return Response(EventSerializer(event).data, status=status.HTTP_200_OK)
    return Response({"error": "Error when reading event"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_event_by_month_endpoint(request, user_id):
    filtered_event = event_service.group_event_by_month(user_id, request.data['month'])
    if filtered_event:
        return Response(EventSerializer(filtered_event, many=True).data, status=status.HTTP_200_OK)
    return Response({"error": "Error when getting monthly event"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_event_by_day_endpoint(request, user_id):
    filtered_event = event_service.group_event_by_day(user_id, request.data['day'])
    if filtered_event:
        return Response(EventSerializer(filtered_event, many=True).data, status=status.HTTP_200_OK)
    return Response({"error": "Error when getting daily event"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PATCH'])
def edit_event_details_endpoint(request, event_id):
    field_values = request.data['field_values']
    success = event_service.edit_event_details(event_id, field_values)
    if success:
        return Response({"success": True, "data":EventSerializer(read_event_details(event_id)).data}, status=status.HTTP_200_OK)
    return Response({"error": "Error when editing event"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_event_endpoint(request, event_id):
    success = MUFC2.services.event_service.delete_event(event_id)
    if success:
        return Response({"success": True}, status=status.HTTP_200_OK)
    return Response({"error": "Error when deleting event"}, status=status.HTTP_400_BAD_REQUEST)



