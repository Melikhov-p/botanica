from django.shortcuts import render

def main(request):
    return render(request, 'shop/main.html')


def contacts(request):
    return render(request, 'shop/contacts.html')
