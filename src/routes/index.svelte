<script context="module">
  export function preload({ params, query }) {
    return this.fetch(`index.json`).then(r => r.json()).then(posts => {
      
      const nextYearBreakLookup = {}

      posts.map((post, index) => {
        if (index < posts.length - 1) {
          const nextPost = posts[index + 1] 
          const nextYear = new Date(nextPost.printDate).getFullYear()
          const thisYear = new Date(post.printDate).getFullYear()
          if (nextYear !== thisYear) {
            nextYearBreakLookup[index] = nextYear
          }
        }
      })
      return { posts, nextYearBreakLookup };
    });
  }
</script>

<script>
  import Header from "../components/Header.svelte"
  import ViewPicker from "../components/ViewPicker.svelte"
  import GridListItem from "../components/GridListItem.svelte"
  import GridListYearBreak from "../components/GridListYearBreak.svelte"

  export let posts;
  export let nextYearBreakLookup;

  let view = "list";

  function changeView(newView) {
    view = newView;
  }
</script>

<svelte:head>
  <title>Christian's Project Archive</title>
</svelte:head>

<Header/>

<div>
  <h1>Christian's Project Archive</h1>
  <p>This is a repository of nearly all the projects I've worked on over the past few years. It's mostly a mix of websites, games, experiments, and other assorted articles of interest.</p>
  <ViewPicker {view} {changeView}/>
  <hr>
  <div class="content">
    {#each posts as post, i}
      <GridListItem {post} {view} />
      {#if nextYearBreakLookup[i]}
        <GridListYearBreak year={nextYearBreakLookup[i]} {view}/>
      {/if}
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
    justify-content: space-between;
    max-width: 640px;
  }
 
</style>
