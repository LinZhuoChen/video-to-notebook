---
canonical_name: Reparameterization Trick
description: Express stochastic sampling as a deterministic function of input + noise
  so gradients can flow.
ontology_source: discovered
aliases: []
occurrence_count: 91
---
# Reparameterization Trick

Express stochastic sampling as a deterministic function of input + noise so gradients can flow.

**91 occurrences** across courses:

- **diffusion-principles-vizuara** L9 (Lecture 2 - Variational Autoencoders Explained From Scratch | Principles of Diffusion Models) @ 5s — Hello everyone and welcome to the second Hello everyone and welcome to the second
lecture of the course principles of le
- **diffusion-principles-vizuara** L9 (Lecture 2 - Variational Autoencoders Explained From Scratch | Principles of Diffusion Models) @ 77s — from scratch. from scratch.
And this lecture is And this lecture is And this lecture is
going to be very important for t
- **diffusion-principles-vizuara** L9 (Lecture 2 - Variational Autoencoders Explained From Scratch | Principles of Diffusion Models) @ 139s — with the understanding of VAS. with the understanding of VAS.
So first we'll take a simple example. So first we'll take 
- **diffusion-principles-vizuara** L9 (Lecture 2 - Variational Autoencoders Explained From Scratch | Principles of Diffusion Models) @ 199s — in cursive. Some of us
u don't write in cursive. So there are a u don't write in cursive. So there are a u don't write i
- **diffusion-principles-vizuara** L9 (Lecture 2 - Variational Autoencoders Explained From Scratch | Principles of Diffusion Models) @ 266s — Then another time you press a button.
Another time you get another hello. This Another time you get another hello. This 
- **diffusion-principles-vizuara** L9 (Lecture 2 - Variational Autoencoders Explained From Scratch | Principles of Diffusion Models) @ 335s — such that or generate a machine such
that the samples drawn from that machine that the samples drawn from that machine t
- **diffusion-principles-vizuara** L9 (Lecture 2 - Variational Autoencoders Explained From Scratch | Principles of Diffusion Models) @ 405s — factors that determine the style of the factors that determine the style of the
handwriting. handwriting. handwriting.
S
- **diffusion-principles-vizuara** L9 (Lecture 2 - Variational Autoencoders Explained From Scratch | Principles of Diffusion Models) @ 483s — So my first intuition is that okay fine So my first intuition is that okay fine
my first job is to figure out all these 
- **diffusion-principles-vizuara** L9 (Lecture 2 - Variational Autoencoders Explained From Scratch | Principles of Diffusion Models) @ 542s — final shape of the handwriting. final shape of the handwriting.
So once you capture the secret recipe So once you captur
- **diffusion-principles-vizuara** L9 (Lecture 2 - Variational Autoencoders Explained From Scratch | Principles of Diffusion Models) @ 597s — machine looks as follows. machine looks as follows.
Secret recipe is given as an input to Secret recipe is given as an i
- **diffusion-principles-vizuara** L9 (Lecture 2 - Variational Autoencoders Explained From Scratch | Principles of Diffusion Models) @ 652s — interesting, right? It it it looks like
okay fine this this it it makes a lot of okay fine this this it it makes a lot o
- **diffusion-principles-vizuara** L9 (Lecture 2 - Variational Autoencoders Explained From Scratch | Principles of Diffusion Models) @ 713s — now um in the rest of this lecture we We now um in the rest of this lecture we We
are going to assume that are going to 
- **diffusion-principles-vizuara** L9 (Lecture 2 - Variational Autoencoders Explained From Scratch | Principles of Diffusion Models) @ 774s — not know these factors beforehand. That
is why they are called as latent is why they are called as latent is why they ar
- **diffusion-principles-vizuara** L9 (Lecture 2 - Variational Autoencoders Explained From Scratch | Principles of Diffusion Models) @ 831s — y-axis is represented by the symbol zed
2. Zed1 stands for slantness of the 2. Zed1 stands for slantness of the 2. Zed1 
- **diffusion-principles-vizuara** L9 (Lecture 2 - Variational Autoencoders Explained From Scratch | Principles of Diffusion Models) @ 888s — below it's it's not neat.
So I have made some spelling mistake So I have made some spelling mistake So I have made some 
- **diffusion-principles-vizuara** L9 (Lecture 2 - Variational Autoencoders Explained From Scratch | Principles of Diffusion Models) @ 933s — mapping which I was talking about. For mapping which I was talking about. For
example, if you pick a point here, you exa
- **diffusion-principles-vizuara** L9 (Lecture 2 - Variational Autoencoders Explained From Scratch | Principles of Diffusion Models) @ 991s — in your class. in your class.
So this is also called as the So this is also called as the So this is also called as the

