<script>
	export let view;
	export let year;
</script>


<div class="item {`${view}`}">
	<strong>{year}</strong>
</div>	


<style>
	.item {
		display: inline-block;
		padding: 10px 0;
		width: 175px;
		height: 175px;
		background-color: white;
		display: flex;
		justify-content: left;
		align-items: center;
	}

	.grid {
		padding: 0;
		margin: 0;
		margin-top: 10px;
		background-color: white;

		border-right: 2px solid black;
	}

	@media (max-width: 400px) {
		.grid {
			border-right: none;
			border-bottom: 2px solid black;
		}
	}

	.list {
		padding: 20px 0;
		width: 100%;
		height: auto;
		flex-grow: 1;

		border-bottom: 2px solid black;
	}

</style>