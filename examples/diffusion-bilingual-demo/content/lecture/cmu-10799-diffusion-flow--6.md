---
course_slug: cmu-10799-diffusion-flow
idx: 6
title: 'CMU 10799 S26: Lecture 7 - Guidance & Controllable Generation - Diffusion
  & Flow Matching'
video_url: https://www.youtube.com/watch?v=lPipzIG6rkc
duration_sec: null
chunks:
- idx: 0
  start_sec: 3.909
  end_sec: 52.869
  text: 'All right. So let''s start get started All right. So let''s start get started

    for the lecture. for the lecture. for the lecture.

    Last time we learned DDIM which is like Last time we learned DDIM which is like
    Last time we learned DDIM which is like

    a fast sampling method. And how we do it a fast sampling method. And how we do
    it a fast sampling method. And how we do it

    is that basically we first uh from any is that basically we first uh from any
    is that basically we first uh from any

    uh uh uh

    noisy time step. We get a uh predicted noisy time step. We get a uh predicted
    noisy time step. We get a uh predicted

    clean image or clean image estimation clean image or clean image estimation clean
    image or clean image estimation

    from that time step. And uh instead of from that time step. And uh instead of
    from that time step. And uh instead of

    um basically going back to t minus one, um basically going back to t minus one,
    um basically going back to t minus one,

    we go back to t minus uh t minus 10 we go back to t minus uh t minus 10 we go
    back to t minus uh t minus 10

    instead so that we can skip uh steps and instead so that we can skip uh steps
    and instead so that we can skip uh steps and

    everything. Okay, so this is like very everything. Okay, so this is like very
    everything. Okay, so this is like very

    nice now, right? And then u this way we nice now, right? And then u this way we
    nice now, right? And then u this way we

    can have like 10x speed up and stuff. Uh can have like 10x speed up and stuff.
    Uh can have like 10x speed up and stuff. Uh

    and we also talk about a bunch of and we also talk about a bunch of and we also
    talk about a bunch of

    different solvers because now we can different solvers because now we can different
    solvers because now we can

    formulate everything into a OD. Uh so formulate everything into a OD. Uh so formulate
    everything into a OD. Uh so

    these things can also speed things up or'
  concept_slugs:
  - classifier-free-guidance
  - classifier-guidance
  - ddim
- idx: 1
  start_sec: 52.869
  end_sec: 107.119
  text: 'these things can also speed things up or these things can also speed things
    up or

    get better results. Now we go like uh time z Now we go like uh time z

    like t minus or time t to tus 10 like t minus or time t to tus 10 like t minus
    or time t to tus 10

    z but do we ever like go the opposite z but do we ever like go the opposite z
    but do we ever like go the opposite

    way? Uh can we do this like somewhat way? Uh can we do this like somewhat way?
    Uh can we do this like somewhat

    sarcastically? sarcastically? sarcastically?

    >> Yeah, we''re going to talk about it >> Yeah, we''re going to talk about it
    >> Yeah, we''re going to talk about it

    today. today. today.

    >> Okay. >> Okay. >> Okay.

    >> Yes, we could. And we''re going to talk >> Yes, we could. And we''re going
    to talk >> Yes, we could. And we''re going to talk

    about it today. Um yeah and uh we also about it today. Um yeah and uh we also
    about it today. Um yeah and uh we also

    um uh we also talked about a lot of um uh we also talked about a lot of um uh
    we also talked about a lot of

    solvers which uh all of them can either solvers which uh all of them can either
    solvers which uh all of them can either

    speed up your process or um just give speed up your process or um just give speed
    up your process or um just give

    you better results and uh we also talk you better results and uh we also talk
    you better results and uh we also talk

    about the design space of diffusion about the design space of diffusion about
    the design space of diffusion

    model. So now you can potentially uh model. So now you can potentially uh model.
    So now you can potentially uh

    design a better diffusion model for your design a better diffusion model for your
    design a better diffusion model for your

    homework three and four uh especially um homework three and four uh especially
    um homework three and four uh especially um

    and uh one thing about this design space and uh one thing about this design space'
  concept_slugs:
  - classifier-free-guidance
  - classifier-guidance
- idx: 2
  start_sec: 107.119
  end_sec: 152.8
  text: 'and uh one thing about this design space

    things is that I misspoke um last time things is that I misspoke um last time
    things is that I misspoke um last time

    about about about

    essentially basically why do we choose essentially basically why do we choose
    essentially basically why do we choose

    to focus more on uh the medium uh time to focus more on uh the medium uh time
    to focus more on uh the medium uh time

    steps uh like so basically the EDM paper steps uh like so basically the EDM paper
    steps uh like so basically the EDM paper

    didn''t really say that it''s because didn''t really say that it''s because didn''t
    really say that it''s because

    they''re more difficult it''s more because they''re more difficult it''s more
    because they''re more difficult it''s more because

    that those medium time steps actually that those medium time steps actually that
    those medium time steps actually

    correspond to more semantically correspond to more semantically correspond to
    more semantically

    meaningful or like structurally meaningful or like structurally meaningful or
    like structurally

    meaningful um like information. So and meaningful um like information. So and
    meaningful um like information. So and

    also this is the part where you can also this is the part where you can also this
    is the part where you can

    actually make the most dent in uh the actually make the most dent in uh the actually
    make the most dent in uh the

    quality of the network which means that quality of the network which means that
    quality of the network which means that

    like you can actually make the most like you can actually make the most like you
    can actually make the most

    progress in terms of the your loss. Um progress in terms of the your loss. Um
    progress in terms of the your loss. Um

    so this is why um we so this is why they so this is why um we so this is why they
    so this is why um we so this is why they

    focus a lot more on the inter in the focus a lot more on the inter in the focus
    a lot more on the inter in the

    medium time steps rather than at the medium time steps rather than at the'
  concept_slugs:
  - classifier-free-guidance
  - classifier-guidance
- idx: 3
  start_sec: 152.8
  end_sec: 215.44
  text: 'medium time steps rather than at the

    beginning or at the end. Any questions beginning or at the end. Any questions
    beginning or at the end. Any questions

    here? Okay, cool. All right, so now that we Okay, cool. All right, so now that
    we

    have seen a lot of different knobs that have seen a lot of different knobs that
    have seen a lot of different knobs that

    we can tune, right, for diffusion we can tune, right, for diffusion we can tune,
    right, for diffusion

    models, are they perfect? Now, do we models, are they perfect? Now, do we models,
    are they perfect? Now, do we

    already find like the perfect gender already find like the perfect gender already
    find like the perfect gender

    models? Now, what do we think? What are models? Now, what do we think? What are
    models? Now, what do we think? What are

    we missing here? You said attention. Why do you want You said attention. Why do
    you want

    attention? attention? attention?

    Uh I think >> why >> why

    everyone is switching. everyone is switching. everyone is switching.

    >> So if everyone''s doing it then it means >> So if everyone''s doing it then
    it means >> So if everyone''s doing it then it means

    it''s better. All right. Um uh we there it''s better. All right. Um uh we there
    it''s better. All right. Um uh we there

    are a lot of people switching to it but are a lot of people switching to it but
    are a lot of people switching to it but

    it''s it''s not necessary because it''s it''s it''s not necessary because it''s
    it''s it''s not necessary because it''s

    like you know mathematically better more like you know mathematically better more
    like you know mathematically better more

    or less it''s like but it has a lot of or less it''s like but it has a lot of
    or less it''s like but it has a lot of

    benefit to it and that''s why everyone''s benefit to it and that''s why everyone''s
    benefit to it and that''s why everyone''s

    doing it. doing it. doing it.

    conditional generation. conditional generation. conditional generation.

    >> Conditional generation, right? So, right >> Conditional generation, right?
    So, right >> Conditional generation, right? So, right

    now we haven''t talked about anything now we haven''t talked about anything'
  concept_slugs:
  - classifier-free-guidance
  - classifier-guidance
- idx: 4
  start_sec: 215.44
  end_sec: 274.08
  text: 'now we haven''t talked about anything

    about conditional generation yet. So about conditional generation yet. So about
    conditional generation yet. So

    far, everything is unconditional. We far, everything is unconditional. We far,
    everything is unconditional. We

    actually don''t know how to do actually don''t know how to do actually don''t
    know how to do

    conditional generation yet. So, what conditional generation yet. So, what conditional
    generation yet. So, what

    would you do? Uh conditional generation would you do? Uh conditional generation
    would you do? Uh conditional generation

    just like just the mo simplest way. How just like just the mo simplest way. How
    just like just the mo simplest way. How

    would you formulate um conditional would you formulate um conditional would you
    formulate um conditional

    generations just in general? Yeah. Okay, good, good, good, good answer. Okay,
    good, good, good, good answer.

    >> So >> So >> So

    the attributes CSV thing has like 40 the attributes CSV thing has like 40 the
    attributes CSV thing has like 40

    binary things. You theoretically I would binary things. You theoretically I would
    binary things. You theoretically I would

    just pick whichever ones I wanted it to just pick whichever ones I wanted it to
    just pick whichever ones I wanted it to

    go and send that go and send that go and send that

    >> and send it into >> and send it into >> and send it into

    >> Okay. Yeah. So both of you like are >> Okay. Yeah. So both of you like are
    >> Okay. Yeah. So both of you like are

    correct the answer. So essentially right correct the answer. So essentially right
    correct the answer. So essentially right

    now what we''re doing is that like we uh now what we''re doing is that like we
    uh now what we''re doing is that like we uh

    randomly sample some noise and then we randomly sample some noise and then we
    randomly sample some noise and then we

    uh go the noise going to some uh go the noise going to some uh go the noise going
    to some

    unconditional generative models and then unconditional generative models and then
    unconditional generative models and then

    we get a unconditional sample and we get a unconditional sample and we get a unconditional
    sample and

    usually what people would do like the usually what people would do like the'
  concept_slugs:
  - classifier-free-guidance
  - classifier-guidance
- idx: 5
  start_sec: 274.08
  end_sec: 317.68
  text: 'usually what people would do like the

    first thing you would try uh is to first thing you would try uh is to first thing
    you would try uh is to

    basically you still have your noise that basically you still have your noise that
    basically you still have your noise that

    you sample from the easy to sample you sample from the easy to sample you sample
    from the easy to sample

    distribution like Gausian and then distribution like Gausian and then distribution
    like Gausian and then

    you''ll have like some labels or like you''ll have like some labels or like you''ll
    have like some labels or like

    some conditions that you uh that you some conditions that you uh that you some
    conditions that you uh that you

    want to condition the model or the want to condition the model or the want to
    condition the model or the

    samples on. So it can be a text samples on. So it can be a text samples on. So
    it can be a text

    description or it can be like the description or it can be like the description
    or it can be like the

    attribute labels or it could be like attribute labels or it could be like attribute
    labels or it could be like

    another image or something like that. another image or something like that. another
    image or something like that.

    Right? So just any condition that we Right? So just any condition that we Right?
    So just any condition that we

    want to apply and then you will train a want to apply and then you will train
    a want to apply and then you will train a

    conditional generated model. Uh so conditional generated model. Uh so conditional
    generated model. Uh so

    basically now your sample is conditioned basically now your sample is conditioned
    basically now your sample is conditioned

    on whatever the actual input that you on whatever the actual input that you on
    whatever the actual input that you

    give to the model. um and then you''ll give to the model. um and then you''ll
    give to the model. um and then you''ll

    get another and then you get a get another and then you get a get another and
    then you get a

    conditional um sample based on whatever conditional um sample based on whatever'
  concept_slugs:
  - classifier-free-guidance
  - classifier-guidance
- idx: 6
  start_sec: 317.68
  end_sec: 376.16
  text: 'conditional um sample based on whatever

    the condition that you specified right the condition that you specified right
    the condition that you specified right

    okay so what what is the what is the okay so what what is the what is the okay
    so what what is the what is the

    major like bottleneck or what is the major like bottleneck or what is the major
    like bottleneck or what is the

    major problem with this kind of major problem with this kind of major problem
    with this kind of

    formulation oh okay there''s a I would also I would oh okay there''s a I would
    also I would

    add another feature is extractor add another feature is extractor add another
    feature is extractor

    alongside the pixel input pixel values. Not sure what that we''re not not sure
    Not sure what that we''re not not sure

    exactly what that means. Do you want to exactly what that means. Do you want to
    exactly what that means. Do you want to

    speak up and uh just uh just like you speak up and uh just uh just like you speak
    up and uh just uh just like you

    you you can unmute yourself and maybe we you you can unmute yourself and maybe
    we you you can unmute yourself and maybe we

    can hear you. Actually, I''m not sure if can hear you. Actually, I''m not sure
    if can hear you. Actually, I''m not sure if

    we can hear you. we can hear you. we can hear you.

    >> It it was for the previous question. I I >> It it was for the previous question.
    I I >> It it was for the previous question. I I

    said I would add another feature vector said I would add another feature vector
    said I would add another feature vector

    like text example that you''ve shown like text example that you''ve shown like
    text example that you''ve shown

    alongside the input the training images. alongside the input the training images.
    alongside the input the training images.

    Ah that that that makes sense. So Ah that that that makes sense. So Ah that that
    that makes sense. So

    basically it''s like when you try to uh basically it''s like when you try to uh
    basically it''s like when you try to uh

    essentially have another feature from essentially have another feature from'
  concept_slugs:
  - classifier-free-guidance
  - classifier-guidance
- idx: 7
  start_sec: 376.16
  end_sec: 420.55
  text: 'essentially have another feature from

    for example maybe another image or like for example maybe another image or like
    for example maybe another image or like

    some uh maybe another like 3D mesh or some uh maybe another like 3D mesh or some
    uh maybe another like 3D mesh or

    something like that. Right. So basically something like that. Right. So basically
    something like that. Right. So basically

    just like whatever it is you will first just like whatever it is you will first
    just like whatever it is you will first

    encode it into another uh feature like encode it into another uh feature like
    encode it into another uh feature like

    vector and then input it into the model. vector and then input it into the model.
    vector and then input it into the model.

    Is that what you mean? Okay. Is that what you mean? Okay. Is that what you mean?
    Okay.

    >> Yes. Yes. Yes. >> Yes. Yes. Yes. >> Yes. Yes. Yes.

    >> Yeah. Yeah. That''s that''s also per like >> Yeah. Yeah. That''s that''s also
    per like >> Yeah. Yeah. That''s that''s also per like

    this is a perfect answer for sure. Uh this is a perfect answer for sure. Uh this
    is a perfect answer for sure. Uh

    but okay. So what what what do you guys but okay. So what what what do you guys
    but okay. So what what what do you guys

    think is like the major bottleneck for think is like the major bottleneck for
    think is like the major bottleneck for

    this kind of um formulation? this kind of um formulation? this kind of um formulation?

    Okay, a lot of people let''s Okay, a lot of people let''s Okay, a lot of people
    let''s

    uh everyone get to answer uh everyone get to answer uh everyone get to answer

    >> expressing text in form of some latent >> expressing text in form of some latent
    >> expressing text in form of some latent

    space. space. space.

    >> Uh why why is that a bottleneck? >> Uh why why is that a bottleneck? >> Uh
    why why is that a bottleneck?

    >> How would we basically turn it into a >> How would we basically turn it into
    a >> How would we basically turn it into a

    norm like we want dark hair or some'
  concept_slugs:
  - classifier-free-guidance
  - classifier-guidance
- idx: 8
  start_sec: 420.55
  end_sec: 473.919
  text: 'norm like we want dark hair or some norm like we want dark hair or some

    different hair? different hair? different hair?

    Um, so you mean like basically how would Um, so you mean like basically how would
    Um, so you mean like basically how would

    you embed the text? Is that like you embed the text? Is that like you embed the
    text? Is that like

    basically like this is the part of of basically like this is the part of of basically
    like this is the part of of

    the bottleneck? Is that what you mean or the bottleneck? Is that what you mean
    or the bottleneck? Is that what you mean or

    Okay. Um, we will talk about it next Okay. Um, we will talk about it next Okay.
    Um, we will talk about it next

    week. But also good answer. All right. week. But also good answer. All right.
    week. But also good answer. All right.

    Let''s see. Okay. Let''s see. Okay. Let''s see. Okay.

    >> Super. >> Super. >> Super.

    Okay. Where does the label come from? Okay. Where does the label come from? Okay.
    Where does the label come from?

    Right. Basically, okay. a lot more training and training data a lot more training
    and training data

    for each condition. for each condition. for each condition.

    >> You need you need different training for >> You need you need different training
    for >> You need you need different training for

    different conditions, right? Okay, different conditions, right? Okay, different
    conditions, right? Okay,

    perfect answer. perfect answer. perfect answer.

    Like basically for each type of Like basically for each type of Like basically
    for each type of

    condition, we will have to train a new condition, we will have to train a new
    condition, we will have to train a new

    model on it, right? So for example, say model on it, right? So for example, say
    model on it, right? So for example, say

    if this model is text conditioned, then if this model is text conditioned, then
    if this model is text conditioned, then

    we cannot use it to to do like class we cannot use it to to do like class we cannot
    use it to to do like class

    label condition, right? If if this model label condition, right? If if this model'
  concept_slugs:
  - classifier-free-guidance
  - classifier-guidance
- idx: 9
  start_sec: 473.919
  end_sec: 525.03
  text: 'label condition, right? If if this model

    is class label condition then we cannot is class label condition then we cannot
    is class label condition then we cannot

    use it for like say condition on like use it for like say condition on like use
    it for like say condition on like

    the depth map or something like that. If the depth map or something like that.
    If the depth map or something like that. If

    it''s like conditioned on another image it''s like conditioned on another image
    it''s like conditioned on another image

    then we cannot use it uh for uh I don''t then we cannot use it uh for uh I don''t
    then we cannot use it uh for uh I don''t

    know like text condition generation know like text condition generation know like
    text condition generation

    right >> sure but like can you like like you >> sure but like can you like like
    you

    can''t just like condition on everything can''t just like condition on everything
    can''t just like condition on everything

    you can think of right that''s the you can think of right that''s the you can
    think of right that''s the

    problem and also even if you could problem and also even if you could problem
    and also even if you could

    formulate your uh model to condition on formulate your uh model to condition on
    formulate your uh model to condition on

    everything that you can think of you everything that you can think of you everything
    that you can think of you

    also need to collect data for everything also need to collect data for everything
    also need to collect data for everything

    Right. That''s really really expensive. Right. That''s really really expensive.
    Right. That''s really really expensive.

    Yeah. Yeah. Yeah.

    >> Like like for example, >> Like like for example, >> Like like for example,

    >> yeah, you could. But even if you want to >> yeah, you could. But even if you
    want to >> yeah, you could. But even if you want to

    do that, you still need to like collect do that, you still need to like collect
    do that, you still need to like collect

    data for everything, right? So sometimes data for everything, right? So sometimes
    data for everything, right? So sometimes

    like the data collection as we uh may'
  concept_slugs:
  - classifier-free-guidance
  - classifier-guidance
