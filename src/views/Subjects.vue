<!-- eslint-disable -->
<template>
	<div class="subjects row">
		<div class="col-8 offset-2">
			<table class="table table-striped">
				<thead>
					<tr>
						<th>Subject Name</th>
						<th></th>
					</tr>
				</thead>
				<tbody>
					<tr v-for="s in subjects" :key="s.id">
						<td>{{ s.name }}</td>
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
			subjects: this.$store.getters.getSubjects
		}
	}
}
</script>
