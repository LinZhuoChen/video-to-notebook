---
course_slug: diffusion-principles-vizuara
idx: 6
title: Lecture 5 - Energy Based Models | Score Function | Principles of Diffusion
  Models
video_url: https://www.youtube.com/watch?v=zRyD7GQ9RHs
duration_sec: null
chunks:
- idx: 0
  start_sec: 4.309
  end_sec: 75.68
  text: 'Hello everyone and welcome to this next Hello everyone and welcome to this
    next

    lecture in of the course principles of lecture in of the course principles of
    lecture in of the course principles of

    diffusion models. diffusion models. diffusion models.

    Firstly before we get started let us Firstly before we get started let us Firstly
    before we get started let us

    quickly recap what all things we have quickly recap what all things we have quickly
    recap what all things we have

    done in this course so far. done in this course so far. done in this course so
    far.

    We started off with We started off with We started off with

    deep generative models. We looked at these kind of models try to We looked at
    these kind of models try to

    predict the true distribution predict the true distribution predict the true distribution

    uh which governs the underlying data uh which governs the underlying data uh which
    governs the underlying data

    and uh we also looked at and uh we also looked at and uh we also looked at

    we do not have access to the true we do not have access to the true we do not
    have access to the true

    distribution. The only thing we have distribution. The only thing we have distribution.
    The only thing we have

    access to is samples from the data. And access to is samples from the data. And
    access to is samples from the data. And

    given the data samples, our objective is given the data samples, our objective
    is given the data samples, our objective is

    to predict the true distribution which to predict the true distribution which
    to predict the true distribution which

    governs this governs this governs this

    data distribution. data distribution. data distribution.

    And uh to do that, let''s say the true And uh to do that, let''s say the true
    And uh to do that, let''s say the true

    distribution is given by P data of X. distribution is given by P data of X. distribution
    is given by P data of X.

    People generally use a neural network to People generally use a neural network
    to People generally use a neural network to

    approximate this two distribution as P5 approximate this two distribution as P5
    approximate this two distribution as P5

    of X. of X.'
  concept_slugs:
  - langevin-dynamics
  - score-function
- idx: 1
  start_sec: 75.68
  end_sec: 150.48
  text: 'of X.

    And our objective then becomes to And our objective then becomes to And our objective
    then becomes to

    determine determine determine

    the probability distribution P5 of X the probability distribution P5 of X the
    probability distribution P5 of X

    over here. over here. over here.

    Okay. Now what are the different methods Okay. Now what are the different methods
    Okay. Now what are the different methods

    which we will use to determine this which we will use to determine this which
    we will use to determine this

    probability distribution. probability distribution. probability distribution.

    And uh the first several lectures are And uh the first several lectures are And
    uh the first several lectures are

    going to be focused on going to be focused on going to be focused on

    these techniques. And the first these techniques. And the first these techniques.
    And the first

    technique that we looked at which is technique that we looked at which is technique
    that we looked at which is

    used to predict the probability used to predict the probability used to predict
    the probability

    distribution of the underlying data distribution of the underlying data distribution
    of the underlying data

    uh is called as variational uh is called as variational uh is called as variational

    autoenccoders or VAEs. In variation autoenccoders, what we do In variation autoenccoders,
    what we do

    is we first convert the data is we first convert the data is we first convert
    the data

    from real space to a latin space from real space to a latin space from real space
    to a latin space

    and then we convert it back to the real and then we convert it back to the real
    and then we convert it back to the real

    space. So the typical architecture of the VA So the typical architecture of the
    VA

    looks like this looks like this looks like this

    and uh the the first part is called as and uh the the first part is called as
    and uh the the first part is called as

    the encoder over here and the second the encoder over here and the second the
    encoder over here and the second

    part is called as the decoder. part is called as the decoder. part is called as
    the decoder.

    The objective is to match the output The objective is to match the output'
  concept_slugs:
  - langevin-dynamics
  - score-function
- idx: 2
  start_sec: 150.48
  end_sec: 226.39
  text: 'The objective is to match the output

    image with the input image as close as image with the input image as close as
    image with the input image as close as

    possible. possible. possible.

    And here we looked at there are two And here we looked at there are two And here
    we looked at there are two

    types of losses. The first loss is the types of losses. The first loss is the
    types of losses. The first loss is the

    reconstruction loss and the second loss is called as the and the second loss is
    called as the

    regularization loss. The practical example that we looked at The practical example
    that we looked at

    for understanding VAS is that of for understanding VAS is that of for understanding
    VAS is that of

    handwritten digits. handwritten digits. handwritten digits.

    So for handwritten digits, our objective So for handwritten digits, our objective
    So for handwritten digits, our objective

    was to feed in several data samples of was to feed in several data samples of
    was to feed in several data samples of

    handwritten uh digits and we wanted our handwritten uh digits and we wanted our
    handwritten uh digits and we wanted our

    VA to predict VA to predict VA to predict

    first of all first of all first of all

    predict this underlying data predict this underlying data predict this underlying
    data

    distribution and after you predict you distribution and after you predict you
    distribution and after you predict you

    can also sample from uh the probability can also sample from uh the probability
    can also sample from uh the probability

    distribution. distribution. distribution.

    One of the main drawbacks of VAS we One of the main drawbacks of VAS we One of
    the main drawbacks of VAS we

    understood is that it produces outputs understood is that it produces outputs
    understood is that it produces outputs

    which are blurry which are blurry which are blurry

    and it requires training of both these and it requires training of both these
    and it requires training of both these

    neural networks parallelly neural networks parallelly neural networks parallelly

    which is computationally intensive. So VAS were the first class of methods So
    VAS were the first class of methods

    which could show that artificial which could show that artificial which could
    show that artificial

    intelligence can be used to produce'
  concept_slugs:
  - langevin-dynamics
  - score-function
- idx: 3
  start_sec: 226.39
  end_sec: 282.72
  text: 'intelligence can be used to produce intelligence can be used to produce

    images which look like they belong to images which look like they belong to images
    which look like they belong to

    the underlying data distribution. the underlying data distribution. the underlying
    data distribution.

    Okay. Now we proceeded ahead from VAS Okay. Now we proceeded ahead from VAS Okay.
    Now we proceeded ahead from VAS

    and we moved to this topic called as and we moved to this topic called as and
    we moved to this topic called as

    diffusion. Now diffusion was a very interesting Now diffusion was a very interesting

    topic because we started with a very topic because we started with a very topic
    because we started with a very

    nice intuition about diffusion that if nice intuition about diffusion that if
    nice intuition about diffusion that if

    you spray a perfume in one corner of the you spray a perfume in one corner of
    the you spray a perfume in one corner of the

    room the molecules are going to diffuse room the molecules are going to diffuse
    room the molecules are going to diffuse

    out throughout the room. So the smell is out throughout the room. So the smell
    is out throughout the room. So the smell is

    going to percolate from one corner of going to percolate from one corner of going
    to percolate from one corner of

    the room to another corner of the room. the room to another corner of the room.
    the room to another corner of the room.

    This is the concept of diffusion and This is the concept of diffusion and This
    is the concept of diffusion and

    there are two main pillars which kind of there are two main pillars which kind
    of there are two main pillars which kind of

    govern this concept. The first is that govern this concept. The first is that
    govern this concept. The first is that

    the distribution becomes uniform and uh the distribution becomes uniform and uh
    the distribution becomes uniform and uh

    all you have is noise at the end. The all you have is noise at the end. The all
    you have is noise at the end. The

    original structure slowly disappears and original structure slowly disappears
    and original structure slowly disappears and

    it becomes uniform. it becomes uniform.'
  concept_slugs:
  - langevin-dynamics
  - score-function
- idx: 4
  start_sec: 282.72
  end_sec: 349.36
  text: 'it becomes uniform.

    We took these key ideas and we We took these key ideas and we We took these key
    ideas and we

    constructed a diffusion model which is constructed a diffusion model which is
    constructed a diffusion model which is

    inspired from the variational inspired from the variational inspired from the
    variational

    autoenccoder. autoenccoder. autoenccoder.

    Now how do we construct something that Now how do we construct something that
    Now how do we construct something that

    is inspired from the variation is inspired from the variation is inspired from
    the variation

    autoenccoder? First of all you replace autoenccoder? First of all you replace
    autoenccoder? First of all you replace

    encoder by something which is let''s say encoder by something which is let''s
    say encoder by something which is let''s say

    called a diffuser. called a diffuser. called a diffuser.

    That is it takes an input data. Let''s That is it takes an input data. Let''s
    That is it takes an input data. Let''s

    say we take an image of a house say we take an image of a house say we take an
    image of a house

    and in a series of steps it gradually and in a series of steps it gradually and
    in a series of steps it gradually

    corrupts the input data. It adds noise corrupts the input data. It adds noise
    corrupts the input data. It adds noise

    in each of these step and finally what in each of these step and finally what
    in each of these step and finally what

    we get is complete noise. So this is called as the forward So this is called as
    the forward

    process. We looked at exactly how this noise is We looked at exactly how this
    noise is

    is injected. What is the mathematical is injected. What is the mathematical is
    injected. What is the mathematical

    formulation of this noise and how you formulation of this noise and how you formulation
    of this noise and how you

    can convert any image to something where can convert any image to something where
    can convert any image to something where

    the structure slowly disappears and it the structure slowly disappears and it
    the structure slowly disappears and it

    becomes uniform. becomes uniform. becomes uniform.

    So you inject noise at every transition. So you inject noise at every transition.'
  concept_slugs:
  - langevin-dynamics
  - score-function
- idx: 5
  start_sec: 349.36
  end_sec: 405.27
  text: 'So you inject noise at every transition.

    So this is the first transition, second, So this is the first transition, second,
    So this is the first transition, second,

    third etc. third etc. third etc.

    Now this is the encoder which is fixed. Now this is the encoder which is fixed.
    Now this is the encoder which is fixed.

    This is very different from the This is very different from the This is very different
    from the

    variational autoenccoder where we learn variational autoenccoder where we learn
    variational autoenccoder where we learn

    the parameters of the encoder and the the parameters of the encoder and the the
    parameters of the encoder and the

    decoder. But in this case the encoder decoder. But in this case the encoder decoder.
    But in this case the encoder

    parameters are completely fixed. parameters are completely fixed. parameters are
    completely fixed.

    Now the next process is that of the Now the next process is that of the Now the
    next process is that of the

    decoder. So you need to take the noise decoder. So you need to take the noise
    decoder. So you need to take the noise

    and produce the given image from the and produce the given image from the and
    produce the given image from the

    noise. noise. noise.

    Now this itself looks like it is a bit Now this itself looks like it is a bit
    Now this itself looks like it is a bit

    challenging but we realize that the challenging but we realize that the challenging
    but we realize that the

    final formula final formula final formula

    in this diffusion model comes to a very in this diffusion model comes to a very
    in this diffusion model comes to a very

    simple concept. Let''s say the noise that simple concept. Let''s say the noise
    that simple concept. Let''s say the noise that

    we have injected is epsilon and in the we have injected is epsilon and in the
    we have injected is epsilon and in the

    reverse process we are trying to predict reverse process we are trying to predict
    reverse process we are trying to predict

    the noise through our neural network the noise through our neural network the
    noise through our neural network

    which is epsilon hat. which is epsilon hat. which is epsilon hat.

    So our objective is to minimize the mean'
  concept_slugs:
  - langevin-dynamics
  - score-function
- idx: 6
  start_sec: 405.27
  end_sec: 461.36
  text: 'So our objective is to minimize the mean So our objective is to minimize
    the mean

    square error between epsilon and epsilon square error between epsilon and epsilon
    square error between epsilon and epsilon

    hat for all these different points in the for all these different points in the

    transition process. For example, if we transition process. For example, if we
    transition process. For example, if we

    take this transition and we ask the take this transition and we ask the take this
    transition and we ask the

    question that for this image, if I want question that for this image, if I want
    question that for this image, if I want

    to reconstruct the original image, how to reconstruct the original image, how
    to reconstruct the original image, how

    much noise should I remove from this much noise should I remove from this much
    noise should I remove from this

    image? And the noise that you remove image? And the noise that you remove image?
    And the noise that you remove

    should match very close to the noise should match very close to the noise should
    match very close to the noise

    which is injected. So essentially this which is injected. So essentially this
    which is injected. So essentially this

    is also can be called as a noise is also can be called as a noise is also can
    be called as a noise

    predictor. And uh the reason this works is because And uh the reason this works
    is because

    let''s say you you consider any image in let''s say you you consider any image
    in let''s say you you consider any image in

    the world you apply the forward process. the world you apply the forward process.
    the world you apply the forward process.

    So every single image in the world can So every single image in the world can
    So every single image in the world can

    be represented as noise. And this is be represented as noise. And this is be represented
    as noise. And this is

    something which was quite interesting. something which was quite interesting.
    something which was quite interesting.

    We we asked the question that what is We we asked the question that what is We
    we asked the question that what is

    something which is common in every something which is common in every'
  concept_slugs:
  - langevin-dynamics
  - score-function
- idx: 7
  start_sec: 461.36
  end_sec: 516.479
  text: 'something which is common in every

    single image on earth. And at a first single image on earth. And at a first single
    image on earth. And at a first

    glance you''re not able to answer it glance you''re not able to answer it glance
    you''re not able to answer it

    because the images look so different. because the images look so different. because
    the images look so different.

    Right? A laptop looks different, a chair Right? A laptop looks different, a chair
    Right? A laptop looks different, a chair

    looks different. But every single image looks different. But every single image
    looks different. But every single image

    can be reconstructed back from noise if can be reconstructed back from noise if
    can be reconstructed back from noise if

    you know how much noise to remove you know how much noise to remove you know how
    much noise to remove

    at every step. So that finally you get at every step. So that finally you get
    at every step. So that finally you get

    the actual image. Now instead of the actual image. Now instead of the actual image.
    Now instead of

    removing noise in one single step, if we removing noise in one single step, if
    we removing noise in one single step, if we

    remove the noise step by step, we can remove the noise step by step, we can remove
    the noise step by step, we can

    have a granular access to the reverse have a granular access to the reverse have
    a granular access to the reverse

    transition process. transition process. transition process.

    And this granular access to the reverse And this granular access to the reverse
    And this granular access to the reverse

    transition process helps us to train the transition process helps us to train
    the transition process helps us to train the

    neural network properly. neural network properly. neural network properly.

    We looked at an example where we could We looked at an example where we could
    We looked at an example where we could

    generate these images very nicely and generate these images very nicely and generate
    these images very nicely and

    diffusion models were a big revolution diffusion models were a big revolution
    diffusion models were a big revolution

    in the field of image generation through in the field of image generation through'
  concept_slugs:
  - langevin-dynamics
  - score-function
- idx: 8
  start_sec: 516.479
  end_sec: 585.829
  text: 'in the field of image generation through

    generative AI. Models were extremely generative AI. Models were extremely generative
    AI. Models were extremely

    important in creating a new wave in the important in creating a new wave in the
    important in creating a new wave in the

    image generation process and uh it was image generation process and uh it was
    image generation process and uh it was

    something which offered a very credible something which offered a very credible
    something which offered a very credible

    alternative to variational alternative to variational alternative to variational

    autoenccoders. Uh okay. So having understood both Uh okay. So having understood
    both

    variational autoenccoders and diffusion variational autoenccoders and diffusion
    variational autoenccoders and diffusion

    models, we move to another important models, we move to another important models,
    we move to another important

    concept which as we will look at it will concept which as we will look at it will
    concept which as we will look at it will

    closely intersect with the diffusion closely intersect with the diffusion closely
    intersect with the diffusion

    framework. However, before looking at framework. However, before looking at framework.
    However, before looking at

    that inter uh that that intersection, we that inter uh that that intersection,
    we that inter uh that that intersection, we

    should first understand about the should first understand about the should first
    understand about the

    concept independently. concept independently. concept independently.

    So the concept uh or the framework that So the concept uh or the framework that
    So the concept uh or the framework that

    we are going to learn today is called as we are going to learn today is called
    as we are going to learn today is called as

    energy based models energy based models energy based models

    and initially we will look at an and initially we will look at an and initially
    we will look at an

    independent analysis of energy based independent analysis of energy based independent
    analysis of energy based

    models and finally we will look at in in models and finally we will look at in
    in models and finally we will look at in in

    in detail how energy based models in detail how energy based models in detail
    how energy based models

    combine very nicely with diffusion combine very nicely with diffusion combine
    very nicely with diffusion

    models in a single cohesive framework.'
  concept_slugs:
  - langevin-dynamics
  - score-function
- idx: 9
  start_sec: 585.829
  end_sec: 648.55
  text: 'models in a single cohesive framework. models in a single cohesive framework.

    So this is something which is very So this is something which is very So this
    is something which is very

    unique and and very different to what unique and and very different to what unique
    and and very different to what

    people in the field of a IML are people in the field of a IML are people in the
    field of a IML are

    generally used to. We don''t really work generally used to. We don''t really work
    generally used to. We don''t really work

    with energy based models that much. with energy based models that much. with energy
    based models that much.

    However, it is very important to However, it is very important to However, it
    is very important to

    understand the evolution of this thread. understand the evolution of this thread.
    understand the evolution of this thread.

    uh and when we understand the evolution uh and when we understand the evolution
    uh and when we understand the evolution

    of this thread properly, we will truly of this thread properly, we will truly
    of this thread properly, we will truly

    be be able to understand be be able to understand be be able to understand

    uh uh uh

    this the current state-of-the-art this the current state-of-the-art this the current
    state-of-the-art

    diffusion models and appreciate them as diffusion models and appreciate them as
    diffusion models and appreciate them as

    well. well. well.

    Okay. So, at the heart of energy based Okay. So, at the heart of energy based
    Okay. So, at the heart of energy based

    models models models

    is modeling probability distributions is modeling probability distributions is
    modeling probability distributions

    using energy functions. using energy functions. using energy functions.

    Remember our objective is to predict the Remember our objective is to predict
    the Remember our objective is to predict the

    probability distribution which matches probability distribution which matches
    probability distribution which matches

    as close as possible to the true data as close as possible to the true data as
    close as possible to the true data

    distribution. So let us denote the distribution. So let us denote the distribution.
    So let us denote the

    probability distribution that we are probability distribution that we are probability
    distribution that we are

    predicting as P5. predicting as P5. predicting as P5.

    So in the energy based models our'
  concept_slugs:
  - langevin-dynamics
  - score-function
