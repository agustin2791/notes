<!-- eslint-disable -->
<template>
	<div class="sections row">
		<div class="col-8 offset-2">
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
						<td>{{ s.name }}</td>
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
			sections: this.$store.getters.getAllSections
		}
	},
	methods: {
		getSubject(sec) {
			let subject = this.$store.getters.getSubjectName(sec)
			return subject
		}
	}
}
</script>
