---
course_slug: diffusion-principles-vizuara
idx: 3
title: 'Lecture 8 - Diffusion Models: A Physical Intuition (SDE Framework) | Principles
  of Diffusion Models'
video_url: https://www.youtube.com/watch?v=57EFSTxL_5o
duration_sec: null
chunks:
- idx: 0
  start_sec: 5.51
  end_sec: 69.19
  text: 'Hello everyone and welcome to the next Hello everyone and welcome to the
    next

    lecture of the course principles of lecture of the course principles of lecture
    of the course principles of

    diffusion models. diffusion models. diffusion models.

    In this lecture I have adopted a In this lecture I have adopted a In this lecture
    I have adopted a

    different style of teaching different style of teaching different style of teaching

    just because the content is so just because the content is so just because the
    content is so

    interesting interesting interesting

    and there is a lot of connection with and there is a lot of connection with and
    there is a lot of connection with

    physics. physics. physics.

    So I''m going to show you or explain the So I''m going to show you or explain
    the So I''m going to show you or explain the

    concepts to you via the means of slides. concepts to you via the means of slides.
    concepts to you via the means of slides.

    So what are we going to learn today So what are we going to learn today So what
    are we going to learn today

    in the principles of diffusion models in the principles of diffusion models in
    the principles of diffusion models

    series? We have so far covered variation series? We have so far covered variation
    series? We have so far covered variation

    autoenccoders then DDPMS autoenccoders then DDPMS autoenccoders then DDPMS

    denoising diffusion probabilistic denoising diffusion probabilistic denoising
    diffusion probabilistic

    models. Then we have covered the energy models. Then we have covered the energy
    models. Then we have covered the energy

    based approach which includes score based approach which includes score based
    approach which includes score

    function and noise condition score function and noise condition score function
    and noise condition score

    network. Today we are going to look at a network. Today we are going to look at
    a network. Today we are going to look at a

    framework which unifies everything framework which unifies everything framework
    which unifies everything

    together. together. together.

    If you are watching this lecture for the If you are watching this lecture for
    the If you are watching this lecture for the

    first time in the series, you have not first time in the series, you have not
    first time in the series, you have not

    looked at other lectures. This is'
  concept_slugs:
  - langevin-dynamics
  - probability-flow-ode
  - sde-formulation
- idx: 1
  start_sec: 69.19
  end_sec: 126.069
  text: 'looked at other lectures. This is looked at other lectures. This is

    supposed to be a standalone lecture to supposed to be a standalone lecture to
    supposed to be a standalone lecture to

    help you get into the diffusion concept help you get into the diffusion concept
    help you get into the diffusion concept

    which is at the heart of so many things which is at the heart of so many things
    which is at the heart of so many things

    at the moment. There are LLMs being made at the moment. There are LLMs being made
    at the moment. There are LLMs being made

    in a diffusive manner as opposed to auto in a diffusive manner as opposed to auto
    in a diffusive manner as opposed to auto

    reggressive manner. In robotics, reggressive manner. In robotics, reggressive
    manner. In robotics,

    diffusion models are used in audio diffusion models are used in audio diffusion
    models are used in audio

    models. The applications are enormous. models. The applications are enormous.
    models. The applications are enormous.

    Today we are going to look at a Today we are going to look at a Today we are going
    to look at a

    framework which unifies the framework which unifies the framework which unifies
    the

    two approaches. One is the DDPM approach two approaches. One is the DDPM approach
    two approaches. One is the DDPM approach

    and second is the score-based approach. and second is the score-based approach.
    and second is the score-based approach.

    And interestingly, this unification And interestingly, this unification And interestingly,
    this unification

    happened later after both these previous happened later after both these previous
    happened later after both these previous

    papers came out. papers came out. papers came out.

    And when you view everything from this And when you view everything from this
    And when you view everything from this

    lens, it makes a lot of sense. lens, it makes a lot of sense. lens, it makes a
    lot of sense.

    And it turns out that both DDPM and And it turns out that both DDPM and And it
    turns out that both DDPM and

    score-based approach are special cases score-based approach are special cases
    score-based approach are special cases

    of this overall unified approach that we of this overall unified approach that
    we of this overall unified approach that we

    are going to discuss today.'
  concept_slugs:
  - langevin-dynamics
  - probability-flow-ode
  - sde-formulation
- idx: 2
  start_sec: 126.069
  end_sec: 193.519
  text: 'are going to discuss today. are going to discuss today.

    The good thing is that this unified The good thing is that this unified The good
    thing is that this unified

    approach has a lot of connection with approach has a lot of connection with approach
    has a lot of connection with

    physics. So there are there is going to physics. So there are there is going to
    physics. So there are there is going to

    be a lot of physical intuition that we be a lot of physical intuition that we
    be a lot of physical intuition that we

    will build in the process. Okay. So firstly by diffusion we Okay. So firstly by
    diffusion we

    understand that something is spreading understand that something is spreading
    understand that something is spreading

    in space right as you can see in these in space right as you can see in these
    in space right as you can see in these

    images there is there is something there images there is there is something there
    images there is there is something there

    is a spread of material in space. Now in today''s lecture we are going to Now
    in today''s lecture we are going to

    understand how this concept of diffusion understand how this concept of diffusion
    understand how this concept of diffusion

    can be connected can be connected can be connected

    to probabilistic models and essentially to probabilistic models and essentially
    to probabilistic models and essentially

    what is the problem that we are even what is the problem that we are even what
    is the problem that we are even

    trying to solve trying to solve trying to solve

    and how is it that physics is helping AI and how is it that physics is helping
    AI and how is it that physics is helping AI

    what is the connection between both of what is the connection between both of
    what is the connection between both of

    these fields these fields these fields

    if you have a background in physics or if you have a background in physics or
    if you have a background in physics or

    mechanics particles fluid meanan mechanics particles fluid meanan mechanics particles
    fluid meanan

    mechanics you''ll find this lecture very mechanics you''ll find this lecture very
    mechanics you''ll find this lecture very

    interesting. Okay. So what do we know about'
  concept_slugs:
  - langevin-dynamics
  - probability-flow-ode
  - sde-formulation
- idx: 3
  start_sec: 193.519
  end_sec: 274.07
  text: 'Okay. So what do we know about

    diffusion? In this image diffusion? In this image diffusion? In this image

    I have shown a dye diffusing or I have shown a dye diffusing or I have shown a
    dye diffusing or

    spreading in a glass of water. spreading in a glass of water. spreading in a glass
    of water.

    I will use the word spreading when I I will use the word spreading when I I will
    use the word spreading when I

    intend to say diffusion because to intend to say diffusion because to intend to
    say diffusion because to

    explain diffusion I cannot use the same explain diffusion I cannot use the same
    explain diffusion I cannot use the same

    word diffusion. word diffusion. word diffusion.

    So initially the shape of the dye was So initially the shape of the dye was So
    initially the shape of the dye was

    maybe spherical. maybe spherical. maybe spherical.

    When you put it on the surface of the When you put it on the surface of the When
    you put it on the surface of the

    liquid liquid liquid

    then the drop slowly goes down and you then the drop slowly goes down and you
    then the drop slowly goes down and you

    can see the liquid gets filled. can see the liquid gets filled. can see the liquid
    gets filled.

    Initially the liquid is white in color Initially the liquid is white in color
    Initially the liquid is white in color

    and slowly the color changes to red. So the structure of the dye which was So
    the structure of the dye which was

    spherical to begin with is completely spherical to begin with is completely spherical
    to begin with is completely

    destroyed in the process. destroyed in the process. destroyed in the process.

    It becomes uniform. It becomes uniform. It becomes uniform.

    Now this is the first property of Now this is the first property of Now this is
    the first property of

    diffusion that we understand. The question that we are trying to ask The question
    that we are trying to ask

    in this entire lecture, you will see in this entire lecture, you will see in this
    entire lecture, you will see

    this is a common thread throughout this is a common thread throughout this is
    a common thread throughout

    is that can we reverse this process?'
  concept_slugs:
  - langevin-dynamics
  - probability-flow-ode
  - sde-formulation
- idx: 4
  start_sec: 277.67
  end_sec: 329.199
  text: 'Can we or in other words can we recover Can we or in other words can we recover

    the original structure? the original structure? the original structure?

    So imagine you''re sitting and you see So imagine you''re sitting and you see
    So imagine you''re sitting and you see

    this glass filled with this red liquid this glass filled with this red liquid
    this glass filled with this red liquid

    and someone tells you what was the and someone tells you what was the and someone
    tells you what was the

    original structure of this dye when it original structure of this dye when it
    original structure of this dye when it

    was poured in the liquid. was poured in the liquid. was poured in the liquid.

    You are thinking like okay this is very You are thinking like okay this is very
    You are thinking like okay this is very

    difficult for me because difficult for me because difficult for me because

    I cannot reverse time. You can see in I cannot reverse time. You can see in I
    cannot reverse time. You can see in

    this figure that if I was able to this figure that if I was able to this figure
    that if I was able to

    reverse time, I could exactly predict reverse time, I could exactly predict reverse
    time, I could exactly predict

    the initial shape of the D when it made the initial shape of the D when it made
    the initial shape of the D when it made

    the contact with water. the contact with water. the contact with water.

    But the problem is that we live in a But the problem is that we live in a But
    the problem is that we live in a

    world where we cannot reverse time. world where we cannot reverse time. world
    where we cannot reverse time.

    If I had a time machine, I could use the If I had a time machine, I could use
    the If I had a time machine, I could use the

    time machine. I can go back in time time machine. I can go back in time time machine.
    I can go back in time

    and I can easily look at the original and I can easily look at the original and
    I can easily look at the original

    shape of the die. shape of the die.'
  concept_slugs:
  - langevin-dynamics
  - probability-flow-ode
  - sde-formulation
- idx: 5
  start_sec: 329.199
  end_sec: 383.759
  text: 'shape of the die.

    But that is not the case. [snorts] But that is not the case. [snorts] But that
    is not the case. [snorts]

    So reversing time is something which is So reversing time is something which is
    So reversing time is something which is

    even out of the question. So how do you even out of the question. So how do you
    even out of the question. So how do you

    recover the structure of the die? This is where it gets more interesting. This
    is where it gets more interesting.

    We cannot just reverse time and all of We cannot just reverse time and all of
    We cannot just reverse time and all of

    us are aware about it. us are aware about it. us are aware about it.

    But let us take a lens and zoom in on But let us take a lens and zoom in on But
    let us take a lens and zoom in on

    the die and see exactly what we see. So the die and see exactly what we see. So
    the die and see exactly what we see. So

    I''m going to take a lens a microscope I''m going to take a lens a microscope
    I''m going to take a lens a microscope

    and I''m going to zoom in on the red dye. and I''m going to zoom in on the red
    dye. and I''m going to zoom in on the red dye.

    I''m going to zoom in even more till I go I''m going to zoom in even more till
    I go I''m going to zoom in even more till I go

    to the particle or the atomic level. to the particle or the atomic level. to the
    particle or the atomic level.

    When I zoom in on the die, I see When I zoom in on the die, I see When I zoom
    in on the die, I see

    something like this. something like this. something like this.

    I see tiny particles moving around and I see tiny particles moving around and
    I see tiny particles moving around and

    wobbling around here and there. wobbling around here and there. wobbling around
    here and there.

    It''s almost like the motion is It''s almost like the motion is It''s almost like
    the motion is

    unpredictable. It''s it''s very random. unpredictable. It''s it''s very random.'
  concept_slugs:
  - langevin-dynamics
  - probability-flow-ode
  - sde-formulation