- idx: 10
  start_sec: 648.55
  end_sec: 717.279
  text: 'So in the energy based models our So in the energy based models our

    objective is to predict P5 of X using objective is to predict P5 of X using objective
    is to predict P5 of X using

    energy functions. energy functions. energy functions.

    Now what exactly is this energy Now what exactly is this energy Now what exactly
    is this energy

    function? Let''s let''s try to understand function? Let''s let''s try to understand
    function? Let''s let''s try to understand

    it. it. it.

    Let this X Let this X Let this X

    be a data point be a data point be a data point

    and the energy function for X is defined and the energy function for X is defined
    and the energy function for X is defined

    as E5 of X. So let''s let''s take a So let''s let''s take a

    simple example where x which is your simple example where x which is your simple
    example where x which is your

    data points they take values from minus4 data points they take values from minus4
    data points they take values from minus4

    to +4 to +4 to +4

    and the energy functions which is and the energy functions which is and the energy
    functions which is

    denoted as ei of x looks like this. denoted as ei of x looks like this. denoted
    as ei of x looks like this.

    It appears like a curve with a cusp at It appears like a curve with a cusp at
    It appears like a curve with a cusp at

    the bottom. the bottom. the bottom.

    Now at the first glance when I look at Now at the first glance when I look at
    Now at the first glance when I look at

    this curve what strikes me is that there this curve what strikes me is that there
    this curve what strikes me is that there

    are two points which are at the minima are two points which are at the minima
    are two points which are at the minima

    of of this curve. of of this curve. of of this curve.

    So So So

    imagine that you take a ball and you imagine that you take a ball and you imagine
    that you take a ball and you

    drop this ball in this curve. drop this ball in this curve.'
  concept_slugs:
  - langevin-dynamics
  - score-function
- idx: 11
  start_sec: 717.279
  end_sec: 777.04
  text: 'drop this ball in this curve.

    What will happen is that the ball will What will happen is that the ball will
    What will happen is that the ball will

    slowly settle down, slowly fall down and slowly settle down, slowly fall down
    and slowly settle down, slowly fall down and

    settle into let''s say this configuration settle into let''s say this configuration
    settle into let''s say this configuration

    because it appears to be a valley. because it appears to be a valley. because
    it appears to be a valley.

    But if you push it even further, it will But if you push it even further, it will
    But if you push it even further, it will

    go ahead and it will fall into this go ahead and it will fall into this go ahead
    and it will fall into this

    valley. valley. valley.

    So the energy landscape has multiple So the energy landscape has multiple So the
    energy landscape has multiple

    valleys in this sample example that we valleys in this sample example that we
    valleys in this sample example that we

    have taken. have taken. have taken.

    But these valleys mean something very But these valleys mean something very But
    these valleys mean something very

    specific. specific. specific.

    So when we look at an energy landscape, So when we look at an energy landscape,
    So when we look at an energy landscape,

    the energies which are the minimum, the the energies which are the minimum, the
    the energies which are the minimum, the

    lowest energy configurations, lowest energy configurations, lowest energy configurations,

    these are the configurations which are these are the configurations which are
    these are the configurations which are

    the most preferable or preferred the most preferable or preferred the most preferable
    or preferred

    configurations. configurations. configurations.

    This is inspired from physics. Let''s say This is inspired from physics. Let''s
    say This is inspired from physics. Let''s say

    we take an apple and I take a apple and we take an apple and I take a apple and
    we take an apple and I take a apple and

    I drop it. So why does the apple come I drop it. So why does the apple come I
    drop it. So why does the apple come

    down and settle on the ground? The down and settle on the ground? The'
  concept_slugs:
  - langevin-dynamics
  - score-function
- idx: 12
  start_sec: 777.04
  end_sec: 835.59
  text: 'down and settle on the ground? The

    reason is that at on on on the ground reason is that at on on on the ground reason
    is that at on on on the ground

    the potential energy of the apple is is the potential energy of the apple is is
    the potential energy of the apple is is

    minimum. And we apply a very similar minimum. And we apply a very similar minimum.
    And we apply a very similar

    sort of a logic here for our data sort of a logic here for our data sort of a
    logic here for our data

    points. What we say is that if we are points. What we say is that if we are points.
    What we say is that if we are

    able to pinpoint the energy function for able to pinpoint the energy function
    for able to pinpoint the energy function for

    all the data points which are given to all the data points which are given to
    all the data points which are given to

    me, I can get a sense of how probable me, I can get a sense of how probable me,
    I can get a sense of how probable

    that each sample is. For example, that each sample is. For example, that each
    sample is. For example,

    here I can say that the probability of x here I can say that the probability of
    x here I can say that the probability of x

    = -4 = -4 = -4

    is much less than the probability of x = is much less than the probability of
    x = is much less than the probability of x =

    -1.5 -1.5 -1.5

    because the energy of this is because the energy of this is because the energy
    of this is

    considerably less compared to the energy considerably less compared to the energy
    considerably less compared to the energy

    of this. of this. of this.

    So the energy function becomes a proxy So the energy function becomes a proxy
    So the energy function becomes a proxy

    for us to comment about the preference for us to comment about the preference
    for us to comment about the preference

    or the probability of the actions. Okay, now that we have seen how the Okay, now
    that we have seen how the

    energy function can be a proxy for how'
  concept_slugs:
  - langevin-dynamics
  - score-function
- idx: 13
  start_sec: 835.59
  end_sec: 892.72
  text: 'energy function can be a proxy for how energy function can be a proxy for
    how

    probable that particular data point or probable that particular data point or
    probable that particular data point or

    sample is, let us dig even deeper. How sample is, let us dig even deeper. How
    sample is, let us dig even deeper. How

    do we convert this energy landscape into do we convert this energy landscape into
    do we convert this energy landscape into

    a set of probabilities? a set of probabilities? a set of probabilities?

    Okay, so first of all, the points which Okay, so first of all, the points which
    Okay, so first of all, the points which

    lower energy should have higher lower energy should have higher lower energy should
    have higher

    probability probability probability

    and the points with higher energy should and the points with higher energy should
    and the points with higher energy should

    have lower probability. This much we have lower probability. This much we have
    lower probability. This much we

    understand from the physical intuition understand from the physical intuition
    understand from the physical intuition

    that we just developed. So the that we just developed. So the that we just developed.
    So the

    probability curve should look something probability curve should look something
    probability curve should look something

    like this. Here it should have high like this. Here it should have high like this.
    Here it should have high

    values values values

    and here it should have high values. So and here it should have high values. So
    and here it should have high values. So

    something like this. something like this. something like this.

    So you can see that these are the exact So you can see that these are the exact
    So you can see that these are the exact

    same points which correspond to the same points which correspond to the same points
    which correspond to the

    energy minima. Now if you superimpose both these curves Now if you superimpose
    both these curves

    you you get something like this. you you get something like this. you you get
    something like this.

    Now the question is that uh we can of Now the question is that uh we can of Now
    the question is that uh we can of

    course draw this schematically and we course draw this schematically and we'
  concept_slugs:
  - langevin-dynamics
  - score-function
- idx: 14
  start_sec: 892.72
  end_sec: 951.189
  text: 'course draw this schematically and we

    can say that okay we want this energy or can say that okay we want this energy
    or can say that okay we want this energy or

    or this probability curve to follow or this probability curve to follow or this
    probability curve to follow

    these rules that it should be inversely these rules that it should be inversely
    these rules that it should be inversely

    proportional to the energy at at that proportional to the energy at at that proportional
    to the energy at at that

    point. But when we are trying to develop point. But when we are trying to develop
    point. But when we are trying to develop

    any framework we need to have the exact any framework we need to have the exact
    any framework we need to have the exact

    mathematical formulation for any mathematical formulation for any mathematical
    formulation for any

    transformation. So here the transformation. So here the transformation. So here
    the

    transformation is converting from energy transformation is converting from energy
    transformation is converting from energy

    to probability and you need to pinpoint to probability and you need to pinpoint
    to probability and you need to pinpoint

    exactly how you are going to exactly how you are going to exactly how you are
    going to

    complete this transformation. complete this transformation. complete this transformation.

    So let''s let''s try to understand can we So let''s let''s try to understand can
    we So let''s let''s try to understand can we

    think of a mathematical function which think of a mathematical function which
    think of a mathematical function which

    can take us from this energy curve to can take us from this energy curve to can
    take us from this energy curve to

    the probability curve. the probability curve. the probability curve.

    The function should have higher higher The function should have higher higher
    The function should have higher higher

    energy with for lower probabilities energy with for lower probabilities energy
    with for lower probabilities

    lower energy for higher probabilities lower energy for higher probabilities lower
    energy for higher probabilities

    and it should have only positive values. and it should have only positive values.
    and it should have only positive values.

    So these are the three criterias which So these are the three criterias which
    So these are the three criterias which

    my function should satisfy'
  concept_slugs:
  - langevin-dynamics
  - score-function
- idx: 15
  start_sec: 951.189
  end_sec: 1023.35
  text: 'my function should satisfy my function should satisfy

    and people use an exponential function and people use an exponential function
    and people use an exponential function

    to relate the energy to the probability to relate the energy to the probability
    to relate the energy to the probability

    because it satisfies all these pro all because it satisfies all these pro all
    because it satisfies all these pro all

    these properties. these properties. these properties.

    So here you can see I have taken a So here you can see I have taken a So here
    you can see I have taken a

    example of the exponential function e to example of the exponential function e
    to example of the exponential function e to

    minus x. minus x. minus x.

    So the value of this function at x=0 is So the value of this function at x=0 is
    So the value of this function at x=0 is

    1 and it gradually decreases as you 1 and it gradually decreases as you 1 and
    it gradually decreases as you

    increase the value of x. increase the value of x. increase the value of x.

    So for higher So for higher So for higher

    energy levels you can see the energy levels you can see the energy levels you
    can see the

    probability is minimum whereas for lower probability is minimum whereas for lower
    probability is minimum whereas for lower

    energy levels the probability is maximum energy levels the probability is maximum
    energy levels the probability is maximum

    and the probability value should lie and the probability value should lie and
    the probability value should lie

    between 0 and one. We should add this between 0 and one. We should add this between
    0 and one. We should add this

    this point also should lie between 0 and this point also should lie between 0
    and this point also should lie between 0 and

    one which also the exponential function one which also the exponential function
    one which also the exponential function

    very nicely satisfies. Okay. So this is the exponential curve Okay. So this is
    the exponential curve

    which we will use as the transformation which we will use as the transformation
    which we will use as the transformation

    from the energies to the probabilities. Now let''s say we denote the probability
    Now let''s say we denote the probability

    density as p5 of x.'
  concept_slugs:
  - langevin-dynamics
  - score-function
- idx: 16
  start_sec: 1023.35
  end_sec: 1076.559
  text: 'density as p5 of x. density as p5 of x.

    Then from the above graph we can find Then from the above graph we can find Then
    from the above graph we can find

    out a function which represents the out a function which represents the out a
    function which represents the

    uh uh

    energy and the probability relation. So energy and the probability relation. So
    energy and the probability relation. So

    let''s let''s try to understand this. So let''s let''s try to understand this.
    So let''s let''s try to understand this. So

    the probability is given as P5 of X and the probability is given as P5 of X and
    the probability is given as P5 of X and

    the energy is given as E5 of X. So this the energy is given as E5 of X. So this
    the energy is given as E5 of X. So this

    is how we relate the energy function to is how we relate the energy function to
    is how we relate the energy function to

    the probability. So now if you give me the probability. So now if you give me
    the probability. So now if you give me

    any value for the energy function, I can any value for the energy function, I
    can any value for the energy function, I can

    give you exactly what is the probability give you exactly what is the probability
    give you exactly what is the probability

    for that data sample for that data sample for that data sample

    u to be sampled from that from from the u to be sampled from that from from the
    u to be sampled from that from from the

    given distribution. given distribution. given distribution.

    Okay. So this is a great starting point. Okay. So this is a great starting point.
    Okay. So this is a great starting point.

    uh we have started with energy functions uh we have started with energy functions
    uh we have started with energy functions

    which derives its its intuition from which derives its its intuition from which
    derives its its intuition from

    physics. In physics if you look at any physics. In physics if you look at any
    physics. In physics if you look at any

    system u every system finally tries to system u every system finally tries to'
  concept_slugs:
  - langevin-dynamics
  - score-function
- idx: 17
  start_sec: 1076.559
  end_sec: 1126.16
  text: 'system u every system finally tries to

    go in a position with the minimum go in a position with the minimum go in a position
    with the minimum

    possible energy and this is something possible energy and this is something possible
    energy and this is something

    which is quite well known. People use it which is quite well known. People use
    it which is quite well known. People use it

    to derive formulas for the variation for to derive formulas for the variation
    for to derive formulas for the variation for

    different quantities. different quantities. different quantities.

    Now here we are going to use a very Now here we are going to use a very Now here
    we are going to use a very

    similar principle but we are going to similar principle but we are going to similar
    principle but we are going to

    use that principle to connect the use that principle to connect the use that principle
    to connect the

    energies to the probabilities of that energies to the probabilities of that energies
    to the probabilities of that

    individual data points. For example, if individual data points. For example, if
    individual data points. For example, if

    you give me 100 images of cats you give me 100 images of cats you give me 100
    images of cats

    and if you tell me pick one image and and if you tell me pick one image and and
    if you tell me pick one image and

    tell me what is the probability of tell me what is the probability of tell me
    what is the probability of

    finding this image finding this image finding this image

    in your given data set. Now to do that in your given data set. Now to do that
    in your given data set. Now to do that

    I''ll first look at okay what''s the I''ll first look at okay what''s the I''ll
    first look at okay what''s the

    energy function value for this image and energy function value for this image
    and energy function value for this image and

    then I''ll calculate the probability for then I''ll calculate the probability
    for then I''ll calculate the probability for

    that using the exponential curve that is that using the exponential curve that
    is that using the exponential curve that is

    the whole idea behind energy based the whole idea behind energy based'
  concept_slugs:
  - langevin-dynamics
  - score-function
- idx: 18
  start_sec: 1126.16
  end_sec: 1200.32
  text: 'the whole idea behind energy based

    models models

    okay now let us discuss after this point okay now let us discuss after this point
    okay now let us discuss after this point

    let''s take an example suppose we have a let''s take an example suppose we have
    a let''s take an example suppose we have a

    set of discrete states which are -3 -2 set of discrete states which are -3 -2
    set of discrete states which are -3 -2

    -1 0 1 2 and 3 let''s Say we have seven -1 0 1 2 and 3 let''s Say we have seven
    -1 0 1 2 and 3 let''s Say we have seven

    values. values. values.

    Okay. And now let us say that we use the Okay. And now let us say that we use
    the Okay. And now let us say that we use the

    above formula and we calculate the above formula and we calculate the above formula
    and we calculate the

    probability densities for all these probability densities for all these probability
    densities for all these

    states. Let''s say we know the energy states. Let''s say we know the energy states.
    Let''s say we know the energy

    values for all these states and then we values for all these states and then we
    values for all these states and then we

    calculate the probability densities. So calculate the probability densities. So
    calculate the probability densities. So

    the probability density for the probability density for the probability density
    for

    minus3 is here -2 -1 0 minus3 is here -2 -1 0 minus3 is here -2 -1 0

    1 2 and 3. 1 2 and 3. 1 2 and 3.

    Here I have used the formula probability Here I have used the formula probability
    Here I have used the formula probability

    of x = e minus e of x. The problem with this method is that the The problem with
    this method is that the

    probabilities do not add up to one. probabilities do not add up to one. probabilities
    do not add up to one.

    And why do we need the probability to And why do we need the probability to And
    why do we need the probability to

    add up to one? We need the probability add up to one? We need the probability'
  concept_slugs:
  - langevin-dynamics
  - score-function
- idx: 19
  start_sec: 1200.32
  end_sec: 1252.87
  text: 'add up to one? We need the probability

    to add up to one because if we are to add up to one because if we are to add up
    to one because if we are

    creating a lot of samples and we are creating a lot of samples and we are creating
    a lot of samples and we are

    creating a probability distribution for creating a probability distribution for
    creating a probability distribution for

    all those samples, all those samples, all those samples,

    the probability distribution should the probability distribution should the probability
    distribution should

    satisfy the addition of all satisfy the addition of all satisfy the addition of
    all

    probabilities to be one. Imagine you uh probabilities to be one. Imagine you uh
    probabilities to be one. Imagine you uh

    you have a coin and the coin has two you have a coin and the coin has two you
    have a coin and the coin has two

    faces. It can either faces. It can either faces. It can either

    come up as heads or it can come up as come up as heads or it can come up as come
    up as heads or it can come up as

    tails. So the probability for each side tails. So the probability for each side
    tails. So the probability for each side

    is 0.5 and.5. It adds up to one. Let''s is 0.5 and.5. It adds up to one. Let''s
    is 0.5 and.5. It adds up to one. Let''s

    take an example of a dice. The take an example of a dice. The take an example
    of a dice. The

    probability of rolling the dice and probability of rolling the dice and probability
    of rolling the dice and

    getting the number 1 is 1x 6. Similarly, getting the number 1 is 1x 6. Similarly,
    getting the number 1 is 1x 6. Similarly,

    getting the number 2 is 1x 6. If you add getting the number 2 is 1x 6. If you
    add getting the number 2 is 1x 6. If you add

    all these probabilities 1x 6 + 2x 6 + 3x all these probabilities 1x 6 + 2x 6 +
    3x all these probabilities 1x 6 + 2x 6 + 3x

    6 + 4x 6. 6 + 4x 6. 6 + 4x 6.

    Uh Uh Uh

    so let''s let''s take that example again.'
  concept_slugs:
  - langevin-dynamics
  - score-function
