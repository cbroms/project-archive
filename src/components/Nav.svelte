<script>
  export let segment;
</script>

<nav>
  ~ <a href='/'>archive</a>
  {#if segment !== undefined}
  	/ <a href='/{segment}'>{segment}</a>
  {/if}
</nav>
