<script>
  import Nav from "./Nav.svelte";

  export let path = "";
</script>

<header>
  <span class="header-thing">Christian Broms</span>
  <nav class="menu">
    <div class="header-thing">
      <a href="https://christianbroms.com">about</a>
      <div class="circle invisible" />
    </div>
    <div class="header-thing">
      <a href="/">projects</a>
      <div class="circle" />
    </div>
  </nav>
</header>
<hr />

<style>
  .circle {
    height: 20px;
    width: 20px;
    margin-left: 15px;
    border-radius: 50%;
    background-color: black;
    display: inline-block;
  }

  .circle.invisible {
    background-color: transparent;
  }

  .header-thing {
    display: flex;
    padding: 5px 0;
  }

  .header-thing > a {
    width: 75px;
    text-align: right;
  }

  header {
    display: flex;
    align-items: flex-end;
    justify-content: space-between;
    max-width: 640px;
  }

  hr {
    margin: 30px 0;
    margin-bottom: 40px;
  }
</style>
