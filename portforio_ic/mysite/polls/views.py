from django.shortcuts import render
from .forms import UploadForm
from .models import UploadImage
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .im import im_to_monokuro
from .facechecker import func_face_checker

# Create your views here.
def index(request):
    params = {
        'title': '人工知能で遊んでみよう',
        'upload_form': UploadForm(),
        'id': None,
    }
    return render(request, 'polls/index.html', params)

def monokuro(request):
    params = {
        'title': 'モノクロ化',
        'id': None,
        'url':None,
        'gray':None,
    }

    if (request.method == 'POST'):
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            upload_image = form.save()
            params['id'] = upload_image.id
            params['url'] = upload_image.image.url
            gray_image = im_to_monokuro(upload_image.image.url)
            params['gray'] = "/media/img/" + gray_image

    return render(request, 'polls/monokuro.html', params)

def face_checker(request):
    params = {
        'title': '顔認識',
    }
    return render(request, 'polls/face_checker.html', params)

def fc_result(request):
    params = {
        'title': '顔認識',
        'face':None,
        'number': "この画像に顔はありませんでした",
    }

    if (request.method == 'POST'):
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            upload_image = form.save()
            # params['id'] = upload_image.id
            # params['url'] = upload_image.image.url
            # gray_image = im_to_monokuro(upload_image.image.url)
            # params['gray'] = "/media/img/" + gray_image
            # print(gray_image)
            num = func_face_checker(upload_image.image.url)
            if num > 0:
                params['number'] = "この画像に、顔が"+str(num)+"件見つかりました"
            params['face'] = "/media/img/face_checker.png"

            image_id = upload_image.id
            # UploadImageのインスタンスを取得
            upload_image = get_object_or_404(UploadImage, id=image_id)
            
            # 画像ファイルの削除
            upload_image.image.delete()
            
            # レコードの削除
            upload_image.delete()

    return render(request, 'polls/fc_result.html', params)
