---
course_slug: cmu-10799-diffusion-flow
idx: 1
title: 'CMU 10799 S26: Lecture 4 - Score-based Models - Diffusion & Flow Matching'
video_url: https://www.youtube.com/watch?v=UEJxHpFEb04
duration_sec: null
chunks:
- idx: 0
  start_sec: 4.47
  end_sec: 57.27
  text: 'So let''s begin. Previously last class uh So let''s begin. Previously last
    class uh

    we have talked about what is diffusion we have talked about what is diffusion
    we have talked about what is diffusion

    model and essentially it''s just like um model and essentially it''s just like
    um model and essentially it''s just like um

    very nice way to turn noise into data. very nice way to turn noise into data.
    very nice way to turn noise into data.

    And how do we do that? Well, basically And how do we do that? Well, basically
    And how do we do that? Well, basically

    uh we in order to construct um the uh we in order to construct um the uh we in
    order to construct um the

    training data or the training signal, training data or the training signal, training
    data or the training signal,

    the supervision signal, we first start the supervision signal, we first start
    the supervision signal, we first start

    from our training data and then we from our training data and then we from our
    training data and then we

    gradually add noise until it becomes gradually add noise until it becomes gradually
    add noise until it becomes

    full Gausian noise. uh and then at uh full Gausian noise. uh and then at uh full
    Gausian noise. uh and then at uh

    you know at at testing time or at you know at at testing time or at you know at
    at testing time or at

    inference time we used to learn the inference time we used to learn the inference
    time we used to learn the

    model uh to gradually den noiseise uh model uh to gradually den noiseise uh model
    uh to gradually den noiseise uh

    and the and the process of adding noise and the and the process of adding noise
    and the and the process of adding noise

    is what we call a for process and then is what we call a for process and then
    is what we call a for process and then

    the process of dnoising is what we call the process of dnoising is what we call
    the process of dnoising is what we call

    a reversed process a reversed process a reversed process

    um reverse not um reverse not um reverse not

    reserve sorry um all right so just a'
  concept_slugs:
  - langevin-dynamics
  - score-function
  - score-matching
- idx: 1
  start_sec: 57.27
  end_sec: 104.479
  text: 'reserve sorry um all right so just a reserve sorry um all right so just a

    reminder what is the forward process reminder what is the forward process reminder
    what is the forward process

    basically ally between each step uh basically ally between each step uh basically
    ally between each step uh

    we''re adding some amount of gausian we''re adding some amount of gausian we''re
    adding some amount of gausian

    noise to the scale version of your noise to the scale version of your noise to
    the scale version of your

    previous uh data sample. Um so basically previous uh data sample. Um so basically
    previous uh data sample. Um so basically

    uh what''s going to h what''s happening in uh what''s going to h what''s happening
    in uh what''s going to h what''s happening in

    math is just uh you know defined as math is just uh you know defined as math is
    just uh you know defined as

    above. So like the your next time your above. So like the your next time your
    above. So like the your next time your

    next time step is equal to basically the next time step is equal to basically
    the next time step is equal to basically the

    scaled version of your previous time scaled version of your previous time scaled
    version of your previous time

    step plus some gian plus some scaled step plus some gian plus some scaled step
    plus some gian plus some scaled

    version of the gausian noise. version of the gausian noise. version of the gausian
    noise.

    All right. So, this is the this is a do All right. So, this is the this is a do
    All right. So, this is the this is a do

    that that you need to remember for the that that you need to remember for the
    that that you need to remember for the

    rest of your life. Um, all right. And uh rest of your life. Um, all right. And
    uh rest of your life. Um, all right. And uh

    what''s nice about it being Gausian is what''s nice about it being Gausian is
    what''s nice about it being Gausian is

    that basically because uh two gausians that basically because uh two gausians
    that basically because uh two gausians

    sums up together is another gausian and sums up together is another gausian and'
  concept_slugs:
  - langevin-dynamics
  - score-function
  - score-matching
- idx: 2
  start_sec: 104.479
  end_sec: 155.599
  text: 'sums up together is another gausian and

    you can just sum up a bunch of gausians. you can just sum up a bunch of gausians.
    you can just sum up a bunch of gausians.

    So that''s why in the forward process you So that''s why in the forward process
    you So that''s why in the forward process you

    can actually you don''t actually need to can actually you don''t actually need
    to can actually you don''t actually need to

    have this cascading chain. uh what you have this cascading chain. uh what you
    have this cascading chain. uh what you

    can do is you can literally just like can do is you can literally just like can
    do is you can literally just like

    you can go from x0 and then you can you can go from x0 and then you can you can
    go from x0 and then you can

    directly get the distribution at any directly get the distribution at any directly
    get the distribution at any

    time step. Um so basically what''s time step. Um so basically what''s time step.
    Um so basically what''s

    happening is that um like we can we can happening is that um like we can we can
    happening is that um like we can we can

    just like calculate some coefficients just like calculate some coefficients just
    like calculate some coefficients

    and then we can directly get the and then we can directly get the and then we
    can directly get the

    distribution of each time step um and given any data each time step um and given
    any data

    sample right and basically XT which is sample right and basically XT which is
    sample right and basically XT which is

    the noisy sample at at time step t is the noisy sample at at time step t is the
    noisy sample at at time step t is

    equal to your the scale version of your equal to your the scale version of your
    equal to your the scale version of your

    training data plus some scale version of training data plus some scale version
    of training data plus some scale version of

    the gausian noise again. Okay, so this the gausian noise again. Okay, so this
    the gausian noise again. Okay, so this

    is the diffusion for process. All right. is the diffusion for process. All right.'
  concept_slugs:
  - langevin-dynamics
  - score-function
  - score-matching
- idx: 3
  start_sec: 155.599
  end_sec: 204.879
  text: 'is the diffusion for process. All right.

    Now, uh how now that we uh we have the Now, uh how now that we uh we have the
    Now, uh how now that we uh we have the

    forward process to train to construct forward process to train to construct forward
    process to train to construct

    our supervision signals, how do we learn our supervision signals, how do we learn
    our supervision signals, how do we learn

    a model to D noiseis and once we have a model to D noiseis and once we have a
    model to D noiseis and once we have

    the model, how do we actually sample the model, how do we actually sample the
    model, how do we actually sample

    from that model? All right. So basic from that model? All right. So basic from
    that model? All right. So basic

    basically uh naively uh you can define basically uh naively uh you can define
    basically uh naively uh you can define

    another gausian uh distribution uh to go another gausian uh distribution uh to
    go another gausian uh distribution uh to go

    backwards backwards backwards

    essentially. Um but uh basically DDPM uh essentially. Um but uh basically DDPM
    uh essentially. Um but uh basically DDPM uh

    which is the main model that we learned which is the main model that we learned
    which is the main model that we learned

    the last time tells us that if we just the last time tells us that if we just
    the last time tells us that if we just

    like simplify everything we if we just like simplify everything we if we just
    like simplify everything we if we just

    like simplify all the settings for like simplify all the settings for like simplify
    all the settings for

    example we just like assume that we we example we just like assume that we we
    example we just like assume that we we

    we fix the variance of the backore we fix the variance of the backore we fix the
    variance of the backore

    process then we only need to learn the process then we only need to learn the
    process then we only need to learn the

    mean of the gausian uh and in addition mean of the gausian uh and in addition'
  concept_slugs:
  - langevin-dynamics
  - score-function
  - score-matching
- idx: 4
  start_sec: 204.879
  end_sec: 248.959
  text: 'mean of the gausian uh and in addition

    we can actually rewrite this mean this we can actually rewrite this mean this
    we can actually rewrite this mean this

    prediction of mean into something that prediction of mean into something that
    prediction of mean into something that

    is with respect to is with respect to is with respect to

    with respect to the prediction of the with respect to the prediction of the with
    respect to the prediction of the

    noise and that just becomes like you''re noise and that just becomes like you''re
    noise and that just becomes like you''re

    learning a noise predictor or you''re learning a noise predictor or you''re learning
    a noise predictor or you''re

    learning a dino noiser essentially right learning a dino noiser essentially right
    learning a dino noiser essentially right

    so at training time what you do is just so at training time what you do is just
    so at training time what you do is just

    literally do regression on the noise literally do regression on the noise literally
    do regression on the noise

    that you''re adding to your in in your that you''re adding to your in in your
    that you''re adding to your in in your

    forward process uh and then in the at forward process uh and then in the at forward
    process uh and then in the at

    sampling time you just basically do okay sampling time you just basically do okay
    sampling time you just basically do okay

    my current time stamp minus a scaled my current time stamp minus a scaled my current
    time stamp minus a scaled

    version of the noise that I predicted version of the noise that I predicted version
    of the noise that I predicted

    plus some you know exploration plus some you know exploration plus some you know
    exploration

    randomness and then I''ll get the and randomness and then I''ll get the and randomness
    and then I''ll get the and

    then I just like go through the entire then I just like go through the entire
    then I just like go through the entire

    chain and I''ll get the sampling and uh chain and I''ll get the sampling and uh
    chain and I''ll get the sampling and uh

    last time there''s some questions about last time there''s some questions about'
  concept_slugs:
  - langevin-dynamics
  - score-function
  - score-matching
- idx: 5
  start_sec: 248.959
  end_sec: 294.24
  text: 'last time there''s some questions about

    why should we do this reparameterization why should we do this reparameterization
    why should we do this reparameterization

    well because doing this regression is well because doing this regression is well
    because doing this regression is

    very is much much easier to train uh very is much much easier to train uh very
    is much much easier to train uh

    than if you just learn this um this very than if you just learn this um this very
    than if you just learn this um this very

    complicated mean which like you know has complicated mean which like you know
    has complicated mean which like you know has

    like very complicated structures at like very complicated structures at like very
    complicated structures at

    different time steps. All right, cool. different time steps. All right, cool.
    different time steps. All right, cool.

    So this is what we learned the last So this is what we learned the last So this
    is what we learned the last

    time. Um so so far we have seen a lot of time. Um so so far we have seen a lot
    of time. Um so so far we have seen a lot of

    gener models right so this is uh this is gener models right so this is uh this
    is gener models right so this is uh this is

    what we seen the first uh in the first what we seen the first uh in the first
    what we seen the first uh in the first

    lecture uh we have talked about uh in lecture uh we have talked about uh in lecture
    uh we have talked about uh in

    details auto reggressive models and VAEs details auto reggressive models and VAEs
    details auto reggressive models and VAEs

    and uh we haven''t talked about what is and uh we haven''t talked about what is
    and uh we haven''t talked about what is

    normalizing flow and what is EVM but normalizing flow and what is EVM but normalizing
    flow and what is EVM but

    like we''re just going to briefly mention like we''re just going to briefly mention
    like we''re just going to briefly mention

    this uh before I do that does anyone this uh before I do that does anyone'
  concept_slugs:
  - langevin-dynamics
  - score-function
  - score-matching
- idx: 6
  start_sec: 294.24
  end_sec: 345.52
  text: 'this uh before I do that does anyone

    know in the audience what is normalizing know in the audience what is normalizing
    know in the audience what is normalizing

    flow by any No way. Nobody know. No way. Nobody know.

    Wow. Okay. I feel a little bit sad, but Wow. Okay. I feel a little bit sad, but
    Wow. Okay. I feel a little bit sad, but

    this is okay. Um, yeah, it it used to be this is okay. Um, yeah, it it used to
    be this is okay. Um, yeah, it it used to be

    pretty popular, I guess, but there''s a pretty popular, I guess, but there''s
    a pretty popular, I guess, but there''s a

    reason why it''s not popular. Uh, but reason why it''s not popular. Uh, but reason
    why it''s not popular. Uh, but

    normalizing flow is basically uh imagine normalizing flow is basically uh imagine
    normalizing flow is basically uh imagine

    that you''re like, you know how like in that you''re like, you know how like in
    that you''re like, you know how like in

    VA we''re learning like a encoder and VA we''re learning like a encoder and VA
    we''re learning like a encoder and

    decoder. Well, now basically you just decoder. Well, now basically you just decoder.
    Well, now basically you just

    say that okay, I''m just going to like uh say that okay, I''m just going to like
    uh say that okay, I''m just going to like uh

    predefine the structure of my gener predefine the structure of my gener predefine
    the structure of my gener

    model so that like basically the mapping model so that like basically the mapping
    model so that like basically the mapping

    from data to the latent quote unquote uh from data to the latent quote unquote
    uh from data to the latent quote unquote uh

    and and the mapping from the latent to and and the mapping from the latent to
    and and the mapping from the latent to

    the data is going to be inversible. So the data is going to be inversible. So
    the data is going to be inversible. So

    like basically the the mapping from data like basically the the mapping from data
    like basically the the mapping from data

    to uh latent is the inverse of the to uh latent is the inverse of the'
  concept_slugs:
  - langevin-dynamics
  - score-function
  - score-matching
- idx: 7
  start_sec: 345.52
  end_sec: 400.87
  text: 'to uh latent is the inverse of the

    mapping from latent to data. So this is mapping from latent to data. So this is
    mapping from latent to data. So this is

    sort of like normalizing flows. Um and sort of like normalizing flows. Um and
    sort of like normalizing flows. Um and

    then EBM is basically just like um then EBM is basically just like um then EBM
    is basically just like um

    because you know how like we like all because you know how like we like all because
    you know how like we like all

    the probability needs to add up to one, the probability needs to add up to one,
    the probability needs to add up to one,

    right? So the EBM is basically just right? So the EBM is basically just right?
    So the EBM is basically just

    saying that okay, we''re just going to saying that okay, we''re just going to
    saying that okay, we''re just going to

    learn like a unnormalized version of the learn like a unnormalized version of
    the learn like a unnormalized version of the

    distribution and then we''re going to distribution and then we''re going to distribution
    and then we''re going to

    normalize it later on using this thing normalize it later on using this thing
    normalize it later on using this thing

    called partition function. And this called partition function. And this called
    partition function. And this

    partition function is literally just partition function is literally just partition
    function is literally just

    like you know integrate like you know integrate like you know integrate

    all the probability together the all the probability together the all the probability
    together the

    anomorized probability together and this anomorized probability together and this
    anomorized probability together and this

    way you can get uh a normalized way you can get uh a normalized way you can get
    uh a normalized

    distribution. Okay cool. Um so distribution. Okay cool. Um so distribution. Okay
    cool. Um so

    unfortunately as we have learned before unfortunately as we have learned before
    unfortunately as we have learned before

    uh likelihood is very difficult to uh likelihood is very difficult to uh likelihood
    is very difficult to

    calculate. Why? Because uh for example calculate. Why? Because uh for example
    calculate. Why? Because uh for example

    if you have a auto reggressive models'
  concept_slugs:
  - langevin-dynamics
  - score-function
  - score-matching