- idx: 6
  start_sec: 383.759
  end_sec: 448.07
  text: 'unpredictable. It''s it''s very random.

    It''s not moving in a specific direction, It''s not moving in a specific direction,
    It''s not moving in a specific direction,

    but but but

    they''re moving up and down. It''s like a they''re moving up and down. It''s like
    a they''re moving up and down. It''s like a

    zigzag motion. zigzag motion. zigzag motion.

    All of us have have seen how the price All of us have have seen how the price
    All of us have have seen how the price

    of a stock varies. It''s it''s up and of a stock varies. It''s it''s up and of
    a stock varies. It''s it''s up and

    down. It''s very zigzag, right? This this down. It''s very zigzag, right? This
    this down. It''s very zigzag, right? This this

    is almost very similar to that. A more technical word for this motion is A more
    technical word for this motion is

    also called as Brownian motion. So also called as Brownian motion. So also called
    as Brownian motion. So

    particles are exhibiting brownian motion particles are exhibiting brownian motion
    particles are exhibiting brownian motion

    and uh this dye is made up of a lot of and uh this dye is made up of a lot of
    and uh this dye is made up of a lot of

    particles like this which are moving in particles like this which are moving in
    particles like this which are moving in

    a fashion like this. a fashion like this. a fashion like this.

    It''s it''s a very peculiar movement. They It''s it''s a very peculiar movement.
    They It''s it''s a very peculiar movement. They

    are not flowing in a specific direction. are not flowing in a specific direction.
    are not flowing in a specific direction.

    They are just moving around here and They are just moving around here and They
    are just moving around here and

    there. Now the question that Now the question that

    I want to ask all of you is that just by I want to ask all of you is that just
    by I want to ask all of you is that just by

    looking at this motion looking at this motion looking at this motion

    can you tell whether it''s the forward can you tell whether it''s the forward
    can you tell whether it''s the forward

    motion or the backward motion?'
  concept_slugs:
  - langevin-dynamics
  - probability-flow-ode
  - sde-formulation
- idx: 7
  start_sec: 450.23
  end_sec: 509.83
  text: 'So when the dye was diffusing and when So when the dye was diffusing and
    when

    we reversed the whole process, we reversed the whole process, we reversed the
    whole process,

    can you tell this movement of particles? can you tell this movement of particles?
    can you tell this movement of particles?

    Does it correspond to the forward motion Does it correspond to the forward motion
    Does it correspond to the forward motion

    or the reverse motion? That is difficult to predict. In fact, That is difficult
    to predict. In fact,

    just by looking at this picture, I have just by looking at this picture, I have
    just by looking at this picture, I have

    absolutely no idea whether this absolutely no idea whether this absolutely no
    idea whether this

    corresponds to the forward motion or the corresponds to the forward motion or
    the corresponds to the forward motion or the

    reverse motion. reverse motion. reverse motion.

    And this is where we come to a very And this is where we come to a very And this
    is where we come to a very

    interesting property. It it turns out interesting property. It it turns out interesting
    property. It it turns out

    that even though macroscopic that even though macroscopic that even though macroscopic

    motions are not time reversible like we motions are not time reversible like we
    motions are not time reversible like we

    just saw with the spread of the die, we just saw with the spread of the die, we
    just saw with the spread of the die, we

    cannot simply reverse time. But at the cannot simply reverse time. But at the
    cannot simply reverse time. But at the

    microscopic level, if you look at these microscopic level, if you look at these
    microscopic level, if you look at these

    individual tiny particles, individual tiny particles, individual tiny particles,

    if you look at the way they are moving, if you look at the way they are moving,
    if you look at the way they are moving,

    it turns out that these motions are it turns out that these motions are it turns
    out that these motions are

    exactly reversible. exactly reversible. exactly reversible.

    Which means that if someone if 10 Which means that if someone if 10 Which means
    that if someone if 10

    seconds have passed and someone tells me'
  concept_slugs:
  - langevin-dynamics
  - probability-flow-ode
  - sde-formulation
- idx: 8
  start_sec: 509.83
  end_sec: 569.68
  text: 'seconds have passed and someone tells me seconds have passed and someone
    tells me

    that Rajett this is the particle which that Rajett this is the particle which
    that Rajett this is the particle which

    is located here right now show me where is located here right now show me where
    is located here right now show me where

    it was located 10 seconds back. I can it was located 10 seconds back. I can it
    was located 10 seconds back. I can

    exactly map the reverse trajectory of exactly map the reverse trajectory of exactly
    map the reverse trajectory of

    that particle and I can pinpoint the that particle and I can pinpoint the that
    particle and I can pinpoint the

    original location and this is because of the property that and this is because
    of the property that

    microscopic motions are time reversible microscopic motions are time reversible
    microscopic motions are time reversible

    and this is the only theme which is used and this is the only theme which is used
    and this is the only theme which is used

    in the entire diffusion literature in in the entire diffusion literature in in
    the entire diffusion literature in

    all the different approaches. This is all the different approaches. This is all
    the different approaches. This is

    the common arc which you will find in the common arc which you will find in the
    common arc which you will find in

    many of these papers. many of these papers. many of these papers.

    something will be reversed in the paper something will be reversed in the paper
    something will be reversed in the paper

    and you''ll be wondering how how did this and you''ll be wondering how how did
    this and you''ll be wondering how how did this

    magically work magically work magically work

    and at the heart of it it turns out that and at the heart of it it turns out that
    and at the heart of it it turns out that

    it is because of this property of it is because of this property of it is because
    of this property of

    microscopic motions being time microscopic motions being time microscopic motions
    being time

    reversible. Now this is where the connection between Now this is where the connection
    between

    physics and AI comes into the picture. physics and AI comes into the picture.'
  concept_slugs:
  - langevin-dynamics
  - probability-flow-ode
  - sde-formulation
- idx: 9
  start_sec: 569.68
  end_sec: 629.35
  text: 'physics and AI comes into the picture.

    This is a well-known physical property This is a well-known physical property
    This is a well-known physical property

    and it makes sense in when you when we and it makes sense in when you when we
    and it makes sense in when you when we

    look at diffusion of liquids and we look look at diffusion of liquids and we look
    look at diffusion of liquids and we look

    at the microscopic and microscopic lens. at the microscopic and microscopic lens.
    at the microscopic and microscopic lens.

    But remember here we are dealing with But remember here we are dealing with But
    remember here we are dealing with

    data. We do not have liquids which we data. We do not have liquids which we data.
    We do not have liquids which we

    can so readily imagine the movement of can so readily imagine the movement of
    can so readily imagine the movement of

    these liquids. these liquids. these liquids.

    We have data, we have pixels, we have We have data, we have pixels, we have We
    have data, we have pixels, we have

    numbers. So how do we even connect it to numbers. So how do we even connect it
    to numbers. So how do we even connect it to

    the process of diffusion? All of it the process of diffusion? All of it the process
    of diffusion? All of it

    looks very looks very looks very

    random and vague. random and vague. random and vague.

    We are going to form this connection in We are going to form this connection in
    We are going to form this connection in

    in in this lecture and u these in in this lecture and u these in in this lecture
    and u these

    individual particles right which you see individual particles right which you
    see individual particles right which you see

    as we move proceed in the lecture you as we move proceed in the lecture you as
    we move proceed in the lecture you

    will see that we will view our data as will see that we will view our data as
    will see that we will view our data as

    one of these particles. So that is the broader arc which we are So that is the
    broader arc which we are

    going to take in today''s lecture.'
  concept_slugs:
  - langevin-dynamics
  - probability-flow-ode
  - sde-formulation
- idx: 10
  start_sec: 633.99
  end_sec: 690.959
  text: 'Okay. Now let us apply this concept Okay. Now let us apply this concept

    to data. to data. to data.

    Why are we applying this concept to Why are we applying this concept to Why are
    we applying this concept to

    data? The diffusion models were first data? The diffusion models were first data?
    The diffusion models were first

    proven to be incredibly successful at proven to be incredibly successful at proven
    to be incredibly successful at

    generating data. generating data. generating data.

    Applications like stable diffusion, Applications like stable diffusion, Applications
    like stable diffusion,

    midjourney, midjourney, midjourney,

    all of them relied on the process of all of them relied on the process of all
    of them relied on the process of

    diffusion to generate data. diffusion to generate data. diffusion to generate
    data.

    Okay. So now what is the problem that we Okay. So now what is the problem that
    we Okay. So now what is the problem that we

    are dealing with? Someone comes up to us are dealing with? Someone comes up to
    us are dealing with? Someone comes up to us

    and shows us a bunch of cat images. Here and shows us a bunch of cat images. Here
    and shows us a bunch of cat images. Here

    I have shown eight images for reference I have shown eight images for reference
    I have shown eight images for reference

    but it can be even 80 or 100 images. but it can be even 80 or 100 images. but
    it can be even 80 or 100 images.

    Someone shows us all of these images of Someone shows us all of these images of
    Someone shows us all of these images of

    cats which are very diverse. You can see cats which are very diverse. You can
    see cats which are very diverse. You can see

    that some of them are whitish, some of that some of them are whitish, some of
    that some of them are whitish, some of

    them have a darker color. them have a darker color. them have a darker color.

    And the eyes are pretty different, some And the eyes are pretty different, some
    And the eyes are pretty different, some

    of them have pretty smaller eyes, some of them have pretty smaller eyes, some
    of them have pretty smaller eyes, some

    of them have wide eyes. of them have wide eyes.'
  concept_slugs:
  - langevin-dynamics
  - probability-flow-ode
  - sde-formulation
- idx: 11
  start_sec: 690.959
  end_sec: 755.35
  text: 'of them have wide eyes.

    And the question they ask us is, And the question they ask us is, And the question
    they ask us is,

    can you find a distribution can you find a distribution can you find a distribution

    using which we can sample images which using which we can sample images which
    using which we can sample images which

    look like cats? look like cats? look like cats?

    [snorts] Now, what is this concept of [snorts] Now, what is this concept of [snorts]
    Now, what is this concept of

    distribution? All of a sudden distribution? All of a sudden distribution? All
    of a sudden

    distribution simply means that we want distribution simply means that we want
    distribution simply means that we want

    to find a common something common between all of common something common between
    all of

    these cats and it should be so these cats and it should be so these cats and it
    should be so

    deeprooted that deeprooted that deeprooted that

    once we find those common factors it once we find those common factors it once
    we find those common factors it

    should allow us to create images which should allow us to create images which
    should allow us to create images which

    look like cats. look like cats. look like cats.

    Let''s take an example of a dice being Let''s take an example of a dice being
    Let''s take an example of a dice being

    rolled. A dice has six faces 1 2 3 4 5 rolled. A dice has six faces 1 2 3 4 5
    rolled. A dice has six faces 1 2 3 4 5

    6. And what will the distribution say? 6. And what will the distribution say?
    6. And what will the distribution say?

    Whenever I sample from this Whenever I sample from this Whenever I sample from
    this

    distribution, I will either get 1 2 3 4 distribution, I will either get 1 2 3
    4 distribution, I will either get 1 2 3 4

    5 or six. I will never get seven or 5 or six. I will never get seven or 5 or six.
    I will never get seven or

    eight. eight. eight.

    So the meaning of distribution is that So the meaning of distribution is that
    So the meaning of distribution is that

    when you sample from it, you should get'
  concept_slugs:
  - langevin-dynamics
  - probability-flow-ode
  - sde-formulation
- idx: 12
  start_sec: 755.35
  end_sec: 808.16
  text: 'when you sample from it, you should get when you sample from it, you should
    get

    something which lies within that something which lies within that something which
    lies within that

    distribution. distribution. distribution.

    For example, if you have a normal For example, if you have a normal For example,
    if you have a normal

    distribution which is centered around distribution which is centered around distribution
    which is centered around

    some value and it tapers off on left and some value and it tapers off on left
    and some value and it tapers off on left and

    right, it means that the probability of right, it means that the probability of
    right, it means that the probability of

    the mean is the maximum and it dies down the mean is the maximum and it dies down
    the mean is the maximum and it dies down

    as you go away from the mean. as you go away from the mean. as you go away from
    the mean.

    So So So

    our whole objective is always to find a our whole objective is always to find
    a our whole objective is always to find a

    distribution using which we can sample distribution using which we can sample
    distribution using which we can sample

    more images. more images. more images.

    If we don''t have a distribution then we If we don''t have a distribution then
    we If we don''t have a distribution then we

    cannot sample variety. We can simply cannot sample variety. We can simply cannot
    sample variety. We can simply

    learn based on these cats. We can learn based on these cats. We can learn based
    on these cats. We can

    understand there are eight cats in the understand there are eight cats in the
    understand there are eight cats in the

    figure and I learn about eight cats. But figure and I learn about eight cats.
    But figure and I learn about eight cats. But

    if we have a distribution, it suddenly if we have a distribution, it suddenly
    if we have a distribution, it suddenly

    gives us the power to sample more images gives us the power to sample more images
    gives us the power to sample more images

    which look like cats. which look like cats. which look like cats.

    And to find such distribution we need an And to find such distribution we need
    an'
  concept_slugs:
  - langevin-dynamics
  - probability-flow-ode
  - sde-formulation
