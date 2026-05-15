---
course_slug: diffusion-principles-vizuara
idx: 7
title: Lecture 4 - Diffusion Models Practical | DDPM | Principles of Diffusion Models
video_url: https://www.youtube.com/watch?v=6to_EG3SJgs
duration_sec: null
chunks:
- idx: 0
  start_sec: 3.27
  end_sec: 70.56
  text: 'Hello everyone. Hello everyone.

    In this lecture, we will continue our In this lecture, we will continue our In
    this lecture, we will continue our

    discussion on dnoising diffusion discussion on dnoising diffusion discussion on
    dnoising diffusion

    probabilistic models or DDPMS. The last lecture focused on the theory The last
    lecture focused on the theory

    of DDPMS of DDPMS of DDPMS

    where we looked at how exactly are where we looked at how exactly are where we
    looked at how exactly are

    diffusion models trained. diffusion models trained. diffusion models trained.

    The theory was quite interesting The theory was quite interesting The theory was
    quite interesting

    and uh we had a forward diffusion and uh we had a forward diffusion and uh we
    had a forward diffusion

    process and then we had a reverse process and then we had a reverse process and
    then we had a reverse

    process which our neural network had to process which our neural network had to
    process which our neural network had to

    learn. My experience with diffusion models has My experience with diffusion models
    has

    been that the theory appears very been that the theory appears very been that
    the theory appears very

    interesting but you cannot truly interesting but you cannot truly interesting
    but you cannot truly

    understand the underlying concepts understand the underlying concepts understand
    the underlying concepts

    unless you supplement it with a unless you supplement it with a unless you supplement
    it with a

    practical example or multiple practical practical example or multiple practical
    practical example or multiple practical

    examples. examples. examples.

    [snorts] Through the practical examples [snorts] Through the practical examples
    [snorts] Through the practical examples

    we will get a firm understanding of the we will get a firm understanding of the
    we will get a firm understanding of the

    theory and it also gives us a gives us a theory and it also gives us a gives us
    a theory and it also gives us a gives us a

    chance to nicely revise the theory. chance to nicely revise the theory. chance
    to nicely revise the theory.

    So in this lecture we''ll be following an So in this lecture we''ll be following
    an So in this lecture we''ll be following an

    interesting approach. interesting approach. interesting approach.

    We will take an example a practical We will take an example a practical'
  concept_slugs:
  - ddpm
  - epsilon-prediction
  - simple-loss-objective
- idx: 1
  start_sec: 70.56
  end_sec: 127.92
  text: 'We will take an example a practical

    example and we will exactly see how the example and we will exactly see how the
    example and we will exactly see how the

    DDPM method is applied to that practical DDPM method is applied to that practical
    DDPM method is applied to that practical

    example to solve the project example to solve the project example to solve the
    project

    and in this process we will revise the and in this process we will revise the
    and in this process we will revise the

    theory that we have covered in the last theory that we have covered in the last
    theory that we have covered in the last

    lecture. It will also help us to get a lecture. It will also help us to get a
    lecture. It will also help us to get a

    intuitive understanding of why the intuitive understanding of why the intuitive
    understanding of why the

    theory works and our internal confidence theory works and our internal confidence
    theory works and our internal confidence

    will also increase in the process. will also increase in the process. will also
    increase in the process.

    [snorts] [snorts] [snorts]

    So let''s get started. [snorts] Before we move ahead, I want to [snorts] Before
    we move ahead, I want to

    make a quick analogy. The diffusion make a quick analogy. The diffusion make a
    quick analogy. The diffusion

    process that we are studying in u these process that we are studying in u these
    process that we are studying in u these

    couple of lectures is is very similar to couple of lectures is is very similar
    to couple of lectures is is very similar to

    how particles diffuse in air. [snorts] how particles diffuse in air. [snorts]
    how particles diffuse in air. [snorts]

    In fact, the theory of diffusion is well In fact, the theory of diffusion is well
    In fact, the theory of diffusion is well

    documented in the field of physics. Uh documented in the field of physics. Uh
    documented in the field of physics. Uh

    imagine let''s say you spray a perfume in imagine let''s say you spray a perfume
    in imagine let''s say you spray a perfume in

    one corner of the room and then the one corner of the room and then the'
  concept_slugs:
  - ddpm
  - epsilon-prediction
  - simple-loss-objective
- idx: 2
  start_sec: 127.92
  end_sec: 195.182
  text: 'one corner of the room and then the

    particles slowly diffuse and the smell particles slowly diffuse and the smell
    particles slowly diffuse and the smell

    percolates in the room. percolates in the room. percolates in the room.

    >> [snorts] >> [snorts] >> [snorts]

    >> This is because the particles are >> This is because the particles are >> This
    is because the particles are

    transferring from one corner of the room transferring from one corner of the room
    transferring from one corner of the room

    to another. to another. to another.

    And another example we can see is that And another example we can see is that
    And another example we can see is that

    of sugar dissolving and spreading in of sugar dissolving and spreading in of sugar
    dissolving and spreading in

    water. water. water.

    Both of these are examples of diffusion Both of these are examples of diffusion
    Both of these are examples of diffusion

    processes. And what is common in both processes. And what is common in both processes.
    And what is common in both

    these examples is the structure slowly these examples is the structure slowly
    these examples is the structure slowly

    disappears and things become uniform and disappears and things become uniform
    and disappears and things become uniform and

    very noisy over time. So what we do in uh DDPM is that So what we do in uh DDPM
    is that

    remember in variation autoenccoder we remember in variation autoenccoder we remember
    in variation autoenccoder we

    had an encoder and a and and a decoder. had an encoder and a and and a decoder.
    had an encoder and a and and a decoder.

    In this case, our structure is the same In this case, our structure is the same
    In this case, our structure is the same

    as that of a VA, as that of a VA, as that of a VA,

    but instead of a encoder being a but instead of a encoder being a but instead
    of a encoder being a

    learnable encoder, we have a fixed learnable encoder, we have a fixed learnable
    encoder, we have a fixed

    encoder. And the encoder takes the input image or And the encoder takes the input
    image or

    the input data samples and converts the the input data samples and converts the
    the input data samples and converts the

    input image into noise.'
  concept_slugs:
  - ddpm
  - epsilon-prediction
  - simple-loss-objective
- idx: 3
  start_sec: 195.182
  end_sec: 258.4
  text: 'input image into noise. input image into noise.

    >> [snorts] >> [snorts]

    >> This is not done through a single >> This is not done through a single >> This
    is not done through a single

    transition but it is done through a transition but it is done through a transition
    but it is done through a

    series of transitions. And then there is a reverse transition And then there is
    a reverse transition

    process where process where process where

    you take the noise as an input and you you take the noise as an input and you
    you take the noise as an input and you

    construct the image back from the noise. construct the image back from the noise.
    construct the image back from the noise.

    This is called as the reverse transition This is called as the reverse transition
    This is called as the reverse transition

    process. Now how to construct the image back from Now how to construct the image
    back from

    the noise is where the heart of the DDPM the noise is where the heart of the DDPM
    the noise is where the heart of the DDPM

    theory lies in. And uh it turns out that theory lies in. And uh it turns out that
    theory lies in. And uh it turns out that

    the final the final the final

    prediction or the final uh conclusion is prediction or the final uh conclusion
    is prediction or the final uh conclusion is

    that if if you want to generate images which if if you want to generate images
    which

    are are sampled from the true are are sampled from the true are are sampled from
    the true

    distribution distribution distribution

    then you need to predict a then you need to predict a then you need to predict
    a

    [clears throat] noise epsilon hat which [clears throat] noise epsilon hat which
    [clears throat] noise epsilon hat which

    is as close as possible to the real is as close as possible to the real is as
    close as possible to the real

    noise which is added in the forward noise which is added in the forward noise
    which is added in the forward

    process. This this sounds very intuitive to begin This this sounds very intuitive
    to begin

    with, right? But uh when you actually with, right? But uh when you actually'
  concept_slugs:
  - ddpm
  - epsilon-prediction
  - simple-loss-objective
- idx: 4
  start_sec: 258.4
  end_sec: 335.199
  text: 'with, right? But uh when you actually

    start doing the mathematics, this is not start doing the mathematics, this is
    not start doing the mathematics, this is not

    very apparent at the beginning very apparent at the beginning very apparent at
    the beginning

    and we only come towards it in in the and we only come towards it in in the and
    we only come towards it in in the

    very end. Now exactly the this noise is added at Now exactly the this noise is
    added at

    what time step? How to compare these two what time step? How to compare these
    two what time step? How to compare these two

    different noise levels? It is hard to different noise levels? It is hard to different
    noise levels? It is hard to

    explain all this in theory. That''s why I explain all this in theory. That''s
    why I explain all this in theory. That''s why I

    thought of having this separate lecture thought of having this separate lecture
    thought of having this separate lecture

    so that we take a nice practical so that we take a nice practical so that we take
    a nice practical

    example. Okay. So the example that we are going Okay. So the example that we are
    going

    to look at is we are going to train our to look at is we are going to train our
    to look at is we are going to train our

    first diffusion model first diffusion model first diffusion model

    to generate images of butterflies. So So

    let''s start understanding the different let''s start understanding the different
    let''s start understanding the different

    steps gradually. steps gradually. steps gradually.

    [snorts and sighs] [snorts and sighs] [snorts and sighs]

    Step number one is the setup where we Step number one is the setup where we Step
    number one is the setup where we

    install all the key files. And uh here install all the key files. And uh here
    install all the key files. And uh here

    you can see I have installed a library you can see I have installed a library
    you can see I have installed a library

    called diffusers. diffusers makes it easy for us to diffusers makes it easy for
    us to

    execute the code and the forward and the execute the code and the forward and
    the'
  concept_slugs:
  - ddpm
  - epsilon-prediction
  - simple-loss-objective