- idx: 20
  start_sec: 1252.87
  end_sec: 1302.549
  text: 'so let''s let''s take that example again. so let''s let''s take that example
    again.

    Uh let''s say you have a dice. Okay. Uh Uh let''s say you have a dice. Okay. Uh
    Uh let''s say you have a dice. Okay. Uh

    and and the probability of finding one and and the probability of finding one
    and and the probability of finding one

    is 1x 6. The probability of getting two is 1x 6. The probability of getting two
    is 1x 6. The probability of getting two

    is 1x 6. I think I made an error by is 1x 6. I think I made an error by is 1x
    6. I think I made an error by

    saying the probability is 2x 6. saying the probability is 2x 6. saying the probability
    is 2x 6.

    Similarly, the probability of getting Similarly, the probability of getting Similarly,
    the probability of getting

    the number six is 1x 6 and you add this the number six is 1x 6 and you add this
    the number six is 1x 6 and you add this

    up together you get the number one. So up together you get the number one. So
    up together you get the number one. So

    this is a very fundamental property this is a very fundamental property this is
    a very fundamental property

    which any probability distribution which any probability distribution which any
    probability distribution

    should satisfy and it doesn''t satisfy should satisfy and it doesn''t satisfy
    should satisfy and it doesn''t satisfy

    here in this case. The sum of all these here in this case. The sum of all these
    here in this case. The sum of all these

    probabilities is 25066. probabilities is 25066. probabilities is 25066.

    Now the question is that how do we Now the question is that how do we Now the
    question is that how do we

    convert this to a distribution which convert this to a distribution which convert
    this to a distribution which

    satisfies the addition of all these satisfies the addition of all these satisfies
    the addition of all these

    probabilities to be one. probabilities to be one. probabilities to be one.

    There is a very simple solution to this There is a very simple solution to this
    There is a very simple solution to this

    and the solution is that we can simply'
  concept_slugs:
  - langevin-dynamics
  - score-function
- idx: 21
  start_sec: 1302.549
  end_sec: 1368.87
  text: 'and the solution is that we can simply and the solution is that we can simply

    normalize the probabilities by dividing normalize the probabilities by dividing
    normalize the probabilities by dividing

    it by the summation of the weights. it by the summation of the weights. it by
    the summation of the weights.

    For example, For example, For example,

    here what I have done is I have taken here what I have done is I have taken here
    what I have done is I have taken

    these same values for all these discrete these same values for all these discrete
    these same values for all these discrete

    states but I have divided it by 25066. states but I have divided it by 25066.
    states but I have divided it by 25066.

    Here you can see in this formula the Here you can see in this formula the Here
    you can see in this formula the

    formula which I''m using is = e^ minus e5 formula which I''m using is = e^ minus
    e5 formula which I''m using is = e^ minus e5

    of x divided by 2.5066. Now if you sum up all these Now if you sum up all these

    probabilities they will definitely sum probabilities they will definitely sum
    probabilities they will definitely sum

    up to one. So our our requirement is is up to one. So our our requirement is is
    up to one. So our our requirement is is

    satisfied. satisfied. satisfied.

    So the number 2.566 is also called as So the number 2.566 is also called as So
    the number 2.566 is also called as

    the partition function. the partition function. the partition function.

    And the final relation between the And the final relation between the And the
    final relation between the

    energy and the probability density energy and the probability density energy and
    the probability density

    function then looks as follows. We are function then looks as follows. We are
    function then looks as follows. We are

    keeping the numerator intact exponential keeping the numerator intact exponential
    keeping the numerator intact exponential

    of minus e5 of x but we are dividing it of minus e5 of x but we are dividing it
    of minus e5 of x but we are dividing it

    by the partition function. by the partition function. by the partition function.

    So for the discrete states it looked'
  concept_slugs:
  - langevin-dynamics
  - score-function
- idx: 22
  start_sec: 1368.87
  end_sec: 1426.08
  text: 'So for the discrete states it looked So for the discrete states it looked

    like this summation of e ra to e5 of x like this summation of e ra to e5 of x
    like this summation of e ra to e5 of x

    x goes from let''s say -4 to 4. x goes from let''s say -4 to 4. x goes from let''s
    say -4 to 4.

    But if you have a continuous state then But if you have a continuous state then
    But if you have a continuous state then

    usually people represent this in the usually people represent this in the usually
    people represent this in the

    form of this integral symbol. form of this integral symbol. form of this integral
    symbol.

    And uh this is the partition function And uh this is the partition function And
    uh this is the partition function

    which represents the summation of which represents the summation of which represents
    the summation of

    all the exponentials in your data set. all the exponentials in your data set.
    all the exponentials in your data set.

    So this is what we want to predict. So this is what we want to predict. So this
    is what we want to predict.

    We want something which can we want the We want something which can we want the
    We want something which can we want the

    framework which can give us this p5 of x framework which can give us this p5 of
    x framework which can give us this p5 of x

    and uh this this looks great right we and uh this this looks great right we and
    uh this this looks great right we

    have expressed p5 of x in terms of the have expressed p5 of x in terms of the
    have expressed p5 of x in terms of the

    energy functions for all these discrete energy functions for all these discrete
    energy functions for all these discrete

    states or continuous states. Now the states or continuous states. Now the states
    or continuous states. Now the

    task boils down to how do we train these task boils down to how do we train these
    task boils down to how do we train these

    energy based models. In other words, how energy based models. In other words,
    how'
  concept_slugs:
  - langevin-dynamics
  - score-function
- idx: 23
  start_sec: 1426.08
  end_sec: 1498.47
  text: 'energy based models. In other words, how

    do we find these energy functions which do we find these energy functions which
    do we find these energy functions which

    correspond to each of these states? correspond to each of these states? correspond
    to each of these states?

    So that is the problem which we want to So that is the problem which we want to
    So that is the problem which we want to

    address in in this section. Okay. So conceptually we want to do Okay. So conceptually
    we want to do

    something like this. something like this.

    Let''s say Let''s say Let''s say

    you have on the x-axis you have your data samples which have been given your data
    samples which have been given

    to you and on the y-axis you have these to you and on the y-axis you have these
    to you and on the y-axis you have these

    probabilities. probabilities. probabilities.

    So this is the data which is good data So this is the data which is good data
    So this is the data which is good data

    which is drawn from your true which is drawn from your true which is drawn from
    your true

    probability distribution and this is the probability distribution and this is
    the probability distribution and this is the

    bad data. bad data. bad data.

    Now Now Now

    if this is my probability curve, what if this is my probability curve, what if
    this is my probability curve, what

    can I infer from this curve? can I infer from this curve? can I infer from this
    curve?

    The first thing I can infer is that the The first thing I can infer is that the
    The first thing I can infer is that the

    probability for good data probability for good data probability for good data

    is less than the probability for bad is less than the probability for bad is less
    than the probability for bad

    data, data, data,

    which is the opposite of what I want. which is the opposite of what I want. which
    is the opposite of what I want.

    Ideally, I want to push the bad data Ideally, I want to push the bad data Ideally,
    I want to push the bad data

    down, push the probability down, and down, push the probability down, and down,
    push the probability down, and

    push the good data up.'
  concept_slugs:
  - langevin-dynamics
  - score-function
- idx: 24
  start_sec: 1498.47
  end_sec: 1549.909
  text: 'push the good data up. push the good data up.

    So I want to move this curve like this. So I want to move this curve like this.
    So I want to move this curve like this.

    The left side I want to push down and The left side I want to push down and The
    left side I want to push down and

    the right side I want to push up. This the right side I want to push up. This
    the right side I want to push up. This

    is exactly what the training of energy is exactly what the training of energy
    is exactly what the training of energy

    based model achieves. Here you can see based model achieves. Here you can see
    based model achieves. Here you can see

    uh after the training is completed. uh after the training is completed. uh after
    the training is completed.

    This is the original curve and this is This is the original curve and this is
    This is the original curve and this is

    the curve which we have after the the curve which we have after the the curve
    which we have after the

    training is completed. training is completed. training is completed.

    So we can clearly see that the So we can clearly see that the So we can clearly
    see that the

    probability for the bad data has been probability for the bad data has been probability
    for the bad data has been

    reduced and the probability for the good reduced and the probability for the good
    reduced and the probability for the good

    data has been increased. data has been increased. data has been increased.

    So schematically this looks fine and So schematically this looks fine and So schematically
    this looks fine and

    theoretically this looks great that we theoretically this looks great that we
    theoretically this looks great that we

    start with the random energy start with the random energy start with the random
    energy

    configuration and slowly modify the configuration and slowly modify the configuration
    and slowly modify the

    energy landscape so that bad data have energy landscape so that bad data have
    energy landscape so that bad data have

    lower probability and the good data have lower probability and the good data have
    lower probability and the good data have

    higher probability. All of us understand'
  concept_slugs:
  - langevin-dynamics
  - score-function
- idx: 25
  start_sec: 1549.909
  end_sec: 1607.039
  text: 'higher probability. All of us understand higher probability. All of us understand

    this. this. this.

    Now we will again use the same Now we will again use the same Now we will again
    use the same

    formulation that we used for variational formulation that we used for variational
    formulation that we used for variational

    autoenccoders autoenccoders autoenccoders

    to to to

    understand the training of energy based understand the training of energy based
    understand the training of energy based

    models. Remember what we did with models. Remember what we did with models. Remember
    what we did with

    variational autoenccoders. We started variational autoenccoders. We started variational
    autoenccoders. We started

    out with maximizing this likelihood log out with maximizing this likelihood log
    out with maximizing this likelihood log

    of p5 of x. of p5 of x. of p5 of x.

    What this means is that What this means is that What this means is that

    if you take samples from the true if you take samples from the true if you take
    samples from the true

    distribution, let''s say the samples distribution, let''s say the samples distribution,
    let''s say the samples

    which are given to you and you put it in which are given to you and you put it
    in which are given to you and you put it in

    your predicted distribution, you should your predicted distribution, you should
    your predicted distribution, you should

    get higher probability. This is exactly get higher probability. This is exactly
    get higher probability. This is exactly

    what we are doing here. This is the good what we are doing here. This is the good
    what we are doing here. This is the good

    data which we are talking about. So we data which we are talking about. So we
    data which we are talking about. So we

    want to maximize this want to maximize this want to maximize this

    which means we want to maximize this. We which means we want to maximize this.
    We which means we want to maximize this. We

    are simply substituting the formula for are simply substituting the formula for
    are simply substituting the formula for

    the probability based on the energy the probability based on the energy the probability
    based on the energy

    functions. functions. functions.

    Uh here E5 of X denotes the energy Uh here E5 of X denotes the energy'
  concept_slugs:
  - langevin-dynamics
  - score-function
- idx: 26
  start_sec: 1607.039
  end_sec: 1680.559
  text: 'Uh here E5 of X denotes the energy

    function. Okay. So now if you break this down, Okay. So now if you break this
    down,

    this is the first term that you get. uh this is the first term that you get. uh
    this is the first term that you get. uh

    remember log of remember log of remember log of

    a by b is equal to log a a by b is equal to log a a by b is equal to log a

    minus log b. minus log b. minus log b.

    So this is the formula that I have used So this is the formula that I have used
    So this is the formula that I have used

    to uh make this simplification. Now once we reach this step we get to a Now once
    we reach this step we get to a

    stage where we have to calculate the log stage where we have to calculate the
    log stage where we have to calculate the log

    of this partition function which let''s of this partition function which let''s
    of this partition function which let''s

    call it zed. call it zed. call it zed.

    The biggest problem with this The biggest problem with this The biggest problem
    with this

    formulation is that the partition formulation is that the partition formulation
    is that the partition

    function is intractable. It is function is intractable. It is function is intractable.
    It is

    impossible to calculate the partition impossible to calculate the partition impossible
    to calculate the partition

    function. function. function.

    And in fact we have faced a very similar And in fact we have faced a very similar
    And in fact we have faced a very similar

    issue. Uh do you remember how we face issue. Uh do you remember how we face issue.
    Uh do you remember how we face

    this issue while training the this issue while training the this issue while training
    the

    variational autoenccoder? variational autoenccoder? variational autoenccoder?

    What we said was if you want to What we said was if you want to What we said was
    if you want to

    calculate this calculate this calculate this

    we want to maximize we want to maximize we want to maximize

    so p5 of x can be written as integral of so p5 of x can be written as integral
    of'
  concept_slugs:
  - langevin-dynamics
  - score-function
- idx: 27
  start_sec: 1680.559
  end_sec: 1740.08
  text: 'so p5 of x can be written as integral of

    p5 of x given z into p of z dz. p5 of x given z into p of z dz. p5 of x given
    z into p of z dz.

    And there we said that this integral is And there we said that this integral is
    And there we said that this integral is

    not possible to calculate. not possible to calculate. not possible to calculate.

    And uh what was the solution? How did we And uh what was the solution? How did
    we And uh what was the solution? How did we

    get over this? There was a very simple get over this? There was a very simple
    get over this? There was a very simple

    trick that we did. And uh the trick that trick that we did. And uh the trick that
    trick that we did. And uh the trick that

    we did was we defined an objective which we did was we defined an objective which
    we did was we defined an objective which

    is always lower than this maximum is always lower than this maximum is always
    lower than this maximum

    likelihood. likelihood. likelihood.

    And we call that objective as elbow. And we call that objective as elbow. And
    we call that objective as elbow.

    So instead of maximizing this which is So instead of maximizing this which is
    So instead of maximizing this which is

    non-tractable, we maximize the elbow non-tractable, we maximize the elbow non-tractable,
    we maximize the elbow

    which is tractable. And in energy based methods And in energy based methods

    we actually do not use the elbow term. we actually do not use the elbow term.
    we actually do not use the elbow term.

    We do not use the elbow approach We do not use the elbow approach We do not use
    the elbow approach

    but instead we introduce the notion of but instead we introduce the notion of
    but instead we introduce the notion of

    something called uh something called uh something called uh

    score function and we use a theory score function and we use a theory score function
    and we use a theory

    called score matching which completely called score matching which completely
    called score matching which completely

    bypasses the partition function. bypasses the partition function.'
  concept_slugs:
  - langevin-dynamics
  - score-function
- idx: 28
  start_sec: 1740.08
  end_sec: 1796.96
  text: 'bypasses the partition function.

    So you might be thinking that what is So you might be thinking that what is So
    you might be thinking that what is

    this new terminology which I''ve this new terminology which I''ve this new terminology
    which I''ve

    introduced. What is this core matching? introduced. What is this core matching?
    introduced. What is this core matching?

    It looks like we are It looks like we are It looks like we are

    defining a score function, right? But defining a score function, right? But defining
    a score function, right? But

    haven''t I already introduced the energy haven''t I already introduced the energy
    haven''t I already introduced the energy

    function? What does the score function function? What does the score function
    function? What does the score function

    even mean? even mean? even mean?

    So this is something which we will So this is something which we will So this
    is something which we will

    understand in the next section in this understand in the next section in this
    understand in the next section in this

    lecture. lecture. lecture.

    But as of now what we need to understand But as of now what we need to understand
    But as of now what we need to understand

    is to design the energy based models is to design the energy based models is to
    design the energy based models

    framework. We first find the relation framework. We first find the relation framework.
    We first find the relation

    between the energy and the probability between the energy and the probability
    between the energy and the probability

    that we have successfully done. Next we that we have successfully done. Next we
    that we have successfully done. Next we

    try to maximize the log likelihood of try to maximize the log likelihood of try
    to maximize the log likelihood of

    the data. the data. the data.

    But when we expand the term we encounter But when we expand the term we encounter
    But when we expand the term we encounter

    a term which a term which a term which

    includes the integral of the partition includes the integral of the partition
    includes the integral of the partition

    function which is impossible to function which is impossible to function which
    is impossible to

    calculate. calculate. calculate.

    And because of that we come up with a And because of that we come up with a'
  concept_slugs:
  - langevin-dynamics
  - score-function
- idx: 29
  start_sec: 1796.96
  end_sec: 1865.75
  text: 'And because of that we come up with a

    alternative objective function which alternative objective function which alternative
    objective function which

    uses something called as the score uses something called as the score uses something
    called as the score

    function. So let us understand what is function. So let us understand what is
    function. So let us understand what is

    this score function and uh this score function and uh this score function and
    uh

    how does it get rid of the partition how does it get rid of the partition how
    does it get rid of the partition

    function. function.

    Okay. So let''s look at it. Okay. So let''s look at it. Okay. So let''s look at
    it.

    Firstly, this this whole challenge of Firstly, this this whole challenge of Firstly,
    this this whole challenge of

    calculating an integral which is calculating an integral which is calculating
    an integral which is

    intractable and coming up with a intractable and coming up with a intractable
    and coming up with a

    solution. solution. solution.

    This has been a a common challenge in This has been a a common challenge in This
    has been a a common challenge in

    almost all the deep generative models almost all the deep generative models almost
    all the deep generative models

    and it and it and it

    uh it is mathematicians who help us to uh it is mathematicians who help us to
    uh it is mathematicians who help us to

    come out of this challenge and design an come out of this challenge and design
    an come out of this challenge and design an

    objective function which is tractable objective function which is tractable objective
    function which is tractable

    which which which

    clearly clearly clearly

    shows that mathematics is extremely shows that mathematics is extremely shows
    that mathematics is extremely

    important and it is the foundations important and it is the foundations important
    and it is the foundations

    behind all of these models for image generation that that we models for image
    generation that that we

    see around us. So whenever I look at see around us. So whenever I look at see
    around us. So whenever I look at

    this I I I have a deep sense of this I I I have a deep sense of this I I I have
    a deep sense of

    appreciation for people who actually sit'
  concept_slugs:
  - langevin-dynamics
  - score-function
