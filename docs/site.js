// Reflex: pequenos ajustes da página (o site funciona sem isto).
(function () {
  // Lembra o idioma escolhido.
  document.querySelectorAll("[data-idioma]").forEach(function (a) {
    a.addEventListener("click", function () {
      try { localStorage.setItem("reflex-idioma", a.getAttribute("data-idioma")); } catch (e) {}
    });
  });

  // Coloca primeiro o download do aparelho que a pessoa está usando.
  var ua = navigator.userAgent || "";
  var so = /Android/i.test(ua) ? "android" : /Windows/i.test(ua) ? "windows" : "";
  if (so) {
    document.documentElement.setAttribute("data-so", so);
    document.querySelectorAll(".botoes, .cartoes").forEach(function (grupo) {
      var item = grupo.querySelector('[data-so="' + so + '"]');
      if (item && item !== grupo.firstElementChild) grupo.insertBefore(item, grupo.firstElementChild);
      if (item && grupo.classList.contains("cartoes")) item.classList.add("cartao-destaque");
    });
  }

  // Mostra a versão mais nova publicada.
  var campos = document.querySelectorAll("[data-versao]");
  if (!campos.length || !window.fetch) return;
  fetch("https://raw.githubusercontent.com/cebratelli-bot/reflex-download/main/arquivos/atualizacao.json", { cache: "no-cache" })
    .then(function (r) { return r.ok ? r.json() : null; })
    .then(function (j) {
      if (!j) return;
      campos.forEach(function (c) {
        var v = j[c.getAttribute("data-versao") + "_versao"];
        if (v) c.textContent = c.textContent.replace(/[\d.]+\s*$/, v);
      });
    })
    .catch(function () {});
})();