- idx: 13
  start_sec: 808.16
  end_sec: 864.399
  text: 'And to find such distribution we need an

    algorithm which is clever enough which algorithm which is clever enough which
    algorithm which is clever enough which

    can understand that okay uh cats have a can understand that okay uh cats have
    a can understand that okay uh cats have a

    specific shape they have a specific set specific shape they have a specific set
    specific shape they have a specific set

    of features of features of features

    uh they have a specific way that they uh they have a specific way that they uh
    they have a specific way that they

    look and you can see right now the way look and you can see right now the way
    look and you can see right now the way

    I''m talking about these features is very I''m talking about these features is
    very I''m talking about these features is very

    vague because it is very difficult for vague because it is very difficult for
    vague because it is very difficult for

    humans to provide a summary of all of humans to provide a summary of all of humans
    to provide a summary of all of

    these features or exactly pinpoint point these features or exactly pinpoint point
    these features or exactly pinpoint point

    the causes of variation in between the the causes of variation in between the
    the causes of variation in between the

    cats and that is exactly why we are cats and that is exactly why we are cats and
    that is exactly why we are

    learning this process [snorts] which can learning this process [snorts] which
    can learning this process [snorts] which can

    help us to predict this probability help us to predict this probability help us
    to predict this probability

    distribution. Okay. Uh I hope that was clear why we Okay. Uh I hope that was clear
    why we

    are trying to find a distribution which are trying to find a distribution which
    are trying to find a distribution which

    can sample images which look like cats can sample images which look like cats
    can sample images which look like cats

    and we will now take inspiration from and we will now take inspiration from and
    we will now take inspiration from

    the diffusion process. Now this is where the diffusion process. Now this is where'
  concept_slugs:
  - langevin-dynamics
  - probability-flow-ode
  - sde-formulation
- idx: 14
  start_sec: 864.399
  end_sec: 937.44
  text: 'the diffusion process. Now this is where

    it gets very interesting. In the next it gets very interesting. In the next it
    gets very interesting. In the next

    set of slides I''m going to replace the set of slides I''m going to replace the
    set of slides I''m going to replace the

    die with data. Okay. So we want to go from images to Okay. So we want to go from
    images to

    distribution which looks like in in in distribution which looks like in in in
    distribution which looks like in in in

    the figure I have shown a contour which the figure I have shown a contour which
    the figure I have shown a contour which

    is a just a schematic distribution which is a just a schematic distribution which
    is a just a schematic distribution which

    can be used to sample the images of can be used to sample the images of can be
    used to sample the images of

    cats. cats. cats.

    Now we don''t have access to it. We only Now we don''t have access to it. We only
    Now we don''t have access to it. We only

    have images to images of the cats and have images to images of the cats and have
    images to images of the cats and

    based on these images we are expected to based on these images we are expected
    to based on these images we are expected to

    find this unknown magical distribution. find this unknown magical distribution.
    find this unknown magical distribution.

    [snorts] Okay. Now the question is Okay. Now the question is

    what if [snorts] we diffuse data instead what if [snorts] we diffuse data instead
    what if [snorts] we diffuse data instead

    of diffusing the die? of diffusing the die? of diffusing the die?

    What if we modify or transform the data such that modify or transform the data
    such that

    the structure of the data completely the structure of the data completely the
    structure of the data completely

    disappears which is the first disappears which is the first disappears which is
    the first

    observation that we looked at in the observation that we looked at in the observation
    that we looked at in the

    diffusion process [snorts] diffusion process [snorts] diffusion process [snorts]

    and then later we recover it. and then later we recover it.'
  concept_slugs:
  - langevin-dynamics
  - probability-flow-ode
  - sde-formulation
- idx: 15
  start_sec: 937.44
  end_sec: 996.949
  text: 'and then later we recover it.

    So we destroy something only to recover So we destroy something only to recover
    So we destroy something only to recover

    it after some point. it after some point. it after some point.

    Now if if someone would have come up Now if if someone would have come up Now
    if if someone would have come up

    with this idea maybe with this idea maybe with this idea maybe

    10 years back 10 years back 10 years back

    it it sounds very cool because whenever it it sounds very cool because whenever
    it it sounds very cool because whenever

    there is a reversal of time involved there is a reversal of time involved there
    is a reversal of time involved

    there is a natural fascination towards there is a natural fascination towards
    there is a natural fascination towards

    it. it. it.

    I don''t know maybe that''s why people I don''t know maybe that''s why people
    I don''t know maybe that''s why people

    love to see movies with time machines in love to see movies with time machines
    in love to see movies with time machines in

    it and that was a part of the reason of it and that was a part of the reason of
    it and that was a part of the reason of

    my fascination towards this field as my fascination towards this field as my fascination
    towards this field as

    well. this this whole idea of diffusing well. this this whole idea of diffusing
    well. this this whole idea of diffusing

    data and later recovering it it sounds data and later recovering it it sounds
    data and later recovering it it sounds

    almost like uh almost like uh almost like uh

    too good to be true and and impossible too good to be true and and impossible
    too good to be true and and impossible

    right and how how will this even work right and how how will this even work right
    and how how will this even work

    [snorts] [snorts] [snorts]

    so we''ll we''ll do something like this uh so we''ll we''ll do something like
    this uh so we''ll we''ll do something like this uh

    when we are diffusing the dye we can when we are diffusing the dye we can when
    we are diffusing the dye we can

    visualize the dye being slowly filling'
  concept_slugs:
  - langevin-dynamics
  - probability-flow-ode
  - sde-formulation
- idx: 16
  start_sec: 996.949
  end_sec: 1053.039
  text: 'visualize the dye being slowly filling visualize the dye being slowly filling

    the liquid and the structure the liquid and the structure the liquid and the structure

    disappearing disappearing disappearing

    When we are diffusing data, this is what When we are diffusing data, this is what
    When we are diffusing data, this is what

    we mean. We get to a point where it we mean. We get to a point where it we mean.
    We get to a point where it

    almost becomes pure noise. You might almost becomes pure noise. You might almost
    becomes pure noise. You might

    have seen this these displays on our TVs have seen this these displays on our
    TVs have seen this these displays on our TVs

    when we are not getting any signal. when we are not getting any signal. when we
    are not getting any signal.

    Right? There is a very uh Right? There is a very uh Right? There is a very uh

    harsh sound which comes on the screen harsh sound which comes on the screen harsh
    sound which comes on the screen

    and the picture looks like this. It''s and the picture looks like this. It''s
    and the picture looks like this. It''s

    it''s filled with these multicolored it''s filled with these multicolored it''s
    filled with these multicolored

    dots. dots. dots.

    And what you''re seeing on the screen And what you''re seeing on the screen And
    what you''re seeing on the screen

    before you have no idea it has before you have no idea it has before you have
    no idea it has

    completely disappeared. completely disappeared. completely disappeared.

    This is exactly what we want to do in This is exactly what we want to do in This
    is exactly what we want to do in

    the forward process where we want to the forward process where we want to the
    forward process where we want to

    diffuse our data so that it becomes pure diffuse our data so that it becomes pure
    diffuse our data so that it becomes pure

    noise. The the the structure disappears. noise. The the the structure disappears.
    noise. The the the structure disappears.

    And then in the reverse process we will And then in the reverse process we will
    And then in the reverse process we will

    do the opposite. In the reverse process, do the opposite. In the reverse process,'
  concept_slugs:
  - langevin-dynamics
  - probability-flow-ode
  - sde-formulation
- idx: 17
  start_sec: 1053.039
  end_sec: 1113.59
  text: 'do the opposite. In the reverse process,

    we will start with noise and then slowly we will start with noise and then slowly
    we will start with noise and then slowly

    we will move backwards and we will we will move backwards and we will we will
    move backwards and we will

    recover the original image. recover the original image. recover the original image.

    [snorts] And the first question that pops in the And the first question that pops
    in the

    mind is mind is mind is

    how do we even begin with this recovery how do we even begin with this recovery
    how do we even begin with this recovery

    process and where is the learning process and where is the learning process and
    where is the learning

    actually happening? actually happening? actually happening?

    Where am I learning the variations in Where am I learning the variations in Where
    am I learning the variations in

    the different features of the cats? the different features of the cats? the different
    features of the cats?

    Where am I learning that okay some cats Where am I learning that okay some cats
    Where am I learning that okay some cats

    have bigger eyes, some have smaller have bigger eyes, some have smaller have bigger
    eyes, some have smaller

    eyes, some have long whiskers, short eyes, some have long whiskers, short eyes,
    some have long whiskers, short

    whiskers, etc. whiskers, etc. whiskers, etc.

    So out of all of this, what is something So out of all of this, what is something
    So out of all of this, what is something

    that is in our control and what is that is in our control and what is that is
    in our control and what is

    something that we are planning to learn? something that we are planning to learn?
    something that we are planning to learn?

    At least that was the first question At least that was the first question At least
    that was the first question

    which came to my mind when I was looking which came to my mind when I was looking
    which came to my mind when I was looking

    at this process. at this process. at this process.

    [snorts] Okay, now comes the interesting part of Okay, now comes the interesting
    part of

    the lecture. the lecture. the lecture.

    We have already said that we are going'
  concept_slugs:
  - langevin-dynamics
  - probability-flow-ode
  - sde-formulation
- idx: 18
  start_sec: 1113.59
  end_sec: 1181.28
  text: 'We have already said that we are going We have already said that we are going

    to apply the diffusion process to data. to apply the diffusion process to data.
    to apply the diffusion process to data.

    But to apply the diffusion, we need to But to apply the diffusion, we need to
    But to apply the diffusion, we need to

    first figure out how will I transform first figure out how will I transform first
    figure out how will I transform

    the data to noise. Visually, this looks the data to noise. Visually, this looks
    the data to noise. Visually, this looks

    very clear. But what is the mathematical very clear. But what is the mathematical
    very clear. But what is the mathematical

    process of doing that? process of doing that? process of doing that?

    And we are going to look at it from a And we are going to look at it from a And
    we are going to look at it from a

    microscopic lens because we have already microscopic lens because we have already
    microscopic lens because we have already

    built our intuition that microscopic built our intuition that microscopic built
    our intuition that microscopic

    processes are time reversible. So we are processes are time reversible. So we
    are processes are time reversible. So we are

    going to look at this forward diffusion going to look at this forward diffusion
    going to look at this forward diffusion

    process from a microscopic lens. Okay. So Okay. So

    we briefly looked at these motion of we briefly looked at these motion of we briefly
    looked at these motion of

    particles, right? particles, right? particles, right?

    >> [snorts] >> [snorts] >> [snorts]

    >> which are swiggling around >> which are swiggling around >> which are swiggling
    around

    uh and and they are moving in a very uh and and they are moving in a very uh and
    and they are moving in a very

    random fashion [snorts] random fashion [snorts] random fashion [snorts]

    and because I''m using the word random and because I''m using the word random
    and because I''m using the word random

    this is also called as a brownian motion this is also called as a brownian motion
    this is also called as a brownian motion

    and you see this motion in a lot of and you see this motion in a lot of'
  concept_slugs:
  - langevin-dynamics
  - probability-flow-ode
  - sde-formulation
