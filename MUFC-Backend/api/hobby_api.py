from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from MUFC2.serializers import HobbySerializer
from MUFC2.services.hobby_service import filter_friends_with_all_hobbies, hobby_rank_popularity, read_hobbies_from_friend, \
    add_hobby_to_friend, remove_hobby_from_friend


@api_view(['GET'])
def get_sorted_hobby_popularity_endpoint(request, user_id):
    sorted_hobbies = hobby_rank_popularity(user_id)
    if sorted_hobbies:
        sorted_hobbies_serialized = HobbySerializer(sorted_hobbies, many=True).data
        return Response(sorted_hobbies_serialized, status=status.HTTP_200_OK)
    return Response({"error": "There is no hobby or error when retrieving ranked hobbies list"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def filter_friends_with_all_hobbies_endpoint(request, user_id):
    filtered_friend_list = filter_friends_with_all_hobbies(user_id, request.data['hobby_list'])

    if filtered_friend_list:
        filtered_friend_serialized = HobbySerializer(filtered_friend_list, many=True).data
        return Response(filtered_friend_serialized, status=status.HTTP_200_OK)
    return Response({"error":"There is no friend or Error while filtering friends"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_friend_hobbies_endpoint(request, friend_id):
    hobbies = read_hobbies_from_friend(friend_id)
    if hobbies:
        hobbies_serialized = HobbySerializer(hobbies, many=True).data
        return Response(hobbies_serialized, status=status.HTTP_200_OK)
    return Response({"error": "There is no hobby or Error while reading hobbies from friend"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def add_hobby_to_friend_endpoint(request, friend_id):
    success = add_hobby_to_friend(friend_id, request.data['hobby_name'])
    if success:
        hobbies = read_hobbies_from_friend(friend_id)
        hobbies_serialized = HobbySerializer(hobbies, many=True).data
        return Response({"success": True, "data": hobbies_serialized}, status=status.HTTP_200_OK)
    return Response({"error": "Error when adding hobby to friend"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def remove_hobby_from_friend_endpoint(request, friend_id):
    success = remove_hobby_from_friend(friend_id, request.data['hobby_name'])
    if success:
        return Response({"success": True}, status=status.HTTP_200_OK)
    return Response({"error": "Error when removing hobby from friend"}, status=status.HTTP_400_BAD_REQUEST)