- idx: 30
  start_sec: 1865.75
  end_sec: 1937.75
  text: 'appreciation for people who actually sit appreciation for people who actually
    sit

    down, they do the mathematics and they down, they do the mathematics and they
    down, they do the mathematics and they

    come up with these objective functions. come up with these objective functions.
    come up with these objective functions.

    Okay. So what is the score and how do we Okay. So what is the score and how do
    we Okay. So what is the score and how do we

    calculate the score? Let''s let''s try to calculate the score? Let''s let''s try
    to calculate the score? Let''s let''s try to

    understand that in detail. Okay. So for a density P of X, the score Okay. So for
    a density P of X, the score

    function has a formula which is given by function has a formula which is given
    by function has a formula which is given by

    gradient of the log of P of X. And this might be a bit difficult for us And this
    might be a bit difficult for us

    to understand because there are two to understand because there are two to understand
    because there are two

    terms involved here. There is a gradient terms involved here. There is a gradient
    terms involved here. There is a gradient

    term which is involved here and there is term which is involved here and there
    is term which is involved here and there is

    a log term which is involved here. a log term which is involved here. a log term
    which is involved here.

    But this score function actually means But this score function actually means
    But this score function actually means

    something very intuitive and that is why something very intuitive and that is
    why something very intuitive and that is why

    it is fun to work with. it is fun to work with. it is fun to work with.

    Intuitively the score forms a vector Intuitively the score forms a vector Intuitively
    the score forms a vector

    field that points towards regions of field that points towards regions of field
    that points towards regions of

    higher probability. So it gives a local higher probability. So it gives a local
    higher probability. So it gives a local

    guide to where the data is most likely guide to where the data is most likely
    guide to where the data is most likely

    to occur.'
  concept_slugs:
  - langevin-dynamics
  - score-function
- idx: 31
  start_sec: 1937.75
  end_sec: 1998.149
  text: 'to occur. to occur.

    Let''s let let''s take a sample example. Let''s let let''s take a sample example.
    Let''s let let''s take a sample example.

    Let us say these black dots these are Let us say these black dots these are Let
    us say these black dots these are

    your data samples. So the color uh the color orange So the color uh the color
    orange

    indicates that the probability of indicates that the probability of indicates
    that the probability of

    finding the samples is very high in this finding the samples is very high in this
    finding the samples is very high in this

    region and in this region. Now apart from this you see arrows all Now apart from
    this you see arrows all

    around the place. These arrows are the around the place. These arrows are the
    around the place. These arrows are the

    score function for every single point. score function for every single point.
    score function for every single point.

    For this point this is the score For this point this is the score For this point
    this is the score

    function. For this point this is the function. For this point this is the function.
    For this point this is the

    score function. And you can see that the score function. And you can see that
    the score function. And you can see that the

    score function is actually pointing us score function is actually pointing us
    score function is actually pointing us

    towards where the data is. Imagine you towards where the data is. Imagine you
    towards where the data is. Imagine you

    are moving out in the open sea and you are moving out in the open sea and you
    are moving out in the open sea and you

    want to find some sharks. And imagine want to find some sharks. And imagine want
    to find some sharks. And imagine

    you have a compass which points to the you have a compass which points to the
    you have a compass which points to the

    direction. Oh, there is the shark. I direction. Oh, there is the shark. I direction.
    Oh, there is the shark. I

    need to go there. This is exactly what need to go there. This is exactly what
    need to go there. This is exactly what

    score function does. It tells you the'
  concept_slugs:
  - langevin-dynamics
  - score-function
- idx: 32
  start_sec: 1998.149
  end_sec: 2049.119
  text: 'score function does. It tells you the score function does. It tells you the

    direction to where the data is located. direction to where the data is located.
    direction to where the data is located.

    So in a way it is incredibly useful, So in a way it is incredibly useful, So in
    a way it is incredibly useful,

    right? right? right?

    uh and we''ll we''ll try to use this score uh and we''ll we''ll try to use this
    score uh and we''ll we''ll try to use this score

    function to actually train our model. function to actually train our model. function
    to actually train our model.

    But this is the idea of score function. But this is the idea of score function.
    But this is the idea of score function.

    So in the above figure the arrows So in the above figure the arrows So in the
    above figure the arrows

    represent the score field which are represent the score field which are represent
    the score field which are

    pointed towards the direction where the pointed towards the direction where the
    pointed towards the direction where the

    density of the data is the maximum. density of the data is the maximum. density
    of the data is the maximum.

    And uh to imagine this happening for a And uh to imagine this happening for a
    And uh to imagine this happening for a

    bunch of let''s say we have images of bunch of let''s say we have images of bunch
    of let''s say we have images of

    cats and we find the score function for cats and we find the score function for
    cats and we find the score function for

    that. So the cat data itself is let''s that. So the cat data itself is let''s
    that. So the cat data itself is let''s

    say in 784 dimensions. say in 784 dimensions. say in 784 dimensions.

    So humans cannot even comprehend this So humans cannot even comprehend this So
    humans cannot even comprehend this

    right? We cannot imagine but intuitively right? We cannot imagine but intuitively
    right? We cannot imagine but intuitively

    we understand that at every point if we we understand that at every point if we
    we understand that at every point if we

    know where the data is where the score know where the data is where the score'
  concept_slugs:
  - langevin-dynamics
  - score-function
- idx: 33
  start_sec: 2049.119
  end_sec: 2098.64
  text: 'know where the data is where the score

    is the maximum is the maximum is the maximum

    we can start from any point and finally we can start from any point and finally
    we can start from any point and finally

    we will land up at the sample we will we will land up at the sample we will we
    will land up at the sample we will

    find the sample finally find the sample finally find the sample finally

    or we will find data points which are or we will find data points which are or
    we will find data points which are

    most likely to be sampled from the true most likely to be sampled from the true
    most likely to be sampled from the true

    probability distribution. probability distribution.

    So imagine that you are moving out in an So imagine that you are moving out in
    an So imagine that you are moving out in an

    open sea and uh you want to find these open sea and uh you want to find these
    open sea and uh you want to find these

    sharks right which are our data. So you sharks right which are our data. So you
    sharks right which are our data. So you

    move you find the score move in the move you find the score move in the move you
    find the score move in the

    direction again find the score and direction again find the score and direction
    again find the score and

    slowly you move and then you finally slowly you move and then you finally slowly
    you move and then you finally

    land up in an area where you find the land up in an area where you find the land
    up in an area where you find the

    actual sample. So for example, if I actual sample. So for example, if I actual
    sample. So for example, if I

    start here, I can slowly move towards start here, I can slowly move towards start
    here, I can slowly move towards

    the area where I find the samples. the area where I find the samples. the area
    where I find the samples.

    Now, but but how how do you move in this Now, but but how how do you move in this
    Now, but but how how do you move in this

    trajectory? trajectory?'
  concept_slugs:
  - langevin-dynamics
  - score-function
- idx: 34
  start_sec: 2098.64
  end_sec: 2158.069
  text: 'trajectory?

    Is is is it can I define it? Can I write Is is is it can I define it? Can I write
    Is is is it can I define it? Can I write

    an equation which can tell me how do I an equation which can tell me how do I
    an equation which can tell me how do I

    move in this trajectory? Let''s let''s try move in this trajectory? Let''s let''s
    try move in this trajectory? Let''s let''s try

    to unpack that as well in in this to unpack that as well in in this to unpack
    that as well in in this

    lecture. lecture.

    But before that, we will take uh the But before that, we will take uh the But
    before that, we will take uh the

    simplest example possible. simplest example possible. simplest example possible.

    Let''s assume that our probability Let''s assume that our probability Let''s assume
    that our probability

    density curve is the goshian. density curve is the goshian. density curve is the
    goshian.

    What does this mean? What does this mean? What does this mean?

    This means that the probability of x= This means that the probability of x= This
    means that the probability of x=

    to0 is the maximum and the probability to0 is the maximum and the probability
    to0 is the maximum and the probability

    dies off as you go towards the right or dies off as you go towards the right or
    dies off as you go towards the right or

    the left. This is the standard normal the left. This is the standard normal the
    left. This is the standard normal

    gshian distribution. We have seen this gshian distribution. We have seen this
    gshian distribution. We have seen this

    distribution in the distribution in the distribution in the

    forward transition process in the DDPM forward transition process in the DDPM
    forward transition process in the DDPM

    framework and also in the reverse framework and also in the reverse framework
    and also in the reverse

    transition process. transition process.

    Okay. So this is the standard normal Okay. So this is the standard normal Okay.
    So this is the standard normal

    distribution which is great. Now distribution which is great. Now distribution
    which is great. Now

    intuitively what do you expect? intuitively what do you expect? intuitively what
    do you expect?

    Let''s say I calculate the score for this'
  concept_slugs:
  - ddpm
  - langevin-dynamics
  - score-function
- idx: 35
  start_sec: 2158.069
  end_sec: 2213.599
  text: 'Let''s say I calculate the score for this Let''s say I calculate the score
    for this

    point. Where will this score point point. Where will this score point point. Where
    will this score point

    towards to this score will the score towards to this score will the score towards
    to this score will the score

    function for this point will be might be function for this point will be might
    be function for this point will be might be

    something like this. Right? because it something like this. Right? because it
    something like this. Right? because it

    points towards the center points towards the center points towards the center

    which has the maximum probability. which has the maximum probability. which has
    the maximum probability.

    Similarly, the score function for this Similarly, the score function for this
    Similarly, the score function for this

    data point data point data point

    would probably look something like this. would probably look something like this.
    would probably look something like this.

    It it points towards the data point It it points towards the data point It it
    points towards the data point

    which has the maximum probability which has the maximum probability which has
    the maximum probability

    and uh I I''ll probably get arrows which and uh I I''ll probably get arrows which
    and uh I I''ll probably get arrows which

    look like this. Remember this is just a look like this. Remember this is just
    a look like this. Remember this is just a

    one-dimensional data. So we have to plot one-dimensional data. So we have to plot
    one-dimensional data. So we have to plot

    our arrows on the x-axis. our arrows on the x-axis. our arrows on the x-axis.

    So let''s see. So the mathematical form So let''s see. So the mathematical form
    So let''s see. So the mathematical form

    for the probability looks like this. You can see that if you substitute x= You
    can see that if you substitute x=

    to0 here you will get maximum value 1x to0 here you will get maximum value 1x
    to0 here you will get maximum value 1x

    <unk>2 pi and as you move towards the <unk>2 pi and as you move towards the <unk>2
    pi and as you move towards the

    right or the left uh the value will right or the left uh the value will'
  concept_slugs:
  - langevin-dynamics
  - score-function
- idx: 36
  start_sec: 2213.599
  end_sec: 2275.68
  text: 'right or the left uh the value will

    decline at x= to infinity or minus decline at x= to infinity or minus decline
    at x= to infinity or minus

    infinity the value becomes zero. infinity the value becomes zero. infinity the
    value becomes zero.

    Now let us calculate the score function. Now let us calculate the score function.
    Now let us calculate the score function.

    uh remember the formula for score uh remember the formula for score uh remember
    the formula for score

    function was gradient of log of p of x. function was gradient of log of p of x.
    function was gradient of log of p of x.

    So let''s take the log of this. What is So let''s take the log of this. What is
    So let''s take the log of this. What is

    the log of this? Remember log of the log of this? Remember log of the log of this?
    Remember log of

    exponential e ra to any quantity let''s exponential e ra to any quantity let''s
    exponential e ra to any quantity let''s

    say p is equal to p itself. say p is equal to p itself. say p is equal to p itself.

    So if I take the log of this I will get So if I take the log of this I will get
    So if I take the log of this I will get

    and and log of and and log of and and log of

    a a a

    is equal to log a + log b. So first of all I do that I split this So first of
    all I do that I split this

    logarithm into two terms. This is term logarithm into two terms. This is term
    logarithm into two terms. This is term

    one and this is term two. one and this is term two. one and this is term two.

    Now this is just some constant log of Now this is just some constant log of Now
    this is just some constant log of

    some constant value some constant value some constant value

    and this is - x square by 2. and this is - x square by 2. and this is - x square
    by 2.

    Now this is just the first term. We have Now this is just the first term. We have'
  concept_slugs:
  - langevin-dynamics
  - score-function
- idx: 37
  start_sec: 2275.68
  end_sec: 2324.16
  text: 'Now this is just the first term. We have

    to take a gradient of this also. to take a gradient of this also. to take a gradient
    of this also.

    Gradient of a constant is zero and the Gradient of a constant is zero and the
    Gradient of a constant is zero and the

    gradient of this is minus x. gradient of this is minus x. gradient of this is
    minus x.

    So the score function that we get is So the score function that we get is So the
    score function that we get is

    simply minus x. Now what does this mean? simply minus x. Now what does this mean?
    simply minus x. Now what does this mean?

    This means that for x = +2 the score is This means that for x = +2 the score is
    This means that for x = +2 the score is

    minus2 which is exactly what we minus2 which is exactly what we minus2 which is
    exactly what we

    expected. At x= minus2 the score is +2 expected. At x= minus2 the score is +2
    expected. At x= minus2 the score is +2

    and the magnitude of the score increases and the magnitude of the score increases
    and the magnitude of the score increases

    as we move away from the mean. So if you as we move away from the mean. So if
    you as we move away from the mean. So if you

    are very far the score tells you that are very far the score tells you that are
    very far the score tells you that

    okay this is the direction of the data okay this is the direction of the data
    okay this is the direction of the data

    but the magnitude is also high which but the magnitude is also high which but
    the magnitude is also high which

    means that you are very far from the means that you are very far from the means
    that you are very far from the

    data. you need to go there with a higher data. you need to go there with a higher
    data. you need to go there with a higher

    magnitude. magnitude. magnitude.

    So uh this is what we get if we actually So uh this is what we get if we actually'
  concept_slugs:
  - langevin-dynamics
  - score-function
- idx: 38
  start_sec: 2324.16
  end_sec: 2381.349
  text: 'So uh this is what we get if we actually

    plot the score function. You can see plot the score function. You can see plot
    the score function. You can see

    that the arrows are pointed towards the that the arrows are pointed towards the
    that the arrows are pointed towards the

    direction where the probability for the direction where the probability for the
    direction where the probability for the

    data sample is the maximum and the data sample is the maximum and the data sample
    is the maximum and the

    magnitude of the arrows also increase as magnitude of the arrows also increase
    as magnitude of the arrows also increase as

    we go towards the left and right because we go towards the left and right because
    we go towards the left and right because

    the distance from the mean increases. So this is the idea of score function So
    this is the idea of score function

    and uh what it represents and uh what it represents and uh what it represents

    quite quite interesting uh in in my quite quite interesting uh in in my quite
    quite interesting uh in in my

    opinion I I think scores when I first opinion I I think scores when I first opinion
    I I think scores when I first

    looked at this in the literature for looked at this in the literature for looked
    at this in the literature for

    example I was reading the DDPM paper example I was reading the DDPM paper example
    I was reading the DDPM paper

    first and there they have very casually first and there they have very casually
    first and there they have very casually

    mentioned that mentioned that mentioned that

    uh you know I developed a framework uh you know I developed a framework uh you
    know I developed a framework

    where where where

    uh both the diffusion and this course uh both the diffusion and this course uh
    both the diffusion and this course

    can be unified from the lens of this can be unified from the lens of this can
    be unified from the lens of this

    same framework same framework same framework

    and at that time I was not aware of the and at that time I was not aware of the
    and at that time I was not aware of the

    score-based framework but'
  concept_slugs:
  - ddpm
  - langevin-dynamics
  - score-function
- idx: 39
  start_sec: 2381.349
  end_sec: 2440.96
  text: 'score-based framework but score-based framework but

    score-based methods score-based methods score-based methods

    is something which has come before is something which has come before is something
    which has come before

    diffusion models and in in the year the diffusion models and in in the year the
    diffusion models and in in the year the

    decade of 2010s itself. decade of 2010s itself. decade of 2010s itself.

    So there have been these two frameworks So there have been these two frameworks
    So there have been these two frameworks

    which have made parallel progress in the which have made parallel progress in
    the which have made parallel progress in the

    deep generative modeling and uh that is deep generative modeling and uh that is
    deep generative modeling and uh that is

    the score based approach and diffusion the score based approach and diffusion
    the score based approach and diffusion

    based approach. based approach. based approach.

    Okay. So uh in this example we can Okay. So uh in this example we can Okay. So
    uh in this example we can

    clearly see that all the points are clearly see that all the points are clearly
    see that all the points are

    pointed towards the center because the pointed towards the center because the
    pointed towards the center because the

    origin has the maximum probability origin has the maximum probability origin has
    the maximum probability

    density and the further you are away density and the further you are away density
    and the further you are away

    from the center the magnitude of the from the center the magnitude of the from
    the center the magnitude of the

    arrows increases because it will require arrows increases because it will require
    arrows increases because it will require

    more force to pull it to the center. Now the question is okay that is great Now
    the question is okay that is great

    but how does the score helps us in but how does the score helps us in but how
    does the score helps us in

    getting rid of the partition function. getting rid of the partition function.
    getting rid of the partition function.

    Remember that was one of the main Remember that was one of the main Remember that
    was one of the main

    challenges which we started out with. We challenges which we started out with.
    We'
  concept_slugs:
  - langevin-dynamics
  - score-function
- idx: 40
  start_sec: 2440.96
  end_sec: 2529.2
  text: 'challenges which we started out with. We

    wanted something which can uh help us wanted something which can uh help us wanted
    something which can uh help us

    offer a tractable alternative to offer a tractable alternative to offer a tractable
    alternative to

    calculate the maximum likelihood of the calculate the maximum likelihood of the
    calculate the maximum likelihood of the

    data. data. data.

    So let''s let''s understand that. So this uh subsection is titled freedom So this
    uh subsection is titled freedom

    from partition function. from partition function. from partition function.

    So we had seen before that calculating So we had seen before that calculating
    So we had seen before that calculating

    the partition function was intractable. the partition function was intractable.
    the partition function was intractable.

    It was difficult to calculate the It was difficult to calculate the It was difficult
    to calculate the

    partition function. partition function. partition function.

    Because of this we could not find an Because of this we could not find an Because
    of this we could not find an

    expression for maximizing the expression for maximizing the expression for maximizing
    the

    probability density likelihood. probability density likelihood. probability density
    likelihood.

    Now let''s see how this formulation Now let''s see how this formulation Now let''s
    see how this formulation

    changes. changes. changes.

    So I would like to actually prove this So I would like to actually prove this
    So I would like to actually prove this

    to see uh whether we are able to do to see uh whether we are able to do to see
    uh whether we are able to do

    this. So okay now the score is given by this. So okay now the score is given by
    this. So okay now the score is given by

    grad of log of p of x right log of a / b is log a minus log b. So it log of a
    / b is log a minus log b. So it

    is log of e^ - e5 of x minus log of integral of e to minus e5 minus log of integral
    of e to minus e5

    of x dx. Now this is simply minus ei of x and Now this is simply minus ei of x
    and

    this this remains same. Now what what happens is that when you'
  concept_slugs:
  - langevin-dynamics
  - score-function
