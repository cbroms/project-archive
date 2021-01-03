<script>
	export let view;
	export let post;

	let loaded = false;
	let timeout = null;
	let hovered = false;

	const onLoad = () => {
		loaded = true;
	}
</script>


<a class="item {`${view}`}" class:loading={!loaded && view === "grid"} href="project/{post.slug}">
	{#if view === "grid"}
		<img src="{post.smallImage}" alt={post.slug} on:load="{onLoad}" />
	{:else}
	<div class="post-line" on:mouseover={() => hovered = true} on:mouseleave={() =>  hovered = false}>
		<div class="post-title">{post.title}</div>
		<div class="post-date">{post.printDate}</div>
		<div class="post-type">{post.category}</div>
	</div>
	{/if}
</a>	

{#if view === "list"}
	<div class="post-description">
		{#if hovered && post.excerpt}
			<div>
				<p class="post-title">{post.excerpt}</p>
			</div>
		{/if}
	</div>
{/if}



<style>

	.item {
		display: inline-block;
		width: 175px;
		height: 175px;
		display: flex;
		justify-content: left;
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
		padding: 0;
		margin: 0;
		margin-top: 10px;
		margin-right: 20px;
	}

	.list {
		width: 640px;
		height: auto;
		flex-grow: 1;
	}

	img {
		min-width: 0;
		max-width: 100%;
		max-height: 100%;
		width: auto;
	}

	.post-description {
		padding-top: 5px;
		padding-left: 20px;
		max-height: 40px;
		display: block;
		width: 280px;
	}

	.post-line {
		padding: 20px 0;
		display: flex;
		flex-wrap: wrap;
		justify-content: space-between;
		width: 640px;
	}

	.post-title {
		width: 100%;
		max-width: 340px;
	}

	.post-date {
		width: 175px;
	}

	.post-type {
		width: 100px;
	}

	@media (max-width: 1100px) {

		a {
			text-decoration: none;
		}

		.post-description {
			display: none;
		}

		.list {
			width: 100%;
		}

		.post-line {
			border-left: 2px solid grey;
			padding-left: 20px;
			margin: 10px 0;
		}

		.post-title {
			font-weight: bold;
			flex-grow: 2;
			margin-bottom: 20px;
		}
		.post-date {
			width: 125px;
		}
		.post-type {
			width: 100px;
			text-align: right;
		}
	}

</style>