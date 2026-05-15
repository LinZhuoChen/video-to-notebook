---
canonical_name: SDE Formulation
description: Continuous-time view of diffusion as a stochastic differential equation;
  unifies VE, VP, and sub-VP SDEs.
ontology_source: discovered
aliases: []
occurrence_count: 53
---
# SDE Formulation

Continuous-time view of diffusion as a stochastic differential equation; unifies VE, VP, and sub-VP SDEs.

**53 occurrences** across courses:

- **diffusion-principles-vizuara** L3 (Lecture 8 - Diffusion Models: A Physical Intuition (SDE Framework) | Principles of Diffusion Models) @ 5s — Hello everyone and welcome to the next Hello everyone and welcome to the next
lecture of the course principles of lectur
- **diffusion-principles-vizuara** L3 (Lecture 8 - Diffusion Models: A Physical Intuition (SDE Framework) | Principles of Diffusion Models) @ 69s — looked at other lectures. This is looked at other lectures. This is
supposed to be a standalone lecture to supposed to b
- **diffusion-principles-vizuara** L3 (Lecture 8 - Diffusion Models: A Physical Intuition (SDE Framework) | Principles of Diffusion Models) @ 126s — are going to discuss today. are going to discuss today.
The good thing is that this unified The good thing is that this 
- **diffusion-principles-vizuara** L3 (Lecture 8 - Diffusion Models: A Physical Intuition (SDE Framework) | Principles of Diffusion Models) @ 193s — Okay. So what do we know about
diffusion? In this image diffusion? In this image diffusion? In this image
I have shown a
- **diffusion-principles-vizuara** L3 (Lecture 8 - Diffusion Models: A Physical Intuition (SDE Framework) | Principles of Diffusion Models) @ 277s — Can we or in other words can we recover Can we or in other words can we recover
the original structure? the original str
- **diffusion-principles-vizuara** L3 (Lecture 8 - Diffusion Models: A Physical Intuition (SDE Framework) | Principles of Diffusion Models) @ 329s — shape of the die.
But that is not the case. [snorts] But that is not the case. [snorts] But that is not the case. [snort
- **diffusion-principles-vizuara** L3 (Lecture 8 - Diffusion Models: A Physical Intuition (SDE Framework) | Principles of Diffusion Models) @ 383s — unpredictable. It's it's very random.
It's not moving in a specific direction, It's not moving in a specific direction, 
- **diffusion-principles-vizuara** L3 (Lecture 8 - Diffusion Models: A Physical Intuition (SDE Framework) | Principles of Diffusion Models) @ 450s — So when the dye was diffusing and when So when the dye was diffusing and when
we reversed the whole process, we reversed
- **diffusion-principles-vizuara** L3 (Lecture 8 - Diffusion Models: A Physical Intuition (SDE Framework) | Principles of Diffusion Models) @ 509s — seconds have passed and someone tells me seconds have passed and someone tells me
that Rajett this is the particle which
- **diffusion-principles-vizuara** L3 (Lecture 8 - Diffusion Models: A Physical Intuition (SDE Framework) | Principles of Diffusion Models) @ 569s — physics and AI comes into the picture.
This is a well-known physical property This is a well-known physical property Thi
- **diffusion-principles-vizuara** L3 (Lecture 8 - Diffusion Models: A Physical Intuition (SDE Framework) | Principles of Diffusion Models) @ 633s — Okay. Now let us apply this concept Okay. Now let us apply this concept
to data. to data. to data.
Why are we applying t
- **diffusion-principles-vizuara** L3 (Lecture 8 - Diffusion Models: A Physical Intuition (SDE Framework) | Principles of Diffusion Models) @ 690s — of them have wide eyes.
And the question they ask us is, And the question they ask us is, And the question they ask us i
- **diffusion-principles-vizuara** L3 (Lecture 8 - Diffusion Models: A Physical Intuition (SDE Framework) | Principles of Diffusion Models) @ 755s — when you sample from it, you should get when you sample from it, you should get
something which lies within that somethi
- **diffusion-principles-vizuara** L3 (Lecture 8 - Diffusion Models: A Physical Intuition (SDE Framework) | Principles of Diffusion Models) @ 808s — And to find such distribution we need an
algorithm which is clever enough which algorithm which is clever enough which a
- **diffusion-principles-vizuara** L3 (Lecture 8 - Diffusion Models: A Physical Intuition (SDE Framework) | Principles of Diffusion Models) @ 864s — the diffusion process. Now this is where
it gets very interesting. In the next it gets very interesting. In the next it 
- **diffusion-principles-vizuara** L3 (Lecture 8 - Diffusion Models: A Physical Intuition (SDE Framework) | Principles of Diffusion Models) @ 937s — and then later we recover it.
So we destroy something only to recover So we destroy something only to recover So we dest
- **diffusion-principles-vizuara** L3 (Lecture 8 - Diffusion Models: A Physical Intuition (SDE Framework) | Principles of Diffusion Models) @ 996s — visualize the dye being slowly filling visualize the dye being slowly filling
the liquid and the structure the liquid an
- **diffusion-principles-vizuara** L3 (Lecture 8 - Diffusion Models: A Physical Intuition (SDE Framework) | Principles of Diffusion Models) @ 1053s — do the opposite. In the reverse process,
we will start with noise and then slowly we will start with noise and then slow
- **diffusion-principles-vizuara** L3 (Lecture 8 - Diffusion Models: A Physical Intuition (SDE Framework) | Principles of Diffusion Models) @ 1113s — We have already said that we are going We have already said that we are going
to apply the diffusion process to data. to
- **diffusion-principles-vizuara** L3 (Lecture 8 - Diffusion Models: A Physical Intuition (SDE Framework) | Principles of Diffusion Models) @ 1181s — and you see this motion in a lot of
physical processes you see these motions physical processes you see these motions ph
- **diffusion-principles-vizuara** L3 (Lecture 8 - Diffusion Models: A Physical Intuition (SDE Framework) | Principles of Diffusion Models) @ 1236s — On the right hand side we are zooming in
on specific particles. So here I have on specific particles. So here I have on 
- **diffusion-principles-vizuara** L3 (Lecture 8 - Diffusion Models: A Physical Intuition (SDE Framework) | Principles of Diffusion Models) @ 1295s — So what am I exactly doing here? Well
imagine that instead of these tiny dots imagine that instead of these tiny dots im
- **diffusion-principles-vizuara** L3 (Lecture 8 - Diffusion Models: A Physical Intuition (SDE Framework) | Principles of Diffusion Models) @ 1355s — I'm planning to take all these images,
divide them into pixels and subject each divide them into pixels and subject each
- **diffusion-principles-vizuara** L3 (Lecture 8 - Diffusion Models: A Physical Intuition (SDE Framework) | Principles of Diffusion Models) @ 1423s — two terms a drift term and a noise term. two terms a drift term and a noise term.
So DDPM has a specific formulation for
- **diffusion-principles-vizuara** L3 (Lecture 8 - Diffusion Models: A Physical Intuition (SDE Framework) | Principles of Diffusion Models) @ 1472s — Well, the first thing I can see is that
I can obviously see some current lines I can obviously see some current lines I 
- **diffusion-principles-vizuara** L3 (Lecture 8 - Diffusion Models: A Physical Intuition (SDE Framework) | Principles of Diffusion Models) @ 1524s — a steady drift term which is the current
of the lake or the river and the second of the lake or the river and the second
- **diffusion-principles-vizuara** L3 (Lecture 8 - Diffusion Models: A Physical Intuition (SDE Framework) | Principles of Diffusion Models) @ 1580s — for this forward diffusion. for this forward diffusion.
Okay. So we have converted data to noise Okay. So we have conver
- **diffusion-principles-vizuara** L3 (Lecture 8 - Diffusion Models: A Physical Intuition (SDE Framework) | Principles of Diffusion Models) @ 1638s — You might relate this to a variational You might relate this to a variational
autoenccoder where there is an encoder aut
- **diffusion-principles-vizuara** L3 (Lecture 8 - Diffusion Models: A Physical Intuition (SDE Framework) | Principles of Diffusion Models) @ 1689s — with our discussion with the time
machine. We were asking that can we machine. We were asking that can we machine. We we
- **diffusion-principles-vizuara** L3 (Lecture 8 - Diffusion Models: A Physical Intuition (SDE Framework) | Principles of Diffusion Models) @ 1745s — more than 40 years back in the year 1982
by a single author Brian Anderson. by a single author Brian Anderson. by a sing
- **diffusion-principles-vizuara** L3 (Lecture 8 - Diffusion Models: A Physical Intuition (SDE Framework) | Principles of Diffusion Models) @ 1812s — appreciate all the researchers who spend appreciate all the researchers who spend
a lot of time in writing these papers.
- **diffusion-principles-vizuara** L3 (Lecture 8 - Diffusion Models: A Physical Intuition (SDE Framework) | Principles of Diffusion Models) @ 1859s — of G of T which is the diffusion term in
the forward process. And the second term the forward process. And the second te
- **diffusion-principles-vizuara** L3 (Lecture 8 - Diffusion Models: A Physical Intuition (SDE Framework) | Principles of Diffusion Models) @ 1912s — reversed from noise to the image and reversed from noise to the image and
this is where the learning will happen. this i
- **diffusion-principles-vizuara** L3 (Lecture 8 - Diffusion Models: A Physical Intuition (SDE Framework) | Principles of Diffusion Models) @ 1964s — where the density of the sharks is
maximum. maximum. maximum.
Now score function is exactly like this Now score function
- **diffusion-principles-vizuara** L3 (Lecture 8 - Diffusion Models: A Physical Intuition (SDE Framework) | Principles of Diffusion Models) @ 2024s — density.
Now where does the gradient and log come Now where does the gradient and log come Now where does the gradient a
- **diffusion-principles-vizuara** L3 (Lecture 8 - Diffusion Models: A Physical Intuition (SDE Framework) | Principles of Diffusion Models) @ 2074s — to predict. Remember we started with a
discussion that we want to predict the discussion that we want to predict the dis
- **diffusion-principles-vizuara** L3 (Lecture 8 - Diffusion Models: A Physical Intuition (SDE Framework) | Principles of Diffusion Models) @ 2134s — For now let's simplify things. Let us For now let's simplify things. Let us
assume that the score function is assume tha
- **diffusion-principles-vizuara** L3 (Lecture 8 - Diffusion Models: A Physical Intuition (SDE Framework) | Principles of Diffusion Models) @ 2190s — comprises of the drift in the forward comprises of the drift in the forward
diffusion and the factor which depends diffu
- **diffusion-principles-vizuara** L3 (Lecture 8 - Diffusion Models: A Physical Intuition (SDE Framework) | Principles of Diffusion Models) @ 2246s — ask the question what is the variation ask the question what is the variation
in the values of these two points. It in t
- **diffusion-principles-vizuara** L3 (Lecture 8 - Diffusion Models: A Physical Intuition (SDE Framework) | Principles of Diffusion Models) @ 2295s — in terms of delta t. So if you have
delta t you calculate delta x then you delta t you calculate delta x then you delta 
- **diffusion-principles-vizuara** L3 (Lecture 8 - Diffusion Models: A Physical Intuition (SDE Framework) | Principles of Diffusion Models) @ 2344s — differential equation or an SDE.
This formulation was laid down in a This formulation was laid down in a This formulatio
- **diffusion-principles-vizuara** L3 (Lecture 8 - Diffusion Models: A Physical Intuition (SDE Framework) | Principles of Diffusion Models) @ 2402s — represents the noise term. So we go from
the first iteration to the second the first iteration to the second the first i
- **diffusion-principles-vizuara** L3 (Lecture 8 - Diffusion Models: A Physical Intuition (SDE Framework) | Principles of Diffusion Models) @ 2454s — you because we know the exact equation
of the reverse process and we use that of the reverse process and we use that of 
- **diffusion-principles-vizuara** L3 (Lecture 8 - Diffusion Models: A Physical Intuition (SDE Framework) | Principles of Diffusion Models) @ 2509s — data set consisting only of images of data set consisting only of images of
handwritten digits which are ones and handwr
- **diffusion-principles-vizuara** L3 (Lecture 8 - Diffusion Models: A Physical Intuition (SDE Framework) | Principles of Diffusion Models) @ 2566s — like these handwritten digits.
Okay. So uh we are expecting a biodal Okay. So uh we are expecting a biodal Okay. So uh w
- **diffusion-principles-vizuara** L3 (Lecture 8 - Diffusion Models: A Physical Intuition (SDE Framework) | Principles of Diffusion Models) @ 2621s — in the image follows a brownie in
motion. motion.
Okay. So just like a paint is diffusing Okay. So just like a paint is 
- **diffusion-principles-vizuara** L3 (Lecture 8 - Diffusion Models: A Physical Intuition (SDE Framework) | Principles of Diffusion Models) @ 2680s — trajectory I have shown but in reality
we have these 784 pixels. So it will be we have these 784 pixels. So it will be w
- **diffusion-principles-vizuara** L3 (Lecture 8 - Diffusion Models: A Physical Intuition (SDE Framework) | Principles of Diffusion Models) @ 2731s — Now the next step is we know that the
microscopic brownian motion is microscopic brownian motion is microscopic brownian
- **diffusion-principles-vizuara** L3 (Lecture 8 - Diffusion Models: A Physical Intuition (SDE Framework) | Principles of Diffusion Models) @ 2788s — as well.
And now you can see on the left hand And now you can see on the left hand And now you can see on the left hand

- **diffusion-principles-vizuara** L3 (Lecture 8 - Diffusion Models: A Physical Intuition (SDE Framework) | Principles of Diffusion Models) @ 2836s — diffusion term but this time the
trajectory is spread into two very trajectory is spread into two very trajectory is spr
- **diffusion-principles-vizuara** L3 (Lecture 8 - Diffusion Models: A Physical Intuition (SDE Framework) | Principles of Diffusion Models) @ 2888s — have seen this word score function in
many papers but only after going through many papers but only after going through 
- **diffusion-principles-vizuara** L3 (Lecture 8 - Diffusion Models: A Physical Intuition (SDE Framework) | Principles of Diffusion Models) @ 2939s — using a very simple approach which can using a very simple approach which can
be implemented in Google Collab and uh be 
- **diffusion-principles-vizuara** L3 (Lecture 8 - Diffusion Models: A Physical Intuition (SDE Framework) | Principles of Diffusion Models) @ 2990s — It's a very nicely written paper and
after this introduction you should be after this introduction you should be after t