- idx: 8
  start_sec: 400.87
  end_sec: 445.28
  text: 'if you have a auto reggressive models if you have a auto reggressive models

    then you need to break things up by the then you need to break things up by the
    then you need to break things up by the

    chain rule and then you need to chain rule and then you need to chain rule and
    then you need to

    calculate each components one by one. So calculate each components one by one.
    So calculate each components one by one. So

    if you have a very high dimensional data if you have a very high dimensional data
    if you have a very high dimensional data

    like image then you''re going to be like image then you''re going to be like image
    then you''re going to be

    calculating you know uh the the the calculating you know uh the the the calculating
    you know uh the the the

    chain rule for for each uh pixel and chain rule for for each uh pixel and chain
    rule for for each uh pixel and

    that''s just like really really painful. that''s just like really really painful.
    that''s just like really really painful.

    And then for VAEEs, while this is nice, And then for VAEEs, while this is nice,
    And then for VAEEs, while this is nice,

    but you''re actually um you''re still but you''re actually um you''re still but
    you''re actually um you''re still

    using a surrogated loss, meaning that using a surrogated loss, meaning that using
    a surrogated loss, meaning that

    you''re you''re actually not directly uh you''re you''re actually not directly
    uh you''re you''re actually not directly uh

    maximizing the likelihood. What you do maximizing the likelihood. What you do
    maximizing the likelihood. What you do

    is you''re maximizing the the like the is you''re maximizing the the like the
    is you''re maximizing the the like the

    lower bound of a likelihood. So, and lower bound of a likelihood. So, and lower
    bound of a likelihood. So, and

    that''s like after all the hard math that that''s like after all the hard math
    that that''s like after all the hard math that

    we did. So, this is like still kind of we did. So, this is like still kind of
    we did. So, this is like still kind of

    suboptimal. suboptimal. suboptimal.

    And uh for normalizing flow just by And uh for normalizing flow just by'
  concept_slugs:
  - langevin-dynamics
  - score-function
  - score-matching
- idx: 9
  start_sec: 445.28
  end_sec: 503.759
  text: 'And uh for normalizing flow just by

    looking at this can anyone tell me what looking at this can anyone tell me what
    looking at this can anyone tell me what

    potential problem it can it can have. Yes. Yes.

    >> Hard to get function inverse and >> Hard to get function inverse and >> Hard
    to get function inverse and

    >> very good. Very good. So for normalizing >> very good. Very good. So for normalizing
    >> very good. Very good. So for normalizing

    flow uh you''ll need weird architectures flow uh you''ll need weird architectures
    flow uh you''ll need weird architectures

    essentially to make sure that everything essentially to make sure that everything
    essentially to make sure that everything

    is invert invertible. And what about is invert invertible. And what about is invert
    invertible. And what about

    energy based model? What about EBM? energy based model? What about EBM? energy
    based model? What about EBM?

    Yes, partition function. Yeah, so this Yes, partition function. Yeah, so this
    Yes, partition function. Yeah, so this

    partition function is generally very partition function is generally very partition
    function is generally very

    very expensive to compute or just very expensive to compute or just very expensive
    to compute or just

    intractable in general. All right. H so intractable in general. All right. H so
    intractable in general. All right. H so

    likelihood is difficult to calculate, likelihood is difficult to calculate, likelihood
    is difficult to calculate,

    right? H so maybe let''s just go right? H so maybe let''s just go right? H so
    maybe let''s just go

    likelihood free. Would that be easier? likelihood free. Would that be easier?
    likelihood free. Would that be easier?

    Uh well for likelihood free model we Uh well for likelihood free model we Uh well
    for likelihood free model we

    have learned GANs and that dominated the have learned GANs and that dominated
    the have learned GANs and that dominated the

    genom or the image generate model for genom or the image generate model for genom
    or the image generate model for

    many many years like five years at many many years like five years at many many
    years like five years at

    least. Um but then it as we have learned least. Um but then it as we have learned'
  concept_slugs:
  - langevin-dynamics
  - score-function
  - score-matching
- idx: 10
  start_sec: 503.759
  end_sec: 564.23
  text: 'least. Um but then it as we have learned

    last time it also has a problem of like last time it also has a problem of like
    last time it also has a problem of like

    very unstable training and also it very unstable training and also it very unstable
    training and also it

    suffers a lot from mo collapse without suffers a lot from mo collapse without
    suffers a lot from mo collapse without

    any tricks. All right. any tricks. All right. any tricks. All right.

    So So So

    is there a better way to avoid directly is there a better way to avoid directly
    is there a better way to avoid directly

    calculating the likelihood? Then is calculating the likelihood? Then is calculating
    the likelihood? Then is

    there a better way to do sort of there a better way to do sort of there a better
    way to do sort of

    likelihood free training? This is the likelihood free training? This is the likelihood
    free training? This is the

    question we''re going to answer today. question we''re going to answer today.
    question we''re going to answer today.

    So if we think about it right, if we So if we think about it right, if we So if
    we think about it right, if we

    just want to do sampling like just just want to do sampling like just just want
    to do sampling like just

    forget about density estimation and forget about density estimation and forget
    about density estimation and

    everything like that for a bit. If we everything like that for a bit. If we everything
    like that for a bit. If we

    just want to do sampling, uh do we just want to do sampling, uh do we just want
    to do sampling, uh do we

    actually need to have a model to actually need to have a model to actually need
    to have a model to

    actually predict the likelihood of the actually predict the likelihood of the
    actually predict the likelihood of the

    data to sample from? >> Hold on. Many voices. Yeah. >> Hold on. Many voices. Yeah.

    to learn a transformation from some to learn a transformation from some to learn
    a transformation from some

    distribution that we know to the space distribution that we know to the space
    distribution that we know to the space

    of images rather than actually having to'
  concept_slugs:
  - langevin-dynamics
  - score-function
  - score-matching
- idx: 11
  start_sec: 564.23
  end_sec: 613.68
  text: 'of images rather than actually having to of images rather than actually having
    to

    comput the comput the comput the

    >> yes that''s right so you just need to >> yes that''s right so you just need
    to >> yes that''s right so you just need to

    learn a transformation right you don''t learn a transformation right you don''t
    learn a transformation right you don''t

    actually need the you don''t actually actually need the you don''t actually actually
    need the you don''t actually

    need the likelihood function and I think need the likelihood function and I think
    need the likelihood function and I think

    someone else also someone else also someone else also

    oh yeah oh yeah oh yeah

    >> you''re jumping ahead but yeah so >> you''re jumping ahead but yeah so >> you''re
    jumping ahead but yeah so

    basically the idea is that basically the idea is that basically the idea is that

    we don''t right and like we We just need we don''t right and like we We just need
    we don''t right and like we We just need

    a way to transform the like a data a way to transform the like a data a way to
    transform the like a data

    sample from whatever initial sample from whatever initial sample from whatever
    initial

    distribution that we have to a data distribution that we have to a data distribution
    that we have to a data

    sample in the desired distribution right sample in the desired distribution right
    sample in the desired distribution right

    so how do we do that how do we construct so how do we do that how do we construct
    so how do we do that how do we construct

    this transformation well the idea is this transformation well the idea is this
    transformation well the idea is

    that like I I''m sure you guys all know that like I I''m sure you guys all know
    that like I I''m sure you guys all know

    what is uh stoastic gradient descent what is uh stoastic gradient descent what
    is uh stoastic gradient descent

    right so this is what you train with right so this is what you train with right
    so this is what you train with

    model so what you do is you sort of just model so what you do is you sort of just'
  concept_slugs:
  - langevin-dynamics
  - score-function
  - score-matching
- idx: 12
  start_sec: 613.68
  end_sec: 660.32
  text: 'model so what you do is you sort of just

    like follow the gra so say suppose you like follow the gra so say suppose you
    like follow the gra so say suppose you

    have a gradient that gives you like u have a gradient that gives you like u have
    a gradient that gives you like u

    useful information about which direction useful information about which direction
    useful information about which direction

    and where and how how far uh you should and where and how how far uh you should
    and where and how how far uh you should

    go uh to get your desired outcome. So go uh to get your desired outcome. So go
    uh to get your desired outcome. So

    you can just like sort of like follow you can just like sort of like follow you
    can just like sort of like follow

    this this gradient with some soassity this this gradient with some soassity this
    this gradient with some soassity

    right and and then you can you can get right and and then you can you can get
    right and and then you can you can get

    the desired outcome. So basically what the desired outcome. So basically what
    the desired outcome. So basically what

    we can do here is sort of we we don''t we can do here is sort of we we don''t
    we can do here is sort of we we don''t

    really actually need the likelihood all really actually need the likelihood all
    really actually need the likelihood all

    we need is sort of like the gradient of we need is sort of like the gradient of
    we need is sort of like the gradient of

    the log likelihood so that we can just the log likelihood so that we can just
    the log likelihood so that we can just

    sort of do stoastic gradient descent or sort of do stoastic gradient descent or
    sort of do stoastic gradient descent or

    ascent I guess in in this case to ascent I guess in in this case to ascent I guess
    in in this case to

    maximize the log likelihood in the data maximize the log likelihood in the data
    maximize the log likelihood in the data

    space right so basically what you can space right so basically what you can'
  concept_slugs:
  - langevin-dynamics
  - score-function
  - score-matching
- idx: 13
  start_sec: 660.32
  end_sec: 705.2
  text: 'space right so basically what you can

    imagine is that you can start from imagine is that you can start from imagine
    is that you can start from

    anywhere on the data space so in this anywhere on the data space so in this anywhere
    on the data space so in this

    case it''s like this 2D plane right so case it''s like this 2D plane right so
    case it''s like this 2D plane right so

    you just say you Start from here and you just say you Start from here and you
    just say you Start from here and

    then you just follow the arrow. So then you just follow the arrow. So then you
    just follow the arrow. So

    follow the or like just like go with the follow the or like just like go with
    the follow the or like just like go with the

    flow flow flow

    essentially. So right so this is your essentially. So right so this is your essentially.
    So right so this is your

    gradient and then just like go and then gradient and then just like go and then
    gradient and then just like go and then

    you''re going to eventually wind up at you''re going to eventually wind up at
    you''re going to eventually wind up at

    some somewhere where it''s supposed to be some somewhere where it''s supposed
    to be some somewhere where it''s supposed to be

    high density. Um and this gradient is high density. Um and this gradient is high
    density. Um and this gradient is

    the gradient of the log likelihood. the gradient of the log likelihood. the gradient
    of the log likelihood.

    Okay. Or the the gradient of the real Okay. Or the the gradient of the real Okay.
    Or the the gradient of the real

    density the log density. Uh so what we density the log density. Uh so what we
    density the log density. Uh so what we

    call this is call this is call this is

    we call the score function right it''s we call the score function right it''s
    we call the score function right it''s

    the gradient with respect to x so with the gradient with respect to x so with
    the gradient with respect to x so with

    respect to the data point of the log respect to the data point of the log'
  concept_slugs:
  - langevin-dynamics
  - score-function
  - score-matching
- idx: 14
  start_sec: 705.2
  end_sec: 751.279
  text: 'respect to the data point of the log

    likelihood so what is happening is that likelihood so what is happening is that
    likelihood so what is happening is that

    like so and then again like what you can like so and then again like what you
    can like so and then again like what you can

    do is you can just sample in the data do is you can just sample in the data do
    is you can just sample in the data

    space and then go with the gradient in space and then go with the gradient in
    space and then go with the gradient in

    the data space and then you''re gonna the data space and then you''re gonna the
    data space and then you''re gonna

    eventually end up at somewhere where eventually end up at somewhere where eventually
    end up at somewhere where

    it''s supposed to be have high likelihood it''s supposed to be have high likelihood
    it''s supposed to be have high likelihood

    okay okay okay

    cool any questions Yeah, cool any questions Yeah, cool any questions Yeah,

    >> here the data space is the 2D plane. >> here the data space is the 2D plane.
    >> here the data space is the 2D plane.

    >> So will this 2D plate be like >> So will this 2D plate be like >> So will this
    2D plate be like

    transformed to regular space? transformed to regular space? transformed to regular
    space?

    >> No. So in this case the uh I guess it''s >> No. So in this case the uh I guess
    it''s >> No. So in this case the uh I guess it''s

    not clear from here but the uh the color not clear from here but the uh the color
    not clear from here but the uh the color

    the point are our uh desired the point are our uh desired the point are our uh
    desired

    distribution. So this is a so we desire distribution. So this is a so we desire
    distribution. So this is a so we desire

    to transform. That''s a actually a great to transform. That''s a actually a great
    to transform. That''s a actually a great

    question. So your source distribution question. So your source distribution question.
    So your source distribution

    just like in diffusion right your source just like in diffusion right your source'
  concept_slugs:
  - langevin-dynamics
  - score-function
  - score-matching
- idx: 15
  start_sec: 751.279
  end_sec: 808.24
  text: 'just like in diffusion right your source

    distribution and your target distribution and your target distribution and your
    target

    distribution should always be in the distribution should always be in the distribution
    should always be in the

    same space. So here our uh like desired same space. So here our uh like desired
    same space. So here our uh like desired

    distribution distribution distribution

    are these like colored mixture of are these like colored mixture of are these
    like colored mixture of

    gausian here. So the here and here and gausian here. So the here and here and
    gausian here. So the here and here and

    we are just uh randomly sample and and we are just uh randomly sample and and
    we are just uh randomly sample and and

    and the in other words the target and the in other words the target and the in
    other words the target

    distribution is also in the 2D plane and distribution is also in the 2D plane
    and distribution is also in the 2D plane and

    then we just like randomly sample a then we just like randomly sample a then we
    just like randomly sample a

    point on this the same 2D plane and then point on this the same 2D plane and then
    point on this the same 2D plane and then

    we follow the gradient of the log we follow the gradient of the log we follow
    the gradient of the log

    density to get to um to get to the the density to get to um to get to the the
    density to get to um to get to the the

    high density region of our desired high density region of our desired high density
    region of our desired

    distribution. I''m sorry. I''m sorry.

    >> Be easier. >> Be easier. >> Be easier.

    >> It will be easier. It could be just It >> It will be easier. It could be just
    It >> It will be easier. It could be just It

    could be just uh P like the gradient of could be just uh P like the gradient of
    could be just uh P like the gradient of

    P theta. That''s fine. Sorry. The P theta. That''s fine. Sorry. The P theta. That''s
    fine. Sorry. The

    gradient of uh of of P gradient of uh of of P'
  concept_slugs:
  - langevin-dynamics
  - score-function
  - score-matching
- idx: 16
  start_sec: 808.24
  end_sec: 855.92
  text: 'gradient of uh of of P

    X uh with respect to X. That''s fine. But X uh with respect to X. That''s fine.
    But X uh with respect to X. That''s fine. But

    later on we''re going to see why because later on we''re going to see why because
    later on we''re going to see why because

    log is easier to calculate in many log is easier to calculate in many log is easier
    to calculate in many

    cases. Yeah. cases. Yeah. cases. Yeah.

    >> Why do we suppose we know this function? >> Why do we suppose we know this
    function? >> Why do we suppose we know this function?

    How do we SAMPLE IT? How do we SAMPLE IT? How do we SAMPLE IT?

    YEAH, GREAT QUESTION. THIS IS WHAT WE''RE YEAH, GREAT QUESTION. THIS IS WHAT WE''RE
    YEAH, GREAT QUESTION. THIS IS WHAT WE''RE

    GOING TO learn today. All right. Cool, GOING TO learn today. All right. Cool,
    GOING TO learn today. All right. Cool,

    cool, cool. Okay. Okay. Um, so let''s cool, cool. Okay. Okay. Um, so let''s cool,
    cool. Okay. Okay. Um, so let''s

    first define what we''re learning here first define what we''re learning here
    first define what we''re learning here

    first. Okay. Um, so uh, so now first. Okay. Um, so uh, so now first. Okay. Um,
    so uh, so now

    we are clear that the goal of our we are clear that the goal of our we are clear
    that the goal of our

    modeling is to get an estimation of the modeling is to get an estimation of the
    modeling is to get an estimation of the

    so-called score function. Right? So so-called score function. Right? So so-called
    score function. Right? So

    basically what we can do is literally we basically what we can do is literally
    we basically what we can do is literally we

    just need to train a model to estimate just need to train a model to estimate
    just need to train a model to estimate

    the score and we can just do that by the score and we can just do that by the
    score and we can just do that by

    minimizing an L2 right regression. This minimizing an L2 right regression. This
    minimizing an L2 right regression. This

    is uh machine learning 101 right. So is uh machine learning 101 right. So'
  concept_slugs:
  - langevin-dynamics
  - score-function
  - score-matching
