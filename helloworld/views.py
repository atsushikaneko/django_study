from django.shortcuts import render

 # templatesディレクトリ内のhelloworld/index.htmlを呼び出し
def index(request):
    return render(request, 'helloworld/index.html')