- idx: 10
  start_sec: 525.03
  end_sec: 567.6
  text: 'like the data collection as we uh may like the data collection as we uh may

    know now is like very very expensive know now is like very very expensive know
    now is like very very expensive

    thing. And this is why like you know thing. And this is why like you know thing.
    And this is why like you know

    Alexander Wong got you know there his Alexander Wong got you know there his Alexander
    Wong got you know there his

    million dollar job now you know just million dollar job now you know just million
    dollar job now you know just

    collecting data is important apparently. collecting data is important apparently.
    collecting data is important apparently.

    Um Um Um

    Can you use a single model to do all of Can you use a single model to do all of
    Can you use a single model to do all of

    that? Can you embed all of that in? that? Can you embed all of that in? that?
    Can you embed all of that in?

    >> Can you embed all of that into it? So, >> Can you embed all of that into it?
    So, >> Can you embed all of that into it? So,

    um this is basically saying that can we um this is basically saying that can we
    um this is basically saying that can we

    do omni models, right? This is what do omni models, right? This is what do omni
    models, right? This is what

    you''re asking. Um well, the answer is you''re asking. Um well, the answer is
    you''re asking. Um well, the answer is

    this is what people are trying to do. Uh this is what people are trying to do.
    Uh this is what people are trying to do. Uh

    but actually but actually but actually

    we we can have another option here. Um we we can have another option here. Um
    we we can have another option here. Um

    and this is why this is like the the and this is why this is like the the and
    this is why this is like the the

    best thing that I like about diffusion. best thing that I like about diffusion.
    best thing that I like about diffusion.

    um which is that basically if you think um which is that basically if you think'
  concept_slugs:
  - classifier-free-guidance
  - classifier-guidance
- idx: 11
  start_sec: 567.6
  end_sec: 617.829
  text: 'um which is that basically if you think

    about it right the unconditional model about it right the unconditional model
    about it right the unconditional model

    that we learned already has a lot of that we learned already has a lot of that
    we learned already has a lot of

    good information about like how to good information about like how to good information
    about like how to

    generate a an a realistic looking image generate a an a realistic looking image
    generate a an a realistic looking image

    right so for example like if you''re right so for example like if you''re right
    so for example like if you''re

    trying to model human faces then an trying to model human faces then an trying
    to model human faces then an

    unconditional model already know how to unconditional model already know how to
    unconditional model already know how to

    generate a human face you just need to generate a human face you just need to
    generate a human face you just need to

    know how to control it better so why know how to control it better so why know
    how to control it better so why

    can''t you just like reuse some of the can''t you just like reuse some of the
    can''t you just like reuse some of the

    knowledge um in the unconditional model knowledge um in the unconditional model
    knowledge um in the unconditional model

    to to to

    better control it into a conditional better control it into a conditional better
    control it into a conditional

    model. Right? So, is it possible for us model. Right? So, is it possible for us
    model. Right? So, is it possible for us

    to reuse the unconditional model at all? to reuse the unconditional model at all?
    to reuse the unconditional model at all?

    Is the number one question that we''re Is the number one question that we''re
    Is the number one question that we''re

    going to answer today. Okay? So, how do going to answer today. Okay? So, how do
    going to answer today. Okay? So, how do

    we do that? we do that? we do that?

    What do we think? What do we think? What do we think?

    Is it possible to to reuse the Is it possible to to reuse the Is it possible to
    to reuse the

    unconditional model to do conditional'
  concept_slugs:
  - classifier-free-guidance
  - classifier-guidance
- idx: 12
  start_sec: 617.829
  end_sec: 677.2
  text: 'unconditional model to do conditional unconditional model to do conditional

    generation at all? sort of. But there''s like a very very sort of. But there''s
    like a very very

    simple answer to this. Okay, I''ll give simple answer to this. Okay, I''ll give
    simple answer to this. Okay, I''ll give

    you guys a hint. Remember how there are you guys a hint. Remember how there are
    you guys a hint. Remember how there are

    two two dudes that we really need to two two dudes that we really need to two
    two dudes that we really need to

    remember from this class? One guy is remember from this class? One guy is remember
    from this class? One guy is

    Gausian. What''s the other guy? Gausian. What''s the other guy? Gausian. What''s
    the other guy?

    >> Bes, right? Yes. Remember the number one >> Bes, right? Yes. Remember the number
    one >> Bes, right? Yes. Remember the number one

    rule in probability theory. So saying rule in probability theory. So saying rule
    in probability theory. So saying

    that you should tattoo uh is that you should tattoo uh is that you should tattoo
    uh is

    uh be theorem, right? So basically we uh be theorem, right? So basically we uh
    be theorem, right? So basically we

    know that diffusion model is basically know that diffusion model is basically
    know that diffusion model is basically

    just modeling the score function which just modeling the score function which
    just modeling the score function which

    is basically just the the gradient of is basically just the the gradient of is
    basically just the the gradient of

    the log probability right by bay theorem the log probability right by bay theorem
    the log probability right by bay theorem

    then we know that if we''re like if we''re then we know that if we''re like if
    we''re then we know that if we''re like if we''re

    trying to the the conditional trying to the the conditional trying to the the
    conditional

    probability can also be written as a probability can also be written as a probability
    can also be written as a

    combination of the unconditional combination of the unconditional combination
    of the unconditional

    probability times the conditional probability times the conditional probability
    times the conditional

    probability of the label given the model probability of the label given the model'
  concept_slugs:
  - classifier-free-guidance
  - classifier-guidance
- idx: 13
  start_sec: 677.2
  end_sec: 728.959
  text: 'probability of the label given the model

    or the the image. Right? So if you write or the the image. Right? So if you write
    or the the image. Right? So if you write

    it in terms of if you write it in terms it in terms of if you write it in terms
    it in terms of if you write it in terms

    of the the score uh then it basically of the the score uh then it basically of
    the the score uh then it basically

    just break it down into the just break it down into the just break it down into
    the

    unconditional score which is given by unconditional score which is given by unconditional
    score which is given by

    the pre-trained unconditional diffusion the pre-trained unconditional diffusion
    the pre-trained unconditional diffusion

    model and this thing is actually a model and this thing is actually a model and
    this thing is actually a

    discriminative model right so it''s the discriminative model right so it''s the
    discriminative model right so it''s the

    probability of the label given the input probability of the label given the input
    probability of the label given the input

    image so that that could be so if you image so that that could be so if you image
    so that that could be so if you

    your condition is a class label then your condition is a class label then your
    condition is a class label then

    it''s a classifier right if the condition it''s a classifier right if the condition
    it''s a classifier right if the condition

    is the image caption then it could be a is the image caption then it could be
    a is the image caption then it could be a

    clip model stuff like that. Right? So clip model stuff like that. Right? So clip
    model stuff like that. Right? So

    basically you can now break the basically you can now break the basically you
    can now break the

    conditional generation score into an conditional generation score into an conditional
    generation score into an

    unconditional score which we can already unconditional score which we can already
    unconditional score which we can already

    you know obtain by pre-training you know obtain by pre-training you know obtain
    by pre-training

    unconditional model unconditional model unconditional model

    plus a uh the gradient from a plus a uh the gradient from a'
  concept_slugs:
  - classifier-free-guidance
  - classifier-guidance
- idx: 14
  start_sec: 728.959
  end_sec: 780.15
  text: 'plus a uh the gradient from a

    discriminative model. Yeah, discriminative model. Yeah, discriminative model.
    Yeah,

    >> here influence like both the model >> here influence like both the model >>
    here influence like both the model

    parameters and the the discriminator. parameters and the the discriminator. parameters
    and the the discriminator.

    >> Uh that''s a great question. I''m I''m >> Uh that''s a great question. I''m
    I''m >> Uh that''s a great question. I''m I''m

    going to keep talking about it and then going to keep talking about it and then
    going to keep talking about it and then

    and and then like but basically um yeah and and then like but basically um yeah
    and and then like but basically um yeah

    that that it''ll get answered. It''ll get that that it''ll get answered. It''ll
    get that that it''ll get answered. It''ll get

    answered but um just imagine they''re answered but um just imagine they''re answered
    but um just imagine they''re

    both encapsulated in one big model for both encapsulated in one big model for
    both encapsulated in one big model for

    now. Okay. All right. Um so this is now. Okay. All right. Um so this is now. Okay.
    All right. Um so this is

    basically what we call classifier basically what we call classifier basically
    what we call classifier

    guidance diffusion. This is like one of guidance diffusion. This is like one of
    guidance diffusion. This is like one of

    the first um like papers that does uh the first um like papers that does uh the
    first um like papers that does uh

    guidance in diffusion. So basically this guidance in diffusion. So basically this
    guidance in diffusion. So basically this

    is like our OG uh score functions, is like our OG uh score functions, is like
    our OG uh score functions,

    right? All you need to do to do right? All you need to do to do right? All you
    need to do to do

    classifier guidance is literally just classifier guidance is literally just classifier
    guidance is literally just

    replace this unconditional score with replace this unconditional score with replace
    this unconditional score with

    the conditional score that we just the conditional score that we just the conditional
    score that we just

    derived by Basu. derived by Basu. derived by Basu.

    That''s it. And you just run your'
  concept_slugs:
  - classifier-free-guidance
  - classifier-guidance
- idx: 15
  start_sec: 780.15
  end_sec: 839.269
  text: 'That''s it. And you just run your That''s it. And you just run your

    sampling as normal and you get a sampling as normal and you get a sampling as
    normal and you get a

    conditional sample. conditional sample. conditional sample.

    So uh in uh basically to compare with So uh in uh basically to compare with So
    uh in uh basically to compare with

    the paradigm that we just that we that the paradigm that we just that we that
    the paradigm that we just that we that

    we had before uh classifier guidance we had before uh classifier guidance we had
    before uh classifier guidance

    diffusion is basically now you have you diffusion is basically now you have you
    diffusion is basically now you have you

    still you still have a noisy image input still you still have a noisy image input
    still you still have a noisy image input

    and then you have your label or like and then you have your label or like and
    then you have your label or like

    your condition or your uh caption and your condition or your uh caption and your
    condition or your uh caption and

    then basically the label sorry the uh then basically the label sorry the uh then
    basically the label sorry the uh

    noisy image will get inputed into the noisy image will get inputed into the noisy
    image will get inputed into the

    unconditional diffusion model uh and as unconditional diffusion model uh and as
    unconditional diffusion model uh and as

    well as the classifier. Uh and then the well as the classifier. Uh and then the
    well as the classifier. Uh and then the

    your your label or your conditions also your your label or your conditions also
    your your label or your conditions also

    get put into the classifier and then get put into the classifier and then get
    put into the classifier and then

    basically the they just uh produce the basically the they just uh produce the
    basically the they just uh produce the

    score and the gradient from the score and the gradient from the score and the
    gradient from the

    classifier and then you''ll get a guided classifier and then you''ll get a guided
    classifier and then you''ll get a guided

    or conditional sample. or conditional sample. or conditional sample.

    All right, any qu yes,'
  concept_slugs:
  - classifier-free-guidance
  - classifier-guidance
- idx: 16
  start_sec: 842.31
  end_sec: 886.88
  text: '>> it''s a classifier. So it''s either like >> it''s a classifier. So it''s
    either like

    it can be anything. So depending on your it can be anything. So depending on your
    it can be anything. So depending on your

    label if your lab if the condition if label if your lab if the condition if label
    if your lab if the condition if

    the condition is a class label then it''s the condition is a class label then
    it''s the condition is a class label then it''s

    literally just like a any classifier. So literally just like a any classifier.
    So literally just like a any classifier. So

    anything that you will train for say anything that you will train for say anything
    that you will train for say

    image net. Um if you if you''re if if the image net. Um if you if you''re if if
    the image net. Um if you if you''re if if the

    the condition is like text then it could the condition is like text then it could
    the condition is like text then it could

    be a clip model and then you just output be a clip model and then you just output
    be a clip model and then you just output

    your clip score and stuff like that. your clip score and stuff like that. your
    clip score and stuff like that.

    How do you calculate? Uh How do you calculate? Uh How do you calculate? Uh

    >> usually back prop right through the >> usually back prop right through the
    >> usually back prop right through the

    model but you take the gradient with model but you take the gradient with model
    but you take the gradient with

    respect to the image instead of the respect to the image instead of the respect
    to the image instead of the

    parameter and then you get a gradient parameter and then you get a gradient parameter
    and then you get a gradient

    right. Yeah. right. Yeah. right. Yeah.

    >> Yeah. >> Yeah. >> Yeah.

    >> I guess that only works for those >> I guess that only works for those >> I
    guess that only works for those

    conditionals actually occurs in your conditionals actually occurs in your conditionals
    actually occurs in your

    training data. You cannot do some training data. You cannot do some'
  concept_slugs:
  - classifier-free-guidance
  - classifier-guidance
- idx: 17
  start_sec: 886.88
  end_sec: 929.839
  text: 'training data. You cannot do some

    interpolation to generate some other interpolation to generate some other interpolation
    to generate some other

    thing. thing. thing.

    >> Um yes uh that is a very great question. >> Um yes uh that is a very great
    question. >> Um yes uh that is a very great question.

    Um actually I''ll uh I''ll continue going Um actually I''ll uh I''ll continue
    going Um actually I''ll uh I''ll continue going

    and then it''ll get answered. Yeah. and then it''ll get answered. Yeah. and then
    it''ll get answered. Yeah.

    >> Like does the classifier need to take >> Like does the classifier need to take
    >> Like does the classifier need to take

    the type set as input because it looks the type set as input because it looks
    the type set as input because it looks

    >> very very good. Very very good. Yeah. >> very very good. Very very good. Yeah.
    >> very very good. Very very good. Yeah.

    You''re you''re jumping ahead a little bit You''re you''re jumping ahead a little
    bit You''re you''re jumping ahead a little bit

    but let''s let''s look at some examples but let''s let''s look at some examples
    but let''s let''s look at some examples

    now. First uh so basically this is like now. First uh so basically this is like
    now. First uh so basically this is like

    a a classifier guidance or uh what we a a classifier guidance or uh what we a
    a classifier guidance or uh what we

    call conditional score. So basically call conditional score. So basically call
    conditional score. So basically

    they just train an unconditional score they just train an unconditional score
    they just train an unconditional score

    function uh score model and then just function uh score model and then just function
    uh score model and then just

    apply exactly that thing and then you apply exactly that thing and then you apply
    exactly that thing and then you

    can get class uh this is a class can get class uh this is a class can get class
    uh this is a class

    conditioned uh cfar and then this is conditioned uh cfar and then this is conditioned
    uh cfar and then this is

    like in painting and this is like like in painting and this is like'
  concept_slugs:
  - classifier-free-guidance
  - classifier-guidance
- idx: 18
  start_sec: 929.839
  end_sec: 982.079
  text: 'like in painting and this is like

    colorization. Yeah. So you can just like colorization. Yeah. So you can just like
    colorization. Yeah. So you can just like

    use the same unconditional model to to use the same unconditional model to to
    use the same unconditional model to to

    perform a lot of conditional generation perform a lot of conditional generation
    perform a lot of conditional generation

    tasks now. Okay. But yes, like you tasks now. Okay. But yes, like you tasks now.
    Okay. But yes, like you

    mentioned, right, mentioned, right, mentioned, right,

    this thing is problematic, right? this thing is problematic, right? this thing
    is problematic, right?

    Because you you need to be conditioned Because you you need to be conditioned
    Because you you need to be conditioned

    on the the classifier actually need to on the the classifier actually need to
    on the the classifier actually need to

    be able to process noisy image and need be able to process noisy image and need
    be able to process noisy image and need

    to be able to recognize like which noise to be able to recognize like which noise
    to be able to recognize like which noise

    level it''s at. Right? So this thing is level it''s at. Right? So this thing is
    level it''s at. Right? So this thing is

    very problematic. This thing just means very problematic. This thing just means
    very problematic. This thing just means

    that we need to train a noisy classifier that we need to train a noisy classifier
    that we need to train a noisy classifier

    for the classifier guidance diffusion. for the classifier guidance diffusion.
    for the classifier guidance diffusion.

    So like what is happening is that like So like what is happening is that like
    So like what is happening is that like

    you cannot just use offtheshelf you cannot just use offtheshelf you cannot just
    use offtheshelf

    classifier anymore. So you cannot just classifier anymore. So you cannot just
    classifier anymore. So you cannot just

    like pull a pre-trained classifier from like pull a pre-trained classifier from
    like pull a pre-trained classifier from

    like GitHub or something like that. You like GitHub or something like that. You
    like GitHub or something like that. You

    need to actually specifically train this need to actually specifically train this'
  concept_slugs:
  - classifier-free-guidance
  - classifier-guidance
- idx: 19
  start_sec: 982.079
  end_sec: 1033.11
  text: 'need to actually specifically train this

    classifier uh to to be able to recognize classifier uh to to be able to recognize
    classifier uh to to be able to recognize

    a noisy image and and and be able to a noisy image and and and be able to a noisy
    image and and and be able to

    process different noise level. And the process different noise level. And the
    process different noise level. And the

    reasoning is because like just imagine reasoning is because like just imagine
    reasoning is because like just imagine

    that you are just pulling like a regular that you are just pulling like a regular
    that you are just pulling like a regular

    celeb a classifier on the like on online celeb a classifier on the like on online
    celeb a classifier on the like on online

    and uh the input you''re going to get to and uh the input you''re going to get
    to and uh the input you''re going to get to

    that classifier is going to be like this that classifier is going to be like this
    that classifier is going to be like this

    this noisy image right and the the this noisy image right and the the this noisy
    image right and the the

    pre-trained classifier has never seen pre-trained classifier has never seen pre-trained
    classifier has never seen

    those noisy image. So it''s just going to those noisy image. So it''s just going
    to those noisy image. So it''s just going to

    give you like very random answers or give you like very random answers or give
    you like very random answers or

    even like very OD answers right and even like very OD answers right and even like
    very OD answers right and

    they''re just not going to give you good they''re just not going to give you good
    they''re just not going to give you good

    gradient at all. Right? So this is very gradient at all. Right? So this is very
    gradient at all. Right? So this is very

    problematic. problematic. problematic.

    Um, is it possible then to use a Um, is it possible then to use a Um, is it possible
    then to use a

    offtheshelf classifier? offtheshelf classifier? offtheshelf classifier?

    What do we think? What do we think?

    I see some someone I see some someone I see some someone

    nodding their head.'
  concept_slugs:
  - classifier-free-guidance
  - classifier-guidance