- idx: 5
  start_sec: 335.199
  end_sec: 411.759
  text: 'execute the code and the forward and the

    reverse transition process. I will reverse transition process. I will reverse
    transition process. I will

    explain that in detail once we come to explain that in detail once we come to
    explain that in detail once we come to

    it. But uh using some simple lines of it. But uh using some simple lines of it.
    But uh using some simple lines of

    code, we can execute our kernels very code, we can execute our kernels very code,
    we can execute our kernels very

    well using the diffusers library. That well using the diffusers library. That
    well using the diffusers library. That

    is why it is very valuable and people is why it is very valuable and people is
    why it is very valuable and people

    use it quite commonly for coding use it quite commonly for coding use it quite
    commonly for coding

    diffusion models. [sighs] [sighs]

    Okay. So next what we have to do is we Okay. So next what we have to do is we
    Okay. So next what we have to do is we

    have to go to hugging face. [snorts]

    we have to go to hugging face and uh we we have to go to hugging face and uh we
    we have to go to hugging face and uh we

    have to create an access token. have to create an access token. have to create
    an access token.

    So this is a process which is quite So this is a process which is quite So this
    is a process which is quite

    simple. You have to go to hugging phase simple. You have to go to hugging phase
    simple. You have to go to hugging phase

    go to tokens and then u you can create a go to tokens and then u you can create
    a go to tokens and then u you can create a

    token with a read and a right token with a read and a right token with a read
    and a right

    permission. It looks something like permission. It looks something like permission.
    It looks something like

    this. Once you have the token, you can run Once you have the token, you can run

    this command to log in using that token. And uh this is something which is you'
  concept_slugs:
  - ddpm
  - epsilon-prediction
  - simple-loss-objective
- idx: 6
  start_sec: 411.759
  end_sec: 493.67
  text: 'And uh this is something which is you

    need to install the git lfs to upload need to install the git lfs to upload need
    to install the git lfs to upload

    your model checkpoints. Okay. So uh in this code block we have Okay. So uh in
    this code block we have

    defined a few functions which are going defined a few functions which are going
    defined a few functions which are going

    to be useful for us as we move along to be useful for us as we move along to be
    useful for us as we move along

    through this notebook. through this notebook. through this notebook.

    Let''s let''s try to understand what these Let''s let''s try to understand what
    these Let''s let''s try to understand what these

    functions are doing. The first function that we have defined The first function
    that we have defined

    is called show images. >> [snorts]

    >> So what this does is given a batch of >> So what this does is given a batch
    of >> So what this does is given a batch of

    images X it makes a grid. images X it makes a grid. images X it makes a grid.

    So you basically see the images in the So you basically see the images in the
    So you basically see the images in the

    form of a grid. [snorts]

    Okay. So this this is just a Okay. So this this is just a Okay. So this this is
    just a

    manipulation trick. Uh given the images manipulation trick. Uh given the images
    manipulation trick. Uh given the images

    as an input, it''s a way of displaying as an input, it''s a way of displaying
    as an input, it''s a way of displaying

    the images in a different format. Okay. So the second is define make grid Okay.
    So the second is define make grid

    given a list of pil images stack them given a list of pil images stack them given
    a list of pil images stack them

    together into a line for easy viewing. together into a line for easy viewing.
    together into a line for easy viewing.

    So what this does is that it stacks So what this does is that it stacks So what
    this does is that it stacks

    images as a single line as opposed to'
  concept_slugs:
  - ddpm
  - epsilon-prediction
  - simple-loss-objective
- idx: 7
  start_sec: 493.67
  end_sec: 550.88
  text: 'images as a single line as opposed to images as a single line as opposed
    to

    converting them to a grid which is converting them to a grid which is converting
    them to a grid which is

    happening in this function. happening in this function. happening in this function.

    We will see exactly how these functions We will see exactly how these functions
    We will see exactly how these functions

    work because we are going to use them in work because we are going to use them
    in work because we are going to use them in

    some of the subsequent cells down below. some of the subsequent cells down below.
    some of the subsequent cells down below.

    [snorts] [snorts]

    Okay. Up until now we have not done Okay. Up until now we have not done Okay.
    Up until now we have not done

    anything with respect to diffusion yet. anything with respect to diffusion yet.
    anything with respect to diffusion yet.

    We have simply been installing We have simply been installing We have simply been
    installing

    libraries. libraries. libraries.

    Notice we have imported numpy torch Notice we have imported numpy torch Notice
    we have imported numpy torch

    torch.nfunctional torch.nfunctional torch.nfunctional

    as f mattplot lib and from pil import as f mattplot lib and from pil import as
    f mattplot lib and from pil import

    image. These are the packages which we image. These are the packages which we
    image. These are the packages which we

    have imported for this code. Okay. Now what about the data set? Okay. Now what
    about the data set?

    Remember the objective the whole Remember the objective the whole Remember the
    objective the whole

    objective of DDPM and uh in fact this objective of DDPM and uh in fact this objective
    of DDPM and uh in fact this

    course is to learn deep generative course is to learn deep generative course is
    to learn deep generative

    modeling which means that we will be modeling which means that we will be modeling
    which means that we will be

    given a true data distribution given a true data distribution given a true data
    distribution

    P data in fact we will not be given two P data in fact we will not be given two
    P data in fact we will not be given two

    true data distribution. We want to true data distribution. We want to'
  concept_slugs:
  - ddpm
  - epsilon-prediction
  - simple-loss-objective
- idx: 8
  start_sec: 550.88
  end_sec: 628.959
  text: 'true data distribution. We want to

    predict the predict the predict the

    data distribution which is P5 of X which data distribution which is P5 of X which
    data distribution which is P5 of X which

    is as close as possible to the true data is as close as possible to the true data
    is as close as possible to the true data

    distribution. distribution. distribution.

    And all we are given are samples which And all we are given are samples which
    And all we are given are samples which

    are drawn from this true data are drawn from this true data are drawn from this
    true data

    distribution that is uh that is the distribution that is uh that is the distribution
    that is uh that is the

    whole whole whole

    problem statement that we have in our problem statement that we have in our problem
    statement that we have in our

    hand. Now in this particular notebook hand. Now in this particular notebook hand.
    Now in this particular notebook

    the samples of data are collected from the samples of data are collected from
    the samples of data are collected from

    this link. Let''s go ahead and uh click this link. Let''s go ahead and uh click
    this link. Let''s go ahead and uh click

    on this link. on this link. on this link.

    [snorts] [snorts]

    It is a data set which consists of It is a data set which consists of It is a
    data set which consists of

    images of butterflies. images of butterflies. images of butterflies.

    Now I think there are around 1,000 Now I think there are around 1,000 Now I think
    there are around 1,000

    images over here. >> If you go and search this data set, you >> If you go and
    search this data set, you

    can see there are 1,000 rows in the can see there are 1,000 rows in the can see
    there are 1,000 rows in the

    search column. [snorts] And this is how the images look [snorts] And this is how
    the images look

    like. like. like.

    [snorts] Okay. So this is the data set that we''ll Okay. So this is the data set
    that we''ll

    be working with a collection of thousand be working with a collection of thousand
    be working with a collection of thousand

    butterfly pictures. butterfly pictures.'
  concept_slugs:
  - ddpm
  - epsilon-prediction
  - simple-loss-objective
- idx: 9
  start_sec: 628.959
  end_sec: 696.24
  text: 'butterfly pictures.

    And uh once you run this code And uh once you run this code And uh once you run
    this code

    [snorts] [snorts]

    in this code what we''ll be doing is we in this code what we''ll be doing is we
    in this code what we''ll be doing is we

    will uh convert these images into 32 pixels. So convert these images into 32 pixels.
    So

    you can see the image size is is 32 and you can see the image size is is 32 and
    you can see the image size is is 32 and

    you''re transforming each image into 32x you''re transforming each image into
    32x you''re transforming each image into 32x

    32. So you''re resizing each image. 32. So you''re resizing each image. 32. So
    you''re resizing each image.

    This is very standard in uh machine This is very standard in uh machine This is
    very standard in uh machine

    learning pre-processing step where we learning pre-processing step where we learning
    pre-processing step where we

    have to make sure that every single have to make sure that every single have to
    make sure that every single

    image in the data set carries the same image in the data set carries the same
    image in the data set carries the same

    dimension which becomes helpful for dimension which becomes helpful for dimension
    which becomes helpful for

    downstream processing. [snorts] Okay. And then the next step that we do Okay.
    And then the next step that we do

    is we uh do a random flip is we uh do a random flip is we uh do a random flip

    and this is just done to augment the and this is just done to augment the and
    this is just done to augment the

    data data data

    and then we do a normalization. So all and then we do a normalization. So all
    and then we do a normalization. So all

    the pixel values are mapped to minus1 to the pixel values are mapped to minus1
    to the pixel values are mapped to minus1 to

    1. 1. 1.

    [snorts] [snorts]

    And uh if you run this you will see that And uh if you run this you will see that
    And uh if you run this you will see that

    we have divided uh we have divided uh'
  concept_slugs:
  - ddpm
  - epsilon-prediction
  - simple-loss-objective
