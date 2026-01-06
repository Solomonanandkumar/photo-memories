document.addEventListener("DOMContentLoaded", function() {
  const albumTiles = document.querySelectorAll(".album");

  albumTiles.forEach(albumEl => {
    const btn = albumEl.querySelector(".album-tile");
    const strip = albumEl.querySelector(".photo-strip");

    btn.addEventListener("click", () => {
      const expanded = btn.getAttribute("aria-expanded") === "true";
      // close any other open album (optional single-open behaviour)
      document.querySelectorAll(".album .photo-strip.open").forEach(s => {
        if (s !== strip) {
          s.classList.remove("open");
          s.previousElementSibling.setAttribute("aria-expanded", "false");
          s.setAttribute("aria-hidden", "true");
        }
      });

      if (expanded) {
        btn.setAttribute("aria-expanded", "false");
        strip.classList.remove("open");
        strip.setAttribute("aria-hidden", "true");
      } else {
        btn.setAttribute("aria-expanded", "true");
        strip.classList.add("open");
        strip.setAttribute("aria-hidden", "false");
        // optional: smooth scroll the album into view
        albumEl.scrollIntoView({behavior: "smooth", block: "nearest"});
      }
    });
  });
});