- idx: 20
  start_sec: 1033.11
  end_sec: 1090.24
  text: 'nodding their head. nodding their head.

    Oh, someone someone on online. Is that Oh, someone someone on online. Is that
    Oh, someone someone on online. Is that

    >> Oh, no. >> Oh, no. >> Oh, no.

    >> Oh, okay. Sorry. Sorry. Sorry. Sorry. >> Oh, okay. Sorry. Sorry. Sorry. Sorry.
    >> Oh, okay. Sorry. Sorry. Sorry. Sorry.

    Um, Um, Um,

    >> actually, I have an idea. >> actually, I have an idea. >> actually, I have
    an idea.

    >> Possible. Okay, let''s go. Um so I recall that we uh earlier we uh Um so I
    recall that we uh earlier we uh

    showed that we could uh estimate X0 from showed that we could uh estimate X0 from
    showed that we could uh estimate X0 from

    XT. Uh X0 will have a lot less noise XT. Uh X0 will have a lot less noise XT.
    Uh X0 will have a lot less noise

    than XT. Maybe we could feed X0 to the than XT. Maybe we could feed X0 to the
    than XT. Maybe we could feed X0 to the

    classifier. classifier. classifier.

    >> Perfect answer. This is exactly what >> Perfect answer. This is exactly what
    >> Perfect answer. This is exactly what

    we''re going to do actually. Great we''re going to do actually. Great we''re going
    to do actually. Great

    answer. Um so remember how we do DDT answer. Um so remember how we do DDT answer.
    Um so remember how we do DDT

    DDIM, right? And at each time step of DDIM, right? And at each time step of DDIM,
    right? And at each time step of

    DDIN, we can actually have a clean data DDIN, we can actually have a clean data
    DDIN, we can actually have a clean data

    estimation from those from each of the estimation from those from each of the
    estimation from those from each of the

    noisy time steps. Then how about let''s noisy time steps. Then how about let''s
    noisy time steps. Then how about let''s

    use the offtheshelf classifier then. use the offtheshelf classifier then. use
    the offtheshelf classifier then.

    Right? So basically what you do is you Right? So basically what you do is you
    Right? So basically what you do is you

    basically just input your um your the basically just input your um your the'
  concept_slugs:
  - classifier-free-guidance
  - classifier-guidance
  - ddim
- idx: 21
  start_sec: 1090.24
  end_sec: 1142.48
  text: 'basically just input your um your the

    the the less noisy the clean data the the less noisy the clean data the the less
    noisy the clean data

    estimation and the condition that you estimation and the condition that you estimation
    and the condition that you

    have into your off-the-shelf classifier. have into your off-the-shelf classifier.
    have into your off-the-shelf classifier.

    And then this off-the-shelf classifier And then this off-the-shelf classifier
    And then this off-the-shelf classifier

    is going to give you some gradient. And is going to give you some gradient. And
    is going to give you some gradient. And

    then this gradient is going can be used then this gradient is going can be used
    then this gradient is going can be used

    to you know modify the intermediate to you know modify the intermediate to you
    know modify the intermediate

    noisy uh examples in your in your noisy uh examples in your in your noisy uh examples
    in your in your

    trajectory and uh this thing is actually trajectory and uh this thing is actually
    trajectory and uh this thing is actually

    called diffusion posterior sampling. So called diffusion posterior sampling. So
    called diffusion posterior sampling. So

    this is actually a thing. Okay. Um so this is actually a thing. Okay. Um so this
    is actually a thing. Okay. Um so

    how diffusion posterior sampling uh do how diffusion posterior sampling uh do
    how diffusion posterior sampling uh do

    things is literally just you start from things is literally just you start from
    things is literally just you start from

    the total noise and then you just the total noise and then you just the total
    noise and then you just

    similar to DDIM you get a clean data similar to DDIM you get a clean data similar
    to DDIM you get a clean data

    estimation from your time step and then estimation from your time step and then
    estimation from your time step and then

    you um you you go back as normal and you um you you go back as normal and you
    um you you go back as normal and

    then but then you apply your um the then but then you apply your um the then but
    then you apply your um the

    gradient that you got from your clean gradient that you got from your clean'
  concept_slugs:
  - classifier-free-guidance
  - classifier-guidance
  - ddim
- idx: 22
  start_sec: 1142.48
  end_sec: 1227.11
  text: 'gradient that you got from your clean

    data estimation um and your data estimation um and your data estimation um and
    your

    off-the-shelf classifier off-the-shelf classifier off-the-shelf classifier

    uh to modify the intermediate samples uh to modify the intermediate samples uh
    to modify the intermediate samples

    and then you do that for every time step and then you do that for every time step
    and then you do that for every time step

    and then eventually you''re going to be and then eventually you''re going to be
    and then eventually you''re going to be

    able to get a conditional sample. Okay. able to get a conditional sample. Okay.
    able to get a conditional sample. Okay.

    Any question? Seems good. Seems good.

    Seems good for real. H. So, DPS is Seems good for real. H. So, DPS is Seems good
    for real. H. So, DPS is

    amazing. It''s like very smart uh amazing. It''s like very smart uh amazing. It''s
    like very smart uh

    algorithm. Uh but can we spot some algorithm. Uh but can we spot some algorithm.
    Uh but can we spot some

    problems here? What do we think? Um

    I mean I mean I mean

    >> so uh we''re adding the guidance value to >> so uh we''re adding the guidance
    value to >> so uh we''re adding the guidance value to

    xtus one but xt - 1 is not x0 t so it''s xtus one but xt - 1 is not x0 t so it''s
    xtus one but xt - 1 is not x0 t so it''s

    actually a bit different actually a bit different actually a bit different

    >> that''s fine right we''re taking the >> that''s fine right we''re taking the
    >> that''s fine right we''re taking the

    gradient with respect to xt >> what what what is the problem here why >> what
    what what is the problem here why

    why do you want to apply I to X0. why do you want to apply I to X0. why do you
    want to apply I to X0.

    >> Um, well, I''m just saying I''m just, uh, >> Um, well, I''m just saying I''m
    just, uh, >> Um, well, I''m just saying I''m just, uh,

    saying that, uh, we, saying that, uh, we, saying that, uh, we,

    um, um, um,

    so, uh, we we took the grade in regards'
  concept_slugs:
  - classifier-free-guidance
  - classifier-guidance
- idx: 23
  start_sec: 1227.11
  end_sec: 1279.84
  text: 'so, uh, we we took the grade in regards so, uh, we we took the grade in regards

    to XT. Uh, but like that''s not where the to XT. Uh, but like that''s not where
    the to XT. Uh, but like that''s not where the

    point is anymore. point is anymore. point is anymore.

    >> Maybe that''s not a problem. I don''t >> Maybe that''s not a problem. I don''t
    >> Maybe that''s not a problem. I don''t

    know. know. know.

    >> Yeah, actually this is a very good >> Yeah, actually this is a very good >>
    Yeah, actually this is a very good

    answer. And this is actually the the answer. And this is actually the the answer.
    And this is actually the the

    problem, the source of the problem, problem, the source of the problem, problem,
    the source of the problem,

    actually. So the first thing we notice actually. So the first thing we notice
    actually. So the first thing we notice

    is that because we''re modifying the is that because we''re modifying the is that
    because we''re modifying the

    intermediate noisy examples, so we''re intermediate noisy examples, so we''re
    intermediate noisy examples, so we''re

    taking the gradient with respect to XT, taking the gradient with respect to XT,
    taking the gradient with respect to XT,

    right? Then taking the gradient with right? Then taking the gradient with right?
    Then taking the gradient with

    respect to XT is actually requiring you respect to XT is actually requiring you
    respect to XT is actually requiring you

    to back prop through both the classifier to back prop through both the classifier
    to back prop through both the classifier

    and the diffusion model, and the diffusion model, and the diffusion model,

    right? And that is really really really right? And that is really really really
    right? And that is really really really

    expensive because usually the diffusion expensive because usually the diffusion
    expensive because usually the diffusion

    model is quite large even though the model is quite large even though the model
    is quite large even though the

    classifier might be small though your classifier might be small though your classifier
    might be small though your

    back prop through like one mediumsiz back prop through like one mediumsiz back
    prop through like one mediumsiz

    model and one large size model right so model and one large size model right so'
  concept_slugs:
  - classifier-free-guidance
  - classifier-guidance
- idx: 24
  start_sec: 1279.84
  end_sec: 1326.799
  text: 'model and one large size model right so

    this thing is just going to takes you this thing is just going to takes you this
    thing is just going to takes you

    like a lot of compute that''s one thing like a lot of compute that''s one thing
    like a lot of compute that''s one thing

    and then the other thing is um basically and then the other thing is um basically
    and then the other thing is um basically

    um there''s this thing called the um there''s this thing called the um there''s
    this thing called the

    diffusion so basically remember how at diffusion so basically remember how at
    diffusion so basically remember how at

    the uh in like lecture four or something the uh in like lecture four or something
    the uh in like lecture four or something

    we were saying that the data usually we were saying that the data usually we were
    saying that the data usually

    reside on lowdimensional manifolds. reside on lowdimensional manifolds. reside
    on lowdimensional manifolds.

    Right? So basically what''s happening is Right? So basically what''s happening
    is Right? So basically what''s happening is

    that actually each noise layer of the that actually each noise layer of the that
    actually each noise layer of the

    diffu each each noise level of the diffu each each noise level of the diffu each
    each noise level of the

    diffusion also follows or concentrate on diffusion also follows or concentrate
    on diffusion also follows or concentrate on

    certain manifolds and this manifolds certain manifolds and this manifolds certain
    manifolds and this manifolds

    actually basically looks like layered actually basically looks like layered actually
    basically looks like layered

    bubble shells um that''s surrounding and bubble shells um that''s surrounding
    and bubble shells um that''s surrounding and

    the the the the data manifold. So just the the the the data manifold. So just
    the the the the data manifold. So just

    imagine the data man met man met man met man met man met man met man met man met

    man met man met man metaphor being like man met man met man metaphor being like
    man met man met man metaphor being like

    like a ball and then the the the noise like a ball and then the the the noise'
  concept_slugs:
  - classifier-free-guidance
  - classifier-guidance
- idx: 25
  start_sec: 1326.799
  end_sec: 1376.4
  text: 'like a ball and then the the the noise

    level the manifold for each noise level level the manifold for each noise level
    level the manifold for each noise level

    is just just like layered shells that is is just just like layered shells that
    is is just just like layered shells that is

    like expanding uh but they''re but like expanding uh but they''re but like expanding
    uh but they''re but

    they''re shells they''re not like um they''re shells they''re not like um they''re
    shells they''re not like um

    they''re not like solid and the reason they''re not like solid and the reason
    they''re not like solid and the reason

    why uh this is happening is because uh why uh this is happening is because uh
    why uh this is happening is because uh

    highdimensional gausians are actually so highdimensional gausians are actually
    so highdimensional gausians are actually so

    bubbles and you can actually prove this bubbles and you can actually prove this
    bubbles and you can actually prove this

    And I''m not going to prove it because And I''m not going to prove it because
    And I''m not going to prove it because

    it''s a but this is a very good exercise it''s a but this is a very good exercise
    it''s a but this is a very good exercise

    to prove. Um so if you want to prove it to prove. Um so if you want to prove it
    to prove. Um so if you want to prove it

    at home uh basically just try to see at home uh basically just try to see at home
    uh basically just try to see

    where is the the majority of the density where is the the majority of the density
    where is the the majority of the density

    concentrated at for high dimensional concentrated at for high dimensional concentrated
    at for high dimensional

    gausian. So basically just like the gausian. So basically just like the gausian.
    So basically just like the

    probability of like the x value within a probability of like the x value within
    a probability of like the x value within a

    certain range or like within a certain certain range or like within a certain
    certain range or like within a certain

    distance from the origin. Uh and then distance from the origin. Uh and then'
  concept_slugs:
  - classifier-free-guidance
  - classifier-guidance
- idx: 26
  start_sec: 1376.4
  end_sec: 1424.32
  text: 'distance from the origin. Uh and then

    and then like basically we''re going to and then like basically we''re going to
    and then like basically we''re going to

    see that around like 90% of the density see that around like 90% of the density
    see that around like 90% of the density

    is going to be concentrated on a certain is going to be concentrated on a certain
    is going to be concentrated on a certain

    shell. Uh so this is why um Gausian even shell. Uh so this is why um Gausian even
    shell. Uh so this is why um Gausian even

    though it has support on the entire data though it has support on the entire data
    though it has support on the entire data

    space is actually just soap bubbles. space is actually just soap bubbles. space
    is actually just soap bubbles.

    Okay highdimensional gions but anyway so Okay highdimensional gions but anyway
    so Okay highdimensional gions but anyway so

    this is kind of leads to uh the second this is kind of leads to uh the second
    this is kind of leads to uh the second

    problem that that this thing has. Um problem that that this thing has. Um problem
    that that this thing has. Um

    basically uh because like all the noisy basically uh because like all the noisy
    basically uh because like all the noisy

    examples also kind of follow some examples also kind of follow some examples also
    kind of follow some

    manifolds. Um so this thing is actually manifolds. Um so this thing is actually
    manifolds. Um so this thing is actually

    really problematic, right? Like really problematic, right? Like really problematic,
    right? Like

    basically the the final guided example basically the the final guided example
    basically the the final guided example

    here is actually pretty problematic here is actually pretty problematic here is
    actually pretty problematic

    because the guidance is actually because the guidance is actually because the
    guidance is actually

    unconstrained. So it''s like it doesn''t unconstrained. So it''s like it doesn''t
    unconstrained. So it''s like it doesn''t

    really tell you that you should stay on really tell you that you should stay on
    really tell you that you should stay on

    the manifold at all. So the guided the manifold at all. So the guided'
  concept_slugs:
  - classifier-free-guidance
  - classifier-guidance
- idx: 27
  start_sec: 1424.32
  end_sec: 1470.72
  text: 'the manifold at all. So the guided

    sample can completely go off the sample can completely go off the sample can completely
    go off the

    manifold and just like wander off and manifold and just like wander off and manifold
    and just like wander off and

    just like becomes like really really you just like becomes like really really
    you just like becomes like really really you

    know has a lot of artifacts you know the know has a lot of artifacts you know
    the know has a lot of artifacts you know the

    human can have like uh just just I don''t human can have like uh just just I don''t
    human can have like uh just just I don''t

    know like elephant uh nose or something know like elephant uh nose or something
    know like elephant uh nose or something

    like that those stuff can happen when like that those stuff can happen when like
    that those stuff can happen when

    you go off the manifold right so you go off the manifold right so you go off the
    manifold right so

    basically to ensure that the the guided basically to ensure that the the guided
    basically to ensure that the the guided

    sample doesn''t go off the manifold that sample doesn''t go off the manifold that
    sample doesn''t go off the manifold that

    much you either need very very very much you either need very very very much you
    either need very very very

    small guidance steps and and or you''ll small guidance steps and and or you''ll
    small guidance steps and and or you''ll

    need a lot of diffusion steps in order need a lot of diffusion steps in order
    need a lot of diffusion steps in order

    for those like smaller uh guidance step for those like smaller uh guidance step
    for those like smaller uh guidance step

    to be effective or the diffusion process to be effective or the diffusion process
    to be effective or the diffusion process

    can like sort of like even out those um can like sort of like even out those um
    can like sort of like even out those um

    uh those artifacts. Okay, so both of the uh those artifacts. Okay, so both of
    the uh those artifacts. Okay, so both of the

    these things basically just contribute these things basically just contribute'
  concept_slugs:
  - classifier-free-guidance
  - classifier-guidance
- idx: 28
  start_sec: 1470.72
  end_sec: 1549.43
  text: 'these things basically just contribute

    to the fact that DPS is really really to the fact that DPS is really really to
    the fact that DPS is really really

    really slow and if you try to reduce the really slow and if you try to reduce
    the really slow and if you try to reduce the

    number of time steps that you um that number of time steps that you um that number
    of time steps that you um that

    you take with DPS, it''s just not going you take with DPS, it''s just not going
    you take with DPS, it''s just not going

    to look good. It''s just going to have a to look good. It''s just going to have
    a to look good. It''s just going to have a

    lot of artifacts. It doesn''t look like a lot of artifacts. It doesn''t look like
    a lot of artifacts. It doesn''t look like a

    real image anymore. Um, okay. So, how do real image anymore. Um, okay. So, how
    do real image anymore. Um, okay. So, how do

    we want to uh improve we want to uh improve we want to uh improve

    people in person? The the people in in people in person? The the people in in
    people in person? The the people in in

    person. That''s uh Yes. >> We we have a simpler answer. Yeah. >> We we have a
    simpler answer. Yeah.

    Okay. Someone Okay. Someone Okay. Someone

    >> Oh, okay. Okay. Sorry. Sorry, let''s just >> Oh, okay. Okay. Sorry. Sorry,
    let''s just >> Oh, okay. Okay. Sorry. Sorry, let''s just

    keep Okay. Okay. Any anyone else >> is that? >> is that?

    >> Wait, >> well, how would you do classifier free >> well, how would you do classifier
    free

    here? This is a unconditional model. You here? This is a unconditional model.
    You here? This is a unconditional model. You

    cannot do classifier free, right? >> Embed text with the same model. >> Embed
    text with the same model.

    Um there''s a simpler answer. Basically Um there''s a simpler answer. Basically
    Um there''s a simpler answer. Basically

    just how do we change the errors here a just how do we change the errors here
    a just how do we change the errors here a

    little bit like how do we is there any'
  concept_slugs:
  - classifier-free-guidance
  - classifier-guidance
- idx: 29
  start_sec: 1549.43
  end_sec: 1596.24
  text: 'little bit like how do we is there any little bit like how do we is there
    any

    other ways that we can apply guidance. >> Yeah. Yeah. So basically the first thing
    >> Yeah. Yeah. So basically the first thing

    that we can do is instead of taking that we can do is instead of taking that we
    can do is instead of taking

    gradient I I think uh probably Alice I gradient I I think uh probably Alice I
    gradient I I think uh probably Alice I

    guess was saying that already like guess was saying that already like guess was
    saying that already like

    before uh was that um like instead of before uh was that um like instead of before
    uh was that um like instead of

    taking gradient with respect to XT the taking gradient with respect to XT the
    taking gradient with respect to XT the

    first thing you can do right is to take first thing you can do right is to take
    first thing you can do right is to take

    gradient with respect to the clean image gradient with respect to the clean image
    gradient with respect to the clean image

    which is the the X0 prediction first which is the the X0 prediction first which
    is the the X0 prediction first

    right because uh this way what you would right because uh this way what you would
    right because uh this way what you would

    what you would get is that you can uh what you would get is that you can uh what
    you would get is that you can uh

    and then add the noise back Okay, so and then add the noise back Okay, so and
    then add the noise back Okay, so

    this way you don''t need to back prop this way you don''t need to back prop this
    way you don''t need to back prop

    through the diffusion model anymore. Um, through the diffusion model anymore.
    Um, through the diffusion model anymore. Um,

    and back propping diff through the and back propping diff through the and back
    propping diff through the

    diffusion model is usually the more diffusion model is usually the more diffusion
    model is usually the more

    expensive thing to do. So because the expensive thing to do. So because the'
  concept_slugs:
  - classifier-free-guidance
  - classifier-guidance
