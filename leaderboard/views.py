from unicodedata import name
from django.shortcuts import render
from leaderboard.models import results
import json

# Create your views here.
def home(request):
    file = open('C:\\Users\Dodzi\\Downloads\\django-json-project\\django-json-project\\leaderboardApp\\leaderboard\\leaderboard.json','r')
    x=file.read()
    data_json = json.loads(x)

    data_dict = {}
    for data in data_json['students']:
        data_dict[data['name']] = data['points']

    # print(data_dict)

    ascending_sorted_scores = sorted(data_dict.items(), key=lambda x:x[1])
    descending_sorted_scores = sorted(data_dict.items(), key=lambda x:x[1], reverse=True)

    ascending_names = []
    ascending_points = []
    descending_names=[]
    descending_points=[]
    x = []
    i=1
    for key,value in ascending_sorted_scores:
        ascending_names.append(key)
        ascending_points.append(value)
        x.append(i)
        i += 1

    ascending_mylist = zip(x, ascending_names, ascending_points)

    for key, value in descending_sorted_scores:
        descending_names.append(key)
        descending_points.append(value)

    descending_mylist = zip(x, descending_names, descending_points)

    data = {
        "ascending_mylist": ascending_mylist,
        "descending_mylist": descending_mylist
    }

    return render(request, 'index.html', data)

# Insert data into database
def insertData(request):
    file = open('C:\\Users\\Dodzi\\Downloads\\django-json-project\\django-json-project\\leaderboardApp\\leaderboard\\leaderboard.json','r')
    x=file.read()
    data_json = json.loads(x)

    data_dict = {}
    for data in data_json['students']:
        data_dict[data['name']] = data['points']

    # print(data_dict)

    ascending_sorted_scores = sorted(data_dict.items(), key=lambda x:x[1])
    descending_sorted_scores = sorted(data_dict.items(), key=lambda x:x[1], reverse=True)

    ascending_names = []
    ascending_points = []
    descending_names=[]
    descending_points=[]
    x = []
    i=1
    for key,value in ascending_sorted_scores:
        ascending_names.append(key)
        ascending_points.append(value)
        x.append(i)
        i += 1

    ascending_mylist = zip(x, ascending_names, ascending_points)

    for key, value in descending_sorted_scores:
        descending_names.append(key)
        descending_points.append(value)

    descending_mylist = zip(x, descending_names, descending_points)

    data={
        "ascending_mylist": ascending_mylist,
        "descending_mylist": descending_mylist,
        "dataSave":"",
        "fetchdata":"",
    }
    if request.method == "POST":
        rank = request.POST.get('rank')
        name = request.POST.get('name')
        point = request.POST.get('point')

        fetchdata = results.objects.filter(rank=rank, name=name, points=point)
        already_saved = "no"
        for n in fetchdata:
            if(n != ""):
                already_saved = "yes"
                data['dataSave'] = "yes"
        try:
            if already_saved != "yes":
                en = results(rank=rank,name=name,points=point)
                en.save()
                data['dataSave'] = "no"

            fetchdata = results.objects.all()
            data['fetchdata'] = fetchdata
            return render(request, "index.html",data)
        except:
            fetchdata = results.objects.all()
            data['fetchdata'] = fetchdata
            data['dataSave'] = "error"
            return render(request, "index.html",data)

    return render(request, "index.html")


def savedRecord(request):
    fetchdata = results.objects.all()
    data={
        "fetchdata":fetchdata
    }
    return render(request, "saved-record.html",data)


def edit(request):
    if request.method == "POST":
        id = request.POST.get('id')
        rank = request.POST.get('rank')
        name = request.POST.get('name')
        point = request.POST.get('point')

        results.objects.filter(id=id).update(rank=rank,name=name,points=point)

    fetchdata = results.objects.all()
    data={
        "fetchdata":fetchdata
    }
    return render(request, "saved-record.html",data)


def delete(request):
    if request.method == "POST":
        id = request.POST.get('id')
        results.objects.filter(id=id).delete()

    fetchdata = results.objects.all()
    data={
        "fetchdata":fetchdata
    }
    return render(request, "saved-record.html",data)