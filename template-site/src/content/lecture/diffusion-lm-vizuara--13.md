---
course_slug: diffusion-lm-vizuara
idx: 13
title: 'Lecture 12: Diffusion LLM Noising Schedule'
video_url: https://www.youtube.com/watch?v=dov4OzCcjU0
duration_sec: null
chunks:
- idx: 0
  start_sec: 3.75
  end_sec: 57.11
  text: 'So what we aim to do is as follows. We So what we aim to do is as follows.
    We

    have a true probability distribution, have a true probability distribution, have
    a true probability distribution,

    right? So let''s say the meaningful right? So let''s say the meaningful right?
    So let''s say the meaningful

    sentences look like this in probability sentences look like this in probability
    sentences look like this in probability

    distribution space. We want to get a distribution space. We want to get a distribution
    space. We want to get a

    probability distribution probability distribution probability distribution

    or we want to predict a probability or we want to predict a probability or we
    want to predict a probability

    distribution which is as close to this distribution which is as close to this
    distribution which is as close to this

    true probability distribution. true probability distribution. true probability
    distribution.

    But we want to predict this not with an But we want to predict this not with an
    But we want to predict this not with an

    auto reggressive model but we want to auto reggressive model but we want to auto
    reggressive model but we want to

    use a diffusion model use a diffusion model use a diffusion model

    for getting this probability for getting this probability for getting this probability

    distribution of the predicted sentences. distribution of the predicted sentences.
    distribution of the predicted sentences.

    Right? Right? Right?

    So we will integrate the three main So we will integrate the three main So we
    will integrate the three main

    characteristics of diffusion models. characteristics of diffusion models. characteristics
    of diffusion models.

    First we need a noising process. Second First we need a noising process. Second
    First we need a noising process. Second

    we need to predict the noise using some we need to predict the noise using some
    we need to predict the noise using some

    sort of a model. And third we need a sort of a model. And third we need a sort
    of a model. And third we need a

    dnoising process. The noising process in dnoising process. The noising process
    in dnoising process. The noising process in

    the case of images was adding noise to the case of images was adding noise to
    the case of images was adding noise to

    an image using a noising schedule maybe'
  concept_slugs:
  - diffusion-language-model
  - masked-diffusion
  - noise-schedule
- idx: 1
  start_sec: 57.11
  end_sec: 101.36
  text: 'an image using a noising schedule maybe an image using a noising schedule
    maybe

    a goshian schedule. The predicting noise a goshian schedule. The predicting noise
    a goshian schedule. The predicting noise

    was the ML model called unit in the case was the ML model called unit in the case
    was the ML model called unit in the case

    of images and the dnoising process which of images and the dnoising process which
    of images and the dnoising process which

    they had was just uh reversing uh the they had was just uh reversing uh the they
    had was just uh reversing uh the

    noising process backwards so that we can noising process backwards so that we
    can noising process backwards so that we can

    generate images from noise. Again I want generate images from noise. Again I want
    generate images from noise. Again I want

    to bring your attention to this visual to bring your attention to this visual
    to bring your attention to this visual

    which we saw in the dnoising process. which we saw in the dnoising process. which
    we saw in the dnoising process.

    What happens is we start with complete What happens is we start with complete
    What happens is we start with complete

    noise and then we bring it back to the noise and then we bring it back to the
    noise and then we bring it back to the

    original image. Now let''s start original image. Now let''s start original image.
    Now let''s start

    implementing these characteristics step implementing these characteristics step
    implementing these characteristics step

    by step. So how do we first of all let''s by step. So how do we first of all let''s
    by step. So how do we first of all let''s

    start with noising process. How do we start with noising process. How do we start
    with noising process. How do we

    integrate noising process in the text? integrate noising process in the text?
    integrate noising process in the text?

    Okay, this is where our understanding of Okay, this is where our understanding
    of Okay, this is where our understanding of

    the ARM model is going to play a very the ARM model is going to play a very the
    ARM model is going to play a very

    very crucial role. Right? So let''s see very crucial role. Right? So let''s see'
  concept_slugs:
  - diffusion-language-model
  - masked-diffusion
  - noise-schedule