- idx: 10
  start_sec: 696.24
  end_sec: 764.47
  text: 'we have divided uh

    we have first of all got the data. I we have first of all got the data. I we have
    first of all got the data. I

    don''t think the train test split is done don''t think the train test split is
    done don''t think the train test split is done

    over here. over here. over here.

    U okay and then we are serving the data U okay and then we are serving the data
    U okay and then we are serving the data

    in in batches. So you''ll see the batch in in batches. So you''ll see the batch
    in in batches. So you''ll see the batch

    size is 64 at a time. So at a time 64 size is 64 at a time. So at a time 64 size
    is 64 at a time. So at a time 64

    samples will be processed in one single samples will be processed in one single
    samples will be processed in one single

    batch. Okay, let''s go ahead. If you just sample Okay, let''s go ahead. If you
    just sample

    some of the images. some of the images. some of the images.

    So here we have you see we have uh use So here we have you see we have uh use
    So here we have you see we have uh use

    this show images function. So show this show images function. So show this show
    images function. So show

    images basically displays the image in images basically displays the image in
    images basically displays the image in

    the form of a grid. the form of a grid. the form of a grid.

    And uh here you can see that we have uh displayed the images and uh displayed
    the images and

    trying yeah the the shape is uh 8 which trying yeah the the shape is uh 8 which
    trying yeah the the shape is uh 8 which

    is number of images and uh three means is number of images and uh three means
    is number of images and uh three means

    every single pixel has three channels every single pixel has three channels every
    single pixel has three channels

    RGB and the pixels are 32x 32 that''s why RGB and the pixels are 32x 32 that''s
    why RGB and the pixels are 32x 32 that''s why

    the shape comes up like this'
  concept_slugs:
  - ddpm
  - epsilon-prediction
  - simple-loss-objective
- idx: 11
  start_sec: 764.47
  end_sec: 831.6
  text: 'the shape comes up like this the shape comes up like this

    and here we are simply and here we are simply and here we are simply

    resizing for u better viewing. So you resizing for u better viewing. So you resizing
    for u better viewing. So you

    can ignore this for now. Just focus your can ignore this for now. Just focus your
    can ignore this for now. Just focus your

    attention on this attention on this attention on this

    code where our train data loader is code where our train data loader is code where
    our train data loader is

    basically containing all these images of basically containing all these images
    of basically containing all these images of

    butterflies. butterflies. butterflies.

    [snorts] Okay. So next comes a very important Okay. So next comes a very important

    step where we define the scheduleuler. step where we define the scheduleuler.
    step where we define the scheduleuler.

    Now first of all what do we mean by a Now first of all what do we mean by a Now
    first of all what do we mean by a

    scheduleuler? To understand that we need scheduleuler? To understand that we need
    scheduleuler? To understand that we need

    to quickly revise our forward diffusion to quickly revise our forward diffusion
    to quickly revise our forward diffusion

    process. process. process.

    So remember that in the forward So remember that in the forward So remember that
    in the forward

    diffusion process what we do is that we diffusion process what we do is that we
    diffusion process what we do is that we

    have a number of these diffusers have a number of these diffusers have a number
    of these diffusers

    u which transform the image slowly and u which transform the image slowly and
    u which transform the image slowly and

    the final image which you see is that of the final image which you see is that
    of the final image which you see is that of

    noise noise noise

    and uh every single and uh every single and uh every single

    transformation here is a gshian kernel transformation here is a gshian kernel
    transformation here is a gshian kernel

    that we apply with a specific mean and that we apply with a specific mean and
    that we apply with a specific mean and

    variance. variance.'
  concept_slugs:
  - ddpm
  - epsilon-prediction
  - simple-loss-objective
- idx: 12
  start_sec: 831.6
  end_sec: 913.75
  text: 'variance.

    Now we had looked at this in quite some Now we had looked at this in quite some
    Now we had looked at this in quite some

    detail to understand uh how these mean detail to understand uh how these mean
    detail to understand uh how these mean

    and variances are are designed and variances are are designed and variances are
    are designed

    but uh I''ll just give you the final uh but uh I''ll just give you the final uh
    but uh I''ll just give you the final uh

    gist of it. gist of it. gist of it.

    So So

    finally what happens is that let''s say finally what happens is that let''s say
    finally what happens is that let''s say

    you have this image okay which you you have this image okay which you you have
    this image okay which you

    want to transform at each step and let''s want to transform at each step and let''s
    want to transform at each step and let''s

    say this image is defined as say this image is defined as say this image is defined
    as

    u x0. Okay. The way you write x1 is x1 u x0. Okay. The way you write x1 is x1
    u x0. Okay. The way you write x1 is x1

    is equal to is equal to is equal to

    alpha 1 alpha 1 alpha 1

    * x0 * x0 * x0

    plus plus plus

    beta 1 * epsilon where epsilon is a beta 1 * epsilon where epsilon is a beta 1
    * epsilon where epsilon is a

    random variable which takes a value random variable which takes a value random
    variable which takes a value

    between 0 and 1. between 0 and 1. between 0 and 1.

    Now this term this entire term Now this term this entire term Now this term this
    entire term

    essentially means that we are sampling essentially means that we are sampling
    essentially means that we are sampling

    from a gshian from a gshian from a gshian

    with a mean of alpha 1 * the mean of x0 with a mean of alpha 1 * the mean of x0
    with a mean of alpha 1 * the mean of x0

    and a standard deviation of beta 1. And we do this for all the subsequent And
    we do this for all the subsequent

    transitions. For example, x2 becomes'
  concept_slugs:
  - ddpm
  - epsilon-prediction
  - simple-loss-objective
- idx: 13
  start_sec: 913.75
  end_sec: 1019.839
  text: 'transitions. For example, x2 becomes transitions. For example, x2 becomes

    alpha 2 x1 alpha 2 x1 alpha 2 x1

    plus beta 2 epsilon. And you see here this epsilon this is And you see here this
    epsilon this is

    the noise that we are adding in the the noise that we are adding in the the noise
    that we are adding in the

    forward diffusion process. forward diffusion process. forward diffusion process.

    And alpha 1 and beta 1 are they have a And alpha 1 and beta 1 are they have a
    And alpha 1 and beta 1 are they have a

    relation they are related in such a way relation they are related in such a way
    relation they are related in such a way

    that their square is always equal to that their square is always equal to that
    their square is always equal to

    one. >> [snorts]

    >> Now in in in the literature what we will >> Now in in in the literature what
    we will >> Now in in in the literature what we will

    commonly see is commonly see is commonly see is

    let''s say we call this alpha 1 squared let''s say we call this alpha 1 squared
    let''s say we call this alpha 1 squared

    as p as p as p

    and this beta 1 square as q. So you can and this beta 1 square as q. So you can
    and this beta 1 square as q. So you can

    rewrite the above equation as root p root p

    q plus root root

    q q q

    sorry root p sorry root p sorry root p

    x0 x0 x0

    plus roo<unk> q plus roo<unk> q plus roo<unk> q

    * epsilon >> [snorts]

    >> So this is how the equation looks like >> So this is how the equation looks
    like >> So this is how the equation looks like

    roo<unk> p of x0 + roo<unk> q into roo<unk> p of x0 + roo<unk> q into roo<unk>
    p of x0 + roo<unk> q into

    epsilon. [snorts] epsilon. [snorts] epsilon. [snorts]

    And now you can further simplify this by And now you can further simplify this
    by And now you can further simplify this by

    writing um by by using this equation that alpha square + beta square is equal'
  concept_slugs:
  - ddpm
  - epsilon-prediction
  - simple-loss-objective
- idx: 14
  start_sec: 1019.839
  end_sec: 1093.909
  text: 'that alpha square + beta square is equal

    to 1. So p + q = 1 to 1. So p + q = 1 to 1. So p + q = 1

    and which which means that q = 1 - p. and which which means that q = 1 - p. and
    which which means that q = 1 - p.

    So you can write this expression as x1 So you can write this expression as x1
    So you can write this expression as x1

    is equal to<unk> I I know this is a bunch of mathematical I I know this is a bunch
    of mathematical

    trickery but this is the common notation trickery but this is the common notation
    trickery but this is the common notation

    which people use in the literature which people use in the literature which people
    use in the literature

    and what they further do is that this P and what they further do is that this
    P and what they further do is that this P

    is replaced by another symbol which is is replaced by another symbol which is
    is replaced by another symbol which is

    alpha. So they write the expression alpha. So they write the expression alpha.
    So they write the expression

    which looks like this. And I''m just explaining this to you And I''m just explaining
    this to you

    because you will see this notation very because you will see this notation very
    because you will see this notation very

    familiar and I don''t want to you to familiar and I don''t want to you to familiar
    and I don''t want to you to

    confuse it with whatever we were confuse it with whatever we were confuse it with
    whatever we were

    initially starting out with. initially starting out with. initially starting out
    with.

    It is just a matter of using a different It is just a matter of using a different
    It is just a matter of using a different

    notations. But fundamentally both of notations. But fundamentally both of notations.
    But fundamentally both of

    these representations mean the exact these representations mean the exact these
    representations mean the exact

    same thing. same thing. same thing.

    Okay. Now let us understand what this Okay. Now let us understand what this Okay.
    Now let us understand what this

    scheduleuler does. Okay. So uh'
  concept_slugs:
  - ddpm
  - epsilon-prediction
  - simple-loss-objective