- idx: 30
  start_sec: 1596.24
  end_sec: 1649.99
  text: 'expensive thing to do. So because the

    because the classifier is usually really because the classifier is usually really
    because the classifier is usually really

    small. So yeah, so the first thing that small. So yeah, so the first thing that
    small. So yeah, so the first thing that

    you can do to speed this up is to you can do to speed this up is to you can do
    to speed this up is to

    instead of taking gradient with respect instead of taking gradient with respect
    instead of taking gradient with respect

    to the clean image, you can just take to the clean image, you can just take to
    the clean image, you can just take

    sorry with respect to the noisy image, sorry with respect to the noisy image,
    sorry with respect to the noisy image,

    you could just take the gradient with you could just take the gradient with you
    could just take the gradient with

    back to the clean image and you don''t back to the clean image and you don''t
    back to the clean image and you don''t

    need a back prop through the diffusion need a back prop through the diffusion
    need a back prop through the diffusion

    anymore. Okay. Any question? >> No. The classifier is off the shelf >> No. The
    classifier is off the shelf

    pre-trained. pre-trained. pre-trained.

    >> No, I think it''s being trained. Yeah. Any other question? Any other question?

    >> Yeah. >> Yeah.

    >> But does it actually make you closer to >> But does it actually make you closer
    to >> But does it actually make you closer to

    the manifold? the manifold? the manifold?

    >> Yeah, that''s another question. Right. So >> Yeah, that''s another question.
    Right. So >> Yeah, that''s another question. Right. So

    like it does it it doesn''t really it like it does it it doesn''t really it like
    it does it it doesn''t really it

    doesn''t really like make you closer to doesn''t really like make you closer to
    doesn''t really like make you closer to

    the manifold right it it still doesn''t the manifold right it it still doesn''t
    the manifold right it it still doesn''t

    have any constraint with respect to the have any constraint with respect to the
    have any constraint with respect to the

    manifold right so what should we do next'
  concept_slugs:
  - classifier-free-guidance
  - classifier-guidance
- idx: 31
  start_sec: 1649.99
  end_sec: 1691.6
  text: 'manifold right so what should we do next manifold right so what should we
    do next

    the other very easy thing to do here is the other very easy thing to do here is
    the other very easy thing to do here is

    after we do this we could literally just after we do this we could literally just
    after we do this we could literally just

    like find the manifold or like what we like find the manifold or like what we
    like find the manifold or like what we

    say the tangent space of the manifold. say the tangent space of the manifold.
    say the tangent space of the manifold.

    So what is the tension space of manifold So what is the tension space of manifold
    So what is the tension space of manifold

    is literally just imagine like a tangent is literally just imagine like a tangent
    is literally just imagine like a tangent

    plane. So like say your manifold is like plane. So like say your manifold is like
    plane. So like say your manifold is like

    a shell and then the the the the tangent a shell and then the the the the tangent
    a shell and then the the the the tangent

    space is literally just the the plane space is literally just the the plane space
    is literally just the the plane

    that tangent to your shell and and that tangent to your shell and and that tangent
    to your shell and and

    basically the reason why we have a basically the reason why we have a basically
    the reason why we have a

    tangent space that is like flatish is tangent space that is like flatish is tangent
    space that is like flatish is

    because um like your um basically each because um like your um basically each
    because um like your um basically each

    point on your manifold is like locally point on your manifold is like locally
    point on your manifold is like locally

    uh low dimensional ukidian. So that''s uh low dimensional ukidian. So that''s
    uh low dimensional ukidian. So that''s

    why everything can be so just this is why everything can be so just this is why
    everything can be so just this is

    like a property of the like the low low like a property of the like the low low'
  concept_slugs:
  - classifier-free-guidance
  - classifier-guidance
- idx: 32
  start_sec: 1691.6
  end_sec: 1738.799
  text: 'like a property of the like the low low

    dimensional manifold. So basically you dimensional manifold. So basically you
    dimensional manifold. So basically you

    can you can basically just like have a can you can basically just like have a
    can you can basically just like have a

    like plane that just like tangent to like plane that just like tangent to like
    plane that just like tangent to

    your shell. Uh but yeah basically we can your shell. Uh but yeah basically we
    can your shell. Uh but yeah basically we can

    just literally uh project uh the the the just literally uh project uh the the
    the just literally uh project uh the the the

    the noisy example onto the manifold the noisy example onto the manifold the noisy
    example onto the manifold

    right and this way we can just get right and this way we can just get right and
    this way we can just get

    things on the manifold directly or at things on the manifold directly or at things
    on the manifold directly or at

    least close to it. Um least close to it. Um least close to it. Um

    uh what what is the problem here then? uh what what is the problem here then?
    uh what what is the problem here then?

    Yeah. Yeah.

    >> Put the manifold. >> Put the manifold. >> Put the manifold.

    >> Yeah. Right. How do you like we don''t >> Yeah. Right. How do you like we don''t
    >> Yeah. Right. How do you like we don''t

    have access to those manifolds like what have access to those manifolds like what
    have access to those manifolds like what

    is going on like like how do you is going on like like how do you is going on
    like like how do you

    actually do this, right? Uh so basically actually do this, right? Uh so basically
    actually do this, right? Uh so basically

    uh what''s happening here is that I think uh what''s happening here is that I
    think uh what''s happening here is that I think

    uh I mentioned this in like the first uh I mentioned this in like the first uh
    I mentioned this in like the first

    class or something. Uh but basically you class or something. Uh but basically
    you'
  concept_slugs:
  - classifier-free-guidance
  - classifier-guidance
- idx: 33
  start_sec: 1738.799
  end_sec: 1784.0
  text: 'class or something. Uh but basically you

    can actually get access to the data can actually get access to the data can actually
    get access to the data

    manifold via the decoder of an manifold via the decoder of an manifold via the
    decoder of an

    autoenccoder. Right? So basically just autoenccoder. Right? So basically just
    autoenccoder. Right? So basically just

    try to imagine that like the encoder is try to imagine that like the encoder is
    try to imagine that like the encoder is

    like compressing like your uh high like compressing like your uh high like compressing
    like your uh high

    dimensional data into a dimensional data into a dimensional data into a

    lowerishdimensional lowerishdimensional lowerishdimensional

    representation space and then this lower representation space and then this lower
    representation space and then this lower

    representation space get decoded back to representation space get decoded back
    to representation space get decoded back to

    the the the high dimensional the the the high dimensional the the the high dimensional

    reconstruction and this compression is reconstruction and this compression is
    reconstruction and this compression is

    sort of like just like getting you sort of like just like getting you sort of
    like just like getting you

    access to the actual manifold of the access to the actual manifold of the access
    to the actual manifold of the

    data. And like if you try to access the data. And like if you try to access the
    data. And like if you try to access the

    tangent space which is which means that tangent space which is which means that
    tangent space which is which means that

    basically just like the the like how basically just like the the like how basically
    just like the the like how

    much you move on the tangent space can much you move on the tangent space can
    much you move on the tangent space can

    sort of be mapped to how much you move sort of be mapped to how much you move
    sort of be mapped to how much you move

    on the on the on the latent space or on on the on the on the latent space or on
    on the on the on the latent space or on

    the like the the yeah the low the like the the yeah the low'
  concept_slugs:
  - classifier-free-guidance
  - classifier-guidance
- idx: 34
  start_sec: 1784.0
  end_sec: 1832.559
  text: 'the like the the yeah the low

    dimensional like representation space. dimensional like representation space.
    dimensional like representation space.

    Um so essentially this is like kind of Um so essentially this is like kind of
    Um so essentially this is like kind of

    complicated to to understand but complicated to to understand but complicated
    to to understand but

    basically just the jacobian which is basically just the jacobian which is basically
    just the jacobian which is

    like the direction and how much you like the direction and how much you like the
    direction and how much you

    should move in of the the decoder can should move in of the the decoder can should
    move in of the the decoder can

    give us access to the tangent space of give us access to the tangent space of
    give us access to the tangent space of

    the the data manifold. So basically all the the data manifold. So basically all
    the the data manifold. So basically all

    you need to do is to take gradient with you need to do is to take gradient with
    you need to do is to take gradient with

    respect to some decoder of the respect to some decoder of the respect to some
    decoder of the

    autoenccoder and you can get access to autoenccoder and you can get access to
    autoenccoder and you can get access to

    the manifold. Uh but this doesn''t really the manifold. Uh but this doesn''t really
    the manifold. Uh but this doesn''t really

    answer our question, right? Because answer our question, right? Because answer
    our question, right? Because

    we like we I mean we could use we like we I mean we could use we like we I mean
    we could use

    autoenccoders to get access to autoenccoders to get access to autoenccoders to
    get access to

    manifolds, but we still don''t have an manifolds, but we still don''t have an
    manifolds, but we still don''t have an

    autoenccoder for each noise level, autoenccoder for each noise level, autoenccoder
    for each noise level,

    right? That''s just like impossible. Who right? That''s just like impossible.
    Who right? That''s just like impossible. Who

    would train a autoenccoder on noisy would train a autoenccoder on noisy would
    train a autoenccoder on noisy

    samples and label them with noise samples and label them with noise'
  concept_slugs:
  - classifier-free-guidance
  - classifier-guidance
- idx: 35
  start_sec: 1832.559
  end_sec: 1884.63
  text: 'samples and label them with noise

    levels, right? Nobody. Nobody would do levels, right? Nobody. Nobody would do
    levels, right? Nobody. Nobody would do

    that. Um but if you that. Um but if you that. Um but if you

    think about it, right? think about it, right? think about it, right?

    There are a lot of people who try to There are a lot of people who try to There
    are a lot of people who try to

    train autoenccoders on clean data, train autoenccoders on clean data, train autoenccoders
    on clean data,

    right? So we have a lot of pre-trained right? So we have a lot of pre-trained
    right? So we have a lot of pre-trained

    autoenccoders and just lying around. So autoenccoders and just lying around. So
    autoenccoders and just lying around. So

    you couldn''t just just use that, right? you couldn''t just just use that, right?
    you couldn''t just just use that, right?

    And so what you can do here is And so what you can do here is And so what you
    can do here is

    the the anime is a little problem. But the the anime is a little problem. But
    the the anime is a little problem. But

    basically what you can do is you can basically what you can do is you can basically
    what you can do is you can

    first project um the clean the guided first project um the clean the guided first
    project um the clean the guided

    clean data estimation onto the actual clean data estimation onto the actual clean
    data estimation onto the actual

    data manifold. So that like basically data manifold. So that like basically data
    manifold. So that like basically

    you get a valid sample uh from your uh you get a valid sample uh from your uh
    you get a valid sample uh from your uh

    from your guidance and then you just uh from your guidance and then you just uh
    from your guidance and then you just uh

    like add noise back to the correct uh um like add noise back to the correct uh
    um like add noise back to the correct uh um

    noise level and then because everything noise level and then because everything
    noise level and then because everything

    is is is

    we have one for clean IM. Oh yes yes uh'
  concept_slugs:
  - classifier-free-guidance
  - classifier-guidance
- idx: 36
  start_sec: 1884.63
  end_sec: 1922.799
  text: 'we have one for clean IM. Oh yes yes uh we have one for clean IM. Oh yes
    yes uh

    you can speak up by the way the the you can speak up by the way the the you can
    speak up by the way the the

    people online can just speak up when you people online can just speak up when
    you people online can just speak up when you

    have things. Sorry I I don''t I didn''t have things. Sorry I I don''t I didn''t
    have things. Sorry I I don''t I didn''t

    check the the but yes this is a great check the the but yes this is a great check
    the the but yes this is a great

    answer. This is exactly what we do here. answer. This is exactly what we do here.
    answer. This is exactly what we do here.

    Um, yeah. So, so yeah. So, we and then Um, yeah. So, so yeah. So, we and then
    Um, yeah. So, so yeah. So, we and then

    and then you just project it back and and then you just project it back and and
    then you just project it back and

    then you just add noise back to the then you just add noise back to the then you
    just add noise back to the

    correct uh noise level here. Um, yeah. correct uh noise level here. Um, yeah.
    correct uh noise level here. Um, yeah.

    And this thing is called manifold And this thing is called manifold And this thing
    is called manifold

    preserving guided diffusion. So, this is preserving guided diffusion. So, this
    is preserving guided diffusion. So, this is

    uh actually my research. uh actually my research. uh actually my research.

    Anyway, but uh but basically this is Anyway, but uh but basically this is Anyway,
    but uh but basically this is

    just like a and why is this a simple way just like a and why is this a simple
    way just like a and why is this a simple way

    like why do we why why is a a good idea like why do we why why is a a good idea
    like why do we why why is a a good idea

    to assume that we have access to to assume that we have access to'
  concept_slugs:
  - classifier-free-guidance
  - classifier-guidance
- idx: 37
  start_sec: 1922.799
  end_sec: 1972.799
  text: 'to assume that we have access to

    autoenccoders? Uh we''re going to talk autoenccoders? Uh we''re going to talk
    autoenccoders? Uh we''re going to talk

    about the next class actually but about the next class actually but about the
    next class actually but

    basically the long story short is that basically the long story short is that
    basically the long story short is that

    many of the modern of SOTA models are many of the modern of SOTA models are many
    of the modern of SOTA models are

    trained on some latence base for example trained on some latence base for example
    trained on some latence base for example

    stable diffusion. So you automatically stable diffusion. So you automatically
    stable diffusion. So you automatically

    have access to the the like a have access to the the like a have access to the
    the like a

    autoenccoder or the latency space of autoenccoder or the latency space of autoenccoder
    or the latency space of

    autoenccoder and actually you just like autoenccoder and actually you just like
    autoenccoder and actually you just like

    take gradient normally and then you take gradient normally and then you take gradient
    normally and then you

    would have just get an on manifold would have just get an on manifold would have
    just get an on manifold

    sample anyway. Yeah. But anyway point sample anyway. Yeah. But anyway point sample
    anyway. Yeah. But anyway point

    being being being

    uh so now this thing is uh both fast and uh so now this thing is uh both fast
    and uh so now this thing is uh both fast and

    good and most importantly both DPS and good and most importantly both DPS and
    good and most importantly both DPS and

    uh MPGd are training free. So you do not uh MPGd are training free. So you do
    not uh MPGd are training free. So you do not

    train any models. You just take a train any models. You just take a train any
    models. You just take a

    pre-trained diffusion model. You take a pre-trained diffusion model. You take
    a pre-trained diffusion model. You take a

    offtheshelf uh classifier clip whatever offtheshelf uh classifier clip whatever
    offtheshelf uh classifier clip whatever

    uh and you can just uh and and this this uh and you can just uh and and this this'
  concept_slugs:
  - classifier-free-guidance
  - classifier-guidance
- idx: 38
  start_sec: 1972.799
  end_sec: 2017.039
  text: 'uh and you can just uh and and this this

    algorithm is applicable to all algorithm is applicable to all algorithm is applicable
    to all

    differentiable guidance or classifiers differentiable guidance or classifiers
    differentiable guidance or classifiers

    or reward models that you have on just or reward models that you have on just
    or reward models that you have on just

    off the shelf. Uh so here basically we off the shelf. Uh so here basically we
    off the shelf. Uh so here basically we

    can apply noisy linear uh inverse can apply noisy linear uh inverse can apply
    noisy linear uh inverse

    problem which means that basically you problem which means that basically you
    problem which means that basically you

    can do uh either like uh gausian deep can do uh either like uh gausian deep can
    do uh either like uh gausian deep

    learning or you can do like super learning or you can do like super learning or
    you can do like super

    resolution both of these work really resolution both of these work really resolution
    both of these work really

    well or you can say say you have like a well or you can say say you have like
    a well or you can say say you have like a

    facial recognition model right you can facial recognition model right you can
    facial recognition model right you can

    use that and use the face ID as your use that and use the face ID as your use
    that and use the face ID as your

    label and then you can do like basically label and then you can do like basically
    label and then you can do like basically

    face ID condition the generation so you face ID condition the generation so you
    face ID condition the generation so you

    are able to um essentially generate the are able to um essentially generate the
    are able to um essentially generate the

    same person but with a different like same person but with a different like same
    person but with a different like

    different in a different context. And different in a different context. And different
    in a different context. And

    you can also turn a unconditional model you can also turn a unconditional model
    you can also turn a unconditional model

    into a text condition model without into a text condition model without'
  concept_slugs:
  - classifier-free-guidance
  - classifier-guidance
- idx: 39
  start_sec: 2017.039
  end_sec: 2069.599
  text: 'into a text condition model without

    training anything by just applying clip training anything by just applying clip
    training anything by just applying clip

    clip guidance to your to to your clip guidance to your to to your clip guidance
    to your to to your

    unconditional model. You can do style unconditional model. You can do style unconditional
    model. You can do style

    guidance and you can even combine guidance and you can even combine guidance and
    you can even combine

    everything. So if you just apply this everything. So if you just apply this everything.
    So if you just apply this

    thing you you apply um phase ID guidance thing you you apply um phase ID guidance
    thing you you apply um phase ID guidance

    to stable diffusion you can get a uh to stable diffusion you can get a uh to stable
    diffusion you can get a uh

    like just a text condition and face ID like just a text condition and face ID
    like just a text condition and face ID

    condition the model from your only text condition the model from your only text
    condition the model from your only text

    condition train diffusion. Okay any condition train diffusion. Okay any condition
    train diffusion. Okay any

    question? Yeah. question? Yeah. question? Yeah.

    >> What does it look like to do a >> What does it look like to do a >> What does
    it look like to do a

    projection? projection? projection?

    >> So basically what it looks like is that >> So basically what it looks like
    is that >> So basically what it looks like is that

    you literally just you literally just you literally just

    You literally just take the so so so so You literally just take the so so so so
    You literally just take the so so so so

    say like your image goes through the say like your image goes through the say
    like your image goes through the

    decoder. So the image usually will go to decoder. So the image usually will go
    to decoder. So the image usually will go to

    an incoder and then the decoder and then an incoder and then the decoder and then
    an incoder and then the decoder and then

    go to your classifier, right? So all you go to your classifier, right? So all
    you'
  concept_slugs:
  - classifier-free-guidance
  - classifier-guidance
- idx: 40
  start_sec: 2069.599
  end_sec: 2115.589
  text: 'go to your classifier, right? So all you

    need to do is to take gradient all the need to do is to take gradient all the
    need to do is to take gradient all the

    way back and that''s that gradient will way back and that''s that gradient will
    way back and that''s that gradient will

    be projected. So you just so instead of be projected. So you just so instead of
    be projected. So you just so instead of

    like only taking gradients through your like only taking gradients through your
    like only taking gradients through your

    classifier, you take gradients through classifier, you take gradients through
    classifier, you take gradients through

    an autoenccoder and a classifier. That''s an autoenccoder and a classifier. That''s
    an autoenccoder and a classifier. That''s

    it. Yeah. And if you''re using stable it. Yeah. And if you''re using stable it.
    Yeah. And if you''re using stable

    diffusion, which we''re going to talk diffusion, which we''re going to talk diffusion,
    which we''re going to talk

    about next class, you just need to like about next class, you just need to like
    about next class, you just need to like

    everything stays in the latent space. everything stays in the latent space. everything
    stays in the latent space.

    You just need to take gradient with You just need to take gradient with You just
    need to take gradient with

    respect to the classifier and the stable respect to the classifier and the stable
    respect to the classifier and the stable

    diffusion decod uh uh VA decoder and diffusion decod uh uh VA decoder and diffusion
    decod uh uh VA decoder and

    that''s it. that''s it. that''s it.

    >> Yeah. the noisy linear inverse problem. >> Yeah. the noisy linear inverse problem.
    >> Yeah. the noisy linear inverse problem.

    >> Oh yeah. So noisy linear inverse problem >> Oh yeah. So noisy linear inverse
    problem >> Oh yeah. So noisy linear inverse problem

    means that say you have like this is means that say you have like this is means
    that say you have like this is

    like you have like a linear operator like you have like a linear operator like
    you have like a linear operator

    that like contaminates or like degrades that like contaminates or like degrades
    that like contaminates or like degrades

    your uh like your your your image. Say'
  concept_slugs:
  - classifier-free-guidance
  - classifier-guidance