- idx: 2
  start_sec: 101.36
  end_sec: 152.63
  text: 'very crucial role. Right? So let''s see

    how noising is included. how noising is included. how noising is included.

    What is the noising process in the text? What is the noising process in the text?
    What is the noising process in the text?

    Right? Right?

    And for this the first thing which is And for this the first thing which is And
    for this the first thing which is

    going to be extremely crucial for us is going to be extremely crucial for us is
    going to be extremely crucial for us is

    that in the case of images we had an that in the case of images we had an that
    in the case of images we had an

    image right which we want to noise or image right which we want to noise or image
    right which we want to noise or

    which we want to subsequently add noise which we want to subsequently add noise
    which we want to subsequently add noise

    to. Um let''s say the image was that of a to. Um let''s say the image was that
    of a to. Um let''s say the image was that of a

    Chinese character. That was an image. We Chinese character. That was an image.
    We Chinese character. That was an image. We

    can successfully go on adding noise to can successfully go on adding noise to
    can successfully go on adding noise to

    this image. this image. this image.

    We add noise. So this is for images. So this is for images.

    What about text? How do we go about What about text? How do we go about What about
    text? How do we go about

    adding noise to a piece of text? So how adding noise to a piece of text? So how
    adding noise to a piece of text? So how

    do we corrupt a piece of text? So the do we corrupt a piece of text? So the do
    we corrupt a piece of text? So the

    whole idea would be to take a bunch of whole idea would be to take a bunch of
    whole idea would be to take a bunch of

    text to corrupt it with noise to predict text to corrupt it with noise to predict
    text to corrupt it with noise to predict

    that noise and then when we start with'
  concept_slugs:
  - diffusion-language-model
  - masked-diffusion
  - noise-schedule
- idx: 3
  start_sec: 152.63
  end_sec: 212.949
  text: 'that noise and then when we start with that noise and then when we start
    with

    noise, we can predict the original text noise, we can predict the original text
    noise, we can predict the original text

    just like how we did in images. So first just like how we did in images. So first
    just like how we did in images. So first

    is how do we add noise to text? is how do we add noise to text? is how do we add
    noise to text?

    So let''s think about ARMs, right? What So let''s think about ARMs, right? What
    So let''s think about ARMs, right? What

    happens in ARMs? ARMs have this uh ARM have this architecture, right? And ARM
    have this architecture, right? And

    here I''m again it''s the exact same here I''m again it''s the exact same here
    I''m again it''s the exact same

    architecture but just a different uh architecture but just a different uh architecture
    but just a different uh

    visual here. So what ARMs do is that you visual here. So what ARMs do is that
    you visual here. So what ARMs do is that you

    have this piece of text which is passed have this piece of text which is passed
    have this piece of text which is passed

    into this architecture. Right? Let''s say into this architecture. Right? Let''s
    say into this architecture. Right? Let''s say

    I have this piece of text called the I have this piece of text called the I have
    this piece of text called the

    next day is bright. next day is bright. next day is bright.

    Okay, I have tokenized it. So let''s say Okay, I have tokenized it. So let''s
    say Okay, I have tokenized it. So let''s say

    the token ids are 1 11 20,000 the token ids are 1 11 20,000 the token ids are
    1 11 20,000

    55 and 3,000. 55 and 3,000. 55 and 3,000.

    And then what I have done is that I have And then what I have done is that I have
    And then what I have done is that I have

    converted it into embedding vectors. converted it into embedding vectors. converted
    it into embedding vectors.

    That''s the next step. So token That''s the next step. So token That''s the next
    step. So token

    embedding. So this is a 384 dimensional'
  concept_slugs:
  - diffusion-language-model
  - masked-diffusion
  - noise-schedule
