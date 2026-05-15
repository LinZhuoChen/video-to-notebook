---
course_slug: diffusion-lm-vizuara
idx: 5
title: 'Lecture 4: How Diffusion Models Work for Image Generation'
video_url: https://www.youtube.com/watch?v=rngYBa46AXY
duration_sec: null
chunks:
- idx: 0
  start_sec: 2.149
  end_sec: 50.31
  text: 'Now that we have seen the probabilistic Now that we have seen the probabilistic

    length of generative AI, let us actually length of generative AI, let us actually
    length of generative AI, let us actually

    see that how do diffusion models achieve see that how do diffusion models achieve
    see that how do diffusion models achieve

    their true purpose. And their true their true purpose. And their true their true
    purpose. And their true

    purpose is to find the underlying purpose is to find the underlying purpose is
    to find the underlying

    probability distribution. For now, we probability distribution. For now, we probability
    distribution. For now, we

    are sticking to images, right? The way are sticking to images, right? The way
    are sticking to images, right? The way

    diffusion models find this purpose is diffusion models find this purpose is diffusion
    models find this purpose is

    through a process of dnoising. through a process of dnoising. through a process
    of dnoising.

    So what it means is that let me show you So what it means is that let me show
    you So what it means is that let me show you

    with an example. with an example. with an example.

    Let''s say that we want to generate Let''s say that we want to generate Let''s
    say that we want to generate

    images of a panda or a bear, right? And images of a panda or a bear, right? And
    images of a panda or a bear, right? And

    these images live somewhere over here. these images live somewhere over here.
    these images live somewhere over here.

    That''s the probability distribution That''s the probability distribution That''s
    the probability distribution

    where you have to sample images which where you have to sample images which where
    you have to sample images which

    look like a bear or a panda. The way look like a bear or a panda. The way look
    like a bear or a panda. The way

    diffusion models work is that they start diffusion models work is that they start
    diffusion models work is that they start

    out with noise. So they may start out at out with noise. So they may start out
    at out with noise. So they may start out at

    some random location in the probability some random location in the probability
    some random location in the probability

    distribution space. Let''s say this is'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 1
  start_sec: 50.31
  end_sec: 99.109
  text: 'distribution space. Let''s say this is distribution space. Let''s say this
    is

    noise and noise can live anywhere, noise and noise can live anywhere, noise and
    noise can live anywhere,

    right? So we start out from a random right? So we start out from a random right?
    So we start out from a random

    location and then the whole goal is to location and then the whole goal is to
    location and then the whole goal is to

    traverse a path. The whole goal is to traverse a path. The whole goal is to traverse
    a path. The whole goal is to

    traverse a path which slowly leads me to traverse a path which slowly leads me
    to traverse a path which slowly leads me to

    this actual probability distribution. this actual probability distribution. this
    actual probability distribution.

    Right? That is the process of dnoising. Right? That is the process of dnoising.
    Right? That is the process of dnoising.

    What dinoising essentially means is that What dinoising essentially means is that
    What dinoising essentially means is that

    you start from a random location which you start from a random location which
    you start from a random location which

    is noise and that may live anywhere in is noise and that may live anywhere in
    is noise and that may live anywhere in

    the probability space and you slowly the probability space and you slowly the
    probability space and you slowly

    move towards locations which start move towards locations which start move towards
    locations which start

    looking like a panda or a bear or looking like a panda or a bear or looking like
    a panda or a bear or

    whatever this animal is right that''s the whatever this animal is right that''s
    the whatever this animal is right that''s the

    process of dnoising this is the path process of dnoising this is the path process
    of dnoising this is the path

    which is followed so you might be which is followed so you might be which is followed
    so you might be

    thinking that okay this seems backward thinking that okay this seems backward
    thinking that okay this seems backward

    right why do I have to start from noise right why do I have to start from noise
    right why do I have to start from noise

    and what good will this do to me if I'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 2
  start_sec: 99.109
  end_sec: 149.91
  text: 'and what good will this do to me if I and what good will this do to me if
    I

    start from noise. Well, look at this start from noise. Well, look at this start
    from noise. Well, look at this

    video, right? video, right? video, right?

    Look at this video again for reference. Look at this video again for reference.
    Look at this video again for reference.

    If you start from noise, If you start from noise, If you start from noise,

    if you start from noise, if you start from noise, if you start from noise,

    you can essentially recover the true you can essentially recover the true you
    can essentially recover the true

    underlying die if you if something is underlying die if you if something is underlying
    die if you if something is

    followed. Now, what is that something? followed. Now, what is that something?
    followed. Now, what is that something?

    How can I recover the actual image from How can I recover the actual image from
    How can I recover the actual image from

    my noise? Well, the idea is to let''s say my noise? Well, the idea is to let''s
    say my noise? Well, the idea is to let''s say

    start with an image. The idea is always start with an image. The idea is always
    start with an image. The idea is always

    in the training, right? This looks like in the training, right? This looks like
    in the training, right? This looks like

    rocket science, but it''s not. If you rocket science, but it''s not. If you rocket
    science, but it''s not. If you

    look at what training a diffusion model look at what training a diffusion model
    look at what training a diffusion model

    actually means in training, what we do actually means in training, what we do
    actually means in training, what we do

    is that we take a bunch of images which is that we take a bunch of images which
    is that we take a bunch of images which

    look like this bear or panda. Let''s say look like this bear or panda. Let''s
    say look like this bear or panda. Let''s say

    we take bunch of images which look like we take bunch of images which look like
    we take bunch of images which look like

    this and we sequentially go on adding'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 3
  start_sec: 149.91
  end_sec: 216.56
  text: 'this and we sequentially go on adding this and we sequentially go on adding

    noise. We sequentially go on adding noise. We sequentially go on adding noise.
    We sequentially go on adding

    noise until it becomes fully noisy. This noise until it becomes fully noisy. This
    noise until it becomes fully noisy. This

    is exactly similar to the video which we is exactly similar to the video which
    we is exactly similar to the video which we

    saw. saw. saw.

    If you recall this video which we saw, If you recall this video which we saw,
    If you recall this video which we saw,

    what is done here is that we what is done here is that we what is done here is
    that we

    sequentially very slowly we stir this sequentially very slowly we stir this sequentially
    very slowly we stir this

    fluid and add noise. See this is exactly fluid and add noise. See this is exactly
    fluid and add noise. See this is exactly

    what we do in training the diffusion what we do in training the diffusion what
    we do in training the diffusion

    model. In training of the diffusion model. In training of the diffusion model.
    In training of the diffusion

    model, we sequentially add noise. model, we sequentially add noise. model, we
    sequentially add noise.

    Uh let me scroll up. We sequentially add Uh let me scroll up. We sequentially
    add Uh let me scroll up. We sequentially add

    noise. Where had I written this? noise. Where had I written this? noise. Where
    had I written this?

    Um where was our where was our

    uh yeah in training the diffusion uh yeah in training the diffusion uh yeah in
    training the diffusion

    process we sequentially go on adding process we sequentially go on adding process
    we sequentially go on adding

    noise right so we start from the image noise right so we start from the image
    noise right so we start from the image

    and we go on adding noise and then what and we go on adding noise and then what
    and we go on adding noise and then what

    we do is that we do is that we do is that

    at several intermediate steps here let''s at several intermediate steps here let''s
    at several intermediate steps here let''s

    say this is my noisy image I will train a machine learning model'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 4
  start_sec: 216.56
  end_sec: 263.199
  text: 'I will train a machine learning model

    to predict how much noise was added to predict how much noise was added to predict
    how much noise was added

    to predict how much noise was added. Why to predict how much noise was added.
    Why to predict how much noise was added. Why

    am I doing this? Because if you take a am I doing this? Because if you take a
    am I doing this? Because if you take a

    noisy image and you subtract the noise noisy image and you subtract the noise
    noisy image and you subtract the noise

    from it, you''ll get the clean image. from it, you''ll get the clean image. from
    it, you''ll get the clean image.

    That''s the whole idea at several stages That''s the whole idea at several stages
    That''s the whole idea at several stages

    of this noising process. So the noising of this noising process. So the noising
    of this noising process. So the noising

    process actually looks something like process actually looks something like process
    actually looks something like

    this. this. this.

    uh if you think about it in the reverse uh if you think about it in the reverse
    uh if you think about it in the reverse

    way at at several stages of this noising way at at several stages of this noising
    way at at several stages of this noising

    process. So t= 1 t=2 t= 3 t= 4 uh we process. So t= 1 t=2 t= 3 t= 4 uh we process.
    So t= 1 t=2 t= 3 t= 4 uh we

    take this image out and we predict how take this image out and we predict how
    take this image out and we predict how

    much noise has been added to this image. much noise has been added to this image.
    much noise has been added to this image.

    So think about it this way right we keep So think about it this way right we keep
    So think about it this way right we keep

    on adding noise but we predict at each on adding noise but we predict at each
    on adding noise but we predict at each

    step we have a model which predicts how step we have a model which predicts how'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 5
  start_sec: 263.199
  end_sec: 313.029
  text: 'step we have a model which predicts how

    much noise has been added to each step. much noise has been added to each step.
    much noise has been added to each step.

    So we have to train an ML model which So we have to train an ML model which So
    we have to train an ML model which

    takes a noisy image as input and tries takes a noisy image as input and tries
    takes a noisy image as input and tries

    to predict the exact noise which was to predict the exact noise which was to predict
    the exact noise which was

    added to the original image to get to added to the original image to get to added
    to the original image to get to

    that step. that step. that step.

    So in our images if you see now what is So in our images if you see now what is
    So in our images if you see now what is

    done is that in noising we actually go done is that in noising we actually go
    done is that in noising we actually go

    in the reverse way. In noising we in the reverse way. In noising we in the reverse
    way. In noising we

    actually go in this way. This is the actually go in this way. This is the actually
    go in this way. This is the

    noising process. And then we sample noising process. And then we sample noising
    process. And then we sample

    noisy images at several locations and noisy images at several locations and noisy
    images at several locations and

    then we predict the noise at each noising trajectory. If you have at each noising
    trajectory. If you have

    a model which predicts the noise that a model which predicts the noise that a
    model which predicts the noise that

    helps me in dnoising also because in helps me in dnoising also because in helps
    me in dnoising also because in

    dnoising I just need to subtract that dnoising I just need to subtract that dnoising
    I just need to subtract that

    noise right to get to the clean image. noise right to get to the clean image.
    noise right to get to the clean image.

    So let''s say if you have if you want to'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 6
  start_sec: 313.029
  end_sec: 361.35
  text: 'So let''s say if you have if you want to So let''s say if you have if you
    want to

    predict images which look like this predict images which look like this predict
    images which look like this

    panda bear panda bear panda bear

    what''s done in diffusion is that you what''s done in diffusion is that you what''s
    done in diffusion is that you

    take a huge amount of training data you take a huge amount of training data you
    take a huge amount of training data you

    add noise to it generate noisy images add noise to it generate noisy images add
    noise to it generate noisy images

    right right right

    you sample randomly from these noisy you sample randomly from these noisy you
    sample randomly from these noisy

    images and predict train an ML model to images and predict train an ML model to
    images and predict train an ML model to

    predict how much noise has been added predict how much noise has been added predict
    how much noise has been added

    that helps you in the dnoising process that helps you in the dnoising process
    that helps you in the dnoising process

    also because if you know how much noise also because if you know how much noise
    also because if you know how much noise

    is added at each step you can dinoise it is added at each step you can dinoise
    it is added at each step you can dinoise it

    effectively. effectively. effectively.

    This only works if if a small amount of This only works if if a small amount of
    This only works if if a small amount of

    noise has been added at every step. And noise has been added at every step. And
    noise has been added at every step. And

    that''s again exactly linked to this that''s again exactly linked to this that''s
    again exactly linked to this

    video because if you know about fluids, video because if you know about fluids,
    video because if you know about fluids,

    you will know that this process is only you will know that this process is only
    you will know that this process is only

    reversible if we stir this fluid very reversible if we stir this fluid very reversible
    if we stir this fluid very

    slowly. If you do this experiment at'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 7
  start_sec: 361.35
  end_sec: 437.749
  text: 'slowly. If you do this experiment at slowly. If you do this experiment at

    home and if you stir this fluid very home and if you stir this fluid very home
    and if you stir this fluid very

    fast and if you reverse it, it will not fast and if you reverse it, it will not
    fast and if you reverse it, it will not

    come back to its original position. So come back to its original position. So
    come back to its original position. So

    see how slowly we stir this. Similarly, see how slowly we stir this. Similarly,
    see how slowly we stir this. Similarly,

    small amount of noise needs to be added small amount of noise needs to be added
    small amount of noise needs to be added

    at each step if we want to recover the at each step if we want to recover the
    at each step if we want to recover the

    original image. original image. original image.

    So to give you a overview of the So to give you a overview of the So to give you
    a overview of the

    diffusion process, we have a forward diffusion process, we have a forward diffusion
    process, we have a forward

    diffusion which I called as noising and diffusion which I called as noising and
    diffusion which I called as noising and

    we have a reverse diffusion. The we have a reverse diffusion. The we have a reverse
    diffusion. The

    prediction of the image or generation of prediction of the image or generation
    of prediction of the image or generation of

    new images actually takes place in the new images actually takes place in the
    new images actually takes place in the

    dnoising. So another thing which I might dnoising. So another thing which I might
    dnoising. So another thing which I might

    write here is that generation. write here is that generation. write here is that
    generation.

    Let me increase the font. Let me increase the font. Let me increase the font.

    Generation of new images. and uh prediction of noise and uh prediction of noise

    prediction of noise prediction of noise prediction of noise

    happens happens during noising. happens during noising.

    So this is also called as reverse So this is also called as reverse So this is
    also called as reverse

    diffusion dnoising and noising is also'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 8
  start_sec: 437.749
  end_sec: 479.99
  text: 'diffusion dnoising and noising is also diffusion dnoising and noising is
    also

    called as forward diffusion. So this called as forward diffusion. So this called
    as forward diffusion. So this

    same intuition which I explained can be same intuition which I explained can be
    same intuition which I explained can be

    looked at in a mathematical perspective looked at in a mathematical perspective
    looked at in a mathematical perspective

    where you start with a clean image X where you start with a clean image X where
    you start with a clean image X

    not. You go on adding noise to it in not. You go on adding noise to it in not.
    You go on adding noise to it in

    something which is called as a noising something which is called as a noising
    something which is called as a noising

    schedule and you get a noisy image and schedule and you get a noisy image and
    schedule and you get a noisy image and

    you have to train an ML model to predict you have to train an ML model to predict
    you have to train an ML model to predict

    the noise at any of these time step. the noise at any of these time step. the
    noise at any of these time step.

    Right? Right? Right?

    Uh so this is how the noise prediction Uh so this is how the noise prediction
    Uh so this is how the noise prediction

    model looks like. You randomly take a model looks like. You randomly take a model
    looks like. You randomly take a

    noisy image and then you train an ML noisy image and then you train an ML noisy
    image and then you train an ML

    model to predict this noise and then if model to predict this noise and then if
    model to predict this noise and then if

    you subtract this noise from this random you subtract this noise from this random
    you subtract this noise from this random

    image then you might get the original image then you might get the original image
    then you might get the original

    image. That''s why reverse diffusion image. That''s why reverse diffusion image.
    That''s why reverse diffusion

    actually works in a very layman way. actually works in a very layman way. actually
    works in a very layman way.

    So again to summarize the way diffusion'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 9
  start_sec: 479.99
  end_sec: 533.19
  text: 'So again to summarize the way diffusion So again to summarize the way diffusion

    for images works is that we take a for images works is that we take a for images
    works is that we take a

    random image from our data set and noise random image from our data set and noise
    random image from our data set and noise

    it. Okay, we feed this noised image into it. Okay, we feed this noised image into
    it. Okay, we feed this noised image into

    an ML model and predict the noise in the an ML model and predict the noise in
    the an ML model and predict the noise in the

    image. Right? This noise prediction image. Right? This noise prediction image.
    Right? This noise prediction

    model eventually sees many different model eventually sees many different model
    eventually sees many different

    combinations of dnoising because it sees combinations of dnoising because it sees
    combinations of dnoising because it sees

    many different combinations of noisy many different combinations of noisy many
    different combinations of noisy

    images and how to predict noise. So images and how to predict noise. So images
    and how to predict noise. So

    through this process, the model through this process, the model through this process,
    the model

    implicitly learns the reverse implicitly learns the reverse implicitly learns
    the reverse

    distribution over the entire data set. distribution over the entire data set.
    distribution over the entire data set.

    There is a mathematical theory towards There is a mathematical theory towards
    There is a mathematical theory towards

    this and a mathematical formulation this and a mathematical formulation this and
    a mathematical formulation

    which proves that if the added noise is which proves that if the added noise is
    which proves that if the added noise is

    less, the model can learn the reverse less, the model can learn the reverse less,
    the model can learn the reverse

    diffusion process to a very good extent. diffusion process to a very good extent.
    diffusion process to a very good extent.

    Uh Uh Uh

    so put another way given an image noise so put another way given an image noise
    so put another way given an image noise

    to any given level the model can predict to any given level the model can predict
    to any given level the model can predict

    how to reduce the noise.'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 10
  start_sec: 533.19
  end_sec: 585.279
  text: 'how to reduce the noise. how to reduce the noise.

    By doing this repeatedly the model can By doing this repeatedly the model can
    By doing this repeatedly the model can

    transform any noise to a sample that transform any noise to a sample that transform
    any noise to a sample that

    lies in a high probability region. Look lies in a high probability region. Look
    lies in a high probability region. Look

    at this sentence. By doing this at this sentence. By doing this at this sentence.
    By doing this

    repeatedly the model can transform any repeatedly the model can transform any
    repeatedly the model can transform any

    noise to a sample that lies in a high noise to a sample that lies in a high noise
    to a sample that lies in a high

    probability region. What this means is probability region. What this means is
    probability region. What this means is

    that the model can that the model can that the model can

    uh take any noise. Yeah, the model can uh take any noise. Yeah, the model can
    uh take any noise. Yeah, the model can

    take any noise and then go to a region take any noise and then go to a region
    take any noise and then go to a region

    of high probability. That''s what happens of high probability. That''s what happens
    of high probability. That''s what happens

    in dnoising if we train the ML model in dnoising if we train the ML model in dnoising
    if we train the ML model

    correctly. So uh So uh

    yeah, this is what I already explained yeah, this is what I already explained
    yeah, this is what I already explained

    to all of you. We start with noise and to all of you. We start with noise and
    to all of you. We start with noise and

    then we do the dnoising process and then then we do the dnoising process and then
    then we do the dnoising process and then

    eventually reach an area of a higher eventually reach an area of a higher eventually
    reach an area of a higher

    probability distribution where the image probability distribution where the image
    probability distribution where the image

    actually lies. actually lies. actually lies.

    That''s the beauty of diffusion process. That''s the beauty of diffusion process.'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 11
  start_sec: 585.279
  end_sec: 641.75
  text: 'That''s the beauty of diffusion process.

    So there are certain key characteristics So there are certain key characteristics
    So there are certain key characteristics

    of diffusion. So there are key characteristics of this So there are key characteristics
    of this

    diffusion process. What are these diffusion process. What are these diffusion
    process. What are these

    characteristics? Well, first we need characteristics? Well, first we need characteristics?
    Well, first we need

    need a noising process. need a noising process. need a noising process.

    We need a noising process. We need a noising process. We need a noising process.

    Second, we need to predict the noise. Second, we need to predict the noise. Second,
    we need to predict the noise.

    What do I mean by noising process? We What do I mean by noising process? We What
    do I mean by noising process? We

    need to decide how a noise is added. So need to decide how a noise is added. So
    need to decide how a noise is added. So

    for example, we can have a gshian for example, we can have a gshian for example,
    we can have a gshian

    process of adding noise. There are process of adding noise. There are process
    of adding noise. There are

    several different processes where you several different processes where you several
    different processes where you

    can add noise at different time steps to can add noise at different time steps
    to can add noise at different time steps to

    the given image. So basically this part the given image. So basically this part
    the given image. So basically this part

    this part of how you are going to this part of how you are going to this part
    of how you are going to

    sequentially add noise to an image is sequentially add noise to an image is sequentially
    add noise to an image is

    called as a noising schedule which I''m called as a noising schedule which I''m
    called as a noising schedule which I''m

    also calling as noising process. The also calling as noising process. The also
    calling as noising process. The

    second is predicting the noise. So here second is predicting the noise. So here
    second is predicting the noise. So here

    we used an ML model right we used an ML model right we used an ML model right

    here we use a machine learning model to'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 12
  start_sec: 641.75
  end_sec: 688.72
  text: 'here we use a machine learning model to here we use a machine learning model
    to

    predict this noise. Um and to make it predict this noise. Um and to make it predict
    this noise. Um and to make it

    more simpler, the machine learning model more simpler, the machine learning model
    more simpler, the machine learning model

    is actually a unit which you don''t need is actually a unit which you don''t need
    is actually a unit which you don''t need

    to worry about right now. But we use to worry about right now. But we use to worry
    about right now. But we use

    some machine learning model to predict some machine learning model to predict
    some machine learning model to predict

    the noise. And the third thing is we the noise. And the third thing is we the
    noise. And the third thing is we

    need to use a dnoising process. We need to use a dnoising process. We need to
    use a dnoising process.

    Why do we need to use a dinoising Why do we need to use a dinoising Why do we
    need to use a dinoising

    process? Well, we need to use a dnoising process? Well, we need to use a dnoising
    process? Well, we need to use a dnoising

    process for generation process for generation process for generation

    for generation of new images because for generation of new images because for
    generation of new images because

    during dnoising is where we start from during dnoising is where we start from
    during dnoising is where we start from

    noise and eventually move towards area noise and eventually move towards area
    noise and eventually move towards area

    of high probability distribution where of high probability distribution where
    of high probability distribution where

    images might lie images of what we want images might lie images of what we want
    images might lie images of what we want

    to generate. to generate. to generate.

    And how do we do this? Well, because in And how do we do this? Well, because in
    And how do we do this? Well, because in

    the noising process, we train using the noising process, we train using the noising
    process, we train using

    those same images which we want to those same images which we want to those same
    images which we want to

    generate. generate.'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 13
  start_sec: 688.72
  end_sec: 757.519
  text: 'generate.

    So these three are the key So these three are the key So these three are the key

    characteristics of a diffusion model. characteristics of a diffusion model. characteristics
    of a diffusion model.

    These are the key characteristics of a These are the key characteristics of a
    These are the key characteristics of a

    diffusion model which is used for diffusion model which is used for diffusion
    model which is used for

    generation. Now take a very closer look at these three take a very closer look
    at these three

    characteristics. Right? characteristics. Right? characteristics. Right?

    Diffusion for image generation evolved Diffusion for image generation evolved
    Diffusion for image generation evolved

    from these three characteristics. images from these three characteristics. images
    from these three characteristics. images

    were generated using these three were generated using these three were generated
    using these three

    characteristics and we have we had characteristics and we have we had characteristics
    and we have we had

    amazing pipelines such as stable amazing pipelines such as stable amazing pipelines
    such as stable

    diffusion diffusion diffusion

    uh uh uh

    which generated images you can see the which generated images you can see the
    which generated images you can see the

    images generated by stable diffusion images generated by stable diffusion images
    generated by stable diffusion

    right they are pretty cool and all of right they are pretty cool and all of right
    they are pretty cool and all of

    them were generated through this them were generated through this them were generated
    through this

    underlying phenomena underlying phenomena underlying phenomena

    so let''s see examples so let''s see examples so let''s see examples

    yeah so all of them were generated yeah so all of them were generated yeah so
    all of them were generated

    through this underlying phenomena of through this underlying phenomena of through
    this underlying phenomena of

    these these three steps, right? A these these three steps, right? A these these
    three steps, right? A

    noising schedule, a machine learning noising schedule, a machine learning noising
    schedule, a machine learning

    model, and then a dnoising for model, and then a dnoising for model, and then
    a dnoising for

    generation. generation. generation.

    Things were pretty cool. Things were Things were pretty cool. Things were Things
    were pretty cool. Things were

    moving in a very uh straightforward moving in a very uh straightforward'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 14
  start_sec: 757.519
  end_sec: 854.629
  text: 'moving in a very uh straightforward

    manner for image generation and people manner for image generation and people
    manner for image generation and people

    were happy. There were companies which were happy. There were companies which
    were happy. There were companies which

    came out which made these awesome, came out which made these awesome, came out
    which made these awesome,

    incredible looking images using incredible looking images using incredible looking
    images using

    diffusion techniques. diffusion techniques. diffusion techniques.

    Now comes the question which Now comes the question which Now comes the question
    which

    every good researcher should ask. every good researcher should ask. every good
    researcher should ask.

    Uh so that is the purpose of this course Uh so that is the purpose of this course
    Uh so that is the purpose of this course

    right? I don''t want to directly explain right? I don''t want to directly explain
    right? I don''t want to directly explain

    the concept to you. I want to take you the concept to you. I want to take you
    the concept to you. I want to take you

    through the journey. So if you look at through the journey. So if you look at
    through the journey. So if you look at

    these three characteristics, a natural these three characteristics, a natural
    these three characteristics, a natural

    question which might come to our mind is question which might come to our mind
    is question which might come to our mind is

    why can''t why can''t why can''t

    why should why should why should

    these these these

    three characteristics So diffusion model for generation has So diffusion model
    for generation has

    these characteristics. So when we look these characteristics. So when we look
    these characteristics. So when we look

    at generation, why are we only at generation, why are we only at generation, why
    are we only

    considering images? Why not text? What considering images? Why not text? What
    considering images? Why not text? What

    prevents these three characteristics prevents these three characteristics prevents
    these three characteristics

    from being applied to text also? from being applied to text also? from being applied
    to text also?

    Then started a whole new field of Then started a whole new field of Then started
    a whole new field of

    diffusion models for text generation. diffusion models for text generation. diffusion
    models for text generation.

    And we are just going to start looking'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 15
  start_sec: 854.629
  end_sec: 879.12
  text: 'And we are just going to start looking And we are just going to start looking

    at this field right now. I hope the at this field right now. I hope the at this
    field right now. I hope the

    motivation for getting into diffusion motivation for getting into diffusion motivation
    for getting into diffusion

    models for text generation is clear for models for text generation is clear for
    models for text generation is clear for

    you. Why should diffusion models only be you. Why should diffusion models only
    be you. Why should diffusion models only be

    restricted for image generation? If restricted for image generation? If restricted
    for image generation? If

    these three characteristics are these three characteristics are these three characteristics
    are

    satisfied for text, why can''t I build a satisfied for text, why can''t I build
    a satisfied for text, why can''t I build a

    diffusion model for text generation? diffusion model for text generation? diffusion
    model for text generation?

    That''s where the concept of language That''s where the concept of language That''s
    where the concept of language

    models for diffusion came into the models for diffusion came into the models for
    diffusion came into the

    picture. Let''s start looking at them picture. Let''s start looking at them picture.
    Let''s start looking at them

    now.'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
---
# Lecture 4: How Diffusion Models Work for Image Generation

See the structured chunks above.