- idx: 15
  start_sec: 1093.909
  end_sec: 1173.83
  text: 'scheduleuler does. Okay. So uh scheduleuler does. Okay. So uh

    you see here what we are doing is from you see here what we are doing is from
    you see here what we are doing is from

    diffusers we are importing DDPM diffusers we are importing DDPM diffusers we are
    importing DDPM

    scheduleuler scheduleuler scheduleuler

    and then we are defining one more and then we are defining one more and then we
    are defining one more

    quantity which is noise scheduleuler quantity which is noise scheduleuler quantity
    which is noise scheduleuler

    equal to DDPM scheduleuler and in the equal to DDPM scheduleuler and in the equal
    to DDPM scheduleuler and in the

    bracket we are writing the number of bracket we are writing the number of bracket
    we are writing the number of

    time steps. time steps. time steps.

    So this DDPM scheduleuler takes care of So this DDPM scheduleuler takes care of
    So this DDPM scheduleuler takes care of

    the entire forward process for us the entire forward process for us the entire
    forward process for us

    and uh let''s let''s try to understand and uh let''s let''s try to understand
    and uh let''s let''s try to understand

    what what happens. what what happens. what what happens.

    So all you need to do is to create the So all you need to do is to create the
    So all you need to do is to create the

    forward transition process forward transition process forward transition process

    uh you need to write this one equation. uh you need to write this one equation.
    uh you need to write this one equation.

    So let''s let''s understand that. So in So let''s let''s understand that. So in
    So let''s let''s understand that. So in

    this line we are plotting plt.plot plot this line we are plotting plt.plot plot
    this line we are plotting plt.plot plot

    noise [snorts] scheduleuler noise [snorts] scheduleuler noise [snorts] scheduleuler

    dotalphas.compro.cpu and in the second plot and in the second plot

    we are taking a square root of 1 minus we are taking a square root of 1 minus
    we are taking a square root of 1 minus

    whatever this first quantity was. whatever this first quantity was. whatever this
    first quantity was.

    Now this is something which is uh the Now this is something which is uh the Now
    this is something which is uh the

    cumulative'
  concept_slugs:
  - ddpm
  - epsilon-prediction
  - simple-loss-objective
- idx: 16
  start_sec: 1177.35
  end_sec: 1243.84
  text: 'mean and the variance starting from the mean and the variance starting from
    the

    first time step to anywhere in the first time step to anywhere in the first time
    step to anywhere in the

    uh in in the forward diffusion process. uh in in the forward diffusion process.
    uh in in the forward diffusion process.

    So let''s let''s try to understand or So let''s let''s try to understand or So
    let''s let''s try to understand or

    before even understanding this uh we before even understanding this uh we before
    even understanding this uh we

    will see how the uh noise scheduleuler will see how the uh noise scheduleuler
    will see how the uh noise scheduleuler

    works. works. works.

    So okay uh just forget about the last So okay uh just forget about the last So
    okay uh just forget about the last

    piece of code for now. Try to focus on piece of code for now. Try to focus on
    piece of code for now. Try to focus on

    this time steps equal to torch dotline this time steps equal to torch dotline
    this time steps equal to torch dotline

    space 0A 9999 comma 8. space 0A 9999 comma 8. space 0A 9999 comma 8.

    So what we are essentially doing is that So what we are essentially doing is that
    So what we are essentially doing is that

    we are creating 8 time steps between 0 we are creating 8 time steps between 0
    we are creating 8 time steps between 0

    and 999 and 999 and 999

    and and and

    the second line is important. No the second line is important. No the second line
    is important. No

    torch.random random like XB torch.random random like XB torch.random random like
    XB

    which means that we are creating noise which means that we are creating noise
    which means that we are creating noise

    values for values for values for

    every single pixel in this image. So you every single pixel in this image. So
    you every single pixel in this image. So you

    see here the noise tensor looks like see here the noise tensor looks like see
    here the noise tensor looks like

    this. U now let''s try to understand what this. U now let''s try to understand
    what this. U now let''s try to understand what

    this noise tensor essentially means. this noise tensor essentially means.'
  concept_slugs:
  - ddpm
  - epsilon-prediction
  - simple-loss-objective
- idx: 17
  start_sec: 1243.84
  end_sec: 1308.159
  text: 'this noise tensor essentially means.

    So imagine that you have uh this image So imagine that you have uh this image
    So imagine that you have uh this image

    right right right

    which is 32x 32 in this case. And in the forward process we had And in the forward
    process we had

    discussed that we have to specify a discussed that we have to specify a discussed
    that we have to specify a

    noise. noise. noise.

    Now this noise the dimension of this Now this noise the dimension of this Now
    this noise the dimension of this

    noise is same as the size of this image noise is same as the size of this image
    noise is same as the size of this image

    because we are adding this noise to each because we are adding this noise to each
    because we are adding this noise to each

    of the pixel in this image. of the pixel in this image. of the pixel in this image.

    That is why here you see the shape of That is why here you see the shape of That
    is why here you see the shape of

    this is XB which is uh the shape of our this is XB which is uh the shape of our
    this is XB which is uh the shape of our

    image itself. And once you define the noise, you can And once you define the noise,
    you can

    simply use the noise scheduleuler which simply use the noise scheduleuler which
    simply use the noise scheduleuler which

    you created using the DDPM scheduleuler you created using the DDPM scheduleuler
    you created using the DDPM scheduleuler

    and you can say noise scheduleuler dot and you can say noise scheduleuler dot
    and you can say noise scheduleuler dot

    add noise add noise add noise

    and you can pass the initial input image and you can pass the initial input image
    and you can pass the initial input image

    the noise values that you want to add the noise values that you want to add the
    noise values that you want to add

    and the number of time steps. Why is the and the number of time steps. Why is
    the and the number of time steps. Why is the

    number of time steps important? because number of time steps important? because'
  concept_slugs:
  - ddpm
  - epsilon-prediction
  - simple-loss-objective
- idx: 18
  start_sec: 1308.159
  end_sec: 1376.63
  text: 'number of time steps important? because

    you need to tell the you need to tell the you need to tell the

    package how many steps you want to carry package how many steps you want to carry
    package how many steps you want to carry

    out in the forward diffusion process. out in the forward diffusion process. out
    in the forward diffusion process.

    For example, when we did this for the For example, when we did this for the For
    example, when we did this for the

    image of the Batman, you can see that we image of the Batman, you can see that
    we image of the Batman, you can see that we

    did it 1 2 3 four times. So there were did it 1 2 3 four times. So there were
    did it 1 2 3 four times. So there were

    four forward diffusion kernels in this four forward diffusion kernels in this
    four forward diffusion kernels in this

    whole process. whole process. whole process.

    Now in this case we want to do it eight Now in this case we want to do it eight
    Now in this case we want to do it eight

    times. So the number is eight. times. So the number is eight. times. So the number
    is eight.

    And as as soon as you specify this, what And as as soon as you specify this, what
    And as as soon as you specify this, what

    is happening under the hood is is happening under the hood is is happening under
    the hood is

    the system is applying this formula. The system is applying this formula The system
    is applying this formula

    eight times. And uh you might be wondering how how And uh you might be wondering
    how how

    are the values for this beta 1, beta 2, are the values for this beta 1, beta 2,
    are the values for this beta 1, beta 2,

    etc. etc. etc.

    designed. So the values are decided designed. So the values are decided designed.
    So the values are decided

    internally through this noise internally through this noise internally through
    this noise

    scheduleuler. You can define specific scheduleuler. You can define specific scheduleuler.
    You can define specific

    values which they have mentioned here. values which they have mentioned here.
    values which they have mentioned here.

    DDPM scheduleuler. You can write beta'
  concept_slugs:
  - ddpm
  - epsilon-prediction
  - simple-loss-objective