- idx: 41
  start_sec: 2529.2
  end_sec: 2586.88
  text: 'Now what what happens is that when you

    take this gradient uh the the first term take this gradient uh the the first term
    take this gradient uh the the first term

    is minus grad of e5 of x which is simply is minus grad of e5 of x which is simply
    is minus grad of e5 of x which is simply

    the gradient of the energy function with the gradient of the energy function with
    the gradient of the energy function with

    a negative sign and this term actually a negative sign and this term actually
    a negative sign and this term actually

    cancels out to zero because because we cancels out to zero because because we
    cancels out to zero because because we

    are summing up over all the data are summing up over all the data are summing
    up over all the data

    samples. it ends up being a uh being a samples. it ends up being a uh being a
    samples. it ends up being a uh being a

    term or an expression which is term or an expression which is term or an expression
    which is

    independent of x and taking a derivative independent of x and taking a derivative
    independent of x and taking a derivative

    of this becomes zero because it is of this becomes zero because it is of this
    becomes zero because it is

    independent of x. So this is how we get independent of x. So this is how we get
    independent of x. So this is how we get

    rid of the partition function rid of the partition function rid of the partition
    function

    uh to calculate the score function. uh to calculate the score function. uh to
    calculate the score function.

    So So

    if you just plainly look at s of x right if you just plainly look at s of x right
    if you just plainly look at s of x right

    to calculate s of x we don''t need to to calculate s of x we don''t need to to
    calculate s of x we don''t need to

    worry about partition function. It worry about partition function. It worry about
    partition function. It

    simply becomes minus grad of e5 of x simply becomes minus grad of e5 of x simply
    becomes minus grad of e5 of x

    that''s all. that''s all.'
  concept_slugs:
  - langevin-dynamics
  - score-function
- idx: 42
  start_sec: 2586.88
  end_sec: 2642.88
  text: 'that''s all.

    So the partition function becomes zero So the partition function becomes zero
    So the partition function becomes zero

    and is not included in the calculation and is not included in the calculation
    and is not included in the calculation

    of the score function. of the score function. of the score function.

    Which is why we get the freedom from the Which is why we get the freedom from
    the Which is why we get the freedom from the

    partition function calculation. Now let us uh move ahead and uh see how Now let
    us uh move ahead and uh see how

    this formulation of the score function this formulation of the score function
    this formulation of the score function

    can be used for training energy based can be used for training energy based can
    be used for training energy based

    models which is our objective in the models which is our objective in the models
    which is our objective in the

    first place. first place. first place.

    So now that we have understood the So now that we have understood the So now that
    we have understood the

    intuition behind s of x which is the intuition behind s of x which is the intuition
    behind s of x which is the

    score function and score function and score function and

    also we have understood that to also we have understood that to also we have understood
    that to

    calculate the score you don''t need to calculate the score you don''t need to
    calculate the score you don''t need to

    rely on the partition function. rely on the partition function. rely on the partition
    function.

    Let us go ahead and understand how how Let us go ahead and understand how how
    Let us go ahead and understand how how

    do we train these energy based models. do we train these energy based models.
    do we train these energy based models.

    Okay. So, uh energy based models are Okay. So, uh energy based models are Okay.
    So, uh energy based models are

    trained using a concept which is called trained using a concept which is called
    trained using a concept which is called

    as score matching. What is score matching? Score matching What is score matching?
    Score matching

    makes sure that the score of the makes sure that the score of the'
  concept_slugs:
  - langevin-dynamics
  - score-function
- idx: 43
  start_sec: 2642.88
  end_sec: 2733.599
  text: 'makes sure that the score of the

    predicted model matches the score of the predicted model matches the score of
    the predicted model matches the score of the

    true probability distribution. true probability distribution. true probability
    distribution.

    So, uh we have two scores over here. The So, uh we have two scores over here.
    The So, uh we have two scores over here. The

    first is the score of the true first is the score of the true first is the score
    of the true

    distribution which makes uses which distribution which makes uses which distribution
    which makes uses which

    which uses the which uses the which uses the

    probability distribution of the probability distribution of the probability distribution
    of the

    underlying data. Remember we do not have underlying data. Remember we do not have
    underlying data. Remember we do not have

    access to this and the second is the score for the and the second is the score
    for the

    predicted distribution. This is what we predicted distribution. This is what we
    predicted distribution. This is what we

    want to train. So the score matching loss looks like So the score matching loss
    looks like

    this. this.

    We want to calculate uh We want to calculate uh We want to calculate uh

    we want to train our model such that the we want to train our model such that
    the we want to train our model such that the

    score function of our predicted model score function of our predicted model score
    function of our predicted model

    matches the score of the true matches the score of the true matches the score
    of the true

    probability distribution. probability distribution.

    And uh this looks fine uh in in And uh this looks fine uh in in And uh this looks
    fine uh in in

    principle. If you expand this uh you principle. If you expand this uh you principle.
    If you expand this uh you

    would know that it it it boils down to would know that it it it boils down to
    would know that it it it boils down to

    uh if if we just use this formulation uh if if we just use this formulation uh
    if if we just use this formulation

    this boils down to this boils down to this boils down to

    ei So ideally we want'
  concept_slugs:
  - langevin-dynamics
  - score-function
- idx: 44
  start_sec: 2733.599
  end_sec: 2782.0
  text: 'So ideally we want

    a loss which looks like this. Now the a loss which looks like this. Now the a
    loss which looks like this. Now the

    question again becomes how do we question again becomes how do we question again
    becomes how do we

    calculate this uh probability data or calculate this uh probability data or calculate
    this uh probability data or

    the the energy function for your the the energy function for your the the energy
    function for your

    underlying samples. You have absolutely underlying samples. You have absolutely
    underlying samples. You have absolutely

    no idea how to calculate this right. no idea how to calculate this right. no idea
    how to calculate this right.

    It''s it''s it''s difficult because we do It''s it''s it''s difficult because
    we do It''s it''s it''s difficult because we do

    not know this. We only have these not know this. We only have these not know this.
    We only have these

    samples. We do not know what is the samples. We do not know what is the samples.
    We do not know what is the

    probability associated with them. what probability associated with them. what
    probability associated with them. what

    is the energy associated with them? If is the energy associated with them? If
    is the energy associated with them? If

    we knew that we could plot the original we knew that we could plot the original
    we knew that we could plot the original

    distribution as it is, right? So let us distribution as it is, right? So let us
    distribution as it is, right? So let us

    park this for now. We will come back to park this for now. We will come back to
    park this for now. We will come back to

    this after some time. this after some time. this after some time.

    Let us first assume that we have trained Let us first assume that we have trained
    Let us first assume that we have trained

    our score function. Okay. So uh let us our score function. Okay. So uh let us
    our score function. Okay. So uh let us

    assume that assume that assume that

    this is known to us. this is known to us. this is known to us.

    Let us assume that we have done the Let us assume that we have done the'
  concept_slugs:
  - langevin-dynamics
  - score-function
- idx: 45
  start_sec: 2782.0
  end_sec: 2829.2
  text: 'Let us assume that we have done the

    training. We have matched this score training. We have matched this score training.
    We have matched this score

    with the uh score for the true model for with the uh score for the true model
    for with the uh score for the true model for

    the true distribution and we have got the true distribution and we have got the
    true distribution and we have got

    the score. The main question is that the score. The main question is that the
    score. The main question is that

    once you get the score, how do you once you get the score, how do you once you
    get the score, how do you

    sample from the score? How do you sample sample from the score? How do you sample
    sample from the score? How do you sample

    the images the images the images

    in in the diffusion model? We were in in the diffusion model? We were in in the
    diffusion model? We were

    directly predicting the probability directly predicting the probability directly
    predicting the probability

    distribution or the noise level. So we distribution or the noise level. So we
    distribution or the noise level. So we

    could subtract the noise iteratively could subtract the noise iteratively could
    subtract the noise iteratively

    from the from the from the

    uh from pure noise and we could get the uh from pure noise and we could get the
    uh from pure noise and we could get the

    image right we could sample but how do image right we could sample but how do
    image right we could sample but how do

    we sample from this score function we sample from this score function we sample
    from this score function

    all we know is the direction of where to all we know is the direction of where
    to all we know is the direction of where to

    go and intuitively it it looks like it go and intuitively it it looks like it
    go and intuitively it it looks like it

    should be possible because if I am in a should be possible because if I am in
    a should be possible because if I am in a

    data point and I know where to go I can data point and I know where to go I can'
  concept_slugs:
  - langevin-dynamics
  - score-function
- idx: 46
  start_sec: 2829.2
  end_sec: 2898.96
  text: 'data point and I know where to go I can

    navigate my way and I can find samples navigate my way and I can find samples
    navigate my way and I can find samples

    from the distribution Okay. And uh this from the distribution Okay. And uh this
    from the distribution Okay. And uh this

    this this this is very interesting this this this is very interesting this this
    this is very interesting

    because it really uh it will help us to because it really uh it will help us to
    because it really uh it will help us to

    understand a bit deeper about understand a bit deeper about understand a bit deeper
    about

    understand the score function in a more understand the score function in a more
    understand the score function in a more

    deeper way. Okay. So the question that deeper way. Okay. So the question that
    deeper way. Okay. So the question that

    we will address is how do you sample the we will address is how do you sample
    the we will address is how do you sample the

    data if you have the score function. Okay. So let''s let''s try to understand
    Okay. So let''s let''s try to understand

    this in detail. So to understand this we will start from So to understand this
    we will start from

    something which is uh even more at a simpler level. Okay. We even more at a simpler
    level. Okay. We

    will start from uh this question that if will start from uh this question that
    if will start from uh this question that if

    you are dropped into a thick fog in a you are dropped into a thick fog in a you
    are dropped into a thick fog in a

    vast landscape and vast landscape and vast landscape and

    your goal is to find the deepest valley your goal is to find the deepest valley
    your goal is to find the deepest valley

    because that is where the treasure is because that is where the treasure is because
    that is where the treasure is

    hidden. hidden. hidden.

    How will you go to the deepest valley? How will you go to the deepest valley?
    How will you go to the deepest valley?

    Here I can visually see that this is the Here I can visually see that this is
    the'
  concept_slugs:
  - langevin-dynamics
  - score-function
- idx: 47
  start_sec: 2898.96
  end_sec: 2950.559
  text: 'Here I can visually see that this is the

    deepest valley and I can see the deepest valley and I can see the deepest valley
    and I can see the

    treasure is hidden there. treasure is hidden there. treasure is hidden there.

    But if your goal is to reach the deepest But if your goal is to reach the deepest
    But if your goal is to reach the deepest

    valley, how would you go to the deepest valley, how would you go to the deepest
    valley, how would you go to the deepest

    valley if you cannot directly visually valley if you cannot directly visually
    valley if you cannot directly visually

    see this? see this? see this?

    Okay, so uh you would like to trace a Okay, so uh you would like to trace a Okay,
    so uh you would like to trace a

    route which looks something like this, route which looks something like this,
    route which looks something like this,

    right? How can you frame it in a different way? How can you frame it in a different
    way?

    The strategy that you will use is since The strategy that you will use is since
    The strategy that you will use is since

    you know that the pressure is in the you know that the pressure is in the you
    know that the pressure is in the

    valley somewhere, you know that going valley somewhere, you know that going valley
    somewhere, you know that going

    down is good and going up is bad. down is good and going up is bad. down is good
    and going up is bad.

    And to reach the valley in the quickest And to reach the valley in the quickest
    And to reach the valley in the quickest

    possible time, you will go in the possible time, you will go in the possible time,
    you will go in the

    direction where the downward slope is direction where the downward slope is direction
    where the downward slope is

    maximum. So this is this is quite intuitive, So this is this is quite intuitive,

    right? Let''s say this is the this is my right? Let''s say this is the this is
    my right? Let''s say this is the this is my

    valley and I start here. and I want to valley and I start here. and I want to'
  concept_slugs:
  - langevin-dynamics
  - score-function
- idx: 48
  start_sec: 2950.559
  end_sec: 3012.72
  text: 'valley and I start here. and I want to

    reach the bottom of the valley. So I''ll reach the bottom of the valley. So I''ll
    reach the bottom of the valley. So I''ll

    make a step like this. I''ll again make a make a step like this. I''ll again make
    a make a step like this. I''ll again make a

    step. I''ll again make a step and I will step. I''ll again make a step and I will
    step. I''ll again make a step and I will

    reach the bottom of the valley. So let reach the bottom of the valley. So let
    reach the bottom of the valley. So let

    us say the slope is given by the symbol us say the slope is given by the symbol
    us say the slope is given by the symbol

    uh q and if your current position is xt uh q and if your current position is xt
    uh q and if your current position is xt

    and your next position is xt + 1 then and your next position is xt + 1 then and
    your next position is xt + 1 then

    you can write your next position like you can write your next position like you
    can write your next position like

    this. So this is actually So this is actually

    the slope. So what we are doing here is let''s say So what we are doing here is
    let''s say

    this is your valley this is your valley this is your valley

    and you are here at XT. Okay. So x t + 1 Okay. So x t + 1

    can be written in terms of if you know can be written in terms of if you know
    can be written in terms of if you know

    this slope you can multiply this slope this slope you can multiply this slope
    this slope you can multiply this slope

    by so this this would be delta t in this by so this this would be delta t in this
    by so this this would be delta t in this

    case you multiply it by delta t and you case you multiply it by delta t and you
    case you multiply it by delta t and you

    would get your next location. would get your next location.'
  concept_slugs:
  - langevin-dynamics
  - score-function
- idx: 49
  start_sec: 3012.72
  end_sec: 3067.589
  text: 'would get your next location.

    But what is the slope here? How do we But what is the slope here? How do we But
    what is the slope here? How do we

    find the slope? This is my energy find the slope? This is my energy find the slope?
    This is my energy

    function ei of x which we started out in function ei of x which we started out
    in function ei of x which we started out in

    the first place. the first place. the first place.

    and uh the the slope is given by grad of and uh the the slope is given by grad
    of and uh the the slope is given by grad of

    E5 of X. E5 of X. E5 of X.

    So then my equation becomes So then my equation becomes So then my equation becomes

    Q q is negative of grad because we are Q q is negative of grad because we are
    Q q is negative of grad because we are

    going in the reverse direction. Here we going in the reverse direction. Here we
    going in the reverse direction. Here we

    can write XT + 1 = XT minus N into can write XT + 1 = XT minus N into can write
    XT + 1 = XT minus N into

    gradient of EI of X. gradient of EI of X. gradient of EI of X.

    This is very similar to the gradient This is very similar to the gradient This
    is very similar to the gradient

    descent equation. uh remember how we descent equation. uh remember how we descent
    equation. uh remember how we

    let''s say this is your parameter let''s say this is your parameter let''s say
    this is your parameter

    w and uh this is your loss. w and uh this is your loss. w and uh this is your
    loss.

    So how do we update the parameter wt + 1 So how do we update the parameter wt
    + 1 So how do we update the parameter wt + 1

    equal to wt minus alpha step size into equal to wt minus alpha step size into
    equal to wt minus alpha step size into

    gradient of the loss function. This is gradient of the loss function. This is
    gradient of the loss function. This is

    exactly what we are doing here. We are'
  concept_slugs:
  - langevin-dynamics
  - score-function
- idx: 50
  start_sec: 3067.589
  end_sec: 3119.44
  text: 'exactly what we are doing here. We are exactly what we are doing here. We
    are

    calculating the gradient of the energy calculating the gradient of the energy
    calculating the gradient of the energy

    and u and u and u

    we are taking a step in the this is what we are taking a step in the this is what
    we are taking a step in the this is what

    this minus sign encodes this gradient this minus sign encodes this gradient this
    minus sign encodes this gradient

    will always have a positive value that''s will always have a positive value that''s
    will always have a positive value that''s

    what that''s how we define it what that''s how we define it what that''s how we
    define it

    and uh the the negative sign ensures and uh the the negative sign ensures and
    uh the the negative sign ensures

    that we are going in the direction of that we are going in the direction of that
    we are going in the direction of

    the slope like the bottom of of the the slope like the bottom of of the the slope
    like the bottom of of the

    valley. valley.

    So this is how we define our movement. So this is how we define our movement.
    So this is how we define our movement.

    If you go up according to the above If you go up according to the above If you
    go up according to the above

    rule, you are guaranteed to move towards rule, you are guaranteed to move towards
    rule, you are guaranteed to move towards

    regions where the energy function is regions where the energy function is regions
    where the energy function is

    minimum. minimum. minimum.

    Now you might see that oh this is this Now you might see that oh this is this
    Now you might see that oh this is this

    looks somewhat familiar, right? How does looks somewhat familiar, right? How does
    looks somewhat familiar, right? How does

    this look familiar? this look familiar? this look familiar?

    Remember uh we looked at the score Remember uh we looked at the score Remember
    uh we looked at the score

    function and it it looked something like function and it it looked something like
    function and it it looked something like

    this which is gradient of the energy this which is gradient of the energy'
  concept_slugs:
  - langevin-dynamics
  - score-function
- idx: 51
  start_sec: 3119.44
  end_sec: 3172.64
  text: 'this which is gradient of the energy

    function. So the negative of this function. So the negative of this function.
    So the negative of this

    actually is the score function itself. actually is the score function itself.
    actually is the score function itself.

    So this can be written as XT + N into S5 So this can be written as XT + N into
    S5 So this can be written as XT + N into S5

    of XT. of XT. of XT.

    So does that mean we are done here? So does that mean we are done here? So does
    that mean we are done here?

    Because if we calculate the Because if we calculate the Because if we calculate
    the

    we are at any point we calculate the we are at any point we calculate the we are
    at any point we calculate the

    score score score

    we take a step size of n and we take we take a step size of n and we take we take
    a step size of n and we take

    that step we move towards xt + 1 we take that step we move towards xt + 1 we take
    that step we move towards xt + 1 we take

    another step we move towards xt +2 so another step we move towards xt +2 so another
    step we move towards xt +2 so

    does that mean our our job is done? Well does that mean our our job is done? Well
    does that mean our our job is done? Well

    we are not done yet because this is only we are not done yet because this is only
    we are not done yet because this is only

    half of the entire puzzle which we have half of the entire puzzle which we have
    half of the entire puzzle which we have

    solved. solved. solved.

    The next half becomes very crucial. The next half becomes very crucial. The next
    half becomes very crucial.

    Consider this scenario where you have Consider this scenario where you have Consider
    this scenario where you have

    reached the bottom of the pit and the reached the bottom of the pit and the reached
    the bottom of the pit and the

    gradient is zero. So you are just gradient is zero. So you are just'
  concept_slugs:
  - langevin-dynamics
  - score-function