- idx: 19
  start_sec: 1181.28
  end_sec: 1236.72
  text: 'and you see this motion in a lot of

    physical processes you see these motions physical processes you see these motions
    physical processes you see these motions

    in polymers you see this even in the in polymers you see this even in the in polymers
    you see this even in the

    movement of stock prices [snorts] movement of stock prices [snorts] movement of
    stock prices [snorts]

    and here if you and here if you and here if you

    The particles are only moving around The particles are only moving around The
    particles are only moving around

    their center. They are not really their center. They are not really their center.
    They are not really

    drifting. drifting. drifting.

    So typically Brownian motion has two So typically Brownian motion has two So typically
    Brownian motion has two

    terms. The first term is the drift term terms. The first term is the drift term
    terms. The first term is the drift term

    and the second term is the noise term or and the second term is the noise term
    or and the second term is the noise term or

    the diffusion term. the diffusion term. the diffusion term.

    The drift term is what carries you with The drift term is what carries you with
    The drift term is what carries you with

    the liquid and the noise term is what the liquid and the noise term is what the
    liquid and the noise term is what

    causes these random perturbations. causes these random perturbations. causes these
    random perturbations.

    Now in this image which I have taken it Now in this image which I have taken it
    Now in this image which I have taken it

    almost looks like the fluid is static almost looks like the fluid is static almost
    looks like the fluid is static

    otherwise these particles will be otherwise these particles will be otherwise
    these particles will be

    flowing right. So there is only the flowing right. So there is only the flowing
    right. So there is only the

    noise term or the diffusion term which noise term or the diffusion term which
    noise term or the diffusion term which

    is being shown in this image. is being shown in this image. is being shown in
    this image.

    On the right hand side we are zooming in On the right hand side we are zooming
    in'
  concept_slugs:
  - langevin-dynamics
  - probability-flow-ode
  - sde-formulation
- idx: 20
  start_sec: 1236.72
  end_sec: 1295.679
  text: 'On the right hand side we are zooming in

    on specific particles. So here I have on specific particles. So here I have on
    specific particles. So here I have

    taken taken taken

    seven particles as reference and I''m seven particles as reference and I''m seven
    particles as reference and I''m

    plotting their trajectory. plotting their trajectory. plotting their trajectory.

    Now here I have assumed there is some Now here I have assumed there is some Now
    here I have assumed there is some

    drift when plotting these trajectories drift when plotting these trajectories
    drift when plotting these trajectories

    but you can see these motions of these but you can see these motions of these
    but you can see these motions of these

    particles almost look like a movement of particles almost look like a movement
    of particles almost look like a movement of

    a stock price. a stock price. a stock price.

    The these are the exact trajectories of The these are the exact trajectories of
    The these are the exact trajectories of

    particles when they follow Brownian particles when they follow Brownian particles
    when they follow Brownian

    motion. motion. motion.

    And there is a mathematical description And there is a mathematical description
    And there is a mathematical description

    of this which is very specific. But for of this which is very specific. But for
    of this which is very specific. But for

    now we are interested in the intuition now we are interested in the intuition
    now we are interested in the intuition

    behind Brownian motion and we are going behind Brownian motion and we are going
    behind Brownian motion and we are going

    to subject our data to the Brownian to subject our data to the Brownian to subject
    our data to the Brownian

    motion. [snorts] motion. [snorts] motion. [snorts]

    Now the first thought is okay I have Now the first thought is okay I have Now
    the first thought is okay I have

    this image which has maybe it''s a 28x 28 this image which has maybe it''s a 28x
    28 this image which has maybe it''s a 28x 28

    image. So there are 784 pixels. image. So there are 784 pixels. image. So there
    are 784 pixels.

    So what am I exactly doing here? Well So what am I exactly doing here? Well'
  concept_slugs:
  - langevin-dynamics
  - probability-flow-ode
  - sde-formulation
- idx: 21
  start_sec: 1295.679
  end_sec: 1355.2
  text: 'So what am I exactly doing here? Well

    imagine that instead of these tiny dots imagine that instead of these tiny dots
    imagine that instead of these tiny dots

    you have 784 dots and all these dots are you have 784 dots and all these dots
    are you have 784 dots and all these dots are

    following a brownie in motion. [snorts] following a brownie in motion. [snorts]
    following a brownie in motion. [snorts]

    So imagine that we have a book here like So imagine that we have a book here like
    So imagine that we have a book here like

    this in front of the screen. This is our this in front of the screen. This is
    our this in front of the screen. This is our

    image. I divide this book into 784 image. I divide this book into 784 image. I
    divide this book into 784

    pixels. I take out each of these pixels pixels. I take out each of these pixels
    pixels. I take out each of these pixels

    and arrange them as dots. And I allow and arrange them as dots. And I allow and
    arrange them as dots. And I allow

    these dots to transform themselves or these dots to transform themselves or these
    dots to transform themselves or

    follow a Brownian motion follow a Brownian motion follow a Brownian motion

    and completely change themselves using and completely change themselves using
    and completely change themselves using

    the Brownian trajectory. And at the end the Brownian trajectory. And at the end
    the Brownian trajectory. And at the end

    of it, I expect these molecules or these of it, I expect these molecules or these
    of it, I expect these molecules or these

    particles to move so far from their particles to move so far from their particles
    to move so far from their

    original value that the entire image original value that the entire image original
    value that the entire image

    will become noise. That is my will become noise. That is my will become noise.
    That is my

    expectation. Okay. So, uh Okay. So, uh

    this is exactly what I''m planning to do. this is exactly what I''m planning to
    do. this is exactly what I''m planning to do.

    I''m planning to take all these images, I''m planning to take all these images,'
  concept_slugs:
  - langevin-dynamics
  - probability-flow-ode
  - sde-formulation
- idx: 22
  start_sec: 1355.2
  end_sec: 1423.11
  text: 'I''m planning to take all these images,

    divide them into pixels and subject each divide them into pixels and subject each
    divide them into pixels and subject each

    pixel to a brownian trajectory so that pixel to a brownian trajectory so that
    pixel to a brownian trajectory so that

    after enough time the data becomes after enough time the data becomes after enough
    time the data becomes

    noise. noise. noise.

    So you can see that I have taken an So you can see that I have taken an So you
    can see that I have taken an

    inspiration from the microscopic motion inspiration from the microscopic motion
    inspiration from the microscopic motion

    of fluid particles and I''m subjecting my of fluid particles and I''m subjecting
    my of fluid particles and I''m subjecting my

    data to this microscopic motion so that data to this microscopic motion so that
    data to this microscopic motion so that

    after enough time has passed it after enough time has passed it after enough time
    has passed it

    completely becomes noise. Now if you look at the two approaches Now if you look
    at the two approaches

    which I discussed earlier the DDPM and which I discussed earlier the DDPM and
    which I discussed earlier the DDPM and

    the score-based approach both of them the score-based approach both of them the
    score-based approach both of them

    have a forward diffusion process which have a forward diffusion process which
    have a forward diffusion process which

    transforms transforms transforms

    image to noise image to noise image to noise

    but but

    they have a specific form in which these they have a specific form in which these
    they have a specific form in which these

    forward diffusion processes are written forward diffusion processes are written
    forward diffusion processes are written

    which are special case of the Brownian which are special case of the Brownian
    which are special case of the Brownian

    motion itself. motion itself. motion itself.

    Now why is it a special case of the Now why is it a special case of the Now why
    is it a special case of the

    Brownian motion itself? Well, the Brownian motion itself? Well, the Brownian motion
    itself? Well, the

    Brownian motion as I mentioned it has Brownian motion as I mentioned it has Brownian
    motion as I mentioned it has

    two terms a drift term and a noise term.'
  concept_slugs:
  - langevin-dynamics
  - probability-flow-ode
  - sde-formulation
- idx: 23
  start_sec: 1423.11
  end_sec: 1472.799
  text: 'two terms a drift term and a noise term. two terms a drift term and a noise
    term.

    So DDPM has a specific formulation for So DDPM has a specific formulation for
    So DDPM has a specific formulation for

    the drift term and the noise term and the drift term and the noise term and the
    drift term and the noise term and

    noise condition score network have a noise condition score network have a noise
    condition score network have a

    specific formulation of the drift term specific formulation of the drift term
    specific formulation of the drift term

    and the noise term. But essentially both and the noise term. But essentially both
    and the noise term. But essentially both

    the trajectories are Brownian motion are the trajectories are Brownian motion
    are the trajectories are Brownian motion are

    following a stochastic motion at the following a stochastic motion at the following
    a stochastic motion at the

    heart of it. heart of it. heart of it.

    Okay, I''m using the drift and uh the Okay, I''m using the drift and uh the Okay,
    I''m using the drift and uh the

    diffusion term a lot. Let us try to diffusion term a lot. Let us try to diffusion
    term a lot. Let us try to

    intuitively understand what these two intuitively understand what these two intuitively
    understand what these two

    terms mean. terms mean. terms mean.

    So let''s take an example that you have a So let''s take an example that you have
    a So let''s take an example that you have a

    simple paper boat. You have a paper boat simple paper boat. You have a paper boat
    simple paper boat. You have a paper boat

    and you have put the paper boat on a and you have put the paper boat on a and
    you have put the paper boat on a

    river on a stream of river on a current. river on a stream of river on a current.
    river on a stream of river on a current.

    Now the question is what will affect the Now the question is what will affect
    the Now the question is what will affect the

    path of this boat? path of this boat? path of this boat?

    Well, the first thing I can see is that Well, the first thing I can see is that'
  concept_slugs:
  - langevin-dynamics
  - probability-flow-ode
  - sde-formulation
- idx: 24
  start_sec: 1472.799
  end_sec: 1524.559
  text: 'Well, the first thing I can see is that

    I can obviously see some current lines I can obviously see some current lines
    I can obviously see some current lines

    in the river. So I''ll say that well in the river. So I''ll say that well in the
    river. So I''ll say that well

    there are some current lines. So the there are some current lines. So the there
    are some current lines. So the

    boat will move according to the current. boat will move according to the current.
    boat will move according to the current.

    Right? That is true. That is the first Right? That is true. That is the first
    Right? That is true. That is the first

    part which is called as the steady part which is called as the steady part which
    is called as the steady

    drift. But there is a second part also drift. But there is a second part also
    drift. But there is a second part also

    which is the random ripples which are which is the random ripples which are which
    is the random ripples which are

    created at any point in in the lake. created at any point in in the lake. created
    at any point in in the lake.

    So these random ripples are going to So these random ripples are going to So these
    random ripples are going to

    swerve the boat left and right along swerve the boat left and right along swerve
    the boat left and right along

    with the drift. This component will be with the drift. This component will be
    with the drift. This component will be

    added to the motion of the boat. Now added to the motion of the boat. Now added
    to the motion of the boat. Now

    this is exactly the diffusion component this is exactly the diffusion component
    this is exactly the diffusion component

    and this is what is responsible for and this is what is responsible for and this
    is what is responsible for

    finally transforming the data to pure finally transforming the data to pure finally
    transforming the data to pure

    noise. The combined motion is a combination of The combined motion is a combination
    of

    a steady drift term which is the current a steady drift term which is the current'
  concept_slugs:
  - langevin-dynamics
  - probability-flow-ode
  - sde-formulation
- idx: 25
  start_sec: 1524.559
  end_sec: 1580.31
  text: 'a steady drift term which is the current

    of the lake or the river and the second of the lake or the river and the second
    of the lake or the river and the second

    term is the diffusion term which are term is the diffusion term which are term
    is the diffusion term which are

    these random ripples which are causing these random ripples which are causing
    these random ripples which are causing

    the boat to swerve left and right. the boat to swerve left and right. the boat
    to swerve left and right.

    Now this analogy is confined to the Now this analogy is confined to the Now this
    analogy is confined to the

    example of boats but example of boats but example of boats but

    this is exactly what we are seeing over this is exactly what we are seeing over
    this is exactly what we are seeing over

    here when we are transforming the data here when we are transforming the data
    here when we are transforming the data

    to noise. We have a drift term and we to noise. We have a drift term and we to
    noise. We have a drift term and we

    have a diffusion term have a diffusion term have a diffusion term

    so far. Okay. Fine. We have looked at so far. Okay. Fine. We have looked at so
    far. Okay. Fine. We have looked at

    the forward diffusion process and uh the forward diffusion process and uh the
    forward diffusion process and uh

    we looked at there are two parts the we looked at there are two parts the we looked
    at there are two parts the

    drift part and the diffusion part and drift part and the diffusion part and drift
    part and the diffusion part and

    the combined motion is a combination of the combined motion is a combination of
    the combined motion is a combination of

    this. [snorts] this. [snorts] this. [snorts]

    Now what we will do is we will apply Now what we will do is we will apply Now
    what we will do is we will apply

    this analogy to our forward diffusion this analogy to our forward diffusion this
    analogy to our forward diffusion

    process and look at a mathematical form process and look at a mathematical form
    process and look at a mathematical form

    for this forward diffusion.'
  concept_slugs:
  - langevin-dynamics
  - probability-flow-ode
  - sde-formulation
