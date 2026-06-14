CragSnap — prototype
====================

What it does
------------
Upload a climbing photo. The app reads the GPS location saved inside the
photo, finds the climbing areas/boulders near that spot (using the free,
open-source OpenBeta climbing database), and lists the routes there — each
linking straight to its Mountain Project page.

It also has two fallbacks if a photo has no location saved:
  • "Use my current location" (only useful if you're standing at the crag)
  • "Try a sample" (loads a real spot near Flagstaff, Boulder CO — great for testing)

How to open it NOW (on your Mac)
--------------------------------
Double-click "index.html". It opens in your browser.
Click "Try a sample" to see it pull real routes. That works immediately.

(Note: uploading a photo to read its GPS also works locally. The
"current location" button needs the page to be hosted over https — see below.)

How to use it on your PHONE
---------------------------
Phones need the page served over https. The easiest free way, no account:
  1. Go to  https://app.netlify.com/drop
  2. Drag this whole "crag-snap" folder onto the page.
  3. You get a public https link — open THAT on your phone.
Then upload a climbing photo you took, and it'll use the photo's location.

Important honest notes
----------------------
• Data comes from OpenBeta, NOT Mountain Project. Mountain Project shut off
  outside access to their data in 2020. OpenBeta is the legal, open
  alternative — it has fewer routes than MP, so some areas may be missing.
• GPS gets you to the right cliff/boulder, but can be off by 10-30 ft, so
  the closest crag is a strong guess, not a guarantee.
• Automatically picking the EXACT route from the image (computer vision) is
  a future feature, not in this prototype.

Files
-----
index.html  — the whole app (this is the only file that matters)
serve.py    — a tiny local web server, only used for testing
README.txt  — this file