- idx: 52
  start_sec: 3172.64
  end_sec: 3220.8
  text: 'gradient is zero. So you are just

    sitting there but there is another pit sitting there but there is another pit
    sitting there but there is another pit

    which is even below which is even below which is even below

    even below this. So this looks something even below this. So this looks something
    even below this. So this looks something

    like this. like this. like this.

    You are stuck somewhere here but there You are stuck somewhere here but there
    You are stuck somewhere here but there

    is another pit which is somewhere over is another pit which is somewhere over
    is another pit which is somewhere over

    here. How will you find this? And in here. How will you find this? And in here.
    How will you find this? And in

    fact the the first curve that we saw was fact the the first curve that we saw
    was fact the the first curve that we saw was

    like this when we started our discussion like this when we started our discussion
    like this when we started our discussion

    on energy based models. Using this on energy based models. Using this on energy
    based models. Using this

    approach you will reach this and the approach you will reach this and the approach
    you will reach this and the

    gradient will be zero and then XT + 1 gradient will be zero and then XT + 1 gradient
    will be zero and then XT + 1

    will be same as XT. You will just stay will be same as XT. You will just stay
    will be same as XT. You will just stay

    here. here. here.

    I need something which can push me out I need something which can push me out
    I need something which can push me out

    of this and take me towards the next of this and take me towards the next of this
    and take me towards the next

    minima which might be lower. So we are here and the global minima we So we are
    here and the global minima we

    will never find. To solve this issue, we will never find. To solve this issue,
    we will never find. To solve this issue, we

    need to provide a shake which gives you need to provide a shake which gives you'
  concept_slugs:
  - langevin-dynamics
  - score-function
- idx: 53
  start_sec: 3220.8
  end_sec: 3269.75
  text: 'need to provide a shake which gives you

    enough random energy to kick you out of enough random energy to kick you out of
    enough random energy to kick you out of

    these small potholes so that you can these small potholes so that you can these
    small potholes so that you can

    keep moving towards the bottom of the keep moving towards the bottom of the keep
    moving towards the bottom of the

    valley which is where the global minima valley which is where the global minima
    valley which is where the global minima

    lies. lies. lies.

    So you need something which can give you So you need something which can give
    you So you need something which can give you

    that shake right which can push you. that shake right which can push you. that
    shake right which can push you.

    And remember in the lecture on diffusion And remember in the lecture on diffusion
    And remember in the lecture on diffusion

    we had discussed about adding noise to we had discussed about adding noise to
    we had discussed about adding noise to

    the data and we had written a simple the data and we had written a simple the
    data and we had written a simple

    expression to add noise as follows. expression to add noise as follows. expression
    to add noise as follows.

    where x i + 1 is the image in the where x i + 1 is the image in the where x i
    + 1 is the image in the

    forward step at the next time step. This forward step at the next time step. This
    forward step at the next time step. This

    is the current time step and this is is the current time step and this is is the
    current time step and this is

    what introduces the noise. what introduces the noise. what introduces the noise.

    Uh this epsilon is a random variable Uh this epsilon is a random variable Uh this
    epsilon is a random variable

    which can take any value between 0 to 1. which can take any value between 0 to
    1. which can take any value between 0 to 1.

    So this above expression also means that So this above expression also means that
    So this above expression also means that

    we are sampling from a gshian'
  concept_slugs:
  - langevin-dynamics
  - score-function
- idx: 54
  start_sec: 3269.75
  end_sec: 3330.64
  text: 'we are sampling from a gshian we are sampling from a gshian

    distribution with a mean of xi and a distribution with a mean of xi and a distribution
    with a mean of xi and a

    standard deviation of beta. standard deviation of beta. standard deviation of
    beta.

    uh this we also saw in variational uh this we also saw in variational uh this
    we also saw in variational

    autoenccoders where given sigma and epi autoenccoders where given sigma and epi
    autoenccoders where given sigma and epi

    sigma and mu for the latent variable the sigma and mu for the latent variable
    the sigma and mu for the latent variable the

    way we wrote zed was mu + sigma * way we wrote zed was mu + sigma * way we wrote
    zed was mu + sigma *

    epsilon epsilon epsilon

    so okay so now we can think okay fine so okay so now we can think okay fine so
    okay so now we can think okay fine

    can we add noise using something like can we add noise using something like can
    we add noise using something like

    this and it turns out we can definitely this and it turns out we can definitely
    this and it turns out we can definitely

    we can add noise which looks something we can add noise which looks something
    we can add noise which looks something

    like So th this part of the expression is So th this part of the expression is

    exactly the same that we looked at exactly the same that we looked at exactly
    the same that we looked at

    before. There is only this new term before. There is only this new term before.
    There is only this new term

    which is added which uh which is added which uh which is added which uh

    has this variable which is the random has this variable which is the random has
    this variable which is the random

    variable epsilon and <unk>2 ea is just a constant which and <unk>2 ea is just
    a constant which

    is probably exists there to make sure is probably exists there to make sure is
    probably exists there to make sure

    the total variance of this xt + 1 is the total variance of this xt + 1 is'
  concept_slugs:
  - langevin-dynamics
  - score-function
- idx: 55
  start_sec: 3330.64
  end_sec: 3389.91
  text: 'the total variance of this xt + 1 is

    maybe a constant or it''s just one that maybe a constant or it''s just one that
    maybe a constant or it''s just one that

    is my hypothesis is my hypothesis is my hypothesis

    this is also called as discrete time this is also called as discrete time this
    is also called as discrete time

    lang update lang update lang update

    Why it is called languin update and not Why it is called languin update and not
    Why it is called languin update and not

    just a gradient descent update? It''s just a gradient descent update? It''s just
    a gradient descent update? It''s

    because we are adding this stoastic term because we are adding this stoastic term
    because we are adding this stoastic term

    which is like a shake. So what this term which is like a shake. So what this term
    which is like a shake. So what this term

    will do is I reach at the bottom of this will do is I reach at the bottom of this
    will do is I reach at the bottom of this

    pit. pit. pit.

    Now xt + 1 is equal to xt Now xt + 1 is equal to xt Now xt + 1 is equal to xt

    plus plus plus

    uh what was the term over here? Yeah. uh what was the term over here? Yeah. uh
    what was the term over here? Yeah.

    Minus n of Minus n of Minus n of

    gradient of the energy plus this stochastic term which is plus this stochastic
    term which is

    <unk>2n into epsilon. So this is zero. <unk>2n into epsilon. So this is zero.
    <unk>2n into epsilon. So this is zero.

    So because the gradient is zero. But So because the gradient is zero. But So because
    the gradient is zero. But

    because of this term I''ll be forced to because of this term I''ll be forced to
    because of this term I''ll be forced to

    move out of this bit and explore new move out of this bit and explore new move
    out of this bit and explore new

    regions which is exactly what we want. regions which is exactly what we want.
    regions which is exactly what we want.

    We want to deliberately add this We want to deliberately add this We want to deliberately
    add this

    stoasticity.'
  concept_slugs:
  - langevin-dynamics
  - score-function
- idx: 56
  start_sec: 3392.95
  end_sec: 3436.64
  text: 'Now we what we do is we replace this Now we what we do is we replace this

    grad of energy by s of x which we have grad of energy by s of x which we have
    grad of energy by s of x which we have

    already seen before and this is the already seen before and this is the already
    seen before and this is the

    final expression that we get. final expression that we get. final expression that
    we get.

    Substituting this in the equation gives Substituting this in the equation gives
    Substituting this in the equation gives

    us the us the us the

    update rule which we can use to sample update rule which we can use to sample
    update rule which we can use to sample

    when we know the predicted score when we know the predicted score when we know
    the predicted score

    function. So this should ideally be si function. So this should ideally be si
    function. So this should ideally be si

    because it is the predicted score because it is the predicted score because it
    is the predicted score

    function. We have not yet looked at how function. We have not yet looked at how
    function. We have not yet looked at how

    to train the score function to match it to train the score function to match it
    to train the score function to match it

    with the real score function. There are with the real score function. There are
    with the real score function. There are

    challenges there. But now we know that challenges there. But now we know that
    challenges there. But now we know that

    once we have the score function, we can once we have the score function, we can
    once we have the score function, we can

    use the langin use the langin use the langin

    sampling method to sample from the score sampling method to sample from the score
    sampling method to sample from the score

    function and we can find a trajectory. function and we can find a trajectory.
    function and we can find a trajectory.

    So ideally if we start from some So ideally if we start from some So ideally if
    we start from some

    trajectory let''s say I start from here trajectory let''s say I start from here'
  concept_slugs:
  - langevin-dynamics
  - score-function
- idx: 57
  start_sec: 3436.64
  end_sec: 3479.119
  text: 'trajectory let''s say I start from here

    with this update I''ll go like this with this update I''ll go like this with this
    update I''ll go like this

    and then I''ll finally I I I need to come and then I''ll finally I I I need to
    come and then I''ll finally I I I need to come

    up to a space where the probability up to a space where the probability up to
    a space where the probability

    density density density

    of uh my my data is maximum and and I of uh my my data is maximum and and I of
    uh my my data is maximum and and I

    can safely sample from it. can safely sample from it. can safely sample from it.

    So this is how you would move. You start So this is how you would move. You start
    So this is how you would move. You start

    with a point, you end up with a point with a point, you end up with a point with
    a point, you end up with a point

    and then that point is your sample. And and then that point is your sample. And
    and then that point is your sample. And

    uh why is that point your sample? uh why is that point your sample? uh why is
    that point your sample?

    Because you''re ending up at a point Because you''re ending up at a point Because
    you''re ending up at a point

    which the where the score function has which the where the score function has
    which the where the score function has

    guided you. So this is like a compass guided you. So this is like a compass guided
    you. So this is like a compass

    which the score function guides you which the score function guides you which
    the score function guides you

    towards. You start from anywhere. You towards. You start from anywhere. You towards.
    You start from anywhere. You

    have no idea where the data is but you have no idea where the data is but you
    have no idea where the data is but you

    have a small compass with you which is have a small compass with you which is
    have a small compass with you which is

    the score function which takes you from the score function which takes you from'
  concept_slugs:
  - langevin-dynamics
  - score-function
- idx: 58
  start_sec: 3479.119
  end_sec: 3535.92
  text: 'the score function which takes you from

    one location to the another and finally one location to the another and finally
    one location to the another and finally

    you end up at a space or a region where you end up at a space or a region where
    you end up at a space or a region where

    the probability density is the maximum. the probability density is the maximum.
    the probability density is the maximum.

    So we are going to now look at exactly So we are going to now look at exactly
    So we are going to now look at exactly

    how to use lang dynamics to sample from how to use lang dynamics to sample from
    how to use lang dynamics to sample from

    a known probability distribution. a known probability distribution. a known probability
    distribution.

    uh remember we''ll consider that the uh remember we''ll consider that the uh remember
    we''ll consider that the

    probability distribution is already probability distribution is already probability
    distribution is already

    known because we want to uh consider known because we want to uh consider known
    because we want to uh consider

    that the score function is already that the score function is already that the
    score function is already

    known. Okay. So now let''s take a practical Okay. So now let''s take a practical

    example and dive into the Google collab example and dive into the Google collab
    example and dive into the Google collab

    notebook. Okay. So the example that we notebook. Okay. So the example that we
    notebook. Okay. So the example that we

    are going to look at is uh are going to look at is uh are going to look at is
    uh

    we are going to consider that we know we are going to consider that we know we
    are going to consider that we know

    this true probability distribution which this true probability distribution which
    this true probability distribution which

    is p data of x. is p data of x. is p data of x.

    So we are going to assume that p data of So we are going to assume that p data
    of So we are going to assume that p data of

    x is known to us. It looks something x is known to us. It looks something'
  concept_slugs:
  - langevin-dynamics
  - score-function
- idx: 59
  start_sec: 3535.92
  end_sec: 3595.119
  text: 'x is known to us. It looks something

    like this. The probability of finding like this. The probability of finding like
    this. The probability of finding

    the samples is maximum at these two the samples is maximum at these two the samples
    is maximum at these two

    locations where you see the spots are locations where you see the spots are locations
    where you see the spots are

    very hot. Right? And as you move away very hot. Right? And as you move away very
    hot. Right? And as you move away

    from uh these points we can see that the from uh these points we can see that
    the from uh these points we can see that the

    probability dies down slowly. So ideally what should happen is So ideally what
    should happen is

    whenever I start from any point let''s whenever I start from any point let''s
    whenever I start from any point let''s

    say here say here say here

    uh my languin dynamic sampling should uh my languin dynamic sampling should uh
    my languin dynamic sampling should

    take me from this point to a point which take me from this point to a point which
    take me from this point to a point which

    is either here or here. is either here or here. is either here or here.

    then I can be sure that my method of then I can be sure that my method of then
    I can be sure that my method of

    sampling using the languin dynamics sampling using the languin dynamics sampling
    using the languin dynamics

    technique has actually worked. technique has actually worked. technique has actually
    worked.

    So let''s look at an example to see So let''s look at an example to see So let''s
    look at an example to see

    whether that actually happens or not. whether that actually happens or not. whether
    that actually happens or not.

    We will look at a Google Collab We will look at a Google Collab We will look at
    a Google Collab

    notebook. I have shared all these links notebook. I have shared all these links
    notebook. I have shared all these links

    down below in the chat uh in in in the down below in the chat uh in in in the
    down below in the chat uh in in in the

    comments. comments.'
  concept_slugs:
  - langevin-dynamics
  - score-function
- idx: 60
  start_sec: 3595.119
  end_sec: 3640.64
  text: 'comments.

    So first we define the setup which are So first we define the setup which are
    So first we define the setup which are

    the two mountain setup as as we saw the two mountain setup as as we saw the two
    mountain setup as as we saw

    there are two peaks in our data there are two peaks in our data there are two
    peaks in our data

    and in this block we calculate the and in this block we calculate the and in this
    block we calculate the

    probability and the scores also. probability and the scores also. probability
    and the scores also.

    Remember we are assuming that the scores Remember we are assuming that the scores
    Remember we are assuming that the scores

    are known to us. We are not discussing are known to us. We are not discussing
    are known to us. We are not discussing

    the training process right now. We are the training process right now. We are
    the training process right now. We are

    only discussing the sampling process. only discussing the sampling process. only
    discussing the sampling process.

    So now what we do is we run the lang So now what we do is we run the lang So now
    what we do is we run the lang

    dynamics here. I want you to take a very dynamics here. I want you to take a very
    dynamics here. I want you to take a very

    close attention to this step which is close attention to this step which is close
    attention to this step which is

    exactly what we wrote before. exactly what we wrote before. exactly what we wrote
    before.

    The position at the next time step is The position at the next time step is The
    position at the next time step is

    the position at the current time step the position at the current time step the
    position at the current time step

    plus EA time the score plus the noise plus EA time the score plus the noise plus
    EA time the score plus the noise

    scale which is square root of 2 EA into scale which is square root of 2 EA into
    scale which is square root of 2 EA into

    noise. We use the exact same equation noise. We use the exact same equation'
  concept_slugs:
  - langevin-dynamics
  - score-function
- idx: 61
  start_sec: 3640.64
  end_sec: 3688.799
  text: 'noise. We use the exact same equation

    which we discuss in theory which we discuss in theory which we discuss in theory

    and then we visualize the path. and then we visualize the path. and then we visualize
    the path.

    So we start from here and we end up over So we start from here and we end up over
    So we start from here and we end up over

    here. This is the end path. here. This is the end path. here. This is the end
    path.

    Now I''ll again run this. We start and we Now I''ll again run this. We start and
    we Now I''ll again run this. We start and we

    again end somewhere here. We will not again end somewhere here. We will not again
    end somewhere here. We will not

    end up at the exact same point every end up at the exact same point every end
    up at the exact same point every

    time because the process is stoastic in time because the process is stoastic in
    time because the process is stoastic in

    nature. But we will end up at a place nature. But we will end up at a place nature.
    But we will end up at a place

    where we are very close to the where we are very close to the where we are very
    close to the

    area where the probability of finding area where the probability of finding area
    where the probability of finding

    data is the maximum. data is the maximum. data is the maximum.

    Now one question you might have is why Now one question you might have is why
    Now one question you might have is why

    do we see these zigzag paths? It almost do we see these zigzag paths? It almost
    do we see these zigzag paths? It almost

    appears like a drunk person is walking, appears like a drunk person is walking,
    appears like a drunk person is walking,

    right? In fact, this is an analogy which right? In fact, this is an analogy which
    right? In fact, this is an analogy which

    is used in a lot of classical textbooks. is used in a lot of classical textbooks.
    is used in a lot of classical textbooks.

    It''s it''s called a drunk hiker. It''s it''s called a drunk hiker.'
  concept_slugs:
  - langevin-dynamics
  - score-function
