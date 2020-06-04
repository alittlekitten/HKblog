from django.db import models

class Cafe(models.Model):#상속
    product_name = models.CharField(max_length=20) #이름넣기 table에(class에) 넣을 요소들 만드는것! 지금 만든걸 migrations해야 sql의 시트의 열로 만듬
    product_price = models.IntegerField()
    # 여기에서 객체값(쿼리셋은) 장고에서 이미 만들어졌기에 과정 생략. 바로 그 객체에 값을 넣어준다고 이해. 상속받은 값(기존값)을 대입하는 기본문.

    