- idx: 26
  start_sec: 1580.31
  end_sec: 1638.71
  text: 'for this forward diffusion. for this forward diffusion.

    Okay. So we have converted data to noise Okay. So we have converted data to noise
    Okay. So we have converted data to noise

    and the change in the pixel values is a and the change in the pixel values is
    a and the change in the pixel values is a

    combination of deterministic drift and combination of deterministic drift and
    combination of deterministic drift and

    stochastic diffusion. stochastic diffusion. stochastic diffusion.

    Now the drift has a specific formula Now the drift has a specific formula Now
    the drift has a specific formula

    which comes as a function f of x t into which comes as a function f of x t into
    which comes as a function f of x t into

    change in time and the second is a change in time and the second is a change in
    time and the second is a

    diffusion term which depends on a diffusion term which depends on a diffusion
    term which depends on a

    function g of t. function g of t. function g of t.

    So the forward diffusion process depends So the forward diffusion process depends
    So the forward diffusion process depends

    on two terms. One is the drift term on two terms. One is the drift term on two
    terms. One is the drift term

    which is denoted as f and the second is which is denoted as f and the second is
    which is denoted as f and the second is

    the diffusion term which is denoted as the diffusion term which is denoted as
    the diffusion term which is denoted as

    g. g. g.

    Now the good part is that we know both Now the good part is that we know both
    Now the good part is that we know both

    of these terms which means that we of these terms which means that we of these
    terms which means that we

    exactly know how we are going to exactly know how we are going to exactly know
    how we are going to

    transform the data to noise. There is transform the data to noise. There is transform
    the data to noise. There is

    absolutely no learning happening here. absolutely no learning happening here.
    absolutely no learning happening here.

    You might relate this to a variational'
  concept_slugs:
  - langevin-dynamics
  - probability-flow-ode
  - sde-formulation
- idx: 27
  start_sec: 1638.71
  end_sec: 1689.76
  text: 'You might relate this to a variational You might relate this to a variational

    autoenccoder where there is an encoder autoenccoder where there is an encoder
    autoenccoder where there is an encoder

    and there is a decoder and the learning and there is a decoder and the learning
    and there is a decoder and the learning

    happens in both the encoder and the happens in both the encoder and the happens
    in both the encoder and the

    decoder. This is very different. We are decoder. This is very different. We are
    decoder. This is very different. We are

    not learning anything in the forward not learning anything in the forward not
    learning anything in the forward

    process. It is completely known to us process. It is completely known to us process.
    It is completely known to us

    because we are the ones who are deciding because we are the ones who are deciding
    because we are the ones who are deciding

    the drift term and the diffusion term. the drift term and the diffusion term.
    the drift term and the diffusion term.

    In DDPM the drift term and diffusion In DDPM the drift term and diffusion In DDPM
    the drift term and diffusion

    term was different. In uh score- based term was different. In uh score- based
    term was different. In uh score- based

    approach the drift term and the approach the drift term and the approach the drift
    term and the

    diffusion term was different. diffusion term was different. diffusion term was
    different.

    But both of these approaches can be But both of these approaches can be But both
    of these approaches can be

    viewed from this microscopic lens where viewed from this microscopic lens where
    viewed from this microscopic lens where

    we are diffusing every single pixel in we are diffusing every single pixel in
    we are diffusing every single pixel in

    the data as a brownian trajectory. Okay, now we come to the second part Okay,
    now we come to the second part

    which is a very crucial part in uh which is a very crucial part in uh which is
    a very crucial part in uh

    today''s lecture. Remember we started today''s lecture. Remember we started today''s
    lecture. Remember we started

    with our discussion with the time with our discussion with the time'
  concept_slugs:
  - langevin-dynamics
  - probability-flow-ode
  - sde-formulation
- idx: 28
  start_sec: 1689.76
  end_sec: 1745.12
  text: 'with our discussion with the time

    machine. We were asking that can we machine. We were asking that can we machine.
    We were asking that can we

    reverse the reverse the reverse the

    diffusion of the dye? Can we bring back diffusion of the dye? Can we bring back
    diffusion of the dye? Can we bring back

    the original spherical nature of the the original spherical nature of the the
    original spherical nature of the

    drop? Can we understand it? And at a drop? Can we understand it? And at a drop?
    Can we understand it? And at a

    microscopic level we had no idea how to microscopic level we had no idea how to
    microscopic level we had no idea how to

    do it. But we looked at a we used a lens do it. But we looked at a we used a lens
    do it. But we looked at a we used a lens

    and looked at it at it microscopically and looked at it at it microscopically
    and looked at it at it microscopically

    and we realized that okay microscopic and we realized that okay microscopic and
    we realized that okay microscopic

    motions are diffused are are are time motions are diffused are are are time motions
    are diffused are are are time

    reversible reversible reversible

    that''s why we subjected these pixels in that''s why we subjected these pixels
    in that''s why we subjected these pixels in

    these cat images to the brownian motion these cat images to the brownian motion
    these cat images to the brownian motion

    and now we come to the main part which and now we come to the main part which
    and now we come to the main part which

    is can we write the reverse process as is can we write the reverse process as
    is can we write the reverse process as

    well it turns out yes we can write the it turns out yes we can write the

    reverse process And uh we are helped and reverse process And uh we are helped
    and reverse process And uh we are helped and

    very grateful to this paper which was very grateful to this paper which was very
    grateful to this paper which was

    released released released

    more than 40 years back in the year 1982 more than 40 years back in the year 1982'
  concept_slugs:
  - langevin-dynamics
  - probability-flow-ode
  - sde-formulation
- idx: 29
  start_sec: 1745.12
  end_sec: 1812.149
  text: 'more than 40 years back in the year 1982

    by a single author Brian Anderson. by a single author Brian Anderson. by a single
    author Brian Anderson.

    And in this paper he wrote a formula And in this paper he wrote a formula And
    in this paper he wrote a formula

    which is so simple that it makes which is so simple that it makes which is so
    simple that it makes

    calculation of these reverse calculation of these reverse calculation of these
    reverse

    trajectories very easy. He actually gave trajectories very easy. He actually gave
    trajectories very easy. He actually gave

    a closed-ended formula using which we a closed-ended formula using which we a
    closed-ended formula using which we

    can reverse the can reverse the can reverse the

    forward diffusion process which is Brown forward diffusion process which is Brown
    forward diffusion process which is Brown

    in motion in motion in motion

    and uh it is incredible how works of and uh it is incredible how works of and
    uh it is incredible how works of

    these single authors are still being these single authors are still being these
    single authors are still being

    used in the AI literature and u they are used in the AI literature and u they
    are used in the AI literature and u they are

    at the heart of diffusion models which at the heart of diffusion models which
    at the heart of diffusion models which

    power image generation, video generation power image generation, video generation
    power image generation, video generation

    and and audio generation. and and audio generation. and and audio generation.

    Whenever I see examples like this, my Whenever I see examples like this, my Whenever
    I see examples like this, my

    belief in research always gets belief in research always gets belief in research
    always gets

    strengthened and u the incremental strengthened and u the incremental strengthened
    and u the incremental

    nature of research where each work nature of research where each work nature of
    research where each work

    builds upon the work which has come builds upon the work which has come builds
    upon the work which has come

    previously. previously. previously.

    It it really uh resonates with me and I It it really uh resonates with me and
    I It it really uh resonates with me and I

    appreciate all the researchers who spend'
  concept_slugs:
  - langevin-dynamics
  - probability-flow-ode
  - sde-formulation
- idx: 30
  start_sec: 1812.149
  end_sec: 1859.84
  text: 'appreciate all the researchers who spend appreciate all the researchers who
    spend

    a lot of time in writing these papers. a lot of time in writing these papers.
    a lot of time in writing these papers.

    Okay. And what does the reverse formula Okay. And what does the reverse formula
    Okay. And what does the reverse formula

    look like? Well, the forward formula has look like? Well, the forward formula
    has look like? Well, the forward formula has

    two terms. The drift term and the two terms. The drift term and the two terms.
    The drift term and the

    diffusion term. As I have shown over diffusion term. As I have shown over diffusion
    term. As I have shown over

    here, here, here,

    the reverse formula the reverse formula the reverse formula

    also has two terms. The diffusion term also has two terms. The diffusion term
    also has two terms. The diffusion term

    remains the same. As you can see, we remains the same. As you can see, we remains
    the same. As you can see, we

    will focus on the drift term, which is will focus on the drift term, which is
    will focus on the drift term, which is

    the combination of the drift term for the combination of the drift term for the
    combination of the drift term for

    the forward diffusion process. And there the forward diffusion process. And there
    the forward diffusion process. And there

    is an additional factor being added is an additional factor being added is an
    additional factor being added

    here. We will only focus on that factor here. We will only focus on that factor
    here. We will only focus on that factor

    right now because that was the biggest right now because that was the biggest
    right now because that was the biggest

    contribution from the Anderson paper. contribution from the Anderson paper. contribution
    from the Anderson paper.

    And that factor is a multiplication of And that factor is a multiplication of
    And that factor is a multiplication of

    two terms. The first term is the square two terms. The first term is the square
    two terms. The first term is the square

    of G of T which is the diffusion term in of G of T which is the diffusion term
    in'
  concept_slugs:
  - langevin-dynamics
  - probability-flow-ode
  - sde-formulation
- idx: 31
  start_sec: 1859.84
  end_sec: 1912.87
  text: 'of G of T which is the diffusion term in

    the forward process. And the second term the forward process. And the second term
    the forward process. And the second term

    is the score function. is the score function. is the score function.

    We have not discussed what is score We have not discussed what is score We have
    not discussed what is score

    function in this lecture. But uh function in this lecture. But uh function in
    this lecture. But uh

    you might have heard me talk about score you might have heard me talk about score
    you might have heard me talk about score

    based approach. based approach. based approach.

    And the reason why the score-based And the reason why the score-based And the
    reason why the score-based

    approach works so beautifully is because approach works so beautifully is because
    approach works so beautifully is because

    it naturally comes up in the formula for it naturally comes up in the formula
    for it naturally comes up in the formula for

    the reverse the reverse the reverse

    diffusion process. It actually comes up diffusion process. It actually comes up
    diffusion process. It actually comes up

    as a separate function. as a separate function. as a separate function.

    And you might look at this equation and And you might look at this equation and
    And you might look at this equation and

    say that I already know f, I already say that I already know f, I already say
    that I already know f, I already

    don''t know g. So can I directly predict don''t know g. So can I directly predict
    don''t know g. So can I directly predict

    the reverse motion? Can I reverse from the reverse motion? Can I reverse from
    the reverse motion? Can I reverse from

    noise to the images of cats? The answer noise to the images of cats? The answer
    noise to the images of cats? The answer

    is no. because the score function is not is no. because the score function is
    not is no. because the score function is not

    very easy to calculate. If this was very very easy to calculate. If this was very
    very easy to calculate. If this was very

    easy then we would have directly easy then we would have directly easy then we
    would have directly

    reversed from noise to the image and'
  concept_slugs:
  - langevin-dynamics
  - probability-flow-ode
  - sde-formulation
