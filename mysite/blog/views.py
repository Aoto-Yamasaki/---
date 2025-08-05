from django.shortcuts import render,redirect
from django.http import HttpResponse

def step1_view(request):
    if request.method == 'POST':
        # 这里可以保存国籍和语言到 session 或数据库
        request.session['nationality'] = request.POST.get('nationality')
        request.session['language'] = request.POST.get('language')
        return redirect('step2')
    return render(request, 'blog/step1.html')

def step2_view(request):
    if request.method == 'POST':
        # 可以获取全部用户数据了
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        region = request.POST.get('region')

        nationality = request.session.get('nationality')
        language = request.session.get('language')

        # 这里可以保存数据，或做后续处理
        # return render(request, 'result.html', {
        #     'nationality': nationality,
        #     'language': language,
        #     'age': age,
        #     'gender': gender,
        #     'region': region
        # })
    
        return redirect('questionnaire')  # ← 改为跳转问卷页面
    return render(request, 'blog/step2.html')

def questionnaire_view(request):
    if request.method == 'POST':
        answer = request.POST.get('answer')
        # 可保存问卷答案
        return render(request, 'thanks.html', {'answer': answer})
    return render(request, 'blog/questionnaire.html')
# blog/questionnaire.html记得前面加一个blog
def home(request):
    return render(request, 'blog/home.html')
# Create your views here.

#TODO：ページ遷移の細かい処理の記述
import requests

def result_view(request):
    tab_list = [
    ('earthquake', '防災 地震'),
    ('tsunami',     '津波 グッズ'),
    ('eruption',    '火山 避難'),
    ('stockpile',   '防災 備蓄品'),
    ('landslide',   '土砂災害 グッズ'),
    ]

    api_url = 'https://app.rakuten.co.jp/services/api/IchibaItem/Search/20220601'
    application_id = '1038808457986695199'

    all_products = {}
    for tab_key, keyword in tab_list:
        params = {
            'applicationId': application_id,
            'keyword': keyword,
            'hits': 4,
        }
        res = requests.get(api_url, params=params)
        items = res.json().get('Items', [])
        products = []
        for item in items:
            data = item['Item']
            products.append({
                'img': data['mediumImageUrls'][0]['imageUrl'],
                'url': data['itemUrl'],
                'name': data['itemName'],
            })
        all_products[tab_key] = products

    current_tab = request.GET.get('tab', 'earthquake')
    products = all_products.get(current_tab, [])

    context = {
    'all_products': all_products,
    'current_tab': current_tab,
    'products': products,   # テンプレの for 用（JSだけで良ければ無くてもOK）
    }
    return render(request, 'blog/result.html', context)


