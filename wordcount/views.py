from django.shortcuts import render
import operator

def homepage(request):
    return render(request, 'homepage.html')

def count(request):
    fulltext = request.GET['fulltext']
    splittedtext = fulltext.split()
    countdictionary = {}
    for word in splittedtext:
        if word in countdictionary:
            countdictionary[word] += 1
        else:
            countdictionary[word] = 1
    sortedlist = sorted(countdictionary.items(), key=operator.itemgetter(1))
    sortedlist.reverse()
    return render(request, 'count.html', {'fulltext': fulltext, 'count': len(splittedtext), 'sortedlist': sortedlist})

def about(request):
    return render(request, 'about.html')