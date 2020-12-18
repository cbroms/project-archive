<script context="module">
  export function preload({ params, query }) {
    return this.fetch(`index.json`).then(r => r.json()).then(posts => {
      return { posts };
    });
  }
</script>

<script>
  import ViewPicker from "../components/ViewPicker.svelte"
  import GridListItem from "../components/GridListItem.svelte"
  export let posts;
  let view = "list";

  function changeView(newView) {
    view = newView;
  }
</script>

<svelte:head>
  <title>Archive</title>
</svelte:head>

<div>
  <h1>Christian's Project Archive</h1>
  <p>This is a repository of nearly all the projects I've worked on over the past few years. It's mostly a mix of websites, games, experiments, and other random articles of interest.</p>
  <ViewPicker {view} {changeView}/>
  <hr>
  <div class="content">
    {#each posts as post}
      <GridListItem {post} {view} />
    {/each}
  </div>
</div>


<style>

  hr {
    margin: 20px 0;
  }
  .content {
    display: flex;
    flex-wrap: wrap;
  }
 
</style>
