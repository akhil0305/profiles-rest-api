from rest_framework.views import APIView            #rest_framework = Django Rest Framework
from rest_framework.response import Response

class HelloApiView(APIView):
    """Test API View"""
    """Way it works - We define a URL which is our end point and then assign it to this view and the Django rest framework handles it by
    calling the appropriate function in the view for the HTTP request you make"""

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as function(get, post, patch, put, delete)',
            'Is similar to a traditional Django view',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message':'Hello!', 'an_apiview':an_apiview})     #Converts given list or dictionary to json file and then returns as response object
