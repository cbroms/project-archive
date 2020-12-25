<script context="module">
  export async function preload({ params, query }) {
    // the `slug` parameter is available because
    // this file is called [slug].html
    const res = await this.fetch(`project/${params.slug}.json`);
    const data = await res.json();

    if (res.status === 200) {
      return { post: data };
    } else {
      this.error(res.status, data.message);
    }
  }
</script>

<script>
  import Header from "../../components/Header.svelte"
  export let post
</script>

<svelte:head>
  <title>{post.title}</title>
<!--  Include canonical links to your blog -->
<!--   <link rel="canonical" href="" /> -->
  
<!-- Update content properties with your URL   -->
<!-- 	<meta property="og:url" content=""} /> -->
	<meta property="og:type" content="article" />
	<meta property="og:title" content={post.title} />
	<meta name="Description" content={post.excerpt} />
	<meta property="og:description" content={post.excerpt} />
  
<!--  Link to your preferred image  -->
<!-- 	<meta property="og:image" content="" /> -->
</svelte:head>

<Header path={post.slug}/>

<header>
  <p>{post.printDate}</p>
  <h1>{post.title}</h1>
  <hr />
</header>

<div class="container">
    <article class="content">
      {@html post.html}
    </article>
</div>


<style>
  .container {
    max-width: 640px;
  }
</style>
