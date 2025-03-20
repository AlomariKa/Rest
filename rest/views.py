import requests
from rest_framework import mixins, viewsets
from rest_framework.response import Response

class MockItemViewSet(mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin,
                      viewsets.GenericViewSet):
# In DRF, you can combine these mixins with GenericViewSet to create a ViewSet with just the desired behaviors.

    def list(self, request, *args, **kwargs):
        # Handle GET (list all items)
        response = requests.get("http://localhost:3000/employees") # # Sends a GET request to the JSON server.
        # response.json() is a method provided by the requests library that parses the JSON response from the server and converts it into a Python object.
        return Response(response.json()) #  Returns the data as an HTTP response (wrapped in DRF's `Response` object).

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
