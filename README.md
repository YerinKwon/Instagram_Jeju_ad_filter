# Instagram_Jeju_ad_filter
## Introduction
오늘날의 인스타그램은 사람들이 여행 관련 정보를 찾아보는 대표적인 수단 중 하나이다. 검색하고 싶은 태그를 입력하면 게시글에 해당 태그나 위치정보가 부착된 게시글을 찾아주기 때문에 유용하기 때문이다. 하지만 영향력이 큰 만큼 수많은 이해관계자들이 이를 악용하여 광고 효과를 얻고 있다. 예를 들어, 운동보조제 광고글에 유명 관광지 태그를 부착하거나 숙박업체나 지역 요식업체에서도 홍보를 위해 다량의 게시글을 올리는 식이다. 이렇게 다량의 광고성 게시글 때문에 실제 정보를 얻고자 하는 사람들은 정확한 정보를 얻기 어렵다. 따라서, 이번 프로젝트에서는 인스타그램에서 #jeju 태그를 검색했을 때 나타나는 게시글 데이터를 바탕으로 naive bayse를 이용하여 이를 여행과 무관한 광고글과 여행과 관련된 광고글, 그리고 비광고글 세 가지로 분류해보았다.

## Data Collection
selenium과 chrome driver를 이용한 웹 크롤러로 게시글을 수집했다. (instagram_crawler.py)
![sample1](./img/Data_Collection.png)

## Preprocessing
한글, 영어, 숫자를 제외한 모든 언어와 이모티콘, 특수문자, html 태그 등을 공백으로 치환했다.
![sample2](./img/Preprocessing.png)

## Tagging
다음과 같이 학습용 데이터를 태깅했다.
> 0: 광고가 아닌 모든 게시글(여행 후기, 일상, 투어)
 
> 1: 제주 여행과 관련이 없는 광고 - 주로 소재지만 제주인 경우 (타투가게, 네일아트 등)

> 2: 제주 여행과 관련이 있는 광고 (민박, 게스트하우스, 스쿠버다이빙, 카페 등)

## Tokenizing
Konlpy의 Okt 모듈을 이용해 형태소로 토큰화했다.

## Probability Calculation
Naive Bayes로 각 집단별 토큰이 등장할 확률을 구하고 로그를 취했다. 집단별 Top 5 토큰은 다음과 같다.
![sample3](./img/Probability_Calculation.png)

## Test
트레이닝 데이터와 마찬가지로 토큰화하고 게시글의 각 토큰이 세 집단에서 등장할 확률을 각각 계산했다. 한 게시글의 모든 토큰에 대해 세 집단 각각에서 등장할 확률을 구한 뒤, 그 합이 가장 높은 집단을 해당 게시글의 집단으로 분류했다.

## Result
![sample4](./img/result_ads.png)
![sample5](./img/result_nonads.png)
![sample6](./img/result_semiads.png)
