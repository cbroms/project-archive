<script>
	export let view;
	export let post;

	let loaded = false;

	const onLoad = () => {
		loaded = true;
	}
</script>


<a class="item {`${view}`}" class:loading="{!loaded && view === "grid"}" href="project/{post.slug}">
	{#if view === "grid"}
		<img src="{post.smallImage}" alt={post.slug} on:load="{onLoad}" />
	{:else}
	<div class="post-line">
		<div class="post-title">{post.title}</div>
		<div class="post-date">{post.printDate}</div>
		<div class="post-type">{post.category}</div>
	</div>
	{/if}
</a>	



<style>

	.item {
		display: inline-block;
		padding: 10px 0;
		width: 175px;
		height: 175px;
		background-color: white;
		display: flex;
		justify-content: center;
		align-items: center;
	}

	@keyframes pulse { 
            0% { 
                opacity: 1; 
            } 
  
            50% { 
                opacity: 0.7;
            } 
  
            100% { 
                opacity: 1;
            } 
        } 

	.loading {
		margin-right: 10px !important;
		margin-bottom: 10px !important;
		background-color: grey !important;	
		animation-name: pulse; 
        animation-duration: 2.0s; 
        animation-timing-function: ease-out; 
		animation-iteration-count: infinite; 
	}

	.grid {
		padding: 10px;
		margin: 0;
		background-color: white;
	}

	.list {
		padding: 20px 0;
		width: 100%;
		height: auto;
		flex-grow: 1;
	}

	img {
		min-width: 0;
		max-width: 100%;
		max-height: 100%;
	}

	.post-line {
		display: flex;
		width: 100%;
	}

	.post-title {
		width: 100%;
		max-width: 340px;
	}

	.post-date {
		width: 200px;
	}

	.post-type {
		width: 100px;
	}

</style>