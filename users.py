from usersapp.serializers import UserSerializer
from usersapp.models import User
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status


class UsersViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def create(self, request):
        if not request.user.is_authenticated:
            return Response("You should be authenticated")
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            response = {'code': 201, 'success': True, "id":serializer.data["id"]}
            return Response(response, status=status.HTTP_201_CREATED, headers=headers)


"""

#Problems and solutions

Problem case: 1
There is a lot of duplicated code that has already being implemented in django res

Solution: Refactor

Problem case: 2
There is syntax error in the user creation object method --create() the closing the bracket is absent.
**Solution: ** Close the bracket

Problem case: 1 Wildcard import
Solution: Since I know that I'll only use one response from the rest_framework.response library, I'll import only Response, rather than importing everything. Reason is that it will put a lot of stuff in my namespace and will likely override some other previous imports from other libraries with the same name

It's bad practice to import wildcard and it impacts readability negatively as you won't know exactly what is been imported and makes debugging difficult

Problem case: 3 we are not using dateutill library
Solution: Don't import it

Problem case: 4
No UserSerializer?
Solution: I'll create and import the UserSerializer

Problem case: 5
Redundant code
Solution: It makes sense to use the serializers perform_create() method instead of instantiating and using the create method from the User object again.

Problem case: 6
Indentation error
Solution: I'll adjust the indentation of the create method into the UsersViewSet Class

Problem case: 7 I don't need the json library
Solution: needless to import it.

Problem case: 8
No User model
Solution I will import the User model in the view since I'm using it

Problem case: 9
Response code for 'created' is 201 not 200
Solution: change status code to 201
Since we have "comment" that means we need to create a custom user model to include that and import it.

It's is_authenticated not is_authenticated(). is_authenticated is not callable.

At the end of the day we have fewer lines of code, a codebase that works and uses best practices and of course, is efficient.

"""
