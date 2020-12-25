<script>
  import Nav from './Nav.svelte'

  export let path = "";
</script>

<header>
  <Nav {path}/>
  <hr>
</header>

<style>
  header {
    margin-bottom: 60px;
  }
  hr {
    margin-top: 20px;
    border: 1px solid grey;
  }
</style>