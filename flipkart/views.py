from django.shortcuts import render


def asus(request):
    asus={'brand':'ASUS','model': 'VIVOBOOK 15 PRO', 'processor': 'RYZEN 7', 'gpu':'RTX 3050TI','cost':'1,40,000'}
    return render(request,'flipkart.html',asus)