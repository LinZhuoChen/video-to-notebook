---
canonical_name: Score Matching
description: Training objective for learning the score function without knowing the
  normalising constant.
ontology_source: discovered
aliases: []
occurrence_count: 154
---
# Score Matching

Training objective for learning the score function without knowing the normalising constant.

**154 occurrences** across courses:

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
- **cmu-10799-diffusion-flow** L9 (CMU 10799 S26: Lecture 10 - Distillation, Consistency Models & Flow Maps - Diffusion & Flow Matching) @ 2837s — otherwise it doesn't make sense I guess.
Yeah. >> Yeah. Oh sorry. Yeah. >> Yeah. Oh sorry. Yeah.
>> How do you weigh the
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
- **diffusion-principles-vizuara** L5 (Lecture 6 - Denoising Score Matching | Principles of Diffusion Models) @ 3s — Hello everyone, welcome to the next Hello everyone, welcome to the next
lecture of the course principles of lecture of t
- **diffusion-principles-vizuara** L5 (Lecture 6 - Denoising Score Matching | Principles of Diffusion Models) @ 75s — in space and you go in that space with a
compass which tells you which direction compass which tells you which direction
- **diffusion-principles-vizuara** L5 (Lecture 6 - Denoising Score Matching | Principles of Diffusion Models) @ 165s — probability distribution. Right? So we
do not know this term. do not know this term. do not know this term.
In supervise
- **diffusion-principles-vizuara** L5 (Lecture 6 - Denoising Score Matching | Principles of Diffusion Models) @ 234s — requirement of this entire probability requirement of this entire probability
distribution which we have no idea distrib
- **diffusion-principles-vizuara** L5 (Lecture 6 - Denoising Score Matching | Principles of Diffusion Models) @ 307s — data which is available to us which is
what makes it incredibly powerful. So we are grateful to this author to So we are
- **diffusion-principles-vizuara** L5 (Lecture 6 - Denoising Score Matching | Principles of Diffusion Models) @ 368s — is close to the sink is pulled inwards. is close to the sink is pulled inwards.
It's like a black hole. If you go near a
- **diffusion-principles-vizuara** L5 (Lecture 6 - Denoising Score Matching | Principles of Diffusion Models) @ 411s — Now assume that you you are close to the
data. Assume that you are the data data. Assume that you are the data data. Ass
- **diffusion-principles-vizuara** L5 (Lecture 6 - Denoising Score Matching | Principles of Diffusion Models) @ 468s — for this training data at every single for this training data at every single
point in the space. You can see the point 
- **diffusion-principles-vizuara** L5 (Lecture 6 - Denoising Score Matching | Principles of Diffusion Models) @ 530s — So just if you look at this visually you
can see that wherever I start in the can see that wherever I start in the can s
- **diffusion-principles-vizuara** L5 (Lecture 6 - Denoising Score Matching | Principles of Diffusion Models) @ 602s — function? So and even we have looked at
one example where uh the loss function one example where uh the loss function on
- **diffusion-principles-vizuara** L5 (Lecture 6 - Denoising Score Matching | Principles of Diffusion Models) @ 679s — the diagonal elements. You can't the diagonal elements. You can't
individually calculate the diagonal individually calcu
- **diffusion-principles-vizuara** L5 (Lecture 6 - Denoising Score Matching | Principles of Diffusion Models) @ 757s — in in real life use cases. And that is
why for a lot of for many years actually why for a lot of for many years actually
- **diffusion-principles-vizuara** L5 (Lecture 6 - Denoising Score Matching | Principles of Diffusion Models) @ 840s — the same word dn noising right and in
diffusion that made sense because we diffusion that made sense because we diffusio
- **diffusion-principles-vizuara** L5 (Lecture 6 - Denoising Score Matching | Principles of Diffusion Models) @ 910s — These three papers are going to form the
foundation of the theory of denoising foundation of the theory of denoising fou
- **diffusion-principles-vizuara** L5 (Lecture 6 - Denoising Score Matching | Principles of Diffusion Models) @ 982s — formulation which was trackable. But
that did not make sense because the that did not make sense because the that did no
- **diffusion-principles-vizuara** L5 (Lecture 6 - Denoising Score Matching | Principles of Diffusion Models) @ 1062s — and you do have access to some of them.
So let's say you have access to 15 or 20 So let's say you have access to 15 or 2
- **diffusion-principles-vizuara** L5 (Lecture 6 - Denoising Score Matching | Principles of Diffusion Models) @ 1128s — nearest magnet is pulling me. If I take
a point here I could say that this is a point here I could say that this is a po
- **diffusion-principles-vizuara** L5 (Lecture 6 - Denoising Score Matching | Principles of Diffusion Models) @ 1185s — uh I will I will superimpose the uh I will I will superimpose the
magnetic fields for all these different magnetic field
- **diffusion-principles-vizuara** L5 (Lecture 6 - Denoising Score Matching | Principles of Diffusion Models) @ 1251s — We take any magnet on the table and we We take any magnet on the table and we
flick it with a hand just like this. I'm f
- **diffusion-principles-vizuara** L5 (Lecture 6 - Denoising Score Matching | Principles of Diffusion Models) @ 1309s — the student, look, this is the ball's
new location. new location. new location.
and we hide the original uh magnet and w
- **diffusion-principles-vizuara** L5 (Lecture 6 - Denoising Score Matching | Principles of Diffusion Models) @ 1382s — student has no idea where this
new ball position came from. But we know new ball position came from. But we know new bal
- **diffusion-principles-vizuara** L5 (Lecture 6 - Denoising Score Matching | Principles of Diffusion Models) @ 1442s — balls, all these magnets that you know balls, all these magnets that you know
that the magnets are placed there. You tha
- **diffusion-principles-vizuara** L5 (Lecture 6 - Denoising Score Matching | Principles of Diffusion Models) @ 1502s — this point should be should move so that
it goes back to the original position it goes back to the original position it 
- **diffusion-principles-vizuara** L5 (Lecture 6 - Denoising Score Matching | Principles of Diffusion Models) @ 1579s — to a new location. to a new location.
So the noisy new spot is represented as So the noisy new spot is represented as So
- **diffusion-principles-vizuara** L5 (Lecture 6 - Denoising Score Matching | Principles of Diffusion Models) @ 1642s — score does exactly the same thing. The
score tells you the direction score tells you the direction score tells you the d
- **diffusion-principles-vizuara** L5 (Lecture 6 - Denoising Score Matching | Principles of Diffusion Models) @ 1722s — of mistakes but the feedback is given of mistakes but the feedback is given
from this. This is the true direction from t
- **diffusion-principles-vizuara** L5 (Lecture 6 - Denoising Score Matching | Principles of Diffusion Models) @ 1799s — It is not like your true It is not like your true
probability distribution of data which probability distribution of dat
- **diffusion-principles-vizuara** L5 (Lecture 6 - Denoising Score Matching | Principles of Diffusion Models) @ 1860s — given any point in space
how can I pull this point so that it how can I pull this point so that it how can I pull this p
- **diffusion-principles-vizuara** L5 (Lecture 6 - Denoising Score Matching | Principles of Diffusion Models) @ 1922s — really making sense. I have an excellent really making sense. I have an excellent
explanation to that which will come so
- **diffusion-principles-vizuara** L5 (Lecture 6 - Denoising Score Matching | Principles of Diffusion Models) @ 1985s — perturvation to the data. We can
simplify the score function which we simplify the score function which we simplify the 
- **diffusion-principles-vizuara** L5 (Lecture 6 - Denoising Score Matching | Principles of Diffusion Models) @ 2054s — uh the mean of this pixel is centered at uh the mean of this pixel is centered at
0.5 because the value is 0.5 but then 
- **diffusion-principles-vizuara** L5 (Lecture 6 - Denoising Score Matching | Principles of Diffusion Models) @ 2136s — And uh in fact
this can be represented this can be represented this can be represented
using a standard normal distribut
- **diffusion-principles-vizuara** L5 (Lecture 6 - Denoising Score Matching | Principles of Diffusion Models) @ 2215s — expression for this probability
distribution. distribution. distribution.
And uh because it is tractable once we And uh 
- **diffusion-principles-vizuara** L5 (Lecture 6 - Denoising Score Matching | Principles of Diffusion Models) @ 2276s — anything is whatever is there in the
exponential itself. So you get this at exponential itself. So you get this at expon
- **diffusion-principles-vizuara** L5 (Lecture 6 - Denoising Score Matching | Principles of Diffusion Models) @ 2347s — you you you might have thought why
didn't I guess it before because it it didn't I guess it before because it it didn't 
- **diffusion-principles-vizuara** L5 (Lecture 6 - Denoising Score Matching | Principles of Diffusion Models) @ 2418s — predict we are trying to match the noise
the noise vector which has been added in the noise vector which has been added 
- **diffusion-principles-vizuara** L5 (Lecture 6 - Denoising Score Matching | Principles of Diffusion Models) @ 2482s — which means that the density is maximum
near somewhere around this maybe minus4 near somewhere around this maybe minus4 
- **diffusion-principles-vizuara** L5 (Lecture 6 - Denoising Score Matching | Principles of Diffusion Models) @ 2575s — So this is the neural network that we So this is the neural network that we
define and the loss function is the main def
- **diffusion-principles-vizuara** L5 (Lecture 6 - Denoising Score Matching | Principles of Diffusion Models) @ 2631s — Okay. And now what is the target score?
The target score is something which The target score is something which The targ
- **diffusion-principles-vizuara** L5 (Lecture 6 - Denoising Score Matching | Principles of Diffusion Models) @ 2699s — And uh finally you see the learned score And uh finally you see the learned score
function which looks something like fu
- **diffusion-principles-vizuara** L5 (Lecture 6 - Denoising Score Matching | Principles of Diffusion Models) @ 2756s — magnet. magnet.
Similarly, if you are somewhere on the Similarly, if you are somewhere on the Similarly, if you are some
- **diffusion-principles-vizuara** L5 (Lecture 6 - Denoising Score Matching | Principles of Diffusion Models) @ 2802s — left you reach magnet number one. If you
are on the far right, you reach magnet are on the far right, you reach magnet a
- **diffusion-principles-vizuara** L5 (Lecture 6 - Denoising Score Matching | Principles of Diffusion Models) @ 2852s — We first add a noise and then we try to We first add a noise and then we try to
predict that noise. predict that noise. 
- **diffusion-principles-vizuara** L5 (Lecture 6 - Denoising Score Matching | Principles of Diffusion Models) @ 2914s — us away from the local minima so that we
explore the global minimas as well. explore the global minimas as well. explore
- **diffusion-principles-vizuara** L5 (Lecture 6 - Denoising Score Matching | Principles of Diffusion Models) @ 2975s — much of a difference. Something might be much of a difference. Something might be
happening in the 3D space right that h
- **diffusion-principles-vizuara** L5 (Lecture 6 - Denoising Score Matching | Principles of Diffusion Models) @ 3026s — Okay. So this is it for dnoising score
matching and uh in the next part matching and uh in the next part matching and uh