- idx: 4
  start_sec: 212.949
  end_sec: 284.4
  text: 'embedding. So this is a 384 dimensional embedding. So this is a 384 dimensional

    vector. vector. vector.

    This is a 384 dimensional vector. This is a 384 dimensional vector. This is a
    384 dimensional vector.

    I''ll just mute my discord. This is a I''ll just mute my discord. This is a I''ll
    just mute my discord. This is a

    384dimensional vector. 384dimensional vector. 384dimensional vector.

    This is a 384dimensional vector. This is a 384dimensional vector. This is a 384dimensional
    vector.

    And this is again a 384dimensional And this is again a 384dimensional And this
    is again a 384dimensional

    vector. Right? This is how it works for vector. Right? This is how it works for
    vector. Right? This is how it works for

    auto reggressive models. Now the auto reggressive models. Now the auto reggressive
    models. Now the

    question which I''m asking to all of you question which I''m asking to all of
    you question which I''m asking to all of you

    is that is that is that

    I want to start with the first step of I want to start with the first step of
    I want to start with the first step of

    these three these three these three

    three characteristics which is the three characteristics which is the three characteristics
    which is the

    noising process. How do I corrupt the noising process. How do I corrupt the noising
    process. How do I corrupt the

    given piece of text by adding noise? given piece of text by adding noise? given
    piece of text by adding noise?

    What can I do over here? So that noise What can I do over here? So that noise
    What can I do over here? So that noise

    is added. Now what does noise mean? is added. Now what does noise mean? is added.
    Now what does noise mean?

    Noise essentially means that this piece Noise essentially means that this piece
    Noise essentially means that this piece

    of text right now let''s say I have the of text right now let''s say I have the
    of text right now let''s say I have the

    actual distribution of true sentences. actual distribution of true sentences.
    actual distribution of true sentences.

    Right? This is the true true sentences Right? This is the true true sentences
    Right? This is the true true sentences

    probability distribution. Let me Let me

    this is the true this is the true'
  concept_slugs:
  - diffusion-language-model
  - masked-diffusion
  - noise-schedule
- idx: 5
  start_sec: 284.4
  end_sec: 325.59
  text: 'this is the true

    sentences probability distribution. sentences probability distribution. sentences
    probability distribution.

    This and this sentence the next day is This and this sentence the next day is
    This and this sentence the next day is

    bright belongs somewhere here. The next bright belongs somewhere here. The next
    bright belongs somewhere here. The next

    day is bright lies somewhere here. So day is bright lies somewhere here. So day
    is bright lies somewhere here. So

    the probability associated with this. So the probability associated with this.
    So the probability associated with this. So

    if this sentence is X, probability if this sentence is X, probability if this
    sentence is X, probability

    associated with X is very high because associated with X is very high because
    associated with X is very high because

    this is a good sentence. Now I want to this is a good sentence. Now I want to
    this is a good sentence. Now I want to

    corrupt this text which means I want to corrupt this text which means I want to
    corrupt this text which means I want to

    take it to spaces. So if this is my take it to spaces. So if this is my take it
    to spaces. So if this is my

    probability distribution space, I want probability distribution space, I want
    probability distribution space, I want

    to take it to spaces here where the to take it to spaces here where the to take
    it to spaces here where the

    probability is very low of it being a probability is very low of it being a probability
    is very low of it being a

    true sentence. How do I do that? How do true sentence. How do I do that? How do
    true sentence. How do I do that? How do

    I corrupt a sentence? The best way to I corrupt a sentence? The best way to I
    corrupt a sentence? The best way to

    corrupt a sentence is to just remove corrupt a sentence is to just remove corrupt
    a sentence is to just remove

    portions of it. Right? portions of it. Right? portions of it. Right?

    If I remove portion of this, if I remove If I remove portion of this, if I remove
    If I remove portion of this, if I remove

    a portion of this, this is no longer a'
  concept_slugs:
  - diffusion-language-model
  - masked-diffusion
  - noise-schedule
- idx: 6
  start_sec: 325.59
  end_sec: 393.12
  text: 'a portion of this, this is no longer a a portion of this, this is no longer
    a

    true sentence. It becomes a cor, it true sentence. It becomes a cor, it true sentence.
    It becomes a cor, it

    becomes a corrupt text or it becomes a becomes a corrupt text or it becomes a
    becomes a corrupt text or it becomes a

    noisy text. Um, this is exactly how noisy text. Um, this is exactly how noisy
    text. Um, this is exactly how

    noising is done at the sentence level. noising is done at the sentence level.
    noising is done at the sentence level.

    So we have input sequences or we have So we have input sequences or we have So
    we have input sequences or we have

    sequences of tokens, right? sequences of tokens, right? sequences of tokens, right?

    In diffusion language models, we corrupt In diffusion language models, we corrupt
    In diffusion language models, we corrupt

    this text by introducing masks. this text by introducing masks. this text by introducing
    masks.

    What this means is that if I have the What this means is that if I have the What
    this means is that if I have the

    next day is bright, next day is bright, next day is bright,

    I will mask this input sequence. Which I will mask this input sequence. Which
    I will mask this input sequence. Which

    means I will let I will say that the means I will let I will say that the means
    I will let I will say that the

    input sequence is this. The mask input sequence is this. The mask input sequence
    is this. The mask

    day mask mask

    bright. bright. bright.

    This is basically corrupting the input This is basically corrupting the input
    This is basically corrupting the input

    sequence by adding masks. sequence by adding masks. sequence by adding masks.

    Right? Uh now how do I add these masks? Right? Uh now how do I add these masks?
    Right? Uh now how do I add these masks?

    The the way I add these masks is by The the way I add these masks is by The the
    way I add these masks is by

    defining something like a noising defining something like a noising defining something
    like a noising

    schedule. Right? So first I define a schedule. Right? So first I define a'
  concept_slugs:
  - diffusion-language-model
  - masked-diffusion
  - noise-schedule