- idx: 19
  start_sec: 1376.63
  end_sec: 1426.24
  text: 'DDPM scheduleuler. You can write beta DDPM scheduleuler. You can write beta

    start and beta end which means that you start and beta end which means that you
    start and beta end which means that you

    can specify how the variance is changing can specify how the variance is changing
    can specify how the variance is changing

    with time. So this is something you can with time. So this is something you can
    with time. So this is something you can

    definitely do. definitely do. definitely do.

    And uh one thing we can understand from And uh one thing we can understand from
    And uh one thing we can understand from

    this graph, I haven''t properly explained this graph, I haven''t properly explained
    this graph, I haven''t properly explained

    what this means is as you increase the what this means is as you increase the
    what this means is as you increase the

    number of time steps you see the number of time steps you see the number of time
    steps you see the

    cumulative mean goes down and the cumulative mean goes down and the cumulative
    mean goes down and the

    cumulative variance goes up. That''s what cumulative variance goes up. That''s
    what cumulative variance goes up. That''s what

    we are seeing in this graph. we are seeing in this graph. we are seeing in this
    graph.

    Why does the cumulative variance go up? Why does the cumulative variance go up?
    Why does the cumulative variance go up?

    Because by default the variance in the Because by default the variance in the
    Because by default the variance in the

    noise schedule has an increasing uh noise schedule has an increasing uh noise
    schedule has an increasing uh

    increasing property. So it increases at increasing property. So it increases at
    increasing property. So it increases at

    every time step and because the square every time step and because the square
    every time step and because the square

    of mean and variance is equal to one, of mean and variance is equal to one, of
    mean and variance is equal to one,

    the mean has to decrease for every time the mean has to decrease for every time
    the mean has to decrease for every time

    step. Now what do I mean by cumulative step. Now what do I mean by cumulative'
  concept_slugs:
  - ddpm
  - epsilon-prediction
  - simple-loss-objective
- idx: 20
  start_sec: 1426.24
  end_sec: 1471.919
  text: 'step. Now what do I mean by cumulative

    mean? Well, cumulative means that if if mean? Well, cumulative means that if if
    mean? Well, cumulative means that if if

    I have a mean of alpha 1 * x0 when I go I have a mean of alpha 1 * x0 when I go
    I have a mean of alpha 1 * x0 when I go

    from x0 to x1 and the scale factor is from x0 to x1 and the scale factor is from
    x0 to x1 and the scale factor is

    alpha 2 when I go from x1 to x2. If alpha 2 when I go from x1 to x2. If alpha
    2 when I go from x1 to x2. If

    someone asks me uh Rajat what is the someone asks me uh Rajat what is the someone
    asks me uh Rajat what is the

    scale factor when you go from X0 to X2 scale factor when you go from X0 to X2
    scale factor when you go from X0 to X2

    [gasps] [gasps] [gasps]

    it is simply the multiplication of these it is simply the multiplication of these
    it is simply the multiplication of these

    means right it is alpha 1 * alpha 2 that means right it is alpha 1 * alpha 2 that
    means right it is alpha 1 * alpha 2 that

    is exactly what they have done here they is exactly what they have done here they
    is exactly what they have done here they

    have plotted and why does the root come have plotted and why does the root come
    have plotted and why does the root come

    here the root comes here because they here the root comes here because they here
    the root comes here because they

    are using this notation where everything are using this notation where everything
    are using this notation where everything

    is replaced by a root is replaced by a root is replaced by a root

    so this is how the the mean in the so this is how the the mean in the so this
    is how the the mean in the

    forward diffusion process the cumulative forward diffusion process the cumulative
    forward diffusion process the cumulative

    mean changes es with time it it actually mean changes es with time it it actually'
  concept_slugs:
  - ddpm
  - epsilon-prediction
  - simple-loss-objective
- idx: 21
  start_sec: 1471.919
  end_sec: 1528.07
  text: 'mean changes es with time it it actually

    reduces in magnitude and the cumulative reduces in magnitude and the cumulative
    reduces in magnitude and the cumulative

    variance it it increases because as we variance it it increases because as we
    variance it it increases because as we

    go closer and closer to the noise we go closer and closer to the noise we go closer
    and closer to the noise we

    want to add as much variance as we can. Okay. So so far what we have seen is uh
    Okay. So so far what we have seen is uh

    I want you to focus on these two I want you to focus on these two I want you to
    focus on these two

    quantities. The first is this quantity quantities. The first is this quantity
    quantities. The first is this quantity

    which is known as noise where we are which is known as noise where we are which
    is known as noise where we are

    specifying how much noise is added in specifying how much noise is added in specifying
    how much noise is added in

    the forward diffusion process for each the forward diffusion process for each
    the forward diffusion process for each

    pixel. And later it will turn out that pixel. And later it will turn out that
    pixel. And later it will turn out that

    this is exactly the quantity that we are this is exactly the quantity that we
    are this is exactly the quantity that we are

    trying to predict in the reverse trying to predict in the reverse trying to predict
    in the reverse

    process. process.

    But for now we should understand that at But for now we should understand that
    at But for now we should understand that at

    every time step we are adding a certain every time step we are adding a certain
    every time step we are adding a certain

    noise level for every pixel in the noise level for every pixel in the noise level
    for every pixel in the

    image. And the shape of this noise is image. And the shape of this noise is image.
    And the shape of this noise is

    exactly the same as the shape of each exactly the same as the shape of each exactly
    the same as the shape of each

    image which is 32x 32x3.'
  concept_slugs:
  - ddpm
  - epsilon-prediction
  - simple-loss-objective
- idx: 22
  start_sec: 1531.11
  end_sec: 1578.88
  text: 'Okay. So in fact it is not by3 I think Okay. So in fact it is not by3 I think

    it''s just 32x 32 because for every pixel it''s just 32x 32 because for every
    pixel it''s just 32x 32 because for every pixel

    u you''re adding a specific noise and if u you''re adding a specific noise and
    if u you''re adding a specific noise and if

    there are 32x 32 pixels for a single there are 32x 32 pixels for a single there
    are 32x 32 pixels for a single

    channel there will be 32x 32 different channel there will be 32x 32 different
    channel there will be 32x 32 different

    noise levels and if it is if we are noise levels and if it is if we are noise
    levels and if it is if we are

    considering three channels 32x 32x3 then considering three channels 32x 32x3 then
    considering three channels 32x 32x3 then

    there will be that that many noise uh there will be that that many noise uh there
    will be that that many noise uh

    parameters which you have to consider. parameters which you have to consider.
    parameters which you have to consider.

    So in this case it will be 3x 32x 33 uh So in this case it will be 3x 32x 33 uh
    So in this case it will be 3x 32x 33 uh

    3x 32x 32. 3x 32x 32. 3x 32x 32.

    Okay. So we have understood intuitively Okay. So we have understood intuitively
    Okay. So we have understood intuitively

    what the noise level means. So whenever what the noise level means. So whenever
    what the noise level means. So whenever

    I write epsilon in this equation now you I write epsilon in this equation now
    you I write epsilon in this equation now you

    should think back and say that okay fine should think back and say that okay fine
    should think back and say that okay fine

    what I''m doing is that I''m corrupting what I''m doing is that I''m corrupting
    what I''m doing is that I''m corrupting

    every single pixel in the image. So I every single pixel in the image. So I every
    single pixel in the image. So I

    need to know how much each each pixel is need to know how much each each pixel
    is'
  concept_slugs:
  - ddpm
  - epsilon-prediction
  - simple-loss-objective
- idx: 23
  start_sec: 1578.88
  end_sec: 1641.269
  text: 'need to know how much each each pixel is

    corrupted by and corrupted by and corrupted by and

    that corruption level I''m identifying through through

    uh this this noise value which I''m uh this this noise value which I''m uh this
    this noise value which I''m

    manually adding. manually adding. manually adding.

    Okay. So this is the forward diffusion Okay. So this is the forward diffusion
    Okay. So this is the forward diffusion

    process. That is excellent. What about process. That is excellent. What about
    process. That is excellent. What about

    the reverse diffusion process? Let''s go the reverse diffusion process? Let''s
    go the reverse diffusion process? Let''s go

    ahead and check it. Now first of all the ahead and check it. Now first of all
    the ahead and check it. Now first of all the

    way our model is defined way our model is defined way our model is defined

    uh remember the objective of the uh remember the objective of the uh remember
    the objective of the

    diffusion model is to predict the noise diffusion model is to predict the noise
    diffusion model is to predict the noise

    level level level

    which is added in the forward diffusion which is added in the forward diffusion
    which is added in the forward diffusion

    process. We want to predict the same process. We want to predict the same process.
    We want to predict the same

    thing in the reverse diffusion process. thing in the reverse diffusion process.
    thing in the reverse diffusion process.

    So in the reverse diffusion process what So in the reverse diffusion process what
    So in the reverse diffusion process what

    happens is that so now we know the happens is that so now we know the happens
    is that so now we know the

    forward diffusion process in detail forward diffusion process in detail forward
    diffusion process in detail

    right in the reverse diffusion process right in the reverse diffusion process
    right in the reverse diffusion process

    let''s say I am given I''m at this time let''s say I am given I''m at this time
    let''s say I am given I''m at this time

    step step step

    I am asked the question what is the I am asked the question what is the I am asked
    the question what is the

    probability that probability that probability that

    uh from this time step you are'
  concept_slugs:
  - ddpm
  - epsilon-prediction
  - simple-loss-objective
