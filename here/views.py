from django.shortcuts import render


def index(request):
    context = {}
    return render(request, 'here/checkin.html', context)


def quick_checkin(request):
    context = {}
    return render(request, 'here/quick.html', context)
    