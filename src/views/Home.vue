<template>
  <div class="home row">
    <div class="subjects col-2">
    	<button class="btn btn-success btn-block">New Subject</button>
    	<hr>
		<div class="list-group list-group-flush">
			<a href
				v-for="sub in subjects"
				:key="sub.id"
				class="list-group-item list-group-action"
				:class="{ active: (selected_sub == sub.id) }"
				@click="selectSub($event, sub.id)">{{ sub.name }}</a>
		</div>
    </div>
    <div v-if="selected_sub" class="col-2">
		<app-sections>
			<div class="list-group list-group-flush">
				<a href
					class="list-group-item list-group-sction"
					v-for="sec in sections" :key="sec.id"
					:class="{ active: (selected_sec == sec.id) }"
					@click="selectSec($event, sec.id)">{{ sec.name }}</a>
			</div>
		</app-sections>
	</div>
	<div v-if="selected_sec" class="col-8">
		<app-notes
			:notes="notes"
			:subject="selected_sub"
			:section="selected_sec">
		</app-notes>
	</div>
  </div>
</template>

<script>
import Sections from '../components/Sections.vue'
import Notes from '../components/Notes.vue'
export default {
  name: 'home',
  data() {
  	return {
  		subjects: [],
  		sections: [],
  		notes: [],
  		selected_sub: null,
  		selected_sec: null
  	}
  },
  methods: {
  	selectSub(e, sub) {
  		e.preventDefault()
  		this.selected_sub = sub
  		this.selected_sec = null
  		this.notes = []
  		this.sections = this.$store.getters.getSections(sub)
  	},
  	selectSec(e, sec) {
  		e.preventDefault()
  		this.notes = []
  		this.notes = this.$store.getters.getNotes(this.selected_sub, sec)
  		this.selected_sec = sec
  	}
  },
  components: {
  	AppSections: Sections,
  	AppNotes: Notes
  },
  created() {
  	this.subjects = this.$store.getters.getSubjects
  },

}
</script>
