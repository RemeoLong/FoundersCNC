from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def home(request):
    return render(request, 'index/index.html', {})


def weatherford_performance_test(request):
    return render(request, 'index/weatherford_performance_test.html', {})


def weatherford_test_stand(request):
    return render(request, 'index/weatherford_test_stand.html', {})


def tool_changer(request):
    return render(request, 'index/tool_changer.html', {})


def present(request):
    return render(request, 'index/present.html', {})


def db(request):
    return render(request, 'index/DB.html', {})
