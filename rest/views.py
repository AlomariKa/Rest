import requests
from rest_framework import mixins, viewsets, status
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import TokenError

# Define the base URL for the external API
# BASE_URL = "http://localhost:3000/employees"
#
# @api_view(['GET'])
# def list_employees(request):
#     """Handle GET request to list all employees."""
#     token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQyNTkzOTUzLCJpYXQiOjE3NDI1OTM2NTMsImp0aSI6IjBjZTBjYWM3ZTgwZjRjZmJhN2QzZTgwYWUyZjk0ZjgxIiwidXNlcl9pZCI6MX0.yE779fgCg6S8zmBXkJIVv8OJA62mQJKDsu1z923IjBc"
#     headers = {
#         "Authorization": f"Bearer {token}",
#         "Content-Type": "application/json"
#     }
#
#     # Set up the headers for the request to the external API
#     response = requests.get(BASE_URL, headers=headers)
#     return Response(response.json(), status=response.status_code)
#
# @api_view(['GET'])
# def retrieve_employee(request, pk):
#     """Handle GET request to retrieve a single employee."""
#     response = requests.get(f"{BASE_URL}/{pk}")
#     return Response(response.json(), status=response.status_code)
#
# @api_view(['POST'])
# def create_employee(request):
#     """Handle POST request to create a new employee."""
#     response = requests.post(BASE_URL, json=request.data)
#     return Response(response.json(), status=response.status_code)
#
# @api_view(['PUT'])
# def update_employee(request, pk):
#     """Handle PUT request to update an existing employee."""
#     response = requests.put(f"{BASE_URL}/{pk}", json=request.data)
#     return Response(response.json(), status=response.status_code)
#
# @api_view(['DELETE'])
# def destroy_employee(request, pk):
#     """Handle DELETE request to delete an employee."""
#     response = requests.delete(f"{BASE_URL}/{pk}")
#     return Response(status=response.status_code)

class MockItemViewSet(mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin,
                      viewsets.GenericViewSet):
    # In DRF, you can combine these mixins with GenericViewSet to create a ViewSet with just the desired behaviors.
    permission_classes = [IsAuthenticated]  # Require authentication for all actions



    def list(self, request, *args, **kwargs):

        response = requests.get("http://localhost:3000/employees", )

        return Response(response.json())

    def retrieve(self, request, pk=None):
        # Handle GET (retrieve single item)

        response = requests.get(f"http://localhost:3000/employees/{pk}")
        return Response(response.json())

    def create(self, request, *args, **kwargs):

        # Handle POST (create new item)
        response = requests.post("http://localhost:3000/employees", json=request.data) # Sends the request's data to the JSON server.

        return Response(response.json(), status=response.status_code) # Returns the created item's data and HTTP status code.

    def update(self, request, pk=None):
        # Handle PUT (update existing item)

        response = requests.put(f"http://localhost:3000/employees/{pk}", json=request.data)
        return Response(response.json(), status=response.status_code)

    def destroy(self, request, pk=None):
        # Handle DELETE (delete an item)

        response = requests.delete(f"http://localhost:3000/employees/{pk}")
        return Response(status=response.status_code)
