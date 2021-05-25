from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet, ViewSet
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from home.api.v1.serializers import (
    AppSerializer,
    PlanSerializer,
    SignupSerializer,
    SubscriptionSerializer,
    UserSerializer,
)


class SignupViewSet(ModelViewSet):
    serializer_class = SignupSerializer
    http_method_names = ["post"]


class LoginViewSet(ViewSet):
    """Based on rest_framework.authtoken.views.ObtainAuthToken"""

    serializer_class = AuthTokenSerializer

    def create(self, request):
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, created = Token.objects.get_or_create(user=user)
        user_serializer = UserSerializer(user)
        return Response({"token": token.key, "user": user_serializer.data})


from home.models import App, Plan, Subscription


class AppViewSet(ModelViewSet):

    queryset = App.objects.all().order_by('id')
    serializer_class = AppSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        qs = App.objects.filter(user=user)
        return qs

    def perform_create(self, serializer):
        request = serializer.context['request']
        serializer.save(user=request.user)


class PlanViewSet(ReadOnlyModelViewSet):

    queryset = Plan.objects.all().order_by('id')
    serializer_class = PlanSerializer
    permission_classes = (IsAuthenticated,)


class SubscriptionViewSet(ModelViewSet):

    queryset = Subscription.objects.all().order_by('id')
    serializer_class = SubscriptionSerializer
    permission_classes = (IsAuthenticated,)
    http_method_names = ['head', 'get', 'post', 'put', 'patch']

    def get_queryset(self):
        user = self.request.user
        qs = Subscription.objects.filter(app__user=user)
        return qs