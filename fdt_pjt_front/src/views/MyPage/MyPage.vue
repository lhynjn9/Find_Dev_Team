<template>
  <div>
    <div class="title">{{ this.currentUser.username }}님의 프로필 페이지</div>
    <div class="container">
      <!-- 사진 및 기본 정보  -->
      <div class="row">
        <div class="col d-flex">
          <div class="d-flex">
            <div class="circle" style="background-color: #c5af3d;">•</div>
            <div class="circle" style="background-color: #e3bfc8;">-</div>
            <div class="circle" style="background-color: #67769d;">+</div>
          </div>
          <div class="d-flex">
            <div class="rectangle" @click="goBack">X</div>
            <div class="arrow" @click="goBack">◀</div>
          </div>
        </div>
        <div class="first">
          이름 : {{ this.currentUser.username }}<br>
          성별 : {{ this.currentUser.sex }}<br>
          지역 : {{ this.currentUser.region }}<br>
          반 : {{ this.currentUser.group }}<br>
          포지션(B/F) : {{ this.currentUser.position }}<br>
          전공 : {{ this.currentUser.major }}
          소개 : {{ this.currentUser.intro }}<br>
          오픈 카카오 : {{ this.currentUser.kakao_chat }}<br>
          GitHub : {{ this.currentUser.github_url }}<br>
          포트폴리오 url : {{ this.currentUser.portfolio_url }}<br>
          <!-- 약점 : {{ this.currentUser.strength }}<br> -->
          팀 : <span v-if="this.currentUser.my_team !== null">{{ this.currentUser.my_team.name }}</span>
          <span v-if="this.currentUser.my_team === null">팀이 없습니다</span>
        </div>
        <div class="d-flex">
          <button>
            <router-link to="/mypage/bookmarkings" class="text-decoration-none" style="color:black">북마크 모아보기</router-link>
          </button>
          <button @click="openModal()" >
            <!-- <router-link class="update" to="/mypage/edit">프로필 수정</router-link> -->
            <div class="update">프로필 수정</div>
          </button>
          <button @click="openModal2()">
            <div class="update">비밀번호 변경</div>
          </button>
          <button @click="signOut()">
            <div class="update">탈퇴하기</div>
          </button>
        </div>
      </div>
    </div>
    <MyPageEdit v-if="modalToggle" :modalToggle="modalToggle" @modal-close-btn="closeModal()"></MyPageEdit>
    <PasswordChange v-if="modalToggle2" :modalToggle="modalToggle2" @modal-close-btn2="closeModal2()"></PasswordChange>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
import MyPageEdit from '@/views/MyPage/MyPageEdit.vue'
import PasswordChange from '@/components/MyPage/PasswordChange.vue'
import router from '@/router'

export default {
  name: 'MyPage',
  components: {
    MyPageEdit,
    PasswordChange,
  },
  data() {
    return {
      modalToggle: false,
      modalToggle2: false,
    }
  },
  computed: {
    ...mapGetters(['currentUser',])
  },
  methods: {
    ...mapActions(['fetchCurrentUser', 'signout']),
    // 프로필 수정 모달 open
    openModal(){
      this.modalToggle = !this.modalToggle
    },
    // 비밀번호 변경 모달 open
    openModal2(){
      this.modalToggle2 = !this.modalToggle2
    },
    // 프로필 수정 모달 close
    closeModal() {
      this.modalToggle = false
    },
    // 비밀번호 수정 모달 close
    closeModal2() {
      this.modalToggle2 = false
    },

    goBack() {
      router.push({ name: 'main' })
    },

    signOut() {
      this.signout()
    }
  },
  created() {
    this.fetchCurrentUser()
  }
}
</script>

<style scoped>
  
  .container {
    background-color: #fcf3e1;
    /* border: 2px solid black; */
    border-radius: 20px;
    box-shadow: 10px 10px;
    width: 700px;
  }

  .title{
    font-family: 'Gowun Dodum', sans-serif;
    font-weight: bolder;
    font-size: 60px;
    text-align: center;
    padding-bottom: 35px;
    color: #FDFDFD;
    text-shadow: #E3B8D3 1px 1px,#E3B8D3 0px 0px,#E3B8D3 1px 1px,#E3B8D3 2px 2px,#E3B8D3 3px 3px,#E3B8D3 4px 4px,#E3B8D3 5px 5px,#E3B8D3 6px 6px,#E3B8D3 7px 7px,#E3B8D3 8px 8px,#E3B8D3 9px 9px,#E3B8D3 10px 10px,#E3B8D3 11px 11px,#E3B8D3 12px 12px,#E3B8D3 13px 13px,#E3B8D3 14px 14px,#E3B8D3 15px 15px,#E3B8D3 16px 16px,#E3B8D3 17px 17px,#E3B8D3 18px 18px,#E3B8D3 19px 19px,#E3B8D3 20px 20px;

  }

  .row{
    padding-bottom: 20px;
  }

  .col{
    background-color: #f7d1ff;
    border-top-left-radius: 20px;
    border-top-right-radius: 20px;
    justify-content: space-between;
    height: 45px;
  }

  .first{
    justify-content: space-between;
    margin-left: 10px
  }
  .circle{
    border-radius: 50%;
    height: 20px;
    width: 20px;
    color: black;
    text-align: center;
    font-weight: bolder;
    /* border: 2px solid black; */
    font-size: 14px;
    margin-right: 10px;
    line-height: 15px;
    margin-top: 10px;
  }

  .rectangle{
    height: 20px;
    width: 20px;
    background-color: #e33c3c;
    transition: transform 100ms, box-shadow 100ms;
    color: white;
    text-align: center;
    font-weight: bolder;
    /* border: 2px solid black; */
    font-size: 15px;
    line-height: 15px;
    box-shadow: black 2px 2px 0px;
    margin-right: 10px;
    cursor: pointer;
    margin-top: 10px;
    
  }

  .rectangle:active{
    transform: translateY(2px) translateX(2px);
    box-shadow: black 0px 0px 0px;
  }

  .arrow{
    height: 20px;
    width: 20px;
    background-color: rgb(43, 154, 69);
    transition: transform 100ms, box-shadow 100ms;
    color: white;
    text-align: center;
    font-weight: bolder;
    /* border: 2px solid black; */
    font-size: 15px;
    line-height: 15px;
    box-shadow: black 2px 2px 0px;
    cursor: pointer;
    margin-top: 10px;
    
  }

  .arrow:active{
    transform: translateY(2px) translateX(2px);
    box-shadow: black 0px 0px 0px;
  }

  button{
    background-color: #DFFF80;
    box-shadow: black 4px 4px 0px;
    /* border: 2px solid black; */
    border-radius: 8px;
    transition: transform 200ms, box-shadow 200ms;
    width : 120px;
    height: 35px;
    margin: auto;
    margin-top: 15px;
    
  }

  button:active{
    transform: translateY(4px) translateX(4px);
    box-shadow: black 0px 0px 0px;
  }

  .update{
    text-decoration: none;
    color:black;
  }

</style>