- idx: 41
  start_sec: 2115.589
  end_sec: 2172.31
  text: 'your uh like your your your image. Say your uh like your your your image.
    Say

    for example you have like a gausian blur for example you have like a gausian blur
    for example you have like a gausian blur

    kernel or you have like some like kernel or you have like some like kernel or
    you have like some like

    downsampling uh kernels and uh and and downsampling uh kernels and uh and and
    downsampling uh kernels and uh and and

    that''s like a that''s what we call a that''s like a that''s what we call a that''s
    like a that''s what we call a

    linear because they are like linear linear because they are like linear linear
    because they are like linear

    kernels or you can approximate these uh kernels or you can approximate these uh
    kernels or you can approximate these uh

    operation by linear kernels. So that''s operation by linear kernels. So that''s
    operation by linear kernels. So that''s

    why we call it a linear inverse problem. why we call it a linear inverse problem.
    why we call it a linear inverse problem.

    Inverse problem means that you try to Inverse problem means that you try to Inverse
    problem means that you try to

    recover the data after the uh before recover the data after the uh before recover
    the data after the uh before

    your operation. That''s why it''s inverse. your operation. That''s why it''s inverse.
    your operation. That''s why it''s inverse.

    And then noisy means that you have And then noisy means that you have And then
    noisy means that you have

    observation noise. So or measurement observation noise. So or measurement observation
    noise. So or measurement

    noise. So like instead of like the noise. So like instead of like the noise. So
    like instead of like the

    actual uh like the degraded sample, the actual uh like the degraded sample, the
    actual uh like the degraded sample, the

    degraded sample actually contains some degraded sample actually contains some
    degraded sample actually contains some

    gausian noise. Um so this is why it''s gausian noise. Um so this is why it''s
    gausian noise. Um so this is why it''s

    called noisy linear inverse problem. Any called noisy linear inverse problem.
    Any called noisy linear inverse problem. Any

    other question? Cool. Cool.

    Now that we''re in the realm of training'
  concept_slugs:
  - classifier-free-guidance
  - classifier-guidance
- idx: 42
  start_sec: 2172.31
  end_sec: 2235.04
  text: 'Now that we''re in the realm of training Now that we''re in the realm of
    training

    free uh guidance, is there any other way free uh guidance, is there any other
    way free uh guidance, is there any other way

    to inject condition into diffusion to inject condition into diffusion to inject
    condition into diffusion

    models training free? What do we think? models training free? What do we think?
    models training free? What do we think?

    People in person and online, please, if People in person and online, please, if
    People in person and online, please, if

    you''re online, you can just unmute. Uh could you try to Uh could you try to

    uh somehow uh somehow uh somehow

    choose your starting noise and see if choose your starting noise and see if choose
    your starting noise and see if

    that like has particular properties. that like has particular properties. that
    like has particular properties.

    >> Yeah. Yeah. That''s something that we''re >> Yeah. Yeah. That''s something
    that we''re >> Yeah. Yeah. That''s something that we''re

    not going to talk about today. But yes, not going to talk about today. But yes,
    not going to talk about today. But yes,

    these things is actually particular these things is actually particular these
    things is actually particular

    powerful for uh for for like more powerful for uh for for like more powerful for
    uh for for like more

    deterministic models, right? Because deterministic models, right? Because deterministic
    models, right? Because

    like diffusion you don''t actually have like diffusion you don''t actually have
    like diffusion you don''t actually have

    an inverse map but for like flow an inverse map but for like flow an inverse map
    but for like flow

    matching and something like that you can matching and something like that you
    can matching and something like that you can

    v you can potentially you know optimize v you can potentially you know optimize
    v you can potentially you know optimize

    your starting point so that you can get your starting point so that you can get
    your starting point so that you can get

    like a more controlled or like better um like a more controlled or like better
    um like a more controlled or like better um

    nonisotropic noise um uh yeah sort of nonisotropic noise um uh yeah sort of'
  concept_slugs:
  - classifier-free-guidance
  - classifier-guidance
- idx: 43
  start_sec: 2235.04
  end_sec: 2277.19
  text: 'nonisotropic noise um uh yeah sort of

    basically it''s the same thing right I basically it''s the same thing right I
    basically it''s the same thing right I

    guess Adrian so like uh like basically guess Adrian so like uh like basically
    guess Adrian so like uh like basically

    what you can do is you can like um what you can do is you can like um what you
    can do is you can like um

    visibly have like a optimization process visibly have like a optimization process
    visibly have like a optimization process

    to optimize ize the initial noise so to optimize ize the initial noise so to optimize
    ize the initial noise so

    that you can have like a you can have a that you can have like a you can have
    a that you can have like a you can have a

    controlled uh like sample at the end. controlled uh like sample at the end. controlled
    uh like sample at the end.

    But these things like have some caveats, But these things like have some caveats,
    But these things like have some caveats,

    right? Because like say if you''re using right? Because like say if you''re using
    right? Because like say if you''re using

    a flow matching model, even though it a flow matching model, even though it a
    flow matching model, even though it

    it''s a deter it has deterministic it''s a deter it has deterministic it''s a
    deter it has deterministic

    mapping, uh it actually you take a lot mapping, uh it actually you take a lot
    mapping, uh it actually you take a lot

    of steps, right? To get to the the final of steps, right? To get to the the final
    of steps, right? To get to the the final

    um like sample. So if you try to do um like sample. So if you try to do um like
    sample. So if you try to do

    optimization, you actually need to do optimization, you actually need to do optimization,
    you actually need to do

    back propagations through like a back propagations through like a back propagations
    through like a

    cascading chain of the same model. Um so cascading chain of the same model. Um
    so cascading chain of the same model. Um so

    so like B and if your model is really'
  concept_slugs:
  - classifier-free-guidance
  - classifier-guidance
- idx: 44
  start_sec: 2277.19
  end_sec: 2362.31
  text: 'so like B and if your model is really so like B and if your model is really

    large the it''s like a lot of memory large the it''s like a lot of memory large
    the it''s like a lot of memory

    requirement right so that might be an requirement right so that might be an requirement
    right so that might be an

    issue so usually people would do this uh issue so usually people would do this
    uh issue so usually people would do this uh

    with like a like a onestep distilled with like a like a onestep distilled with
    like a like a onestep distilled

    model which is something that we''re model which is something that we''re model
    which is something that we''re

    going to talk about the week after next going to talk about the week after next
    going to talk about the week after next

    week um yeah and uh yeah so this thing week um yeah and uh yeah so this thing
    week um yeah and uh yeah so this thing

    is people actually do it um but good is people actually do it um but good is people
    actually do it um but good

    good answer but uh what else can we do okay let me give you a hint okay let me
    give you a hint

    Remember this is how we do DDPM. What Remember this is how we do DDPM. What Remember
    this is how we do DDPM. What

    else can we change about DDPM besides else can we change about DDPM besides else
    can we change about DDPM besides

    adding another gradient? Nobody is thinking. No. Nobody is thinking. No.

    Okay. So >> Instead of having another gradient >> Instead of having another gradient

    >> instead of having another gradient. >> instead of having another gradient.
    >> instead of having another gradient.

    >> Yeah. Can we just like sample? >> Yeah. Can we just like sample? >> Yeah. Can
    we just like sample?

    >> Um >> Um >> Um

    what do you mean? what do you mean? what do you mean?

    >> Uh from like the interest rate or not >> Uh from like the interest rate or
    not >> Uh from like the interest rate or not

    the classifier basically. the classifier basically. the classifier basically.

    >> Okay. The classifier cannot be trained,'
  concept_slugs:
  - classifier-free-guidance
  - classifier-guidance
  - ddpm
- idx: 45
  start_sec: 2362.31
  end_sec: 2414.72
  text: '>> Okay. The classifier cannot be trained, >> Okay. The classifier cannot
    be trained,

    right? They cannot sample, right? You right? They cannot sample, right? You right?
    They cannot sample, right? You

    cannot sample from a classifier because cannot sample from a classifier because
    cannot sample from a classifier because

    it''s a discriminated model. You there''s it''s a discriminated model. You there''s
    it''s a discriminated model. You there''s

    no way to sample from a classifier. no way to sample from a classifier. no way
    to sample from a classifier.

    Yeah. What else? No gradient this time. Okay. Uh D. Okay. Yeah. Yeah. Someone
    Okay. Uh D. Okay. Yeah. Yeah. Someone

    someone can do something like someone can do something like someone can do something
    like

    self-guidance instead of a classifier self-guidance instead of a classifier self-guidance
    instead of a classifier

    model. model. model.

    Very similar. Were you gonna say Very similar. Were you gonna say Very similar.
    Were you gonna say

    something? Okay. Okay. Um but you were something? Okay. Okay. Um but you were
    something? Okay. Okay. Um but you were

    going to say something. Okay. going to say something. Okay. going to say something.
    Okay.

    You might uh like do multiple steps and You might uh like do multiple steps and
    You might uh like do multiple steps and

    then pick the one that was saying that then pick the one that was saying that
    then pick the one that was saying that

    this is good. Ah yeah yeah yeah yeah this is good. Ah yeah yeah yeah yeah this
    is good. Ah yeah yeah yeah yeah

    this is actually um yeah that''s a good this is actually um yeah that''s a good
    this is actually um yeah that''s a good

    answer too but like I I guess that thing answer too but like I I guess that thing
    answer too but like I I guess that thing

    also need gradient right but that''s a also need gradient right but that''s a
    also need gradient right but that''s a

    good answer and I believe people were good answer and I believe people were good
    answer and I believe people were

    doing that I think there''s a paper doing that I think there''s a paper doing
    that I think there''s a paper

    called like LGD loss guided diffusion or called like LGD loss guided diffusion
    or'
  concept_slugs:
  - classifier-free-guidance
  - classifier-guidance
- idx: 46
  start_sec: 2414.72
  end_sec: 2456.24
  text: 'called like LGD loss guided diffusion or

    something um uh that paper that paper something um uh that paper that paper something
    um uh that paper that paper

    was actually done by uh like the same was actually done by uh like the same was
    actually done by uh like the same

    author of DDIM and he''s also the founder author of DDIM and he''s also the founder
    author of DDIM and he''s also the founder

    of the uh company which is going to give of the uh company which is going to give
    of the uh company which is going to give

    us a talk like the week after the next us a talk like the week after the next
    us a talk like the week after the next

    week. But anyway, um yeah, so so you can week. But anyway, um yeah, so so you
    can week. But anyway, um yeah, so so you can

    do and then they they didn''t really pick do and then they they didn''t really
    pick do and then they they didn''t really pick

    the best one, they kind of do it like a the best one, they kind of do it like
    a the best one, they kind of do it like a

    Monte Carlo um style stuff. Okay. Uh Monte Carlo um style stuff. Okay. Uh Monte
    Carlo um style stuff. Okay. Uh

    create a proxy distribution or instead create a proxy distribution or instead
    create a proxy distribution or instead

    of going to t minus one, we go back to t of going to t minus one, we go back to
    t of going to t minus one, we go back to t

    and if a classifier is against it. Yes, and if a classifier is against it. Yes,
    and if a classifier is against it. Yes,

    that''s actually a great answer. Uh we''re that''s actually a great answer. Uh
    we''re that''s actually a great answer. Uh we''re

    going to talk about it later, but that''s going to talk about it later, but that''s
    going to talk about it later, but that''s

    a very very very good answer. This is a very very very good answer. This is a
    very very very good answer. This is

    actually a great trick that you should actually a great trick that you should'
  concept_slugs:
  - classifier-free-guidance
  - classifier-guidance
  - ddim
- idx: 47
  start_sec: 2456.24
  end_sec: 2497.68
  text: 'actually a great trick that you should

    do. create a proxy distribution. This is do. create a proxy distribution. This
    is do. create a proxy distribution. This is

    um that''s kind of something that we''re um that''s kind of something that we''re
    um that''s kind of something that we''re

    going to do here. Um so basically say if going to do here. Um so basically say
    if going to do here. Um so basically say if

    we already know what we''re going to we already know what we''re going to we already
    know what we''re going to

    generate, right? Then what we could do generate, right? Then what we could do
    generate, right? Then what we could do

    is we don''t we don''t need to use this is we don''t we don''t need to use this
    is we don''t we don''t need to use this

    like X0 estimation anymore, right? We like X0 estimation anymore, right? We like
    X0 estimation anymore, right? We

    can just like if we know the exact image can just like if we know the exact image
    can just like if we know the exact image

    that we''re going to generate, then we that we''re going to generate, then we
    that we''re going to generate, then we

    just use the actual X0 as the as the as just use the actual X0 as the as the as
    just use the actual X0 as the as the as

    the X0 at time t. And then we just like the X0 at time t. And then we just like
    the X0 at time t. And then we just like

    and then we just like go on with DIM, and then we just like go on with DIM, and
    then we just like go on with DIM,

    right? And then we can we can eventually right? And then we can we can eventually
    right? And then we can we can eventually

    get the probably get something similar get the probably get something similar
    get the probably get something similar

    back even though like there there will back even though like there there will
    back even though like there there will

    be some difference because because it''s be some difference because because it''s
    be some difference because because it''s

    generated. Um but the problem is we generated. Um but the problem is we'
  concept_slugs:
  - classifier-free-guidance
  - classifier-guidance
- idx: 48
  start_sec: 2497.68
  end_sec: 2545.839
  text: 'generated. Um but the problem is we

    don''t have what we want to generate yet, don''t have what we want to generate
    yet, don''t have what we want to generate yet,

    right? Because if we do, why why are we right? Because if we do, why why are we
    right? Because if we do, why why are we

    still generating? It doesn''t make sense. still generating? It doesn''t make sense.
    still generating? It doesn''t make sense.

    Um but do we really need to know exactly Um but do we really need to know exactly
    Um but do we really need to know exactly

    what we want to generate here? Like just what we want to generate here? Like just
    what we want to generate here? Like just

    just look at this, right? So this is the just look at this, right? So this is
    the just look at this, right? So this is the

    x0 that we''re going to use at time t and x0 that we''re going to use at time
    t and x0 that we''re going to use at time t and

    this is the exactly the thing that we this is the exactly the thing that we this
    is the exactly the thing that we

    try to generate. Do you think do you try to generate. Do you think do you try
    to generate. Do you think do you

    guys think we need exactly like we need guys think we need exactly like we need
    guys think we need exactly like we need

    to exactly know like what we need to to exactly know like what we need to to exactly
    know like what we need to

    generate in order to swap this in? What generate in order to swap this in? What
    generate in order to swap this in? What

    do we think? do we think? do we think?

    No. Why not? >> You can use the unconditional generation >> You can use the unconditional
    generation

    at first. at first. at first.

    >> Nah. No, because uh then this is the way >> Nah. No, because uh then this is
    the way >> Nah. No, because uh then this is the way

    that we''re going to inject condition, that we''re going to inject condition,
    that we''re going to inject condition,

    right? So, this needs to have a right? So, this needs to have a'
  concept_slugs:
  - classifier-free-guidance
  - classifier-guidance
- idx: 49
  start_sec: 2545.839
  end_sec: 2587.589
  text: 'right? So, this needs to have a

    condition in it. condition in it. condition in it.

    Okay. Hold on. The people on in person Okay. Hold on. The people on in person
    Okay. Hold on. The people on in person

    first. Yeah. first. Yeah. first. Yeah.

    >> That has the same classification part >> That has the same classification part
    >> That has the same classification part

    like Yeah. Yeah. Yeah. Basically, like Yeah. Yeah. Yeah. Basically, like Yeah.
    Yeah. Yeah. Basically,

    basically. And then people No, we just basically. And then people No, we just
    basically. And then people No, we just

    need a very rough idea because even that need a very rough idea because even that
    need a very rough idea because even that

    will be better than the noise. Yes, that will be better than the noise. Yes, that
    will be better than the noise. Yes, that

    is very correct. So, we don''t Yeah. So, is very correct. So, we don''t Yeah.
    So, is very correct. So, we don''t Yeah. So,

    basically you guys kind of have a basically you guys kind of have a basically
    you guys kind of have a

    similar idea, right? We don''t really similar idea, right? We don''t really similar
    idea, right? We don''t really

    need the exact image. All we need is for need the exact image. All we need is
    for need the exact image. All we need is for

    the image as long as the image contains the image as long as the image contains
    the image as long as the image contains

    enough information that we need. So that enough information that we need. So that
    enough information that we need. So that

    then we can just use it to swap in X0, then we can just use it to swap in X0,
    then we can just use it to swap in X0,

    right? So don''t we don''t really need to right? So don''t we don''t really need
    to right? So don''t we don''t really need to

    do this. So we we just need something do this. So we we just need something do
    this. So we we just need something

    that look like this, right? We need like that look like this, right? We need like
    that look like this, right? We need like

    a really rough uh or preliminary version'
  concept_slugs:
  - classifier-free-guidance
  - classifier-guidance
- idx: 50
  start_sec: 2587.589
  end_sec: 2658.0
  text: 'a really rough uh or preliminary version a really rough uh or preliminary
    version

    of what we want to generate. But the of what we want to generate. But the of what
    we want to generate. But the

    problem is that we don''t we don''t we problem is that we don''t we don''t we
    problem is that we don''t we don''t we

    don''t really have that either, right? don''t really have that either, right?
    don''t really have that either, right?

    Or or do we What do we think? What do we Or or do we What do we think? What do
    we Or or do we What do we think? What do we

    think? think? think?

    Do we >> added noise back when you saw the >> added noise back when you saw the

    original one to go back? Then you would original one to go back? Then you would
    original one to go back? Then you would

    have something more similar. have something more similar. have something more
    similar.

    >> Um, not even that. Like it''s it''s like >> Um, not even that. Like it''s it''s
    like >> Um, not even that. Like it''s it''s like

    the answer is like not model related at the answer is like not model related at
    the answer is like not model related at

    all. It''s like a super simple thing to all. It''s like a super simple thing to
    all. It''s like a super simple thing to

    do. All right. How about we just draw one, right. How about we just draw one,

    right? Like right? Like right? Like

    we don''t really need like the like we don''t really need like the like we don''t
    really need like the like

    because we really don''t need the exact because we really don''t need the exact
    because we really don''t need the exact

    like image, right? We can just like draw like image, right? We can just like draw
    like image, right? We can just like draw

    a random like sketch or like a stroke a random like sketch or like a stroke a
    random like sketch or like a stroke

    painting I guess and then and then use painting I guess and then and then use
    painting I guess and then and then use

    that as x0ero. How about that? that as x0ero. How about that?'
  concept_slugs:
  - classifier-free-guidance
  - classifier-guidance