- idx: 7
  start_sec: 393.12
  end_sec: 462.8
  text: 'schedule. Right? So first I define a

    time step. Let''s say I go from time time step. Let''s say I go from time time
    step. Let''s say I go from time

    equal to 1 till time equal to 6. equal to 1 till time equal to 6. equal to 1 till
    time equal to 6.

    And I define the number of tokens uh proportional to uh proportional to

    let''s say my time let''s say t divided by let''s say my time let''s say t divided
    by let''s say my time let''s say t divided by

    so if 6 is capital t divided by capital so if 6 is capital t divided by capital
    so if 6 is capital t divided by capital

    t so if my t is equal to 1 t so if my t is equal to 1 t so if my t is equal to
    1

    um I will approximately mask um I will approximately mask um I will approximately
    mask

    16th of the tokens If my t is equal to 2, I will If my t is equal to 2, I will

    approximately mask 26 of the tokens. If approximately mask 26 of the tokens. If
    approximately mask 26 of the tokens. If

    my t is equal to 6, I will mask all of my t is equal to 6, I will mask all of
    my t is equal to 6, I will mask all of

    the tokens. So you see at t equal to0, I have my So you see at t equal to0, I
    have my

    entire entire entire

    clean sequence which is not masked. So clean sequence which is not masked. So
    clean sequence which is not masked. So

    that''s the correct sequence. Think of it that''s the correct sequence. Think
    of it that''s the correct sequence. Think of it

    like lying in the correct probability like lying in the correct probability like
    lying in the correct probability

    distribution space. As more and more distribution space. As more and more distribution
    space. As more and more

    noise gets added, I move out of this noise gets added, I move out of this noise
    gets added, I move out of this

    probability distribution space and start probability distribution space and start
    probability distribution space and start

    going haywire. So maybe initially when going haywire. So maybe initially when'
  concept_slugs:
  - diffusion-language-model
  - masked-diffusion
  - noise-schedule
- idx: 8
  start_sec: 462.8
  end_sec: 536.08
  text: 'going haywire. So maybe initially when

    only one mask is added, I go to a lower only one mask is added, I go to a lower
    only one mask is added, I go to a lower

    probability. When two masks are added, I probability. When two masks are added,
    I probability. When two masks are added, I

    go to even lower probability. When all go to even lower probability. When all
    go to even lower probability. When all

    the masks are added, it''s complete the masks are added, it''s complete the masks
    are added, it''s complete

    noise. So I go to a probability noise. So I go to a probability noise. So I go
    to a probability

    distribution or I go to a space in my distribution or I go to a space in my distribution
    or I go to a space in my

    probability distribution space which probability distribution space which probability
    distribution space which

    contains no meaningful text at all. I go contains no meaningful text at all. I
    go contains no meaningful text at all. I go

    to a random location basically. to a random location basically. to a random location
    basically.

    Uh so if you see Uh so if you see Uh so if you see

    diffusion noise schedule images diffusion noise schedule images diffusion noise
    schedule images

    and maybe let''s see a gif. Noising schedule. Noising schedule Noising schedule.
    Noising schedule

    diffusion. Yeah, take a look at this. This is a Yeah, take a look at this. This
    is a

    noising schedule, right? I have a dog noising schedule, right? I have a dog noising
    schedule, right? I have a dog

    image on the left. I keep on adding image on the left. I keep on adding image
    on the left. I keep on adding

    noise and then it becomes complete noise and then it becomes complete noise and
    then it becomes complete

    noise. The way it happens in text is can noise. The way it happens in text is
    can noise. The way it happens in text is can

    be represented by be represented by be represented by

    uh this kind of a thing. Yeah. So the uh this kind of a thing. Yeah. So the uh
    this kind of a thing. Yeah. So the

    way it happens in text is that uh at way it happens in text is that uh at'
  concept_slugs:
  - diffusion-language-model
  - masked-diffusion
  - noise-schedule
