from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.utils.encoders import JSONEncoder

from MUFC2.model.friend import Friend
from MUFC2.serializers import FriendSerializer
from MUFC2.services.friend_service import get_friend_details, get_friends_from_user, add_friend, update_friend_all_att, \
    delete_friend, update_friend_single_att, rank_friends_with_ordering, should_promptly_contact_friend


@api_view(['GET'])
def get_friend_details_endpoint(request, friend_id):
    details = get_friend_details(friend_id)
    if details:
        return Response(FriendSerializer(details).data, status=status.HTTP_200_OK)
    return Response({"message": "Failed to get friend details"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def get_friends_from_user_endpoint(request, user_id):
    friend_list = get_friends_from_user(user_id)
    if friend_list:
        serialized_friends = FriendSerializer(friend_list, many=True).data
        return Response(serialized_friends, status=status.HTTP_200_OK)
    else:
        return Response({"message": "Failed to get list friends"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def add_friend_endpoint(request, user_id):
    data = request.data
    friend = add_friend(
        user_id=user_id,
        name = data['name'],
        email = data['email'],
        phone = data['phone'],
        dob = data['dob'],
        level_friendship=data['level_friendship'],
        last_contacted=data['last_contacted'],
        notes=data['notes'],
        facebook = data['facebook'],
        whatsapp=data['whatsapp'],
        insta = data['insta'],
        tele = data['tele'],
    )
    if friend:
        friend_data = FriendSerializer(friend).data
        return Response(friend_data, status=status.HTTP_200_OK)
    return Response({"message": "Failed to add friend"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['PATCH'])
def update_friend_all_att_endpoint(request, friend_id):
    fields_values = request.data  # Fields and values provided in JSON payload

    success = update_friend_all_att(friend_id, fields_values)

    if success:
        friend_data = FriendSerializer(get_friend_details(friend_id)).data
        return Response({"message": "Friend updated successfully", "data":friend_data}, status=status.HTTP_200_OK)
    elif success is None:
        return Response({"error": "Friend does not exist"}, status=status.HTTP_404_NOT_FOUND)
    else:
        return Response({"error": "Validation or unknown error occurred during update"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_friend_endpoint(request, friend_id):
    success = delete_friend(friend_id)

    if success:
        return Response({"message": "Friend deleted successfully"}, status=status.HTTP_200_OK)
    elif success is None:
        return Response({"error": "Friend does not exist"}, status=status.HTTP_404_NOT_FOUND)
    else:
        return Response({"error": "Validation or unknown error occurred during delete"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PATCH'])
def update_friend_single_att_endpoint(request, friend_id):
    data = request.data
    attribute = data.get('attribute')
    value = data.get('value')

    if update_friend_single_att(friend_id, attribute, value):
        return Response({"message": "Friend updated successfully", "data": FriendSerializer(get_friend_details(friend_id)).data}, status=status.HTTP_200_OK)
    return Response({"error": "Friend does not exist"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def get_sorted_friend_list(request, user_id):
    sorted_list = rank_friends_with_ordering(user_id, request.GET.get('attribute'), request.GET.get('order'))

    if sorted_list:
        sorted_list_serialized = FriendSerializer(sorted_list, many=True).data
        return Response(sorted_list_serialized, status=status.HTTP_200_OK)
    return Response({"message": "Error in retrieving sorted friend list"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def get_promptly_contact_friend_endpoint(request, user_id):
    contact_list = should_promptly_contact_friend(user_id, request.GET.get('expiration_period'), request.GET.get('notification_period'))
    if contact_list:
        contact_list_serialized = FriendSerializer(contact_list, many=True).data
        return Response(contact_list_serialized, status=status.HTTP_200_OK)
    return Response({"message": "Error in retrieving promptly contacted friend list"}, status=status.HTTP_404_NOT_FOUND)






