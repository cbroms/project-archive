<div class="layout">
  <main>
    <slot></slot>
  </main>

  <footer>
    <hr />
    <span class="footer-thing">
      &copy; 2016-{new Date().getFullYear()} Christian Broms
    </span>
    <span class="footer-thing"
      >~
      <a
        href="https://christianbroms.com"
        target="_blank"
        rel="noopener noreferrer"
        >about</a
      ></span
    >
    <span class="footer-thing">
      ~
      <a href="/">archive</a>
    </span>
    <span class="footer-thing">
      ~
      <a
        href="https://github.com/cbroms"
        target="_blank"
        rel="noopener noreferrer"
        >code</a
      >
    </span>
  </footer>
</div>

<style>
  .layout {
    margin: 40px;
  }

  .footer-thing {
    padding-right: 10px;
    padding-top: 10px;
    display: inline-block;
  }

  .footer-thing > a {
    color: #636363;
  }

  hr {
    margin-top: 50px;
    margin-bottom: 20px;
    border: 1px solid #636363;
    background-color: #636363;
  }

  footer {
    color: #636363;
    font-size: 14px;
  }
</style>
