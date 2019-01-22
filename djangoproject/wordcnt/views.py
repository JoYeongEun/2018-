from django.shortcuts import render

# Create your views here.
def home(reqeust):
    return render(reqeust,'home.html')

def about(reqeust):
    return render(reqeust,'about.html')

def result(reqeust):
    text = reqeust.GET['fulltext']
    words = text.split()

    word_dictionary = {}

    for word in words:
        if word in word_dictionary:
            word_dictionary[word]+=1
        else :
            word_dictionary[word]=1

    return render(reqeust,'result.html',{'full':text,'total':len(nouns),'dictionary':word_dictionary.items()})