Sobh's Portfolio - how to preview and deploy
Contents: index.html, assets/ (images), reels/ (videos + posters), serve.py (preview server).
Keep all of them together in one folder.
Preview: run  python3 serve.py  in this folder and open http://localhost:8000
  (do NOT use "python3 -m http.server": it has no Range support, so videos cannot be seeked).
Deploy: upload the whole folder to a host that serves .mp4 with Range requests (most static hosts do).
Enquiry form: sends through FormSubmit to sobhazadm@gmail.com. The FIRST submission sends an activation email to that address; click "Activate Form" once. Test it after deploying.
Testimonials: the three cards are fictional samples with no label. Replace them with genuine entries in TESTIMONIALS in index.html before launch. Delete all entries and the section is removed.
