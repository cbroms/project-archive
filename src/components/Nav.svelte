<script>
  	export let path;
</script>

<nav>
  ~ <a href='/'>archive</a>
  {#if path !== undefined}
  	/ <a href='/project/{path}'>{path}</a>
  {/if}
</nav>