- idx: 51
  start_sec: 2658.0
  end_sec: 2706.15
  text: 'that as x0ero. How about that?

    It turns out you can definitely do that. It turns out you can definitely do that.
    It turns out you can definitely do that.

    So say like this is like your input and So say like this is like your input and
    So say like this is like your input and

    then you you start you start by going then you you start you start by going then
    you you start you start by going

    back some noise. back some noise. back some noise.

    This is actually not predicted noise. This is actually not predicted noise. This
    is actually not predicted noise.

    This is actually just noise. Let me let This is actually just noise. Let me let
    This is actually just noise. Let me let

    me change that me change that me change that

    noise. noise. noise.

    Okay. Okay. Okay.

    Yeah. So this is just a noise. Okay. And Yeah. So this is just a noise. Okay.
    And Yeah. So this is just a noise. Okay. And

    then you just add noise to it. And then then you just add noise to it. And then
    then you just add noise to it. And then

    you just continue on DDIM as normal. And you just continue on DDIM as normal.
    And you just continue on DDIM as normal. And

    then you would have get something that then you would have get something that
    then you would have get something that

    is very close to your drawing. is very close to your drawing. is very close to
    your drawing.

    And notice that right now we don''t need And notice that right now we don''t need
    And notice that right now we don''t need

    to go back all the way to the beginning to go back all the way to the beginning
    to go back all the way to the beginning

    anymore. Right? We just start from the anymore. Right? We just start from the
    anymore. Right? We just start from the

    middle of the diffusion with the with middle of the diffusion with the with middle
    of the diffusion with the with

    this this this sketch that we created. this this this sketch that we created.
    this this this sketch that we created.

    um swapping in as one of the x0 in the'
  concept_slugs:
  - classifier-free-guidance
  - classifier-guidance
  - ddim
- idx: 52
  start_sec: 2706.15
  end_sec: 2759.2
  text: 'um swapping in as one of the x0 in the um swapping in as one of the x0 in
    the

    middle and just just continue on middle and just just continue on middle and just
    just continue on

    diffusion as if nothing has nothing diffusion as if nothing has nothing diffusion
    as if nothing has nothing

    nothing nothing nothing

    has happened um and you would would have has happened um and you would would have
    has happened um and you would would have

    get something that look like you''re get something that look like you''re get
    something that look like you''re

    drawing but also realistic uh so this drawing but also realistic uh so this drawing
    but also realistic uh so this

    thing is called SD is also my research thing is called SD is also my research
    thing is called SD is also my research

    haha uh but uh basically what''s haha uh but uh basically what''s haha uh but
    uh basically what''s

    happening here is that um so say you happening here is that um so say you happening
    here is that um so say you

    have some yeah have some yeah have some yeah

    >> you''re good at drawing >> you''re good at drawing >> you''re good at drawing

    >> you dry yourself literally. Yeah. >> you dry yourself literally. Yeah. >> you
    dry yourself literally. Yeah.

    So this is actually something called So this is actually something called So this
    is actually something called

    image to image uh translation right >> not sure what they used they probably >>
    not sure what they used they probably

    train a model honestly but this thing is train a model honestly but this thing
    is train a model honestly but this thing is

    also training free right you don''t also training free right you don''t also training
    free right you don''t

    really need to train anything for this really need to train anything for this
    really need to train anything for this

    all you need to do is to draw something all you need to do is to draw something
    all you need to do is to draw something

    you draw a paint painting and draw some you draw a paint painting and draw some
    you draw a paint painting and draw some

    like rough ideas of like what do you like rough ideas of like what do you'
  concept_slugs:
  - classifier-free-guidance
  - classifier-guidance
- idx: 53
  start_sec: 2759.2
  end_sec: 2809.19
  text: 'like rough ideas of like what do you

    want to generate and then just like want to generate and then just like want to
    generate and then just like

    hijack the the diffusion process by hijack the the diffusion process by hijack
    the the diffusion process by

    inserting uh your input and then Add inserting uh your input and then Add inserting
    uh your input and then Add

    some noise but not all the way the noise some noise but not all the way the noise
    some noise but not all the way the noise

    to it and then just in continue on the to it and then just in continue on the
    to it and then just in continue on the

    diffus diffusion process as if nothing diffus diffusion process as if nothing
    diffus diffusion process as if nothing

    has happened and then like at the end has happened and then like at the end has
    happened and then like at the end

    you would have get a very realistic you would have get a very realistic you would
    have get a very realistic

    image >> just by just with the scaling that we >> just by just with the scaling
    that we

    added. added. added.

    >> Yeah. Yep. Yep. Nothing is changed. You >> Yeah. Yep. Yep. Nothing is changed.
    You >> Yeah. Yep. Yep. Nothing is changed. You

    don''t change your model at all. don''t change your model at all. don''t change
    your model at all.

    Basically all you do is you start at the Basically all you do is you start at
    the Basically all you do is you start at the

    middle of the diffusion and instead of middle of the diffusion and instead of
    middle of the diffusion and instead of

    using a like a model produced uh using a like a model produced uh using a like
    a model produced uh

    intermediate noisy uh example what you intermediate noisy uh example what you
    intermediate noisy uh example what you

    do is you you you create this noisy do is you you you create this noisy do is
    you you you create this noisy

    example by adding some noise to your uh example by adding some noise to your uh
    example by adding some noise to your uh

    to your input and and this way it''s'
  concept_slugs:
  - classifier-free-guidance
  - classifier-guidance
- idx: 54
  start_sec: 2809.19
  end_sec: 2855.52
  text: 'to your input and and this way it''s to your input and and this way it''s

    going to create something that like kind going to create something that like kind
    going to create something that like kind

    of look like a actual intermediate of look like a actual intermediate of look
    like a actual intermediate

    example from your model but it''s example from your model but it''s example from
    your model but it''s

    actually not. It actually has some actually not. It actually has some actually
    not. It actually has some

    information from your user input. >> Why wouldn''t it? Right. Well, like Okay,
    >> Why wouldn''t it? Right. Well, like Okay,

    so it actually has some constraints. So so it actually has some constraints. So
    so it actually has some constraints. So

    I I''m going to talk about it later I I''m going to talk about it later I I''m
    going to talk about it later

    actually. So let let''s continue and then actually. So let let''s continue and
    then actually. So let let''s continue and then

    you''re gonna we''re going to talk about you''re gonna we''re going to talk about
    you''re gonna we''re going to talk about

    it later. Um so essentially apparently it later. Um so essentially apparently
    it later. Um so essentially apparently

    this thing is actually very uh it can this thing is actually very uh it can this
    thing is actually very uh it can

    apply to many like imageto image apply to many like imageto image apply to many
    like imageto image

    translation tasks. So like like translation tasks. So like like translation tasks.
    So like like

    surprisingly versatile. Uh so surprisingly versatile. Uh so surprisingly versatile.
    Uh so

    essentially what you can do you can do a essentially what you can do you can do
    a essentially what you can do you can do a

    stroke painting to image. So you just stroke painting to image. So you just stroke
    painting to image. So you just

    have like a few stroke paintings. Uh and have like a few stroke paintings. Uh
    and have like a few stroke paintings. Uh and

    then you can create like some realistic then you can create like some realistic
    then you can create like some realistic

    looking image from it based on your looking image from it based on your'
  concept_slugs:
  - classifier-free-guidance
  - classifier-guidance
- idx: 55
  start_sec: 2855.52
  end_sec: 2894.16
  text: 'looking image from it based on your

    pre-trained diffusion model and say like pre-trained diffusion model and say like
    pre-trained diffusion model and say like

    you dislike the gray sky of um you dislike the gray sky of um you dislike the
    gray sky of um

    Pittsburgh. You''re really sick of it Pittsburgh. You''re really sick of it Pittsburgh.
    You''re really sick of it

    like and you just like really dislike like and you just like really dislike like
    and you just like really dislike

    this winter weather you know just uh you this winter weather you know just uh
    you this winter weather you know just uh you

    know very uh let''s just say it''s a very know very uh let''s just say it''s a
    very know very uh let''s just say it''s a very

    valid feeling here. Uh then you can just valid feeling here. Uh then you can just
    valid feeling here. Uh then you can just

    add some blue strokes on the sky and add some blue strokes on the sky and add
    some blue strokes on the sky and

    then it become blue sky with some then it become blue sky with some then it become
    blue sky with some

    clouds. It''s very nice, right? And uh clouds. It''s very nice, right? And uh
    clouds. It''s very nice, right? And uh

    you can also do a image com compositing, you can also do a image com compositing,
    you can also do a image com compositing,

    right? So for example, say you''re not right? So for example, say you''re not
    right? So for example, say you''re not

    good at photoshopping. Uh then what you good at photoshopping. Uh then what you
    good at photoshopping. Uh then what you

    do is you can just literally like copy do is you can just literally like copy
    do is you can just literally like copy

    and paste like your like a new hairstyle and paste like your like a new hairstyle
    and paste like your like a new hairstyle

    or like a pair of glasses on you and or like a pair of glasses on you and or like
    a pair of glasses on you and

    then the diffusion model can uh the SD then the diffusion model can uh the SD'
  concept_slugs:
  - classifier-free-guidance
  - classifier-guidance
- idx: 56
  start_sec: 2894.16
  end_sec: 2939.589
  text: 'then the diffusion model can uh the SD

    is going to generate something that''s is going to generate something that''s
    is going to generate something that''s

    realistic looking but with the correct realistic looking but with the correct
    realistic looking but with the correct

    edit. Yeah. um for the showbase editing. edit. Yeah. um for the showbase editing.
    edit. Yeah. um for the showbase editing.

    >> Yes. >> Yes. >> Yes.

    >> Is it correct or assume there''s no >> Is it correct or assume there''s no
    >> Is it correct or assume there''s no

    guarantee that the model is also not guarantee that the model is also not guarantee
    that the model is also not

    going to modify like other parts of the going to modify like other parts of the
    going to modify like other parts of the

    >> It''s a great question. It''s actually >> It''s a great question. It''s actually
    >> It''s a great question. It''s actually

    there is guarantee because for the there is guarantee because for the there is
    guarantee because for the

    editing all of the editing things uh you editing all of the editing things uh
    you editing all of the editing things uh you

    will have to apply a mask. So what you will have to apply a mask. So what you
    will have to apply a mask. So what you

    do is you basically you first uh do your do is you basically you first uh do your
    do is you basically you first uh do your

    normal diffusion and then you revert the normal diffusion and then you revert
    the normal diffusion and then you revert the

    changes of the parts that you do not changes of the parts that you do not changes
    of the parts that you do not

    want to change with a mask. want to change with a mask. want to change with a
    mask.

    between between between

    you need to have some buffers between you need to have some buffers between you
    need to have some buffers between

    the unmasked and the mass partah but the unmasked and the mass partah but the
    unmasked and the mass partah but

    yeah let''s let''s look at an example so yeah let''s let''s look at an example
    so yeah let''s let''s look at an example so

    this is a very terribly masked uh image'
  concept_slugs:
  - classifier-free-guidance
  - classifier-guidance
- idx: 57
  start_sec: 2939.589
  end_sec: 2974.64
  text: 'this is a very terribly masked uh image this is a very terribly masked uh
    image

    but basically you see how like if you do but basically you see how like if you
    do but basically you see how like if you do

    general modeling research this is the general modeling research this is the general
    modeling research this is the

    thing you get to do to advisor and they thing you get to do to advisor and they
    thing you get to do to advisor and they

    can''t get mad at you just photoshop some can''t get mad at you just photoshop
    some can''t get mad at you just photoshop some

    different hairstyle for them but yeah so different hairstyle for them but yeah
    so different hairstyle for them but yeah so

    basically what I did here is I I''ve just basically what I did here is I I''ve
    just basically what I did here is I I''ve just

    like copy and paste some like random like copy and paste some like random like
    copy and paste some like random

    hairstyle to rust and uh I masked out hairstyle to rust and uh I masked out hairstyle
    to rust and uh I masked out

    his face but uh and and then basically his face but uh and and then basically
    his face but uh and and then basically

    what you can see here is that like the what you can see here is that like the
    what you can see here is that like the

    the hair gets smoother and more the hair gets smoother and more the hair gets
    smoother and more

    realistic but because I didn''t really so realistic but because I didn''t really
    so realistic but because I didn''t really so

    I masked out this part of his hair as I masked out this part of his hair as I
    masked out this part of his hair as

    well so that part didn''t get changed and well so that part didn''t get changed
    and well so that part didn''t get changed and

    it''s not very smooth and if you get it''s not very smooth and if you get it''s
    not very smooth and if you get

    better masking skills than I do then better masking skills than I do then'
  concept_slugs:
  - classifier-free-guidance
  - classifier-guidance
- idx: 58
  start_sec: 2974.64
  end_sec: 3029.44
  text: 'better masking skills than I do then

    then you would have get a better um then you would have get a better um then you
    would have get a better um

    image. Yeah. like I think similar to image. Yeah. like I think similar to image.
    Yeah. like I think similar to

    that um what like what''s the extent of that um what like what''s the extent of
    that um what like what''s the extent of

    how the model can edit like create a how the model can edit like create a how
    the model can edit like create a

    good image from >> great great question >> great great question

    connects like very very strongly connects like very very strongly connects like
    very very strongly

    connected to this thing um so basically connected to this thing um so basically
    connected to this thing um so basically

    uh another thing uh that we kind of like uh another thing uh that we kind of like
    uh another thing uh that we kind of like

    discovered from uh or I guess validated discovered from uh or I guess validated
    discovered from uh or I guess validated

    I guess from uh the SD research is that I guess from uh the SD research is that
    I guess from uh the SD research is that

    basically there''s a thing called basically there''s a thing called basically
    there''s a thing called

    controllability fidelity trade-off in controllability fidelity trade-off in controllability
    fidelity trade-off in

    conditional gen conditional generation conditional gen conditional generation
    conditional gen conditional generation

    especially the ones without training. Uh especially the ones without training.
    Uh especially the ones without training. Uh

    so basically what you do is like say if so basically what you do is like say if
    so basically what you do is like say if

    you you start from like the very you you start from like the very you you start
    from like the very

    beginning of diffusion right and then beginning of diffusion right and then beginning
    of diffusion right and then

    you insert your your image there but the you insert your your image there but
    the you insert your your image there but the

    majority of the the image is going to be majority of the the image is going to
    be'
  concept_slugs:
  - classifier-free-guidance
  - classifier-guidance
- idx: 59
  start_sec: 3029.44
  end_sec: 3076.39
  text: 'majority of the the image is going to be

    noise right so you just going to noise right so you just going to noise right
    so you just going to

    generate unconditionally like normal but generate unconditionally like normal
    but generate unconditionally like normal but

    if you insert it too late then depending if you insert it too late then depending
    if you insert it too late then depending

    on how good your painting is right say on how good your painting is right say
    on how good your painting is right say

    if your painting is like really abstract if your painting is like really abstract
    if your painting is like really abstract

    then like you''re just not going to get then like you''re just not going to get
    then like you''re just not going to get

    any like you the like basically the any like you the like basically the any like
    you the like basically the

    diffusion effect is just not going to be diffusion effect is just not going to
    be diffusion effect is just not going to be

    enough for you to create a realistic enough for you to create a realistic enough
    for you to create a realistic

    image. So what you need to do is you image. So what you need to do is you image.
    So what you need to do is you

    kind of need to kind of need to kind of need to

    find a sweet spot in this trade-off that find a sweet spot in this trade-off that
    find a sweet spot in this trade-off that

    can give you like essentially um like can give you like essentially um like can
    give you like essentially um like

    enough so that your output still look enough so that your output still look enough
    so that your output still look

    like your input but also uh enough like your input but also uh enough like your
    input but also uh enough

    fidelity so that your output actually fidelity so that your output actually fidelity
    so that your output actually

    look like a real image. And uh to answer look like a real image. And uh to answer
    look like a real image. And uh to answer

    your question, basically depending on your question, basically depending on your
    question, basically depending on

    like how abstract I guess your image is,'
  concept_slugs:
  - classifier-free-guidance
  - classifier-guidance
- idx: 60
  start_sec: 3076.39
  end_sec: 3114.88
  text: 'like how abstract I guess your image is, like how abstract I guess your image
    is,

    um essentially you you will need to um essentially you you will need to um essentially
    you you will need to

    adjust like where do you start? So for adjust like where do you start? So for
    adjust like where do you start? So for

    example, if you''re just doing like uh example, if you''re just doing like uh
    example, if you''re just doing like uh

    the this the hairstyle thing and most of the this the hairstyle thing and most
    of the this the hairstyle thing and most of

    the image is already very realistic, you the image is already very realistic,
    you the image is already very realistic, you

    just need to like smooth things out, just need to like smooth things out, just
    need to like smooth things out,

    then you should start late and but if then you should start late and but if then
    you should start late and but if

    you are doing like stroke painting, then you are doing like stroke painting, then
    you are doing like stroke painting, then

    you should start earlier than that, you should start earlier than that, you should
    start earlier than that,

    right? Um so and uh I forgot to make right? Um so and uh I forgot to make right?
    Um so and uh I forgot to make

    slides for this but basically the reason slides for this but basically the reason
    slides for this but basically the reason

    why this is happening is what I talked why this is happening is what I talked
    why this is happening is what I talked

    about last class actually is that like about last class actually is that like
    about last class actually is that like

    the diffusion process did I talk about the diffusion process did I talk about
    the diffusion process did I talk about

    this wait maybe maybe I made slides for this wait maybe maybe I made slides for
    this wait maybe maybe I made slides for

    this I''m not sure actually uh oh I did this I''m not sure actually uh oh I did
    this I''m not sure actually uh oh I did

    not never mind um but basically the not never mind um but basically the'
  concept_slugs:
  - classifier-free-guidance
  - classifier-guidance
- idx: 61
  start_sec: 3114.88
  end_sec: 3164.0
  text: 'not never mind um but basically the

    reason why this is happening is that um reason why this is happening is that um
    reason why this is happening is that um

    the diffusion process the diffusion process the diffusion process

    the forward process of diffusion is uh the forward process of diffusion is uh
    the forward process of diffusion is uh

    is gradually applying is gradually applying is gradually applying

    uh highpass highpass filter. So uh highpass highpass filter. So uh highpass highpass
    filter. So

    basically what''s happening is that like basically what''s happening is that like
    basically what''s happening is that like

    it''s gonna like filtering out high it''s gonna like filtering out high it''s
    gonna like filtering out high

    filtering out lower and lower frequency filtering out lower and lower frequency
    filtering out lower and lower frequency

    of the information in your image. So at of the information in your image. So at
    of the information in your image. So at

    the beginning it''s just going to like the beginning it''s just going to like
    the beginning it''s just going to like

    blur some details which is like very blur some details which is like very blur
    some details which is like very

    very high frequency and then at the end very high frequency and then at the end
    very high frequency and then at the end

    you just lost all the information. So you just lost all the information. So you
    just lost all the information. So

    when you''re like reversing it, you when when you''re like reversing it, you when
    when you''re like reversing it, you when

    you''re reversing the process, you''re you''re reversing the process, you''re
    you''re reversing the process, you''re

    first constructing low uh frequency first constructing low uh frequency first
    constructing low uh frequency

    informations which is basically just informations which is basically just informations
    which is basically just

    like large uh chunks of colors like large uh chunks of colors like large uh chunks
    of colors

    essentially. And and then as you go in essentially. And and then as you go in
    essentially. And and then as you go in

    the reverse process, you''re able to the reverse process, you''re able to the
    reverse process, you''re able to

    reconstruct the uh the high frequency reconstruct the uh the high frequency'
  concept_slugs:
  - classifier-free-guidance
  - classifier-guidance
