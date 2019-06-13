<template>
	<div class="study" style="text-align: center;">
		<button class="btn btn-primary"
			@click.prevent="shuffle">Shuffle</button>
		<div class="card">
			<div class="flash_card">
				<div class="card-word" v-if="showSide == 0">{{ cards[show_card].word }}</div>
				<div class="card-def" v-if="showSide == 1">{{ cards[show_card].def }}</div>
			</div>		
		</div>
		<div class="row">
			<div class="col-2">
				<button class="btn btn-primary" @click.prevent="prev">Prev</button>
			</div>
			<div class="col-8">
				<button class="btn btn-primary" @click.prevent="flipCard">Flip</button>
			</div>
			<div class="col-2">
				<button class="btn btn-primary" @click.prevent="next">Next</button>
			</div>
		</div>
	</div>
</template>

<script>
	export default {
		props: ['list'],
		data() {
			return {
				cards: this.list,
				show_card: 0,
				showSide: 0
			}
		},
		methods: {
			shuffle() {
				let unShuffle = this.list,
					shuffled = [];
				for (let i = (unShuffle.length - 1); i >= 0; i--) {
					let randIndex = Math.floor(Math.random() * (i+1));
					shuffled.push(unShuffle[randIndex]);
					let temp = unShuffle[randIndex]
					unShuffle.splice(randIndex, 1);
					unShuffle.push(temp)
				}
				this.cards = shuffled;
				for (let s in shuffled) {
					console.log(shuffled[s].id + ": " + shuffled[s].word)
				}
				unShuffle.sort(function(a, b) {
					if (a.id > b.id) {
						return 1
					} else if (a.id < b.id) {
						return -1
					} else {
						return 0
					}
				})
			},
			prev() {
				this.showSide = 0
				if (this.show_card > 0) {
					this.show_card--
				}
			},
			next() {
				this.showSide = 0
				if (this.show_card != (this.cards.length - 1)) {
					this.show_card++
				}
			},
			flipCard() {
				let card = document.getElementsByClassName('flash_card')[0]
				if (this.showSide == 0) {
					this.showSide = 1
				} else {
					this.showSide = 0
				}
				
			}
		}
	}
</script>

<style lang="scss" scoped>
.study {
	background: #ddd;
	padding-top: 10px;
	.card {
		width: 75%;
		margin: 15px auto;
		min-height: 200px;
		position: relative;
		.card-word {
			position: absolute;
			top: 50%;
			left: 50%;
			transform: translate(-50%, -50%);
			index: 1;
		}
		.card-def {
			position: absolute;
			top: 50%;
			left: 50%;
			transform: translate(-50%, -50%);
			index: -1;
		}
	}
	.row {
		background: #fff;
		padding: 5px 0;
	}
}

</style>

