/* eslint-disable */
import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
  	user: { id: 1, username: 'jdiazbarriga', email: 'jagustin2791@gmail.com' },
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
  			user_id: 1
  		},
  		{
  			id: 2,
  			note: 'This is a note for this chapter (chapter 2) of the this subject (PJM 460)',
  			subject_id: 1,
  			section_id: 2,
  			user_id: 1
  		},
  		{
  			id: 3,
  			note: 'This is a note for this chapter (chapter 1) of the this subject (CSC 472)',
  			subject_id: 2,
  			section_id: 3,
  			user_id: 1
  		}
  	],
  	flash_cards: [
  		{
		  "id": 1,
		  "word": "amet",
		  "def": "Enterprise-wide hybrid capacity",
		  "subject_id": 1,
		  "section_id": 1,
		  "user_id": 1
		}, {
		  "id": 2,
		  "word": "erat",
		  "def": "Intuitive zero defect system engine",
		  "subject_id": 1,
		  "section_id": 1,
		  "user_id": 1
		}, {
		  "id": 3,
		  "word": "congue",
		  "def": "Multi-layered fault-tolerant attitude",
		  "subject_id": 1,
		  "section_id": 1,
		  "user_id": 1
		}, {
		  "id": 4,
		  "word": "donec",
		  "def": "Customer-focused exuding firmware",
		  "subject_id": 1,
		  "section_id": 1,
		  "user_id": 1
		}, {
		  "id": 5,
		  "word": "diam",
		  "def": "Distributed background policy",
		  "subject_id": 1,
		  "section_id": 1,
		  "user_id": 1
		}, {
		  "id": 6,
		  "word": "donec",
		  "def": "Cloned full-range middleware",
		  "subject_id": 1,
		  "section_id": 1,
		  "user_id": 1
		}, {
		  "id": 7,
		  "word": "amet",
		  "def": "Customer-focused leading edge project",
		  "subject_id": 1,
		  "section_id": 1,
		  "user_id": 1
		}, {
		  "id": 8,
		  "word": "sed",
		  "def": "Up-sized non-volatile groupware",
		  "subject_id": 1,
		  "section_id": 1,
		  "user_id": 1
		}, {
		  "id": 9,
		  "word": "vestibulum",
		  "def": "Balanced tertiary Graphical User Interface",
		  "subject_id": 1,
		  "section_id": 1,
		  "user_id": 1
		}, {
		  "id": 10,
		  "word": "primis",
		  "def": "Optimized homogeneous definition",
		  "subject_id": 1,
		  "section_id": 1,
		  "user_id": 1
		}
  	]
  },
  mutations: {
  	'NEW_SUBJECT'(state, subject) {
  		if (subject) {
  			subject.id = Math.floor(Math.random() * 100)
  			state.subjects.push(subject)
  			return state.subjects
  		}
  		return state.subjects
  	},
  	'NEW_SECTION'(state, section) {
  		if (section) {
  			section.id = Math.floor(Math.random() * 100)
  			state.sections.push(section)
  			return state.sections
  		}
  		return state.sections
  	},
  	'NEW_NOTE'(state, note) {
  		if (note) {
  			note.id = Math.floor(Math.random() * 100)
  			state.notes.push(note)
  			return state.notes
  		}
  		return state.notes
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
  			card.id = Math.floor(Math.random() * 100)
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
	  		console.log(sub_id)
	  		let subject = state.subjects.find( sub => { if (sub.id == sub_id) return sub });
	  		console.log(subject.name)
	  		return subject.name
	  	}
	  },
	  'DELETE_SUBJECT'(state, sub_id) {
		  if (sub_id) {
			  // delete subject
		  }
	  }
  },
  actions: {
  	newSubject({ commit }, subject) {
  		commit('NEW_SUBJECT', subject)
  	},
  	newSection({ commit }, section) {
  		commit('NEW_SECTION', section);
  	},
  	newNote({ commit }, note) {
  		commit('NEW_NOTE', note)
  	},
  	editNote({ commit }, changes) {
  		commit('EDIT_NOTE', changes)
  	},
  	deletNote({ commit }, note_id) {
  		commit('DELETE_CARD', note_id)
  	},
  	newCard({ commit }, card) {
  		commit('NEW_CARD', card)
  	},
  	editCard({ commit }, changes) {
  		commit('EDIT_CARD', changes)
  	},
  	deleteCard({ commit }, card_id) {
  		commit('DELETE_CARD', card_id)
  	},
  	getSubject({ commit }, sub_id) {
  		commit('GET_SUBJECT', sub_id)
	},
	deleteSubject({ commit }, sub_id) {
		commit('DELETE_SUBJECT', sub_id)
	}
  },
  getters: {
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
  		return (sub) => state.subjects.find(subject => (subject.id == sub)).name
  	}
  }
})
