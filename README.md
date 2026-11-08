Apex Elite Lending LLC marketing site (static). Edit build.py and run `python3 build.py`.

GitHub Pages publishes the `main` branch (`https://phillipalvaranga-arch.github.io/apex-elite-lending/`). HTML is cached for about 10 minutes. There was no service worker before `apex-elite-v1`. After a content change, bump `ASSET_VERSION` in `build.py` and regenerate so installed browsers drop the previous cache and load the new pages from the network. Reopen or refresh a tablet once after each publish.
