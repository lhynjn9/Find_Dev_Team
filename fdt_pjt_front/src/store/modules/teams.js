import axios from 'axios'
import drf from '@/api/drf'
import router from '@/router'


// 개별 팀 조회 및 수정
// 팀 생성

// teams.js
export default {
  state: {
    teams: [],
    team: {},
    searchInfos: null,
    keyword: null,
  },
  getters: {
    teams: state => state.teams,
    team: state => state.team,
    keyword: state => state.keyword,
  },
  mutations: {
    SET_TEAMS: (state, teams) => state.teams = teams,
    // 라우터 로직을 바꿔봐야함
    SET_TEAM: (state, team) => state.team = team,
    SEARCH_MEMBER: (state, data) => state.keyword = data

  },
  actions: {
    // 전체 팀 조회
    fetchTeams({ commit }){
      axios({
        url: drf.teams.teams(),
        method: 'get',
      })
      .then(res => commit('SET_TEAMS', res.data))
      .catch(err => console.error(err.response))
    },

    // 개별 팀 조회
    fetchTeam({ commit, getters }, teamId){
      axios({
        url: drf.teams.myteam(teamId),
        method: 'get',
        headers: getters.authHeader,
      })
      .then(res => commit('SET_TEAM', res.data))
      .catch(err => {
        console.error(err.response)
        if(err.response.status === 404){
          router.push({ name: 'NotFound404' })
        }
      })
    },

    // 팀 생성
    createTeam({ commit, getters }, {team, userInfo}){
      axios({
        url: drf.teams.teamcreate(),
        method: 'post',
        data: team,
        headers: getters.authHeader,
      })
      .then(res => {
        commit('SET_TEAM', res.data)
        const team_data = {id: res.data.id, name: res.data.name}
        userInfo.my_team = team_data
        this.commit('SET_CURRENT_USER', userInfo)
        router.push({
          name: 'team',
          params:{ teamId: getters.team.id }
        })
      })
    },

    // 팀 수정
    updateTeam({ commit, getters }, { id, name, intro, leader, total_number, theme, team_member, common_interest, number, kakao_chat }){
      console.log(team_member)
      axios({
        url: drf.teams.myteam(id),
        method: 'put',
        data: { name, intro, leader, total_number, theme, team_member, common_interest, number, kakao_chat },
        headers: getters.authHeader,
      })
      .then(res => {
        commit('SET_TEAM', res.data)
        // 팀 수정이 모달이니 라우터를 돌릴 필요가 없음
        // router.push({
        //   name: 'team',
        //   params: { teamId: getters.team.id }
        // })
      })
      },

      // 팀 검색
      searchMember({ commit }, data) {
        const member = {
          member: data
        }
        axios({
          url: drf.teams.memebersearch(),
          method: "get",
          params: member,
        })
        .then(res => {
          // 데이터를 완전히 지웠을 경우에 대한 처리
          if (data === "") {
            res.data = []
          }
          // console.log(res.data)
          commit("SEARCH_MEMBER", res.data)
        })
        .catch(err => {
          console.error(err.response.data)
        })
      }
    }

  }
