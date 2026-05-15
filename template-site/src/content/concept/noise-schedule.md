---
canonical_name: Noise Schedule
description: Choice of beta_t (or alpha_bar_t) that controls how much noise is added
  per step — linear, cosine, sigmoid variants.
ontology_source: discovered
aliases: []
occurrence_count: 56
---
# Noise Schedule

Choice of beta_t (or alpha_bar_t) that controls how much noise is added per step — linear, cosine, sigmoid variants.

**56 occurrences** across courses:

- **diffusion-lm-vizuara** L13 (Lecture 12: Diffusion LLM Noising Schedule) @ 3s — So what we aim to do is as follows. We So what we aim to do is as follows. We
have a true probability distribution, have
- **diffusion-lm-vizuara** L13 (Lecture 12: Diffusion LLM Noising Schedule) @ 57s — an image using a noising schedule maybe an image using a noising schedule maybe
a goshian schedule. The predicting noise
- **diffusion-lm-vizuara** L13 (Lecture 12: Diffusion LLM Noising Schedule) @ 101s — very crucial role. Right? So let's see
how noising is included. how noising is included. how noising is included.
What i
- **diffusion-lm-vizuara** L13 (Lecture 12: Diffusion LLM Noising Schedule) @ 152s — that noise and then when we start with that noise and then when we start with
noise, we can predict the original text no
- **diffusion-lm-vizuara** L13 (Lecture 12: Diffusion LLM Noising Schedule) @ 212s — embedding. So this is a 384 dimensional embedding. So this is a 384 dimensional
vector. vector. vector.
This is a 384 di
- **diffusion-lm-vizuara** L13 (Lecture 12: Diffusion LLM Noising Schedule) @ 284s — this is the true
sentences probability distribution. sentences probability distribution. sentences probability distribut
- **diffusion-lm-vizuara** L13 (Lecture 12: Diffusion LLM Noising Schedule) @ 325s — a portion of this, this is no longer a a portion of this, this is no longer a
true sentence. It becomes a cor, it true s
- **diffusion-lm-vizuara** L13 (Lecture 12: Diffusion LLM Noising Schedule) @ 393s — schedule. Right? So first I define a
time step. Let's say I go from time time step. Let's say I go from time time step. 
- **diffusion-lm-vizuara** L13 (Lecture 12: Diffusion LLM Noising Schedule) @ 462s — going haywire. So maybe initially when
only one mask is added, I go to a lower only one mask is added, I go to a lower o
- **diffusion-lm-vizuara** L13 (Lecture 12: Diffusion LLM Noising Schedule) @ 536s — way it happens in text is that uh at
time equal to 1, you almost have an time equal to 1, you almost have an time equal 
- **diffusion-lm-vizuara** L13 (Lecture 12: Diffusion LLM Noising Schedule) @ 580s — it's a Bernoli distribution. So the
probability of masking is way higher. probability of masking is way higher. probabil
- **diffusion-lm-vizuara** L13 (Lecture 12: Diffusion LLM Noising Schedule) @ 644s — 3,000. Right? Now these are masked. So
this is masked and this is masked. So this is masked and this is masked. So this 
- **diffusion-lm-vizuara** L13 (Lecture 12: Diffusion LLM Noising Schedule) @ 695s — a noisy input with mask tokens. Okay. a noisy input with mask tokens. Okay.
Everything else remains exactly the Everythi
- **diffusion-lm-vizuara** L13 (Lecture 12: Diffusion LLM Noising Schedule) @ 743s — architecture if you compare them side by architecture if you compare them side by
side is the input which goes into this
- **diffusion-lm-vizuara** L13 (Lecture 12: Diffusion LLM Noising Schedule) @ 783s — targets
then we sorry we get the predictions then we sorry we get the predictions then we sorry we get the predictions
t
- **diffusion-lm-vizuara** L13 (Lecture 12: Diffusion LLM Noising Schedule) @ 831s — what is the noising process in the case
of diffusion language models. The next of diffusion language models. The next of
- **diffusion-principles-vizuara** L4 (Lecture 7 - Noise Conditional Score Networks | Principles of Diffusion Models) @ 4s — Hello everyone, welcome to the next Hello everyone, welcome to the next
lecture of the course principles of lecture of t
- **diffusion-principles-vizuara** L4 (Lecture 7 - Noise Conditional Score Networks | Principles of Diffusion Models) @ 67s — calculate the magnetic field for all the
magnets and superimpose them together so magnets and superimpose them together 
- **diffusion-principles-vizuara** L4 (Lecture 7 - Noise Conditional Score Networks | Principles of Diffusion Models) @ 133s — idea where this ball came from. idea where this ball came from.
But we have an idea where it came from. But we have an i
- **diffusion-principles-vizuara** L4 (Lecture 7 - Noise Conditional Score Networks | Principles of Diffusion Models) @ 211s — Okay. And
the force required to pull the ball back the force required to pull the ball back the force required to pull t
- **diffusion-principles-vizuara** L4 (Lecture 7 - Noise Conditional Score Networks | Principles of Diffusion Models) @ 274s — Now this can also be represented as a
noise vector. Right? noise vector. Right? noise vector. Right?
[snorts] This is ou
- **diffusion-principles-vizuara** L4 (Lecture 7 - Noise Conditional Score Networks | Principles of Diffusion Models) @ 337s — And if this perturbed noise is very And if this perturbed noise is very
small, you could assume that whatever small, you
- **diffusion-principles-vizuara** L4 (Lecture 7 - Noise Conditional Score Networks | Principles of Diffusion Models) @ 393s — exactly what we saw here. Minus noise
divided by sigma. divided by sigma. divided by sigma.
And the predicted score is w
- **diffusion-principles-vizuara** L4 (Lecture 7 - Noise Conditional Score Networks | Principles of Diffusion Models) @ 461s — as I said before uh the field of score
matching has evolved matching has evolved matching has evolved
through years. So 
- **diffusion-principles-vizuara** L4 (Lecture 7 - Noise Conditional Score Networks | Principles of Diffusion Models) @ 529s — that.
It's a very beautifully written paper It's a very beautifully written paper It's a very beautifully written paper

