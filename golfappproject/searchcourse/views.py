from django.shortcuts import render
from django.http import HttpResponse
from .forms import CourseForm
import urllib.parse
import requests
import json

def search(request):
    my_dict = {
        'form': CourseForm(),
        'insert_forms': '初期値'
    }

    if (request.method == 'POST'):
        my_dict['insert_forms'] = '文字列:' + request.POST['course_name']
        my_dict['form'] = CourseForm(request.POST)

    return render(request,'searchcourse/search.html',my_dict)

def select(request):

    # コースが選択されていない or selectをもう一度開いたら戻る
    if len(request.POST)==0:
        return search(request)
    
    my_dict= {
        'course_name': request.POST['course_name'],
        'course_info': ""
    }
    # return render(request,'searchcourse/search.html',my_dict)

    # コース検索用URL作成
    url = 'https://app.rakuten.co.jp/services/api/Gora/GoraGolfCourseSearch/20170623'
    course_parm = {
        'format': 'json',
        'applicationId': '1056265260001309349',
        'keyword': request.POST['course_name']
    }
    gene_param = urllib.parse.urlencode(course_parm)

    # コース情報の取得
    course_info = requests.get(f'{url}?{gene_param}')
    json_dict = course_info.json()

    print(json_dict['Items'][0]['Item']['golfCourseId'])

    course_id=json_dict['Items'][0]['Item']['golfCourseId']


    my_dict['course_info'] = json_dict['count']

    course_detail_url = "https://booking.gora.golf.rakuten.co.jp/guide/course_info/disp/c_id/{}?l-id=gr_cg_courseinfo_menu".format(course_id)

    print(course_detail_url)
    


    
    return render(request,'searchcourse/select.html',my_dict)