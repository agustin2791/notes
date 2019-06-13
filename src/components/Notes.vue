<template scope="props">
	<div class="notes">
		<br>
		<button class="btn btn-primary add-note-flash"
			@click="newNoteDisplay = true">
			Add Note
		</button>
		<div v-if="newNoteDisplay"
			class="form-group">
			<form>
				<textarea-autosize 
					v-model="newNote"
					class="form-control"></textarea-autosize>
				<br>
				<button class="btn btn-primary"
						@click="createNewNote($event)">Submit</button>
				<button class="btn btn-default"
					@click="newNoteDisplay = false">
					Cancel
				</button>
			</form>
		</div>
		<div v-for="note in notes"
			 :key="note.id">
			<div v-if="editCurrentNote == note.id">
				<textarea-autosize v-model="noteEdit"
					class="form-control"></textarea-autosize>
				<button class="btn btn-primary"
					@click.prevent="saveEdit(note.id)">
					Save
				</button>
				<button class="btn btn-default"
					@click.prevent="clearEdit">
						Cancel
				</button>
			</div>
			<p 
				style="white-space: pre"
				@click="startEdit(note.id)"
				v-else>{{ note.note }}</p>
		</div>
    <div v-if="isLoading" class="loading">
      <div class="center-spinner">
        Logging in... <b-spinner variant="success" label="Logging in..."></b-spinner>
      </div>
    </div>
	</div>
</template>

<script type="text/javascript">
export default {
  props: ['subject', 'section'],
  data () {
    return {
    	// notes: [],
    	newNoteDisplay: false,
	    newNote: null,
	    editCurrentNote: null,
	    isEditing: false,
	    noteEdit: null
    }
  },
  computed: {
    notes() {
      return this.$store.getters.getNotes(this.subject, this.section)
    }
  },
  methods: {
  	createNewNote(e) {
  		e.preventDefault()
      this.loading()
  		let nuNote = {
  			note: this.newNote,
  			subject_id: this.subject,
  			section_id: this.section
  		}
  		this.$store.dispatch('newNote', nuNote)
        .then(res => {
            this.notLoading()
            this.newNoteDisplay = false
            this.newNote = null
        })
  		
  	},
  	startEdit(note_id) {
  		let toEdit = this.notes.find(function(note) {
  			if (note.id == note_id) {
  				return note
  			}
  		})
  		this.noteEdit = toEdit.note
  		this.editCurrentNote = note_id
  	},
  	saveEdit(note_id) {
  		this.$store.dispatch('editNote', {id: note_id, edit: this.noteEdit})
  		this.notes = this.$store.getters.getNotes(this.subject, this.section)
  		this.noteEdit = null
  		this.editCurrentNote = null
  	},
  	clearEdit() {
  		this.editCurrentNote = null
  		this.noteEdit = null
  	}
  },
  watch: {
  	section() {
  		this.notes = this.$store.getters.getNotes(this.subject, this.section)
  	}
  },
  created() {
  	
  }
}
</script>
