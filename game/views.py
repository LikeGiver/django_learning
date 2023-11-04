from django.http import HttpResponse


def index(request):
    line1 = '<h1 style="text-align: center">我的第一个网页</h1>'
    line2 = '<img src="https://i2.hdslb.com/bfs/archive/158e0e4a7df2c4d2baa9d71e9b675f1abc82dd6d.jpg@672w_378h_1c_!web-home-common-cover.avif">'
    return HttpResponse(line1+line2)
