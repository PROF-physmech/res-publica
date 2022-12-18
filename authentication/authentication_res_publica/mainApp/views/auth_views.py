from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.exceptions import ValidationError
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from ..models import Users
from ..serializers import LoginSerializer, ErrorSerializer
import logging

from ..utils.passwordHasher import verify_password

logger = logging.getLogger(__name__)
"""Логгер для вывода протокола действий и ошибок"""

errorResponse = openapi.Response(
    description='Ответ с сообщением об ошибке',
    schema=ErrorSerializer,
)
"""Описание для документации ответа метода в случае возникновения ошибки"""


class AdminLogin(APIView):
    """Класс реализующий метод входа администраторов в систему"""
    parser_classes = [JSONParser]
    renderer_classes = [JSONRenderer]

    def handle_exception(self, exc: Exception) -> Response:
        """Обработчик ошибок метода .post"""
        logger.debug('Error thrown while processing admin login')
        if isinstance(exc, ValidationError):
            logger.debug(f'Validation error: {exc.detail}')
            logger.debug('Sending response')
            return Response(exc.detail, exc.status_code)
        if isinstance(exc, Users.DoesNotExist):  # todo:  inspect exception paras
            logger.debug('Query error: user not found')
            logger.debug('Sending response')
            return Response(
                {'message': 'User not found'},
                status.HTTP_401_UNAUTHORIZED
            )
        if isinstance(exc, Users.MultipleObjectsReturned):  # todo: inspect exception paras
            logger.error('Query error: login is not unique')
            logger.debug('Sending response')
            return Response(
                {'message': 'Login is not unique'},
                status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        logger.debug('Ended possible exceptions, delegating to default handler')
        super().handle_exception(exc)

    @swagger_auto_schema(
        request_body=LoginSerializer,
        operation_summary='Точка входа администраторов',
        tags=['Authentication'],
        security=[],
        responses={
            '401': errorResponse,
            '400': errorResponse,
            '500': errorResponse,
        }
    )
    def post(self, request: Request) -> Response:
        """Метод входа администраторов в систему"""
        logger.debug('Starting to process admin login')
        ser = LoginSerializer(data=request.data)
        logger.debug(f'Created serializer from request data: {ser}')
        logger.debug('Starting to validate login data')
        ser.is_valid(raise_exception=True)
        logger.debug('Login data validated successfuly')
        data = ser.validated_data
        logger.debug(f'Validated data: {data}')
        logger.debug('Starting to retrieve user by login')
        user = Users.objects.get(user_login=data['login'])
        logger.debug(f'Found user: {user}')
        logger.debug('Starting to verify password')
        if not verify_password(data['password'], user.user_pass):
            logger.debug('Verification failed')
            logger.debug('Sending response')
            return Response(
                {'message': 'Incorrect password'},
                status.HTTP_401_UNAUTHORIZED,
            )
        logger.debug('Verification passed')
        logger.debug('Calling for authorisation service for tokens')
        #   call authorisation service
        #   handle response
        #   return tokens
        return Response(ser.data, status.HTTP_202_ACCEPTED)

# todo: create abstuct class and sub class logins (admin, user) from it