- idx: 17
  start_sec: 855.92
  end_sec: 908.069
  text: 'is uh machine learning 101 right. So

    very easy very easy uh uh uh very easy very easy uh uh uh very easy very easy
    uh uh uh

    formulation. And this L2 here uh it has formulation. And this L2 here uh it has
    formulation. And this L2 here uh it has

    a fancy name specifically because it has a fancy name specifically because it
    has a fancy name specifically because it has

    the this um score function thing but the this um score function thing but the
    this um score function thing but

    it''s called fishial divergence. You it''s called fishial divergence. You it''s
    called fishial divergence. You

    don''t really need to remember this this don''t really need to remember this this
    don''t really need to remember this this

    name but just but just like it''s name but just but just like it''s name but just
    but just like it''s

    literally just you are minimizing an L2 literally just you are minimizing an L2
    literally just you are minimizing an L2

    which is L2 which is L2 which is L2

    onto the the true score but here comes onto the the true score but here comes
    onto the the true score but here comes

    the question right oh actually before we the question right oh actually before
    we the question right oh actually before we

    here comes the question this thing is here comes the question this thing is here
    comes the question this thing is

    nice now because it doesn''t have any nice now because it doesn''t have any nice
    now because it doesn''t have any

    inractable partition function like EBM inractable partition function like EBM
    inractable partition function like EBM

    uh it has no adversary training like in uh it has no adversary training like in
    uh it has no adversary training like in

    GANs it has no weird architectures to GANs it has no weird architectures to GANs
    it has no weird architectures to

    enforce invertability like uh enforce invertability like uh enforce invertability
    like uh

    normalizing flows and you also do not normalizing flows and you also do not normalizing
    flows and you also do not

    need to break everything up into chain need to break everything up into chain
    need to break everything up into chain

    rules rules rules

    like auto reggressive models. So it can'
  concept_slugs:
  - langevin-dynamics
  - score-function
  - score-matching
- idx: 18
  start_sec: 908.069
  end_sec: 947.44
  text: 'like auto reggressive models. So it can like auto reggressive models. So
    it can

    sample or generate everything all at sample or generate everything all at sample
    or generate everything all at

    once once you have uh you know learned once once you have uh you know learned
    once once you have uh you know learned

    the model supposedly right like all the the model supposedly right like all the
    the model supposedly right like all the

    dimensions all at once. Uh so that''s dimensions all at once. Uh so that''s dimensions
    all at once. Uh so that''s

    nice but the question is how do you nice but the question is how do you nice but
    the question is how do you

    train the model right because now this train the model right because now this
    train the model right because now this

    even though the formulation is very easy even though the formulation is very easy
    even though the formulation is very easy

    it it comes the qu like the first it it comes the qu like the first it it comes
    the qu like the first

    question you should ask is how do we question you should ask is how do we question
    you should ask is how do we

    even get this ground true score right even get this ground true score right even
    get this ground true score right

    because the data set usually doesn''t because the data set usually doesn''t because
    the data set usually doesn''t

    come with the score it it certainly do come with the score it it certainly do
    come with the score it it certainly do

    not come with the the log density right not come with the the log density right
    not come with the the log density right

    because if it does come with log density because if it does come with log density
    because if it does come with log density

    then we what what why what are we then we what what why what are we then we what
    what why what are we

    learning here right so how do we even do learning here right so how do we even
    do learning here right so how do we even do

    this L2 without this ground truth score. this L2 without this ground truth score.'
  concept_slugs:
  - langevin-dynamics
  - score-function
  - score-matching
- idx: 19
  start_sec: 947.44
  end_sec: 995.43
  text: 'this L2 without this ground truth score.

    Turns out you don''t even need to use the Turns out you don''t even need to use
    the Turns out you don''t even need to use the

    ground truth score in your loss ground truth score in your loss ground truth score
    in your loss

    function. Why? function. Why? function. Why?

    H because of calculus practice. H because of calculus practice. H because of calculus
    practice.

    All right. So basically what you need to All right. So basically what you need
    to All right. So basically what you need to

    do here is you need to first break this do here is you need to first break this
    do here is you need to first break this

    L2 up this expectation of L2 up uh into L2 up this expectation of L2 up uh into
    L2 up this expectation of L2 up uh into

    three parts. Uh and then you may notice three parts. Uh and then you may notice
    three parts. Uh and then you may notice

    that because this is going to be a loss that because this is going to be a loss
    that because this is going to be a loss

    function, right? It''s a loss function function, right? It''s a loss function
    function, right? It''s a loss function

    with respect to theta and the first part with respect to theta and the first part
    with respect to theta and the first part

    of the the first part of the equation is of the the first part of the equation
    is of the the first part of the equation is

    not even like related to theta. It''s a not even like related to theta. It''s
    a not even like related to theta. It''s a

    constant with respect to theta. Right? constant with respect to theta. Right?
    constant with respect to theta. Right?

    So the first part of the the three So the first part of the the three So the first
    part of the the three

    components we can just cross it out. We components we can just cross it out. We
    components we can just cross it out. We

    don''t even need it. All right. So now we don''t even need it. All right. So now
    we don''t even need it. All right. So now we

    simplify uh the L2 the the original L2'
  concept_slugs:
  - langevin-dynamics
  - score-function
  - score-matching
- idx: 20
  start_sec: 995.43
  end_sec: 1047.039
  text: 'simplify uh the L2 the the original L2 simplify uh the L2 the the original
    L2

    into two parts here. And then the first into two parts here. And then the first
    into two parts here. And then the first

    part doesn''t really have the log density part doesn''t really have the log density
    part doesn''t really have the log density

    or the score function anymore. So this or the score function anymore. So this
    or the score function anymore. So this

    is good. So we can just get that. Uh the is good. So we can just get that. Uh
    the is good. So we can just get that. Uh the

    second part still have log density. And second part still have log density. And
    second part still have log density. And

    how do we simplify that? Uh well how do we simplify that? Uh well how do we simplify
    that? Uh well

    basically you it''s literally just basically you it''s literally just basically
    you it''s literally just

    calculus practice here. Um you don''t calculus practice here. Um you don''t calculus
    practice here. Um you don''t

    really need to like like know the really need to like like know the really need
    to like like know the

    details now, but I''m just going to walk details now, but I''m just going to walk
    details now, but I''m just going to walk

    through everything. Um but basically through everything. Um but basically through
    everything. Um but basically

    what you do is you first uh break up the what you do is you first uh break up
    the what you do is you first uh break up the

    expectation and then notice that the expectation and then notice that the expectation
    and then notice that the

    gradient of log probability or log any gradient of log probability or log any
    gradient of log probability or log any

    the gradient of log actually is the the gradient of log actually is the the gradient
    of log actually is the

    derivative of log is one over derivative of log is one over derivative of log
    is one over

    the the function right so basically you the the function right so basically you
    the the function right so basically you

    can have the gradient of uh log of p can have the gradient of uh log of p'
  concept_slugs:
  - langevin-dynamics
  - score-function
  - score-matching
- idx: 21
  start_sec: 1047.039
  end_sec: 1093.679
  text: 'can have the gradient of uh log of p

    with respect to x into you can break it with respect to x into you can break it
    with respect to x into you can break it

    into this thing right uh and then these into this thing right uh and then these
    into this thing right uh and then these

    two things cancel these 2 px p theta x two things cancel these 2 px p theta x
    two things cancel these 2 px p theta x

    cancelled and then you you''re going to cancelled and then you you''re going to
    cancelled and then you you''re going to

    get something very nice just a very get something very nice just a very get something
    very nice just a very

    short the integral of the inner product short the integral of the inner product
    short the integral of the inner product

    of the gradient of px and the learn the of the gradient of px and the learn the
    of the gradient of px and the learn the

    function and then basically what you do is this and then basically what you do
    is this

    is this part is like just trust me bro is this part is like just trust me bro
    is this part is like just trust me bro

    it''s going to get there type of thing it''s going to get there type of thing
    it''s going to get there type of thing

    where you just integrate by par and then where you just integrate by par and then
    where you just integrate by par and then

    you can actually eliminate the first you can actually eliminate the first you
    can actually eliminate the first

    part of the by par part um because the part of the by par part um because the
    part of the by par part um because the

    boundary will vanish when the when the boundary will vanish when the when the
    boundary will vanish when the when the

    coordinate goes to infinite um or or at coordinate goes to infinite um or or at
    coordinate goes to infinite um or or at

    least this is like our assumption. Uh least this is like our assumption. Uh least
    this is like our assumption. Uh

    and then you can basically just get and then you can basically just get'
  concept_slugs:
  - langevin-dynamics
  - score-function
  - score-matching
- idx: 22
  start_sec: 1093.679
  end_sec: 1138.4
  text: 'and then you can basically just get

    something like this. So um yeah this is something like this. So um yeah this is
    something like this. So um yeah this is

    a this is like we we probably wouldn''t a this is like we we probably wouldn''t
    a this is like we we probably wouldn''t

    have time to do all the derivation of have time to do all the derivation of have
    time to do all the derivation of

    this part but this is a trust me bro this part but this is a trust me bro this
    part but this is a trust me bro

    moment and feel free to look at the moment and feel free to look at the moment
    and feel free to look at the

    original paper after the class but original paper after the class but original
    paper after the class but

    basically what you will get after basically what you will get after basically
    what you will get after

    integration by power and with the integration by power and with the integration
    by power and with the

    assumption of uh boundary vanishing assumption of uh boundary vanishing assumption
    of uh boundary vanishing

    you''re going to get uh something like you''re going to get uh something like
    you''re going to get uh something like

    this and this is literally just the this and this is literally just the this and
    this is literally just the

    negative of expectation of this this negative of expectation of this this negative
    of expectation of this this

    thing and then this thing is a the trace thing and then this thing is a the trace
    thing and then this thing is a the trace

    of the Jacobian of the Jacobian of the Jacobian

    of the score function. All right. So all of the score function. All right. So
    all of the score function. All right. So all

    the math doesn''t really matter that the math doesn''t really matter that the
    math doesn''t really matter that

    much. I mean does matter but like much. I mean does matter but like much. I mean
    does matter but like

    doesn''t really matter for now. Um all we doesn''t really matter for now. Um all
    we doesn''t really matter for now. Um all we

    need to remember is that the second part need to remember is that the second part'
  concept_slugs:
  - langevin-dynamics
  - score-function
  - score-matching
- idx: 23
  start_sec: 1138.4
  end_sec: 1181.2
  text: 'need to remember is that the second part

    of the two things left. It''s going to of the two things left. It''s going to
    of the two things left. It''s going to

    come boils down to the negative of the come boils down to the negative of the
    come boils down to the negative of the

    expectation of the trace of the Jacobia expectation of the trace of the Jacobia
    expectation of the trace of the Jacobia

    of the score model. All right. Cool. Uh of the score model. All right. Cool. Uh
    of the score model. All right. Cool. Uh

    so so this is what we get at the end. Um so so this is what we get at the end.
    Um so so this is what we get at the end. Um

    so the first part is sort of like L2 so the first part is sort of like L2 so the
    first part is sort of like L2

    norm of your uh score function and then norm of your uh score function and then
    norm of your uh score function and then

    the second part is the trace of the the second part is the trace of the the second
    part is the trace of the

    Jacobian of the score function. Uh yeah Jacobian of the score function. Uh yeah
    Jacobian of the score function. Uh yeah

    and uh yeah so this is like the the and uh yeah so this is like the the and uh
    yeah so this is like the the

    final score matching loss and this is final score matching loss and this is final
    score matching loss and this is

    what we call the score matching loss. what we call the score matching loss. what
    we call the score matching loss.

    Yeah. All right. So you may notice this Yeah. All right. So you may notice this
    Yeah. All right. So you may notice this

    is very nice, right? Because right now is very nice, right? Because right now
    is very nice, right? Because right now

    in the score matching loss in the final in the score matching loss in the final
    in the score matching loss in the final

    loss that we get, we don''t really need a loss that we get, we don''t really need
    a'
  concept_slugs:
  - langevin-dynamics
  - score-function
  - score-matching
- idx: 24
  start_sec: 1181.2
  end_sec: 1238.07
  text: 'loss that we get, we don''t really need a

    ground true score. It''s it''s like ground true score. It''s it''s like ground
    true score. It''s it''s like

    actually pretty pretty sick. So all you actually pretty pretty sick. So all you
    actually pretty pretty sick. So all you

    need to do is you just need you can just need to do is you just need you can just
    need to do is you just need you can just

    calculate everything with your model and calculate everything with your model
    and calculate everything with your model and

    then it can magically work. This is then it can magically work. This is then it
    can magically work. This is

    amazing, right? Is this truly amazing? amazing, right? Is this truly amazing?
    amazing, right? Is this truly amazing?

    What do we think? What do we think? Oh What do we think? What do we think? Oh
    What do we think? What do we think? Oh

    yeah. and and obviously like if you if yeah. and and obviously like if you if
    yeah. and and obviously like if you if

    you have a bunch of data then you can you have a bunch of data then you can you
    have a bunch of data then you can

    just you know average over your data. just you know average over your data. just
    you know average over your data.

    So this is amazing right now we can do So this is amazing right now we can do
    So this is amazing right now we can do

    learning learning learning

    or can we actually or can we actually or can we actually

    what can be a potential problem if what can be a potential problem if what can
    be a potential problem if

    you''re if you''re gonna implement this you''re if you''re gonna implement this
    you''re if you''re gonna implement this

    how do you think of the problem how do you think of the problem how do you think
    of the problem

    very strange to me very strange to me very strange to me

    >> how do you well >> how do you well >> how do you well

    >> like >> like >> like

    >> okay yeah yeah like answer the question >> yeah exactly right because the score
    >> yeah exactly right because the score

    function has the same dimensionality of'
  concept_slugs:
  - langevin-dynamics
  - score-function
  - score-matching
