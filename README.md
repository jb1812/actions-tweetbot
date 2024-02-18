# An automated Twitter bot using Python and GitHub actions.

![](https://www.google.com/imgres?imgurl=https%3A%2F%2Fi.ytimg.com%2Fvi%2FUGv_bJkF1kg%2Fmaxresdefault.jpg&tbnid=x37lyFIQ7TKclM&vet=12ahUKEwjikrDaprSEAxWy_zgGHdL9C8wQMygCegQIARBa..i&imgrefurl=https%3A%2F%2Fm.youtube.com%2Fwatch%3Fv%3DUGv_bJkF1kg&docid=FrAU96fVt50TDM&w=1280&h=720&q=twitter%20bot%20with%20python&ved=2ahUKEwjikrDaprSEAxWy_zgGHdL9C8wQMygCegQIARBa)

This repository uses GitHub actions to implement Python scripts that tweet random number facts and random cat facts with cat images. The tweets are done from [@Sci_Nuggets](https://x.com/Sci_Nuggets?t=YYwgI7SnRbPlEwcQpJbNOw&s=09) account every hour, at a delay of 15 minutes, between 11:00- 21:00 IST.

- Install all third-party packages from `requirements.txt`
- Use `A.py` to obtain and tweet random number facts using [NumbersAPI](https://rapidapi.com/divad12/api/numbers-1) and [TwitterAPI](https://developer.twitter.com/en/docs/twitter-api).
- Use `B.py` to obtain and tweet random cat facts with cat images using [CatFactsAPI](https://catfact.ninja/), [SefinekAPI](https://api.sefinek.net/) and [Twitter API](https://developer.twitter.com/en/docs/twitter-api).
- Schedule the tweets using GitHub Action in `.github/workflows/actions.yml`
