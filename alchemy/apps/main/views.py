from django.shortcuts import render

def start_main(request):
    return render(request,'index.html')