- idx: 9
  start_sec: 536.08
  end_sec: 580.64
  text: 'way it happens in text is that uh at

    time equal to 1, you almost have an time equal to 1, you almost have an time equal
    to 1, you almost have an

    entire clean text with maybe some mask entire clean text with maybe some mask
    entire clean text with maybe some mask

    over here. But as time increases, over here. But as time increases, over here.
    But as time increases,

    as time becomes two, I have two masks. as time becomes two, I have two masks.
    as time becomes two, I have two masks.

    At time as time becomes three, I have At time as time becomes three, I have At
    time as time becomes three, I have

    three masks. As time increases almost three masks. As time increases almost three
    masks. As time increases almost

    everything becomes masked. So if I watch everything becomes masked. So if I watch
    everything becomes masked. So if I watch

    the full noising you''ll see that you the full noising you''ll see that you the
    full noising you''ll see that you

    start with lower masks and then you start with lower masks and then you start
    with lower masks and then you

    increase the number of masks. That''s increase the number of masks. That''s increase
    the number of masks. That''s

    basically what is meant by a noising basically what is meant by a noising basically
    what is meant by a noising

    schedule. In the case of diffusion LLMs schedule. In the case of diffusion LLMs
    schedule. In the case of diffusion LLMs

    it''s also called as a masking schedule it''s also called as a masking schedule
    it''s also called as a masking schedule

    and the masking schedule is basically and the masking schedule is basically and
    the masking schedule is basically

    proportional to the time. The further proportional to the time. The further proportional
    to the time. The further

    along we are in the noising schedule the along we are in the noising schedule
    the along we are in the noising schedule the

    more masks there will be. Usually there more masks there will be. Usually there
    more masks there will be. Usually there

    is a probability associated with it. So is a probability associated with it. So
    is a probability associated with it. So

    it''s a Bernoli distribution. So the it''s a Bernoli distribution. So the'
  concept_slugs:
  - diffusion-language-model
  - masked-diffusion
  - noise-schedule
- idx: 10
  start_sec: 580.64
  end_sec: 644.24
  text: 'it''s a Bernoli distribution. So the

    probability of masking is way higher. probability of masking is way higher. probability
    of masking is way higher.

    Probability of masking all tokens is way Probability of masking all tokens is
    way Probability of masking all tokens is way

    higher as time is increased. But this higher as time is increased. But this higher
    as time is increased. But this

    animation suffices to understand how animation suffices to understand how animation
    suffices to understand how

    masking works for text. Okay. masking works for text. Okay. masking works for
    text. Okay.

    Um Um Um

    yeah. So yeah. So yeah. So

    what does it mean by masking essentially what does it mean by masking essentially
    what does it mean by masking essentially

    right? What it essentially means is that right? What it essentially means is that
    right? What it essentially means is that

    we just in our vocabulary. So if we have we just in our vocabulary. So if we have
    we just in our vocabulary. So if we have

    a vocabulary of 100,000 a vocabulary of 100,000 a vocabulary of 100,000

    100,000 100,000 100,000

    and the vocabulary is uh the boy etc. We and the vocabulary is uh the boy etc.
    We and the vocabulary is uh the boy etc. We

    add one more token to this vocabulary add one more token to this vocabulary add
    one more token to this vocabulary

    that''s the mask token right. So now that''s the mask token right. So now that''s
    the mask token right. So now

    wherever there is a mask so here we have wherever there is a mask so here we have
    wherever there is a mask so here we have

    a mask right or here there is a mask and a mask right or here there is a mask
    and a mask right or here there is a mask and

    here there is a mask here there is a mask here there is a mask

    right or here there is a mask. So the right or here there is a mask. So the right
    or here there is a mask. So the

    original tokens were 1 11 20,000 55 and original tokens were 1 11 20,000 55 and
    original tokens were 1 11 20,000 55 and

    3,000. Right? Now these are masked. So 3,000. Right? Now these are masked. So'
  concept_slugs:
  - diffusion-language-model
  - masked-diffusion
  - noise-schedule
