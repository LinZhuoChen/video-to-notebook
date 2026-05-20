---
canonical_name: Classifier Guidance
description: Use gradients of a separately trained classifier to steer diffusion sampling
  toward a class.
ontology_source: discovered
aliases: []
occurrence_count: 83
---
# Classifier Guidance

Use gradients of a separately trained classifier to steer diffusion sampling toward a class.

**83 occurrences** across courses:

- **cmu-10799-diffusion-flow** L6 (CMU 10799 S26: Lecture 7 - Guidance & Controllable Generation - Diffusion & Flow Matching) @ 3s — All right. So let's start get started All right. So let's start get started
for the lecture. for the lecture. for the le
- **cmu-10799-diffusion-flow** L6 (CMU 10799 S26: Lecture 7 - Guidance & Controllable Generation - Diffusion & Flow Matching) @ 52s — these things can also speed things up or these things can also speed things up or
get better results. Now we go like uh 
- **cmu-10799-diffusion-flow** L6 (CMU 10799 S26: Lecture 7 - Guidance & Controllable Generation - Diffusion & Flow Matching) @ 107s — and uh one thing about this design space
things is that I misspoke um last time things is that I misspoke um last time t
- **cmu-10799-diffusion-flow** L6 (CMU 10799 S26: Lecture 7 - Guidance & Controllable Generation - Diffusion & Flow Matching) @ 152s — medium time steps rather than at the
beginning or at the end. Any questions beginning or at the end. Any questions begin
- **cmu-10799-diffusion-flow** L6 (CMU 10799 S26: Lecture 7 - Guidance & Controllable Generation - Diffusion & Flow Matching) @ 215s — now we haven't talked about anything
about conditional generation yet. So about conditional generation yet. So about con
- **cmu-10799-diffusion-flow** L6 (CMU 10799 S26: Lecture 7 - Guidance & Controllable Generation - Diffusion & Flow Matching) @ 274s — usually what people would do like the
first thing you would try uh is to first thing you would try uh is to first thing 
- **cmu-10799-diffusion-flow** L6 (CMU 10799 S26: Lecture 7 - Guidance & Controllable Generation - Diffusion & Flow Matching) @ 317s — conditional um sample based on whatever
the condition that you specified right the condition that you specified right th
- **cmu-10799-diffusion-flow** L6 (CMU 10799 S26: Lecture 7 - Guidance & Controllable Generation - Diffusion & Flow Matching) @ 376s — essentially have another feature from
for example maybe another image or like for example maybe another image or like fo
- **cmu-10799-diffusion-flow** L6 (CMU 10799 S26: Lecture 7 - Guidance & Controllable Generation - Diffusion & Flow Matching) @ 420s — norm like we want dark hair or some norm like we want dark hair or some
different hair? different hair? different hair?

