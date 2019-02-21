import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
  	user: { id: 1, username: 'jdiazbarriga', email: 'jagustin2791@gmail.com'},
  	subjects: [
  		{
  			id: 1,
  			name: 'PJM 460',
  		  	user_id: 1
  		},
  		{
  			id: 2,
  			name: 'CSC 372',
  			user_id: 1
  		}
  	],
  	sections: [
  		{
  			id: 1,
  			name: 'Chapter 1',
  			subject_id: 1,
  			user_id: 1
  		},
  		{
  			id: 2,
  			name: 'Chapter 2',
  			subject_id: 1,
  			user_id: 1
  		},
  		{
  			id: 3,
  			name: 'Chapter 1',
  			subject_id: 2,
  			user_id: 1
  		}
  	],
  	notes: [
  		{
  			id: 1,
  			note: 'This is a note for this chapter (chapter 1) of the this subject (PJM 460)',
  			subject_id: 1,
  			section_id: 1,
  			user_id: 1,
  		},
  		{
  			id: 2,
  			note: 'This is a note for this chapter (chapter 2) of the this subject (PJM 460)',
  			subject_id: 1,
  			section_id: 2,
  			user_id: 1,
  		},
  		{
  			id: 3,
  			note: 'This is a note for this chapter (chapter 1) of the this subject (CSC 472)',
  			subject_id: 2,
  			section_id: 3,
  			user_id: 1,
  		},
  	],
  	flash_cards : [
  		{
  			id: 1,
  			word: 'First word',
  			def: 'This is the def of the first word',
  			subject_id: 1,
  			section_id: 1,
  			user_id: 1
  		}
  	]
  },
  mutations: {

  },
  actions: {

  },
  getters: {
  	getSubjects(state) {
  		return state.subjects
  	},
  	getSections(state) {
  		return (sub) => state.sections.filter(sec => sec.subject_id == sub);
  	},
  	getNotes(state) {
  		return (sub, sec) => state.notes.filter(note => (note.subject_id == sub && note.section_id == sec));
  	}
  }
})
