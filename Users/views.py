from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# In-memory storage
users = {} # dictionary to store users with ID as key
next_id = 1  # starts from 1 and increments manually

@api_view(['POST'])
def create_user(request): # function to create user
    global next_id
    name = request.data.get('name')
    email = request.data.get('email')

    if not name or not email:
        return Response({'error': 'Both name and email are required.'}, status=400)

    user_id = next_id
    next_id += 1

    user = {'id': user_id, 'name': name, 'email': email}
    users[user_id] = user

    return Response(user, status=201)


@api_view(['GET'])
def get_user_detail(request, id): # function to get user details by ID
    try:
        id = int(id)
    except ValueError:
        return Response({'Invalid ID format.'}, status=400)

    user = users.get(id)
    if not user:
        return Response({'User not found.'}, status=404)

    return Response(user)
