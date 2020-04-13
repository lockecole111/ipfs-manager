from django.shortcuts import render
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET, require_POST
from django.http import JsonResponse
from ipfs.models import User,File
from django.contrib.auth import (login as django_login, logout as django_logout, authenticate)
# Create your views here.
def make_api_response(data, status=200):
    resp = JsonResponse(data={'data':data}, status=status)
    resp['Access-Control-Allow-Origin'] = '*'
    resp['Access-Control-Allow-Methods'] = 'POST'
    resp['Access-Control-Allow-Headers'] = 'Authorization'
    resp['Content-Type'] = 'application/json; charset=utf-8'
    return resp

@require_POST
@csrf_exempt
def register(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    if not all([username, password]):
        return make_api_response("Missing Parameter.", 422)
    try:
        User.objects.get(username=username)
        return make_api_response("Username exist, please change.", 409)
    except User.DoesNotExist:
        User.objects.create_user(username=username, password=password)
        return make_api_response("Register success.")

@require_POST
@csrf_exempt
def login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    if not all([username, password]):
        return make_api_response("Missing Parameter.", 422)

    user = authenticate(request, username=username, password=password)
    if not user:
        return make_api_response("Login failed.", 401)
    else:
        django_login(request,user)
        return make_api_response("Login success.")

@require_POST
@csrf_exempt
def add(request):
    user = request.user
    if not user:
        return make_api_response("Please Login.", 401)   
    name = request.POST.get('name')
    hash = request.POST.get('hash')
    size = request.POST.get('size')
    if not all([name, hash, size]):
        return make_api_response("Missing Parameter.", 422)
    if File.objects.filter(hash=hash, user=user).exists():
        return make_api_response("File exist.", 409)
    request_file = File()
    request_file.name = name
    request_file.size = size
    request_file.hash = hash
    request_file.user = user
    request_file.save()
    return make_api_response("Add success.")

@require_POST
@csrf_exempt
def delete(request):
    user = request.user
    if not user:
        return make_api_response("Please Login.", 401)   
    hash = request.POST.get('hash')
    if not hash:
        return make_api_response("Missing Parameter.", 422)
    try:
        request_file = File.objects.get(hash=hash)
    except File.DoesNotExist:
        return make_api_response("file not found.", 404)
    request_file.delete()
    return make_api_response("Delete success.")

@require_GET
@csrf_exempt
def list_files(request):
    user = request.user
    if not user:
        return make_api_response("Please Login.", 401)
    files = File.objects.filter(user=user).order_by('-id')
    res = []
    for item in files:
        res.append({'name':item.name, 'hash':item.hash, 'time':item.time.timestamp(), 'size':item.size})
    return make_api_response(res)



