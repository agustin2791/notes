<template scope="props">
	<div class="notes">
		<button class="btn btn-primary">Add Note</button>
		{{ subject }} | {{ section }}
		<hr>
		<div v-for="note in notes"
			:key="note.id">
			{{ note.note }}
		</div>
	</div>
</template>

<script type="text/javascript">
export default {
	props: ['notes', 'subject', 'section'],
	data() {
		return {
			newNote: {
				note: null
			}
		}
	}
}
</script>