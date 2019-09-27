<template>
	<div class="sections">
		<b-button v-b-modal.new_section
				  class="btn btn-sm add-btn btn-block">New Section</b-button>
		<b-modal id="new_section"
				 title="New Section"
				 hide-footer
				 size="lg">
			<form>
				<div class="form-group row">
					<label for="title"
						   class="col-form-label col-form-label-md col-sm-2">
						Section Title
					</label>
					<input type="text"
						   v-model="secTitle"
						   class="form-control col-sm-9">
				</div>
				<button class="btn btn-primary"
						@click="submitForm($event)">Submit</button>
			</form>
		</b-modal>
	</div>
</template>

<script>
export default {
	props: ['subject'],
	data() {
		return {
			secTitle: null
		}
	},
	computed: {
		validateTitle() {
			let sections = this.$store.getters('getSections', this.subject)
			for (sec in sections) {
				if (sections[sec].section == this.secTitle) {
					return true
				}
			}
			return false
		}
	},
	methods: {
		submitForm(e) {
			e.preventDefault()
			let new_sec = {
				section: this.secTitle,
				subject_id: this.subject
			};
			this.$store.dispatch('newSection', new_sec)
				.then(res => {
					this.$emit('newSecSubmitted')
					this.secTitle = null
					this.$root.$emit('bv::hide::modal', 'new_section')
				})
			
		}
	}
}
</script>