- idx: 11
  start_sec: 644.24
  end_sec: 695.11
  text: '3,000. Right? Now these are masked. So

    this is masked and this is masked. So this is masked and this is masked. So this
    is masked and this is masked. So

    this will be replaced with 1 0 0 0 1 this will be replaced with 1 0 0 0 1 this
    will be replaced with 1 0 0 0 1

    which is the token ID for the mask. And which is the token ID for the mask. And
    which is the token ID for the mask. And

    this will also be replaced with 10 0 01 this will also be replaced with 10 0 01
    this will also be replaced with 10 0 01

    which is the token ID for the mask. And which is the token ID for the mask. And

    then this input sequence will go into then this input sequence will go into then
    this input sequence will go into

    the transformer architecture. Right? the transformer architecture. Right? the
    transformer architecture. Right?

    This input sequence goes into the This input sequence goes into the This input
    sequence goes into the

    transformer architecture transformer architecture transformer architecture

    or when I say transformer architecture or when I say transformer architecture
    or when I say transformer architecture

    actually this is the input sequence actually this is the input sequence actually
    this is the input sequence

    which goes over here which goes through which goes over here which goes through
    which goes over here which goes through

    the input the processor and the output. the input the processor and the output.
    the input the processor and the output.

    So we start with a noisy input with mask So we start with a noisy input with mask
    So we start with a noisy input with mask

    tokens whereas on the left hand side is tokens whereas on the left hand side is
    tokens whereas on the left hand side is

    the ARM. In the ARM we start with the the ARM. In the ARM we start with the the
    ARM. In the ARM we start with the

    entire sequence whereas in the case of entire sequence whereas in the case of
    entire sequence whereas in the case of

    diffusion language models we start with diffusion language models we start with
    diffusion language models we start with

    a noisy input with mask tokens. Okay.'
  concept_slugs:
  - diffusion-language-model
  - masked-diffusion
  - noise-schedule
- idx: 12
  start_sec: 695.11
  end_sec: 743.35
  text: 'a noisy input with mask tokens. Okay. a noisy input with mask tokens. Okay.

    Everything else remains exactly the Everything else remains exactly the Everything
    else remains exactly the

    same. Now we''ll see what are the changes same. Now we''ll see what are the changes
    same. Now we''ll see what are the changes

    when we go through this IPO block. What when we go through this IPO block. What
    when we go through this IPO block. What

    are the changes when we go through the I are the changes when we go through the
    I are the changes when we go through the I

    um um um

    I P and the O block in the next step. I P and the O block in the next step. I
    P and the O block in the next step.

    But the first thing which I wanted all But the first thing which I wanted all
    But the first thing which I wanted all

    of you to understand is how the noising of you to understand is how the noising
    of you to understand is how the noising

    process actually works. So to give a process actually works. So to give a process
    actually works. So to give a

    more concrete feel to it, let''s say if more concrete feel to it, let''s say if
    more concrete feel to it, let''s say if

    we have four time steps, t= 1, t=2, we have four time steps, t= 1, t=2, we have
    four time steps, t= 1, t=2,

    uh here we have t= 3 and here we have t uh here we have t= 3 and here we have
    t uh here we have t= 3 and here we have t

    equal to 4. Right? Initially nothing is equal to 4. Right? Initially nothing is
    equal to 4. Right? Initially nothing is

    masked but as the time increases you''ll masked but as the time increases you''ll
    masked but as the time increases you''ll

    see more and more masks to the input see more and more masks to the input see
    more and more masks to the input

    tokens. Um yeah so the first difference between Um yeah so the first difference
    between

    the ARM architecture and the diffusion the ARM architecture and the diffusion
    the ARM architecture and the diffusion

    architecture if you compare them side by'
  concept_slugs:
  - diffusion-language-model
  - masked-diffusion
  - noise-schedule
