from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(['GET'])
def api_root(request, format=None):
    response = Response({
        'products': reverse('product-list', request=request, format=format),
        'users': reverse('user-list', request=request, format=format),
        'categories': reverse('category-list', request=request, format=format),
<<<<<<< HEAD
        'sign-up': reverse('user-create', request=request, format=format)
=======
>>>>>>> 37228d8634f9299cb08dc0a0af3415304659af19
    })
    return response