- idx: 24
  start_sec: 1641.269
  end_sec: 1690.96
  text: 'uh from this time step you are uh from this time step you are

    transitioning so you''re predicting what transitioning so you''re predicting what
    transitioning so you''re predicting what

    is the image in the previous time step is the image in the previous time step
    is the image in the previous time step

    given the image at the current time given the image at the current time given
    the image at the current time

    And you can only find that if you know And you can only find that if you know
    And you can only find that if you know

    how much noise is subtracted from the how much noise is subtracted from the how
    much noise is subtracted from the

    current time step. Right? current time step. Right? current time step. Right?

    So the reverse process has two inputs. So the reverse process has two inputs.
    So the reverse process has two inputs.

    The first input is whatever your image The first input is whatever your image
    The first input is whatever your image

    is at the current time step and the is at the current time step and the is at
    the current time step and the

    second input is which time step are you second input is which time step are you
    second input is which time step are you

    looking at. For example, if you''re looking at. For example, if you''re looking
    at. For example, if you''re

    looking at this, then I am at let''s say looking at this, then I am at let''s
    say looking at this, then I am at let''s say

    in the reverse process, I am at time in the reverse process, I am at time in the
    reverse process, I am at time

    step equal to zero. Then if if I proceed step equal to zero. Then if if I proceed
    step equal to zero. Then if if I proceed

    ahead, ahead, ahead,

    I I look at this image and I''m at time I I look at this image and I''m at time
    I I look at this image and I''m at time

    step equal to 1. step equal to 1. step equal to 1.

    Then I I again proceed ahead and I I Then I I again proceed ahead and I I'
  concept_slugs:
  - ddpm
  - epsilon-prediction
  - simple-loss-objective
- idx: 25
  start_sec: 1690.96
  end_sec: 1741.19
  text: 'Then I I again proceed ahead and I I

    look at time step equal to two. And for look at time step equal to two. And for
    look at time step equal to two. And for

    each of these time step, my image looks each of these time step, my image looks
    each of these time step, my image looks

    different. But the main objective is different. But the main objective is different.
    But the main objective is

    given the time step and the current given the time step and the current given
    the time step and the current

    image I want to predict the image which image I want to predict the image which
    image I want to predict the image which

    has come before that. So I''m going in has come before that. So I''m going in
    has come before that. So I''m going in

    the reverse direction. the reverse direction. the reverse direction.

    And And And

    to do that people usually use a model to do that people usually use a model to
    do that people usually use a model

    which is called as a unit. which is called as a unit. which is called as a unit.

    Now we have not covered exactly what Now we have not covered exactly what Now
    we have not covered exactly what

    unit is in in this unit is in in this unit is in in this

    in these lectures because that is not in these lectures because that is not in
    these lectures because that is not

    the purpose of this course which is the the purpose of this course which is the
    the purpose of this course which is the

    principles of diffusion models. But principles of diffusion models. But principles
    of diffusion models. But

    essentially what we are doing is we are essentially what we are doing is we are
    essentially what we are doing is we are

    passing an image at at the start which passing an image at at the start which
    passing an image at at the start which

    is which is the current image and we are is which is the current image and we
    are is which is the current image and we are

    also passing the time step. We are also passing the time step. We are also passing
    the time step. We are

    passing both these quantities.'
  concept_slugs:
  - ddpm
  - epsilon-prediction
  - simple-loss-objective
- idx: 26
  start_sec: 1741.19
  end_sec: 1789.44
  text: 'passing both these quantities. passing both these quantities.

    So the model has the input image. It So the model has the input image. It So the
    model has the input image. It

    goes through several blocks of resonate goes through several blocks of resonate
    goes through several blocks of resonate

    layers each of which halves the image layers each of which halves the image layers
    each of which halves the image

    size by two. Then through the same size by two. Then through the same size by
    two. Then through the same

    number of blocks we upsample it again. number of blocks we upsample it again.
    number of blocks we upsample it again.

    And the final And the final And the final

    image is that of the same size as the image is that of the same size as the image
    is that of the same size as the

    input image. Why is that the case? input image. Why is that the case? input image.
    Why is that the case?

    Remember finally we have to predict the Remember finally we have to predict the
    Remember finally we have to predict the

    noise level which has been subtracted noise level which has been subtracted noise
    level which has been subtracted

    from every image to go to the previous from every image to go to the previous
    from every image to go to the previous

    image. And as we have seen the noise has image. And as we have seen the noise
    has image. And as we have seen the noise has

    the same dimensions as that of image. So the same dimensions as that of image.
    So the same dimensions as that of image. So

    the unit architecture makes sense for us the unit architecture makes sense for
    us the unit architecture makes sense for us

    because the input and the output have because the input and the output have because
    the input and the output have

    the same size. the same size. the same size.

    Now intuitively why do people choose Now intuitively why do people choose Now
    intuitively why do people choose

    unit? It has traditionally worked out to unit? It has traditionally worked out
    to unit? It has traditionally worked out to

    be the best and even in most of the be the best and even in most of the'
  concept_slugs:
  - ddpm
  - epsilon-prediction
  - simple-loss-objective
- idx: 27
  start_sec: 1789.44
  end_sec: 1842.87
  text: 'be the best and even in most of the

    modern diffusion architectures you will modern diffusion architectures you will
    modern diffusion architectures you will

    see the unit architecture very commonly see the unit architecture very commonly
    see the unit architecture very commonly

    used. Even in stable diffusion they use used. Even in stable diffusion they use
    used. Even in stable diffusion they use

    a unit architecture. I will [snorts] a unit architecture. I will [snorts] a unit
    architecture. I will [snorts]

    link a link in the description where we link a link in the description where we
    link a link in the description where we

    have taught unit very nicely in one of have taught unit very nicely in one of
    have taught unit very nicely in one of

    our recent lectures. our recent lectures. our recent lectures.

    Okay. So now comes the important part Okay. So now comes the important part Okay.
    So now comes the important part

    where we are actually defining the unit where we are actually defining the unit
    where we are actually defining the unit

    model and this also exists within the model and this also exists within the model
    and this also exists within the

    diffusers library. So we say that from diffusers library. So we say that from
    diffusers library. So we say that from

    diffusers import unit model diffusers import unit model diffusers import unit
    model

    and we say model equal to unit 2D model. and we say model equal to unit 2D model.
    and we say model equal to unit 2D model.

    Sample size is the image size which is Sample size is the image size which is
    Sample size is the image size which is

    the input and the output image uh size. the input and the output image uh size.
    the input and the output image uh size.

    Number of input and output channels are Number of input and output channels are
    Number of input and output channels are

    three. We already know how many resonant three. We already know how many resonant
    three. We already know how many resonant

    layers to use per unit block two. layers to use per unit block two. layers to
    use per unit block two.

    These are the dimensions of the These are the dimensions of the These are the
    dimensions of the

    different output channels and the number'
  concept_slugs:
  - ddpm
  - epsilon-prediction
  - simple-loss-objective
- idx: 28
  start_sec: 1842.87
  end_sec: 1888.24
  text: 'different output channels and the number different output channels and the
    number

    of types in the down and the uplock. of types in the down and the uplock. of types
    in the down and the uplock.

    This is largely standard so you don''t This is largely standard so you don''t
    This is largely standard so you don''t

    have to worry about this too much. have to worry about this too much. have to
    worry about this too much.

    Once we have defined the unit model Once we have defined the unit model Once we
    have defined the unit model

    uh we can actually create uh go ahead uh we can actually create uh go ahead uh
    we can actually create uh go ahead

    and create a training loop. Now this is and create a training loop. Now this is
    and create a training loop. Now this is

    something that is interesting. The first something that is interesting. The first
    something that is interesting. The first

    thing that we have to understand is that thing that we have to understand is that
    thing that we have to understand is that

    whenever we are defining this unit model whenever we are defining this unit model
    whenever we are defining this unit model

    we [snorts] have to pass two things to we [snorts] have to pass two things to
    we [snorts] have to pass two things to

    it. we have to pass an image and we have it. we have to pass an image and we have
    it. we have to pass an image and we have

    to pass the time step and then the model to pass the time step and then the model
    to pass the time step and then the model

    will predict something which has exact will predict something which has exact
    will predict something which has exact

    same shape as the input image. So let''s same shape as the input image. So let''s
    same shape as the input image. So let''s

    try to understand how we train this try to understand how we train this try to
    understand how we train this

    model and I think this is one of the model and I think this is one of the model
    and I think this is one of the

    most important part of this lecture most important part of this lecture'
  concept_slugs:
  - ddpm
  - epsilon-prediction
  - simple-loss-objective
- idx: 29
  start_sec: 1888.24
  end_sec: 1939.279
  text: 'most important part of this lecture

    because when we are looking at the because when we are looking at the because
    when we are looking at the

    theory we don''t really get to see the theory we don''t really get to see the
    theory we don''t really get to see the

    training loop for a practical example. training loop for a practical example.
    training loop for a practical example.

    So this is something which will give you So this is something which will give
    you So this is something which will give you

    a lot of confidence that you have really a lot of confidence that you have really
    a lot of confidence that you have really

    understood the diffusion theory well. understood the diffusion theory well. understood
    the diffusion theory well.

    Okay. So the first thing we do is we set Okay. So the first thing we do is we
    set Okay. So the first thing we do is we set

    the noise scheduleuler. the noise scheduleuler. the noise scheduleuler.

    Uh we use noise scheduleuler equal to Uh we use noise scheduleuler equal to Uh
    we use noise scheduleuler equal to

    DDPM scheduleuler. We have looked at DDPM scheduleuler. We have looked at DDPM
    scheduleuler. We have looked at

    this before. Number of time steps is this before. Number of time steps is this
    before. Number of time steps is

    1,000. 1,000. 1,000.

    Number of train time steps is 1,000. And Number of train time steps is 1,000.
    And Number of train time steps is 1,000. And

    beta schedule is so this is just a beta schedule is so this is just a beta schedule
    is so this is just a

    scheduleuler which which tells what is scheduleuler which which tells what is
    scheduleuler which which tells what is

    the variation in the beta values with the variation in the beta values with the
    variation in the beta values with

    time how fast the variance is going to time how fast the variance is going to
    time how fast the variance is going to

    grow. Remember we had said that the grow. Remember we had said that the grow.
    Remember we had said that the

    variance beta increases as the time variance beta increases as the time variance
    beta increases as the time

    steps increases and the mean actually steps increases and the mean actually'
  concept_slugs:
  - ddpm
  - epsilon-prediction
  - simple-loss-objective