- idx: 32
  start_sec: 1912.87
  end_sec: 1964.48
  text: 'reversed from noise to the image and reversed from noise to the image and

    this is where the learning will happen. this is where the learning will happen.
    this is where the learning will happen.

    Why is the score function difficult to Why is the score function difficult to
    Why is the score function difficult to

    calculate? calculate? calculate?

    Well to understand that first we will Well to understand that first we will Well
    to understand that first we will

    have to look at what is a score function have to look at what is a score function
    have to look at what is a score function

    exactly exactly exactly

    and I''m going to give you a analogy to and I''m going to give you a analogy to
    and I''m going to give you a analogy to

    understand the score function. Imagine understand the score function. Imagine
    understand the score function. Imagine

    that you''re out in the ocean and you''re that you''re out in the ocean and you''re
    that you''re out in the ocean and you''re

    trying to find a shark. trying to find a shark. trying to find a shark.

    You go with a compass You go with a compass You go with a compass

    which gives you exactly where the sharks which gives you exactly where the sharks
    which gives you exactly where the sharks

    are present. are present. are present.

    So you start out with a random location. So you start out with a random location.
    So you start out with a random location.

    Your compass tells you go go left. You Your compass tells you go go left. You
    Your compass tells you go go left. You

    go towards the left direction. You move. go towards the left direction. You move.
    go towards the left direction. You move.

    Then your compos says oh no no no go go Then your compos says oh no no no go go
    Then your compos says oh no no no go go

    right. Go straight. Go left. and then it right. Go straight. Go left. and then
    it right. Go straight. Go left. and then it

    guides you until you are in the region guides you until you are in the region
    guides you until you are in the region

    where the density of the sharks is where the density of the sharks is'
  concept_slugs:
  - langevin-dynamics
  - probability-flow-ode
  - sde-formulation
- idx: 33
  start_sec: 1964.48
  end_sec: 2024.72
  text: 'where the density of the sharks is

    maximum. maximum. maximum.

    Now score function is exactly like this Now score function is exactly like this
    Now score function is exactly like this

    compass and sharks are your data. You''re compass and sharks are your data. You''re
    compass and sharks are your data. You''re

    using a compass to navigate yourself using a compass to navigate yourself using
    a compass to navigate yourself

    around the data field so that you find around the data field so that you find
    around the data field so that you find

    the region where the data is maximum the region where the data is maximum the
    region where the data is maximum

    where the data density is maximum. where the data density is maximum. where the
    data density is maximum.

    [snorts] So the score function points to [snorts] So the score function points
    to [snorts] So the score function points to

    the direction where the direction where the direction where

    the density of the data is maximum. the density of the data is maximum. the density
    of the data is maximum.

    If you look at this this example, the If you look at this this example, the If
    you look at this this example, the

    black dots is the region where the black dots is the region where the black dots
    is the region where the

    density of the data is the highest. That density of the data is the highest. That
    density of the data is the highest. That

    is where the sharks are present. And you is where the sharks are present. And
    you is where the sharks are present. And you

    can see all the arrows are kind of can see all the arrows are kind of can see
    all the arrows are kind of

    pointing towards those regions. Well, pointing towards those regions. Well, pointing
    towards those regions. Well,

    those arrows are the score function. And those arrows are the score function.
    And those arrows are the score function. And

    you can write them as gradient of log of you can write them as gradient of log
    of you can write them as gradient of log of

    P of T where P of T is the probability P of T where P of T is the probability
    P of T where P of T is the probability

    density. density.'
  concept_slugs:
  - langevin-dynamics
  - probability-flow-ode
  - sde-formulation
- idx: 34
  start_sec: 2024.72
  end_sec: 2074.0
  text: 'density.

    Now where does the gradient and log come Now where does the gradient and log come
    Now where does the gradient and log come

    from? Well, the gradient comes from uh from? Well, the gradient comes from uh
    from? Well, the gradient comes from uh

    your objective of going from lower your objective of going from lower your objective
    of going from lower

    density to a higher density. So the density to a higher density. So the density
    to a higher density. So the

    gradient naturally puts you in that gradient naturally puts you in that gradient
    naturally puts you in that

    direction. direction. direction.

    And where does the log come from? If you And where does the log come from? If
    you And where does the log come from? If you

    are in a region where the probability is are in a region where the probability
    is are in a region where the probability is

    very low then you need a very large step very low then you need a very large step
    very low then you need a very large step

    right that''s why you take a log because right that''s why you take a log because
    right that''s why you take a log because

    log of lower value is very high. So if log of lower value is very high. So if
    log of lower value is very high. So if

    you''re very large if you''re away from you''re very large if you''re away from
    you''re very large if you''re away from

    the sharks you take bigger steps and you the sharks you take bigger steps and
    you the sharks you take bigger steps and you

    move closer faster. move closer faster. move closer faster.

    That is what the score function does. That is what the score function does. That
    is what the score function does.

    Now if you look at this formula you can Now if you look at this formula you can
    Now if you look at this formula you can

    see that it has this probability see that it has this probability see that it
    has this probability

    function which is exactly what we want function which is exactly what we want
    function which is exactly what we want

    to predict. Remember we started with a to predict. Remember we started with a'
  concept_slugs:
  - langevin-dynamics
  - probability-flow-ode
  - sde-formulation
- idx: 35
  start_sec: 2074.0
  end_sec: 2134.63
  text: 'to predict. Remember we started with a

    discussion that we want to predict the discussion that we want to predict the
    discussion that we want to predict the

    distribution of the cats and this distribution of the cats and this distribution
    of the cats and this

    probability function is something which probability function is something which
    probability function is something which

    we do not know. That is the reason we we do not know. That is the reason we we
    do not know. That is the reason we

    cannot substitute this value directly in cannot substitute this value directly
    in cannot substitute this value directly in

    the score function the score function the score function

    which becomes the bottleneck in this which becomes the bottleneck in this which
    becomes the bottleneck in this

    formula. formula. formula.

    So what is the way around? How do we So what is the way around? How do we So what
    is the way around? How do we

    learn the score function? In today''s lecture, I will not be In today''s lecture,
    I will not be

    covering how the score function is covering how the score function is covering
    how the score function is

    learned. But I am going to assume that learned. But I am going to assume that
    learned. But I am going to assume that

    we have learned the score function. we have learned the score function. we have
    learned the score function.

    To understand how the score function is To understand how the score function is
    To understand how the score function is

    learned, you can look at my previous two learned, you can look at my previous
    two learned, you can look at my previous two

    lectures which talk about score function lectures which talk about score function
    lectures which talk about score function

    in much more detail. But the process is again simple. Uh we But the process is
    again simple. Uh we

    add noise deliberately and then we learn add noise deliberately and then we learn
    add noise deliberately and then we learn

    how much noise is added and in that how much noise is added and in that how much
    noise is added and in that

    process we learn the score function. process we learn the score function. process
    we learn the score function.

    For now let''s simplify things. Let us'
  concept_slugs:
  - langevin-dynamics
  - probability-flow-ode
  - sde-formulation
- idx: 36
  start_sec: 2134.63
  end_sec: 2190.31
  text: 'For now let''s simplify things. Let us For now let''s simplify things. Let
    us

    assume that the score function is assume that the score function is assume that
    the score function is

    already learned. already learned. already learned.

    Okay. So uh let us say that we know the Okay. So uh let us say that we know the
    Okay. So uh let us say that we know the

    score function already and in the score function already and in the score function
    already and in the

    process of learning the score function process of learning the score function
    process of learning the score function

    we have learned a lot about our data as we have learned a lot about our data as
    we have learned a lot about our data as

    well. Okay. Now let''s say we know the score Okay. Now let''s say we know the
    score

    function. So we know f, we know g and we function. So we know f, we know g and
    we function. So we know f, we know g and we

    know s. The natural question is how do know s. The natural question is how do
    know s. The natural question is how do

    we sample from this? we sample from this? we sample from this?

    How do we go back from noise to the How do we go back from noise to the How do
    we go back from noise to the

    data? If we already have the reverse data? If we already have the reverse data?
    If we already have the reverse

    time process equation given by Anderson time process equation given by Anderson
    time process equation given by Anderson

    and we know all the terms, how do we go and we know all the terms, how do we go
    and we know all the terms, how do we go

    back back from noise to data? back back from noise to data? back back from noise
    to data?

    Let''s look at uh the diffusion the the Let''s look at uh the diffusion the the
    Let''s look at uh the diffusion the the

    reverse process again and uh again I''m reverse process again and uh again I''m
    reverse process again and uh again I''m

    emphasizing that the drift term here emphasizing that the drift term here emphasizing
    that the drift term here

    comprises of the drift in the forward'
  concept_slugs:
  - langevin-dynamics
  - probability-flow-ode
  - sde-formulation
- idx: 37
  start_sec: 2190.31
  end_sec: 2246.23
  text: 'comprises of the drift in the forward comprises of the drift in the forward

    diffusion and the factor which depends diffusion and the factor which depends
    diffusion and the factor which depends

    on the score function and the diffusion on the score function and the diffusion
    on the score function and the diffusion

    term remains the same. term remains the same. term remains the same.

    Now our only job is to discretise this Now our only job is to discretise this
    Now our only job is to discretise this

    which means that we are going to replace which means that we are going to replace
    which means that we are going to replace

    dx by delta x. We are going to replace dx by delta x. We are going to replace
    dx by delta x. We are going to replace

    dt by deltat t and we are going to dt by deltat t and we are going to dt by deltat
    t and we are going to

    replace dw by a random variable zed replace dw by a random variable zed replace
    dw by a random variable zed

    which takes a value between 0 and 1 and which takes a value between 0 and 1 and
    which takes a value between 0 and 1 and

    root of delta t. This is the diffusion root of delta t. This is the diffusion
    root of delta t. This is the diffusion

    term in the brownian motion. term in the brownian motion. term in the brownian
    motion.

    Now the key concept here is that the Now the key concept here is that the Now
    the key concept here is that the

    noise scales with the square root of noise scales with the square root of noise
    scales with the square root of

    time and not time itself. time and not time itself. time and not time itself.

    The reason is that if you take any The reason is that if you take any The reason
    is that if you take any

    brownian trajectory and you take any two brownian trajectory and you take any
    two brownian trajectory and you take any two

    points separated by a gap of delta t you points separated by a gap of delta t
    you points separated by a gap of delta t you

    ask the question what is the variation'
  concept_slugs:
  - langevin-dynamics
  - probability-flow-ode
  - sde-formulation
- idx: 38
  start_sec: 2246.23
  end_sec: 2295.76
  text: 'ask the question what is the variation ask the question what is the variation

    in the values of these two points. It in the values of these two points. It in
    the values of these two points. It

    turns out that turns out that turns out that

    the variance in these values of the variance in these values of the variance in
    these values of

    difference between these two points difference between these two points difference
    between these two points

    scales as deltat t which is the scales as deltat t which is the scales as deltat
    t which is the

    difference in this time which means that difference in this time which means that
    difference in this time which means that

    as you move further and farther away if as you move further and farther away if
    as you move further and farther away if

    you fix one point if the second point you fix one point if the second point you
    fix one point if the second point

    moves farther and further away the moves farther and further away the moves farther
    and further away the

    variance will go on increasing as delta variance will go on increasing as delta
    variance will go on increasing as delta

    t. Now because the variance increases as t. Now because the variance increases
    as t. Now because the variance increases as

    delta t the standard deviation increases delta t the standard deviation increases
    delta t the standard deviation increases

    at as root of delta t and that is why at as root of delta t and that is why at
    as root of delta t and that is why

    you have a root of delta t in this you have a root of delta t in this you have
    a root of delta t in this

    formula. Okay. Now you might say okay what is the Okay. Now you might say okay
    what is the

    next step? Well now you have learned to next step? Well now you have learned to
    next step? Well now you have learned to

    find the increment of x which is the find the increment of x which is the find
    the increment of x which is the

    pixel intensity pixel intensity pixel intensity

    in terms of delta t. So if you have in terms of delta t. So if you have'
  concept_slugs:
  - langevin-dynamics
  - probability-flow-ode
  - sde-formulation
