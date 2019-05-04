<template>
  <div class="home">
    <div class="sidebar">
		<h2>Subject</h2>
		<select v-model="selected_sub" @change="selectSub($event, selected_sub)">
			<option value="">Select Subject</option>
			<option v-for="(sub, index) in subjects" :key="index" :value="sub.id">{{ sub.name }}</option>
		</select><br><br>
		<b-button v-b-modal.new_subject
				  class="btn btn-success btn-sm">Add Subject</b-button>
		<hr>
		<h3 v-if="selected_sub">Section</h3>
		<select v-if="selected_sub"
			v-model="selected_sec"
			@change="selectSec($event, selected_sec)">
			<option value="">Select Section</option>
			<option v-for="(sec, index) in sections" :key="index" :value="sec.id">{{ sec.name }}</option>
		</select>
		<br>
		<br>
    	<!-- <b-button v-b-modal.new_subject
				  class="btn btn-success btn-block">New Subject</b-button> -->
    	<!-- <hr>
		<div class="list-group list-group-flush">
			<a href
				v-for="sub in subjects"
				:key="sub.id"
				class="list-group-item list-group-action"
				:class="{ active: (selected_sub == sub.id) }"
				@click="selectSub($event, sub.id)">{{ sub.name }}</a>
		</div> -->
    <!-- </div>
    <div v-if="selected_sub" class="col-2"> -->
		<app-sections
		    v-if="selected_sub"
			:subject="selected_sub"
			@newSecSubmitted="updateSec">
			<div class="list-group list-group-flush">
				<a href
					class="list-group-item list-group-sction"
					v-for="sec in sections" :key="sec.id"
					:class="{ active: (selected_sec == sec.id) }"
					@click="selectSec($event, sec.id)">{{ sec.name }}</a>
			</div>
		</app-sections>
	</div>
	<div v-if="selected_sec" class="notes-content">
		<ul class="nav nav-tabs">
			<li class="nav-item">
				<a href
					class="nav-link"
					:class="{active: (noteFlash == 'AppNotes')}"
					@click="$event.preventDefault(), noteFlash = 'AppNotes'">Notes</a>
			</li>
			<li class="nav-item">
				<a href
					class="nav-link"
					:class="{active: (noteFlash == 'AppFlashCards')}"
					@click="$event.preventDefault(), noteFlash = 'AppFlashCards'">Flash Cards</a>
			</li>
		</ul>
		
		<component :is="noteFlash"
			:subject="selected_sub"
			:section="selected_sec"></component>
	</div>
	<b-modal id="new_subject"
				 title="New Section"
				 hide-footer
				 size="lg">
		<form>
			<div class="form-group row">
				<label for="title"
					   class="col-form-label col-form-label-md col-sm-2">
					Subject
				</label>
				<input type="text"
					   v-model="new_subject"
					   class="form-control col-sm-9">
			</div>
			<button class="btn btn-primary"
					@click="submitSubject($event)">Submit</button>
		</form>
	</b-modal>
  </div>
</template>

<script>
import Sections from '../components/Sections.vue'
import Notes from '../components/Notes.vue'
import FlashCards from '../components/FlashCards.vue'
export default {
  name: 'home',
  data () {
  	return {
  		subjects: [],
  		sections: [],
  		notes: [],
  		selected_sub: null,
  		selected_sec: null,
  		submitSec: false,
  		new_subject: null,
  		noteFlash: 'AppNotes'
  	}
  },
  methods: {
  	selectSub (e, sub) {
  		e.preventDefault()
  		this.selected_sub = sub
  		this.selected_sec = null
  		this.notes = []
  		this.sections = this.$store.getters.getSections(sub)
  	},
  	selectSec (e, sec) {
  		e.preventDefault()
  		this.notes = []
  		this.notes = this.$store.getters.getNotes(this.selected_sub, sec)
  		this.selected_sec = sec
  	},
  	updateSub () {
  		this.subjects = this.$store.getters.getSubjects
  	},
  	updateSec () {
  		this.sections = this.$store.getters.getSections(this.selected_sub)
  	},
  	submitSubject(e) {
		e.preventDefault()
		let new_sub = {
			name: this.new_subject,
			user_id: 1
		};
		this.$store.dispatch('newSubject', new_sub)
		this.new_subject = null
		this.$root.$emit('bv::hide::modal', 'new_subject')
	}
  },
  components: {
  	AppSections: Sections,
  	AppNotes: Notes,
  	AppFlashCards: FlashCards
  },
  created () {
  	this.subjects = this.$store.getters.getSubjects
  }

}
</script>

<style lang="scss" scoped>
.home {
	width: 100%;
	display: block;
	.sidebar {
		border: solid thin #333;
		padding: 20px 5px;
		margin: 5px;
		width: 20%;
		display: inline-block;
		vertical-align: top;
		select {
			width: 100%;
			background: #fff;
			height: 40px;
			border: solid thin #333;
			border-radius: 0px;
		}
	}
	.notes-content {
		width: 75%;
		display: inline-block;
		vertical-align: top;
		margin: 5px;
	}
}

</style>
