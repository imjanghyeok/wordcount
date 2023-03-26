from django.shortcuts import render


# Create your views here.
def main(request):
    return render(request,'main.html')

def about(request):
    return render(request,'about.html')    

def result(request):
    
    sequence=request.GET.get('sequence')
    
    if not sequence: 
        text = request.GET.get('text')
        global text_dict
        global text_list
        text_list = text.split()
        text_dict = {}
        for word in text_list:
            if word in text_dict:
                text_dict[word] +=1
            else:
                text_dict[word] = 1
        return render(request,'result.html',{'words':text_dict.items()})
    else:
        if request.GET['sequence'] == "ascending_key": 
            words = sorted(text_dict.items(), key=lambda x:x[0], reverse=False)
            return render(request,'result.html',{'words':words})
        elif request.GET['sequence'] == "descending_key":
            words = sorted(text_dict.items(), key=lambda x:x[0], reverse=True)
            return render(request,'result.html',{'words':words})
        elif request.GET['sequence'] == "ascending_value":
            words = sorted(text_dict.items(), key=lambda x:x[1], reverse=False)
            return render(request,'result.html',{'words':words})
        elif request.GET['sequence'] == "descending_value":
            words = sorted(text_dict.items(), key=lambda x:x[1], reverse=True)
            return render(request,'result.html',{'words':words})
    
    
    