- idx: 30
  start_sec: 1939.279
  end_sec: 2009.19
  text: 'steps increases and the mean actually

    goes down and because the sum of the goes down and because the sum of the goes
    down and because the sum of the

    squares is equal to one. squares is equal to one. squares is equal to one.

    Okay. We use a AdamW optimizer in in Okay. We use a AdamW optimizer in in Okay.
    We use a AdamW optimizer in in

    this case this case this case

    and uh let''s try to understand the and uh let''s try to understand the and uh
    let''s try to understand the

    number of epochs are 30 okay that''s fine number of epochs are 30 okay that''s
    fine number of epochs are 30 okay that''s fine

    for step and batch in enumerate train for step and batch in enumerate train for
    step and batch in enumerate train

    data loader data loader data loader

    clean images so clean images is we clean images so clean images is we clean images
    so clean images is we

    consider a batch of images so here the consider a batch of images so here the
    consider a batch of images so here the

    batch size is 64 so we have 64 images in batch size is 64 so we have 64 images
    in batch size is 64 so we have 64 images in

    a batch a batch a batch

    and this is the noise that we add to and this is the noise that we add to and
    this is the noise that we add to

    each image. Now this is important because this is Now this is important because
    this is

    the noise that we add in the forward the noise that we add in the forward the
    noise that we add in the forward

    diffusion process diffusion process diffusion process

    and u and u and u

    BS is this the batch size. Now this is the step which is the Now this is the step
    which is the

    forward diffusion process. forward diffusion process.

    What we do is uh What we do is uh What we do is uh

    actually the forward diffusion process actually the forward diffusion process
    actually the forward diffusion process

    has already been defined. Uh what what has already been defined. Uh what what
    has already been defined. Uh what what

    we do uh is in in this step. This is the'
  concept_slugs:
  - ddpm
  - epsilon-prediction
  - simple-loss-objective
- idx: 31
  start_sec: 2009.19
  end_sec: 2064.55
  text: 'we do uh is in in this step. This is the we do uh is in in this step. This
    is the

    main forward diffusion process. But I main forward diffusion process. But I main
    forward diffusion process. But I

    will discuss that a bit later after we will discuss that a bit later after we
    will discuss that a bit later after we

    discuss this here. What we are doing is discuss this here. What we are doing is
    discuss this here. What we are doing is

    that this time steps might be misleading that this time steps might be misleading
    that this time steps might be misleading

    because it might tell you that because it might tell you that because it might
    tell you that

    uh am I sampling all these thousand time uh am I sampling all these thousand time
    uh am I sampling all these thousand time

    steps or am I doing something else. So steps or am I doing something else. So
    steps or am I doing something else. So

    here what we are doing is that we are here what we are doing is that we are here
    what we are doing is that we are

    picking one random time step out of picking one random time step out of picking
    one random time step out of

    these thousand time steps and we are these thousand time steps and we are these
    thousand time steps and we are

    doing it for all the images which are doing it for all the images which are doing
    it for all the images which are

    there in our batch size. So sometimes I there in our batch size. So sometimes
    I there in our batch size. So sometimes I

    might pick 100, sometimes I might pick might pick 100, sometimes I might pick
    might pick 100, sometimes I might pick

    500, sometimes I might pick 600 etc. 500, sometimes I might pick 600 etc. 500,
    sometimes I might pick 600 etc.

    We will understand why we are picking a We will understand why we are picking
    a We will understand why we are picking a

    random image. random image. random image.

    Okay. Now have a look at this. So this is where the forward diffusion So this
    is where the forward diffusion

    process actually runs. What we say is'
  concept_slugs:
  - ddpm
  - epsilon-prediction
  - simple-loss-objective
- idx: 32
  start_sec: 2064.55
  end_sec: 2122.079
  text: 'process actually runs. What we say is process actually runs. What we say
    is

    noise scheduleuler dot add noise. noise scheduleuler dot add noise. noise scheduleuler
    dot add noise.

    So we are starting to corrupt the images So we are starting to corrupt the images
    So we are starting to corrupt the images

    and using one single line we can do and using one single line we can do and using
    one single line we can do

    that. All we have to do is we have to that. All we have to do is we have to that.
    All we have to do is we have to

    pass our images in our batch size. We pass our images in our batch size. We pass
    our images in our batch size. We

    have to pass the noise level at each have to pass the noise level at each have
    to pass the noise level at each

    time step which is epsilon time step which is epsilon time step which is epsilon

    and we have to pass this time steps and we have to pass this time steps and we
    have to pass this time steps

    which is this which is this which is this

    random random random

    random time step which we have selected random time step which we have selected
    random time step which we have selected

    for each image. for each image. for each image.

    So So

    then the forward diffusion process will then the forward diffusion process will
    then the forward diffusion process will

    proceed only till that time step. So proceed only till that time step. So proceed
    only till that time step. So

    here if if let''s say I sample 100 right. here if if let''s say I sample 100 right.
    here if if let''s say I sample 100 right.

    So I will generate all the noisy images So I will generate all the noisy images
    So I will generate all the noisy images

    from the clean image till the 100 time from the clean image till the 100 time
    from the clean image till the 100 time

    step. step. step.

    Now what I do is I Now what I do is I Now what I do is I

    in the next line I actually get the in the next line I actually get the'
  concept_slugs:
  - ddpm
  - epsilon-prediction
  - simple-loss-objective
- idx: 33
  start_sec: 2122.079
  end_sec: 2186.31
  text: 'in the next line I actually get the

    model prediction. So I pass this these model prediction. So I pass this these
    model prediction. So I pass this these

    noisy images noisy images noisy images

    uh to my model uh to my model uh to my model

    and uh what I do is I select this time and uh what I do is I select this time
    and uh what I do is I select this time

    step also which is one random value step also which is one random value step also
    which is one random value

    let''s say the value of 500 which I have let''s say the value of 500 which I have
    let''s say the value of 500 which I have

    chosen randomly chosen randomly chosen randomly

    and I get the prediction of this this and I get the prediction of this this and
    I get the prediction of this this

    model. model. model.

    So here I am using the unit model and So here I am using the unit model and So
    here I am using the unit model and

    I''m directly getting the prediction. I''m directly getting the prediction. I''m
    directly getting the prediction.

    So here the idea is like because you So here the idea is like because you So here
    the idea is like because you

    have specified this time step here noisy have specified this time step here noisy
    have specified this time step here noisy

    images images images

    only contains that image which is only contains that image which is only contains
    that image which is

    generated towards the very end. It is generated towards the very end. It is generated
    towards the very end. It is

    the image which is generated at that the image which is generated at that the
    image which is generated at that

    time step at 800 time step. And what we time step at 800 time step. And what we
    time step at 800 time step. And what we

    are saying is that given that image and are saying is that given that image and
    are saying is that given that image and

    the time step stamp which is 800, can my the time step stamp which is 800, can
    my the time step stamp which is 800, can my

    model model model

    predict how much noise has been added to'
  concept_slugs:
  - ddpm
  - epsilon-prediction
  - simple-loss-objective
- idx: 34
  start_sec: 2186.31
  end_sec: 2241.92
  text: 'predict how much noise has been added to predict how much noise has been
    added to

    that image so that I can get back to my that image so that I can get back to my
    that image so that I can get back to my

    original image as closely as possible. original image as closely as possible.
    original image as closely as possible.

    And to do that all I do is I I create a And to do that all I do is I I create
    a And to do that all I do is I I create a

    mean square error loss between the mean square error loss between the mean square
    error loss between the

    predicted noise and the actual noise. predicted noise and the actual noise. predicted
    noise and the actual noise.

    And you might be wondering why am I And you might be wondering why am I And you
    might be wondering why am I

    sampling a random time step here. The sampling a random time step here. The sampling
    a random time step here. The

    reason this random reason this random reason this random

    time step is sampled is because every time step is sampled is because every time
    step is sampled is because every

    time you''re going through this loop, time you''re going through this loop, time
    you''re going through this loop,

    you''re sampling something different. you''re sampling something different. you''re
    sampling something different.

    So sometimes you might pick 100, So sometimes you might pick 100, So sometimes
    you might pick 100,

    sometimes you might pick 500, sometimes sometimes you might pick 500, sometimes
    sometimes you might pick 500, sometimes

    you might pick 600. you might pick 600. you might pick 600.

    So eventually in this process the model So eventually in this process the model
    So eventually in this process the model

    learns that okay uh given learns that okay uh given learns that okay uh given

    whichever step I am at in the reverse whichever step I am at in the reverse whichever
    step I am at in the reverse

    diffusion process I can successfully diffusion process I can successfully diffusion
    process I can successfully

    generate my original image by generate my original image by generate my original
    image by

    subtracting an appropriate level of subtracting an appropriate level of'
  concept_slugs:
  - ddpm
  - epsilon-prediction
  - simple-loss-objective
