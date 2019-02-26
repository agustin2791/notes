<template>
	<div class="flash">
		<br>
		<b-button v-b-modal.new_card variant="primary">Add Card</b-button> 
		<button class="btn btn-primary"></button>
		<br>
		<br>
		<table class="table table-striped">
			<thead>
				<tr>
					<th>Term</th>
					<th>Definition</th>
					<th></th>
				</tr>
			</thead>
			<tbody>
				<tr v-for="c in flashCards"
					:key="c.id">
					<td>{{ c.word }}</td>
					<td>{{ c.def }}</td>
					<td>
						<button class="btn btn-primary">Edit</button>
						<button class="btn btn-danger">Delete</button>
					</td>
				</tr>
			</tbody>
		</table>
		<b-modal
			id="new_card"
			size="lg"
			title="New Flash Card"
			hide-footer>
			<form>
				<div class="form-group">
					<label class="my-2">Term</label>
					<input type="text" class="my-6 form-control" v-model="newCard.term">
				</div>
				<div class="form-group">
					<label class="my-2">Definition</label>
					<textarea-autosize row="4" type="text" class="my-6 form-control" v-model="newCard.def"></textarea-autosize>
				</div>
				<button class="btn btn-primary"
					@click.prevent="newFlashCard">Create</button>
			</form>
		</b-modal>
	</div>
</template>

<script>
	export default {
		props: ['subject', 'section'],
		data() {
			return {
				flashCards: [],
				newCard: {
					term: null,
					def: ''
				},
				editCard: {
					term: null,
					def: null
				}
			}
		},
		methods: {
			newFlashCard() {
				let card = {
					word: this.newCard.term,
					def: this.newCard.def,
					subject_id: this.subject,
					section_id: this.section,
					user_id: 1
				};
				this.$store.dispatch('newCard', card)
				this.flashCards = this.$store.getters.getCards(this.subject, this.section)
				this.$root.$emit('bv::hide::modal', 'new_card')
				this.newCard = {term: null, def: null}
			}
		},
		watch: {
			section() {
				this.flashCards = this.$store.getters.getCards(this.subject, this.section)
			}
		},
		created() {
			this.flashCards = this.$store.getters.getCards(this.subject, this.section)
		}
	}
</script>
