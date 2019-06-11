<!-- eslint-disable -->
<template>
	<div class="subjects row">
		<div class="col-8 offset-2">
			<br>
			<b-input-group size="md" prepend="New Subject">
				<b-form-input v-model="newSubject"></b-form-input>
				<b-input-group-append>
					<b-button class="btn-primary"
						@click.prevent="addSubject">Add Subject</b-button>
				</b-input-group-append>
			</b-input-group>
			<table class="table table-striped">
				<thead>
					<tr>
						<th @click="sortList()">Subject Name 
							<div v-if="isSorted" class="sort-option">
								<span class="fa" :class="{'fa-angle-down': sort == 'desc', 'fa-angle-up': sort == 'asc'}"></span>
							</div>
							<div v-else class="sort-option">
								<span class="fa fa-angle-up"></span>
								<span class="fa fa-angle-down"></span>
							</div>
						</th>
						<th></th>
					</tr>
				</thead>
				<tbody>
					<tr v-for="s in sortedSubjects" :key="s.id">
						<td>
							<input type="text" 
								name="edit_subject"
								class="form-control"
								v-model="edit"
								v-if="editId === s.id">
							<p v-else>{{ s.subject }}</p>
						</td>
						<td style="text-align: right">
							<button type="button"
								class="btn btn-primary"
								@click.prevent="startEdit(s.id)"
								v-if="editId != s.id">
								Edit
							</button>
							&nbsp;
							<button type="button"
								class="btn btn-primary"
								@click.prevent="submitEdit"
								v-if="editId === s.id">
								Submit		
							</button>
							<button type="text"
								class="btn btn-default"
								@click.prevent="cancelEdit"
								v-if="editId === s.id">
								Cancel		
							</button>&nbsp;
							<button type="button"
								class="btn btn-danger"
								@click.prevent="deleteSubject(s.id)">
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
					<p>You are about to delete this Subject</p>
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
			isSorted: false,
			sort: null,
			editId: null,
			edit: null,
			toDelete: false,
			deleteId: null,
			newSubject: null
		}
	},
	computed: {
	  	subjects() {
	  		let subs = this.$store.getters.getSubjects
	  		return subs
	  	},
		sortedSubjects() {
			let subs = this.subjects;
			if (this.isSorted && this.sort == 'asc') {
				subs.sort((a,b) => {
					if (a.name.toLowerCase() > b.name.toLowerCase()) {
						return 1;
					} else if (a.name.toLowerCase() < b.name.toLowerCase()) {
						return -1;
					} else {
						return 0;
					}
				})
			} else if (this.isSorted && this.sort == 'desc') {
				subs.sort((a, b) => {
					if (a.name.toLowerCase() > b.name.toLowerCase()) {
						return -1;
					} else if (a.name.toLowerCase() < b.name.toLowerCase()) {
						return 1;
					} else {
						return 0;
					}
				})
			}
			return subs;
		}
	},
	methods: {
		sortList() {
			if (this.sort == null || this.sort == 'desc') {
				this.sort = 'asc'
			} else if (this.sort == 'asc') {
				this.sort = 'desc';
			}
			this.isSorted = true;
		},
		addSubject() {
			if (this.newSubject != null) {
				let newSub = {
					subject: this.newSubject
				};
				this.$store.dispatch('newSubject', newSub);
			}
			this.newSubject = null;
		},
		startEdit(id) {
			this.toEdit = true
			this.editId = id
			this.edit = this.subjects.find(sub => {
				if (sub.id === id) {
					return sub
				}
			}).subject
		},
		submitEdit() {
			this.$store.dispatch('editSubject', {id: this.editId, edit: this.edit})
			this.editId = null
			this.edit = null
		},
		cancelEdit() {
			this.editId = null
			this.edit = null
		},
		deleteSubject(id) {
			this.deleteId = id;
			this.toDelete = true;
		},
		confirmDel() {
			this.$store.dispatch('deleteSubject', this.deleteId);
			this.toDelete = false;
			this.deleteId = null;
		},
		cancelDel() {
			this.toDelete = false;
			this.deleteId = null;
		}
	}

}
</script>