- **cmu-10799-diffusion-flow** L6 (CMU 10799 S26: Lecture 7 - Guidance & Controllable Generation - Diffusion & Flow Matching) @ 473s — label condition, right? If if this model
is class label condition then we cannot is class label condition then we cannot
- **cmu-10799-diffusion-flow** L6 (CMU 10799 S26: Lecture 7 - Guidance & Controllable Generation - Diffusion & Flow Matching) @ 525s — like the data collection as we uh may like the data collection as we uh may
know now is like very very expensive know no
- **cmu-10799-diffusion-flow** L6 (CMU 10799 S26: Lecture 7 - Guidance & Controllable Generation - Diffusion & Flow Matching) @ 567s — um which is that basically if you think
about it right the unconditional model about it right the unconditional model ab
- **cmu-10799-diffusion-flow** L6 (CMU 10799 S26: Lecture 7 - Guidance & Controllable Generation - Diffusion & Flow Matching) @ 617s — unconditional model to do conditional unconditional model to do conditional
generation at all? sort of. But there's like
- **cmu-10799-diffusion-flow** L6 (CMU 10799 S26: Lecture 7 - Guidance & Controllable Generation - Diffusion & Flow Matching) @ 677s — probability of the label given the model
or the the image. Right? So if you write or the the image. Right? So if you wri
- **cmu-10799-diffusion-flow** L6 (CMU 10799 S26: Lecture 7 - Guidance & Controllable Generation - Diffusion & Flow Matching) @ 728s — plus a uh the gradient from a
discriminative model. Yeah, discriminative model. Yeah, discriminative model. Yeah,
>> her
- **cmu-10799-diffusion-flow** L6 (CMU 10799 S26: Lecture 7 - Guidance & Controllable Generation - Diffusion & Flow Matching) @ 780s — That's it. And you just run your That's it. And you just run your
sampling as normal and you get a sampling as normal an
- **cmu-10799-diffusion-flow** L6 (CMU 10799 S26: Lecture 7 - Guidance & Controllable Generation - Diffusion & Flow Matching) @ 842s — >> it's a classifier. So it's either like >> it's a classifier. So it's either like
it can be anything. So depending on 
- **cmu-10799-diffusion-flow** L6 (CMU 10799 S26: Lecture 7 - Guidance & Controllable Generation - Diffusion & Flow Matching) @ 886s — training data. You cannot do some
interpolation to generate some other interpolation to generate some other interpolatio
- **cmu-10799-diffusion-flow** L6 (CMU 10799 S26: Lecture 7 - Guidance & Controllable Generation - Diffusion & Flow Matching) @ 929s — like in painting and this is like
colorization. Yeah. So you can just like colorization. Yeah. So you can just like colo
- **cmu-10799-diffusion-flow** L6 (CMU 10799 S26: Lecture 7 - Guidance & Controllable Generation - Diffusion & Flow Matching) @ 982s — need to actually specifically train this
classifier uh to to be able to recognize classifier uh to to be able to recogni
- **cmu-10799-diffusion-flow** L6 (CMU 10799 S26: Lecture 7 - Guidance & Controllable Generation - Diffusion & Flow Matching) @ 1033s — nodding their head. nodding their head.
Oh, someone someone on online. Is that Oh, someone someone on online. Is that Oh
- **cmu-10799-diffusion-flow** L6 (CMU 10799 S26: Lecture 7 - Guidance & Controllable Generation - Diffusion & Flow Matching) @ 1090s — basically just input your um your the
the the less noisy the clean data the the less noisy the clean data the the less n
- **cmu-10799-diffusion-flow** L6 (CMU 10799 S26: Lecture 7 - Guidance & Controllable Generation - Diffusion & Flow Matching) @ 1142s — gradient that you got from your clean
data estimation um and your data estimation um and your data estimation um and you
- **cmu-10799-diffusion-flow** L6 (CMU 10799 S26: Lecture 7 - Guidance & Controllable Generation - Diffusion & Flow Matching) @ 1227s — so, uh, we we took the grade in regards so, uh, we we took the grade in regards
to XT. Uh, but like that's not where the
- **cmu-10799-diffusion-flow** L6 (CMU 10799 S26: Lecture 7 - Guidance & Controllable Generation - Diffusion & Flow Matching) @ 1279s — model and one large size model right so
this thing is just going to takes you this thing is just going to takes you this
- **cmu-10799-diffusion-flow** L6 (CMU 10799 S26: Lecture 7 - Guidance & Controllable Generation - Diffusion & Flow Matching) @ 1326s — like a ball and then the the the noise
level the manifold for each noise level level the manifold for each noise level l
- **cmu-10799-diffusion-flow** L6 (CMU 10799 S26: Lecture 7 - Guidance & Controllable Generation - Diffusion & Flow Matching) @ 1376s — distance from the origin. Uh and then
and then like basically we're going to and then like basically we're going to and 
- **cmu-10799-diffusion-flow** L6 (CMU 10799 S26: Lecture 7 - Guidance & Controllable Generation - Diffusion & Flow Matching) @ 1424s — the manifold at all. So the guided
sample can completely go off the sample can completely go off the sample can complete
- **cmu-10799-diffusion-flow** L6 (CMU 10799 S26: Lecture 7 - Guidance & Controllable Generation - Diffusion & Flow Matching) @ 1470s — these things basically just contribute
to the fact that DPS is really really to the fact that DPS is really really to th
- **cmu-10799-diffusion-flow** L6 (CMU 10799 S26: Lecture 7 - Guidance & Controllable Generation - Diffusion & Flow Matching) @ 1549s — little bit like how do we is there any little bit like how do we is there any
other ways that we can apply guidance. >> 
- **cmu-10799-diffusion-flow** L6 (CMU 10799 S26: Lecture 7 - Guidance & Controllable Generation - Diffusion & Flow Matching) @ 1596s — expensive thing to do. So because the
because the classifier is usually really because the classifier is usually really 
- **cmu-10799-diffusion-flow** L6 (CMU 10799 S26: Lecture 7 - Guidance & Controllable Generation - Diffusion & Flow Matching) @ 1649s — manifold right so what should we do next manifold right so what should we do next
the other very easy thing to do here i
- **cmu-10799-diffusion-flow** L6 (CMU 10799 S26: Lecture 7 - Guidance & Controllable Generation - Diffusion & Flow Matching) @ 1691s — like a property of the like the low low
dimensional manifold. So basically you dimensional manifold. So basically you di
- **cmu-10799-diffusion-flow** L6 (CMU 10799 S26: Lecture 7 - Guidance & Controllable Generation - Diffusion & Flow Matching) @ 1738s — class or something. Uh but basically you
can actually get access to the data can actually get access to the data can act
- **cmu-10799-diffusion-flow** L6 (CMU 10799 S26: Lecture 7 - Guidance & Controllable Generation - Diffusion & Flow Matching) @ 1784s — the like the the yeah the low
dimensional like representation space. dimensional like representation space. dimensional 
- **cmu-10799-diffusion-flow** L6 (CMU 10799 S26: Lecture 7 - Guidance & Controllable Generation - Diffusion & Flow Matching) @ 1832s — samples and label them with noise
levels, right? Nobody. Nobody would do levels, right? Nobody. Nobody would do levels, 
- **cmu-10799-diffusion-flow** L6 (CMU 10799 S26: Lecture 7 - Guidance & Controllable Generation - Diffusion & Flow Matching) @ 1884s — we have one for clean IM. Oh yes yes uh we have one for clean IM. Oh yes yes uh
you can speak up by the way the the you 
- **cmu-10799-diffusion-flow** L6 (CMU 10799 S26: Lecture 7 - Guidance & Controllable Generation - Diffusion & Flow Matching) @ 1922s — to assume that we have access to
autoenccoders? Uh we're going to talk autoenccoders? Uh we're going to talk autoenccode
- **cmu-10799-diffusion-flow** L6 (CMU 10799 S26: Lecture 7 - Guidance & Controllable Generation - Diffusion & Flow Matching) @ 1972s — uh and you can just uh and and this this
algorithm is applicable to all algorithm is applicable to all algorithm is appl
- **cmu-10799-diffusion-flow** L6 (CMU 10799 S26: Lecture 7 - Guidance & Controllable Generation - Diffusion & Flow Matching) @ 2017s — into a text condition model without
training anything by just applying clip training anything by just applying clip trai
- **cmu-10799-diffusion-flow** L6 (CMU 10799 S26: Lecture 7 - Guidance & Controllable Generation - Diffusion & Flow Matching) @ 2069s — go to your classifier, right? So all you
need to do is to take gradient all the need to do is to take gradient all the n
- **cmu-10799-diffusion-flow** L6 (CMU 10799 S26: Lecture 7 - Guidance & Controllable Generation - Diffusion & Flow Matching) @ 2115s — your uh like your your your image. Say your uh like your your your image. Say
for example you have like a gausian blur f
- **cmu-10799-diffusion-flow** L6 (CMU 10799 S26: Lecture 7 - Guidance & Controllable Generation - Diffusion & Flow Matching) @ 2172s — Now that we're in the realm of training Now that we're in the realm of training
free uh guidance, is there any other way
- **cmu-10799-diffusion-flow** L6 (CMU 10799 S26: Lecture 7 - Guidance & Controllable Generation - Diffusion & Flow Matching) @ 2235s — nonisotropic noise um uh yeah sort of
basically it's the same thing right I basically it's the same thing right I basica
- **cmu-10799-diffusion-flow** L6 (CMU 10799 S26: Lecture 7 - Guidance & Controllable Generation - Diffusion & Flow Matching) @ 2277s — so like B and if your model is really so like B and if your model is really
large the it's like a lot of memory large th
- **cmu-10799-diffusion-flow** L6 (CMU 10799 S26: Lecture 7 - Guidance & Controllable Generation - Diffusion & Flow Matching) @ 2362s — >> Okay. The classifier cannot be trained, >> Okay. The classifier cannot be trained,
right? They cannot sample, right? 
- **cmu-10799-diffusion-flow** L6 (CMU 10799 S26: Lecture 7 - Guidance & Controllable Generation - Diffusion & Flow Matching) @ 2414s — called like LGD loss guided diffusion or
something um uh that paper that paper something um uh that paper that paper som
- **cmu-10799-diffusion-flow** L6 (CMU 10799 S26: Lecture 7 - Guidance & Controllable Generation - Diffusion & Flow Matching) @ 2456s — actually a great trick that you should
do. create a proxy distribution. This is do. create a proxy distribution. This is
- **cmu-10799-diffusion-flow** L6 (CMU 10799 S26: Lecture 7 - Guidance & Controllable Generation - Diffusion & Flow Matching) @ 2497s — generated. Um but the problem is we
don't have what we want to generate yet, don't have what we want to generate yet, do
- **cmu-10799-diffusion-flow** L6 (CMU 10799 S26: Lecture 7 - Guidance & Controllable Generation - Diffusion & Flow Matching) @ 2545s — right? So, this needs to have a
condition in it. condition in it. condition in it.
Okay. Hold on. The people on in perso
- **cmu-10799-diffusion-flow** L6 (CMU 10799 S26: Lecture 7 - Guidance & Controllable Generation - Diffusion & Flow Matching) @ 2587s — a really rough uh or preliminary version a really rough uh or preliminary version
of what we want to generate. But the o
- **cmu-10799-diffusion-flow** L6 (CMU 10799 S26: Lecture 7 - Guidance & Controllable Generation - Diffusion & Flow Matching) @ 2658s — that as x0ero. How about that?
It turns out you can definitely do that. It turns out you can definitely do that. It turn
- **cmu-10799-diffusion-flow** L6 (CMU 10799 S26: Lecture 7 - Guidance & Controllable Generation - Diffusion & Flow Matching) @ 2706s — um swapping in as one of the x0 in the um swapping in as one of the x0 in the
middle and just just continue on middle an
- **cmu-10799-diffusion-flow** L6 (CMU 10799 S26: Lecture 7 - Guidance & Controllable Generation - Diffusion & Flow Matching) @ 2759s — like rough ideas of like what do you
want to generate and then just like want to generate and then just like want to gen
- **cmu-10799-diffusion-flow** L6 (CMU 10799 S26: Lecture 7 - Guidance & Controllable Generation - Diffusion & Flow Matching) @ 2809s — to your input and and this way it's to your input and and this way it's
going to create something that like kind going t
- **cmu-10799-diffusion-flow** L6 (CMU 10799 S26: Lecture 7 - Guidance & Controllable Generation - Diffusion & Flow Matching) @ 2855s — looking image from it based on your
pre-trained diffusion model and say like pre-trained diffusion model and say like pr
- **cmu-10799-diffusion-flow** L6 (CMU 10799 S26: Lecture 7 - Guidance & Controllable Generation - Diffusion & Flow Matching) @ 2894s — then the diffusion model can uh the SD
is going to generate something that's is going to generate something that's is go
- **cmu-10799-diffusion-flow** L6 (CMU 10799 S26: Lecture 7 - Guidance & Controllable Generation - Diffusion & Flow Matching) @ 2939s — this is a very terribly masked uh image this is a very terribly masked uh image
but basically you see how like if you do
- **cmu-10799-diffusion-flow** L6 (CMU 10799 S26: Lecture 7 - Guidance & Controllable Generation - Diffusion & Flow Matching) @ 2974s — better masking skills than I do then
then you would have get a better um then you would have get a better um then you wo
- **cmu-10799-diffusion-flow** L6 (CMU 10799 S26: Lecture 7 - Guidance & Controllable Generation - Diffusion & Flow Matching) @ 3029s — majority of the the image is going to be
noise right so you just going to noise right so you just going to noise right s
- **cmu-10799-diffusion-flow** L6 (CMU 10799 S26: Lecture 7 - Guidance & Controllable Generation - Diffusion & Flow Matching) @ 3076s — like how abstract I guess your image is, like how abstract I guess your image is,
um essentially you you will need to um
- **cmu-10799-diffusion-flow** L6 (CMU 10799 S26: Lecture 7 - Guidance & Controllable Generation - Diffusion & Flow Matching) @ 3114s — not never mind um but basically the
reason why this is happening is that um reason why this is happening is that um reas
- **cmu-10799-diffusion-flow** L6 (CMU 10799 S26: Lecture 7 - Guidance & Controllable Generation - Diffusion & Flow Matching) @ 3164s — reconstruct the uh the high frequency
details more and more. And this is why details more and more. And this is why deta
- **cmu-10799-diffusion-flow** L6 (CMU 10799 S26: Lecture 7 - Guidance & Controllable Generation - Diffusion & Flow Matching) @ 3211s — like determine like which time step
should I go and stuff like that which is should I go and stuff like that which is sh
- **cmu-10799-diffusion-flow** L6 (CMU 10799 S26: Lecture 7 - Guidance & Controllable Generation - Diffusion & Flow Matching) @ 3257s — generation uh if you start at time zero generation uh if you start at time zero
which means that there's no diffusion at
- **cmu-10799-diffusion-flow** L6 (CMU 10799 S26: Lecture 7 - Guidance & Controllable Generation - Diffusion & Flow Matching) @ 3311s — people were saying is that like at the people were saying is that like at the
beginning of the diffusion it's like begin
- **cmu-10799-diffusion-flow** L6 (CMU 10799 S26: Lecture 7 - Guidance & Controllable Generation - Diffusion & Flow Matching) @ 3350s — basically what you can do is say you're basically what you can do is say you're
like unhappy with your uh w with this li
- **cmu-10799-diffusion-flow** L6 (CMU 10799 S26: Lecture 7 - Guidance & Controllable Generation - Diffusion & Flow Matching) @ 3386s — steps uh in your longriven dynamic for
you to reach the the good part of the of you to reach the the good part of the of
- **cmu-10799-diffusion-flow** L6 (CMU 10799 S26: Lecture 7 - Guidance & Controllable Generation - Diffusion & Flow Matching) @ 3438s — Yeah.
Could you speak to like theoretical like Could you speak to like theoretical like Could you speak to like theoreti
- **cmu-10799-diffusion-flow** L6 (CMU 10799 S26: Lecture 7 - Guidance & Controllable Generation - Diffusion & Flow Matching) @ 3482s — problem. Yeah, like if you do not train
for this particular task, you just try for this particular task, you just try fo
- **cmu-10799-diffusion-flow** L6 (CMU 10799 S26: Lecture 7 - Guidance & Controllable Generation - Diffusion & Flow Matching) @ 3525s — search based thing like Monte Carlo
research type of type of style type of research type of type of style type of resear
- **cmu-10799-diffusion-flow** L6 (CMU 10799 S26: Lecture 7 - Guidance & Controllable Generation - Diffusion & Flow Matching) @ 3572s — part or the other the part.
>> Oh, so like masking here meaning that >> Oh, so like masking here meaning that >> Oh, so 
- **cmu-10799-diffusion-flow** L6 (CMU 10799 S26: Lecture 7 - Guidance & Controllable Generation - Diffusion & Flow Matching) @ 3626s — learn good information. Uh usually
unconditional models can give you very unconditional models can give you very uncondi
- **cmu-10799-diffusion-flow** L6 (CMU 10799 S26: Lecture 7 - Guidance & Controllable Generation - Diffusion & Flow Matching) @ 3683s — what you can do is if you do a weighted
average of the two the two distributions average of the two the two distribution
- **cmu-10799-diffusion-flow** L6 (CMU 10799 S26: Lecture 7 - Guidance & Controllable Generation - Diffusion & Flow Matching) @ 3736s — conditions that is like that everyone conditions that is like that everyone
has, right? So, for example, like say has, r
- **cmu-10799-diffusion-flow** L6 (CMU 10799 S26: Lecture 7 - Guidance & Controllable Generation - Diffusion & Flow Matching) @ 3780s — score solo you kind of just like do a
weighted mixture of of both. Uh so like weighted mixture of of both. Uh so like we
- **cmu-10799-diffusion-flow** L6 (CMU 10799 S26: Lecture 7 - Guidance & Controllable Generation - Diffusion & Flow Matching) @ 3841s — have your uh input image and then you have your uh input image and then you
can literally just like specify your can lit
- **cmu-10799-diffusion-flow** L6 (CMU 10799 S26: Lecture 7 - Guidance & Controllable Generation - Diffusion & Flow Matching) @ 3882s — you'll have to have both the te the
image and then the text and then extract image and then the text and then extract im
- **cmu-10799-diffusion-flow** L6 (CMU 10799 S26: Lecture 7 - Guidance & Controllable Generation - Diffusion & Flow Matching) @ 3926s — to like map your text into some feature to like map your text into some feature
space and this feature extractor could s
- **cmu-10799-diffusion-flow** L6 (CMU 10799 S26: Lecture 7 - Guidance & Controllable Generation - Diffusion & Flow Matching) @ 3969s — it's uh it it just gets you like clearer
features and this is why it it actually features and this is why it it actually
- **cmu-10799-diffusion-flow** L6 (CMU 10799 S26: Lecture 7 - Guidance & Controllable Generation - Diffusion & Flow Matching) @ 4015s — but all right now you know how to turn but all right now you know how to turn
an unconditional model into a an unconditi
- **cmu-10799-diffusion-flow** L6 (CMU 10799 S26: Lecture 7 - Guidance & Controllable Generation - Diffusion & Flow Matching) @ 4059s — Max. Please come to come in person. If Max. Please come to come in person. If
you want to ask questions, it's going to y
- **cmu-10799-diffusion-flow** L6 (CMU 10799 S26: Lecture 7 - Guidance & Controllable Generation - Diffusion & Flow Matching) @ 4098s — is not final class but like the the
fourth class in the next two weeks we're fourth class in the next two weeks we're fo