- **diffusion-principles-vizuara** L9 (Lecture 2 - Variational Autoencoders Explained From Scratch | Principles of Diffusion Models) @ 1057s — typical handwriting typical handwriting
let's say it is divided into 28x 28 let's say it is divided into 28x 28 let's sa
- **diffusion-principles-vizuara** L9 (Lecture 2 - Variational Autoencoders Explained From Scratch | Principles of Diffusion Models) @ 1119s — latent space is has a mean of zero and a latent space is has a mean of zero and a
standard deviation of one or any other
- **diffusion-principles-vizuara** L9 (Lecture 2 - Variational Autoencoders Explained From Scratch | Principles of Diffusion Models) @ 1167s — So for now what we have seen is that we
have this general architecture for the have this general architecture for the ha
- **diffusion-principles-vizuara** L9 (Lecture 2 - Variational Autoencoders Explained From Scratch | Principles of Diffusion Models) @ 1234s — another word for this machine which is
called as decoder. called as decoder. called as decoder.
Let us quickly summarize
- **diffusion-principles-vizuara** L9 (Lecture 2 - Variational Autoencoders Explained From Scratch | Principles of Diffusion Models) @ 1304s — vary. So here you can see that as the
yellow dot moves around the Latin space, yellow dot moves around the Latin space, 
- **diffusion-principles-vizuara** L9 (Lecture 2 - Variational Autoencoders Explained From Scratch | Principles of Diffusion Models) @ 1364s — next. So far we have used the decoder to
generate samples from the latent generate samples from the latent generate samp
- **diffusion-principles-vizuara** L9 (Lecture 2 - Variational Autoencoders Explained From Scratch | Principles of Diffusion Models) @ 1435s — we create a latent space with the latent
variables. So just as before we assume variables. So just as before we assume v
- **diffusion-principles-vizuara** L9 (Lecture 2 - Variational Autoencoders Explained From Scratch | Principles of Diffusion Models) @ 1494s — know. [snorts]
Now let's say we have chosen a point in Now let's say we have chosen a point in Now let's say we have cho
- **diffusion-principles-vizuara** L9 (Lecture 2 - Variational Autoencoders Explained From Scratch | Principles of Diffusion Models) @ 1556s — we can represent digit 5 as a bunch of we can represent digit 5 as a bunch of
pixels pixels pixels
which are divided as 
- **diffusion-principles-vizuara** L9 (Lecture 2 - Variational Autoencoders Explained From Scratch | Principles of Diffusion Models) @ 1628s — five, if you closely look at it, it it
does look like a five. It's it's it's does look like a five. It's it's it's does 
- **diffusion-principles-vizuara** L9 (Lecture 2 - Variational Autoencoders Explained From Scratch | Principles of Diffusion Models) @ 1688s — is that with this approach we will get a
fixed shape of five every time but we fixed shape of five every time but we fix
- **diffusion-principles-vizuara** L9 (Lecture 2 - Variational Autoencoders Explained From Scratch | Principles of Diffusion Models) @ 1750s — restricted to zero and one. You are open
to the possibility of to the possibility of to the possibility of
a color which
- **diffusion-principles-vizuara** L9 (Lecture 2 - Variational Autoencoders Explained From Scratch | Principles of Diffusion Models) @ 1808s — the decoder does not give a single value
but for every pixel the decoder gives but for every pixel the decoder gives but
- **diffusion-principles-vizuara** L9 (Lecture 2 - Variational Autoencoders Explained From Scratch | Principles of Diffusion Models) @ 1873s — deterministic approach only.
So now let us So now let us So now let us
have a simple example to understand how have a si
- **diffusion-principles-vizuara** L9 (Lecture 2 - Variational Autoencoders Explained From Scratch | Principles of Diffusion Models) @ 1936s — So the decoder is nothing but a neural
network which is trained to take inputs network which is trained to take inputs n
- **diffusion-principles-vizuara** L9 (Lecture 2 - Variational Autoencoders Explained From Scratch | Principles of Diffusion Models) @ 1991s — somewhere towards the right, which means
that it has to be a bit bright and the that it has to be a bit bright and the t
- **diffusion-principles-vizuara** L9 (Lecture 2 - Variational Autoencoders Explained From Scratch | Principles of Diffusion Models) @ 2050s — now we have covered now we have covered
one part of the story which explains the one part of the story which explains th
- **diffusion-principles-vizuara** L9 (Lecture 2 - Variational Autoencoders Explained From Scratch | Principles of Diffusion Models) @ 2110s — part, you will understand that we have
made a major assumption. made a major assumption. made a major assumption.
Rememb
- **diffusion-principles-vizuara** L9 (Lecture 2 - Variational Autoencoders Explained From Scratch | Principles of Diffusion Models) @ 2174s — recipe and then you need to map all
these handwriting styles to the secret these handwriting styles to the secret these 
- **diffusion-principles-vizuara** L9 (Lecture 2 - Variational Autoencoders Explained From Scratch | Principles of Diffusion Models) @ 2233s — the latin space to access to generate the latin space to access to generate
digit five. One option is to access all digi
- **diffusion-principles-vizuara** L9 (Lecture 2 - Variational Autoencoders Explained From Scratch | Principles of Diffusion Models) @ 2284s — Wouldn't it be better if we knew which
part of the Latin space to access for part of the Latin space to access for part 
- **diffusion-principles-vizuara** L9 (Lecture 2 - Variational Autoencoders Explained From Scratch | Principles of Diffusion Models) @ 2340s — decoder.
So the overall architecture looks like So the overall architecture looks like So the overall architecture looks
- **diffusion-principles-vizuara** L9 (Lecture 2 - Variational Autoencoders Explained From Scratch | Principles of Diffusion Models) @ 2400s — this architecture is very similar to a
plain autoenccoder where you have an plain autoenccoder where you have an plain a
- **diffusion-principles-vizuara** L9 (Lecture 2 - Variational Autoencoders Explained From Scratch | Principles of Diffusion Models) @ 2463s — a dis or or a region which is the most a dis or or a region which is the most
probable region of finding the digit proba
- **diffusion-principles-vizuara** L9 (Lecture 2 - Variational Autoencoders Explained From Scratch | Principles of Diffusion Models) @ 2521s — we are going to look at a nice visual we are going to look at a nice visual
description to understand this much descript
- **diffusion-principles-vizuara** L9 (Lecture 2 - Variational Autoencoders Explained From Scratch | Principles of Diffusion Models) @ 2592s — individual points. So 99% of these
points, they they produce garbage. So points, they they produce garbage. So points, t
- **diffusion-principles-vizuara** L9 (Lecture 2 - Variational Autoencoders Explained From Scratch | Principles of Diffusion Models) @ 2654s — regions which tell you that this is the
region corresponding to the dog. This is region corresponding to the dog. This i
- **diffusion-principles-vizuara** L9 (Lecture 2 - Variational Autoencoders Explained From Scratch | Principles of Diffusion Models) @ 2708s — space which is continuous and the space which is continuous and the
garbage gaps are now filled with garbage gaps are no
- **diffusion-principles-vizuara** L9 (Lecture 2 - Variational Autoencoders Explained From Scratch | Principles of Diffusion Models) @ 2767s — So the two stories put together form the
variational autoenccoder. variational autoenccoder.
We first looked at the deco
- **diffusion-principles-vizuara** L9 (Lecture 2 - Variational Autoencoders Explained From Scratch | Principles of Diffusion Models) @ 2823s — the areas in the latin space? How do you
know which levers to pull in the know which levers to pull in the know which le
- **diffusion-principles-vizuara** L9 (Lecture 2 - Variational Autoencoders Explained From Scratch | Principles of Diffusion Models) @ 2888s — uh styles of the students when they uh styles of the students when they
wrote the word hello or the handwritten wrote th
- **diffusion-principles-vizuara** L9 (Lecture 2 - Variational Autoencoders Explained From Scratch | Principles of Diffusion Models) @ 2949s — going to give you the latent space
distribution given the image. So that's distribution given the image. So that's distr
- **diffusion-principles-vizuara** L9 (Lecture 2 - Variational Autoencoders Explained From Scratch | Principles of Diffusion Models) @ 3009s — the encoder like this and the decoder the encoder like this and the decoder
going from a smaller line here to a going fr
- **diffusion-principles-vizuara** L9 (Lecture 2 - Variational Autoencoders Explained From Scratch | Principles of Diffusion Models) @ 3076s — these variational autoenccoders trained.
How do you train these to generate How do you train these to generate How do yo
- **diffusion-principles-vizuara** L9 (Lecture 2 - Variational Autoencoders Explained From Scratch | Principles of Diffusion Models) @ 3125s — and then sample from it. So we are going
to take a real example in the next class to take a real example in the next cla
- **diffusion-principles-vizuara** L9 (Lecture 2 - Variational Autoencoders Explained From Scratch | Principles of Diffusion Models) @ 3176s — is not deterministic but rather it is is not deterministic but rather it is
probabilistic. probabilistic. probabilistic.
- **diffusion-principles-vizuara** L9 (Lecture 2 - Variational Autoencoders Explained From Scratch | Principles of Diffusion Models) @ 3228s — image which is generated at the end.
This is all that is happening in the This is all that is happening in the This is a
- **diffusion-principles-vizuara** L9 (Lecture 2 - Variational Autoencoders Explained From Scratch | Principles of Diffusion Models) @ 3304s — tells you the hidden factors of
variation behind that image. variation behind that image. variation behind that image.
[
- **diffusion-principles-vizuara** L9 (Lecture 2 - Variational Autoencoders Explained From Scratch | Principles of Diffusion Models) @ 3370s — can lie. So it appears to be a very can lie. So it appears to be a very
smart and a clever machine. smart and a clever m
- **diffusion-principles-vizuara** L9 (Lecture 2 - Variational Autoencoders Explained From Scratch | Principles of Diffusion Models) @ 3431s — the final image should be as close as
possible to the original image. So you possible to the original image. So you poss
- **diffusion-principles-vizuara** L9 (Lecture 2 - Variational Autoencoders Explained From Scratch | Principles of Diffusion Models) @ 3490s — encode and the second neural network is
the machine which learns to decode. the machine which learns to decode. the mach
- **diffusion-principles-vizuara** L9 (Lecture 2 - Variational Autoencoders Explained From Scratch | Principles of Diffusion Models) @ 3560s — a dot like this and you pass it to the a dot like this and you pass it to the
decoder and you get a value of zero decode
- **diffusion-principles-vizuara** L9 (Lecture 2 - Variational Autoencoders Explained From Scratch | Principles of Diffusion Models) @ 3607s — our predicted distribution which should
match as close as possible to the true match as close as possible to the true ma
- **diffusion-principles-vizuara** L9 (Lecture 2 - Variational Autoencoders Explained From Scratch | Principles of Diffusion Models) @ 3679s — points in the latin space which is also
given in this formula. given in this formula. given in this formula.
I I don't w
- **diffusion-principles-vizuara** L9 (Lecture 2 - Variational Autoencoders Explained From Scratch | Principles of Diffusion Models) @ 3741s — the visualization before where we saw
that it's like finding or that it's like finding or that it's like finding or
samp
- **diffusion-principles-vizuara** L9 (Lecture 2 - Variational Autoencoders Explained From Scratch | Principles of Diffusion Models) @ 3797s — that point being real?
And this actually does not even make use And this actually does not even make use And this actual
- **diffusion-principles-vizuara** L9 (Lecture 2 - Variational Autoencoders Explained From Scratch | Principles of Diffusion Models) @ 3866s — Now the question is that what is the Now the question is that what is the
elbow objective? [snorts] elbow objective? [sn
- **diffusion-principles-vizuara** L9 (Lecture 2 - Variational Autoencoders Explained From Scratch | Principles of Diffusion Models) @ 3925s — I will not get very mathematical here
and I will not focus too much on the and I will not focus too much on the and I wi
- **diffusion-principles-vizuara** L9 (Lecture 2 - Variational Autoencoders Explained From Scratch | Principles of Diffusion Models) @ 3984s — So this essentially says that
whatever image you're looking at the end whatever image you're looking at the end whatever
- **diffusion-principles-vizuara** L9 (Lecture 2 - Variational Autoencoders Explained From Scratch | Principles of Diffusion Models) @ 4053s — in any fashion but
in more realistic settings the in more realistic settings the in more realistic settings the
distribu
- **diffusion-principles-vizuara** L9 (Lecture 2 - Variational Autoencoders Explained From Scratch | Principles of Diffusion Models) @ 4110s — will be average in terms of the will be average in terms of the
slantness, in terms of the neatness etc. slantness, in t
- **diffusion-principles-vizuara** L9 (Lecture 2 - Variational Autoencoders Explained From Scratch | Principles of Diffusion Models) @ 4172s — how likely is the reconstructed
um output. um output. um output.
What is the probability of that? And we What is the pro
- **diffusion-principles-vizuara** L9 (Lecture 2 - Variational Autoencoders Explained From Scratch | Principles of Diffusion Models) @ 4235s — our encoder distribution to stay as
close as possible to a gshian which close as possible to a gshian which close as pos
- **diffusion-principles-vizuara** L9 (Lecture 2 - Variational Autoencoders Explained From Scratch | Principles of Diffusion Models) @ 4298s — want to compress the earth cat into
something which captures the essence of something which captures the essence of some
- **diffusion-principles-vizuara** L9 (Lecture 2 - Variational Autoencoders Explained From Scratch | Principles of Diffusion Models) @ 4350s — objective and we try to maximize the
elbow. elbow. elbow.
So since the true objective is always So since the true object
- **diffusion-principles-vizuara** L9 (Lecture 2 - Variational Autoencoders Explained From Scratch | Principles of Diffusion Models) @ 4407s — want to move our code to the yellow
distribution. We want to move it as distribution. We want to move it as distribution
- **diffusion-principles-vizuara** L9 (Lecture 2 - Variational Autoencoders Explained From Scratch | Principles of Diffusion Models) @ 4463s — what remains and it makes sense from an what remains and it makes sense from an
intuitive standpoint because later intui
- **diffusion-principles-vizuara** L9 (Lecture 2 - Variational Autoencoders Explained From Scratch | Principles of Diffusion Models) @ 4520s — going to come together very nicely in
this last practical example. Our task is this last practical example. Our task is 
- **diffusion-principles-vizuara** L9 (Lecture 2 - Variational Autoencoders Explained From Scratch | Principles of Diffusion Models) @ 4581s — hidden factors which we have absolutely hidden factors which we have absolutely
no clue what they are but the encoder is
- **diffusion-principles-vizuara** L9 (Lecture 2 - Variational Autoencoders Explained From Scratch | Principles of Diffusion Models) @ 4633s — So remember our decoder setup looks like
this. It's it it needs to take the this. It's it it needs to take the this. It'
- **diffusion-principles-vizuara** L9 (Lecture 2 - Variational Autoencoders Explained From Scratch | Principles of Diffusion Models) @ 4690s — So it should take the latent vector and So it should take the latent vector and
it should generate the reconstructed it 
- **diffusion-principles-vizuara** L9 (Lecture 2 - Variational Autoencoders Explained From Scratch | Principles of Diffusion Models) @ 4747s — first machine do? The first machine
actually does the reverse. It takes the actually does the reverse. It takes the actu
- **diffusion-principles-vizuara** L9 (Lecture 2 - Variational Autoencoders Explained From Scratch | Principles of Diffusion Models) @ 4813s — region which has the mu of.5 comma.5 and region which has the mu of.5 comma.5 and
the sigma of 2a 2. Right? So you need 
- **diffusion-principles-vizuara** L9 (Lecture 2 - Variational Autoencoders Explained From Scratch | Principles of Diffusion Models) @ 4861s — the GitHub repo in the description the GitHub repo in the description
section. section. section.
[snorts] [snorts]
Okay.
- **diffusion-principles-vizuara** L9 (Lecture 2 - Variational Autoencoders Explained From Scratch | Principles of Diffusion Models) @ 4916s — So this is our entire encoder decoder So this is our entire encoder decoder
architecture whatever we discussed as archit
- **diffusion-principles-vizuara** L9 (Lecture 2 - Variational Autoencoders Explained From Scratch | Principles of Diffusion Models) @ 4971s — This compares every pixel of the input
with the output. If the original pixel with the output. If the original pixel wit
- **diffusion-principles-vizuara** L9 (Lecture 2 - Variational Autoencoders Explained From Scratch | Principles of Diffusion Models) @ 5026s — zero and a standard deviation of one. To
ensure that the mean is zero, we add a ensure that the mean is zero, we add a e
- **diffusion-principles-vizuara** L9 (Lecture 2 - Variational Autoencoders Explained From Scratch | Principles of Diffusion Models) @ 5080s — because log of a small value is a big uh
number and there is a negative sign number and there is a negative sign number 
- **diffusion-principles-vizuara** L9 (Lecture 2 - Variational Autoencoders Explained From Scratch | Principles of Diffusion Models) @ 5134s — the uh description. But first I just
want to want to want to
describe everything that we have describe everything that w
- **diffusion-principles-vizuara** L9 (Lecture 2 - Variational Autoencoders Explained From Scratch | Principles of Diffusion Models) @ 5186s — for longer duration maybe we'll get an for longer duration maybe we'll get an
even better distribution which is even bet
- **diffusion-principles-vizuara** L9 (Lecture 2 - Variational Autoencoders Explained From Scratch | Principles of Diffusion Models) @ 5241s — this training proceeds and this is the this training proceeds and this is the
quality of the reconstructions because qua
- **diffusion-principles-vizuara** L9 (Lecture 2 - Variational Autoencoders Explained From Scratch | Principles of Diffusion Models) @ 5295s — latin space uh you see that the it's
it's kind of blur in some cases which it's kind of blur in some cases which it's ki
- **diffusion-principles-vizuara** L9 (Lecture 2 - Variational Autoencoders Explained From Scratch | Principles of Diffusion Models) @ 5345s — is that it it produces blurry outputs
and there is a very nice reason for it. and there is a very nice reason for it. an
- **diffusion-principles-vizuara** L9 (Lecture 2 - Variational Autoencoders Explained From Scratch | Principles of Diffusion Models) @ 5397s — applications I have seen and uh there
are encoders and distribute and and are encoders and distribute and and are encode
