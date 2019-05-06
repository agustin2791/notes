<template>
	<div class="flash">
		<div class="add-note-flash">
			<b-button v-b-modal.new_card variant="primary">Add Card</b-button><span>&nbsp;</span>
			<b-button v-b-modal.study
				variant="primary"
				@click.prevent="triggerStudy">Study</b-button>
		</div>
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
						<button class="btn btn-primary"
							@click.prevent="startEdit(c)">Edit</button>
						<button class="btn btn-danger"
							@click.prevent="delCard(c.id)">Delete</button>
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
					<textarea-autosize style="min-height: 61px" class="my-6 form-control" v-model="newCard.def"></textarea-autosize>
				</div>
				<button class="btn btn-primary"
					@click.prevent="newFlashCard">Create</button>
			</form>
		</b-modal>
		<b-modal
			id="edit_card"
			size="lg"
			title="Edit Flash Card"
			hide-footer>
			<form>
				<div class="form-group">
					<label class="my-2">Term</label>
					<input type="text" class="my-6 form-control" v-model="editCard.term">
				</div>
				<div class="form-group">
					<label class="my-2">Definition</label>
					<textarea-autosize style="min-height: 61px" class="my-6 form-control" v-model="editCard.def"></textarea-autosize>
				</div>
				<button class="btn btn-primary"
					@click.prevent="editFlashCard">Change</button>
			</form>
		</b-modal>
		<b-modal
			id="study"
			size="xl"
			title="Flash Card"
			hide-footer
			hide-header
			hide-header-close>
			<app-study-cards v-if="showCards"
				:list="flashCards">
			</app-study-cards>
		</b-modal>
	</div>
</template>

<script>
	import StudyCards from './StudyCards.vue'
	export default {
		props: ['subject', 'section'],
		data() {
			return {
				flashCards: [],
				showStudy: false,
				newCard: {
					term: null,
					def: null
				},
				editCard: {
					id: null,
					term: null,
					def: null
				},
				showCards: false
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
			},
			startEdit(card) {
				this.editCard.id = card.id
				this.editCard.term = card.word
				this.editCard.def = card.def
				this.$root.$emit('bv::show::modal', 'edit_card')
			},
			editFlashCard() {
				let edit = {
					id: this.editCard.id,
					word: this.editCard.term,
					def: this.editCard.def,
					sebject_id: this.subject,
					section_id: this.section
				}
				this.$store.dispatch('editCard', edit)
				this.flashCards = this.$store.getters.getCards(this.subject, this.section)
				this.editCard = {
					id: null,
					term: null,
					def: null
				}
				this.$root.$emit('bv::hide::modal', 'edit_card')
			},
			delCard(card_id) {
				this.$store.dispatch('deleteCard', card_id)
				this.flashCards = this.$store.getters.getCards(this.subject, this.section)
			},
			triggerStudy() {
				let vm = this;
				vm.showCards = false;
				setTimeout(function() {
					vm.showCards = true;
				}, 500);
			}
		},
		watch: {
			section() {
				this.flashCards = this.$store.getters.getCards(this.subject, this.section)
			}
		},
		created() {
			this.flashCards = this.$store.getters.getCards(this.subject, this.section)
		},
		components: {
			AppStudyCards: StudyCards 
		}
	}

</script>

<style lang="scss">
#study {
	background: #333;
}
</style>