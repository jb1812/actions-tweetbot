# An automated Twitter bot using Python and GitHub actions.

This repository uses GitHub actions to implement Python scripts that tweet random number facts and random cat facts with cat images. The tweets are done from [@Sci_Nuggets](https://x.com/Sci_Nuggets?t=YYwgI7SnRbPlEwcQpJbNOw&s=09) account every hour, at a delay of 15 minutes, between 11:00- 21:00 IST.

- Install all third-party packages from `requirements.txt`
- Use `A.py` to obtain and tweet random number facts using [NumbersAPI](https://rapidapi.com/divad12/api/numbers-1) and [TwitterAPI](https://developer.twitter.com/en/docs/twitter-api).
- Use `B.py` to obtain and tweet random cat facts with cat images using [CatFactsAPI](https://catfact.ninja/), [SefinekAPI](https://api.sefinek.net/) and [Twitter API](https://developer.twitter.com/en/docs/twitter-api).
- Schedule the tweets using GitHub Action in `.github/workflows/actions.yml`