- idx: 25
  start_sec: 1238.07
  end_sec: 1297.12
  text: 'function has the same dimensionality of function has the same dimensionality
    of

    the of the data, right? Yeah. So, you the of the data, right? Yeah. So, you the
    of the data, right? Yeah. So, you

    can just Yeah, can just Yeah, can just Yeah,

    >> you can just take the jacobian there. >> you can just take the jacobian there.
    >> you can just take the jacobian there.

    >> Yeah. Yeah. Exactly. Okay. But you were >> Yeah. Yeah. Exactly. Okay. But you
    were >> Yeah. Yeah. Exactly. Okay. But you were

    gonna say why is this not practical, gonna say why is this not practical, gonna
    say why is this not practical,

    right? right? right?

    >> Yes, that''s right. Uh >> Yes, that''s right. Uh >> Yes, that''s right. Uh

    that is correct. that is correct. that is correct.

    Um yeah. So for any of you who have uh Um yeah. So for any of you who have uh
    Um yeah. So for any of you who have uh

    you know tried to calculate Jacobian you know tried to calculate Jacobian you
    know tried to calculate Jacobian

    with PyTorch uh you realize that just with PyTorch uh you realize that just with
    PyTorch uh you realize that just

    just calculating Jacobian itself is just calculating Jacobian itself is just calculating
    Jacobian itself is

    actually not optimized that well at all actually not optimized that well at all
    actually not optimized that well at all

    and it''s actually really really and it''s actually really really and it''s actually
    really really

    expensive and uh yeah so this this thing expensive and uh yeah so this this thing
    expensive and uh yeah so this this thing

    is like super super expensive to is like super super expensive to is like super
    super expensive to

    calculate. Uh so is there another way calculate. Uh so is there another way calculate.
    Uh so is there another way

    is there another way to do this? is there another way to do this? is there another
    way to do this?

    Yes. Estimate. Estimate. Continue. Well, Yes. Estimate. Estimate. Continue. Well,
    Yes. Estimate. Estimate. Continue. Well,

    actually, does anyone else? Uh, actually, does anyone else? Uh, actually, does
    anyone else? Uh,

    no one else. Do you have a Do you have a no one else. Do you have a Do you have
    a'
  concept_slugs:
  - langevin-dynamics
  - score-function
  - score-matching
- idx: 26
  start_sec: 1297.12
  end_sec: 1362.159
  text: 'no one else. Do you have a Do you have a

    Do you have a Do you have a Do you have a

    >> Well, yes, but it''s kind of related to >> Well, yes, but it''s kind of related
    to >> Well, yes, but it''s kind of related to

    how how how

    to get transform. to get transform. to get transform.

    So, maybe just sample those. You''re you''re on you''re on a good track, You''re
    you''re on you''re on a good track,

    but this is not not exactly. Basically, but this is not not exactly. Basically,
    but this is not not exactly. Basically,

    we''re just trying to like avoid this we''re just trying to like avoid this we''re
    just trying to like avoid this

    whole Jacovian thing in in entirely. whole Jacovian thing in in entirely. whole
    Jacovian thing in in entirely.

    Does anyone else have any thoughts? Does anyone else have any thoughts? Does anyone
    else have any thoughts?

    >> From the distribution >> From the distribution >> From the distribution

    >> where >> where >> where

    the distribution the distribution the distribution

    >> sample distribution directly >> sample distribution directly >> sample distribution
    directly

    >> from a distribution directly. What kind >> from a distribution directly. What
    kind >> from a distribution directly. What kind

    of distribution? Just give me the first distribution that Just give me the first
    distribution that

    you that you can comment. you that you can comment. you that you can comment.

    Did someone say Gausian? Yes. Yeah. Did someone say Gausian? Yes. Yeah. Did someone
    say Gausian? Yes. Yeah.

    That''s right. That''s right. Exactly. That''s right. That''s right. Exactly.
    That''s right. That''s right. Exactly.

    This is why I say you need a tattoo bay This is why I say you need a tattoo bay
    This is why I say you need a tattoo bay

    rule on your right hand and then the the rule on your right hand and then the
    the rule on your right hand and then the the

    portrait of Gausian on the left hand. portrait of Gausian on the left hand. portrait
    of Gausian on the left hand.

    This is how important it is. All right. This is how important it is. All right.
    This is how important it is. All right.

    Literally Gausian. Okay. So basically Literally Gausian. Okay. So basically'
  concept_slugs:
  - langevin-dynamics
  - score-function
  - score-matching
- idx: 27
  start_sec: 1362.159
  end_sec: 1405.84
  text: 'Literally Gausian. Okay. So basically

    what you do is uh and this is what we what you do is uh and this is what we what
    you do is uh and this is what we

    call dnoising score matching. Why so get call dnoising score matching. Why so
    get call dnoising score matching. Why so get

    den noising? Well, basically uh you know den noising? Well, basically uh you know
    den noising? Well, basically uh you know

    the the true score of the data is very the the true score of the data is very
    the the true score of the data is very

    very difficult to calculate, right? Uh very difficult to calculate, right? Uh
    very difficult to calculate, right? Uh

    but if you just perturb a little bit of but if you just perturb a little bit of
    but if you just perturb a little bit of

    your your data, so you from this super your your data, so you from this super
    your your data, so you from this super

    clean image to a slightly noisy image. clean image to a slightly noisy image.
    clean image to a slightly noisy image.

    But now this say this perturbation But now this say this perturbation But now
    this say this perturbation

    kernel is a gausian, right? So you just kernel is a gausian, right? So you just
    kernel is a gausian, right? So you just

    add some gausian noise to it. Uh then add some gausian noise to it. Uh then add
    some gausian noise to it. Uh then

    now uh this this this uh this now uh this this this uh this now uh this this this
    uh this

    distribution became known, right? it distribution became known, right? it distribution
    became known, right? it

    became became became

    it becomes like a distribution that we it becomes like a distribution that we
    it becomes like a distribution that we

    know how to calculate the score of know how to calculate the score of know how
    to calculate the score of

    right. So basically what you need to do right. So basically what you need to do
    right. So basically what you need to do

    is you just need a sample data and then is you just need a sample data and then'
  concept_slugs:
  - langevin-dynamics
  - score-function
  - score-matching
- idx: 28
  start_sec: 1405.84
  end_sec: 1455.669
  text: 'is you just need a sample data and then

    perturb it a little bit and now it perturb it a little bit and now it perturb
    it a little bit and now it

    becomes this like it''s easier to becomes this like it''s easier to becomes this
    like it''s easier to

    calculate distribution. Yeah the the calculate distribution. Yeah the the calculate
    distribution. Yeah the the

    dude the the the goat. Okay. So dude the the the goat. Okay. So dude the the the
    goat. Okay. So

    basically um yeah to to to just write it basically um yeah to to to just write
    it basically um yeah to to to just write it

    down formally uh if your perturbation down formally uh if your perturbation down
    formally uh if your perturbation

    kernel is some like zero mean gausian uh kernel is some like zero mean gausian
    uh kernel is some like zero mean gausian uh

    so you just add some gausian noise to it so you just add some gausian noise to
    it so you just add some gausian noise to it

    um then the perturb the distribution um then the perturb the distribution um then
    the perturb the distribution

    like so the distribution that you''re like so the distribution that you''re like
    so the distribution that you''re

    actually going to calculate the score actually going to calculate the score actually
    going to calculate the score

    from uh it''s just have this very easy from uh it''s just have this very easy
    from uh it''s just have this very easy

    and nice uh formula that tells you the and nice uh formula that tells you the
    and nice uh formula that tells you the

    density or the conditional density I density or the conditional density I density
    or the conditional density I

    guess because you''re conditioning on a guess because you''re conditioning on
    a guess because you''re conditioning on a

    data data data

    and the score is literally literally and the score is literally literally and
    the score is literally literally

    just this. You can do your algebra. just this. You can do your algebra. just this.
    You can do your algebra.

    Sorry, you can do your calculus. This is Sorry, you can do your calculus. This
    is Sorry, you can do your calculus. This is

    literally this. Uh so yeah, for for'
  concept_slugs:
  - langevin-dynamics
  - score-function
  - score-matching
- idx: 29
  start_sec: 1455.669
  end_sec: 1525.83
  text: 'literally this. Uh so yeah, for for literally this. Uh so yeah, for for

    those of you who wonder why log density those of you who wonder why log density
    those of you who wonder why log density

    easier basically. Um yeah. So so so now easier basically. Um yeah. So so so now
    easier basically. Um yeah. So so so now

    the gradient of the log density is the gradient of the log density is the gradient
    of the log density is

    literally just one over theta square, literally just one over theta square, literally
    just one over theta square,

    which is your variance. one over which is your variance. one over which is your
    variance. one over

    variance times the noise essentially. variance times the noise essentially. variance
    times the noise essentially.

    Uh or like the negative of the noise I Uh or like the negative of the noise I
    Uh or like the negative of the noise I

    guess. guess. guess.

    All right. All right. All right.

    Any question here? No. No.

    Okay. It''s interesting. It''s curious Okay. It''s interesting. It''s curious
    Okay. It''s interesting. It''s curious

    that you guys do not have question that you guys do not have question that you
    guys do not have question

    because I would have had question. Yeah. >> There''s no Jacobian anymore because
    >> There''s no Jacobian anymore because

    uh because we can ex we can calculate uh because we can ex we can calculate uh
    because we can ex we can calculate

    exactly the ground now we have the exactly the ground now we have the exactly
    the ground now we have the

    ground truth. So the Jacobian is for the ground truth. So the Jacobian is for
    the ground truth. So the Jacobian is for the

    case where we do not have the ground case where we do not have the ground case
    where we do not have the ground

    truth score and here we do have the truth score and here we do have the truth
    score and here we do have the

    ground truth score. uh it just that the ground truth score. uh it just that the
    ground truth score. uh it just that the

    ground truth is not the actual ground ground truth is not the actual ground ground
    truth is not the actual ground

    truth it''s a perturbed ground truth then'
  concept_slugs:
  - langevin-dynamics
  - score-function
  - score-matching
- idx: 30
  start_sec: 1525.83
  end_sec: 1564.48
  text: 'truth it''s a perturbed ground truth then truth it''s a perturbed ground
    truth then

    you may have a question but like let''s you may have a question but like let''s
    you may have a question but like let''s

    marinate question a little bit um okay marinate question a little bit um okay
    marinate question a little bit um okay

    but let''s say everything works out right but let''s say everything works out
    right but let''s say everything works out right

    let''s say everything works out then once let''s say everything works out then
    once let''s say everything works out then once

    we have a trained model now we have we we have a trained model now we have we
    we have a trained model now we have we

    know two ways to train our models once know two ways to train our models once
    know two ways to train our models once

    that we have the trained model uh then that we have the trained model uh then
    that we have the trained model uh then

    we can do gradient as right just like we can do gradient as right just like we
    can do gradient as right just like

    what we did in the data space to to get what we did in the data space to to get
    what we did in the data space to to get

    a sample and this sort of gradient thing a sample and this sort of gradient thing
    a sample and this sort of gradient thing

    is called long driven dynamic is such a is called long driven dynamic is such
    a is called long driven dynamic is such a

    cool name. It''s a Yeah, I feel like I chose my uh you know Yeah, I feel like
    I chose my uh you know

    my my my name for the for the Twitter my my my name for the for the Twitter my
    my my name for the for the Twitter

    too soon. I should have chose long too soon. I should have chose long too soon.
    I should have chose long

    dynamics better than electronic kel but dynamics better than electronic kel but
    dynamics better than electronic kel but

    anyway it''s fine. Um uh so what you do anyway it''s fine. Um uh so what you do'
  concept_slugs:
  - langevin-dynamics
  - score-function
  - score-matching
- idx: 31
  start_sec: 1564.48
  end_sec: 1610.48
  text: 'anyway it''s fine. Um uh so what you do

    is you first draw draw a sample from is you first draw draw a sample from is you
    first draw draw a sample from

    your data space using some easy to your data space using some easy to your data
    space using some easy to

    sample prior distribution for example sample prior distribution for example sample
    prior distribution for example

    like a gausian or something like that. like a gausian or something like that.
    like a gausian or something like that.

    And then basically at each step what you And then basically at each step what
    you And then basically at each step what you

    do is you uh you you do gradient ascent do is you uh you you do gradient ascent
    do is you uh you you do gradient ascent

    with some small step size and then you with some small step size and then you
    with some small step size and then you

    add some stoasticity in it. Um and then add some stoasticity in it. Um and then
    add some stoasticity in it. Um and then

    if you have a train the model already if you have a train the model already if
    you have a train the model already

    you can swap the this this score part you can swap the this this score part you
    can swap the this this score part

    into the score model right that you into the score model right that you into the
    score model right that you

    just learn to predict the score. So it just learn to predict the score. So it
    just learn to predict the score. So it

    become the predicted score. Uh and then become the predicted score. Uh and then
    become the predicted score. Uh and then

    uh this noise thing is just to add uh this noise thing is just to add uh this
    noise thing is just to add

    exploration so that you don''t you know exploration so that you don''t you know
    exploration so that you don''t you know

    just uh overconfident exploit too much. just uh overconfident exploit too much.
    just uh overconfident exploit too much.

    Okay. Okay. Okay.

    So this is what could have happened if So this is what could have happened if'
  concept_slugs:
  - langevin-dynamics
  - score-function
  - score-matching
- idx: 32
  start_sec: 1610.48
  end_sec: 1664.08
  text: 'So this is what could have happened if

    you do laundry dynamic essentially. So you do laundry dynamic essentially. So
    you do laundry dynamic essentially. So

    at the beginning, right, we just like at the beginning, right, we just like at
    the beginning, right, we just like

    just sample all over the place. And then just sample all over the place. And then
    just sample all over the place. And then

    as you progress in your gradient ascent, as you progress in your gradient ascent,
    as you progress in your gradient ascent,

    you''re going to ended up in this nice you''re going to ended up in this nice
    you''re going to ended up in this nice

    location, this nice like cluster where location, this nice like cluster where
    location, this nice like cluster where

    it''s supposed to have high density. Okay, any question? Okay, any question?

    All right. Anyway, point being uh so All right. Anyway, point being uh so All
    right. Anyway, point being uh so

    you have question. This is great. I you have question. This is great. I you have
    question. This is great. I

    actually Actually maybe let me let me uh actually Actually maybe let me let me
    uh actually Actually maybe let me let me uh

    let me go through this part and then and let me go through this part and then
    and let me go through this part and then and

    then maybe this question will be um so then maybe this question will be um so
    then maybe this question will be um so

    uh so this is the uh so this is the uh so this is the

    scorebased model pipeline. You basically scorebased model pipeline. You basically
    scorebased model pipeline. You basically

    train your model using score matching or train your model using score matching
    or train your model using score matching or

    the noising score matching or any type the noising score matching or any type
    the noising score matching or any type

    of score matching. Uh they have like of score matching. Uh they have like of score
    matching. Uh they have like

    variants of score matchings. Uh but variants of score matchings. Uh but variants
    of score matchings. Uh but

    anyway you just train your model to anyway you just train your model to'
  concept_slugs:
  - langevin-dynamics
  - score-function
  - score-matching
- idx: 33
  start_sec: 1664.08
  end_sec: 1740.96
  text: 'anyway you just train your model to

    predict the score and then you use predict the score and then you use predict
    the score and then you use

    dynamic to sample. Uh however does it dynamic to sample. Uh however does it dynamic
    to sample. Uh however does it

    actually work? What is your question? Uh actually work? What is your question?
    Uh actually work? What is your question? Uh

    why do we need exploration if we are why do we need exploration if we are why
    do we need exploration if we are

    already following the gradient? already following the gradient? already following
    the gradient?

    >> Great great question. Why? Uh turns out >> Great great question. Why? Uh turns
    out >> Great great question. Why? Uh turns out

    it''s actually very important. But first it''s actually very important. But first
    it''s actually very important. But first

    let''s you can let''s think about it. Uh let''s you can let''s think about it.
    Uh let''s you can let''s think about it. Uh

    does it actually work? And also another does it actually work? And also another
    does it actually work? And also another

    question is if it doesn''t have question is if it doesn''t have question is if
    it doesn''t have

    exploration, what''s going to happen? exploration, what''s going to happen? exploration,
    what''s going to happen?

    Maybe this is like actually a good Maybe this is like actually a good Maybe this
    is like actually a good

    All right, talk to your neighbor. Uh All right, talk to your neighbor. Uh All
    right, talk to your neighbor. Uh

    yeah, just uh for let''s say three yeah, just uh for let''s say three yeah, just
    uh for let''s say three

    minuteish Um, and then we''re going to minuteish Um, and then we''re going to
    minuteish Um, and then we''re going to

    come back. come back. come back.

    It''s three to five minute. Talk to your It''s three to five minute. Talk to your
    It''s three to five minute. Talk to your

    neighbor. Think about it. And then I''m neighbor. Think about it. And then I''m
    neighbor. Think about it. And then I''m

    going to survey the classroom again. Times up. Times up. All right, let''s Times
    up. Times up. All right, let''s

    survey. Let''s survey. Uh we are starting survey. Let''s survey. Uh we are starting'
  concept_slugs:
  - langevin-dynamics
  - score-function
  - score-matching
