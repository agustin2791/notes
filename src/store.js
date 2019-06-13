/* eslint-disable */
import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
  	user: null,
    idToken: null,
    subjects: null,
    sections: null,
  	notes: null,
    flash_cards: null
  },
  mutations: {
    // Populate State
    'SET_SUBJECTS'(state, data) {
      state.subjects = data.subject
    },
    'SET_SECTIONS'(state, data) {
      state.sections = data
    },
    'SET_NOTES'(state, data) {
      state.notes = data
    },
    'SET_CARDS'(state, data) {
      state.flash_cards = data
    },
  	'NEW_SUBJECT'(state, subjects) {
  		if (subjects) {
  			state.subjects = subjects
  			return state.subjects
  		}
  		return state.subjects
  	},
  	'NEW_SECTION'(state, section) {
  		if (section) {
  			state.sections.push(section)
  			return state.sections
  		}
  		return state.sections
  	},
  	'NEW_NOTE'(state, note) {
  		if (note) {
  			state.notes.push(note)
  			return state.notes
  		}
  		return state.notes
  	},
    'NEW_CARD'(state, flash_card) {
      if (flash_card) {
        state.flash_cards.push(flash_card)
      }
    },
  	'EDIT_NOTE'(state, changes) {
  		if (changes) {
  			let editNote = state.notes.find(function(note) {if (note.id == changes.id) {return note}});
  			let indexNote = state.notes.indexOf(editNote);
  			editNote.note = changes.edit;
  			state.notes.splice(indexNote, 1, editNote);
  			return state.notes
  		}
  	},
  	'DELETE_NOTE'(state, note_id) {
  		if (note_id) {
  			let delNote = state.notes.find(function(note) { if (note.id == note_id) { return note }});
  			let indexNote = state.notes.indexOf(delNote);
  			state.notes.splice(indexNote, 1)
  			return state.notes
  		}
  	},
  	'NEW_CARD'(state, card) {
  		if (card) {
  			state.flash_cards.push(card)
  			return state.flash_cards
  		}
  	},
  	'EDIT_CARD'(state, changes) {
  		if (changes) {
  			let editCard = state.flash_cards.find(function(card) { if (card.id == changes.id ) { return card }});
  			let indexCard = state.flash_cards.indexOf(editCard);
  			editCard.word = changes.word
  			editCard.def = changes.def
  			state.flash_cards.splice(indexCard, 1, editCard)
  			return state.flash_cards
  		}
  	},
  	'DELETE_CARD'(state, card_id) {
	  	if (card_id) {
	  		let delCard = state.flash_cards.find(function(card) { if (card.id == card_id) { return card }});
	  		let indexCard = state.flash_cards.indexOf(delCard);
	  		state.flash_cards.splice(indexCard, 1)
	  		return state.flash_cards
	  	}
	  },
	  'GET_SUBJECT'(state, sub_id) {
	  	if (sub_id) {
	  		let subject = state.subjects.find( sub => { if (sub.id == sub_id) return sub });
	  		return subject.name
	  	}
	  },
    'EDIT_SUBJECT'(state, sub) {
       if (sub) {
         for (let s in state.subjects) {
           if (state.subjects[s].id == sub.id) {
             state.subjects[s].subject = sub.subject
           }
         }
       }
    },
	  'DELETE_SUBJECT'(state, sub_id) {
		  if (sub_id) {
			  // delete subject
        let subject = state.subjects.find(sub => { if (sub.id == sub_id) return sub})
        let indexSub = state.subjects.indexOf(subject)
        state.subjects.splice(indexSub, 1)
        return state.subjects
		  }
	  },
    'EDIT_SECTION'(state, changes) {
      if (changes) {
        let sec = state.sections.find(s => { if (s.id === changes.id ) { return s }});
        let secId = state.sections.indexOf(sec);
        sec.section = changes.edit;
        state.sections.splice(secId, 1, sec);
        return;
      }
    },
    'DELETE_SECTION'(state, sec_id) {
      if (sec_id) {
        let sec = state.sections.find(s => { if (s.id === sec_id ) { return s }});
        let secId = state.sections.indexOf(sec);
        state.sections.splice(secId, 1)
        return;
      }
    },
    // Authentication
    'AUTH_USER'(state, auth) {
      state.idToken = auth.token
      state.user = {
        id: auth._id,
        first_name: auth.first_name,
        last_name: auth.last_name,
        username: auth.username,
        email: auth.email 
      };
    },
    'USER_LOGOUT'(state) {
      state.user = null
      state.idToken = null
      state.subjects = null
      state.sections = null
      state.notes = null
      state.flash_card = null
    },
    'SET_TOKEN'(state, token) {
      state.idToken = token
    }
  },
  actions: {
  	async newSubject({ commit, state }, subject) {
      subject.user_id = state.user.id
      return axios.post(/* http://localhost:5000 */'/api/subjects/' + subject.user_id, subject)
        .then(res => {
          let update_sub = res.data.results
          commit('NEW_SUBJECT', update_sub)
        })
  	},
  	async newSection({ commit, state }, section) {
      section.user_id = state.user.id
      return axios.post(/* http://localhost:5000 */'/api/sections/' + section.user_id, section)
        .then(res => {
          commit('NEW_SECTION', res.data.results.reverse()[0]);
        })
  	},
  	async newNote({ commit, state }, note) {
      note.user_id = state.user.id
      return axios.post(/* http://localhost:5000 */'/api/notes/' + note.user_id, note)
        .then(res => {
          let update = res.data.results
          commit('NEW_NOTE', update)
        })
  		
  	},
  	editNote({ commit }, changes) {
      commit('EDIT_NOTE', changes)
      return axios.put(/* http://localhost:5000 */'/api/notes/note/' + changes.id, changes)  		
  	},
  	deletNote({ commit }, note_id) {
  		commit('DELETE_CARD', note_id)
  	},
    async newCard({ commit, state }, flash_card) {
      flash_card.user_id = state.user.id
      return axios.post(/* http://localhost:5000 */'/api/flash_cards/' + flash_card.user_id, flash_card)
        .then(res => {
          commit('NEW_CARD', res.data.results)
        })
    },
  	editCard({ commit }, changes) {
  		commit('EDIT_CARD', changes)
      return axios.put(/* http://localhost:5000 */'/api/flash_cards/flash_card/' + changes.id, changes)
        .then(res => {
          console.log(res)
        })
  	},
  	deleteCard({ commit }, card_id) {
  		commit('DELETE_CARD', card_id)
      return axios.delete(/* http://localhost:5000 */'/api/flash_cards/flash_card/' + card_id)
  	},
  	getSubject({ commit }, sub_id) {
  		commit('GET_SUBJECT', sub_id)
  	},
    editSubject({ commit }, sub) {
      return axios.put(/* http://localhost:5000 */'/api/subjects/subject/' + sub.id, sub)
        .then(res => {
          commit('EDIT_SUBJECT', res.data)
        })
    },
    editSection({ commit }, changes) {
      commit('EDIT_SECTION', changes)
      return axios.put(/* http://localhost:5000 */'/api/sections/section/' + changes.id, changes)
    },
    deleteSection({ commit }, sec_id) {
      commit('DELETE_SECTION', sec_id)
      return axios.delete(/* http://localhost:5000 */'/api/sections/section/' + sec_id)
    },
  	deleteSubject({ commit }, sub_id) {
  		commit('DELETE_SUBJECT', sub_id)
      return axios.delete(/* http://localhost:5000 */'/api/subjects/subject/' + sub_id)
        .then(res => {
        })
  	},
    // Populate States
    populateData({ commit }, user_id) {
      // sections
      axios.get(/* http://localhost:5000 */'/api/subjects/' + user_id)
        .then(res => {
          commit('SET_SUBJECTS', res.data.results)
        })
      // subjects
      axios.get(/* http://localhost:5000 */'/api/sections/' + user_id)
        .then(res => {
          commit('SET_SECTIONS', res.data.results)
        })
      axios.get(/* http://localhost:5000 */'/api/notes/' + user_id)
         .then(res => {
           commit('SET_NOTES', res.data.results)
         })
      axios.get(/* http://localhost:5000 */'/api/flash_cards/' + user_id)
        .then(res => {
          commit('SET_CARDS', res.data.results)
        })
    },
    // Authentication
    register({commit, dispatch}, authData) {
      let newRegister = {
        "first_name": authData.first_name,
        "last_name": authData.last_name,
        "username": authData.username,
        "email": authData.email,
        "password": authData.password
      };
      // let dispatch = JSON.parse(newRegister);
      return axios.post(/* http://localhost:5000 */'/auth/register', newRegister)
        .then(res => {
          console.log('new register: ' + res)
          return dispatch('login', res.data.data);
        })
        .catch(err => {
          console.log(err)
        })
    },
    async login({ commit, dispatch }, authData) {
      return axios.post(/* http://localhost:5000 */'/auth/login', {
        username: authData.username,
        password: authData.password
      })
        .then(res => {
          commit('AUTH_USER', res.data.data);
          const data = res.data.data
          const token = data.token
          // const now = new Date()
          const duration = new Date(new Date().getTime() + 604800 * 1000)
          localStorage.setItem('token', token);
          localStorage.setItem('expirationDate', duration)
          dispatch('populateData', data._id)
          return {'status': 'ok'}
        })
        .catch(err => { return {'status': 'err'} })
    },
    loginCheck({ commit, dispatch }) {
      const token = localStorage.getItem('token')
      if (!token) return;
      commit('SET_TOKEN', token)
      const duration = new Date(localStorage.getItem('expirationDate'))
      const now = new Date()
      if (now >= duration) return;
      if (now <= duration) {
        axios.get(/* http://localhost:5000 */'/auth/user', {headers: {'Authorization': 'Bearer ' + token}})
          .then(res => {
            if (res.data.ok) {
              let data = res.data.data;
              data.token = token;
              commit('AUTH_USER', data)
              dispatch('populateData', data._id)
            }
          })
      }
    },
    logout({ commit }) {
      commit('USER_LOGOUT');
      localStorage.clear();
    }
  },
  getters: {
    getUser(state) {
      return state.user
    },
  	getSubjects (state) {
  		return state.subjects
  	},
  	getAllSections (state) {
  		return state.sections
  	},
  	getSections (state) {
  		return (sub) => state.sections.filter(sec => sec.subject_id == sub)
  	},
  	getNotes (state) {
  		return (sub, sec) => state.notes.filter(note => (note.subject_id == sub && note.section_id == sec))
  	},
  	getCards (state) {
  		return (sub, sec) => state.flash_cards.filter(note => (note.subject_id == sub && note.section_id == sec))
  	},
  	getSubjectName (state) {
  		return (sub) => state.subjects.find(subject => (subject.id == sub)).subject
  	},
    // filterSections (state) {
    //   return (sub) => state.sections.filter(secs => (secs.subject_id == sub))
    // }
  }
})
