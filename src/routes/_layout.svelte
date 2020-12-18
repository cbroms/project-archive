<script>
  import Header from '../components/Header.svelte';

  export let segment;
</script>

<div class="layout">
  <Header {segment}/>

  <main>
    <slot></slot>
  </main>

  <footer>
    <hr>
    <span>
     &copy; 2016-{new Date().getFullYear()} Christian Broms
    </span>
  </footer>

</div>


<style>
  .layout {
    margin: 40px;
  }

   hr {
    margin-top: 50px;
    margin-bottom: 20px;
    border: 1px solid grey;
  }

  footer {
    color: grey;
    font-size: 14px;
  }
  
</style>