- idx: 39
  start_sec: 2295.76
  end_sec: 2344.96
  text: 'in terms of delta t. So if you have

    delta t you calculate delta x then you delta t you calculate delta x then you
    delta t you calculate delta x then you

    again substitute delta t calculate delta again substitute delta t calculate delta
    again substitute delta t calculate delta

    x and you move from noise to the data x and you move from noise to the data x
    and you move from noise to the data

    recursively using this equation. recursively using this equation. recursively
    using this equation.

    Once you have discretized this you can Once you have discretized this you can
    Once you have discretized this you can

    enter into a loop where you can enter into a loop where you can enter into a loop
    where you can

    continuously run this discretization continuously run this discretization continuously
    run this discretization

    and uh you can reach to the original and uh you can reach to the original and
    uh you can reach to the original

    image. this equation or because of this image. this equation or because of this
    image. this equation or because of this

    nature of discretization and the way nature of discretization and the way nature
    of discretization and the way

    this equation appears, it is also called this equation appears, it is also called
    this equation appears, it is also called

    as a stochastic differential equation. as a stochastic differential equation.
    as a stochastic differential equation.

    An ordinary differential equation would An ordinary differential equation would
    An ordinary differential equation would

    not have this second part which comes up not have this second part which comes
    up not have this second part which comes up

    as root of delta t square root of time. as root of delta t square root of time.
    as root of delta t square root of time.

    It would only have this first part. But It would only have this first part. But
    It would only have this first part. But

    here we have the second part also. That here we have the second part also. That
    here we have the second part also. That

    is why it is called as a stochastic is why it is called as a stochastic is why
    it is called as a stochastic

    differential equation or an SDE. differential equation or an SDE.'
  concept_slugs:
  - langevin-dynamics
  - probability-flow-ode
  - sde-formulation
- idx: 40
  start_sec: 2344.96
  end_sec: 2402.24
  text: 'differential equation or an SDE.

    This formulation was laid down in a This formulation was laid down in a This formulation
    was laid down in a

    paper by Song and Arman in the year paper by Song and Arman in the year paper
    by Song and Arman in the year

    2020. I will link the description below 2020. I will link the description below
    2020. I will link the description below

    in the description section. in the description section. in the description section.

    But essentially at the heart of the But essentially at the heart of the But essentially
    at the heart of the

    paper it''s it it talks about paper it''s it it talks about paper it''s it it
    talks about

    discretizing this equation and forming a discretizing this equation and forming
    a discretizing this equation and forming a

    connection between the SDE framework connection between the SDE framework connection
    between the SDE framework

    which is the stochastic differential which is the stochastic differential which
    is the stochastic differential

    equation framework and the previous two equation framework and the previous two
    equation framework and the previous two

    approaches which were DDPM and score approaches which were DDPM and score approaches
    which were DDPM and score

    based function or NCSN noise conditional based function or NCSN noise conditional
    based function or NCSN noise conditional

    score networks. The sampling process looks something The sampling process looks
    something

    like this. We start with noise. like this. We start with noise. like this. We
    start with noise.

    Then um Then um Then um

    remember we have two terms. We have a remember we have two terms. We have a remember
    we have two terms. We have a

    diffusion term and we have a noise term. diffusion term and we have a noise term.
    diffusion term and we have a noise term.

    This is the sorry we have a drift term This is the sorry we have a drift term
    This is the sorry we have a drift term

    and a noise term. So the blue arrow and a noise term. So the blue arrow and a
    noise term. So the blue arrow

    represents the drift term. The red arrow represents the drift term. The red arrow
    represents the drift term. The red arrow

    represents the noise term. So we go from represents the noise term. So we go from'
  concept_slugs:
  - langevin-dynamics
  - probability-flow-ode
  - sde-formulation
- idx: 41
  start_sec: 2402.24
  end_sec: 2454.88
  text: 'represents the noise term. So we go from

    the first iteration to the second the first iteration to the second the first
    iteration to the second

    iteration. Then we again do diffusion iteration. Then we again do diffusion iteration.
    Then we again do diffusion

    and drift. We go here. Again we do drift and drift. We go here. Again we do drift
    and drift. We go here. Again we do drift

    and diffusion. We go here. You can see and diffusion. We go here. You can see
    and diffusion. We go here. You can see

    the clarity of the image is slowly the clarity of the image is slowly the clarity
    of the image is slowly

    becoming better and better and better. becoming better and better and better.
    becoming better and better and better.

    And we do this until we get the original And we do this until we get the original
    And we do this until we get the original

    image. image. image.

    This is also called as the oiler maruama This is also called as the oiler maruama
    This is also called as the oiler maruama

    solver. This is the simplest way of solver. This is the simplest way of solver.
    This is the simplest way of

    solving this particular stoastic solving this particular stoastic solving this
    particular stoastic

    differential equation. And you can see differential equation. And you can see
    differential equation. And you can see

    it can be visualized in the drift and it can be visualized in the drift and it
    can be visualized in the drift and

    the noise components. the noise components. the noise components.

    So this is how we solve the forward So this is how we solve the forward So this
    is how we solve the forward

    process and the reverse process. Um and process and the reverse process. Um and
    process and the reverse process. Um and

    why we have used the microscopic nature why we have used the microscopic nature
    why we have used the microscopic nature

    of the diffusion which we discussed at of the diffusion which we discussed at
    of the diffusion which we discussed at

    the start. Now it might become clear to the start. Now it might become clear to
    the start. Now it might become clear to

    you because we know the exact equation you because we know the exact equation'
  concept_slugs:
  - langevin-dynamics
  - probability-flow-ode
  - sde-formulation
- idx: 42
  start_sec: 2454.88
  end_sec: 2509.27
  text: 'you because we know the exact equation

    of the reverse process and we use that of the reverse process and we use that
    of the reverse process and we use that

    same equation for sampling. same equation for sampling. same equation for sampling.

    The only thing we have done here is we The only thing we have done here is we
    The only thing we have done here is we

    have different ways of or we have have different ways of or we have have different
    ways of or we have

    predicted the score function directly. predicted the score function directly.
    predicted the score function directly.

    We have assumed we know the score We have assumed we know the score We have assumed
    we know the score

    function but there is a way to predict function but there is a way to predict
    function but there is a way to predict

    the score function from the data itself. Okay. So uh now what we will do is we
    Okay. So uh now what we will do is we

    will take a example a practical example will take a example a practical example
    will take a example a practical example

    and we will understand the forward and and we will understand the forward and
    and we will understand the forward and

    diffusion process from a practical point diffusion process from a practical point
    diffusion process from a practical point

    of view and uh through this we will also of view and uh through this we will also
    of view and uh through this we will also

    get a firm understanding of the concepts get a firm understanding of the concepts
    get a firm understanding of the concepts

    we have discussed so far and uh we will we have discussed so far and uh we will
    we have discussed so far and uh we will

    get confidence in the SDE or the get confidence in the SDE or the get confidence
    in the SDE or the

    stoastic differential equation stoastic differential equation stoastic differential
    equation

    framework. framework. framework.

    The example we will take is imagine The example we will take is imagine The example
    we will take is imagine

    you''re training a generative model on a you''re training a generative model on
    a you''re training a generative model on a

    data set consisting only of images of'
  concept_slugs:
  - langevin-dynamics
  - probability-flow-ode
  - sde-formulation
- idx: 43
  start_sec: 2509.27
  end_sec: 2566.72
  text: 'data set consisting only of images of data set consisting only of images
    of

    handwritten digits which are ones and handwritten digits which are ones and handwritten
    digits which are ones and

    eights. eights. eights.

    Now instead of cats we are taking these Now instead of cats we are taking these
    Now instead of cats we are taking these

    two handwritten digits 1 and 8. two handwritten digits 1 and 8. two handwritten
    digits 1 and 8.

    And the objective is is to find out the And the objective is is to find out the
    And the objective is is to find out the

    probability density probability density probability density

    or the distribution of these images. or the distribution of these images. or the
    distribution of these images.

    Now let''s say the distribution looks Now let''s say the distribution looks Now
    let''s say the distribution looks

    like a biodal distribution like a biodal distribution like a biodal distribution

    where the first mode corresponds to where the first mode corresponds to where
    the first mode corresponds to

    digit one and the second mode digit one and the second mode digit one and the
    second mode

    corresponds to digit two. I have taken a corresponds to digit two. I have taken
    a corresponds to digit two. I have taken a

    biodal data distribution because it''s biodal data distribution because it''s
    biodal data distribution because it''s

    going to help me explain certain things. going to help me explain certain things.
    going to help me explain certain things.

    But this is the distribution that we But this is the distribution that we But
    this is the distribution that we

    want to sample from. But we have no idea want to sample from. But we have no idea
    want to sample from. But we have no idea

    about this distribution. We are only about this distribution. We are only about
    this distribution. We are only

    given a bunch of handwritten digits once given a bunch of handwritten digits once
    given a bunch of handwritten digits once

    and eights and we are asked to sample and eights and we are asked to sample and
    eights and we are asked to sample

    images from a distribution which look images from a distribution which look images
    from a distribution which look

    like these handwritten digits. like these handwritten digits.'
  concept_slugs:
  - langevin-dynamics
  - probability-flow-ode
  - sde-formulation
- idx: 44
  start_sec: 2566.72
  end_sec: 2621.44
  text: 'like these handwritten digits.

    Okay. So uh we are expecting a biodal Okay. So uh we are expecting a biodal Okay.
    So uh we are expecting a biodal

    distribution. This is what where we want distribution. This is what where we want
    distribution. This is what where we want

    to go. to go. to go.

    Now imagine that this is the Now imagine that this is the Now imagine that this
    is the

    distribution which is the dye and you distribution which is the dye and you distribution
    which is the dye and you

    are diffusing the dye so that the are diffusing the dye so that the are diffusing
    the dye so that the

    structure slowly disappears. The red structure slowly disappears. The red structure
    slowly disappears. The red

    paint is slowly dissolving in water paint is slowly dissolving in water paint
    is slowly dissolving in water

    becoming uniform over time and uh we are becoming uniform over time and uh we
    are becoming uniform over time and uh we are

    using a forward diffusion process as the using a forward diffusion process as
    the using a forward diffusion process as the

    first step first step first step

    and we are going to use this microscopic and we are going to use this microscopic
    and we are going to use this microscopic

    approach. So we are going to subject approach. So we are going to subject approach.
    So we are going to subject

    every pixel in these handwritten digits every pixel in these handwritten digits
    every pixel in these handwritten digits

    to a brownian motion and then we will to a brownian motion and then we will to
    a brownian motion and then we will

    learn to reverse the brownian motion. learn to reverse the brownian motion. learn
    to reverse the brownian motion.

    Okay. So we will diffuse each Okay. So we will diffuse each Okay. So we will diffuse
    each

    handwritten digit such such that like a handwritten digit such such that like
    a handwritten digit such such that like a

    particle each image follows a brownie in particle each image follows a brownie
    in particle each image follows a brownie in

    motion or more specifically each pixel motion or more specifically each pixel
    motion or more specifically each pixel

    in the image follows a brownie in in the image follows a brownie in'
  concept_slugs:
  - langevin-dynamics
  - probability-flow-ode
  - sde-formulation
- idx: 45
  start_sec: 2621.44
  end_sec: 2680.56
  text: 'in the image follows a brownie in

    motion. motion.

    Okay. So just like a paint is diffusing Okay. So just like a paint is diffusing
    Okay. So just like a paint is diffusing

    in water our in water our in water our

    original distribution is diffusing and original distribution is diffusing and
    original distribution is diffusing and

    we are transforming it to noise using we are transforming it to noise using we
    are transforming it to noise using

    brownian motion. How does that look brownian motion. How does that look brownian
    motion. How does that look

    like? Well, on the left you can see this like? Well, on the left you can see this
    like? Well, on the left you can see this

    is the distribution which we don''t have is the distribution which we don''t have
    is the distribution which we don''t have

    any idea about. But we are transforming any idea about. But we are transforming
    any idea about. But we are transforming

    every image through a trajectory which every image through a trajectory which
    every image through a trajectory which

    looks like this. You can see as we move looks like this. You can see as we move
    looks like this. You can see as we move

    from left to right the myodel from left to right the myodel from left to right
    the myodel

    distribution gets converted to a distribution gets converted to a distribution
    gets converted to a

    unimodel distribution because it gets unimodel distribution because it gets unimodel
    distribution because it gets

    converted to noise. converted to noise. converted to noise.

    And all of these trajectories And all of these trajectories And all of these trajectories

    these are the brownian motion followed these are the brownian motion followed
    these are the brownian motion followed

    by every single pixel or we can rather by every single pixel or we can rather
    by every single pixel or we can rather

    say image in this trajectory. say image in this trajectory. say image in this
    trajectory.

    Now this is a simplified picture. In Now this is a simplified picture. In Now
    this is a simplified picture. In

    reality reality reality

    uh this is just a one-dimensional uh this is just a one-dimensional uh this is
    just a one-dimensional

    trajectory I have shown but in reality trajectory I have shown but in reality'
  concept_slugs:
  - langevin-dynamics
  - probability-flow-ode
  - sde-formulation
