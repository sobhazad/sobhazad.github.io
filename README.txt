Sobh's Portfolio - how to preview and deploy
Contents: index.html, assets/ (images), reels/ (videos + posters), serve.py (preview server).
Keep all of them together in one folder.
Preview: run  python3 serve.py  in this folder and open http://localhost:8000
  (do NOT use "python3 -m http.server": it has no Range support, so videos cannot be seeked).
Deploy: upload the whole folder to a host that serves .mp4 with Range requests (most static hosts do).
Contact: the enquiry form was removed. The contact area has Email me (mailto), Copy email, LinkedIn and Behance buttons. To change the address, edit the three places in the #contact section of index.html (visible text, the Available for work link and the Email me button).
Testimonials: the three cards are fictional samples with no label. Replace them with genuine entries in TESTIMONIALS in index.html before launch. Delete all entries and the section is removed.

Gallery movement: social-media, grid, reel-cover and reels galleries advance by one item about every 4-5 seconds while they are on screen. They pause on hover, keyboard focus, touch/drag/scroll (resuming after an idle delay), after arrow clicks, while any viewer/dialog/video is open, in hidden tabs, and when the visitor prefers reduced motion. Each gallery has a small pause/play button. At the end a gallery dissolves back to the first item (no clones, so counters and viewers are unaffected). Timing lives in setup() inside the "gentle automatic movement" block of index.html (every: 4300+ms).
