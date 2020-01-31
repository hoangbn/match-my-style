# MatchMyStyle
## Inspiration
We were inspired by the difficulty of filtering out the clothes we were interested in from all the available options. As a group of motivated undergraduate software developers, we were determined to find a solution.

## What it does
MatchMyStyle intelligently filters brand catalogs using past items from your personal wardrobe that you love. It aims to enhance the shopping experience for both brands and their consumers.

## How we built it
We split our tech stack into three core ecosystems. Our backend ecosystem hosted its own API to communicate with the machine learning model, Cloud Firestore, Firebase Storage and our frontend. Cloud Firestore was used to store our user dataset for training purposes with the ability to add additional images and host them on Firebase Storage.

The ML ecosystem was built using Google Cloud's Vision API and fetched images using Firebase Storage buckets. It learns from images of past items you love from your personal wardrobe to deliver intelligent filters.

Finally, the frontend ecosystem demonstrates the potential that could be achieved by a fashion brand's catalog being coupled with our backend and ML technology to filter the items that matter to an individual user.

## Challenges we ran into
We knew going into this project that we wanted to accomplish something ambitious that could have a tangible impact on people to increase productivity. One of the biggest hurdles we encountered was finding the appropriate tools to facilitate our machine learning routine in a span of 24 hours. Eventually we decided on Google Cloud's Vision API which proved successful.

Our backend was the glue that held the entire project together. Ensuring efficient and robust communication across frontend and the machine learning routine involved many endpoints and moving parts.

Our frontend was our hook that we hoped would show brands and consumers the true potential of our technology. Featuring a custom design made in Figma and developed using JavaScript, React, and CSS, it attempts to demonstrate how our backend and ML ecosystems could be integrated into any brand's pre-existing frontend catalog.

## Accomplishments that we're proud of
We're proud of finishing all of the core ecosystems and showing the potential of MatchMyStyle.

## What we learned
We learned tons in the 24 hours of development. We became more familiar with Google Cloud's Vision API and the services it offers. We worked on our Python / Flask skills and familiarized ourselves with Cloud Firestore, and Firebase Storage. Finally, we improved our design skills and got better at developing more complex frontend code to bring it to life.

## What's next for MatchMyStyle
We would love to see if fashion brands would be interested in our technology and any other ideas they may have on how we could offer value to both them and their consumers.