- idx: 34
  start_sec: 1740.96
  end_sec: 1806.47
  text: 'survey. Let''s survey. Uh we are starting

    from this column again. from this column again. from this column again.

    Hello friends. Uh Hello friends. Uh Hello friends. Uh

    does anyone want to share their thoughts does anyone want to share their thoughts
    does anyone want to share their thoughts

    whether or not this actually works? All right, we''re Oh, someone saved you. All
    right, we''re Oh, someone saved you.

    But uh you know, next time next time But uh you know, next time next time But
    uh you know, next time next time

    we''re already make eye contact. we''re already make eye contact. we''re already
    make eye contact.

    >> All right, >> All right, >> All right,

    >> we believe that it''s really difficult to >> we believe that it''s really difficult
    to >> we believe that it''s really difficult to

    actually sample from um sample the actually sample from um sample the actually
    sample from um sample the

    scores from the uh from the model scores from the uh from the model scores from
    the uh from the model

    because you might end up in the low because you might end up in the low because
    you might end up in the low

    density region density region density region

    >> which is which is kind of difficult to >> which is which is kind of difficult
    to >> which is which is kind of difficult to

    uh you know because the model is not uh you know because the model is not uh you
    know because the model is not

    trained. trained. trained.

    >> Very nice. Very nice. Great. Great >> Very nice. Very nice. Great. Great >>
    Very nice. Very nice. Great. Great

    answer. All right. Uh what about the answer. All right. Uh what about the answer.
    All right. Uh what about the

    middle column? middle column? middle column?

    Middle column. Do we have another answer of why why it may or may not work? of
    why why it may or may not work?

    Oh, did you raise your hand? Oh no, did you raise your hand? Oh no,

    this is very unfortunate. Someone this is very unfortunate. Someone this is very
    unfortunate. Someone

    someone in the middle column that I someone in the middle column that I someone
    in the middle column that I

    haven''t been that I haven''t been talked'
  concept_slugs:
  - langevin-dynamics
  - score-function
  - score-matching
- idx: 35
  start_sec: 1806.47
  end_sec: 1872.799
  text: 'haven''t been that I haven''t been talked haven''t been that I haven''t been
    talked

    to today. There''s so many people in the to today. There''s so many people in
    the to today. There''s so many people in the

    middle column though. for real. All right. for real. All right.

    Um, Um, Um,

    what about the left column first? Some thoughts? Okay. Yes. Some thoughts? Okay.
    Yes.

    It''s too too difficult to me to know. It''s too too difficult to me to know.
    It''s too too difficult to me to know.

    >> It''s just I don''t know if this >> It''s just I don''t know if this >> It''s
    just I don''t know if this

    but I guess maybe the sound tool always but I guess maybe the sound tool always
    but I guess maybe the sound tool always

    move moves towards move moves towards move moves towards

    a very dense distribution rather than a very dense distribution rather than a
    very dense distribution rather than

    the right distribution. the right distribution. the right distribution.

    >> Very nice. Great answer too. Great >> Very nice. Great answer too. Great >>
    Very nice. Great answer too. Great

    answer. All right. Um answer. All right. Um answer. All right. Um

    let''s uh let''s review the the solution let''s uh let''s review the the solution
    let''s uh let''s review the the solution

    or let''s review the answer. Okay. Um so or let''s review the answer. Okay. Um
    so or let''s review the answer. Okay. Um so

    yeah, no is that it actually very yeah, no is that it actually very yeah, no is
    that it actually very

    difficult to make it work in practice. difficult to make it work in practice.
    difficult to make it work in practice.

    And why? Uh the first one is actually a And why? Uh the first one is actually
    a And why? Uh the first one is actually a

    little bit more difficult to think little bit more difficult to think little bit
    more difficult to think

    about. Uh but the other two people about. Uh but the other two people about. Uh
    but the other two people

    nailed it basically. Um so the first one nailed it basically. Um so the first
    one nailed it basically. Um so the first one

    is what we call the manifold is what we call the manifold'
  concept_slugs:
  - langevin-dynamics
  - score-function
  - score-matching
- idx: 36
  start_sec: 1872.799
  end_sec: 1919.75
  text: 'is what we call the manifold

    hypothesis. What does it mean is that hypothesis. What does it mean is that hypothesis.
    What does it mean is that

    basically usually the data that we want basically usually the data that we want
    basically usually the data that we want

    to train on uh are reside on the like a to train on uh are reside on the like
    a to train on uh are reside on the like a

    lower dimensional manifold and what it lower dimensional manifold and what it
    lower dimensional manifold and what it

    means is basically like uh even though means is basically like uh even though
    means is basically like uh even though

    you have a very very high dimensional you have a very very high dimensional you
    have a very very high dimensional

    data like image like 4K image or data like image like 4K image or data like image
    like 4K image or

    something um like say you''re only the something um like say you''re only the
    something um like say you''re only the

    data is only about human faces right data is only about human faces right data
    is only about human faces right

    then you can sort of just describe the then you can sort of just describe the
    then you can sort of just describe the

    human faces with like I don''t know 128 human faces with like I don''t know 128
    human faces with like I don''t know 128

    like facial landmarks and that''s the like facial landmarks and that''s the like
    facial landmarks and that''s the

    actual dimensionality quote unquote like actual dimensionality quote unquote like
    actual dimensionality quote unquote like

    the meaningful dimensionality of your of the meaningful dimensionality of your
    of the meaningful dimensionality of your of

    your data. So rather than 4K time 4K, your data. So rather than 4K time 4K, your
    data. So rather than 4K time 4K,

    you actually have a very low dimensional you actually have a very low dimensional
    you actually have a very low dimensional

    manifold for the data. And what it also manifold for the data. And what it also
    manifold for the data. And what it also

    means is that what means is that what means is that what

    what here says like some area of the'
  concept_slugs:
  - langevin-dynamics
  - score-function
  - score-matching
- idx: 37
  start_sec: 1919.75
  end_sec: 1963.76
  text: 'what here says like some area of the what here says like some area of the

    data space will not have support. What data space will not have support. What
    data space will not have support. What

    it means is that basically not all 4K it means is that basically not all 4K it
    means is that basically not all 4K

    images are human face images, right? So images are human face images, right? So
    images are human face images, right? So

    basically like you could have like basically like you could have like basically
    like you could have like

    complete gion noise or you can have like complete gion noise or you can have like
    complete gion noise or you can have like

    human face with like five eyes or human face with like five eyes or human face
    with like five eyes or

    something that that that may that''s um something that that that may that''s um
    something that that that may that''s um

    could be I guess or or like human face could be I guess or or like human face
    could be I guess or or like human face

    with um with um with um

    I don''t know with some animal features I don''t know with some animal features
    I don''t know with some animal features

    or something like right like like that or something like right like like that
    or something like right like like that

    right so that may that may or may not be right so that may that may or may not
    be right so that may that may or may not be

    considered as human right so basically considered as human right so basically
    considered as human right so basically

    that just means that not all images are that just means that not all images are
    that just means that not all images are

    human faces and what''s gonna happen is human faces and what''s gonna happen is
    human faces and what''s gonna happen is

    that just that just that just

    Like when the score that is going Like when the score that is going Like when
    the score that is going

    outside that''s going out from the outside that''s going out from the outside
    that''s going out from the

    manifold from some point from on the manifold from some point from on the'
  concept_slugs:
  - langevin-dynamics
  - score-function
  - score-matching
- idx: 38
  start_sec: 1963.76
  end_sec: 2008.799
  text: 'manifold from some point from on the

    manifold to some point that''s not on the manifold to some point that''s not on
    the manifold to some point that''s not on the

    manifold the score is going to blow up manifold the score is going to blow up
    manifold the score is going to blow up

    right this because like basically you''re right this because like basically you''re
    right this because like basically you''re

    going from nonzero density or like non going from nonzero density or like non
    going from nonzero density or like non

    negative infinity density to negative negative infinity density to negative negative
    infinity density to negative

    infinity density right so score is just infinity density right so score is just
    infinity density right so score is just

    gonna like the the the magnitude is just gonna like the the the magnitude is just
    gonna like the the the magnitude is just

    gonna blow up right and And the other gonna blow up right and And the other gonna
    blow up right and And the other

    thing is that as we can see here thing is that as we can see here thing is that
    as we can see here

    basically this is like just a score basically this is like just a score basically
    this is like just a score

    matching uh experiment that people ran matching uh experiment that people ran
    matching uh experiment that people ran

    and if you have this sort of like and if you have this sort of like and if you
    have this sort of like

    manifold hypothesis of your data then manifold hypothesis of your data then manifold
    hypothesis of your data then

    the the the score matching um the score the the the score matching um the score
    the the the score matching um the score

    estimation is actually not very estimation is actually not very estimation is
    actually not very

    consistent. So it just like really consistent. So it just like really consistent.
    So it just like really

    really unstable. really unstable. really unstable.

    Okay. Um so this is the first thing and Okay. Um so this is the first thing and
    Okay. Um so this is the first thing and

    then the second thing. Yeah. Yeah. Yeah. then the second thing. Yeah. Yeah. Yeah.'
  concept_slugs:
  - langevin-dynamics
  - score-function
  - score-matching
- idx: 39
  start_sec: 2008.799
  end_sec: 2050.0
  text: 'then the second thing. Yeah. Yeah. Yeah.

    >> What is this the left plot even showing >> What is this the left plot even
    showing >> What is this the left plot even showing

    either? Oh sorry the the the so uh the either? Oh sorry the the the so uh the
    either? Oh sorry the the the so uh the

    left plot is showing that basically this left plot is showing that basically this
    left plot is showing that basically this

    uh score matching so basically this one uh score matching so basically this one
    uh score matching so basically this one

    type of score matching loss when you type of score matching loss when you type
    of score matching loss when you

    only when you train on very very clean only when you train on very very clean
    only when you train on very very clean

    data and I think this is CR10 or data and I think this is CR10 or data and I think
    this is CR10 or

    something but basically this is like if something but basically this is like if
    something but basically this is like if

    you just do score matching if you you just do score matching if you you just do
    score matching if you

    actually train your model with score actually train your model with score actually
    train your model with score

    matching your loss function is going to matching your loss function is going to
    matching your loss function is going to

    look like this and it''s like completely look like this and it''s like completely
    look like this and it''s like completely

    just like sh just like very bad um but just like sh just like very bad um but
    just like sh just like very bad um but

    this is basically ally if you just this is basically ally if you just this is
    basically ally if you just

    perturb it with like a very very like perturb it with like a very very like perturb
    it with like a very very like

    invisible gausian noise and because it''s invisible gausian noise and because
    it''s invisible gausian noise and because it''s

    gausian right now the entire ambient gausian right now the entire ambient gausian
    right now the entire ambient

    space or entire data space now has space or entire data space now has'
  concept_slugs:
  - langevin-dynamics
  - score-function
  - score-matching
- idx: 40
  start_sec: 2050.0
  end_sec: 2097.52
  text: 'space or entire data space now has

    support uh and then the score matching support uh and then the score matching
    support uh and then the score matching

    actually behave really really nicely actually behave really really nicely actually
    behave really really nicely

    yeah yeah yeah

    >> so the loss become sort of converging >> so the loss become sort of converging
    >> so the loss become sort of converging

    it''s still pretty high right it''s like it''s still pretty high right it''s like
    it''s still pretty high right it''s like

    minus minus minus

    >> yeah yeah and >> yeah yeah and >> yeah yeah and

    >> it''s like 10^ six uh >> it''s like 10^ six uh >> it''s like 10^ six uh

    >> is that that >> is that that >> is that that

    >> but like but this is not what supposed >> but like but this is not what supposed
    >> but like but this is not what supposed

    to do by the way. But this is just to to do by the way. But this is just to to
    do by the way. But this is just to

    show that like the score matching loss show that like the score matching loss
    show that like the score matching loss

    is like super unstable when you have is like super unstable when you have is like
    super unstable when you have

    like data that reside on low dimensional like data that reside on low dimensional
    like data that reside on low dimensional

    manifold and if you have some invisible manifold and if you have some invisible
    manifold and if you have some invisible

    gausian noise that basically put support gausian noise that basically put support
    gausian noise that basically put support

    on even if just a little bit on on even if just a little bit on on even if just
    a little bit on

    everywhere else it''s going to stabilize everywhere else it''s going to stabilize
    everywhere else it''s going to stabilize

    your training. Uh okay divine you first your training. Uh okay divine you first
    your training. Uh okay divine you first

    the the the

    >> example that you mentioned where the >> example that you mentioned where the
    >> example that you mentioned where the

    image is eventually boiled down to say image is eventually boiled down to say'
  concept_slugs:
  - langevin-dynamics
  - score-function
  - score-matching
- idx: 41
  start_sec: 2097.52
  end_sec: 2145.19
  text: 'image is eventually boiled down to say

    10 features or something in that case 10 features or something in that case 10
    features or something in that case

    the manifold is load eventually how is the manifold is load eventually how is
    the manifold is load eventually how is

    this making it load eventually how how this making it load eventually how how
    this making it load eventually how how

    >> oh this is not making it low dimensional >> oh this is not making it low dimensional
    >> oh this is not making it low dimensional

    this is making a a data that basically this is making a a data that basically
    this is making a a data that basically

    so the data the data dimension itself is so the data the data dimension itself
    is so the data the data dimension itself is

    really high but the actual manifold like really high but the actual manifold like
    really high but the actual manifold like

    the actual meaningful dimensions are low the actual meaningful dimensions are
    low the actual meaningful dimensions are low

    >> noise makes the for manifold low is that >> noise makes the for manifold low
    is that >> noise makes the for manifold low is that

    >> no no no the the the the the basically >> no no no the the the the the basically
    >> no no no the the the the the basically

    what I was saying that like the the data what I was saying that like the the data
    what I was saying that like the the data

    before before you add gian noise the before before you add gian noise the before
    before you add gian noise the

    data only has support on the parts where data only has support on the parts where
    data only has support on the parts where

    it can be projected onto this low it can be projected onto this low it can be
    projected onto this low

    dimensional manifold. So not everywhere. dimensional manifold. So not everywhere.
    dimensional manifold. So not everywhere.

    So basically you you''re going to have So basically you you''re going to have
    So basically you you''re going to have

    somewhere that there''s like no support somewhere that there''s like no support
    somewhere that there''s like no support

    there''s no probability and that''s why'
  concept_slugs:
  - langevin-dynamics
  - score-function
  - score-matching
