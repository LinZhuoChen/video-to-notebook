---
canonical_name: Score Function
description: Gradient of the log density, ∇_x log p(x); central object of score-based
  generative models.
ontology_source: discovered
aliases: []
occurrence_count: 190
---
# Score Function

Gradient of the log density, ∇_x log p(x); central object of score-based generative models.

**190 occurrences** across courses:

- **cmu-10799-diffusion-flow** L1 (CMU 10799 S26: Lecture 4 - Score-based Models - Diffusion & Flow Matching) @ 4s — So let's begin. Previously last class uh So let's begin. Previously last class uh
we have talked about what is diffusion
- **cmu-10799-diffusion-flow** L1 (CMU 10799 S26: Lecture 4 - Score-based Models - Diffusion & Flow Matching) @ 57s — reserve sorry um all right so just a reserve sorry um all right so just a
reminder what is the forward process reminder 
- **cmu-10799-diffusion-flow** L1 (CMU 10799 S26: Lecture 4 - Score-based Models - Diffusion & Flow Matching) @ 104s — sums up together is another gausian and
you can just sum up a bunch of gausians. you can just sum up a bunch of gausians
- **cmu-10799-diffusion-flow** L1 (CMU 10799 S26: Lecture 4 - Score-based Models - Diffusion & Flow Matching) @ 155s — is the diffusion for process. All right.
Now, uh how now that we uh we have the Now, uh how now that we uh we have the N
- **cmu-10799-diffusion-flow** L1 (CMU 10799 S26: Lecture 4 - Score-based Models - Diffusion & Flow Matching) @ 204s — mean of the gausian uh and in addition
we can actually rewrite this mean this we can actually rewrite this mean this we 
- **cmu-10799-diffusion-flow** L1 (CMU 10799 S26: Lecture 4 - Score-based Models - Diffusion & Flow Matching) @ 248s — last time there's some questions about
why should we do this reparameterization why should we do this reparameterization
- **cmu-10799-diffusion-flow** L1 (CMU 10799 S26: Lecture 4 - Score-based Models - Diffusion & Flow Matching) @ 294s — this uh before I do that does anyone
know in the audience what is normalizing know in the audience what is normalizing k
- **cmu-10799-diffusion-flow** L1 (CMU 10799 S26: Lecture 4 - Score-based Models - Diffusion & Flow Matching) @ 345s — to uh latent is the inverse of the
mapping from latent to data. So this is mapping from latent to data. So this is mappi
- **cmu-10799-diffusion-flow** L1 (CMU 10799 S26: Lecture 4 - Score-based Models - Diffusion & Flow Matching) @ 400s — if you have a auto reggressive models if you have a auto reggressive models
then you need to break things up by the then
- **cmu-10799-diffusion-flow** L1 (CMU 10799 S26: Lecture 4 - Score-based Models - Diffusion & Flow Matching) @ 445s — And uh for normalizing flow just by
looking at this can anyone tell me what looking at this can anyone tell me what look
- **cmu-10799-diffusion-flow** L1 (CMU 10799 S26: Lecture 4 - Score-based Models - Diffusion & Flow Matching) @ 503s — least. Um but then it as we have learned
last time it also has a problem of like last time it also has a problem of like
- **cmu-10799-diffusion-flow** L1 (CMU 10799 S26: Lecture 4 - Score-based Models - Diffusion & Flow Matching) @ 564s — of images rather than actually having to of images rather than actually having to
comput the comput the comput the
>> ye
- **cmu-10799-diffusion-flow** L1 (CMU 10799 S26: Lecture 4 - Score-based Models - Diffusion & Flow Matching) @ 613s — model so what you do is you sort of just
like follow the gra so say suppose you like follow the gra so say suppose you l
- **cmu-10799-diffusion-flow** L1 (CMU 10799 S26: Lecture 4 - Score-based Models - Diffusion & Flow Matching) @ 660s — space right so basically what you can
imagine is that you can start from imagine is that you can start from imagine is t
- **cmu-10799-diffusion-flow** L1 (CMU 10799 S26: Lecture 4 - Score-based Models - Diffusion & Flow Matching) @ 705s — respect to the data point of the log
likelihood so what is happening is that likelihood so what is happening is that lik
- **cmu-10799-diffusion-flow** L1 (CMU 10799 S26: Lecture 4 - Score-based Models - Diffusion & Flow Matching) @ 751s — just like in diffusion right your source
distribution and your target distribution and your target distribution and your
- **cmu-10799-diffusion-flow** L1 (CMU 10799 S26: Lecture 4 - Score-based Models - Diffusion & Flow Matching) @ 808s — gradient of uh of of P
X uh with respect to X. That's fine. But X uh with respect to X. That's fine. But X uh with respe
- **cmu-10799-diffusion-flow** L1 (CMU 10799 S26: Lecture 4 - Score-based Models - Diffusion & Flow Matching) @ 855s — is uh machine learning 101 right. So
very easy very easy uh uh uh very easy very easy uh uh uh very easy very easy uh uh
- **cmu-10799-diffusion-flow** L1 (CMU 10799 S26: Lecture 4 - Score-based Models - Diffusion & Flow Matching) @ 908s — like auto reggressive models. So it can like auto reggressive models. So it can
sample or generate everything all at sam
- **cmu-10799-diffusion-flow** L1 (CMU 10799 S26: Lecture 4 - Score-based Models - Diffusion & Flow Matching) @ 947s — this L2 without this ground truth score.
Turns out you don't even need to use the Turns out you don't even need to use t
- **cmu-10799-diffusion-flow** L1 (CMU 10799 S26: Lecture 4 - Score-based Models - Diffusion & Flow Matching) @ 995s — simplify uh the L2 the the original L2 simplify uh the L2 the the original L2
into two parts here. And then the first in
- **cmu-10799-diffusion-flow** L1 (CMU 10799 S26: Lecture 4 - Score-based Models - Diffusion & Flow Matching) @ 1047s — can have the gradient of uh log of p
with respect to x into you can break it with respect to x into you can break it wit
- **cmu-10799-diffusion-flow** L1 (CMU 10799 S26: Lecture 4 - Score-based Models - Diffusion & Flow Matching) @ 1093s — and then you can basically just get
something like this. So um yeah this is something like this. So um yeah this is some
- **cmu-10799-diffusion-flow** L1 (CMU 10799 S26: Lecture 4 - Score-based Models - Diffusion & Flow Matching) @ 1138s — need to remember is that the second part
of the two things left. It's going to of the two things left. It's going to of 
- **cmu-10799-diffusion-flow** L1 (CMU 10799 S26: Lecture 4 - Score-based Models - Diffusion & Flow Matching) @ 1181s — loss that we get, we don't really need a
ground true score. It's it's like ground true score. It's it's like ground true
- **cmu-10799-diffusion-flow** L1 (CMU 10799 S26: Lecture 4 - Score-based Models - Diffusion & Flow Matching) @ 1238s — function has the same dimensionality of function has the same dimensionality of
the of the data, right? Yeah. So, you th
- **cmu-10799-diffusion-flow** L1 (CMU 10799 S26: Lecture 4 - Score-based Models - Diffusion & Flow Matching) @ 1297s — no one else. Do you have a Do you have a
Do you have a Do you have a Do you have a
>> Well, yes, but it's kind of relate
- **cmu-10799-diffusion-flow** L1 (CMU 10799 S26: Lecture 4 - Score-based Models - Diffusion & Flow Matching) @ 1362s — Literally Gausian. Okay. So basically
what you do is uh and this is what we what you do is uh and this is what we what y
- **cmu-10799-diffusion-flow** L1 (CMU 10799 S26: Lecture 4 - Score-based Models - Diffusion & Flow Matching) @ 1405s — is you just need a sample data and then
perturb it a little bit and now it perturb it a little bit and now it perturb it
- **cmu-10799-diffusion-flow** L1 (CMU 10799 S26: Lecture 4 - Score-based Models - Diffusion & Flow Matching) @ 1455s — literally this. Uh so yeah, for for literally this. Uh so yeah, for for
those of you who wonder why log density those of
- **cmu-10799-diffusion-flow** L1 (CMU 10799 S26: Lecture 4 - Score-based Models - Diffusion & Flow Matching) @ 1525s — truth it's a perturbed ground truth then truth it's a perturbed ground truth then
you may have a question but like let's
- **cmu-10799-diffusion-flow** L1 (CMU 10799 S26: Lecture 4 - Score-based Models - Diffusion & Flow Matching) @ 1564s — anyway it's fine. Um uh so what you do
is you first draw draw a sample from is you first draw draw a sample from is you 
- **cmu-10799-diffusion-flow** L1 (CMU 10799 S26: Lecture 4 - Score-based Models - Diffusion & Flow Matching) @ 1610s — So this is what could have happened if
you do laundry dynamic essentially. So you do laundry dynamic essentially. So you
- **cmu-10799-diffusion-flow** L1 (CMU 10799 S26: Lecture 4 - Score-based Models - Diffusion & Flow Matching) @ 1664s — anyway you just train your model to
predict the score and then you use predict the score and then you use predict the sc
- **cmu-10799-diffusion-flow** L1 (CMU 10799 S26: Lecture 4 - Score-based Models - Diffusion & Flow Matching) @ 1740s — survey. Let's survey. Uh we are starting
from this column again. from this column again. from this column again.
Hello f
- **cmu-10799-diffusion-flow** L1 (CMU 10799 S26: Lecture 4 - Score-based Models - Diffusion & Flow Matching) @ 1806s — haven't been that I haven't been talked haven't been that I haven't been talked
to today. There's so many people in the 
- **cmu-10799-diffusion-flow** L1 (CMU 10799 S26: Lecture 4 - Score-based Models - Diffusion & Flow Matching) @ 1872s — is what we call the manifold
hypothesis. What does it mean is that hypothesis. What does it mean is that hypothesis. Wha
- **cmu-10799-diffusion-flow** L1 (CMU 10799 S26: Lecture 4 - Score-based Models - Diffusion & Flow Matching) @ 1919s — what here says like some area of the what here says like some area of the
data space will not have support. What data sp
- **cmu-10799-diffusion-flow** L1 (CMU 10799 S26: Lecture 4 - Score-based Models - Diffusion & Flow Matching) @ 1963s — manifold from some point from on the
manifold to some point that's not on the manifold to some point that's not on the m
- **cmu-10799-diffusion-flow** L1 (CMU 10799 S26: Lecture 4 - Score-based Models - Diffusion & Flow Matching) @ 2008s — then the second thing. Yeah. Yeah. Yeah.
>> What is this the left plot even showing >> What is this the left plot even s
- **cmu-10799-diffusion-flow** L1 (CMU 10799 S26: Lecture 4 - Score-based Models - Diffusion & Flow Matching) @ 2050s — space or entire data space now has
support uh and then the score matching support uh and then the score matching support
- **cmu-10799-diffusion-flow** L1 (CMU 10799 S26: Lecture 4 - Score-based Models - Diffusion & Flow Matching) @ 2097s — image is eventually boiled down to say
10 features or something in that case 10 features or something in that case 10 fe
- **cmu-10799-diffusion-flow** L1 (CMU 10799 S26: Lecture 4 - Score-based Models - Diffusion & Flow Matching) @ 2145s — there's no probability and that's why there's no probability and that's why
the score is going to blow up and adding the
- **cmu-10799-diffusion-flow** L1 (CMU 10799 S26: Lecture 4 - Score-based Models - Diffusion & Flow Matching) @ 2202s — is like they they they train on the is like they they they train on the
clean data. So it's like not I mean yes clean da
- **cmu-10799-diffusion-flow** L1 (CMU 10799 S26: Lecture 4 - Score-based Models - Diffusion & Flow Matching) @ 2248s — without any data right? So what's going
to happen here is that um so say this is to happen here is that um so say this i
- **cmu-10799-diffusion-flow** L1 (CMU 10799 S26: Lecture 4 - Score-based Models - Diffusion & Flow Matching) @ 2294s — really know where to move in the low
density region. So you're just going to density region. So you're just going to den
- **cmu-10799-diffusion-flow** L1 (CMU 10799 S26: Lecture 4 - Score-based Models - Diffusion & Flow Matching) @ 2342s — high density from higher density right high density from higher density right
so like say this is your like intended so 
- **cmu-10799-diffusion-flow** L1 (CMU 10799 S26: Lecture 4 - Score-based Models - Diffusion & Flow Matching) @ 2388s — >> it it depends on like what exactly is >> it it depends on like what exactly is
this distribution say if this uh this 
- **cmu-10799-diffusion-flow** L1 (CMU 10799 S26: Lecture 4 - Score-based Models - Diffusion & Flow Matching) @ 2434s — Okay.
All right. Any other question? Cool. Cool.
All right. So, we have all these All right. So, we have all these All r
- **cmu-10799-diffusion-flow** L1 (CMU 10799 S26: Lecture 4 - Score-based Models - Diffusion & Flow Matching) @ 2508s — thing doesn't exist anymore, right? And thing doesn't exist anymore, right? And
then now the perturbed like say you have
- **cmu-10799-diffusion-flow** L1 (CMU 10799 S26: Lecture 4 - Score-based Models - Diffusion & Flow Matching) @ 2557s — large of a of a noise, then it you're
just learning a very noisy distribution. just learning a very noisy distribution. 
- **cmu-10799-diffusion-flow** L1 (CMU 10799 S26: Lecture 4 - Score-based Models - Diffusion & Flow Matching) @ 2613s — about which region that we are uh that about which region that we are uh that
we're s we should be sampling at, then we'
- **cmu-10799-diffusion-flow** L1 (CMU 10799 S26: Lecture 4 - Score-based Models - Diffusion & Flow Matching) @ 2659s — sample from, you are going to just
gradually decrease the noise or the gradually decrease the noise or the gradually dec
- **cmu-10799-diffusion-flow** L1 (CMU 10799 S26: Lecture 4 - Score-based Models - Diffusion & Flow Matching) @ 2705s — have that next? uh we have the pseudo
code and you know the long dynam dynamic code and you know the long dynam dynamic 
- **cmu-10799-diffusion-flow** L1 (CMU 10799 S26: Lecture 4 - Score-based Models - Diffusion & Flow Matching) @ 2750s — And then at training time you do this
multi-level den noising score matching multi-level den noising score matching mult
- **cmu-10799-diffusion-flow** L1 (CMU 10799 S26: Lecture 4 - Score-based Models - Diffusion & Flow Matching) @ 2843s — Yeah, just just think about it. Uh,
basically the difference between DDPM, basically the difference between DDPM, basica
- **cmu-10799-diffusion-flow** L1 (CMU 10799 S26: Lecture 4 - Score-based Models - Diffusion & Flow Matching) @ 2928s — that the the the score is sort of it has that the the the score is sort of it has
like another factor or it has another 
- **cmu-10799-diffusion-flow** L1 (CMU 10799 S26: Lecture 4 - Score-based Models - Diffusion & Flow Matching) @ 2989s — we have infinite numbers of noise level? we have infinite numbers of noise level?
What do you what do we think is going 
- **cmu-10799-diffusion-flow** L1 (CMU 10799 S26: Lecture 4 - Score-based Models - Diffusion & Flow Matching) @ 3047s — tailor estimation of of of the real
thing and you can actually write both of thing and you can actually write both of th
- **cmu-10799-diffusion-flow** L1 (CMU 10799 S26: Lecture 4 - Score-based Models - Diffusion & Flow Matching) @ 3102s — because you see how like basically if
you do xt plus delta t minus xt is going you do xt plus delta t minus xt is going 
- **cmu-10799-diffusion-flow** L1 (CMU 10799 S26: Lecture 4 - Score-based Models - Diffusion & Flow Matching) @ 3148s — you just add some stoasticity. So this you just add some stoasticity. So this
is why it's called stochastic is why it's 
- **cmu-10799-diffusion-flow** L1 (CMU 10799 S26: Lecture 4 - Score-based Models - Diffusion & Flow Matching) @ 3208s — and we choose the for process right so
we know f and g uh and then it's we know f and g uh and then it's we know f and g
- **cmu-10799-diffusion-flow** L1 (CMU 10799 S26: Lecture 4 - Score-based Models - Diffusion & Flow Matching) @ 3261s — to use a oiler solver which is like to use a oiler solver which is like
probably simple simplest solver uh that probably
- **cmu-10799-diffusion-flow** L1 (CMU 10799 S26: Lecture 4 - Score-based Models - Diffusion & Flow Matching) @ 3309s — apply the change in x to x and then we apply the change in x to x and then we
apply delta t to t apply delta t to t appl
- **cmu-10799-diffusion-flow** L1 (CMU 10799 S26: Lecture 4 - Score-based Models - Diffusion & Flow Matching) @ 3373s — written as this like this function this written as this like this function this
this uh so there are four process can be
- **cmu-10799-diffusion-flow** L1 (CMU 10799 S26: Lecture 4 - Score-based Models - Diffusion & Flow Matching) @ 3440s — the G as variance and in the VE
formulation we do not have any formulation we do not have any formulation we do not have
- **cmu-10799-diffusion-flow** L1 (CMU 10799 S26: Lecture 4 - Score-based Models - Diffusion & Flow Matching) @ 3489s — did diffusion. This class we did did diffusion. This class we did
scorebased model and we also learned scorebased model 
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
- **diffusion-principles-vizuara** L6 (Lecture 5 - Energy Based Models | Score Function | Principles of Diffusion Models) @ 4s — Hello everyone and welcome to this next Hello everyone and welcome to this next
lecture in of the course principles of l
- **diffusion-principles-vizuara** L6 (Lecture 5 - Energy Based Models | Score Function | Principles of Diffusion Models) @ 75s — of X.
And our objective then becomes to And our objective then becomes to And our objective then becomes to
determine de
- **diffusion-principles-vizuara** L6 (Lecture 5 - Energy Based Models | Score Function | Principles of Diffusion Models) @ 150s — The objective is to match the output
image with the input image as close as image with the input image as close as image
- **diffusion-principles-vizuara** L6 (Lecture 5 - Energy Based Models | Score Function | Principles of Diffusion Models) @ 226s — intelligence can be used to produce intelligence can be used to produce
images which look like they belong to images whi
- **diffusion-principles-vizuara** L6 (Lecture 5 - Energy Based Models | Score Function | Principles of Diffusion Models) @ 282s — it becomes uniform.
We took these key ideas and we We took these key ideas and we We took these key ideas and we
constru
- **diffusion-principles-vizuara** L6 (Lecture 5 - Energy Based Models | Score Function | Principles of Diffusion Models) @ 349s — So you inject noise at every transition.
So this is the first transition, second, So this is the first transition, secon
- **diffusion-principles-vizuara** L6 (Lecture 5 - Energy Based Models | Score Function | Principles of Diffusion Models) @ 405s — So our objective is to minimize the mean So our objective is to minimize the mean
square error between epsilon and epsil
- **diffusion-principles-vizuara** L6 (Lecture 5 - Energy Based Models | Score Function | Principles of Diffusion Models) @ 461s — something which is common in every
single image on earth. And at a first single image on earth. And at a first single im
- **diffusion-principles-vizuara** L6 (Lecture 5 - Energy Based Models | Score Function | Principles of Diffusion Models) @ 516s — in the field of image generation through
generative AI. Models were extremely generative AI. Models were extremely gener
- **diffusion-principles-vizuara** L6 (Lecture 5 - Energy Based Models | Score Function | Principles of Diffusion Models) @ 585s — models in a single cohesive framework. models in a single cohesive framework.
So this is something which is very So this
- **diffusion-principles-vizuara** L6 (Lecture 5 - Energy Based Models | Score Function | Principles of Diffusion Models) @ 648s — So in the energy based models our So in the energy based models our
objective is to predict P5 of X using objective is t
- **diffusion-principles-vizuara** L6 (Lecture 5 - Energy Based Models | Score Function | Principles of Diffusion Models) @ 717s — drop this ball in this curve.
What will happen is that the ball will What will happen is that the ball will What will ha
- **diffusion-principles-vizuara** L6 (Lecture 5 - Energy Based Models | Score Function | Principles of Diffusion Models) @ 777s — down and settle on the ground? The
reason is that at on on on the ground reason is that at on on on the ground reason is
- **diffusion-principles-vizuara** L6 (Lecture 5 - Energy Based Models | Score Function | Principles of Diffusion Models) @ 835s — energy function can be a proxy for how energy function can be a proxy for how
probable that particular data point or pro
- **diffusion-principles-vizuara** L6 (Lecture 5 - Energy Based Models | Score Function | Principles of Diffusion Models) @ 892s — course draw this schematically and we
can say that okay we want this energy or can say that okay we want this energy or 
- **diffusion-principles-vizuara** L6 (Lecture 5 - Energy Based Models | Score Function | Principles of Diffusion Models) @ 951s — my function should satisfy my function should satisfy
and people use an exponential function and people use an exponenti
- **diffusion-principles-vizuara** L6 (Lecture 5 - Energy Based Models | Score Function | Principles of Diffusion Models) @ 1023s — density as p5 of x. density as p5 of x.
Then from the above graph we can find Then from the above graph we can find Then
- **diffusion-principles-vizuara** L6 (Lecture 5 - Energy Based Models | Score Function | Principles of Diffusion Models) @ 1076s — system u every system finally tries to
go in a position with the minimum go in a position with the minimum go in a posit
- **diffusion-principles-vizuara** L6 (Lecture 5 - Energy Based Models | Score Function | Principles of Diffusion Models) @ 1126s — the whole idea behind energy based
models models
okay now let us discuss after this point okay now let us discuss after 
- **diffusion-principles-vizuara** L6 (Lecture 5 - Energy Based Models | Score Function | Principles of Diffusion Models) @ 1200s — add up to one? We need the probability
to add up to one because if we are to add up to one because if we are to add up t
- **diffusion-principles-vizuara** L6 (Lecture 5 - Energy Based Models | Score Function | Principles of Diffusion Models) @ 1252s — so let's let's take that example again. so let's let's take that example again.
Uh let's say you have a dice. Okay. Uh U
- **diffusion-principles-vizuara** L6 (Lecture 5 - Energy Based Models | Score Function | Principles of Diffusion Models) @ 1302s — and the solution is that we can simply and the solution is that we can simply
normalize the probabilities by dividing no
- **diffusion-principles-vizuara** L6 (Lecture 5 - Energy Based Models | Score Function | Principles of Diffusion Models) @ 1368s — So for the discrete states it looked So for the discrete states it looked
like this summation of e ra to e5 of x like th
- **diffusion-principles-vizuara** L6 (Lecture 5 - Energy Based Models | Score Function | Principles of Diffusion Models) @ 1426s — energy based models. In other words, how
do we find these energy functions which do we find these energy functions which
- **diffusion-principles-vizuara** L6 (Lecture 5 - Energy Based Models | Score Function | Principles of Diffusion Models) @ 1498s — push the good data up. push the good data up.
So I want to move this curve like this. So I want to move this curve like 
- **diffusion-principles-vizuara** L6 (Lecture 5 - Energy Based Models | Score Function | Principles of Diffusion Models) @ 1549s — higher probability. All of us understand higher probability. All of us understand
this. this. this.
Now we will again us
- **diffusion-principles-vizuara** L6 (Lecture 5 - Energy Based Models | Score Function | Principles of Diffusion Models) @ 1607s — Uh here E5 of X denotes the energy
function. Okay. So now if you break this down, Okay. So now if you break this down,
t
- **diffusion-principles-vizuara** L6 (Lecture 5 - Energy Based Models | Score Function | Principles of Diffusion Models) @ 1680s — so p5 of x can be written as integral of
p5 of x given z into p of z dz. p5 of x given z into p of z dz. p5 of x given z
- **diffusion-principles-vizuara** L6 (Lecture 5 - Energy Based Models | Score Function | Principles of Diffusion Models) @ 1740s — bypasses the partition function.
So you might be thinking that what is So you might be thinking that what is So you migh
- **diffusion-principles-vizuara** L6 (Lecture 5 - Energy Based Models | Score Function | Principles of Diffusion Models) @ 1796s — And because of that we come up with a
alternative objective function which alternative objective function which alternat
- **diffusion-principles-vizuara** L6 (Lecture 5 - Energy Based Models | Score Function | Principles of Diffusion Models) @ 1865s — appreciation for people who actually sit appreciation for people who actually sit
down, they do the mathematics and they
- **diffusion-principles-vizuara** L6 (Lecture 5 - Energy Based Models | Score Function | Principles of Diffusion Models) @ 1937s — to occur. to occur.
Let's let let's take a sample example. Let's let let's take a sample example. Let's let let's take a
- **diffusion-principles-vizuara** L6 (Lecture 5 - Energy Based Models | Score Function | Principles of Diffusion Models) @ 1998s — score function does. It tells you the score function does. It tells you the
direction to where the data is located. dire
- **diffusion-principles-vizuara** L6 (Lecture 5 - Energy Based Models | Score Function | Principles of Diffusion Models) @ 2049s — know where the data is where the score
is the maximum is the maximum is the maximum
we can start from any point and fina
- **diffusion-principles-vizuara** L6 (Lecture 5 - Energy Based Models | Score Function | Principles of Diffusion Models) @ 2098s — trajectory?
Is is is it can I define it? Can I write Is is is it can I define it? Can I write Is is is it can I define i
- **diffusion-principles-vizuara** L6 (Lecture 5 - Energy Based Models | Score Function | Principles of Diffusion Models) @ 2158s — Let's say I calculate the score for this Let's say I calculate the score for this
point. Where will this score point poi
- **diffusion-principles-vizuara** L6 (Lecture 5 - Energy Based Models | Score Function | Principles of Diffusion Models) @ 2213s — right or the left uh the value will
decline at x= to infinity or minus decline at x= to infinity or minus decline at x= 
- **diffusion-principles-vizuara** L6 (Lecture 5 - Energy Based Models | Score Function | Principles of Diffusion Models) @ 2275s — Now this is just the first term. We have
to take a gradient of this also. to take a gradient of this also. to take a gra
- **diffusion-principles-vizuara** L6 (Lecture 5 - Energy Based Models | Score Function | Principles of Diffusion Models) @ 2324s — So uh this is what we get if we actually
plot the score function. You can see plot the score function. You can see plot 
- **diffusion-principles-vizuara** L6 (Lecture 5 - Energy Based Models | Score Function | Principles of Diffusion Models) @ 2381s — score-based framework but score-based framework but
score-based methods score-based methods score-based methods
is somet
- **diffusion-principles-vizuara** L6 (Lecture 5 - Energy Based Models | Score Function | Principles of Diffusion Models) @ 2440s — challenges which we started out with. We
wanted something which can uh help us wanted something which can uh help us wan
- **diffusion-principles-vizuara** L6 (Lecture 5 - Energy Based Models | Score Function | Principles of Diffusion Models) @ 2529s — Now what what happens is that when you
take this gradient uh the the first term take this gradient uh the the first term
- **diffusion-principles-vizuara** L6 (Lecture 5 - Energy Based Models | Score Function | Principles of Diffusion Models) @ 2586s — that's all.
So the partition function becomes zero So the partition function becomes zero So the partition function beco
- **diffusion-principles-vizuara** L6 (Lecture 5 - Energy Based Models | Score Function | Principles of Diffusion Models) @ 2642s — makes sure that the score of the
predicted model matches the score of the predicted model matches the score of the predi
- **diffusion-principles-vizuara** L6 (Lecture 5 - Energy Based Models | Score Function | Principles of Diffusion Models) @ 2733s — So ideally we want
a loss which looks like this. Now the a loss which looks like this. Now the a loss which looks like t
- **diffusion-principles-vizuara** L6 (Lecture 5 - Energy Based Models | Score Function | Principles of Diffusion Models) @ 2782s — Let us assume that we have done the
training. We have matched this score training. We have matched this score training. 
- **diffusion-principles-vizuara** L6 (Lecture 5 - Energy Based Models | Score Function | Principles of Diffusion Models) @ 2829s — data point and I know where to go I can
navigate my way and I can find samples navigate my way and I can find samples na
- **diffusion-principles-vizuara** L6 (Lecture 5 - Energy Based Models | Score Function | Principles of Diffusion Models) @ 2898s — Here I can visually see that this is the
deepest valley and I can see the deepest valley and I can see the deepest valle
- **diffusion-principles-vizuara** L6 (Lecture 5 - Energy Based Models | Score Function | Principles of Diffusion Models) @ 2950s — valley and I start here. and I want to
reach the bottom of the valley. So I'll reach the bottom of the valley. So I'll r
- **diffusion-principles-vizuara** L6 (Lecture 5 - Energy Based Models | Score Function | Principles of Diffusion Models) @ 3012s — would get your next location.
But what is the slope here? How do we But what is the slope here? How do we But what is th
- **diffusion-principles-vizuara** L6 (Lecture 5 - Energy Based Models | Score Function | Principles of Diffusion Models) @ 3067s — exactly what we are doing here. We are exactly what we are doing here. We are
calculating the gradient of the energy cal
- **diffusion-principles-vizuara** L6 (Lecture 5 - Energy Based Models | Score Function | Principles of Diffusion Models) @ 3119s — this which is gradient of the energy
function. So the negative of this function. So the negative of this function. So th
- **diffusion-principles-vizuara** L6 (Lecture 5 - Energy Based Models | Score Function | Principles of Diffusion Models) @ 3172s — gradient is zero. So you are just
sitting there but there is another pit sitting there but there is another pit sitting 
- **diffusion-principles-vizuara** L6 (Lecture 5 - Energy Based Models | Score Function | Principles of Diffusion Models) @ 3220s — need to provide a shake which gives you
enough random energy to kick you out of enough random energy to kick you out of 
- **diffusion-principles-vizuara** L6 (Lecture 5 - Energy Based Models | Score Function | Principles of Diffusion Models) @ 3269s — we are sampling from a gshian we are sampling from a gshian
distribution with a mean of xi and a distribution with a mea
- **diffusion-principles-vizuara** L6 (Lecture 5 - Energy Based Models | Score Function | Principles of Diffusion Models) @ 3330s — the total variance of this xt + 1 is
maybe a constant or it's just one that maybe a constant or it's just one that maybe
- **diffusion-principles-vizuara** L6 (Lecture 5 - Energy Based Models | Score Function | Principles of Diffusion Models) @ 3392s — Now we what we do is we replace this Now we what we do is we replace this
grad of energy by s of x which we have grad of
- **diffusion-principles-vizuara** L6 (Lecture 5 - Energy Based Models | Score Function | Principles of Diffusion Models) @ 3436s — trajectory let's say I start from here
with this update I'll go like this with this update I'll go like this with this u
- **diffusion-principles-vizuara** L6 (Lecture 5 - Energy Based Models | Score Function | Principles of Diffusion Models) @ 3479s — the score function which takes you from
one location to the another and finally one location to the another and finally 
- **diffusion-principles-vizuara** L6 (Lecture 5 - Energy Based Models | Score Function | Principles of Diffusion Models) @ 3535s — x is known to us. It looks something
like this. The probability of finding like this. The probability of finding like th
- **diffusion-principles-vizuara** L6 (Lecture 5 - Energy Based Models | Score Function | Principles of Diffusion Models) @ 3595s — comments.
So first we define the setup which are So first we define the setup which are So first we define the setup whi
- **diffusion-principles-vizuara** L6 (Lecture 5 - Energy Based Models | Score Function | Principles of Diffusion Models) @ 3640s — noise. We use the exact same equation
which we discuss in theory which we discuss in theory which we discuss in theory
a
- **diffusion-principles-vizuara** L6 (Lecture 5 - Energy Based Models | Score Function | Principles of Diffusion Models) @ 3688s — It's it's called a drunk hiker.
It's like someone is drunk and walking It's like someone is drunk and walking It's like 
- **diffusion-principles-vizuara** L6 (Lecture 5 - Energy Based Models | Score Function | Principles of Diffusion Models) @ 3738s — So I want all of you to run this tweak a
little things here and there have fun little things here and there have fun lit
- **diffusion-principles-vizuara** L6 (Lecture 5 - Energy Based Models | Score Function | Principles of Diffusion Models) @ 3795s — since sampling with langu dynamics only
requires the score like we saw in this requires the score like we saw in this re
- **diffusion-principles-vizuara** L6 (Lecture 5 - Energy Based Models | Score Function | Principles of Diffusion Models) @ 3867s — and score matching fits this vector and score matching fits this vector
field by minimizing the mean square field by min
- **diffusion-principles-vizuara** L6 (Lecture 5 - Energy Based Models | Score Function | Principles of Diffusion Models) @ 3940s — know how to pronounce this name.
uh however they they came up with a uh however they they came up with a uh however they
- **diffusion-principles-vizuara** L6 (Lecture 5 - Energy Based Models | Score Function | Principles of Diffusion Models) @ 4007s — a summation of this and a constant.
So basically minimizing this meant that So basically minimizing this meant that So b
- **diffusion-principles-vizuara** L6 (Lecture 5 - Energy Based Models | Score Function | Principles of Diffusion Models) @ 4081s — like this. A1 A2 A3
A4 A5 A6 A4 A5 A6 A4 A5 A6
A7 A8 and A9. So the trace of this A7 A8 and A9. So the trace of this A7 
- **diffusion-principles-vizuara** L6 (Lecture 5 - Energy Based Models | Score Function | Principles of Diffusion Models) @ 4151s — uh it is it is completely fine for our uh it is it is completely fine for our
purposes what we need to understand is pur
- **diffusion-principles-vizuara** L6 (Lecture 5 - Energy Based Models | Score Function | Principles of Diffusion Models) @ 4205s — Which makes a lot of sense, right? In Which makes a lot of sense, right? In
the previous example that we looked at the p
- **diffusion-principles-vizuara** L6 (Lecture 5 - Energy Based Models | Score Function | Principles of Diffusion Models) @ 4274s — where we are trying to make the data
samples appear as syncs. samples appear as syncs. samples appear as syncs.
which is
- **diffusion-principles-vizuara** L6 (Lecture 5 - Energy Based Models | Score Function | Principles of Diffusion Models) @ 4327s — more to this term.
So the this term drives So the this term drives So the this term drives
scores to zero in the higher 
- **diffusion-principles-vizuara** L6 (Lecture 5 - Energy Based Models | Score Function | Principles of Diffusion Models) @ 4381s — Now uh once we have understood this, Now uh once we have understood this,
this is where the actual training of the this 
- **diffusion-principles-vizuara** L6 (Lecture 5 - Energy Based Models | Score Function | Principles of Diffusion Models) @ 4437s — distribution. So in a way we will take a
look at the whole uh whole pipeline. look at the whole uh whole pipeline. look 
- **diffusion-principles-vizuara** L6 (Lecture 5 - Energy Based Models | Score Function | Principles of Diffusion Models) @ 4518s — loss is made up of two terms. The first loss is made up of two terms. The first
is the trace of the Jacobian is the trac
- **diffusion-principles-vizuara** L6 (Lecture 5 - Energy Based Models | Score Function | Principles of Diffusion Models) @ 4570s — predictions for the x score and the y
score to create a vector. score to create a vector. score to create a vector.
Next
- **diffusion-principles-vizuara** L6 (Lecture 5 - Energy Based Models | Score Function | Principles of Diffusion Models) @ 4620s — completely appear like a sync but there completely appear like a sync but there
are arrows coming in from the left and a
- **diffusion-principles-vizuara** L6 (Lecture 5 - Energy Based Models | Score Function | Principles of Diffusion Models) @ 4669s — we go to any other point. So we are we go to any other point. So we are
going to see trajectories like these. going to s
- **diffusion-principles-vizuara** L6 (Lecture 5 - Energy Based Models | Score Function | Principles of Diffusion Models) @ 4713s — perturve ourselves from the valleys so perturve ourselves from the valleys so
that we don't miss any other treasures tha
- **diffusion-principles-vizuara** L6 (Lecture 5 - Energy Based Models | Score Function | Principles of Diffusion Models) @ 4759s — them yet. We will make the connection in
the next lecture. the next lecture. the next lecture.
So initially used to enab
- **diffusion-principles-vizuara** L6 (Lecture 5 - Energy Based Models | Score Function | Principles of Diffusion Models) @ 4815s — Scores are given by gradient of
logarithm of uh the probability. It logarithm of uh the probability. It logarithm of uh 
- **diffusion-principles-vizuara** L6 (Lecture 5 - Energy Based Models | Score Function | Principles of Diffusion Models) @ 4862s — neural network to match the scores and neural network to match the scores and
to do that we use a score matching loss to
