# Bixbar
> **Notion** : https://www.notion.so/ccookncook/Bixbar-b5401104a0d64fdc838d27505fbf27b2<br/>
  **Todo** : https://www.notion.so/e22d389dddc04614a970bdd6ab76b43e?v=d27a9f78c04f42d5938b95431c942317<br/>
  **Google Drive** : https://drive.google.com/drive/folders/1sxu2eGAEShhobkIA0Yb8Y_naYrI2JI9L
  
- **[Bixbar](https://github.com/kordood/Bixbar/tree/master/Bixbar)**
  - Server
- **[ccookncook.bixbar](https://github.com/kordood/Bixbar/tree/master/ccookncook.bixbar)**
  - Bixby
- **[Crawling](https://github.com/kordood/Bixbar/tree/master/crawling)**
  - Crawling

# URLs
Notion : [www.Bixbar.com](http://www.Bixbar.com)

cocktail : [http://www.bixbar.com/cocktail/?q=](http://www.bixbar.com/cocktail/?q=)

liquor : [http://www.bixbar.com/liquor/?q=](http://www.bixbar.com/liquor/?q=)

base : [http://www.bixbar.com/base/?q=](http://www.bixbar.com/base/?q=cognac)

getfood : [http://www.bixbar.com/getfood/?q=](http://www.bixbar.com/getfood/?q=cognac)

<br/>

# Bixbar Interface
![제목 없음-2 복사](https://user-images.githubusercontent.com/28800101/85257078-2fec3e00-b4a0-11ea-8c1d-b3540ba630f2.png)

<br/>

# 주요기능

- **칵테일 제조법 전달**

  - 레시피와 재료 등의 정보를 제공

- **베이스를 이용한 칵테일 검색**

  - 해당 베이스가 들어가는 칵테일 리스트 

- **칵테일에 어울리는 안주 추천**

  - 칵테일-안주 페어링 정보에서 가장 높은 정확도를 보이는 안주 추천

- **사용자 맞춤 칵테일 추천**

  - 사용자의 연령대, 성별 및 기본 취향을 수집하여 정확한 사용자 맞춤 추천
  
<br/>

# About Project

> 숭실대학교 소프트웨어학부 2019-2 ~ 2020-1 캡스톤디자인종합프로젝트

<br/>

# 팀 구성

- **[박정아](http://github.com/co3oing)**
  - Database 설계 및 구축, Data 삽입 및 조회 구현
- **[송혜령](http://github.com/HyeRyeongSong)**
  - 크롤링, 크롤링한 Data를 JSON 파일로 파싱
- **[임규형](http://github.com/GyuHyoung)**
  - Bixby NLP Training, 캡슐 설계, Modeling구현, 디자인, 웹서버와의 통신 구현
- **[최민성](http://github.com/kordood)**
  - Django 웹서버 구축, Bixby와의 통신(Response) 구현
  
 <br/>
 
# Project Architecture
- **시스템 대블록 설계**

![Untitled4](https://user-images.githubusercontent.com/28800101/84741780-86fa9a80-afea-11ea-9395-e4caf4ef2994.png)

- **Database**

![Untitled5](https://user-images.githubusercontent.com/28800101/84741783-86fa9a80-afea-11ea-89e2-1c7763c18c66.png)

- **Flow Chart**

![Bixby_FlowChart0](https://user-images.githubusercontent.com/28800101/84741784-87933100-afea-11ea-9792-230548c76ac6.png)

<br/>

# 개발환경

- **Bixby**

  - Bixby Developer Studio
  - Javascript

- **Server & DB**

  - AWS
  - AWS Personalize
  - Django
  - Python 3.7
  - SQLite

- **Crawling**

  - Jupyter Notebook
  - Python 3.7
  - [liquor.com](http://liquor.com/)
  - [Instagram](https://www.instagram.com/)
