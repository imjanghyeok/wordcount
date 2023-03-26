from django.shortcuts import render


# Create your views here.
def main(request):
    return render(request,'main.html')

def about(request):
    return render(request,'about.html')    

def result(request):
    if request.method == 'GET': 
        text = request.GET['text']
        text_list = text.split()
        text_dict = {}
        for word in text_list:
            if word in text_dict:
                text_dict[word] +=1
            else:
                text_dict[word] = 1
        return render(request,'result.html',{'words':text_dict.items()})
    elif request.POST['sequence'] == "ascending_key": 
        text = request.GET['text']
        text_list = text.split()
        text_dict = {}
        for word in text_list:
            if word in text_dict:
                text_dict[word] +=1
            else:
                text_dict[word] = 1
        words = sorted(text_dict.items(), key=lambda x:x[0], reverse=False)
        return render(request,'result.html',{'words':words})
    elif request.POST['sequence'] == "descending_key":
        text = request.GET['text']
        text_list = text.split()
        text_dict = {}
        for word in text_list:
            if word in text_dict:
                text_dict[word] +=1
            else:
                text_dict[word] = 1
        words = sorted(text_dict.items(), key=lambda x:x[0], reverse=True)
        return render(request,'result.html',{'words':words})
    elif request.POST['sequence'] == "ascending_value":
        text = request.GET['text']
        text_list = text.split()
        text_dict = {}
        for word in text_list:
            if word in text_dict:
                text_dict[word] +=1
            else:
                text_dict[word] = 1
        words = sorted(text_dict.items(), key=lambda x:x[1], reverse=False)
        return render(request,'result.html',{'words':words})
    elif request.POST['sequence'] == "descending_value":
        text = request.GET['text']
        text_list = text.split()
        text_dict = {}
        for word in text_list:
            if word in text_dict:
                text_dict[word] +=1
            else:
                text_dict[word] = 1
        words = sorted(text_dict.items(), key=lambda x:x[1], reverse=True)
        return render(request,'result.html',{'words':words})
    
    
    