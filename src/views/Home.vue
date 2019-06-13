<template>
  <div class="home">
    <div class="sidebar">
		<div class="row">
			<div class="col-6">
				<select v-model="selected_sub" @change="selectSub($event, selected_sub)">
					<option value="">Select Subject</option>
					<option v-for="(sub, index) in subjects" :key="index" :value="sub.id">{{ sub.subject }}</option>
				</select>
				<div class="row">
					<div class="col-md-6 col-sm-6 col-xs-12">
						<em>Subject</em>
					</div>
					<div class="col-md-6 col-sm-6 col-xs-12 text-md-right">
						<b-button v-b-modal.new_subject class="btn btn-sm add-btn">Add Subject</b-button>
					</div>
				</div>
			</div>
			<div class="col-6" v-if="selected_sub">
				<select v-if="selected_sub"
					v-model="selected_sec"
					@change="selectSec($event, selected_sec)">
					<option value="">Select Section</option>
					<option v-for="(sec, index) in sections" :key="index" :value="sec.id">{{ sec.section }}</option>
				</select>
				<div class="row">
					<div class="col-md-6 col-sm-6 col-xs-12">
						<em>Section</em>
					</div>
					<div class="col-md-6 col-sm-6 col-xs-12 text-md-right">
						<app-sections
							v-if="selected_sub"
							:subject="selected_sub"
							@newSecSubmitted="updateSec">
						</app-sections>
					</div>
				</div>
			</div>
		</div>
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
			subject: this.new_subject
		};
		this.$store.dispatch('newSubject', new_sub)
			.then(res => {
				this.new_subject = null
				this.$root.$emit('bv::hide::modal', 'new_subject')
			})		
	}
  },
  components: {
  	AppSections: Sections,
  	AppNotes: Notes,
  	AppFlashCards: FlashCards
  },
  computed: {
  	subjects() {
  		let subs = this.$store.getters.getSubjects
  		return subs
  	}
  }

}
</script>

<style lang="scss">
// @import '../assets/custom.scss';
	.loading {
		width: 100%;
		height: 100%;
		position: absolute;
		top: 0;
		left: 0;
		z-index: 1000;
		background: rgba(0, 0, 0, 0.75);
		.center-spinner {
			position: absolute;
			top: 50%;
			left: 50%;
			transform: translate(-50%, -50%);
			color: #fff;
		}
	}
</style>