- idx: 62
  start_sec: 3688.799
  end_sec: 3738.319
  text: 'It''s it''s called a drunk hiker.

    It''s like someone is drunk and walking It''s like someone is drunk and walking
    It''s like someone is drunk and walking

    here and there and finally reaching the here and there and finally reaching the
    here and there and finally reaching the

    final solution. And this this this final solution. And this this this final solution.
    And this this this

    apparent drunkenness is because of the apparent drunkenness is because of the
    apparent drunkenness is because of the

    the third term which we have added which the third term which we have added which
    the third term which we have added which

    which introduces the noise in the update which introduces the noise in the update
    which introduces the noise in the update

    rule because we have that epsilon rule because we have that epsilon rule because
    we have that epsilon

    sitting over there. we have these paths sitting over there. we have these paths
    sitting over there. we have these paths

    which appear zigzag otherwise we will which appear zigzag otherwise we will which
    appear zigzag otherwise we will

    get an update which appears probably get an update which appears probably get
    an update which appears probably

    smooth with continuous derivatives at at smooth with continuous derivatives at
    at smooth with continuous derivatives at at

    all time steps. all time steps. all time steps.

    So this is amazing right we are actually So this is amazing right we are actually
    So this is amazing right we are actually

    able to simulate trajectories once we able to simulate trajectories once we able
    to simulate trajectories once we

    have the score function we can reach a have the score function we can reach a
    have the score function we can reach a

    point where point where point where

    it looks like we are reaching the point it looks like we are reaching the point
    it looks like we are reaching the point

    where the probability of that data being where the probability of that data being
    where the probability of that data being

    sampled from the two distribution is sampled from the two distribution is sampled
    from the two distribution is

    maximum. maximum. maximum.

    So I want all of you to run this tweak a So I want all of you to run this tweak
    a'
  concept_slugs:
  - langevin-dynamics
  - score-function
- idx: 63
  start_sec: 3738.319
  end_sec: 3795.839
  text: 'So I want all of you to run this tweak a

    little things here and there have fun little things here and there have fun little
    things here and there have fun

    with the notebook and really develop with the notebook and really develop with
    the notebook and really develop

    confidence in the lang dynamics confidence in the lang dynamics confidence in
    the lang dynamics

    technique. technique. technique.

    Later we will see a very close parallel Later we will see a very close parallel
    Later we will see a very close parallel

    between the lang dynamics and the between the lang dynamics and the between the
    lang dynamics and the

    diffusion method as well. diffusion method as well. diffusion method as well.

    And it is amazing that this lang dynamic And it is amazing that this lang dynamic
    And it is amazing that this lang dynamic

    sampling is in fact related to sampling is in fact related to sampling is in fact
    related to

    diffusion. But that is the beauty of diffusion. But that is the beauty of diffusion.
    But that is the beauty of

    this course. we will slowly unpack it. this course. we will slowly unpack it.
    this course. we will slowly unpack it.

    Okay. So now we will look at how exactly Okay. So now we will look at how exactly
    Okay. So now we will look at how exactly

    does the score function training happen. does the score function training happen.
    does the score function training happen.

    How is the score function trained? How is the score function trained? How is the
    score function trained?

    We we we briefly mentioned something We we we briefly mentioned something We we
    we briefly mentioned something

    called score matching but now we are called score matching but now we are called
    score matching but now we are

    going to look at score matching in more going to look at score matching in more
    going to look at score matching in more

    detail. detail. detail.

    This is also called as scorebased This is also called as scorebased This is also
    called as scorebased

    generative models. generative models. generative models.

    The key idea is that since sampling with The key idea is that since sampling with
    The key idea is that since sampling with

    since sampling with langu dynamics only since sampling with langu dynamics only'
  concept_slugs:
  - langevin-dynamics
  - score-function
- idx: 64
  start_sec: 3795.839
  end_sec: 3867.029
  text: 'since sampling with langu dynamics only

    requires the score like we saw in this requires the score like we saw in this
    requires the score like we saw in this

    formula it only requires the score we formula it only requires the score we formula
    it only requires the score we

    can learn it directly from a neural can learn it directly from a neural can learn
    it directly from a neural

    network. So let''s say this is your data network. So let''s say this is your data
    network. So let''s say this is your data

    and uh the ground truth score is given and uh the ground truth score is given
    and uh the ground truth score is given

    in black. These are the black arrows in black. These are the black arrows in black.
    These are the black arrows

    and the blue arrows is our predictions. So we can see that it''s not exactly So
    we can see that it''s not exactly

    accurate. Um in many places our accurate. Um in many places our accurate. Um in
    many places our

    predictions are slightly predictions are slightly predictions are slightly

    different different different

    than the ground truth. But the whole than the ground truth. But the whole than
    the ground truth. But the whole

    objective of the scorebased generative objective of the scorebased generative
    objective of the scorebased generative

    models is to predict the score function models is to predict the score function
    models is to predict the score function

    such that it matches the ground truth such that it matches the ground truth such
    that it matches the ground truth

    score as closely as possible. So this is score as closely as possible. So this
    is score as closely as possible. So this is

    just a visual representation of that. Now this true score function is given by
    Now this true score function is given by

    this and the predicted score function is this and the predicted score function
    is this and the predicted score function is

    given by given by given by

    this where the only thing we have done this where the only thing we have done
    this where the only thing we have done

    is replace data by five over here is replace data by five over here is replace
    data by five over here

    and score matching fits this vector'
  concept_slugs:
  - langevin-dynamics
  - score-function
- idx: 65
  start_sec: 3867.029
  end_sec: 3940.079
  text: 'and score matching fits this vector and score matching fits this vector

    field by minimizing the mean square field by minimizing the mean square field
    by minimizing the mean square

    error between the true and the estimated error between the true and the estimated
    error between the true and the estimated

    scores which looks something like this. scores which looks something like this.
    scores which looks something like this.

    Now the main issue is that it is very Now the main issue is that it is very Now
    the main issue is that it is very

    difficult to find this. This is difficult to find this. This is difficult to find
    this. This is

    intractable. Why is it interractable? We don''t know P Why is it interractable?
    We don''t know P

    data. data.

    How are we going to calculate grad of How are we going to calculate grad of How
    are we going to calculate grad of

    log of P of data? It''s it''s it it log of P of data? It''s it''s it it log of
    P of data? It''s it''s it it

    appears impossible. appears impossible. appears impossible.

    However, there was a paper there was a paper which was released by there was a
    paper which was released by

    these two people in the year 2005 which

    showed that this score matching showed that this score matching showed that this
    score matching

    objective can be converted into a objective can be converted into a objective
    can be converted into a

    tractable score matching objective. Let''s try to look at this paper so that Let''s
    try to look at this paper so that

    we develop some kind of an appreciation we develop some kind of an appreciation
    we develop some kind of an appreciation

    for the work which has happened over two for the work which has happened over
    two for the work which has happened over two

    decades of of literature to reach where decades of of literature to reach where
    decades of of literature to reach where

    we are right now. we are right now. we are right now.

    So these are the authors. I I I do not So these are the authors. I I I do not
    So these are the authors. I I I do not

    know how to pronounce this name. know how to pronounce this name.'
  concept_slugs:
  - langevin-dynamics
  - score-function
- idx: 66
  start_sec: 3940.079
  end_sec: 4007.839
  text: 'know how to pronounce this name.

    uh however they they came up with a uh however they they came up with a uh however
    they they came up with a

    technique to technique to technique to

    distill that objective function into distill that objective function into distill
    that objective function into

    something which is tractable. This is something which is tractable. This is something
    which is tractable. This is

    very similar to what we did with the very similar to what we did with the very
    similar to what we did with the

    elbow objective in variation elbow objective in variation elbow objective in variation

    autoenccoders. autoenccoders. autoenccoders.

    However, this is a bit different because However, this is a bit different because
    However, this is a bit different because

    we are not directly we are not directly we are not directly

    calculating the lower bound on it, but calculating the lower bound on it, but
    calculating the lower bound on it, but

    rather we are finding a rather we are finding a rather we are finding a

    uh a term or an expression whose uh a term or an expression whose uh a term or
    an expression whose

    expected value is exactly the same as expected value is exactly the same as expected
    value is exactly the same as

    the expected value of the term that we the expected value of the term that we
    the expected value of the term that we

    want to calculate. want to calculate. want to calculate.

    So in a way it''s not an approximation So in a way it''s not an approximation
    So in a way it''s not an approximation

    like elbow but it''s it''s it''s a like elbow but it''s it''s it''s a like elbow
    but it''s it''s it''s a

    different representation of the same different representation of the same different
    representation of the same

    expression. Okay. So this was this is the uh this is Okay. So this was this is
    the uh this is

    what we want what we want what we want

    what we want to calculate and uh this this paper kind of and uh this this paper
    kind of

    reformulated this objective as reformulated this objective as reformulated this
    objective as

    a summation of this and a constant. a summation of this and a constant.'
  concept_slugs:
  - langevin-dynamics
  - score-function
- idx: 67
  start_sec: 4007.839
  end_sec: 4081.44
  text: 'a summation of this and a constant.

    So basically minimizing this meant that So basically minimizing this meant that
    So basically minimizing this meant that

    we want to minimize this and you see here we do not have the SS and you see here
    we do not have the SS

    data anymore over here or S of X which data anymore over here or S of X which
    data anymore over here or S of X which

    is the true is the true is the true

    we do not have we do not have we do not have

    somehow magically somehow magically somehow magically

    the score function has disappeared from the score function has disappeared from
    the score function has disappeared from

    the loss the loss the loss

    and it has been replaced by two terms. and it has been replaced by two terms.
    and it has been replaced by two terms.

    The first term is the trace The first term is the trace The first term is the
    trace

    of grad of S S5 of X. So we are taking of grad of S S5 of X. So we are taking
    of grad of S S5 of X. So we are taking

    the gradient of the score function and the gradient of the score function and
    the gradient of the score function and

    the second term is the the second term is the the second term is the

    square error of the square error of the square error of the

    score function matrix. score function matrix. score function matrix.

    So let us try to understand both of So let us try to understand both of So let
    us try to understand both of

    these terms and exactly what they mean. these terms and exactly what they mean.
    these terms and exactly what they mean.

    First let us look at the trace. First let us look at the trace. First let us look
    at the trace.

    What is the meaning of a trace of a What is the meaning of a trace of a What is
    the meaning of a trace of a

    matrix? matrix? matrix?

    Let us say we have a matrix which looks Let us say we have a matrix which looks
    Let us say we have a matrix which looks

    like this. A1 A2 A3 like this. A1 A2 A3'
  concept_slugs:
  - langevin-dynamics
  - score-function
- idx: 68
  start_sec: 4081.44
  end_sec: 4151.03
  text: 'like this. A1 A2 A3

    A4 A5 A6 A4 A5 A6 A4 A5 A6

    A7 A8 and A9. So the trace of this A7 A8 and A9. So the trace of this A7 A8 and
    A9. So the trace of this

    matrix is simply the addition of a1 + a5 matrix is simply the addition of a1 +
    a5 matrix is simply the addition of a1 + a5

    plus a9. This is the trace and This is the trace and

    what we are doing here is we are simply what we are doing here is we are simply
    what we are doing here is we are simply

    taking a1 squared plus taking a1 squared plus taking a1 squared plus

    a2 squar + a3 squar + dot dot dot a9 a2 squar + a3 squar + dot dot dot a9 a2 squar
    + a3 squar + dot dot dot a9

    squared and dividing it by 2. squared and dividing it by 2. squared and dividing
    it by 2.

    And this is something which we can And this is something which we can And this
    is something which we can

    easily calculate. Right? Once we have easily calculate. Right? Once we have easily
    calculate. Right? Once we have

    this this this

    uh this is only dependent on the network uh this is only dependent on the network
    uh this is only dependent on the network

    that we want to train. that we want to train. that we want to train.

    So now suddenly we have an objective So now suddenly we have an objective So now
    suddenly we have an objective

    function where function where function where

    every single entity depends on the every single entity depends on the every single
    entity depends on the

    neural network that we want to train. So neural network that we want to train.
    So neural network that we want to train. So

    we are no longer dependent on something we are no longer dependent on something
    we are no longer dependent on something

    which is interactable. Now both of these terms they mean Now both of these terms
    they mean

    something very unique. Even if you don''t something very unique. Even if you don''t
    something very unique. Even if you don''t

    understand the derivation of this understand the derivation of this understand
    the derivation of this

    uh it is it is completely fine for our'
  concept_slugs:
  - langevin-dynamics
  - score-function
- idx: 69
  start_sec: 4151.03
  end_sec: 4205.75
  text: 'uh it is it is completely fine for our uh it is it is completely fine for
    our

    purposes what we need to understand is purposes what we need to understand is
    purposes what we need to understand is

    the intuitive meaning behind both of the intuitive meaning behind both of the
    intuitive meaning behind both of

    these terms. The first term which is the these terms. The first term which is
    the these terms. The first term which is the

    trace let''s see trace let''s see trace let''s see

    the trace term measures the divergence the trace term measures the divergence
    the trace term measures the divergence

    of your arrows. It measures if the of your arrows. It measures if the of your
    arrows. It measures if the

    arrows are spreading out or if the arrows are spreading out or if the arrows are
    spreading out or if the

    arrows are arrows are arrows are

    are converging at a specific point. are converging at a specific point. are converging
    at a specific point.

    So if we have a trace which is positive, So if we have a trace which is positive,
    So if we have a trace which is positive,

    the arrows are exploding outwards like a the arrows are exploding outwards like
    a the arrows are exploding outwards like a

    bomb which is going off. And if we have bomb which is going off. And if we have
    bomb which is going off. And if we have

    a negative trace, the arrows are sucking a negative trace, the arrows are sucking
    a negative trace, the arrows are sucking

    inwards. inwards. inwards.

    And since we are minimizing the loss, we And since we are minimizing the loss,
    we And since we are minimizing the loss, we

    are trying to minimize this trace. Which are trying to minimize this trace. Which
    are trying to minimize this trace. Which

    means we want to make it as negative as means we want to make it as negative as
    means we want to make it as negative as

    possible. Which means that we want to possible. Which means that we want to possible.
    Which means that we want to

    make our data samples look as syncs. make our data samples look as syncs. make
    our data samples look as syncs.

    Which makes a lot of sense, right? In'
  concept_slugs:
  - langevin-dynamics
  - score-function
- idx: 70
  start_sec: 4205.75
  end_sec: 4274.48
  text: 'Which makes a lot of sense, right? In Which makes a lot of sense, right?
    In

    the previous example that we looked at the previous example that we looked at
    the previous example that we looked at

    these these were the two let''s say these these were the two let''s say these
    these were the two let''s say

    probability contours. So what this first probability contours. So what this first
    probability contours. So what this first

    term does is it makes the score function term does is it makes the score function
    term does is it makes the score function

    looks like this. So that the true data the region around So that the true data
    the region around

    the true data appears like a drain the true data appears like a drain the true
    data appears like a drain

    which is what we want because if if which is what we want because if if which
    is what we want because if if

    someone starts from here because of this sink or drain like because of this sink
    or drain like

    structure you''ll move towards the actual structure you''ll move towards the actual
    structure you''ll move towards the actual

    data point. data point. data point.

    So So

    positive trace looks like this. It''s positive trace looks like this. It''s positive
    trace looks like this. It''s

    almost like it''s diverging outwards and almost like it''s diverging outwards
    and almost like it''s diverging outwards and

    negative trace looks like this. It''s negative trace looks like this. It''s negative
    trace looks like this. It''s

    diverging inwards. diverging inwards. diverging inwards.

    In fluid flows, people often equate In fluid flows, people often equate In fluid
    flows, people often equate

    these trace terms to zero these trace terms to zero these trace terms to zero

    in in in many of the cases because you in in in many of the cases because you
    in in in many of the cases because you

    cannot have fluid particles which are cannot have fluid particles which are cannot
    have fluid particles which are

    expanding or contracting. expanding or contracting. expanding or contracting.

    Okay. Anyway, so this is the first term Okay. Anyway, so this is the first term
    Okay. Anyway, so this is the first term

    where we are trying to make the data where we are trying to make the data'
  concept_slugs:
  - langevin-dynamics
  - score-function
- idx: 71
  start_sec: 4274.48
  end_sec: 4327.679
  text: 'where we are trying to make the data

    samples appear as syncs. samples appear as syncs. samples appear as syncs.

    which is what you see over here also. If which is what you see over here also.
    If which is what you see over here also. If

    you see this this this uh you see this this this uh you see this this this uh

    probably that image we do not have at probably that image we do not have at probably
    that image we do not have at

    the moment. But if you just look at this the moment. But if you just look at this
    the moment. But if you just look at this

    image, this area is like a sink, right? image, this area is like a sink, right?
    image, this area is like a sink, right?

    The arrows appear like this oriented The arrows appear like this oriented The
    arrows appear like this oriented

    towards that region from all directions. towards that region from all directions.
    towards that region from all directions.

    So this term is intuitive. The second So this term is intuitive. The second So
    this term is intuitive. The second

    term, it measures the length or the term, it measures the length or the term,
    it measures the length or the

    strength of your arrows. It wants the strength of your arrows. It wants the strength
    of your arrows. It wants the

    arrows to be as as small as possible. So arrows to be as as small as possible.
    So arrows to be as as small as possible. So

    you want this squared term to be zero. you want this squared term to be zero.
    you want this squared term to be zero.

    So you want the arrows to be as small as So you want the arrows to be as small
    as So you want the arrows to be as small as

    possible. Why do you want small arrows? possible. Why do you want small arrows?
    possible. Why do you want small arrows?

    It''s because regions where P of data is It''s because regions where P of data
    is It''s because regions where P of data is

    high will have more score and contribute high will have more score and contribute
    high will have more score and contribute

    more to this term. more to this term.'
  concept_slugs:
  - langevin-dynamics
  - score-function
- idx: 72
  start_sec: 4327.679
  end_sec: 4378.87
  text: 'more to this term.

    So the this term drives So the this term drives So the this term drives

    scores to zero in the higher probability scores to zero in the higher probability
    scores to zero in the higher probability

    areas and those locations become areas and those locations become areas and those
    locations become

    stationary. So now let''s say in in the stationary. So now let''s say in in the
    stationary. So now let''s say in in the

    example of the two mountain case where example of the two mountain case where
    example of the two mountain case where

    this was the probability this was the probability this was the probability

    this was the area where the probability this was the area where the probability
    this was the area where the probability

    was maximum. What our formulation does was maximum. What our formulation does
    was maximum. What our formulation does

    is areas where the probability is is areas where the probability is is areas where
    the probability is

    maximum high probability areas it will maximum high probability areas it will
    maximum high probability areas it will

    force the score to be zero. Which means force the score to be zero. Which means
    force the score to be zero. Which means

    that once someone comes here they will that once someone comes here they will
    that once someone comes here they will

    not be guided anywhere. It is a not be guided anywhere. It is a not be guided
    anywhere. It is a

    stationary point. They will just sit stationary point. They will just sit stationary
    point. They will just sit

    there which is what we want. Right? We there which is what we want. Right? We
    there which is what we want. Right? We

    want the sink to divert the want the sink to divert the want the sink to divert
    the

    people towards the actual samples and people towards the actual samples and people
    towards the actual samples and

    then once they are diverted you want then once they are diverted you want then
    once they are diverted you want

    them to sit there which is what uh them to sit there which is what uh them to
    sit there which is what uh

    happens with this term. So the locations happens with this term. So the locations
    happens with this term. So the locations

    become stationary.'
  concept_slugs:
  - langevin-dynamics
  - score-function