- **diffusion-principles-vizuara** L4 (Lecture 7 - Noise Conditional Score Networks | Principles of Diffusion Models) @ 583s — image or data sample into noise and then
we predicted the reverse distribution we predicted the reverse distribution we 
- **diffusion-principles-vizuara** L4 (Lecture 7 - Noise Conditional Score Networks | Principles of Diffusion Models) @ 659s — Now look at what is happening here. Your Now look at what is happening here. Your
space is huge. This is the your entire
- **diffusion-principles-vizuara** L4 (Lecture 7 - Noise Conditional Score Networks | Principles of Diffusion Models) @ 728s — 2005 which we explained and this is the
loss that we try to minimize. Okay. Now
this score is given by gradient of this 
- **diffusion-principles-vizuara** L4 (Lecture 7 - Noise Conditional Score Networks | Principles of Diffusion Models) @ 809s — completely fine. Everything is defined.
This the slope is defined right? You This the slope is defined right? You This t
- **diffusion-principles-vizuara** L4 (Lecture 7 - Noise Conditional Score Networks | Principles of Diffusion Models) @ 867s — score vector will not be defined. score vector will not be defined.
And imagine that you're going with a And imagine tha
- **diffusion-principles-vizuara** L4 (Lecture 7 - Noise Conditional Score Networks | Principles of Diffusion Models) @ 928s — transformed from a low dimensional
manifold to a higher dimensional space. manifold to a higher dimensional space. manif
- **diffusion-principles-vizuara** L4 (Lecture 7 - Noise Conditional Score Networks | Principles of Diffusion Models) @ 1020s — Remember in the previous formulation by Remember in the previous formulation by
Vincent, we just had one noise. Vincent,
- **diffusion-principles-vizuara** L4 (Lecture 7 - Noise Conditional Score Networks | Principles of Diffusion Models) @ 1104s — you are flicking the magnet
not just once with one level, but you're not just once with one level, but you're not just o
- **diffusion-principles-vizuara** L4 (Lecture 7 - Noise Conditional Score Networks | Principles of Diffusion Models) @ 1182s — multiple levels of noise? multiple levels of noise?
We don't do this in diffusion also. In We don't do this in diffusion
- **diffusion-principles-vizuara** L4 (Lecture 7 - Noise Conditional Score Networks | Principles of Diffusion Models) @ 1248s — is it a single neural network which is
trained on trained on trained on
uh for all these losses and if it's a uh for all
- **diffusion-principles-vizuara** L4 (Lecture 7 - Noise Conditional Score Networks | Principles of Diffusion Models) @ 1333s — Remember now the score does not just Remember now the score does not just
depend on X depend on X depend on X
but it dep
- **diffusion-principles-vizuara** L4 (Lecture 7 - Noise Conditional Score Networks | Principles of Diffusion Models) @ 1407s — and land as close as possible to the and land as close as possible to the
data point. Now the interesting thing is that 
- **diffusion-principles-vizuara** L4 (Lecture 7 - Noise Conditional Score Networks | Principles of Diffusion Models) @ 1498s — The only difference is that it is
performed sequentially performed sequentially performed sequentially
multiple times. L
- **diffusion-principles-vizuara** L4 (Lecture 7 - Noise Conditional Score Networks | Principles of Diffusion Models) @ 1581s — Okay. So you are purposely deliberately
inputting a very high noise level so inputting a very high noise level so inputt
- **diffusion-principles-vizuara** L4 (Lecture 7 - Noise Conditional Score Networks | Principles of Diffusion Models) @ 1637s — here [snorts] the destination is not our
data but it's far away from our data data but it's far away from our data data 
- **diffusion-principles-vizuara** L4 (Lecture 7 - Noise Conditional Score Networks | Principles of Diffusion Models) @ 1690s — we are moving according to the lang
dynamics update rule. This time the dynamics update rule. This time the dynamics upd
- **diffusion-principles-vizuara** L4 (Lecture 7 - Noise Conditional Score Networks | Principles of Diffusion Models) @ 1747s — sample the entire data, right? Even if, sample the entire data, right? Even if,
let's say, you have handwritten digits l
- **diffusion-principles-vizuara** L4 (Lecture 7 - Noise Conditional Score Networks | Principles of Diffusion Models) @ 1800s — matching formula that it it it finally
tries to predict the noise itself and tries to predict the noise itself and tries
- **diffusion-principles-vizuara** L4 (Lecture 7 - Noise Conditional Score Networks | Principles of Diffusion Models) @ 1861s — please go through this for people who please go through this for people who
like to see how both are connected and like 
- **diffusion-principles-vizuara** L4 (Lecture 7 - Noise Conditional Score Networks | Principles of Diffusion Models) @ 1934s — uh and then
which is exactly what which is exactly what which is exactly what
we want to predict right we want to we wan
- **diffusion-principles-vizuara** L4 (Lecture 7 - Noise Conditional Score Networks | Principles of Diffusion Models) @ 1992s — the reverse transition kernel is we are the reverse transition kernel is we are
trying to predict how much noise was try
- **diffusion-principles-vizuara** L4 (Lecture 7 - Noise Conditional Score Networks | Principles of Diffusion Models) @ 2049s — when we are inferring we do it n uh we when we are inferring we do it n uh we
do it l times as as we saw here there do i
- **diffusion-principles-vizuara** L4 (Lecture 7 - Noise Conditional Score Networks | Principles of Diffusion Models) @ 2096s — this and you do it for some specific
time steps t so if the time step is time steps t so if the time step is time steps 
- **diffusion-principles-vizuara** L4 (Lecture 7 - Noise Conditional Score Networks | Principles of Diffusion Models) @ 2159s — So this is exactly how the anal So this is exactly how the anal
land dynamics loop looks like. land dynamics loop looks 
- **diffusion-principles-vizuara** L4 (Lecture 7 - Noise Conditional Score Networks | Principles of Diffusion Models) @ 2221s — you
uh define your score network which is uh define your score network which is uh define your score network which is
ty
- **diffusion-principles-vizuara** L4 (Lecture 7 - Noise Conditional Score Networks | Principles of Diffusion Models) @ 2288s — And that is exactly what we see in the
practical U notebook as well. practical U notebook as well. practical U notebook 
- **diffusion-principles-vizuara** L4 (Lecture 7 - Noise Conditional Score Networks | Principles of Diffusion Models) @ 2355s — if I run this inference for this epox
where the loss is very low, you can see where the loss is very low, you can see wh
- **diffusion-principles-vizuara** L4 (Lecture 7 - Noise Conditional Score Networks | Principles of Diffusion Models) @ 2406s — manifold
and by adding noise we are spreading it and by adding noise we are spreading it and by adding noise we are spre
- **diffusion-principles-vizuara** L4 (Lecture 7 - Noise Conditional Score Networks | Principles of Diffusion Models) @ 2448s — which have very low density of of the
data. And adding noise helps us to do data. And adding noise helps us to do data. 
- **diffusion-principles-vizuara** L4 (Lecture 7 - Noise Conditional Score Networks | Principles of Diffusion Models) @ 2501s — strength of low strength also. And once strength of low strength also. And once
we train the network to understand all w
- **diffusion-principles-vizuara** L4 (Lecture 7 - Noise Conditional Score Networks | Principles of Diffusion Models) @ 2556s — images, videos or audio. As an homework, images, videos or audio. As an homework,
I want you to play around with this I 
