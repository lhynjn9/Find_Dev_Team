# 프로젝트 팀을 찾는 사이트(가제)

### 🚀 프로젝트 소개

- 진행 일정 : 22.06.13 ~ 22.06.

- 팀원

| 이름   | 담당 영역 | Github                        |
| ------ | --------- | ----------------------------- |
| 박시원 |           | https://github.com/siwon-park |
| 이현정 |           | https://github.com/lhynjn9    |

- 목표
  - 사용자가 등록한 개발 역량 표시
  - 팀 구성을 위한 이메일/메시지/DM 기능
  - HTML, CSS, JavaScript, Bootstrap, Vue.js, REST API, Database 등을 활용한 실제 서비스 설계
  - SSAFY 7기 배포
    - 피드백 점검
    - 서비스 관리 및 유지 보수
- 기획 의도
  - 프로젝트 팀을 찾기 위한 개발자 정보 제공 프로젝트
  - 나의 개발 능력을 나타내고 팀의 역량을 드러내어 쌍방으로 소통할 수 있는 사이트
  - 본인의 개발 역량 정보를 제공하고 다른 사람들의 개발 역량 정보를 확인하여 프로젝트 팀 구성에 도움을 주기 위한 프로젝트



### 🛠Tech Stack

![image](https://user-images.githubusercontent.com/93081720/170559780-a977ed18-e589-4ffd-bb49-2f24d92cdeac.png)



### 🎶기획 단계

- 기능 명세서

  ![unknown](https://user-images.githubusercontent.com/97647987/175548098-779d3e75-143a-4db8-b2fd-9710ecc7c9de.png)

  

- 데이터베이스 모델링(ERD)

  ![image-20220609215301830](https://user-images.githubusercontent.com/97647987/174428289-757c5b86-5a74-4b5b-90b8-c9d70002f214.png)

- 컴포넌트 설계

  ![unknown](https://user-images.githubusercontent.com/97647987/175553416-599fdf93-07fd-4e87-a7f0-0a17cf294698.png)

  

- 서비스 플로우 차트

  ![unknown](https://user-images.githubusercontent.com/97647987/175549772-ef0490ac-26bf-4b1b-aeb8-245ecb88a258.png)

  

### 🛺 프로젝트 파일 구조

### 🔎구현 서비스

![unknown](https://user-images.githubusercontent.com/97647987/175561760-b65f80c5-90d7-494e-8634-50c132bab463.png)



### 🚔 프로젝트 회고

- 배운점

  | NO.  | Content                                                      |
  | ---- | ------------------------------------------------------------ |
  | 1    | - OneToOneField : 1:1 외래키 관계 설정                       |
  | 2    | 1. 기본 재정의 : adapter 정보 : 정보 저장용<br />2. 회원 가입 필드는 회원가입에 들어가야 하는 필드만 받아 올 수 있게 새로 serializer 정의(Register serializer 사용)<br />3. static, media file의 차이점<br />- static : 개발자가 준비해놓은 파일<br />- media : 사용자가 업로드한 파일 |
  | 3    | - Related Manager is not Iterable; 예) team.team_member는 related manager이기 떄문에 for 구문으로 반복이 불가능하다. |
  | 4    | - Related Manager와 같은 쿼리셋에는 인스턴스를 넣어야만 한다. 딕셔너리의 출력형태가 인스턴스와 똑같이 생겼다고해서 딕셔너리를 넣을 수는 없다(TypeError발생) |
  |      |                                                              |

  


- 이슈관리

  | No.  | Name | Content                                                      | Solve                            | follow-up |
  | ---- | ---- | ------------------------------------------------------------ | -------------------------------- | --------- |
  | 1    |      | print(team.team_member) = accounts.User.None                 | ??어케함?? 도대체 왜?.? Why not? |           |
  | 2    |      | team 수정에서 팀 맴버에 다른 유저 추가할 시, DB에 데이터가 들어가지 않음 | Yes                              |           |
  |      |      |                                                              |                                  |           |
  |      |      |                                                              |                                  |           |
  |      |      |                                                              |                                  |           |

  

- 느낀점

- 성과

