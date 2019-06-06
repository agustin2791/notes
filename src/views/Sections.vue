<!-- eslint-disable -->
<template>
	<div class="sections row">
		<div class="col-8 offset-2">
			<br>
			<b-form inline>
				<label for="new_section">New Section: </label>
				<b-form-input v-model="newSection"
					class="mb-2 mr-sm-2 mb-sm-0"></b-form-input>
				<label for="select_subject">Subject: </label>
				<b-form-select :options="subjects"
					class="mb-2 mr-sm-2 mb-sm-0"
					v-model="subjectSel"
					size="md"></b-form-select>
				<b-button class="btn-primary"
					@click.prevent="addSection">Add Subject</b-button>
			</b-form>
			<br>
			<table class="table table-striped">
				<thead>
					<tr>
						<th>Section Name</th>
						<th>Subject Name</th>
						<th></th>
					</tr>
				</thead>
				<tbody>
					<tr v-for="s in sections" :key="s.id">
						<td>{{ s.section }}</td>
						<td>{{ getSubject(s.subject_id) }}</td>
						<td style="text-align: right">
							<button type="button"
								class="btn btn-primary">
								Edit
							</button>&nbsp;
							<button type="button"
								class="btn btn-danger">
								Delete
							</button>
						</td>
					</tr>
				</tbody>
			</table>
		</div>
	</div>
</template>

<script>
/* eslint-disable */
export default {
	data() {
		return {
			newSection: null,
			subjectSel: null,
		}
	},
	computed: {
		subjects() {
			let subjects = this.$store.getters.getSubjects;
			let subs = [];
			for (let i in subjects) {
				let sub = {value: subjects[i].id, text: subjects[i].subject};
				subs.push(sub)
			}
			return subs;
		},
		sections() {
			return this.$store.getters.getAllSections
		}
	},
	methods: {
		getSubject(sec) {
			let subject = this.$store.getters.getSubjectName(sec)
			return subject
		},
		addSection() {
			let new_sec = {
				section: this.newSection,
				subject_id: this.subjectSel
			};
			this.$store.dispatch('newSection', new_sec)
				.then(res => {
					this.newSection = null;
					this.subjectSel = null;
				});
			
		}
	}
}
</script>
