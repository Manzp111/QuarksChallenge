from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


users = {} # Dictionary to store users
next_id = 1 # Global variable to track the next user ID

@api_view(['GET', 'POST'])
def create_user(request): # Endpoint to create a user or list all users
    global next_id

    if request.method == 'GET':
        if not users:
            return Response({'No users found.'}, status=404)
        return Response(list(users.values()), status=200)

    if request.method == 'POST':
        name = request.data.get('name')
        email = request.data.get('email')

        if not name or not email:
            return Response({'name and email are required.'}, status=400)

        user_id = next_id
        next_id += 1

        user = {'id': user_id, 'name': name, 'email': email}
        users[user_id] = user

        return Response(user, status=201)


@api_view(['GET'])
def get_user_detail(request, id): # Endpoint to get user details by ID
    try:
        id = int(id)
    except ValueError:
        return Response({'Invalid ID format.'}, status=400)

    user = users.get(id)
    if not user:
        return Response({'User not found.'}, status=404)

    return Response(user)
