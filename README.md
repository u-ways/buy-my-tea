# Buy My Tea

Just a small script to automate my tea purchase.

## Usage Example

1. Add it as a cron job to run every Tuesday:

```sh
{ crontab -l; echo "30 2 * * TUE python3 path/to/buy-my-tea/main.py"; } | crontab -
```

2. Or run it directly:

```sh
python3 path/to/buy-my-tea/main.py
```

## Background

Where I currently live, there is a small but popular local business that sells [Taiwanese Milk Tea (Bubble Tea)][1]. The business channel is found on Instagram, where they have a link to pre-order your tea of choice using Google forms. (This a common trend where small local businesses start their shop through social media like Instagram) 

## Problem 

Here is the catch:
- The business operates two days a week only. 
- The pre-order form is available one day before the operation date, usually at 2-3 pm.
- There are only 35 cups to serve per operation day. (70 cups per week) 
- This local business has about 1000 organic followers, and so they have to compete to secure one of those precious 35 cups (some buy two or more cups, there is no limit per customer, unfortunately.) 

As a result, the shop sales out in **minutes**. From my observation, the form stays up for 4-6 minutes max before all cups are sold out, and thus pre-ordering is a fierce competition. To my luck, I tried ordering from that shop five weeks straight with no success as I could never be free around the pre-order time slot with 5-6 minutes accuracy. 

It got to the point where I had to text the owner to try some of that tea and the owner was generous enough to allow me to fill the form in advance! (I mean, what kind of grass did they put inside that tea that's making locals fight over it?) 

![Asking to pre-order in advance](/imgs/old_convo.jpg)

Sure enough, it was delicious! However, the problem was not solved. I still cannot find the time (or justify making the time) to spend at least 1 hour glued on my screen to fill in my details and tea of choice within 4-6 minutes.

## Solution

Meet buy-my-tea. The product of years of formal education. If the above text did not explain what this script does, here is a sequence diagram:

![Scripts's sequence diagram](/imgs/buy-my-tea_seq.png)

Years of formal education, well-spent.

![Bubble teas](/imgs/bubble_teas.jpg)

---

**Note**: 
There is no trace of ID for the tea shop to prevent spam.
If you are interested in ordering from the shop, please email me, and I will send you the details.

[1]: https://en.m.wikipedia.org/wiki/Bubble_tea