- idx: 42
  start_sec: 2145.19
  end_sec: 2202.95
  text: 'there''s no probability and that''s why there''s no probability and that''s
    why

    the score is going to blow up and adding the score is going to blow up and adding
    the score is going to blow up and adding

    small amount of gausian noise make small amount of gausian noise make small amount
    of gausian noise make

    everywhere has probability everywhere has probability everywhere has probability

    data that''s good because then you have data that''s good because then you have
    data that''s good because then you have

    support everywhere support everywhere support everywhere

    >> well but your this is not your choice >> well but your this is not your choice
    >> well but your this is not your choice

    right right right

    >> is your data >> is your data >> is your data

    >> but to understand >> but to understand >> but to understand

    >> it''s not necessarily like good or bad >> it''s not necessarily like good or
    bad >> it''s not necessarily like good or bad

    it''s just saying that this loss function it''s just saying that this loss function
    it''s just saying that this loss function

    is not good enough for the data that we is not good enough for the data that we
    is not good enough for the data that we

    usually usually usually

    We assume that when perturbing with some We assume that when perturbing with some
    We assume that when perturbing with some

    amount of ging noise our data moves out amount of ging noise our data moves out
    amount of ging noise our data moves out

    of this low dimensional manifold and of this low dimensional manifold and of this
    low dimensional manifold and

    sort of like a sort of like a sort of like a

    >> yeah right like if you add gausian noise >> yeah right like if you add gausian
    noise >> yeah right like if you add gausian noise

    is no longer clean anymore right yeah is no longer clean anymore right yeah is
    no longer clean anymore right yeah

    that''s correct yes there''s going to be noise to it right there''s going to be
    noise to it right

    >> uh >> uh >> uh

    so those are kind of already So this is what already happens. So this So this
    is what already happens. So this

    is like they they they train on the'
  concept_slugs:
  - langevin-dynamics
  - score-function
  - score-matching
- idx: 43
  start_sec: 2202.95
  end_sec: 2248.8
  text: 'is like they they they train on the is like they they they train on the

    clean data. So it''s like not I mean yes clean data. So it''s like not I mean
    yes clean data. So it''s like not I mean yes

    obviously there will be noise but obviously there will be noise but obviously
    there will be noise but

    basically even those noisy data you can basically even those noisy data you can
    basically even those noisy data you can

    fit like yeah there''s still low fit like yeah there''s still low fit like yeah
    there''s still low

    dimensional manifold. dimensional manifold. dimensional manifold.

    >> Yeah compared to if you actually add >> Yeah compared to if you actually add
    >> Yeah compared to if you actually add

    noise to it. Yeah. Okay. Any more noise to it. Yeah. Okay. Any more noise to it.
    Yeah. Okay. Any more

    questions? questions? questions?

    No. Okay cool. All right. Uh the second No. Okay cool. All right. Uh the second
    No. Okay cool. All right. Uh the second

    pitfall is actually come from the right pitfall is actually come from the right
    pitfall is actually come from the right

    column. Very nice. Uh basically what''s column. Very nice. Uh basically what''s
    column. Very nice. Uh basically what''s

    happening is that even if we do have happening is that even if we do have happening
    is that even if we do have

    full support data space like even if we full support data space like even if we
    full support data space like even if we

    have probability everywhere the score have probability everywhere the score have
    probability everywhere the score

    estimation is still inaccurate in the estimation is still inaccurate in the estimation
    is still inaccurate in the

    low low density region right because we low low density region right because we
    low low density region right because we

    don''t even see those data very often. So don''t even see those data very often.
    So don''t even see those data very often. So

    how can we learn a a an accurate model how can we learn a a an accurate model
    how can we learn a a an accurate model

    without any data right? So what''s going without any data right? So what''s going'
  concept_slugs:
  - langevin-dynamics
  - score-function
  - score-matching
- idx: 44
  start_sec: 2248.8
  end_sec: 2294.32
  text: 'without any data right? So what''s going

    to happen here is that um so say this is to happen here is that um so say this
    is to happen here is that um so say this is

    like your actual data score that your like your actual data score that your like
    your actual data score that your

    estimated score may look like something estimated score may look like something
    estimated score may look like something

    like this right then our initial samples like this right then our initial samples
    like this right then our initial samples

    are usually in the low density regions are usually in the low density regions
    are usually in the low density regions

    right for example say we sample from a right for example say we sample from a
    right for example say we sample from a

    gausian right the gausian a gausian gausian right the gausian a gausian gausian
    right the gausian a gausian

    image is very very very low density if image is very very very low density if
    image is very very very low density if

    they have any density right it in the they have any density right it in the they
    have any density right it in the

    actual real human face image um actual real human face image um actual real human
    face image um

    distribution so what you''re going to end distribution so what you''re going to
    end distribution so what you''re going to end

    up with you''re going to end up with up with you''re going to end up with up with
    you''re going to end up with

    something here basically. And if you if something here basically. And if you if
    something here basically. And if you if

    you follow the real score, you could by you follow the real score, you could by
    you follow the real score, you could by

    long dynamic go to the high density long dynamic go to the high density long dynamic
    go to the high density

    region. But if you use you learn the region. But if you use you learn the region.
    But if you use you learn the

    score because the learn score doesn''t score because the learn score doesn''t
    score because the learn score doesn''t

    really know where to move in the low really know where to move in the low'
  concept_slugs:
  - langevin-dynamics
  - score-function
  - score-matching
- idx: 45
  start_sec: 2294.32
  end_sec: 2342.15
  text: 'really know where to move in the low

    density region. So you''re just going to density region. So you''re just going
    to density region. So you''re just going to

    move sort of randomly and then you you move sort of randomly and then you you
    move sort of randomly and then you you

    can end up in somewhere like here where can end up in somewhere like here where
    can end up in somewhere like here where

    there''s still low density. there''s still low density. there''s still low density.

    Okay. Okay.

    Any any questions? Any any questions? Any any questions?

    No question. No question. No question.

    All right. Uh, last one is from the All right. Uh, last one is from the All right.
    Uh, last one is from the

    Yeah, it''s from the left column. Yeah, it''s from the left column. Yeah, it''s
    from the left column.

    Basically, what happen is that if you Basically, what happen is that if you Basically,
    what happen is that if you

    just go with a flow, if you just do just go with a flow, if you just do just go
    with a flow, if you just do

    gradient or ascent, right? The gradient gradient or ascent, right? The gradient
    gradient or ascent, right? The gradient

    doesn''t really know like it just knows doesn''t really know like it just knows
    doesn''t really know like it just knows

    that okay uh like from here I should that okay uh like from here I should that
    okay uh like from here I should

    flow to here, from here I should flow to flow to here, from here I should flow
    to flow to here, from here I should flow to

    here, right? it doesn''t really know uh here, right? it doesn''t really know uh
    here, right? it doesn''t really know uh

    like basically it cannot really like basically it cannot really like basically
    it cannot really

    distinguish or like a lot of times it''s distinguish or like a lot of times it''s
    distinguish or like a lot of times it''s

    not completely it''s not 100% you cannot not completely it''s not 100% you cannot
    not completely it''s not 100% you cannot

    but a lot of times it cannot distinguish but a lot of times it cannot distinguish
    but a lot of times it cannot distinguish

    high density from higher density right'
  concept_slugs:
  - langevin-dynamics
  - score-function
  - score-matching
- idx: 46
  start_sec: 2342.15
  end_sec: 2388.15
  text: 'high density from higher density right high density from higher density right

    so like say this is your like intended so like say this is your like intended
    so like say this is your like intended

    data data distribution then your dynamic data data distribution then your dynamic
    data data distribution then your dynamic

    can just look like they have equal can just look like they have equal can just
    look like they have equal

    density in two in the two mixture density in two in the two mixture density in
    two in the two mixture

    whereas because you just follow the whereas because you just follow the whereas
    because you just follow the

    gradient you just go with the flow but gradient you just go with the flow but
    gradient you just go with the flow but

    in reality ity they could have one has in reality ity they could have one has
    in reality ity they could have one has

    higher density and one have lower higher density and one have lower higher density
    and one have lower

    density even though they''re both like density even though they''re both like
    density even though they''re both like

    high density regions so to speak. high density regions so to speak. high density
    regions so to speak.

    >> Yeah. couldn''t. So assuming we had the >> Yeah. couldn''t. So assuming we
    had the >> Yeah. couldn''t. So assuming we had the

    real score function in that case this is real score function in that case this
    is real score function in that case this is

    not a problem right it''s because we not a problem right it''s because we not
    a problem right it''s because we

    could not learn it because in that case could not learn it because in that case
    could not learn it because in that case

    even even even

    >> even if you have it is still a problem >> even if you have it is still a problem
    >> even if you have it is still a problem

    right right

    >> the direction from that low density >> the direction from that low density
    >> the direction from that low density

    region the directions would map towards region the directions would map towards
    region the directions would map towards

    the the

    >> it it depends on like what exactly is'
  concept_slugs:
  - langevin-dynamics
  - score-function
  - score-matching
- idx: 47
  start_sec: 2388.15
  end_sec: 2434.23
  text: '>> it it depends on like what exactly is >> it it depends on like what exactly
    is

    this distribution say if this uh this distribution say if this uh this distribution
    say if this uh

    distribution is a mixture of gausian distribution is a mixture of gausian distribution
    is a mixture of gausian

    where those the the weight of two where those the the weight of two where those
    the the weight of two

    components add up to one so it''s like components add up to one so it''s like
    components add up to one so it''s like

    one minus lambda for for one and then one minus lambda for for one and then one
    minus lambda for for one and then

    lambda for the other then if you lambda for the other then if you lambda for the
    other then if you

    calculate the score the score doesn''t calculate the score the score doesn''t
    calculate the score the score doesn''t

    have lambda in it right so then you have have lambda in it right so then you have
    have lambda in it right so then you have

    no idea I mean technically technically no idea I mean technically technically
    no idea I mean technically technically

    if you move slow enough right if you if you move slow enough right if you if you
    move slow enough right if you

    move like if you just like make micro move like if you just like make micro move
    like if you just like make micro

    movement every time then technically you movement every time then technically
    you movement every time then technically you

    could still sample the correct could still sample the correct could still sample
    the correct

    distribution but then you need to just distribution but then you need to just
    distribution but then you need to just

    do micro movement every time so it''s do micro movement every time so it''s do
    micro movement every time so it''s

    going to be very very slow and in the going to be very very slow and in the going
    to be very very slow and in the

    paper it''s actually called slow mixing paper it''s actually called slow mixing
    paper it''s actually called slow mixing

    of launch dynamic. Yeah, but good of launch dynamic. Yeah, but good of launch
    dynamic. Yeah, but good

    question. question. question.

    Okay.'
  concept_slugs:
  - langevin-dynamics
  - score-function
  - score-matching
- idx: 48
  start_sec: 2434.24
  end_sec: 2508.87
  text: 'Okay.

    All right. Any other question? Cool. Cool.

    All right. So, we have all these All right. So, we have all these All right. So,
    we have all these

    problems. problems. problems.

    Is it problem? Is it possible to solve Is it problem? Is it possible to solve
    Is it problem? Is it possible to solve

    all these problem all at once? all these problem all at once? all these problem
    all at once?

    What do we think? Very true. Very true. But but okay say Very true. Very true.
    But but okay say

    it is possible. it is possible. it is possible.

    What would be the thing to fix What would be the thing to fix What would be the
    thing to fix

    everything? Just say some words like the the the the Just say some words like
    the the the the

    first thing that you think of like the first thing that you think of like the
    first thing that you think of like the

    theme of this this whole lecture theory. theme of this this whole lecture theory.
    theme of this this whole lecture theory.

    Yeah. Yeah. Yay. Yeah. Yeah. Literally. Yeah. Yeah. Yay. Yeah. Yeah. Literally.
    Yeah. Yeah. Yay. Yeah. Yeah. Literally.

    So, yeah, just think about it like every So, yeah, just think about it like every
    So, yeah, just think about it like every

    time you don''t know what to do, you you time you don''t know what to do, you
    you time you don''t know what to do, you you

    channel your inner gouge and this is channel your inner gouge and this is channel
    your inner gouge and this is

    what this is what you do. Okay. Um, what this is what you do. Okay. Um, what this
    is what you do. Okay. Um,

    okay. Actually, literally adding gausian okay. Actually, literally adding gausian
    okay. Actually, literally adding gausian

    noise just solves everything, right? noise just solves everything, right? noise
    just solves everything, right?

    Because basically if you have a perturb Because basically if you have a perturb
    Because basically if you have a perturb

    the distribution now first of all it has the distribution now first of all it
    has the distribution now first of all it has

    support everywhere. So, the manifold support everywhere. So, the manifold support
    everywhere. So, the manifold

    thing doesn''t exist anymore, right? And'
  concept_slugs:
  - langevin-dynamics
  - score-function
  - score-matching
- idx: 49
  start_sec: 2508.87
  end_sec: 2557.76
  text: 'thing doesn''t exist anymore, right? And thing doesn''t exist anymore, right?
    And

    then now the perturbed like say you have then now the perturbed like say you have
    then now the perturbed like say you have

    like a high density to higher density like a high density to higher density like
    a high density to higher density

    right then like uh like like the higher right then like uh like like the higher
    right then like uh like like the higher

    and the high are going to be more and the high are going to be more and the high
    are going to be more

    distinguishable and also the low density distinguishable and also the low density
    distinguishable and also the low density

    region are going to be easier to get region are going to be easier to get region
    are going to be easier to get

    sampled when at during training right so sampled when at during training right
    so sampled when at during training right so

    it''s just going to be like easier for it''s just going to be like easier for
    it''s just going to be like easier for

    the model to learn all right the model to learn all right the model to learn all
    right

    now we should have some questions right now we should have some questions right
    now we should have some questions right

    yes That''s exactly correct. Right. So the That''s exactly correct. Right. So
    the

    problem is if we add noise, right? Like problem is if we add noise, right? Like
    problem is if we add noise, right? Like

    how much noise should we add? Because if how much noise should we add? Because
    if how much noise should we add? Because if

    if if we we add too small amount of if if we we add too small amount of if if
    we we add too small amount of

    noise, then it''s just going to not going noise, then it''s just going to not
    going noise, then it''s just going to not going

    to have any effect, right? If we add too to have any effect, right? If we add
    too to have any effect, right? If we add too

    large of a of a noise, then it you''re large of a of a noise, then it you''re'
  concept_slugs:
  - langevin-dynamics
  - score-function
  - score-matching
- idx: 50
  start_sec: 2557.76
  end_sec: 2613.19
  text: 'large of a of a noise, then it you''re

    just learning a very noisy distribution. just learning a very noisy distribution.
    just learning a very noisy distribution.

    That''s not what we want. So how much That''s not what we want. So how much That''s
    not what we want. So how much

    noise should we add? Right? That''s a noise should we add? Right? That''s a noise
    should we add? Right? That''s a

    that''s the question. That''s the question that''s the question. That''s the question
    that''s the question. That''s the question

    that you that you asked like a while that you that you asked like a while that
    you that you asked like a while

    ago. All right. So, ago. All right. So, ago. All right. So,

    what do we think? >> Yes. >> Yes.

    >> Should be smaller than the step size. >> Should be smaller than the step size.
    >> Should be smaller than the step size.

    >> But now that you you mentioned the step >> But now that you you mentioned the
    step >> But now that you you mentioned the step

    size, size, size,

    >> what are we what are we thinking? >> what are we what are we thinking? >> what
    are we what are we thinking?

    We we have we''re taking many many steps, We we have we''re taking many many steps,
    We we have we''re taking many many steps,

    right? So, right? So, right? So,

    It should decrease as we get closer to It should decrease as we get closer to
    It should decrease as we get closer to

    the the

    >> Yes. >> Yes.

    >> Yeah. Yeah. Yeah. Exactly. Correct. So, >> Yeah. Yeah. Yeah. Exactly. Correct.
    So, >> Yeah. Yeah. Yeah. Exactly. Correct. So,

    what if we just like start big? So, we what if we just like start big? So, we
    what if we just like start big? So, we

    just like at the beginning, let''s just just like at the beginning, let''s just
    just like at the beginning, let''s just

    add a bunch of noise, right? And then as add a bunch of noise, right? And then
    as add a bunch of noise, right? And then as

    we become like more and more confident we become like more and more confident
    we become like more and more confident

    about which region that we are uh that'
  concept_slugs:
  - langevin-dynamics
  - score-function
  - score-matching
