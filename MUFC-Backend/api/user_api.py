from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from MUFC2.model.user import User
from MUFC2.serializers import UserSerializer
from MUFC2.services.user_service import get_user_from_id, create_user, update_user, delete_user, update_all_user_fields

@api_view(['POST'])
def create_user_endpoint(request):
    data = request.data
    user = create_user(
        username = data.get('username'),
        password = data.get('password'),
        name = data.get('name'),
        email = data.get('email'),
        phone = data.get('phone'),
        dob = data.get('dob'),
        tele = data.get('tele'),
    )
    if user:
        return Response(UserSerializer(user), status=status.HTTP_201_CREATED)
    return Response({"message": "Failed to create new user"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_user_from_id_endpoint(request, user_id):
    user = get_user_from_id(user_id)
    if user:
        return Response(UserSerializer(user).data, status=status.HTTP_200_OK)
    return Response({"error": "User not found!"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['PATCH'])
def update_all_user_fields_endpoint(request, user_id):
    success = update_all_user_fields(user_id, request.data['field_values'])
    if success:
        return Response({"message": "User updated successfully!", "data": UserSerializer(get_user_from_id(user_id)).data}, status=status.HTTP_200_OK)
    return Response({"message": "Failed to update fields"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PATCH'])
def update_user_attribute_endpoint(request, user_id):
    data = request.data
    attribute = data.get('attribute')
    value = data.get('value')

    if update_user(user_id, attribute, value):
        return Response({"message": f"User updated with {attribute} field successfully!", "data": UserSerializer(get_user_from_id(user_id)).data},  status=status.HTTP_200_OK)
    return Response({"error": "Update failed!"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete_user_endpoint(request, user_id):
    if delete_user(user_id):
        return Response({"message": "User deleted successfully!"}, status=status.HTTP_204_NO_CONTENT)
    return Response({"error": "User deletion failed"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
# @permission_classes([AllowAny])
# @csrf_exempt
def login_endpoint(request):
    identifier = request.data.get('identifier')
    password = request.data.get('password')

    user = None

    if User.objects.filter(username=identifier).exists():
        user = authenticate(username=identifier, password=password)
    elif User.objects.filter(email=identifier).exists():
        user_obj = User.objects.get(email = identifier)
        user = authenticate(username=user_obj.username, password=password)
    if user is not None:
        token, _ = Token.objects.get_or_create(user = user)
        return Response({"token": token.key,
                         "message": "Login successful",
                         "user_id":user.id,
                         "username": user.username,}
                        , status=status.HTTP_200_OK)

    return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)




