from django.shortcuts import render

# Create your views here.

def view1(request):
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
    return render(request, 'screen_split/some_view.html', d)
#    return HttpResponse("Hello, world.")

def view2(request):
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
    return render(request, 'screen_split/some_view.html', d)

def view_over(request):
    return render(request, 'screen_split/view_over.html')
