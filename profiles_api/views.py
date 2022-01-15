from rest_framework.views import APIView            #rest_framework = Django Rest Framework
from rest_framework.response import Response
from rest_framework import status       #They are a list of HTTP status codes that i Can use to return responses
from rest_framework import viewsets

from profiles_api import serializers

class HelloApiView(APIView):
    """Test API View"""
    """Way it works - We define a URL which is our end point and then assign it to this view and the Django rest framework handles it by
    calling the appropriate function in the view for the HTTP request you make"""

    serializer_class = serializers.HelloSerializer      #says whenever you put a POST, PUT or PATCH request expect i/p as in serializers.py - name

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as function(get, post, patch, put, delete)',
            'Is similar to a traditional Django view',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message':'Hello!', 'an_apiview':an_apiview})     #Converts given list or dictionary to json file and then returns as response object

    def post(self, request):
        """Creeate a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():       #validates the serializer input, i.e, checks if name is less than 10 characters as in serializer.py
            name = serializer.validated_data.get('name')   #retrieves the name field defined and any field you defined in serializer.py can be retrieved this Way
            message = f'Hello {name}'
            return Response({'message':message})
        else:               #by default Response() returns a HTTP 200 Okay status
            return Response( serializer.errors,      #serializer.error gives all the errors that were validated based on the conditions you gave
                status = status.HTTP_400_BAD_REQUEST     #you can also pass integer 400
            )

    def put(self, request, pk=None):        #pk - is the id of the object to be updated with the put request. put - is removing existing object and updating it with new object provided
        """Handle updating an object"""

        return Response({'method':'PUT'})

    def patch(self, request, pk=None):      #only update a field of the object, eg, if name is an object containing fname and lname, update fname
        """Handle a partial update of an object"""

        return Response({'method' : 'PATCH'})

    def delete(self, request, pk=None):
        """Delete an Object"""

        return Response({'method':'DELETE'})

class HelloViewSet(viewsets.ViewSet):
    """Test API Viewset"""
    """In Viewsets we add functions, to perform actions in a typical API"""

    serializer_class = serializers.HelloSerializer

    def list(self, request):            #similar to HTTP get
        """Return a Hello message"""

        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update)',
            'Automatically maps URLs using Routers',
            'Provides more functionality using less code',
        ]

        return Response({'message':'Hello!', 'a_viewset':a_viewset})

    def create(self, request):
        """Create a new Hello message"""

        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'meassage' : message})
        else:
            return Response(serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """Handle getting object by its ID"""

        return Response({'http method':'GET'})

    def update(self, request, pk=None):
        """Handle updating an object"""

        return Response({'http method':'PUT'})

    def partial_update(self, request, pk=None):
        """Handle updating part of an object"""

        return Response({'http method':'PATCH'})

    def destroy(self, request, pk=None):
        """Handle removing an object"""

        return Request({'http method':'DELETE'})