- idx: 51
  start_sec: 2613.19
  end_sec: 2659.599
  text: 'about which region that we are uh that about which region that we are uh
    that

    we''re s we should be sampling at, then we''re s we should be sampling at, then
    we''re s we should be sampling at, then

    we''re just going to like decrease the we''re just going to like decrease the
    we''re just going to like decrease the

    noise as we go. noise as we go. noise as we go.

    Right? So this thing is called a Right? So this thing is called a Right? So this
    thing is called a

    kneeling longer dynamic kneeling longer dynamic kneeling longer dynamic

    because it''s a kneeling, right? because it''s a kneeling, right? because it''s
    a kneeling, right?

    Yeah. Also, by the way, a new launch Yeah. Also, by the way, a new launch Yeah.
    Also, by the way, a new launch

    dynamic has a really, really cool dynamic has a really, really cool dynamic has
    a really, really cool

    Chinese name. Like the Chinese Chinese name. Like the Chinese Chinese name. Like
    the Chinese

    translation is so cool. It''s like translation is so cool. It''s like translation
    is so cool. It''s like

    anyway, great name for your Twitter anyway, great name for your Twitter anyway,
    great name for your Twitter

    handle. Not important. The point being, handle. Not important. The point being,
    handle. Not important. The point being,

    so this is how you this is how you do a so this is how you this is how you do
    a so this is how you this is how you do a

    neo dynamic. So you start from the right neo dynamic. So you start from the right
    neo dynamic. So you start from the right

    actually. So you start from the right, actually. So you start from the right,
    actually. So you start from the right,

    you add a lot of noise and then as you you add a lot of noise and then as you
    you add a lot of noise and then as you

    get closer to or more and more certain get closer to or more and more certain
    get closer to or more and more certain

    about which uh region that you should about which uh region that you should about
    which uh region that you should

    sample from, you are going to just sample from, you are going to just'
  concept_slugs:
  - langevin-dynamics
  - score-function
  - score-matching
- idx: 52
  start_sec: 2659.599
  end_sec: 2705.44
  text: 'sample from, you are going to just

    gradually decrease the noise or the gradually decrease the noise or the gradually
    decrease the noise or the

    exploration term that you''re adding at exploration term that you''re adding at
    exploration term that you''re adding at

    each um that at each step. So this also each um that at each step. So this also
    each um that at each step. So this also

    answer the question of why we need answer the question of why we need answer the
    question of why we need

    exploration. Yeah, exploration. Yeah, exploration. Yeah,

    >> this analing effect is what we''re doing >> this analing effect is what we''re
    doing >> this analing effect is what we''re doing

    sampling during training. is still just sampling during training. is still just
    sampling during training. is still just

    part of the distribution with that one part of the distribution with that one
    part of the distribution with that one

    decided noise. decided noise. decided noise.

    >> What do you think? Do you think we >> What do you think? Do you think we >>
    What do you think? Do you think we

    should do that or do you think we should do that or do you think we should do
    that or do you think we

    shouldn''t do that? We should not. Why? shouldn''t do that? We should not. Why?
    shouldn''t do that? We should not. Why?

    >> Because then >> Because then >> Because then

    we we have that distribution and we need we we have that distribution and we need
    we we have that distribution and we need

    messing up that distribution. messing up that distribution. messing up that distribution.

    >> Yeah. Right. So you don''t even know like >> Yeah. Right. So you don''t even
    know like >> Yeah. Right. So you don''t even know like

    basically so at training time you should basically so at training time you should
    basically so at training time you should

    be learning a noise level condition be learning a noise level condition be learning
    a noise level condition

    model. model. model.

    >> Very very good. Very very good. Do we >> Very very good. Very very good. Do
    we >> Very very good. Very very good. Do we

    have that next? uh we have the pseudo have that next? uh we have the pseudo'
  concept_slugs:
  - langevin-dynamics
  - score-function
  - score-matching
- idx: 53
  start_sec: 2705.44
  end_sec: 2750.4
  text: 'have that next? uh we have the pseudo

    code and you know the long dynam dynamic code and you know the long dynam dynamic
    code and you know the long dynam dynamic

    left over. Yeah. But basically literally left over. Yeah. But basically literally
    left over. Yeah. But basically literally

    just uh you you you do you have a step just uh you you you do you have a step
    just uh you you you do you have a step

    size and then you know as as time goes size and then you know as as time goes
    size and then you know as as time goes

    you you decrease the noise that you add. you you decrease the noise that you add.
    you you decrease the noise that you add.

    Um but yeah Um but yeah Um but yeah

    this is why we''re learning a noise this is why we''re learning a noise this is
    why we''re learning a noise

    conditioned score model because now we conditioned score model because now we
    conditioned score model because now we

    do not have one level of noise. We have do not have one level of noise. We have
    do not have one level of noise. We have

    multiple levels of noise. Right? So this multiple levels of noise. Right? So this
    multiple levels of noise. Right? So this

    is like how you would have sample uh is like how you would have sample uh is like
    how you would have sample uh

    from a noise condition score network in from a noise condition score network in
    from a noise condition score network in

    CSN. Uh and u yeah so basically how you CSN. Uh and u yeah so basically how you
    CSN. Uh and u yeah so basically how you

    should parameterize your network is should parameterize your network is should
    parameterize your network is

    going to be uh you should be taking your going to be uh you should be taking your
    going to be uh you should be taking your

    current sample noisy and the current current sample noisy and the current current
    sample noisy and the current

    noise level that you''re dealing with. noise level that you''re dealing with.
    noise level that you''re dealing with.

    And then at training time you do this And then at training time you do this'
  concept_slugs:
  - langevin-dynamics
  - score-function
  - score-matching
- idx: 54
  start_sec: 2750.4
  end_sec: 2843.68
  text: 'And then at training time you do this

    multi-level den noising score matching multi-level den noising score matching
    multi-level den noising score matching

    because at each time you basically because at each time you basically because
    at each time you basically

    you''re doing a denoising score matching you''re doing a denoising score matching
    you''re doing a denoising score matching

    at every noise level. It just you just at every noise level. It just you just
    at every noise level. It just you just

    need to be able to do it with in need to be able to do it with in need to be able
    to do it with in

    multiple levels and at sampling time you multiple levels and at sampling time
    you multiple levels and at sampling time you

    can just do a new launch dynamic. >> Uh you mean like density estimation or >>
    Uh you mean like density estimation or

    what do you mean by learning what do you mean by learning what do you mean by
    learning

    distribution? This is learning distribution? This is learning distribution? This
    is learning

    distribution. distribution. distribution.

    Right. Right. Right.

    >> Yeah. But if you''re asking about density >> Yeah. But if you''re asking about
    density >> Yeah. But if you''re asking about density

    estimation, we''re going to talk about estimation, we''re going to talk about
    estimation, we''re going to talk about

    next class. Actually, we don''t have time next class. Actually, we don''t have
    time next class. Actually, we don''t have time

    for this class. Actually, we may not for this class. Actually, we may not for
    this class. Actually, we may not

    even get through all everything this even get through all everything this even
    get through all everything this

    class, which is interesting. I guess I''m class, which is interesting. I guess
    I''m class, which is interesting. I guess I''m

    improving. Anyway, uh, any more improving. Anyway, uh, any more improving. Anyway,
    uh, any more

    questions? Cool. No more question. Cool. No more question.

    Hold up. Wait a minute. Hold up. Wait a minute. Hold up. Wait a minute.

    Doesn''t that look familiar? It kind of just look like diffusion, It kind of just
    look like diffusion,

    right? What is going on? right? What is going on? right? What is going on?

    Is this just diffusion? Yeah, just just think about it. Uh,'
  concept_slugs:
  - langevin-dynamics
  - score-function
  - score-matching
- idx: 55
  start_sec: 2843.68
  end_sec: 2928.23
  text: 'Yeah, just just think about it. Uh,

    basically the difference between DDPM, basically the difference between DDPM,
    basically the difference between DDPM,

    which is what we learned last last time, which is what we learned last last time,
    which is what we learned last last time,

    and this new thing noise condition score and this new thing noise condition score
    and this new thing noise condition score

    network, network, network,

    if you look at them, if you look at them, if you look at them,

    they''re practically the same. specifically the only difference sort of specifically
    the only difference sort of

    is how you define your noising process is how you define your noising process
    is how you define your noising process

    essentially and how you calculate the essentially and how you calculate the essentially
    and how you calculate the

    loss, right? loss, right? loss, right?

    And uh and it turns out that And uh and it turns out that And uh and it turns
    out that

    they are kind of connected. So basically they are kind of connected. So basically
    they are kind of connected. So basically

    what you can do is you can sort of if what you can do is you can sort of if what
    you can do is you can sort of if

    you define your um the noisy sample with you define your um the noisy sample with
    you define your um the noisy sample with

    respect to the noise and the clean data respect to the noise and the clean data
    respect to the noise and the clean data

    you can sort of like write both of them you can sort of like write both of them
    you can sort of like write both of them

    into the same formula. You just have into the same formula. You just have into
    the same formula. You just have

    different hyperparameter choices for the different hyperparameter choices for
    the different hyperparameter choices for the

    formula formula formula

    and the loss function are pretty much the the loss function are pretty much the

    same. same. same.

    like you''re both learning to d noiseise like you''re both learning to d noiseise
    like you''re both learning to d noiseise

    essentially and the only difference is essentially and the only difference is
    essentially and the only difference is

    that the the the score is sort of it has'
  concept_slugs:
  - langevin-dynamics
  - score-function
  - score-matching
- idx: 56
  start_sec: 2928.23
  end_sec: 2989.109
  text: 'that the the the score is sort of it has that the the the score is sort of
    it has

    like another factor or it has another like another factor or it has another like
    another factor or it has another

    coefficient coefficient coefficient

    in the front. So basically DDPN and this in the front. So basically DDPN and this
    in the front. So basically DDPN and this

    noise noise condition score thing is the noise noise condition score thing is
    the noise noise condition score thing is the

    same thing. same thing. same thing.

    Basically practically the same thing. Basically practically the same thing. Basically
    practically the same thing.

    In other words, In other words, In other words,

    this multi-level score matching thing is this multi-level score matching thing
    is this multi-level score matching thing is

    the same as all the elbow and stuff that the same as all the elbow and stuff that
    the same as all the elbow and stuff that

    we derived from last class. we derived from last class. we derived from last class.

    Isn''t that cool? I thought that was Isn''t that cool? I thought that was Isn''t
    that cool? I thought that was

    pretty cool. pretty cool. pretty cool.

    Anyhow, so basically they''re the same Anyhow, so basically they''re the same
    Anyhow, so basically they''re the same

    thing. If you need to remember anything thing. If you need to remember anything
    thing. If you need to remember anything

    from this class, this is one you need to from this class, this is one you need
    to from this class, this is one you need to

    remember. Scorebased model, diffusion remember. Scorebased model, diffusion remember.
    Scorebased model, diffusion

    model, pretty much the same thing. model, pretty much the same thing. model, pretty
    much the same thing.

    We just have two ways to derive them, We just have two ways to derive them, We
    just have two ways to derive them,

    but they''re the same. Uh, but they''re the same. Uh, but they''re the same. Uh,

    okay, let''s see if we can get through okay, let''s see if we can get through
    okay, let''s see if we can get through

    this. Uh, so what''s going to happen if this. Uh, so what''s going to happen if
    this. Uh, so what''s going to happen if

    we have infinite numbers of noise level?'
  concept_slugs:
  - langevin-dynamics
  - score-function
  - score-matching
- idx: 57
  start_sec: 2989.109
  end_sec: 3047.92
  text: 'we have infinite numbers of noise level? we have infinite numbers of noise
    level?

    What do you what do we think is going to What do you what do we think is going
    to What do you what do we think is going to

    happen? mode collapse. mode collapse.

    >> It''s actually not going to do more >> It''s actually not going to do more
    >> It''s actually not going to do more

    collapse. Good choice. Good. Good. Good collapse. Good choice. Good. Good. Good
    collapse. Good choice. Good. Good. Good

    try. But it''s not going to try. But it''s not going to try. But it''s not going
    to

    >> Yeah. Yeah. Yeah. What you say? >> Yeah. Yeah. Yeah. What you say? >> Yeah.
    Yeah. Yeah. What you say?

    >> Then just have like a continuous. >> Yes. You''re just gonna have a continuous
    >> Yes. You''re just gonna have a continuous

    thing, right? So it becomes what we call thing, right? So it becomes what we call
    thing, right? So it becomes what we call

    a continuous time stoastic process which a continuous time stoastic process which
    a continuous time stoastic process which

    can pretty much be defined by a stoastic can pretty much be defined by a stoastic
    can pretty much be defined by a stoastic

    differential equation or what we just differential equation or what we just differential
    equation or what we just

    going to call now SDEES. going to call now SDEES. going to call now SDEES.

    All right. All right.

    And uh so when we have infinite amount And uh so when we have infinite amount
    And uh so when we have infinite amount

    uh infinite numbers of noise levels uh uh infinite numbers of noise levels uh
    uh infinite numbers of noise levels uh

    what it''s going to do is that you can what it''s going to do is that you can
    what it''s going to do is that you can

    actually write the forward process into actually write the forward process into
    actually write the forward process into

    this um so this is like a first order this um so this is like a first order this
    um so this is like a first order

    tailor estimation of of of the real tailor estimation of of of the real'
  concept_slugs:
  - langevin-dynamics
  - score-function
  - score-matching
- idx: 58
  start_sec: 3047.92
  end_sec: 3102.72
  text: 'tailor estimation of of of the real

    thing and you can actually write both of thing and you can actually write both
    of thing and you can actually write both of

    them into this this format and uh if you them into this this format and uh if
    you them into this this format and uh if you

    organize it a little bit both of them organize it a little bit both of them organize
    it a little bit both of them

    actually also share the same formulation actually also share the same formulation
    actually also share the same formulation

    now. So now it becomes basically now. So now it becomes basically now. So now
    it becomes basically

    to move forward for delta time delta t to move forward for delta time delta t
    to move forward for delta time delta t

    steps you are actually just adding steps you are actually just adding steps you
    are actually just adding

    some function times delta t which is the some function times delta t which is
    the some function times delta t which is the

    time interval that you''re going to move time interval that you''re going to move
    time interval that you''re going to move

    forward plus forward plus forward plus

    some scaled uh some some scaled gausian some scaled uh some some scaled gausian
    some scaled uh some some scaled gausian

    noise and this is scaling is also noise and this is scaling is also noise and
    this is scaling is also

    depending on the delta t that you''re depending on the delta t that you''re depending
    on the delta t that you''re

    moving and similarly for ddpm this is moving and similarly for ddpm this is moving
    and similarly for ddpm this is

    the same only the only difference is that the only the only difference is that
    the

    choice of the function the two functions choice of the function the two functions
    choice of the function the two functions

    are going to be different for both. Um are going to be different for both. Um
    are going to be different for both. Um

    so essentially what you can do and so essentially what you can do and so essentially
    what you can do and

    because you see how like basically if because you see how like basically if'
  concept_slugs:
  - langevin-dynamics
  - score-function
  - score-matching
