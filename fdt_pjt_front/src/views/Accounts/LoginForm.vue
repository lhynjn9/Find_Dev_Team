<template>
  <div>
    <div class="container">
      <div class="row">
        <div class="col d-flex" style="height:40px;">
          <div class="d-flex align-items-center">
            <div class="circle" style="background-color: #c5af3d;">•</div>
            <div class="circle" style="background-color: #e3bfc8;">-</div>
            <div class="circle" style="background-color: #67769d;">+</div>
          </div>
        </div>
      </div>
      <div class="row">
        <form>
          <div class="my-1">
            <span>유저이름: </span>
            <label for="username"></label>
            <input type="text" v-model="login_credentials.username" placeholder="username" id="username">
          </div>
          <div class="my-1">
            <span>비밀번호: </span>
            <label for="password"></label>
            <input type="password" v-model="login_credentials.password" placeholder="password" id="password">
          </div>
        </form> 
        <div class="d-flex justify-content-left">
          <div class="me-1">
            <input class="btn" type="submit" @click="login(login_credentials)">
          </div>
          <div class="mx-1">
            <button @click="openModal()" class="btn">회원가입</button>
          </div>
        </div>
      </div>
    </div>
    <!-- 에러부분 추가 작업 필요 -->
    <!-- <p v-for="(errors, field) in authError" :key="field">
      {{ field }}
      <ul>
        <li v-for="(error, idx) in errors" :key="idx">
          {{ error }}
        </li>
      </ul>
    </p> -->
    <AccountErrorList v-if="authError !== null"></AccountErrorList>
    <SignUpModal v-if="modalToggle" :modalToggle="modalToggle" @modal-close-btn="closeModal()"></SignUpModal>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
import SignUpModal from '@/views/Accounts/SignUpModal.vue'
import AccountErrorList from '@/components/Accounts/AccountErrorList.vue'

export default {
  name: 'LoginForm',
  components: {
    SignUpModal,
    AccountErrorList,
  },
  data() {
    return {
      modalToggle: false,
      login_credentials: {
        username: '',
        password: '',
      },
    }
  },
  computed: {
    ...mapGetters(['authError',]),
  },
  methods: {
    ...mapActions(['login',]),
    openModal(){
      this.modalToggle = !this.modalToggle
    },
    closeModal() {
      this.modalToggle = false
    }
  }
}
</script>

<style scoped>
.container {
  background-color: #fcf3e1;
  /* border: 2px solid black; */
  border-radius: 20px;
  box-shadow: 10px 10px;
  width: 500px;
  height: 300px;
}

.btn {
  background-color: #DFFF80;
  /* border: 1px solid black; */
  box-shadow: 3px 3px;
  transition: transform 200ms, box-shadow 200ms;
  margin-top: 10px;
}

.btn:active {
  transform: translateY(4px) translateX(4px);
}

#username, #password {
  background-color: white;
  border-radius: 5px;
  /* border: 1px solid black; */
}

a {
  text-decoration: none;
  color: black;
}

.col {
    background-color: #f7d1ff;
    border-top-left-radius: 20px;
    border-top-right-radius: 20px;
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
  }

</style>