- idx: 62
  start_sec: 3164.0
  end_sec: 3211.2
  text: 'reconstruct the uh the high frequency

    details more and more. And this is why details more and more. And this is why
    details more and more. And this is why

    basically based on like how much detail basically based on like how much detail
    basically based on like how much detail

    you have in your image, you should you have in your image, you should you have
    in your image, you should

    choose different time steps. Um okay, choose different time steps. Um okay, choose
    different time steps. Um okay,

    any question? Yes. any question? Yes. any question? Yes.

    >> Like manually chewing >> Like manually chewing >> Like manually chewing

    back. How do you back. How do you back. How do you

    >> You literally But you literally just >> You literally But you literally just
    >> You literally But you literally just

    manually But but usually around like you manually But but usually around like
    you manually But but usually around like you

    start with if if it''s like if Yeah. start with if if it''s like if Yeah. start
    with if if it''s like if Yeah.

    literally just like you kind of eyeball literally just like you kind of eyeball
    literally just like you kind of eyeball

    it and then if it''s like really uh it and then if it''s like really uh it and
    then if it''s like really uh

    abstract then you should just start abstract then you should just start abstract
    then you should just start

    around 04 to point 6. If it''s like around 04 to point 6. If it''s like around
    04 to point 6. If it''s like

    really not abstract you just start like really not abstract you just start like
    really not abstract you just start like

    around 0 2. Um but uh I think someone around 0 2. Um but uh I think someone around
    0 2. Um but uh I think someone

    was having a question last time was like was having a question last time was like
    was having a question last time was like

    do you uh like can we train a model to do you uh like can we train a model to
    do you uh like can we train a model to

    like determine like which time step like determine like which time step'
  concept_slugs:
  - classifier-free-guidance
  - classifier-guidance
- idx: 63
  start_sec: 3211.2
  end_sec: 3257.589
  text: 'like determine like which time step

    should I go and stuff like that which is should I go and stuff like that which
    is should I go and stuff like that which is

    what you said I think this is what we what you said I think this is what we what
    you said I think this is what we

    thought about for this project but we thought about for this project but we thought
    about for this project but we

    didn''t do it so it''s going to be very didn''t do it so it''s going to be very
    didn''t do it so it''s going to be very

    useful basically just like you look at useful basically just like you look at
    useful basically just like you look at

    you can potentially train the model to you can potentially train the model to
    you can potentially train the model to

    determine like which time step you determine like which time step you determine
    like which time step you

    should go but we did not do that this is should go but we did not do that this
    is should go but we did not do that this is

    not what has been done not what has been done not what has been done

    >> for by us at least. Yeah. the same time >> uh oh yeah everything is generated
    that >> uh oh yeah everything is generated that

    that is final time step here yeah what I that is final time step here yeah what
    I that is final time step here yeah what I

    what I''m showing here is so the t0 here what I''m showing here is so the t0 here
    what I''m showing here is so the t0 here

    means the starting time of the SDI means the starting time of the SDI means the
    starting time of the SDI

    process um so basically if you start at process um so basically if you start at
    process um so basically if you start at

    time one that just means that it''s full time one that just means that it''s full
    time one that just means that it''s full

    noise and then you just do unconditional noise and then you just do unconditional
    noise and then you just do unconditional

    generation uh if you start at time zero'
  concept_slugs:
  - classifier-free-guidance
  - classifier-guidance
- idx: 64
  start_sec: 3257.589
  end_sec: 3311.99
  text: 'generation uh if you start at time zero generation uh if you start at time
    zero

    which means that there''s no diffusion at which means that there''s no diffusion
    at which means that there''s no diffusion at

    all so you just output your input. Yeah. all so you just output your input. Yeah.
    all so you just output your input. Yeah.

    Yeah. So everything here is the final Yeah. So everything here is the final Yeah.
    So everything here is the final

    sample. Yeah. some question? H can we change the some question? H can we change
    the

    number of sampling stats based on the number of sampling stats based on the number
    of sampling stats based on the

    quality? quality? quality?

    Yes. Thank you. Dang it. Today the Yes. Thank you. Dang it. Today the Yes. Thank
    you. Dang it. Today the

    questions and the answers are fire. Oh questions and the answers are fire. Oh
    questions and the answers are fire. Oh

    my god. Yes. Uh actually uh pro tip uh my god. Yes. Uh actually uh pro tip uh
    my god. Yes. Uh actually uh pro tip uh

    which is something that you should do if which is something that you should do
    if which is something that you should do if

    you''re trying to do guidance based you''re trying to do guidance based you''re
    trying to do guidance based

    conditional generation uh is that like conditional generation uh is that like
    conditional generation uh is that like

    basically you should try to like guide basically you should try to like guide
    basically you should try to like guide

    more or like you should try to like make more or like you should try to like make
    more or like you should try to like make

    the most dent uh like in the the most dent uh like in the the most dent uh like
    in the

    intermediate time steps just the same as intermediate time steps just the same
    as intermediate time steps just the same as

    what we learned from EDM actually and what we learned from EDM actually and what
    we learned from EDM actually and

    this is basically this is like what this is basically this is like what this is
    basically this is like what

    people were saying is that like at the'
  concept_slugs:
  - classifier-free-guidance
  - classifier-guidance
- idx: 65
  start_sec: 3311.99
  end_sec: 3350.63
  text: 'people were saying is that like at the people were saying is that like at
    the

    beginning of the diffusion it''s like beginning of the diffusion it''s like beginning
    of the diffusion it''s like

    really chaotic you can''t really control really chaotic you can''t really control
    really chaotic you can''t really control

    anything because it''s going to get anything because it''s going to get anything
    because it''s going to get

    noised up Anyway, um but then and at the noised up Anyway, um but then and at
    the noised up Anyway, um but then and at the

    end it''s like most of the things the end it''s like most of the things the end
    it''s like most of the things the

    structures and everything is already structures and everything is already structures
    and everything is already

    determined. So you can''t really like determined. So you can''t really like determined.
    So you can''t really like

    make so much ch changes anymore. It''s make so much ch changes anymore. It''s
    make so much ch changes anymore. It''s

    like only in the middle is where you can like only in the middle is where you
    can like only in the middle is where you can

    make the most change or like make the make the most change or like make the make
    the most change or like make the

    most meaningful changes. So this is why most meaningful changes. So this is why
    most meaningful changes. So this is why

    when you''re trying to do guidance style when you''re trying to do guidance style
    when you''re trying to do guidance style

    type of thing, you should try to do it type of thing, you should try to do it
    type of thing, you should try to do it

    uh more in the middle. And the other uh more in the middle. And the other uh more
    in the middle. And the other

    thing that you should do is you can even thing that you should do is you can even
    thing that you should do is you can even

    I think someone someone''s like someone I think someone someone''s like someone
    I think someone someone''s like someone

    mentioned this I forgot who but like mentioned this I forgot who but like mentioned
    this I forgot who but like

    basically what you can do is say you''re'
  concept_slugs:
  - classifier-free-guidance
  - classifier-guidance
- idx: 66
  start_sec: 3350.63
  end_sec: 3386.72
  text: 'basically what you can do is say you''re basically what you can do is say
    you''re

    like unhappy with your uh w with this like unhappy with your uh w with this like
    unhappy with your uh w with this

    particular x uh the this guidance that particular x uh the this guidance that
    particular x uh the this guidance that

    you got then what you can do you can you got then what you can do you can you
    got then what you can do you can

    just redo this right you can just add just redo this right you can just add just
    redo this right you can just add

    noise back and then you get another noise back and then you get another noise
    back and then you get another

    sample of xt and then you just like do sample of xt and then you just like do
    sample of xt and then you just like do

    everything again and then you can just everything again and then you can just
    everything again and then you can just

    do it like infinite number of times do it like infinite number of times do it
    like infinite number of times

    until you get to like a good uh uh until until you get to like a good uh uh until
    until you get to like a good uh uh until

    a good good sample that you like. Uh so a good good sample that you like. Uh so
    a good good sample that you like. Uh so

    basically this thing uh we were also basically this thing uh we were also basically
    this thing uh we were also

    thinking about why this is makes sense. thinking about why this is makes sense.
    thinking about why this is makes sense.

    We didn''t really write it in any paper We didn''t really write it in any paper
    We didn''t really write it in any paper

    but basically this is like sort of just but basically this is like sort of just
    but basically this is like sort of just

    imagine like kind of you have like more imagine like kind of you have like more
    imagine like kind of you have like more

    steps uh in your longriven dynamic for steps uh in your longriven dynamic for'
  concept_slugs:
  - classifier-free-guidance
  - classifier-guidance
- idx: 67
  start_sec: 3386.72
  end_sec: 3437.99
  text: 'steps uh in your longriven dynamic for

    you to reach the the good part of the of you to reach the the good part of the
    of you to reach the the good part of the of

    the distribution. But yeah, but the distribution. But yeah, but the distribution.
    But yeah, but

    basically what you can do is say you''re basically what you can do is say you''re

    unhappy with your current uh guidance, unhappy with your current uh guidance,
    unhappy with your current uh guidance,

    then you can just go back to your then you can just go back to your then you can
    just go back to your

    original noise level and then do original noise level and then do original noise
    level and then do

    everything again. And that that''s everything again. And that that''s everything
    again. And that that''s

    usually going to improve the quality of usually going to improve the quality of
    usually going to improve the quality of

    both your uh sample and also the both your uh sample and also the both your uh
    sample and also the

    condition the like the the guidance. condition the like the the guidance. condition
    the like the the guidance.

    Okay. Okay.

    Yeah. So uh so this is like basically Yeah. So uh so this is like basically Yeah.
    So uh so this is like basically

    what people get uh like so this is an what people get uh like so this is an what
    people get uh like so this is an

    impainting task. So this is like when impainting task. So this is like when impainting
    task. So this is like when

    they do when they do not do any time they do when they do not do any time they
    do when they do not do any time

    traveling, they just don''t really traveling, they just don''t really traveling,
    they just don''t really

    generate a good dog. But then if you do generate a good dog. But then if you do
    generate a good dog. But then if you do

    time traveling 20 times, you just get a time traveling 20 times, you just get
    a time traveling 20 times, you just get a

    very realistic dog instead. very realistic dog instead. very realistic dog instead.

    Okay. Okay.

    Any questions regarding guidance? Any questions regarding guidance? Any questions
    regarding guidance?

    Yeah.'
  concept_slugs:
  - classifier-free-guidance
  - classifier-guidance
- idx: 68
  start_sec: 3438.0
  end_sec: 3482.64
  text: 'Yeah.

    Could you speak to like theoretical like Could you speak to like theoretical like
    Could you speak to like theoretical like

    I understand the concept of a GAN being I understand the concept of a GAN being
    I understand the concept of a GAN being

    entirely different my that''s the closest entirely different my that''s the closest
    entirely different my that''s the closest

    thing I have to thinking of like machine thing I have to thinking of like machine
    thing I have to thinking of like machine

    translation to a similar quality of what translation to a similar quality of what
    translation to a similar quality of what

    you''ve got. Could you talk a bit about you''ve got. Could you talk a bit about
    you''ve got. Could you talk a bit about

    the differences there? the differences there? the differences there?

    >> Yeah. Yeah, that''s actually a great >> Yeah. Yeah, that''s actually a great
    >> Yeah. Yeah, that''s actually a great

    question. So, uh the SDEID paper that we question. So, uh the SDEID paper that
    we question. So, uh the SDEID paper that we

    did was actually at the tail end of the did was actually at the tail end of the
    did was actually at the tail end of the

    Gan era. So all of our baselines were Gan era. So all of our baselines were Gan
    era. So all of our baselines were

    comparing to GANs and that particular comparing to GANs and that particular comparing
    to GANs and that particular

    task basically you try to do training task basically you try to do training task
    basically you try to do training

    free image to image translation is like free image to image translation is like
    free image to image translation is like

    GAN is like pretty much completely GAN is like pretty much completely GAN is like
    pretty much completely

    fails. It''s just like cannot do. So this fails. It''s just like cannot do. So
    this fails. It''s just like cannot do. So this

    is actually is actually is actually

    >> it''s not training free right that''s the >> it''s not training free right
    that''s the >> it''s not training free right that''s the

    problem. Yeah, like if you do not train problem. Yeah, like if you do not train'
  concept_slugs:
  - classifier-free-guidance
  - classifier-guidance
- idx: 69
  start_sec: 3482.64
  end_sec: 3525.04
  text: 'problem. Yeah, like if you do not train

    for this particular task, you just try for this particular task, you just try
    for this particular task, you just try

    to use your pre-trained unconditional to use your pre-trained unconditional to
    use your pre-trained unconditional

    model, GANs basically just fails. Like model, GANs basically just fails. Like
    model, GANs basically just fails. Like

    no matter what you try to like like a no matter what you try to like like a no
    matter what you try to like like a

    lot of people try to do like the initial lot of people try to do like the initial
    lot of people try to do like the initial

    noise uh optimizations and everything noise uh optimizations and everything noise
    uh optimizations and everything

    and it just doesn''t it just does not and it just doesn''t it just does not and
    it just doesn''t it just does not

    work well at all. Um yeah, so this is work well at all. Um yeah, so this is work
    well at all. Um yeah, so this is

    actually a pretty unique perk for actually a pretty unique perk for actually a
    pretty unique perk for

    diffusion based uh models. Okay. Okay. diffusion based uh models. Okay. Okay.
    diffusion based uh models. Okay. Okay.

    Um what do we do if a condition is not Um what do we do if a condition is not
    Um what do we do if a condition is not

    differentiable? differentiable? differentiable?

    Great question. Um we''re not gonna talk Great question. Um we''re not gonna talk
    Great question. Um we''re not gonna talk

    about it. Are we gonna talk? We''re not about it. Are we gonna talk? We''re not
    about it. Are we gonna talk? We''re not

    gonna talk about it this time. Um but gonna talk about it this time. Um but gonna
    talk about it this time. Um but

    basically um there are research that is basically um there are research that is
    basically um there are research that is

    trying to you can either like trying to you can either like trying to you can
    either like

    approximate it or you can do like like a approximate it or you can do like like
    a approximate it or you can do like like a

    search based thing like Monte Carlo search based thing like Monte Carlo'
  concept_slugs:
  - classifier-free-guidance
  - classifier-guidance
- idx: 70
  start_sec: 3525.04
  end_sec: 3572.319
  text: 'search based thing like Monte Carlo

    research type of type of style type of research type of type of style type of
    research type of type of style type of

    thing or you can use like a like like thing or you can use like a like like thing
    or you can use like a like like

    what I said before I guess a reward what I said before I guess a reward what I
    said before I guess a reward

    model to approximate what is happening. model to approximate what is happening.
    model to approximate what is happening.

    Um so yeah so there are multiple ways Um so yeah so there are multiple ways Um
    so yeah so there are multiple ways

    we''re not going to talk about this today we''re not going to talk about this
    today we''re not going to talk about this today

    unfortunately. Um and actually um the unfortunately. Um and actually um the unfortunately.
    Um and actually um the

    paper that I am participating not really paper that I am participating not really
    paper that I am participating not really

    a lead author by any by any means um a lead author by any by any means um a lead
    author by any by any means um

    uh is actually what is doing this kind uh is actually what is doing this kind
    uh is actually what is doing this kind

    of search thing and it''s like a of search thing and it''s like a of search thing
    and it''s like a

    flow-based model and yeah so you can do flow-based model and yeah so you can do
    flow-based model and yeah so you can do

    either search either search either search

    or you can use a reward model like RHF or you can use a reward model like RHF
    or you can use a reward model like RHF

    type of thing to to approximate it using type of thing to to approximate it using
    type of thing to to approximate it using

    a differentiable function. Okay, any a differentiable function. Okay, any a differentiable
    function. Okay, any

    other question? other question? other question?

    Yeah. >> The the time travel only of the mask >> The the time travel only of the
    mask

    part or the other the part. part or the other the part.'
  concept_slugs:
  - classifier-free-guidance
  - classifier-guidance
- idx: 71
  start_sec: 3572.319
  end_sec: 3626.64
  text: 'part or the other the part.

    >> Oh, so like masking here meaning that >> Oh, so like masking here meaning that
    >> Oh, so like masking here meaning that

    only the mask only the part that is only the mask only the part that is only the
    mask only the part that is

    getting mass is is modified. Everything getting mass is is modified. Everything
    getting mass is is modified. Everything

    else will just get Yeah. Yeah. else will just get Yeah. Yeah. else will just get
    Yeah. Yeah.

    This is in painting. Yeah. So, okay. Any This is in painting. Yeah. So, okay.
    Any This is in painting. Yeah. So, okay. Any

    other question? other question?

    Okay. Cool. But like let''s just say that Okay. Cool. But like let''s just say
    that Okay. Cool. But like let''s just say that

    everything that we just talked about everything that we just talked about everything
    that we just talked about

    here are like just here are like just here are like just

    like very unique things that only pretty like very unique things that only pretty
    like very unique things that only pretty

    much only diffusion can do. But what if much only diffusion can do. But what if
    much only diffusion can do. But what if

    we''re just like normal people like like we''re just like normal people like like
    we''re just like normal people like like

    everyone else? We have trained an everyone else? We have trained an everyone else?
    We have trained an

    unconditional model and we have trained unconditional model and we have trained
    unconditional model and we have trained

    a conditional model just like a conditional model just like a conditional model
    just like

    normal people. Uh is there any way that normal people. Uh is there any way that
    normal people. Uh is there any way that

    we can like improve our conditional we can like improve our conditional we can
    like improve our conditional

    generation uh by leveraging both because generation uh by leveraging both because
    generation uh by leveraging both because

    we know that unconditional model learn we know that unconditional model learn
    we know that unconditional model learn

    good information. The conditional model good information. The conditional model
    good information. The conditional model

    learn good information. Uh usually learn good information. Uh usually'
  concept_slugs:
  - classifier-free-guidance
  - classifier-guidance