- idx: 35
  start_sec: 2241.92
  end_sec: 2297.27
  text: 'subtracting an appropriate level of

    noise from that image. So it is it it noise from that image. So it is it it noise
    from that image. So it is it it

    becomes more robust to becomes more robust to becomes more robust to

    the different time steps. So let''s say the different time steps. So let''s say
    the different time steps. So let''s say

    we are converting back from noise to the we are converting back from noise to
    the we are converting back from noise to the

    actual data and I''m somewhere in the actual data and I''m somewhere in the actual
    data and I''m somewhere in the

    middle. So from that point if you want middle. So from that point if you want
    middle. So from that point if you want

    to go back you need to be sure how much to go back you need to be sure how much
    to go back you need to be sure how much

    noise I need to subtract from that noise I need to subtract from that noise I
    need to subtract from that

    point. That is why this this time step point. That is why this this time step
    point. That is why this this time step

    values values values

    are selected randomly. They they keep are selected randomly. They they keep are
    selected randomly. They they keep

    varying as you go through uh these steps varying as you go through uh these steps
    varying as you go through uh these steps

    and these epochs. and these epochs. and these epochs.

    And then uh these are some standard And then uh these are some standard And then
    uh these are some standard

    loss.backward backward which is the loss.backward backward which is the loss.backward
    backward which is the

    backward propagation and then we take a backward propagation and then we take
    a backward propagation and then we take a

    step using the optimizer and optimize step using the optimizer and optimize step
    using the optimizer and optimize

    the loss. the loss. the loss.

    So you can see here the loss uh nicely So you can see here the loss uh nicely
    So you can see here the loss uh nicely

    drops down and uh here the noise drops down and uh here the noise drops down and
    uh here the noise

    prediction shape is like this 40x3x'
  concept_slugs:
  - ddpm
  - epsilon-prediction
  - simple-loss-objective
- idx: 36
  start_sec: 2297.27
  end_sec: 2368.079
  text: 'prediction shape is like this 40x3x prediction shape is like this 40x3x

    32x 32 and uh here 32x 32 and uh here 32x 32 and uh here

    32x 32 is because it''s the pixel size 32x 32 is because it''s the pixel size
    32x 32 is because it''s the pixel size

    and three is the number of channels and three is the number of channels and three
    is the number of channels

    which is RGB which is RGB which is RGB

    and I think 40 comes up because I''m and I think 40 comes up because I''m and
    I think 40 comes up because I''m

    using a batch size of uh 40. Let''s try using a batch size of uh 40. Let''s try
    using a batch size of uh 40. Let''s try

    to understand where the number 40 to understand where the number 40 to understand
    where the number 40

    actually comes from. Yeah, this is interesting. This this Yeah, this is interesting.
    This this

    should have been uh 64 actually because should have been uh 64 actually because
    should have been uh 64 actually because

    the batch size which I''m using is 64. the batch size which I''m using is 64.
    the batch size which I''m using is 64.

    Let''s see. So the batch size is 64 but I get a So the batch size is 64 but I
    get a

    tensor which has a value of uh tensor which has a value of uh tensor which has
    a value of uh

    the first the first the first

    uh number which I see over here is 40 uh number which I see over here is 40 uh
    number which I see over here is 40

    which is interesting. Uh I will I will which is interesting. Uh I will I will
    which is interesting. Uh I will I will

    figure this out. If anyone manages to figure this out. If anyone manages to figure
    this out. If anyone manages to

    figure it out please post in the uh the figure it out please post in the uh the
    figure it out please post in the uh the

    the comments below. So this is how you the comments below. So this is how you
    the comments below. So this is how you

    see the plots gradually varying. The see the plots gradually varying. The'
  concept_slugs:
  - ddpm
  - epsilon-prediction
  - simple-loss-objective
- idx: 37
  start_sec: 2368.079
  end_sec: 2418.15
  text: 'see the plots gradually varying. The

    loss decreases with time which is loss decreases with time which is loss decreases
    with time which is

    exactly what we expect. exactly what we expect. exactly what we expect.

    And then finally you can And then finally you can And then finally you can

    uh sample from your output and generate uh sample from your output and generate
    uh sample from your output and generate

    images. Now option two is where we write images. Now option two is where we write
    images. Now option two is where we write

    the sampling loop which is important for the sampling loop which is important
    for the sampling loop which is important for

    our consideration. our consideration. our consideration.

    In the sampling loop what we do is we In the sampling loop what we do is we In
    the sampling loop what we do is we

    begin with a noise level which is random begin with a noise level which is random
    begin with a noise level which is random

    and we run through the scheduleuler from and we run through the scheduleuler from
    and we run through the scheduleuler from

    time steps from most to least noisy and time steps from most to least noisy and
    time steps from most to least noisy and

    we remove a small amount of noise each we remove a small amount of noise each
    we remove a small amount of noise each

    step based on the model prediction. step based on the model prediction. step based
    on the model prediction.

    So So

    this is the residual which is at every this is the residual which is at every
    this is the residual which is at every

    time step which I am at. How much noise time step which I am at. How much noise
    time step which I am at. How much noise

    do I need to remove from the model do I need to remove from the model do I need
    to remove from the model

    and then you update the sample with that and then you update the sample with that
    and then you update the sample with that

    much noise. This is probably going to much noise. This is probably going to much
    noise. This is probably going to

    have a negative value and you go to the'
  concept_slugs:
  - ddpm
  - epsilon-prediction
  - simple-loss-objective
- idx: 38
  start_sec: 2418.15
  end_sec: 2462.64
  text: 'have a negative value and you go to the have a negative value and you go
    to the

    previous sample. Then then you again previous sample. Then then you again previous
    sample. Then then you again

    find the residual. Then you again go to find the residual. Then you again go to
    find the residual. Then you again go to

    the previous image. So you you start the previous image. So you you start the
    previous image. So you you start

    with noise and you go to previous with noise and you go to previous with noise
    and you go to previous

    images. And this you do eight times images. And this you do eight times images.
    And this you do eight times

    because you start with eight images because you start with eight images because
    you start with eight images

    which are completely noise and then you which are completely noise and then you
    which are completely noise and then you

    slowly den noiseise them and you reach slowly den noiseise them and you reach
    slowly den noiseise them and you reach

    towards the original image. towards the original image. towards the original image.

    So this is how the diffusion process So this is how the diffusion process So this
    is how the diffusion process

    actually works in practice. I want you actually works in practice. I want you
    actually works in practice. I want you

    to practice uh tweaking the unit model to practice uh tweaking the unit model
    to practice uh tweaking the unit model

    understanding exactly what it takes as understanding exactly what it takes as
    understanding exactly what it takes as

    an input what it gives as an output the an input what it gives as an output the
    an input what it gives as an output the

    dimensions of the output of the model. dimensions of the output of the model.
    dimensions of the output of the model.

    Once you understand this, you will get Once you understand this, you will get
    Once you understand this, you will get

    much more confident in the theory behind much more confident in the theory behind
    much more confident in the theory behind

    DDPM. And if the mathematics has DDPM. And if the mathematics has DDPM. And if
    the mathematics has

    slightly overwhelmed you, don''t worry. slightly overwhelmed you, don''t worry.'
  concept_slugs:
  - ddpm
  - epsilon-prediction
  - simple-loss-objective
- idx: 39
  start_sec: 2462.64
  end_sec: 2502.68
  text: 'slightly overwhelmed you, don''t worry.

    You can focus on this practical side of You can focus on this practical side of
    You can focus on this practical side of

    the things more so that you get a more the things more so that you get a more
    the things more so that you get a more

    deeper understanding of the concepts. deeper understanding of the concepts. deeper
    understanding of the concepts.

    Thank you very much everyone and uh I''m Thank you very much everyone and uh I''m
    Thank you very much everyone and uh I''m

    very interested to I was very uh excited very interested to I was very uh excited
    very interested to I was very uh excited

    to talk about this lecture with all of to talk about this lecture with all of
    to talk about this lecture with all of

    you because I really believe that you because I really believe that you because
    I really believe that

    practical should be supplemented with practical should be supplemented with practical
    should be supplemented with

    theory at least for some critical topic theory at least for some critical topic
    theory at least for some critical topic

    so that you develop a very nice so that you develop a very nice so that you develop
    a very nice

    understanding of that topic. Thanks understanding of that topic. Thanks understanding
    of that topic. Thanks

    everyone and I''ll see you in the next everyone and I''ll see you in the next
    everyone and I''ll see you in the next

    lecture where we will discuss a lecture where we will discuss a lecture where
    we will discuss a

    completely new framework called energy completely new framework called energy
    completely new framework called energy

    based models and we will see how this based models and we will see how this based
    models and we will see how this

    framework very nicely merges with the framework very nicely merges with the framework
    very nicely merges with the

    framework of diffusion.'
  concept_slugs:
  - ddpm
  - epsilon-prediction
  - simple-loss-objective
---
# Lecture 4 - Diffusion Models Practical | DDPM | Principles of Diffusion Models

See the structured chunks above.
