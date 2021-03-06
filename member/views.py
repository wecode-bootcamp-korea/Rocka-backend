import json
import bcrypt
import jwt

from django.views import  View
from django.http import HttpResponse, JsonResponse

from .models import Member, Gender, ShippingAddress
from laka.settings import SECRET_KEY

class LoginConfirm:
	def __init__(self,original_function):
		self.original_function = original_function

	def __call__(self, request, *args, **kwargs):
		token = request.headers.get("Authorization", None)
		try:
			if token:
				token_payload	= jwt.decode(token, SECRET_KEY, algorithms="HS256")
				user			= Member.objects.get(nickname=token_payload['nickname'])
				request.user	= user
				return self.original_function(self, request, *args, **kwargs)

			return JsonResponse({'message':'INVALID_USER'}, status=401)

		except jwt.DecodeError:
			return JsonResponse({'message':'INVALID_TOKEN'}, status=401)

		except Member.DoesNotExist:
			return JsonResponse({'message':'INVALID_USER'}, status=401)

class SignUpView(View):
    def post(self, request):
        signup_data = json.loads(request.body)

        try:
            if Member.objects.filter(nickname=signup_data['nickname']).exists():
                return HttpResponse(status=401)

            password = signup_data['password'].encode('utf-8')

            password_encrypt = bcrypt.hashpw(password, bcrypt.gensalt())
            password_encrypt = password_encrypt.decode('utf-8')

            gender = Gender.objects.get(id=signup_data['gender']).id
            Member(
                nickname        = signup_data['nickname'],
                password        = password_encrypt,
                fullname        = signup_data['fullname'],
                email           = signup_data['email'],
                address         = signup_data['address'],
                phone_number    = signup_data['phone_number'],
                gender_id       = gender,
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