- idx: 73
  start_sec: 4381.83
  end_sec: 4437.76
  text: 'Now uh once we have understood this, Now uh once we have understood this,

    this is where the actual training of the this is where the actual training of
    the this is where the actual training of the

    uh scores happen so that they match with uh scores happen so that they match with
    uh scores happen so that they match with

    the the the

    real scores as much as possible. And we real scores as much as possible. And we
    real scores as much as possible. And we

    will take a very interesting practical will take a very interesting practical
    will take a very interesting practical

    example to understand how this example to understand how this example to understand
    how this

    formulation is used formulation is used formulation is used

    to learn the score function. to learn the score function. to learn the score function.

    The example that we will take is we will The example that we will take is we will
    The example that we will take is we will

    assume that these are the data samples. assume that these are the data samples.
    assume that these are the data samples.

    Remember we are not assuming that the Remember we are not assuming that the Remember
    we are not assuming that the

    probability is known here. We are only probability is known here. We are only
    probability is known here. We are only

    assuming that the data samples is known. assuming that the data samples is known.
    assuming that the data samples is known.

    And from this we want to predict the And from this we want to predict the And
    from this we want to predict the

    score function from this data. We will not stop at this though. We''ll We will
    not stop at this though. We''ll

    predict the score function and then predict the score function and then predict
    the score function and then

    we''ll sample through land dynamics to we''ll sample through land dynamics to
    we''ll sample through land dynamics to

    see if we can find any new points. see if we can find any new points. see if we
    can find any new points.

    uh which belong to this underlying uh which belong to this underlying uh which
    belong to this underlying

    distribution. So in a way we will take a distribution. So in a way we will take
    a'
  concept_slugs:
  - langevin-dynamics
  - score-function
- idx: 74
  start_sec: 4437.76
  end_sec: 4518.79
  text: 'distribution. So in a way we will take a

    look at the whole uh whole pipeline. look at the whole uh whole pipeline. look
    at the whole uh whole pipeline.

    Okay, let''s try to understand this. Okay, let''s try to understand this. Okay,
    let''s try to understand this.

    We''ll look at uh this very interesting We''ll look at uh this very interesting
    We''ll look at uh this very interesting

    Google collab notebook. Google collab notebook. Google collab notebook.

    So when I come across core function, it So when I come across core function, it
    So when I come across core function, it

    reminds me of some of the concepts in reminds me of some of the concepts in reminds
    me of some of the concepts in

    fluid mechanics which I had learned. So fluid mechanics which I had learned. So
    fluid mechanics which I had learned. So

    it gives me a lot of pleasure to it gives me a lot of pleasure to it gives me
    a lot of pleasure to

    understand them. understand them. understand them.

    Okay. So in the first uh step we Okay. So in the first uh step we Okay. So in
    the first uh step we

    set up the data. We generate two set up the data. We generate two set up the data.
    We generate two

    interlocking moon shapes interlocking moon shapes interlocking moon shapes

    which look something like this. Okay. So the training data looks like Okay. So
    the training data looks like

    this. And in the in the next step what this. And in the in the next step what
    this. And in the in the next step what

    we do is we define the score neural we do is we define the score neural we do
    is we define the score neural

    network which network which network which

    looks like this. It is a simple multi-layer perceptron It is a simple multi-layer
    perceptron

    where as an output we predict the score where as an output we predict the score
    where as an output we predict the score

    values and this is where you and this is where you

    uh uh

    define your loss. We can see that the define your loss. We can see that the define
    your loss. We can see that the

    loss is made up of two terms. The first'
  concept_slugs:
  - langevin-dynamics
  - score-function
- idx: 75
  start_sec: 4518.79
  end_sec: 4570.159
  text: 'loss is made up of two terms. The first loss is made up of two terms. The
    first

    is the trace of the Jacobian is the trace of the Jacobian is the trace of the
    Jacobian

    which is what we discussed before which is what we discussed before which is what
    we discussed before

    and the second is the nom square which and the second is the nom square which
    and the second is the nom square which

    is over here. is over here. is over here.

    Now you can see that both of these terms Now you can see that both of these terms
    Now you can see that both of these terms

    depend on this score prediction matrix depend on this score prediction matrix
    depend on this score prediction matrix

    which is what our model has predicted. which is what our model has predicted.
    which is what our model has predicted.

    It does not depend on the true scores at It does not depend on the true scores
    at It does not depend on the true scores at

    all. So we can easily define the loss all. So we can easily define the loss all.
    So we can easily define the loss

    function without knowing the true function without knowing the true function without
    knowing the true

    scores. So this is one of the most scores. So this is one of the most scores.
    So this is one of the most

    important step which is the score important step which is the score important
    step which is the score

    matching loss which all of us need to matching loss which all of us need to matching
    loss which all of us need to

    understand very clearly. This is exactly understand very clearly. This is exactly
    understand very clearly. This is exactly

    the same that we have discussed in the same that we have discussed in the same
    that we have discussed in

    theory. Okay. Uh let''s let''s go ahead. Okay. Uh let''s let''s go ahead.

    The output of the score network is two The output of the score network is two
    The output of the score network is two

    because it is a vector and we have because it is a vector and we have because
    it is a vector and we have

    predictions for the x score and the y predictions for the x score and the y'
  concept_slugs:
  - langevin-dynamics
  - score-function
- idx: 76
  start_sec: 4570.159
  end_sec: 4620.07
  text: 'predictions for the x score and the y

    score to create a vector. score to create a vector. score to create a vector.

    Next we have a training loop which is a Next we have a training loop which is
    a Next we have a training loop which is a

    standard training loop in machine standard training loop in machine standard training
    loop in machine

    learning. And here I have trained for learning. And here I have trained for learning.
    And here I have trained for

    800 epochs and you can see the loss 800 epochs and you can see the loss 800 epochs
    and you can see the loss

    going down with the time. going down with the time. going down with the time.

    And then finally as you uh train uh your And then finally as you uh train uh your
    And then finally as you uh train uh your

    scores to scores to scores to

    predict the true scores even without predict the true scores even without predict
    the true scores even without

    knowing the value of them just from the knowing the value of them just from the
    knowing the value of them just from the

    data samples. data samples. data samples.

    We ask this question that which way We ask this question that which way We ask
    this question that which way

    towards the data and uh this is what we towards the data and uh this is what we
    towards the data and uh this is what we

    get towards the end which is amazing get towards the end which is amazing get
    towards the end which is amazing

    right this this this looks like a valid right this this this looks like a valid
    right this this this looks like a valid

    score speed because we are pointing score speed because we are pointing score
    speed because we are pointing

    towards the data and if you look at any towards the data and if you look at any
    towards the data and if you look at any

    single point which is near your data single point which is near your data single
    point which is near your data

    distribution you can see that it doesn''t distribution you can see that it doesn''t
    distribution you can see that it doesn''t

    completely appear like a sync but there'
  concept_slugs:
  - langevin-dynamics
  - score-function
- idx: 77
  start_sec: 4620.07
  end_sec: 4669.669
  text: 'completely appear like a sync but there completely appear like a sync but
    there

    are arrows coming in from the left and are arrows coming in from the left and
    are arrows coming in from the left and

    the right arrows are not coming in from the right arrows are not coming in from
    the right arrows are not coming in from

    the top or the bottom here which is the top or the bottom here which is the top
    or the bottom here which is

    interesting interesting interesting

    But it it it does appear like it''s But it it it does appear like it''s But it
    it it does appear like it''s

    creating syncs over there and these data creating syncs over there and these data
    creating syncs over there and these data

    points are stationary. So you will find points are stationary. So you will find
    points are stationary. So you will find

    you not find arrows which are very close you not find arrows which are very close
    you not find arrows which are very close

    to your data samples. to your data samples. to your data samples.

    Now you might say that Rajat we have now Now you might say that Rajat we have
    now Now you might say that Rajat we have now

    predicted the scores. Let''s use langin predicted the scores. Let''s use langin
    predicted the scores. Let''s use langin

    dynamics and sample from it. Right? And dynamics and sample from it. Right? And
    dynamics and sample from it. Right? And

    what what we are going to do with what what we are going to do with what what
    we are going to do with

    languin dynamics is that languin dynamics is that languin dynamics is that

    let''s say this is the uh score field. We let''s say this is the uh score field.
    We let''s say this is the uh score field. We

    start with any point and langaming start with any point and langaming start with
    any point and langaming

    dynamics is going to take us to a final dynamics is going to take us to a final
    dynamics is going to take us to a final

    point. point. point.

    Similarly, we start from any other point Similarly, we start from any other point
    Similarly, we start from any other point

    we go to any other point. So we are'
  concept_slugs:
  - langevin-dynamics
  - score-function
- idx: 78
  start_sec: 4669.669
  end_sec: 4713.35
  text: 'we go to any other point. So we are we go to any other point. So we are

    going to see trajectories like these. going to see trajectories like these. going
    to see trajectories like these.

    And in this example, I have shown one And in this example, I have shown one And
    in this example, I have shown one

    single trajectory which is appearing in single trajectory which is appearing in
    single trajectory which is appearing in

    uh blue. So the trajectory starts over uh blue. So the trajectory starts over
    uh blue. So the trajectory starts over

    here which is the green dot and it ends here which is the green dot and it ends
    here which is the green dot and it ends

    over here. So you can see that it is over here. So you can see that it is over
    here. So you can see that it is

    ending at a place which is almost ending at a place which is almost ending at
    a place which is almost

    similar to where the data samples lie similar to where the data samples lie similar
    to where the data samples lie

    which is which is amazing right and it which is which is amazing right and it
    which is which is amazing right and it

    appears like again a drunken hiker which appears like again a drunken hiker which
    appears like again a drunken hiker which

    is going zigzag and the hiker finally is going zigzag and the hiker finally is
    going zigzag and the hiker finally

    lands to a place where you find the lands to a place where you find the lands
    to a place where you find the

    samples. So this lecture felt like a samples. So this lecture felt like a samples.
    So this lecture felt like a

    treasure hunt in a way that the treasure treasure hunt in a way that the treasure
    treasure hunt in a way that the treasure

    is located in some valleys with a is located in some valleys with a is located
    in some valleys with a

    minimum energy and we are trying to minimum energy and we are trying to minimum
    energy and we are trying to

    locate those valleys but we also locate those valleys but we also locate those
    valleys but we also

    perturve ourselves from the valleys so'
  concept_slugs:
  - langevin-dynamics
  - score-function
- idx: 79
  start_sec: 4713.35
  end_sec: 4759.6
  text: 'perturve ourselves from the valleys so perturve ourselves from the valleys
    so

    that we don''t miss any other treasures that we don''t miss any other treasures
    that we don''t miss any other treasures

    which are even bigger than what we have which are even bigger than what we have
    which are even bigger than what we have

    found. So we appear like a drunken hiker found. So we appear like a drunken hiker
    found. So we appear like a drunken hiker

    and we find these treasures finally and we find these treasures finally and we
    find these treasures finally

    and uh this paper is immensely helpful and uh this paper is immensely helpful
    and uh this paper is immensely helpful

    for us to uh derive these score matching for us to uh derive these score matching
    for us to uh derive these score matching

    loss. We have not gone into the uh loss. We have not gone into the uh loss. We
    have not gone into the uh

    details of it. It is slightly involved details of it. It is slightly involved
    details of it. It is slightly involved

    but I''m very grateful to their but I''m very grateful to their but I''m very
    grateful to their

    contribution because without that we contribution because without that we contribution
    because without that we

    will not have diffusion models that we will not have diffusion models that we
    will not have diffusion models that we

    see right now. see right now. see right now.

    Okay. So uh in the next chapter we will Okay. So uh in the next chapter we will
    Okay. So uh in the next chapter we will

    look at the foundational role of score look at the foundational role of score
    look at the foundational role of score

    function in modern diffusion models. function in modern diffusion models. function
    in modern diffusion models.

    Remember there are these two parallel Remember there are these two parallel Remember
    there are these two parallel

    tracks which I keep talking about but I tracks which I keep talking about but
    I tracks which I keep talking about but I

    have never made the connection between have never made the connection between
    have never made the connection between

    them yet. We will make the connection in them yet. We will make the connection
    in'
  concept_slugs:
  - langevin-dynamics
  - score-function
- idx: 80
  start_sec: 4759.6
  end_sec: 4815.76
  text: 'them yet. We will make the connection in

    the next lecture. the next lecture. the next lecture.

    So initially used to enable efficient So initially used to enable efficient So
    initially used to enable efficient

    training of EBMS the score function has training of EBMS the score function has
    training of EBMS the score function has

    now evolved into a central component of now evolved into a central component of
    now evolved into a central component of

    a new generation of generative models a new generation of generative models a
    new generation of generative models

    which is which is amazing. which is which is amazing. which is which is amazing.

    And uh in this lecture we looked at a And uh in this lecture we looked at a And
    uh in this lecture we looked at a

    whole new framework which is based on whole new framework which is based on whole
    new framework which is based on

    energies. energies. energies.

    And uh similar to diffusion this is also And uh similar to diffusion this is also
    And uh similar to diffusion this is also

    inspired from physics. inspired from physics. inspired from physics.

    We want to we want our data to lie in We want to we want our data to lie in We
    want to we want our data to lie in

    configurations where the energy is configurations where the energy is configurations
    where the energy is

    minimum. minimum.

    And since we cannot predict the energy And since we cannot predict the energy
    And since we cannot predict the energy

    function directly, function directly, function directly,

    since the uh partition function which is since the uh partition function which
    is since the uh partition function which is

    the integral of the energy function over the integral of the energy function over
    the integral of the energy function over

    all possible data points is intractable, all possible data points is intractable,
    all possible data points is intractable,

    we define another objective function we define another objective function we define
    another objective function

    which is tractable and that is based on which is tractable and that is based on
    which is tractable and that is based on

    a term which is called as scores. a term which is called as scores. a term which
    is called as scores.

    Scores are given by gradient of Scores are given by gradient of'
  concept_slugs:
  - langevin-dynamics
  - score-function
- idx: 81
  start_sec: 4815.76
  end_sec: 4862.31
  text: 'Scores are given by gradient of

    logarithm of uh the probability. It logarithm of uh the probability. It logarithm
    of uh the probability. It

    turns out that the scores appear as turns out that the scores appear as turns
    out that the scores appear as

    compass for us towards the data. If you compass for us towards the data. If you
    compass for us towards the data. If you

    if you are at any point in the grid, you if you are at any point in the grid,
    you if you are at any point in the grid, you

    take your compass out, it points to the take your compass out, it points to the
    take your compass out, it points to the

    direction of where exactly is the data. direction of where exactly is the data.
    direction of where exactly is the data.

    Now if we have this core function, we Now if we have this core function, we Now
    if we have this core function, we

    looked at a technique called long lang looked at a technique called long lang
    looked at a technique called long lang

    dynamics which allows us to sample from dynamics which allows us to sample from
    dynamics which allows us to sample from

    sample data sample data sample data

    which appears to be very close to the which appears to be very close to the which
    appears to be very close to the

    points where the distribution of the points where the distribution of the points
    where the distribution of the

    data lies in. We looked at an example data lies in. We looked at an example data
    lies in. We looked at an example

    where it''s like two mountains and we where it''s like two mountains and we where
    it''s like two mountains and we

    started from any point and we reached started from any point and we reached started
    from any point and we reached

    towards one of the peak of the mountains towards one of the peak of the mountains
    towards one of the peak of the mountains

    using lang dynamics. using lang dynamics. using lang dynamics.

    Now the question is how do we train our Now the question is how do we train our
    Now the question is how do we train our

    neural network to match the scores and'
  concept_slugs:
  - langevin-dynamics
  - score-function
- idx: 82
  start_sec: 4862.31
  end_sec: 4905.28
  text: 'neural network to match the scores and neural network to match the scores
    and

    to do that we use a score matching loss to do that we use a score matching loss
    to do that we use a score matching loss

    where we use an alternative expression where we use an alternative expression
    where we use an alternative expression

    which is tractable which which is tractable which which is tractable which

    very nicely does not involve anything to very nicely does not involve anything
    to very nicely does not involve anything to

    do with the probability of the data or do with the probability of the data or
    do with the probability of the data or

    the energy of the true data. I''m again the energy of the true data. I''m again
    the energy of the true data. I''m again

    very fascinated with the mathematics of very fascinated with the mathematics of
    very fascinated with the mathematics of

    it all. simple mathematical tricks can it all. simple mathematical tricks can
    it all. simple mathematical tricks can

    uh uh

    become the markers towards the starter become the markers towards the starter
    become the markers towards the starter

    of a whole new framework where now we of a whole new framework where now we of
    a whole new framework where now we

    are seeing energy based models used in are seeing energy based models used in
    are seeing energy based models used in

    diffusion as well. Thank you everyone. diffusion as well. Thank you everyone.
    diffusion as well. Thank you everyone.

    We are proceeding very nicely in this We are proceeding very nicely in this We
    are proceeding very nicely in this

    course and I''m excited to teach the next course and I''m excited to teach the
    next course and I''m excited to teach the next

    concept which is the role of score concept which is the role of score concept
    which is the role of score

    function in modern diffusion models.'
  concept_slugs:
  - langevin-dynamics
  - score-function
---
# Lecture 5 - Energy Based Models | Score Function | Principles of Diffusion Models

See the structured chunks above.
