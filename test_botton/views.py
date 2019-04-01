from django.shortcuts import render
#from django.http import HttpResponse
#from django.template import loader

# Create your views here.
def some_view(request):
    message=''
    if request.method == 'POST':
        if 'button_1' in request.POST:
        # ボタン1がクリックされた場合の処理
            message = 'test 1 !!!'
        elif 'button_2' in request.POST:
        # ボタン2がクリックされた場合の処理
            message = "test 2 !"
    d ={
        'message' : message
        }
    return render(request, 'test_botton/some_view.html', d)
 #    return HttpResponse("Hello, world.")
