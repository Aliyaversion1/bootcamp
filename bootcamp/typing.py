# from rest_framework import renderers, viewport 
# from rest_ framework import permissions 
# from rest_framework.decorators import apl_view, action 
# from rest_framework. response import Response
# from rest_framework. reverse import reverse 
# from django.contrib.auth.models import User

# from snippets.models import snippet
# from snippets.permission import IsOwnerOrReadOnly
# from snippets.seriulizers import SnippetSerializer,UserSerializer


# class SnippetViewSet(viewsets.ModeViewset);
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwneerOrReadOnly]
   
#     @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
# def highlight(self, request, *args, **kwargs):
#     snippet = self.get_object()
#     return Response(Snippet.highlighted)

#     def perform_create(self, serialiser):
#         serializer.save(owner=self.request.user)


# class UserViewSet(viewset)




name = input()
last_name = input()
age = input()
city = input()
print(f" You are {name} {last_name} {age}  You live in {city}")