- idx: 72
  start_sec: 3626.64
  end_sec: 3683.839
  text: 'learn good information. Uh usually

    unconditional models can give you very unconditional models can give you very
    unconditional models can give you very

    good uh image qualities and conditional good uh image qualities and conditional
    good uh image qualities and conditional

    model can give you very good control. Uh model can give you very good control.
    Uh model can give you very good control. Uh

    can we you know combine the two models can we you know combine the two models
    can we you know combine the two models

    somehow uh and and get a better somehow uh and and get a better somehow uh and
    and get a better

    generation better conditional generation better conditional generation better
    conditional

    generation. Is it possible? generation. Is it possible? generation. Is it possible?

    What do we think? What do we think?

    >> Uh okay. Uh two people let''s both of >> Uh okay. Uh two people let''s both
    of >> Uh okay. Uh two people let''s both of

    them. Okay. >> Uh let''s think about a training freeway. >> Uh let''s think about
    a training freeway.

    Yeah. Go ahead. Yeah. Go ahead. Yeah. Go ahead.

    >> I just >> I just >> I just

    >> Yes. Amazing. Perfect answer. H. Yeah. >> Yes. Amazing. Perfect answer. H.
    Yeah. >> Yes. Amazing. Perfect answer. H. Yeah.

    So basically let''s just say that we have So basically let''s just say that we
    have So basically let''s just say that we have

    a conditional uh distribution and a conditional uh distribution and a conditional
    uh distribution and

    unconditional distribution here. So like unconditional distribution here. So like
    unconditional distribution here. So like

    the unconditional distribution is a the unconditional distribution is a the unconditional
    distribution is a

    equal weighted mixture of gausian of two equal weighted mixture of gausian of
    two equal weighted mixture of gausian of two

    modes and then your conditional modes and then your conditional modes and then
    your conditional

    distribution is just one with the modes. distribution is just one with the modes.
    distribution is just one with the modes.

    Let''s just say that right then basically Let''s just say that right then basically
    Let''s just say that right then basically

    what you can do is if you do a weighted what you can do is if you do a weighted'
  concept_slugs:
  - classifier-free-guidance
  - classifier-guidance
- idx: 73
  start_sec: 3683.839
  end_sec: 3736.71
  text: 'what you can do is if you do a weighted

    average of the two the two distributions average of the two the two distributions
    average of the two the two distributions

    what you can do is you can actually get what you can do is you can actually get
    what you can do is you can actually get

    a sharper distribution that is still a sharper distribution that is still a sharper
    distribution that is still

    concentrated on your the conditional the concentrated on your the conditional
    the concentrated on your the conditional the

    mode that you want but it''s just going mode that you want but it''s just going
    mode that you want but it''s just going

    to be sharper. It''s just going to give to be sharper. It''s just going to give
    to be sharper. It''s just going to give

    you like like like you like like like you like like like

    higher density on the thing that is like higher density on the thing that is like
    higher density on the thing that is like

    more prominent to your condition. Um yeah but but but but yeah anyway so Um yeah
    but but but but yeah anyway so

    yeah so this is this this is what we yeah so this is this this is what we yeah
    so this is this this is what we

    could do right and the reason why it could do right and the reason why it could
    do right and the reason why it

    gets kind of sharper is because like gets kind of sharper is because like gets
    kind of sharper is because like

    just imagine that you''re kind of like just imagine that you''re kind of like
    just imagine that you''re kind of like

    penalizing basically you''re like trying penalizing basically you''re like trying
    penalizing basically you''re like trying

    to like um like emphasize on the uh the to like um like emphasize on the uh the
    to like um like emphasize on the uh the

    features that the con that this features that the con that this features that
    the con that this

    particular condition has and then just particular condition has and then just
    particular condition has and then just

    like try to like uh penalize the like try to like uh penalize the like try to
    like uh penalize the

    conditions that is like that everyone'
  concept_slugs:
  - classifier-free-guidance
  - classifier-guidance
- idx: 74
  start_sec: 3736.71
  end_sec: 3780.0
  text: 'conditions that is like that everyone conditions that is like that everyone

    has, right? So, for example, like say has, right? So, for example, like say has,
    right? So, for example, like say

    you''re um say you''re trying to generate you''re um say you''re trying to generate
    you''re um say you''re trying to generate

    a like a like like a woman with a dark a like a like like a woman with a dark
    a like a like like a woman with a dark

    hair, right? Then like what this is hair, right? Then like what this is hair,
    right? Then like what this is

    doing is like it''s going to like doing is like it''s going to like doing is like
    it''s going to like

    accentuate the woman part and the dark accentuate the woman part and the dark
    accentuate the woman part and the dark

    hair part and you''re just going to like hair part and you''re just going to like
    hair part and you''re just going to like

    make everything else like less important make everything else like less important
    make everything else like less important

    and then just going to like you''re going and then just going to like you''re
    going and then just going to like you''re going

    to very concentrating on generating to very concentrating on generating to very
    concentrating on generating

    woman with dark hair. It''s just like woman with dark hair. It''s just like woman
    with dark hair. It''s just like

    very very prominent uh like features. very very prominent uh like features. very
    very prominent uh like features.

    All right. So this thing is classifier All right. So this thing is classifier
    All right. So this thing is classifier

    free guidance literally that um so what free guidance literally that um so what
    free guidance literally that um so what

    you do is you basically just like uh do you do is you basically just like uh do
    you do is you basically just like uh do

    a weighted so instead of using your a weighted so instead of using your a weighted
    so instead of using your

    conditional score solo or unconditional conditional score solo or unconditional
    conditional score solo or unconditional

    score solo you kind of just like do a score solo you kind of just like do a'
  concept_slugs:
  - classifier-free-guidance
  - classifier-guidance
- idx: 75
  start_sec: 3780.0
  end_sec: 3841.829
  text: 'score solo you kind of just like do a

    weighted mixture of of both. Uh so like weighted mixture of of both. Uh so like
    weighted mixture of of both. Uh so like

    your so basically it''s gamma is usually your so basically it''s gamma is usually
    your so basically it''s gamma is usually

    greater than one here. Uh so what you do greater than one here. Uh so what you
    do greater than one here. Uh so what you do

    is you basically just like try to like is you basically just like try to like
    is you basically just like try to like

    make the conditional features more make the conditional features more make the
    conditional features more

    prominent and make the unconditional prominent and make the unconditional prominent
    and make the unconditional

    features less prominent. Um any question is training free if you already have
    to is training free if you already have to

    train the models? That''s actually a good train the models? That''s actually a
    good train the models? That''s actually a good

    question. Do we even need to train two question. Do we even need to train two
    question. Do we even need to train two

    models? models? models?

    What do we think? What do we think? Yes. What do we think? Yes.

    >> We can just do >> We can just do >> We can just do

    unconditional run with the conditional unconditional run with the conditional
    unconditional run with the conditional

    model over here. model over here. model over here.

    >> Yeah. Yeah. Exactly. Exactly. Right. So >> Yeah. Yeah. Exactly. Exactly. Right.
    So >> Yeah. Yeah. Exactly. Exactly. Right. So

    what we could do is that ignore the what we could do is that ignore the what we
    could do is that ignore the

    conditional unconditional part. What we conditional unconditional part. What we
    conditional unconditional part. What we

    could do is we have like a pseudo could do is we have like a pseudo could do is
    we have like a pseudo

    unconditional diffusion using the same unconditional diffusion using the same
    unconditional diffusion using the same

    uh conditional distribution uh the uh conditional distribution uh the uh conditional
    distribution uh the

    diffusion model. Right? So you still diffusion model. Right? So you still diffusion
    model. Right? So you still

    have your uh input image and then you'
  concept_slugs:
  - classifier-free-guidance
  - classifier-guidance
- idx: 76
  start_sec: 3841.829
  end_sec: 3882.88
  text: 'have your uh input image and then you have your uh input image and then you

    can literally just like specify your can literally just like specify your can
    literally just like specify your

    condition to be none to be nothing to be condition to be none to be nothing to
    be condition to be none to be nothing to be

    empty string right and then you just empty string right and then you just empty
    string right and then you just

    like both inputs still into the same like both inputs still into the same like
    both inputs still into the same

    conditional diffusion models and now conditional diffusion models and now conditional
    diffusion models and now

    instead of having like some specified instead of having like some specified instead
    of having like some specified

    condition the condition will just be condition the condition will just be condition
    the condition will just be

    nothing. You use empty string right and nothing. You use empty string right and
    nothing. You use empty string right and

    then you can still get a unconditional then you can still get a unconditional
    then you can still get a unconditional

    generation out of it u if you train it generation out of it u if you train it
    generation out of it u if you train it

    correct. Yeah, correct. Yeah, correct. Yeah,

    >> like you still need a model that can >> like you still need a model that can
    >> like you still need a model that can

    like ingest these two modalities like ingest these two modalities like ingest
    these two modalities

    >> modality. No, >> modality. No, >> modality. No,

    >> it should be able to take it as >> it should be able to take it as >> it should
    be able to take it as

    >> uh uh yeah. So, so now it''s just a >> uh uh yeah. So, so now it''s just a
    >> uh uh yeah. So, so now it''s just a

    normal conditional. Yeah. So, you will normal conditional. Yeah. So, you will
    normal conditional. Yeah. So, you will

    need to do the normal thing now. So, need to do the normal thing now. So, need
    to do the normal thing now. So,

    you''ll have to have both the te the you''ll have to have both the te the'
  concept_slugs:
  - classifier-free-guidance
  - classifier-guidance
- idx: 77
  start_sec: 3882.88
  end_sec: 3926.87
  text: 'you''ll have to have both the te the

    image and then the text and then extract image and then the text and then extract
    image and then the text and then extract

    the feature. But like so this is just to the feature. But like so this is just
    to the feature. But like so this is just to

    say that like we can have a pseudo say that like we can have a pseudo say that
    like we can have a pseudo

    unconditional model by like just unconditional model by like just unconditional
    model by like just

    changing the text into an empty string. changing the text into an empty string.
    changing the text into an empty string.

    Okay. Okay. Why empty V as using zero? Okay. Okay. Why empty V as using zero?
    Okay. Okay. Why empty V as using zero?

    Uh you can like actually define this to Uh you can like actually define this to
    Uh you can like actually define this to

    be anything. Um so for example, if you be anything. Um so for example, if you
    be anything. Um so for example, if you

    are using a class label condition, uh if are using a class label condition, uh
    if are using a class label condition, uh if

    you''re doing class label condition, then you''re doing class label condition,
    then you''re doing class label condition, then

    it could be all zero, right? Because it could be all zero, right? Because it could
    be all zero, right? Because

    it''s none of the class, right? So just it''s none of the class, right? So just
    it''s none of the class, right? So just

    one whole vector become all zero. That''s one whole vector become all zero. That''s
    one whole vector become all zero. That''s

    fine. But usually um empty string will fine. But usually um empty string will
    fine. But usually um empty string will

    be more stable especially if you''re be more stable especially if you''re be more
    stable especially if you''re

    using like a more complicated like text using like a more complicated like text
    using like a more complicated like text

    in uh encoder because you will first try in uh encoder because you will first
    try in uh encoder because you will first try

    to like map your text into some feature'
  concept_slugs:
  - classifier-free-guidance
  - classifier-guidance
- idx: 78
  start_sec: 3926.87
  end_sec: 3969.28
  text: 'to like map your text into some feature to like map your text into some feature

    space and this feature extractor could space and this feature extractor could
    space and this feature extractor could

    be like some clip or some like language be like some clip or some like language
    be like some clip or some like language

    models right so like if you just do all models right so like if you just do all
    models right so like if you just do all

    zero it may not be numerically stable so zero it may not be numerically stable
    so zero it may not be numerically stable so

    you should use like you should still you should use like you should still you
    should use like you should still

    encode something and that that that''s encode something and that that that''s
    encode something and that that that''s

    something you just empty string or you something you just empty string or you
    something you just empty string or you

    can like actually hardcode a like a can like actually hardcode a like a can like
    actually hardcode a like a

    non-condition, that''s fine, too. But non-condition, that''s fine, too. But non-condition,
    that''s fine, too. But

    basically, you just like you you could basically, you just like you you could
    basically, you just like you you could

    uh just like use the same model to to do uh just like use the same model to to
    do uh just like use the same model to to do

    both conditional and unconditional uh both conditional and unconditional uh both
    conditional and unconditional uh

    like generation as long as you include like generation as long as you include
    like generation as long as you include

    the unconditional like conditions in the unconditional like conditions in the
    unconditional like conditions in

    your training and that''s fine, right? Um your training and that''s fine, right?
    Um your training and that''s fine, right? Um

    so basically classifier free guidance is so basically classifier free guidance
    is so basically classifier free guidance is

    able to like like I said, right? So like able to like like I said, right? So like
    able to like like I said, right? So like

    it''s uh it it just gets you like clearer it''s uh it it just gets you like clearer'
  concept_slugs:
  - classifier-free-guidance
  - classifier-guidance
- idx: 79
  start_sec: 3969.28
  end_sec: 4015.349
  text: 'it''s uh it it just gets you like clearer

    features and this is why it it actually features and this is why it it actually
    features and this is why it it actually

    just like usually gives you like more uh just like usually gives you like more
    uh just like usually gives you like more uh

    desirable results and uh but like one desirable results and uh but like one desirable
    results and uh but like one

    thing that you should know is that like thing that you should know is that like
    thing that you should know is that like

    because because because

    because we have the controllability because we have the controllability because
    we have the controllability

    fidelity tradeoff, right? So just fidelity tradeoff, right? So just fidelity tradeoff,
    right? So just

    imagine that you push like this gamma to imagine that you push like this gamma
    to imagine that you push like this gamma to

    all the way to infinite, right? Then all the way to infinite, right? Then all
    the way to infinite, right? Then

    this thing will just be completely this thing will just be completely this thing
    will just be completely

    broken, right? So this gamma like this broken, right? So this gamma like this
    broken, right? So this gamma like this

    classifier free guidance scale also need classifier free guidance scale also need
    classifier free guidance scale also need

    to be tuned uh in practice and yeah and to be tuned uh in practice and yeah and
    to be tuned uh in practice and yeah and

    then uh in next class uh in in in the in then uh in next class uh in in in the
    in then uh in next class uh in in in the in

    the class after max class we''re going to the class after max class we''re going
    to the class after max class we''re going to

    talk about essentially like how do we talk about essentially like how do we talk
    about essentially like how do we

    use this in the text condition model and use this in the text condition model
    and use this in the text condition model and

    it''s actually also very interesting. Um it''s actually also very interesting.
    Um it''s actually also very interesting. Um

    but all right now you know how to turn'
  concept_slugs:
  - classifier-free-guidance
  - classifier-guidance
- idx: 80
  start_sec: 4015.349
  end_sec: 4059.91
  text: 'but all right now you know how to turn but all right now you know how to
    turn

    an unconditional model into a an unconditional model into a an unconditional model
    into a

    conditional one. Congratulations. So conditional one. Congratulations. So conditional
    one. Congratulations. So

    like if you want to train models, you like if you want to train models, you like
    if you want to train models, you

    can do classifier guidance or uh if you can do classifier guidance or uh if you
    can do classifier guidance or uh if you

    haven''t trained your conditional model haven''t trained your conditional model
    haven''t trained your conditional model

    yet, train your conditional model so yet, train your conditional model so yet,
    train your conditional model so

    that you can do classifier free that you can do classifier free that you can do
    classifier free

    guidance. Uh and but you can also choose guidance. Uh and but you can also choose
    guidance. Uh and but you can also choose

    to not train anything and do uh to not train anything and do uh to not train anything
    and do uh

    diffusion posterior sampling uh the diffusion posterior sampling uh the diffusion
    posterior sampling uh the

    manifold thing or SDEit or if you manifold thing or SDEit or if you manifold thing
    or SDEit or if you

    already have a conditional model just already have a conditional model just already
    have a conditional model just

    feel free to use classifier free feel free to use classifier free feel free to
    use classifier free

    guidance and it''s usually going to give guidance and it''s usually going to give
    guidance and it''s usually going to give

    you better result with the correct you better result with the correct you better
    result with the correct

    scale. Okay. Um, so in the next two scale. Okay. Um, so in the next two scale.
    Okay. Um, so in the next two

    weeks we''re gonna be going to the realm weeks we''re gonna be going to the realm
    weeks we''re gonna be going to the realm

    of the soda methods. Yay, finally. Um, of the soda methods. Yay, finally. Um,
    of the soda methods. Yay, finally. Um,

    so next class we''re gonna just hear from so next class we''re gonna just hear
    from so next class we''re gonna just hear from

    Max. Please come to come in person. If'
  concept_slugs:
  - classifier-free-guidance
  - classifier-guidance
- idx: 81
  start_sec: 4059.91
  end_sec: 4098.4
  text: 'Max. Please come to come in person. If Max. Please come to come in person.
    If

    you want to ask questions, it''s going to you want to ask questions, it''s going
    to you want to ask questions, it''s going to

    be really fun. I promise. Uh, and then be really fun. I promise. Uh, and then
    be really fun. I promise. Uh, and then

    the Thursday we''re going to be talking the Thursday we''re going to be talking
    the Thursday we''re going to be talking

    about text to image models and uh, how about text to image models and uh, how
    about text to image models and uh, how

    to make your model quality sota or at to make your model quality sota or at to
    make your model quality sota or at

    least this is what people think that least this is what people think that least
    this is what people think that

    that that they do that they do. And uh that that they do that they do. And uh
    that that they do that they do. And uh

    uh in the following week we''re going to uh in the following week we''re going
    to uh in the following week we''re going to

    be talking about essentially how to make be talking about essentially how to make
    be talking about essentially how to make

    your model like just like like lightning your model like just like like lightning
    your model like just like like lightning

    fast like just like how to sample from fast like just like how to sample from
    fast like just like how to sample from

    these like iterative uh uh sampling these like iterative uh uh sampling these
    like iterative uh uh sampling

    procedures with only one step. Is it procedures with only one step. Is it procedures
    with only one step. Is it

    even possible? Then we''re going to do it even possible? Then we''re going to
    do it even possible? Then we''re going to do it

    by using something like distillation. by using something like distillation. by
    using something like distillation.

    And then the the final class in the next And then the the final class in the next
    And then the the final class in the next

    is not final class but like the the is not final class but like the the'
  concept_slugs:
  - classifier-free-guidance
  - classifier-guidance
  - image-generation
- idx: 82
  start_sec: 4098.4
  end_sec: 4130.759
  text: 'is not final class but like the the

    fourth class in the next two weeks we''re fourth class in the next two weeks we''re
    fourth class in the next two weeks we''re

    going to be hearing from uh Alex who''s going to be hearing from uh Alex who''s
    going to be hearing from uh Alex who''s

    from Luma and this is like a video from Luma and this is like a video from Luma
    and this is like a video

    generation startup and they are they''re generation startup and they are they''re
    generation startup and they are they''re

    doing like meme meme machines type of doing like meme meme machines type of doing
    like meme meme machines type of

    things. So yeah it''s going to be really things. So yeah it''s going to be really
    things. So yeah it''s going to be really

    fun as well I think. Um yeah but uh fun as well I think. Um yeah but uh fun as
    well I think. Um yeah but uh

    that''s it for today''s class. that''s it for today''s class. that''s it for today''s
    class.

    Yeah. So Yeah. So Yeah. So

    yeah class is over. Let me know if yeah class is over. Let me know if yeah class
    is over. Let me know if

    there''s any remaining questions. Thank there''s any remaining questions. Thank
    there''s any remaining questions. Thank

    you guys for coming in this weather. you guys for coming in this weather. you
    guys for coming in this weather.

    Bye people on Zoom.'
  concept_slugs:
  - classifier-free-guidance
  - classifier-guidance
---
# CMU 10799 S26: Lecture 7 - Guidance & Controllable Generation - Diffusion & Flow Matching

See the structured chunks above.
