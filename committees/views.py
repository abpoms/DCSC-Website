from django.shortcuts import render


def index(request):
    context = {}
    return render(request, 'committees/index.html', context)


def detail(request, committee_abbreviation):
    context = {}
    return render(request, 'committees/detail.html', context)
