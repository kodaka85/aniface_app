from django.shortcuts import render, redirect
from PIL import Image
import numpy as np
import base64
import tensorflow as tf
import os

#学習モデルのロード
from tensorflow.keras.models import load_model
current_dir = os.getcwd()
model_path = current_dir + '\\model\\ani_predict.hdf5'
model = load_model(model_path)




from django.core.files.storage import FileSystemStorage

def fileupload(request):
　  if request.method == 'POST' and request.FILES['htmlfile']:
        htmlfile = request.FILES['htmlfile']
        fileobject = FileSystemStorage()
        filedata = fileobject.save(htmlfile.name, htmlfile )
        upload_url = fileobject.url(data)
        return render(request, 'upload.html')
    return render(request, 'upload.html')


def upload(request):
      
    #画像データの取得
    pic = request.FILES['picture']

    #簡易エラーチェック（拡張子）
    root, ext = os.path.splitext(pic.name)
    if ext != '.png':
        message ="【ERROR】png以外の拡張子ファイルが指定されています。"
        return render(request, 'index.html', {
                "message": message,
                })


    if request.method =='POST':
        result=[]　#(入力画像,キャラ名)
        label=[]
        img = Image.open(pic)
        img = img.resize((150, 150))
        img = image.img_to_array(img)
        img = np.expand_dims(x, axis=0)
        classified = anime(img)
        label.append(classified) #キャラ名
        
         #入力画像とキャラ名をまとめて格納→入力画像でなく、推測したキャラの画像を表示したい。

        feature[0,i] = classified
        if anime.features[0,i]== 1:
            src = Image.open('./aniface/character_img/'+str(i))
            src = base64.b64encode(src)
            src = str(src)[2:-1]
            result.append((src, label))]


        context = {
            'result': result,
        }
        return render(request, 'result.html', context)
    
    else:
        return redirect('index')


def anime(input):
    categories = []
    #予測
    features = model.predict(img)
    #features[0,i] if features[0,i]==1: return categories[i]
    #予測結果によって処理を分ける
    if features[0,0] == 1:
        return "選ばれたのは、shanaでした。"

    elif features[0,1] == 1:
        return "選ばれたのは、haruhiでした。"

    else:
        return "選ばれたのは、hatsuneでした。"
    