- idx: 46
  start_sec: 2680.56
  end_sec: 2731.52
  text: 'trajectory I have shown but in reality

    we have these 784 pixels. So it will be we have these 784 pixels. So it will be
    we have these 784 pixels. So it will be

    in a 784dimensional space which is in a 784dimensional space which is in a 784dimensional
    space which is

    impossible for us to visualize impossible for us to visualize impossible for us
    to visualize

    but for clarity we have assumed that but for clarity we have assumed that but
    for clarity we have assumed that

    it''s a 1D for for reference and the it''s a 1D for for reference and the it''s
    a 1D for for reference and the

    particles look like you can see there is particles look like you can see there
    is particles look like you can see there is

    a drift term and a diffusion term both a drift term and a diffusion term both
    a drift term and a diffusion term both

    because if there was just a diffusion because if there was just a diffusion because
    if there was just a diffusion

    term you would see the particles moving term you would see the particles moving
    term you would see the particles moving

    around the mean but now we are seeing around the mean but now we are seeing around
    the mean but now we are seeing

    the particles also drifting with time. the particles also drifting with time.
    the particles also drifting with time.

    So this is the forward diffusion So this is the forward diffusion So this is the
    forward diffusion

    process. We have transformed the process. We have transformed the process. We
    have transformed the

    data to noise. data to noise. data to noise.

    Now we are going to and and and here we Now we are going to and and and here we
    Now we are going to and and and here we

    know the drift term, the diffusion term know the drift term, the diffusion term
    know the drift term, the diffusion term

    F and G are decided by us. We know them F and G are decided by us. We know them
    F and G are decided by us. We know them

    completely. completely. completely.

    Now the next step is we know that the Now the next step is we know that the'
  concept_slugs:
  - langevin-dynamics
  - probability-flow-ode
  - sde-formulation
- idx: 47
  start_sec: 2731.52
  end_sec: 2788.4
  text: 'Now the next step is we know that the

    microscopic brownian motion is microscopic brownian motion is microscopic brownian
    motion is

    reversible. Uh because as you can see we reversible. Uh because as you can see
    we reversible. Uh because as you can see we

    cannot tell if this video is being cannot tell if this video is being cannot tell
    if this video is being

    played forward or backward. played forward or backward. played forward or backward.

    and Anderson has given us the formula and Anderson has given us the formula and
    Anderson has given us the formula

    for the reverse motion. for the reverse motion. for the reverse motion.

    And we are going to assume that we have And we are going to assume that we have
    And we are going to assume that we have

    trained a neural network to learn the trained a neural network to learn the trained
    a neural network to learn the

    score function. That is one block which score function. That is one block which
    score function. That is one block which

    is not covered in this lecture. Uh but is not covered in this lecture. Uh but
    is not covered in this lecture. Uh but

    we are going to assume for now that the we are going to assume for now that the
    we are going to assume for now that the

    score function is learned. score function is learned. score function is learned.

    uh typically the score function assumes uh typically the score function assumes
    uh typically the score function assumes

    a a a

    unit as as an architecture but uh we unit as as an architecture but uh we unit
    as as an architecture but uh we

    will cover that briefly towards the end will cover that briefly towards the end
    will cover that briefly towards the end

    of this lecture. Okay. So the score function is predicted Okay. So the score function
    is predicted

    using a model which we train and once we using a model which we train and once
    we using a model which we train and once we

    know that we have access to F, G and S know that we have access to F, G and S
    know that we have access to F, G and S

    as well. as well.'
  concept_slugs:
  - langevin-dynamics
  - probability-flow-ode
  - sde-formulation
- idx: 48
  start_sec: 2788.4
  end_sec: 2836.72
  text: 'as well.

    And now you can see on the left hand And now you can see on the left hand And
    now you can see on the left hand

    side we have noise and we are using the side we have noise and we are using the
    side we have noise and we are using the

    discretized formulation of the SD which discretized formulation of the SD which
    discretized formulation of the SD which

    is the oiler maruama equation and we are is the oiler maruama equation and we
    are is the oiler maruama equation and we are

    going from noise to data and we know going from noise to data and we know going
    from noise to data and we know

    exactly what the trajectory to follow exactly what the trajectory to follow exactly
    what the trajectory to follow

    because the microscopic motion is time because the microscopic motion is time
    because the microscopic motion is time

    reversible right so we know F we know G reversible right so we know F we know
    G reversible right so we know F we know G

    and we know S. So as long as the score and we know S. So as long as the score
    and we know S. So as long as the score

    function is trained properly, we should function is trained properly, we should
    function is trained properly, we should

    be able to go from noise to images which be able to go from noise to images which
    be able to go from noise to images which

    you can see from uh you can see from uh you can see from uh

    this image which articulates the this image which articulates the this image which
    articulates the

    brownian motion trajectories but rather brownian motion trajectories but rather
    brownian motion trajectories but rather

    in a reverse way. So you can see that in a reverse way. So you can see that in
    a reverse way. So you can see that

    the reverse motion also looks like a the reverse motion also looks like a the
    reverse motion also looks like a

    brownian motion brownian motion brownian motion

    uh where there is a drift term and a uh where there is a drift term and a uh where
    there is a drift term and a

    diffusion term but this time the diffusion term but this time the'
  concept_slugs:
  - langevin-dynamics
  - probability-flow-ode
  - sde-formulation
- idx: 49
  start_sec: 2836.72
  end_sec: 2888.88
  text: 'diffusion term but this time the

    trajectory is spread into two very trajectory is spread into two very trajectory
    is spread into two very

    nicely and uh we do get a biodal nicely and uh we do get a biodal nicely and uh
    we do get a biodal

    distribution at the end which is very distribution at the end which is very distribution
    at the end which is very

    interesting. This is how we learn to generate samples This is how we learn to
    generate samples

    from a distribution which is not known from a distribution which is not known
    from a distribution which is not known

    to us. But we are only given some to us. But we are only given some to us. But
    we are only given some

    handful of images and uh this is exactly handful of images and uh this is exactly
    handful of images and uh this is exactly

    the framework which current diffusion the framework which current diffusion the
    framework which current diffusion

    models follow. models follow. models follow.

    Uh there are two tracks which is first Uh there are two tracks which is first
    Uh there are two tracks which is first

    is DDPM and the second is the energy is DDPM and the second is the energy is DDPM
    and the second is the energy

    based track which is the score function. based track which is the score function.
    based track which is the score function.

    But the stochastic differential equation But the stochastic differential equation
    But the stochastic differential equation

    approach SD approach unifies both of approach SD approach unifies both of approach
    SD approach unifies both of

    these where both of these are just these where both of these are just these where
    both of these are just

    special cases of selecting the drift special cases of selecting the drift special
    cases of selecting the drift

    term and the diffusion term. term and the diffusion term. term and the diffusion
    term.

    And we can see now why the score And we can see now why the score And we can see
    now why the score

    function becomes so important. You might function becomes so important. You might
    function becomes so important. You might

    have seen this word score function in have seen this word score function in'
  concept_slugs:
  - langevin-dynamics
  - probability-flow-ode
  - sde-formulation
- idx: 50
  start_sec: 2888.88
  end_sec: 2939.99
  text: 'have seen this word score function in

    many papers but only after going through many papers but only after going through
    many papers but only after going through

    the SD framework we really understand the SD framework we really understand the
    SD framework we really understand

    why it becomes plays such an important why it becomes plays such an important
    why it becomes plays such an important

    role in the formulation. role in the formulation. role in the formulation.

    Now we actually solve this problem uh Now we actually solve this problem uh Now
    we actually solve this problem uh

    using Google Collab. I have shared the using Google Collab. I have shared the
    using Google Collab. I have shared the

    link in the description section. I want link in the description section. I want
    link in the description section. I want

    all of you to go through the details of all of you to go through the details of
    all of you to go through the details of

    this notebook properly, understand all this notebook properly, understand all
    this notebook properly, understand all

    the different components the different components the different components

    and uh finally the results we get after and uh finally the results we get after
    and uh finally the results we get after

    500 iterations. It''s it''s it''s not very 500 iterations. It''s it''s it''s not
    very 500 iterations. It''s it''s it''s not very

    good. After 5,000 iterations, you can good. After 5,000 iterations, you can good.
    After 5,000 iterations, you can

    see we are slowly starting to predict see we are slowly starting to predict see
    we are slowly starting to predict

    the digits as 8 and 1. the digits as 8 and 1. the digits as 8 and 1.

    um I I could have continued to 50,000 um I I could have continued to 50,000 um
    I I could have continued to 50,000

    where it can give more clarity to these where it can give more clarity to these
    where it can give more clarity to these

    images but you can see we are slowly images but you can see we are slowly images
    but you can see we are slowly

    starting to learn how to generate images starting to learn how to generate images
    starting to learn how to generate images

    using a very simple approach which can'
  concept_slugs:
  - langevin-dynamics
  - probability-flow-ode
  - sde-formulation
- idx: 51
  start_sec: 2939.99
  end_sec: 2990.48
  text: 'using a very simple approach which can using a very simple approach which
    can

    be implemented in Google Collab and uh be implemented in Google Collab and uh
    be implemented in Google Collab and uh

    this is a playground for all of you just this is a playground for all of you just
    this is a playground for all of you just

    feel free to experiment dive deeper into feel free to experiment dive deeper into
    feel free to experiment dive deeper into

    the individual cells get your hands the individual cells get your hands the individual
    cells get your hands

    dirty with the diffusion process because dirty with the diffusion process because
    dirty with the diffusion process because

    it is an incredibly useful skill to it is an incredibly useful skill to it is
    an incredibly useful skill to

    master diffusion master diffusion master diffusion

    And again as I said in the middle of the And again as I said in the middle of
    the And again as I said in the middle of the

    lecture there is a certain fascination lecture there is a certain fascination
    lecture there is a certain fascination

    towards the diffusion process. I think towards the diffusion process. I think
    towards the diffusion process. I think

    it stems from the fascination towards it stems from the fascination towards it
    stems from the fascination towards

    reversal of time itself which is what reversal of time itself which is what reversal
    of time itself which is what

    diffusion processes achieve. There are diffusion processes achieve. There are
    diffusion processes achieve. There are

    applications in uh video generation applications in uh video generation applications
    in uh video generation

    image generation even robotics there are image generation even robotics there
    are image generation even robotics there are

    some amazing policies which generate some amazing policies which generate some
    amazing policies which generate

    actions using diffusion. actions using diffusion. actions using diffusion.

    I will link the main paper which I will link the main paper which I will link
    the main paper which

    describes the SD frame uh framework in describes the SD frame uh framework in
    describes the SD frame uh framework in

    the description. Please go through it. the description. Please go through it.
    the description. Please go through it.

    It''s a very nicely written paper and It''s a very nicely written paper and'
  concept_slugs:
  - langevin-dynamics
  - probability-flow-ode
  - sde-formulation
- idx: 52
  start_sec: 2990.48
  end_sec: 3004.92
  text: 'It''s a very nicely written paper and

    after this introduction you should be after this introduction you should be after
    this introduction you should be

    able to understand it. Thank you very able to understand it. Thank you very able
    to understand it. Thank you very

    much everyone and I I hope you enjoyed much everyone and I I hope you enjoyed
    much everyone and I I hope you enjoyed

    this new approach which I taught this this new approach which I taught this this
    new approach which I taught this

    lecture with and uh I will see you in lecture with and uh I will see you in lecture
    with and uh I will see you in

    the next lecture.'
  concept_slugs:
  - langevin-dynamics
  - probability-flow-ode
  - sde-formulation
---
# Lecture 8 - Diffusion Models: A Physical Intuition (SDE Framework) | Principles of Diffusion Models

See the structured chunks above.