- idx: 59
  start_sec: 3102.72
  end_sec: 3148.15
  text: 'because you see how like basically if

    you do xt plus delta t minus xt is going you do xt plus delta t minus xt is going
    you do xt plus delta t minus xt is going

    to be this thing right. So it''s going to to be this thing right. So it''s going
    to to be this thing right. So it''s going to

    be uh f * delta t plus g * square root be uh f * delta t plus g * square root
    be uh f * delta t plus g * square root

    of delta t plus uh times some gausian of delta t plus uh times some gausian of
    delta t plus uh times some gausian

    noise. So basically if you take delta t noise. So basically if you take delta
    t noise. So basically if you take delta t

    to infinite decimally small then you are to infinite decimally small then you
    are to infinite decimally small then you are

    going to be able to get this sd right. going to be able to get this sd right.
    going to be able to get this sd right.

    Why this is a sd because uh this part is Why this is a sd because uh this part
    is Why this is a sd because uh this part is

    deterministic right? So this part is deterministic right? So this part is deterministic
    right? So this part is

    what we call the drift. So like what we call the drift. So like what we call the
    drift. So like

    basically this is just like how you''re basically this is just like how you''re
    basically this is just like how you''re

    gonna shift and then this is where you gonna shift and then this is where you
    gonna shift and then this is where you

    add a gausian noise. This W thing is add a gausian noise. This W thing is add
    a gausian noise. This W thing is

    what they call the wiener process. Uh what they call the wiener process. Uh what
    they call the wiener process. Uh

    but it''s also just brownian motion just but it''s also just brownian motion just
    but it''s also just brownian motion just

    literally gausian noise basically. So literally gausian noise basically. So literally
    gausian noise basically. So

    you just add some stoasticity. So this'
  concept_slugs:
  - langevin-dynamics
  - score-function
  - score-matching
- idx: 60
  start_sec: 3148.15
  end_sec: 3208.0
  text: 'you just add some stoasticity. So this you just add some stoasticity. So
    this

    is why it''s called stochastic is why it''s called stochastic is why it''s called
    stochastic

    differential equation. differential equation. differential equation.

    Okay. Okay, any question? So this is a Okay. Okay, any question? So this is a
    Okay. Okay, any question? So this is a

    forward process. All right, now we have a forward All right, now we have a forward

    process. How do we learn the backward process. How do we learn the backward process.
    How do we learn the backward

    process? >> It''s literally just a reverse SDE. >> It''s literally just a reverse
    SDE.

    Actually, there''s a dude called Anderson Actually, there''s a dude called Anderson
    Actually, there''s a dude called Anderson

    and this dude in 1982 just give you the and this dude in 1982 just give you the
    and this dude in 1982 just give you the

    formula. Basically it just be like if formula. Basically it just be like if formula.
    Basically it just be like if

    you have a for SDE you can literally get you have a for SDE you can literally
    get you have a for SDE you can literally get

    a backward SD uh like back if you are a backward SD uh like back if you are a
    backward SD uh like back if you are

    trying to estimate some distribution and trying to estimate some distribution
    and trying to estimate some distribution and

    and and this backore SD or this reverse and and this backore SD or this reverse
    and and this backore SD or this reverse

    SDE is going to have a score function in SDE is going to have a score function
    in SDE is going to have a score function in

    it. Oh it. Oh it. Oh

    dang. Uh so now now if you if you look dang. Uh so now now if you if you look
    dang. Uh so now now if you if you look

    at it right the f and the g are both at it right the f and the g are both at it
    right the f and the g are both

    defined by our foret defined by our foret defined by our foret

    and we choose the for process right so and we choose the for process right so'
  concept_slugs:
  - langevin-dynamics
  - score-function
  - score-matching
- idx: 61
  start_sec: 3208.0
  end_sec: 3261.51
  text: 'and we choose the for process right so

    we know f and g uh and then it''s we know f and g uh and then it''s we know f
    and g uh and then it''s

    literally just gausian right so who literally just gausian right so who literally
    just gausian right so who

    cares like we you can sample gausian any cares like we you can sample gausian
    any cares like we you can sample gausian any

    any from any time right so the only any from any time right so the only any from
    any time right so the only

    thing that needs to be learned is thing that needs to be learned is thing that
    needs to be learned is

    literally the score function right so literally the score function right so literally
    the score function right so

    how you train a score SDE is literally how you train a score SDE is literally
    how you train a score SDE is literally

    just score matching in continuous time just score matching in continuous time
    just score matching in continuous time

    and that''s it. So we just already and that''s it. So we just already and that''s
    it. So we just already

    learned how to you know train this re learned how to you know train this re learned
    how to you know train this re

    reverse SDE model already. reverse SDE model already. reverse SDE model already.

    Okay. Okay.

    And for sampling uh basically for any And for sampling uh basically for any And
    for sampling uh basically for any

    differential equation you can sort try differential equation you can sort try
    differential equation you can sort try

    to use a solver to solve it. This is to use a solver to solve it. This is to use
    a solver to solve it. This is

    like some fancy name um but it''s like some fancy name um but it''s like some
    fancy name um but it''s

    literally just like how you discretise literally just like how you discretise
    literally just like how you discretise

    your steps and then try to make your steps and then try to make your steps and
    then try to make

    estimations and for example if you try estimations and for example if you try
    estimations and for example if you try

    to use a oiler solver which is like'
  concept_slugs:
  - langevin-dynamics
  - score-function
  - score-matching
- idx: 62
  start_sec: 3261.51
  end_sec: 3309.03
  text: 'to use a oiler solver which is like to use a oiler solver which is like

    probably simple simplest solver uh that probably simple simplest solver uh that
    probably simple simplest solver uh that

    then you can literally just do your then you can literally just do your then you
    can literally just do your

    first sample from your source first sample from your source first sample from
    your source

    distribution and remember now because we distribution and remember now because
    we distribution and remember now because we

    have continuous time so the time goes have continuous time so the time goes have
    continuous time so the time goes

    from zero to one continuously so there''s from zero to one continuously so there''s
    from zero to one continuously so there''s

    no big t anymore okay so now we sample no big t anymore okay so now we sample
    no big t anymore okay so now we sample

    x1 one from the source distribution. x1 one from the source distribution. x1 one
    from the source distribution.

    This is basically X big T. And then we This is basically X big T. And then we
    This is basically X big T. And then we

    estimate the displacement of the X that estimate the displacement of the X that
    estimate the displacement of the X that

    we''re going to make for this delta T we''re going to make for this delta T we''re
    going to make for this delta T

    time and we just use the reverse SDE time and we just use the reverse SDE time
    and we just use the reverse SDE

    formula, right? And then the only thing formula, right? And then the only thing
    formula, right? And then the only thing

    that we do not know from the reverse SD that we do not know from the reverse SD
    that we do not know from the reverse SD

    formula is the score. But we already formula is the score. But we already formula
    is the score. But we already

    learned a model from score matching. So learned a model from score matching. So
    learned a model from score matching. So

    this is nice. And we literally just this is nice. And we literally just this is
    nice. And we literally just

    apply the change in x to x and then we'
  concept_slugs:
  - langevin-dynamics
  - score-function
  - score-matching
- idx: 63
  start_sec: 3309.03
  end_sec: 3373.91
  text: 'apply the change in x to x and then we apply the change in x to x and then
    we

    apply delta t to t apply delta t to t apply delta t to t

    and that''s it. and that''s it. and that''s it.

    And then we iterate until t becomes And then we iterate until t becomes And then
    we iterate until t becomes

    zero. zero. zero.

    Oh, I guess in this case I guess it Oh, I guess in this case I guess it Oh, I
    guess in this case I guess it

    should it should start from zero and should it should start from zero and should
    it should start from zero and

    then t becomes one. But you know same then t becomes one. But you know same then
    t becomes one. But you know same

    similar or or or I guess the t should be minus. or or or I guess the t should
    be minus.

    Yeah. Any question? Yeah. question? Yeah.

    >> In DDPM in the forward process, we can >> In DDPM in the forward process, we
    can >> In DDPM in the forward process, we can

    get the image at any time step get the image at any time step get the image at
    any time step

    instantly. Can we do this with the SD as instantly. Can we do this with the SD
    as instantly. Can we do this with the SD as

    well? well? well?

    >> What do you think? >> What do you think? >> What do you think?

    >> Not sure. >> Not sure. >> Not sure.

    >> Why not? It''s still a bunch of gausian, >> Why not? It''s still a bunch of
    gausian, >> Why not? It''s still a bunch of gausian,

    right? Actually, great question. Now right? Actually, great question. Now right?
    Actually, great question. Now

    that you mentioned the DDPM, uh basically uh basically

    uh the DDPM and NCSN are this uh the DDPM and NCSN are this uh the DDPM and NCSN
    are this

    three time version of the of the model, three time version of the of the model,
    three time version of the of the model,

    right? And we know that they can be right? And we know that they can be right?
    And we know that they can be

    written as this like this function this'
  concept_slugs:
  - langevin-dynamics
  - score-function
  - score-matching
- idx: 64
  start_sec: 3373.91
  end_sec: 3440.079
  text: 'written as this like this function this written as this like this function
    this

    this uh so there are four process can be this uh so there are four process can
    be this uh so there are four process can be

    written as this function of f and g written as this function of f and g written
    as this function of f and g

    right. So actually if you just make it right. So actually if you just make it
    right. So actually if you just make it

    continuous time and then it''s just going continuous time and then it''s just
    going continuous time and then it''s just going

    to become the continuous version of DDPM to become the continuous version of DDPM
    to become the continuous version of DDPM

    and uh ncsn um and this is just going to and uh ncsn um and this is just going
    to and uh ncsn um and this is just going to

    become become become

    literally literally literally

    uh yeah it''s literally just the same uh yeah it''s literally just the same uh
    yeah it''s literally just the same

    thing basically but with continuous time thing basically but with continuous time
    thing basically but with continuous time

    step. Okay, any more questions? Okay, any more questions?

    >> Yeah. VP. VP.

    >> Great question. VP means variance >> Great question. VP means variance >> Great
    question. VP means variance

    preserving. V means variance exploding. preserving. V means variance exploding.
    preserving. V means variance exploding.

    Why? What do you think? >> All right. Yeah. Yeah. >> All right. Yeah. Yeah.

    >> Because >> Because >> Because

    like adds variance to your uh to your like adds variance to your uh to your like
    adds variance to your uh to your

    process. So the more fine steps you process. So the more fine steps you process.
    So the more fine steps you

    take, the more variance. take, the more variance. take, the more variance.

    >> Yeah, basic. Yeah, pretty much. So >> Yeah, basic. Yeah, pretty much. So >>
    Yeah, basic. Yeah, pretty much. So

    basically as you can see here right so basically as you can see here right so
    basically as you can see here right so

    the G as variance and in the VE the G as variance and in the VE'
  concept_slugs:
  - langevin-dynamics
  - score-function
  - score-matching
- idx: 65
  start_sec: 3440.079
  end_sec: 3489.43
  text: 'the G as variance and in the VE

    formulation we do not have any formulation we do not have any formulation we do
    not have any

    adjustment of the X like whatever X you adjustment of the X like whatever X you
    adjustment of the X like whatever X you

    have you''re going to add more variance have you''re going to add more variance
    have you''re going to add more variance

    to it so that''s why it''s various to it so that''s why it''s various to it so
    that''s why it''s various

    exploding and then variance preserving exploding and then variance preserving
    exploding and then variance preserving

    is because we''re actually going to is because we''re actually going to is because
    we''re actually going to

    adjust the variance the total variance adjust the variance the total variance
    adjust the variance the total variance

    of the whole thing so that the variance of the whole thing so that the variance
    of the whole thing so that the variance

    is sort of just like quote unquote uni is sort of just like quote unquote uni
    is sort of just like quote unquote uni

    variant if you will so you''re just like variant if you will so you''re just like
    variant if you will so you''re just like

    variance preserving so you all you''re variance preserving so you all you''re
    variance preserving so you all you''re

    going to preserve the same variance as going to preserve the same variance as
    going to preserve the same variance as

    you you you

    Okay, Okay, Okay,

    perfect timing actually. Okay, so now we perfect timing actually. Okay, so now
    we perfect timing actually. Okay, so now we

    can train this score SD model and it can train this score SD model and it can
    train this score SD model and it

    works super well. This is like a 1K works super well. This is like a 1K works
    super well. This is like a 1K

    image. Absolutely gorgeous. Um, yeah. So image. Absolutely gorgeous. Um, yeah.
    So image. Absolutely gorgeous. Um, yeah. So

    now uh we have seen a bunch now uh we have seen a bunch now uh we have seen a
    bunch

    of gener models and the last class we of gener models and the last class we of
    gener models and the last class we

    did diffusion. This class we did'
  concept_slugs:
  - langevin-dynamics
  - score-function
  - score-matching
- idx: 66
  start_sec: 3489.43
  end_sec: 3536.44
  text: 'did diffusion. This class we did did diffusion. This class we did

    scorebased model and we also learned scorebased model and we also learned scorebased
    model and we also learned

    that they''re basically just the same that they''re basically just the same that
    they''re basically just the same

    thing, right? Okay, they they can be thing, right? Okay, they they can be thing,
    right? Okay, they they can be

    unified um under the same score SDE unified um under the same score SDE unified
    um under the same score SDE

    formulation. Um the question now that formulation. Um the question now that formulation.
    Um the question now that

    Joshman asked was that Joshman asked was that Joshman asked was that

    now but we derive it everything from the now but we derive it everything from
    the now but we derive it everything from the

    sampling perspective. sampling perspective. sampling perspective.

    How do we do density estimation? Right? How do we do density estimation? Right?
    How do we do density estimation? Right?

    How do we actually calculate the How do we actually calculate the How do we actually
    calculate the

    distribution or the likelihood? Um we distribution or the likelihood? Um we distribution
    or the likelihood? Um we

    haven''t talked about that. We''re going haven''t talked about that. We''re going
    haven''t talked about that. We''re going

    to talk about that next class. And also, to talk about that next class. And also,
    to talk about that next class. And also,

    is there even simpler way to do the same is there even simpler way to do the same
    is there even simpler way to do the same

    thing? I feel like everything just too thing? I feel like everything just too
    thing? I feel like everything just too

    complicated. Is what is the simplest way complicated. Is what is the simplest
    way complicated. Is what is the simplest way

    to do the same thing that we want to do? to do the same thing that we want to
    do? to do the same thing that we want to do?

    This is what we''re going to talk about This is what we''re going to talk about
    This is what we''re going to talk about

    next class, which is flow matching. next class, which is flow matching. next class,
    which is flow matching.

    Okay, class is over. Thank you guys.'
  concept_slugs:
  - langevin-dynamics
  - score-function
  - score-matching
---
# CMU 10799 S26: Lecture 4 - Score-based Models - Diffusion & Flow Matching

See the structured chunks above.
