---
canonical_name: Epsilon Prediction
description: Parameterise the network to predict the noise epsilon added to x_0; the
  original DDPM choice.
ontology_source: discovered
aliases: []
occurrence_count: 40
---
# Epsilon Prediction

Parameterise the network to predict the noise epsilon added to x_0; the original DDPM choice.

**40 occurrences** across courses:

- **diffusion-principles-vizuara** L7 (Lecture 4 - Diffusion Models Practical | DDPM | Principles of Diffusion Models) @ 3s — Hello everyone. Hello everyone.
In this lecture, we will continue our In this lecture, we will continue our In this lect
- **diffusion-principles-vizuara** L7 (Lecture 4 - Diffusion Models Practical | DDPM | Principles of Diffusion Models) @ 70s — We will take an example a practical
example and we will exactly see how the example and we will exactly see how the exam
- **diffusion-principles-vizuara** L7 (Lecture 4 - Diffusion Models Practical | DDPM | Principles of Diffusion Models) @ 127s — one corner of the room and then the
particles slowly diffuse and the smell particles slowly diffuse and the smell partic
- **diffusion-principles-vizuara** L7 (Lecture 4 - Diffusion Models Practical | DDPM | Principles of Diffusion Models) @ 195s — input image into noise. input image into noise.
>> [snorts] >> [snorts]
>> This is not done through a single >> This is 
- **diffusion-principles-vizuara** L7 (Lecture 4 - Diffusion Models Practical | DDPM | Principles of Diffusion Models) @ 258s — with, right? But uh when you actually
start doing the mathematics, this is not start doing the mathematics, this is not 
- **diffusion-principles-vizuara** L7 (Lecture 4 - Diffusion Models Practical | DDPM | Principles of Diffusion Models) @ 335s — execute the code and the forward and the
reverse transition process. I will reverse transition process. I will reverse t
- **diffusion-principles-vizuara** L7 (Lecture 4 - Diffusion Models Practical | DDPM | Principles of Diffusion Models) @ 411s — And uh this is something which is you
need to install the git lfs to upload need to install the git lfs to upload need t
- **diffusion-principles-vizuara** L7 (Lecture 4 - Diffusion Models Practical | DDPM | Principles of Diffusion Models) @ 493s — images as a single line as opposed to images as a single line as opposed to
converting them to a grid which is convertin
- **diffusion-principles-vizuara** L7 (Lecture 4 - Diffusion Models Practical | DDPM | Principles of Diffusion Models) @ 550s — true data distribution. We want to
predict the predict the predict the
data distribution which is P5 of X which data dis
- **diffusion-principles-vizuara** L7 (Lecture 4 - Diffusion Models Practical | DDPM | Principles of Diffusion Models) @ 628s — butterfly pictures.
And uh once you run this code And uh once you run this code And uh once you run this code
[snorts] [
- **diffusion-principles-vizuara** L7 (Lecture 4 - Diffusion Models Practical | DDPM | Principles of Diffusion Models) @ 696s — we have divided uh
we have first of all got the data. I we have first of all got the data. I we have first of all got th
- **diffusion-principles-vizuara** L7 (Lecture 4 - Diffusion Models Practical | DDPM | Principles of Diffusion Models) @ 764s — the shape comes up like this the shape comes up like this
and here we are simply and here we are simply and here we are 
- **diffusion-principles-vizuara** L7 (Lecture 4 - Diffusion Models Practical | DDPM | Principles of Diffusion Models) @ 831s — variance.
Now we had looked at this in quite some Now we had looked at this in quite some Now we had looked at this in q
- **diffusion-principles-vizuara** L7 (Lecture 4 - Diffusion Models Practical | DDPM | Principles of Diffusion Models) @ 913s — transitions. For example, x2 becomes transitions. For example, x2 becomes
alpha 2 x1 alpha 2 x1 alpha 2 x1
plus beta 2 e
- **diffusion-principles-vizuara** L7 (Lecture 4 - Diffusion Models Practical | DDPM | Principles of Diffusion Models) @ 1019s — that alpha square + beta square is equal
to 1. So p + q = 1 to 1. So p + q = 1 to 1. So p + q = 1
and which which means 
- **diffusion-principles-vizuara** L7 (Lecture 4 - Diffusion Models Practical | DDPM | Principles of Diffusion Models) @ 1093s — scheduleuler does. Okay. So uh scheduleuler does. Okay. So uh
you see here what we are doing is from you see here what w
- **diffusion-principles-vizuara** L7 (Lecture 4 - Diffusion Models Practical | DDPM | Principles of Diffusion Models) @ 1177s — mean and the variance starting from the mean and the variance starting from the
first time step to anywhere in the first
- **diffusion-principles-vizuara** L7 (Lecture 4 - Diffusion Models Practical | DDPM | Principles of Diffusion Models) @ 1243s — this noise tensor essentially means.
So imagine that you have uh this image So imagine that you have uh this image So im
- **diffusion-principles-vizuara** L7 (Lecture 4 - Diffusion Models Practical | DDPM | Principles of Diffusion Models) @ 1308s — number of time steps important? because
you need to tell the you need to tell the you need to tell the
package how many 
- **diffusion-principles-vizuara** L7 (Lecture 4 - Diffusion Models Practical | DDPM | Principles of Diffusion Models) @ 1376s — DDPM scheduleuler. You can write beta DDPM scheduleuler. You can write beta
start and beta end which means that you star
- **diffusion-principles-vizuara** L7 (Lecture 4 - Diffusion Models Practical | DDPM | Principles of Diffusion Models) @ 1426s — step. Now what do I mean by cumulative
mean? Well, cumulative means that if if mean? Well, cumulative means that if if m
- **diffusion-principles-vizuara** L7 (Lecture 4 - Diffusion Models Practical | DDPM | Principles of Diffusion Models) @ 1471s — mean changes es with time it it actually
reduces in magnitude and the cumulative reduces in magnitude and the cumulative
- **diffusion-principles-vizuara** L7 (Lecture 4 - Diffusion Models Practical | DDPM | Principles of Diffusion Models) @ 1531s — Okay. So in fact it is not by3 I think Okay. So in fact it is not by3 I think
it's just 32x 32 because for every pixel i
- **diffusion-principles-vizuara** L7 (Lecture 4 - Diffusion Models Practical | DDPM | Principles of Diffusion Models) @ 1578s — need to know how much each each pixel is
corrupted by and corrupted by and corrupted by and
that corruption level I'm id
- **diffusion-principles-vizuara** L7 (Lecture 4 - Diffusion Models Practical | DDPM | Principles of Diffusion Models) @ 1641s — uh from this time step you are uh from this time step you are
transitioning so you're predicting what transitioning so y
- **diffusion-principles-vizuara** L7 (Lecture 4 - Diffusion Models Practical | DDPM | Principles of Diffusion Models) @ 1690s — Then I I again proceed ahead and I I
look at time step equal to two. And for look at time step equal to two. And for loo
- **diffusion-principles-vizuara** L7 (Lecture 4 - Diffusion Models Practical | DDPM | Principles of Diffusion Models) @ 1741s — passing both these quantities. passing both these quantities.
So the model has the input image. It So the model has the 
- **diffusion-principles-vizuara** L7 (Lecture 4 - Diffusion Models Practical | DDPM | Principles of Diffusion Models) @ 1789s — be the best and even in most of the
modern diffusion architectures you will modern diffusion architectures you will mode
- **diffusion-principles-vizuara** L7 (Lecture 4 - Diffusion Models Practical | DDPM | Principles of Diffusion Models) @ 1842s — different output channels and the number different output channels and the number
of types in the down and the uplock. o
- **diffusion-principles-vizuara** L7 (Lecture 4 - Diffusion Models Practical | DDPM | Principles of Diffusion Models) @ 1888s — most important part of this lecture
because when we are looking at the because when we are looking at the because when w
- **diffusion-principles-vizuara** L7 (Lecture 4 - Diffusion Models Practical | DDPM | Principles of Diffusion Models) @ 1939s — steps increases and the mean actually
goes down and because the sum of the goes down and because the sum of the goes dow
- **diffusion-principles-vizuara** L7 (Lecture 4 - Diffusion Models Practical | DDPM | Principles of Diffusion Models) @ 2009s — we do uh is in in this step. This is the we do uh is in in this step. This is the
main forward diffusion process. But I 
- **diffusion-principles-vizuara** L7 (Lecture 4 - Diffusion Models Practical | DDPM | Principles of Diffusion Models) @ 2064s — process actually runs. What we say is process actually runs. What we say is
noise scheduleuler dot add noise. noise sche
- **diffusion-principles-vizuara** L7 (Lecture 4 - Diffusion Models Practical | DDPM | Principles of Diffusion Models) @ 2122s — in the next line I actually get the
model prediction. So I pass this these model prediction. So I pass this these model 
- **diffusion-principles-vizuara** L7 (Lecture 4 - Diffusion Models Practical | DDPM | Principles of Diffusion Models) @ 2186s — predict how much noise has been added to predict how much noise has been added to
that image so that I can get back to m
- **diffusion-principles-vizuara** L7 (Lecture 4 - Diffusion Models Practical | DDPM | Principles of Diffusion Models) @ 2241s — subtracting an appropriate level of
noise from that image. So it is it it noise from that image. So it is it it noise fr
- **diffusion-principles-vizuara** L7 (Lecture 4 - Diffusion Models Practical | DDPM | Principles of Diffusion Models) @ 2297s — prediction shape is like this 40x3x prediction shape is like this 40x3x
32x 32 and uh here 32x 32 and uh here 32x 32 and
- **diffusion-principles-vizuara** L7 (Lecture 4 - Diffusion Models Practical | DDPM | Principles of Diffusion Models) @ 2368s — see the plots gradually varying. The
loss decreases with time which is loss decreases with time which is loss decreases 
- **diffusion-principles-vizuara** L7 (Lecture 4 - Diffusion Models Practical | DDPM | Principles of Diffusion Models) @ 2418s — have a negative value and you go to the have a negative value and you go to the
previous sample. Then then you again pre
- **diffusion-principles-vizuara** L7 (Lecture 4 - Diffusion Models Practical | DDPM | Principles of Diffusion Models) @ 2462s — slightly overwhelmed you, don't worry.
You can focus on this practical side of You can focus on this practical side of Y