- idx: 13
  start_sec: 743.35
  end_sec: 783.839
  text: 'architecture if you compare them side by architecture if you compare them
    side by

    side is the input which goes into this side is the input which goes into this
    side is the input which goes into this

    input block the processor block and the input block the processor block and the
    input block the processor block and the

    output block this input itself is output block this input itself is output block
    this input itself is

    different here we take a bunch of token different here we take a bunch of token
    different here we take a bunch of token

    ids and we add masks right so when the ids and we add masks right so when the
    ids and we add masks right so when the

    forward pass is done first a random time forward pass is done first a random time
    forward pass is done first a random time

    step is chosen based on that time step step is chosen based on that time step
    step is chosen based on that time step

    we decide how much noise is added how do we decide how much noise is added how
    do we decide how much noise is added how do

    we know how much noise to add because we we know how much noise to add because
    we we know how much noise to add because we

    a noise schedule which is defined. So a noise schedule which is defined. So a
    noise schedule which is defined. So

    let''s say if a time step equal to three let''s say if a time step equal to three
    let''s say if a time step equal to three

    is chosen. The time step is chosen is chosen. The time step is chosen is chosen.
    The time step is chosen

    randomly in each forward pass. So here randomly in each forward pass. So here
    randomly in each forward pass. So here

    what happens is that in ARM architecture what happens is that in ARM architecture
    what happens is that in ARM architecture

    I told you that a batch is selected I told you that a batch is selected I told
    you that a batch is selected

    right? batch is selected then we get the right? batch is selected then we get
    the right? batch is selected then we get the

    targets targets'
  concept_slugs:
  - diffusion-language-model
  - masked-diffusion
  - noise-schedule
- idx: 14
  start_sec: 783.839
  end_sec: 831.519
  text: 'targets

    then we sorry we get the predictions then we sorry we get the predictions then
    we sorry we get the predictions

    then we get the loss then we get the loss then we get the loss

    then we update the parameters then we update the parameters then we update the
    parameters

    and then we choose a new batch this and then we choose a new batch this and then
    we choose a new batch this

    process stays the same for the diffusion process stays the same for the diffusion
    process stays the same for the diffusion

    LLM but it''s just that whenever a new LLM but it''s just that whenever a new
    LLM but it''s just that whenever a new

    batch is selected a new time step is batch is selected a new time step is batch
    is selected a new time step is

    also randomly selected also randomly selected also randomly selected

    so if you have sim six time steps a new so if you have sim six time steps a new
    so if you have sim six time steps a new

    time step will be selected from 1 to time step will be selected from 1 to time
    step will be selected from 1 to

    six. So if time step number three is six. So if time step number three is six.
    So if time step number three is

    selected, selected, selected,

    if time step number three is se if time step number three is se if time step number
    three is se

    selected, roughly 50% of the input token selected, roughly 50% of the input token
    selected, roughly 50% of the input token

    sequence will be masked and they''ll be sequence will be masked and they''ll be
    sequence will be masked and they''ll be

    fed into the architecture. The input, fed into the architecture. The input, fed
    into the architecture. The input,

    the processor and the output, the input, the processor and the output, the input,
    the processor and the output, the input,

    the processor and the output. Okay. the processor and the output. Okay. the processor
    and the output. Okay.

    So until now what we have seen is that So until now what we have seen is that
    So until now what we have seen is that

    what is the noising process in the case what is the noising process in the case'
  concept_slugs:
  - diffusion-language-model
  - masked-diffusion
  - noise-schedule
- idx: 15
  start_sec: 831.519
  end_sec: 858.16
  text: 'what is the noising process in the case

    of diffusion language models. The next of diffusion language models. The next
    of diffusion language models. The next

    step which we are going to see is that step which we are going to see is that
    step which we are going to see is that

    how do we predict the noise. So in the how do we predict the noise. So in the
    how do we predict the noise. So in the

    case of uh images the noise is predicted case of uh images the noise is predicted
    case of uh images the noise is predicted

    by unit. But let''s see in the case of by unit. But let''s see in the case of
    by unit. But let''s see in the case of

    diffusion language models how do we diffusion language models how do we diffusion
    language models how do we

    predict the noise? What kind of a model predict the noise? What kind of a model
    predict the noise? What kind of a model

    do we need to predict the noise? Um and do we need to predict the noise? Um and
    do we need to predict the noise? Um and

    the answer is much simpler than you the answer is much simpler than you the answer
    is much simpler than you

    think. So, let''s get into that right'
  concept_slugs:
  - diffusion-language-model
  - masked-diffusion
  - noise-schedule
---
# Lecture 12: Diffusion LLM Noising Schedule

See the structured chunks above.
