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
						<td>
							<input type="text" 
								v-model="editSec"
								class="form-control"
								v-if="editId == s.id">
							<p v-else>{{ s.section }}</p>
						</td>
						<td>{{ getSubject(s.subject_id) }}</td>
						<td style="text-align: right">
							<button type="button"
								class="btn btn-primary"
								v-if="!editId"
								@click.prevent="editSection(s.id)">
								Edit
							</button>
							<button type="button"
								class="btn btn-primary"
								v-if="editId == s.id"
								@click.prevent="submitEdit">
								Update
							</button>
							<button type="button"
								class="btn btn-primary"
								v-if="editId == s.id"
								@click.prevent="cancelEdit">
								Cancel
							</button>&nbsp;
							<button type="button"
								class="btn btn-danger"
								@click.prevent="deleteSection(s.id)">
								Delete
							</button>
						</td>
					</tr>
				</tbody>
			</table>
		</div>
		<div v-if="toDelete" class="confirm-delete">
			<div class="confirm-container">
				<div class="confirm-title">
					<h2>Are you sure?</h2>
				</div>
				<div class="confirm-content">
					<p>You are about to delete this Section</p>
					<div class="confirm-buttons">
						<button class="btn btn-danger" @click.prevent="confirmDel">Yes, Delete</button>
						<button class="btn btn-info" @click.prevent="cancelDel">Cancel</button>
					</div>
				</div>
			</div>
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
			editId: null,
			editSec: null,
			toDelete: false,
			secDelId: null
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
			if (this.subjectSel) {
				return this.$store.getters.getSections(this.subjectSel)
			}
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
			
		},
		editSection(id) {
			let sec = this.sections.find(s => {
				if (s.id == id) {
					return s
				}
			})
			this.editSec = sec.section
			this.editId = id
		},
		cancelEdit() {
			this.editId = null
			this.editSec = null
		},
		submitEdit() {
			let changes = {id: this.editId, edit: this.editSec}
			this.$store.dispatch('editSection', changes)
			this.editId = null
			this.editSec = null
		},
		submitSection() {
			let changes = {id: this.editId, edit: this.editSec}
			this.$store.dispatch('editSection', changes)
			this.editId = null
			this.editSec = null
		},
		deleteSection(sec) {
			this.toDelete = true
			this.secDelId = sec
		},
		confirmDel() {
			this.$store.dispatch('deleteSection', this.secDelId)
			this.toDelete = false
			this.secDelId = null
		},
		cancelDel() {
			this.toDelete = false
			this.secDelId = null
		}

	}
}
</script>
