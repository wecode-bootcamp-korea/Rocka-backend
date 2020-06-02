import json
import bcrypt
import jwt

from django.views import  View
from django.http import HttpResponse, JsonResponse

from .models import Member, Gender, ShippingAddress
from laka.settings import SECRET_KEY

class SignUpView(View):
    def post(self, request):
        signup_data = json.loads(request.body)

        try:
            if Member.objects.filter(nickname=signup_data['nickname']).exists():
                return HttpResponse(status=401)

            password = signup_data['password'].encode('utf-8')

            password_encrypt = bcrypt.hashpw(password, bcrypt.gensalt())
            password_encrypt = password_encrypt.decode('utf-8')

            gender = Gender.objects.get(name=signup_data['gender'])
            Member(
                nickname        = signup_data['nickname'],
                password        = password_encrypt,
                fullname        = signup_data['fullname'],
                email           = signup_data['email'],
                phone_number    = signup_data['phone_number'],
                gender          = gender,
            ).save()

            return HttpResponse(status=200)

        except KeyError:
            return JsonResponse({"message":"INVALID_KEYS"}, status=400)

class SignInView(View):
    def post(self, request):
        signin_data = json.loads(request.body)

        try:
            if Member.objects.filter(nickname=signin_data['nickname']).exists():
                user = Member.objects.get(nickname=signin_data['nickname'])

                if bcrypt.checkpw(signin_data['password'].encode('utf-8'), user.password.encode('utf-8')):
                    token = jwt.encode({'nickname':signin_data['nickname']}, SECRET_KEY, algorithm = "HS256")
                    token = token.decode('utf-8')

                    return JsonResponse({"token":token}, status=200)

                else:
                    return HttpResponse(status=401)

            return HttpResponse(status=400)

        except KeyError:
            return JsonResponse({"message":"INVALID_KEYS"}, status=400)

class TokenCheckView(View):
    def post(self, request):
        data = json.loads(request.body)

        token_info = jwt.decode(data['token'], SECRET_KEY, algorithm = 'HS256')

        if Member.objects.filter(nickname=token_info['nickname']).exists():
            return HttpResponse(status=200)

        return HttpResponse(status=403)

