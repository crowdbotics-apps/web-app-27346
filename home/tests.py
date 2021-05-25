import json
import decimal

from django.urls import reverse
from django.test import Client
from rest_framework.test import APITestCase
from rest_framework import status

from home.models import App, Plan, Subscription, User


class TestSetup(APITestCase):

    data = {
        'username': 'vibrito',
        'email': 'ramalhodevitor@gmail.com',
        'password': 'test123@',
    }

    @classmethod
    def setUpClass(cls):
        cls.registerUser()
        cls.createApp()
        cls.createPlans()
        super().setUpClass()

    def setUp(self):
        self.authenticateUser()
        super().setUp()

    def tearDown(self):
        super().tearDown()

    @classmethod
    def tearDownClass(cls):
        cls.destroyUser()
        cls.destroyApp()
        cls.destroyPlans()

    @classmethod
    def registerUser(cls):
        Client().post("/rest-auth/registration/", cls.data)

    def authenticateUser(self):
        response = self.client.post("/rest-auth/login/", self.data)
        self.token = response.data['key']

    @classmethod
    def getUser(cls):
        cls.user = User.objects.first()

    @classmethod
    def createApp(cls):

        cls.getUser()
        cls.app = App.objects.create(
            name="Test",
            description="Test App",
            type="Web",
            framework="Django",
            user=cls.user
        )

    @classmethod
    def createPlans(cls):

        plans = [
            ['Free', 'Free Plan', 0.00],
            ['Standard', 'Standard Plan', 10.00],
            ['Pro', 'Pro Plan', 25.00]
        ]
        for plan in plans:
            Plan.objects.create(
                name=plan[0], 
                description=plan[1], 
                price=decimal.Decimal(plan[2])
            )

    @classmethod
    def destroyUser(cls):
        User.objects.all().delete()

    @classmethod
    def destroyApp(cls):
        App.objects.all().delete()

    @classmethod
    def destroyPlans(cls):
        Plan.objects.all().delete()


class AppTestCase(TestSetup):

    def test_app_get(self):
        response = self.client.get("/api/v1/apps/", format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_app_post(self):
        data = {
            "name": "Test",
            "description": "Test App",
            "type": "Web",
            "framework": "Django",
        }
        response = self.client.post("/api/v1/apps/", data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.get("/api/v1/apps/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_app_get_specific_id(self):
        response = self.client.get("/api/v1/apps/1/", format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # TODO: add more test to increase coverage


class PlanTestCase(TestSetup):

    def test_plan_get(self):
        response = self.client.get("/api/v1/plans/", format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)

    def test_plan_get_specific_id(self):
        response = self.client.get("/api/v1/plans/4/", format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_plan_get_unexistent_specific_id(self):
        response = self.client.get("/api/v1/plans/7/", format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_plan_forbidden_post(self):
        data = {}
        response = self.client.post("/api/v1/plans/", data, format='json')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_plan_forbidden_put(self):
        data = {}
        response = self.client.put("/api/v1/plans/4/", data, format='json')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_plan_forbidden_patch(self):
        data = {}
        response = self.client.patch("/api/v1/plans/4/", data, format='json')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    # TODO: add more test to increase coverage


class SubscriptionTestCase(TestSetup):

    def test_susbcription_plan_get(self):
        response = self.client.get("/api/v1/plans/", format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)

    def test_subscription_get_empty(self):
        response = self.client.get("/api/v1/subscriptions/", format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)

    # TODO: add more test to increase coverage