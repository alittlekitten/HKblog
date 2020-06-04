from django.shortcuts import render, redirect# 16번쨰 줄 쓰기 위해 추가 그동안은 render만 쓰다가.
from .models import Cafe # 10번째줄에 Cafe쓰기 위해서 model안에서 여기로 가져와준거!

def index(request):
    return render(request, 'index.html')

def create(request):
    return render(request, 'create.html')

def create_pro(request):
    cafe_product = Cafe()#create에서 입력한 값이 상품명 안으로 들어가는 것을 구현!
    cafe_product.product_name = request.GET['product_name']#request에서 받은 것을 #뒤에있는건 html의 화면에서 이름 거기 적은걸 끌어온다는 걸 구현
    cafe_product.product_price = request.GET['product_price']#이제 아래부터 아까 migraitons로 orm거쳐 만든 열에대해서 받아온 각 객체를 행으로 넣는게 아래!
    cafe_product.save()#위의 기능의 쿼리셋 메소드 사용.
    #url명 안에 들어있는거 가져오기 위해 render는 템플릿 불러오고 redirect는 url명 가져오는 것 사용 index로 넘어가게 된다.
    return redirect('index')

def show(request):#db에 있는걸 여기에 보여줘야 목록이 뜸! product부터
    products = Cafe.objects#model의 Cafe의 객체(받은것들을)를 가져와서 쿼리셋 형태로 만들어줌. 그걸 가져온것 리스트형태..?안에 딕셔너리 개별! 이걸 각각 아래의 형태로 출력
    return render(request, 'show.html', {'products':products})#뭐를 가지고 넘어갈건지가 3번쨰! key값은 뭐로 받을지 그냥 선언한거 뒤의 값이랑 다름
    #cr - index create createpro show까지 작업한것 앞으로 ud구현해야함!

def updateSearch(request):
    return render(request, 'updateSearch.html')

def search(request):#db에서 가져와서 일치하는 것 찾아서 띄우기. 쿼리셋 메소드 사용 all다음
    product = Cafe.objects.filter(product_name = request.GET['product_name']) #object까지가 쿼리셋 filter는 쿼리셋 메소드 해서 updateSearch하는거에서 업데이트서치이름을 가져온것. 뒤는 위의 get과 마찬가지 인데, 여기서 =이 진짜 ==의 같다의 의미로 사용된거만 바뀜(위는 대입) 그래서 필터검색인것! 사용
    return render(request, 'update.html', {'product':product[0]})#이 product는 쿼리셋인데, 리스트형태임. 위의 메소드중 위에서 썻던 GET의 경우는 하나만, filter는 객체의 모든 것을 가져오므로 그래서 하나로 특정하기 위해 0을 써준것 그리고 위처럼 모든걸 가져올 필요가 없으니 한정해준것(위의 products와 구분)

def update(request):#수정과정, but 아메리카노를 db에서 가져와서 그 정보를 에스프레소로 바꾸어주어야! 그러면 아메리카노를 가져와야함 이게 updatehtml에 59번째줄!
    product = Cafe.objects.filter(pk=request.GET['product_id'])[0] #0이 왜붙지? #pk는 db에있는 id 0001에 있는 그거 가져와서 아까 2가지만 넘겼으면 못쓸텐데 다 넘기고 히든해준것! productid는 히든에서 가져왔고. 그걸 가져와서 수정하는것. 굳이 보일필요 없으니 안썻던거고 이거도 같다는 표시 =이
    product.product_name = request.GET['product_name']#수정해주는 과정 아메리카노의 이름을 수정해줌.
    product.product_price = request.GET['product_price']
    product.save()#덮어쓰기
    return redirect('index') #홈페이지로 돌아가기

def deleteSearch(request):
    return render(request, 'deleteSearch.html')

def find(request):#find 메소드 구현이라고 이야기함. 삭제할 상품명을 request로 받아옴! deleteSearch의 설정을통해
    products = Cafe.objects.filter(product_name__contains=request.GET['product_name'])#contains를 적어줘서 delete..에서 가져옴 그래서 products에 리스트형식저장
    product = []#빈리스트
    for i in products:
        product.append(i)#가져온 걸 하나씩 가져옴.

    return render(request, 'delete.html',{'products':product})#로보내줘야함 product에 담긴거를 저형태로 바꾸어서 delete.html로 보내줌.

def delete(request):
    check_list = request.GET.getlist('chk')
    product = Cafe.objects.filter(product_name__in=check_list)#그 리스트를 받아와서 리스트 안에 들어있는 product name들을 필터링. 쿼리셋 형태로 저장. 위의 contains는 포함하고 있니? 이고, 이거랑 조금 다름.
    product.delete()#그 받아온걸 지우는것
    return redirect('index')
