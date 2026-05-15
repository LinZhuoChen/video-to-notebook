---
course_slug: cmu-10799-diffusion-flow
idx: 12
title: 'CMU 10799 S26: Lecture 13 - Discrete Flow Matching & Edit Flow - Diffusion
  & Flow Matching'
video_url: https://www.youtube.com/watch?v=bK-LfpKLv0g
duration_sec: null
chunks:
- idx: 0
  start_sec: 3.35
  end_sec: 48.079
  text: 'Okay, so let''s get started. uh so far uh Okay, so let''s get started. uh
    so far uh

    our last class we have talked about you our last class we have talked about you
    our last class we have talked about you

    know two ways to do discrete diffusion know two ways to do discrete diffusion
    know two ways to do discrete diffusion

    like the first one is like we do the like the first one is like we do the like
    the first one is like we do the

    categorical noise and then d noiseis and categorical noise and then d noiseis
    and categorical noise and then d noiseis and

    that''s corresponding to basically the that''s corresponding to basically the
    that''s corresponding to basically the

    ddpm formulation of continuous diffusion ddpm formulation of continuous diffusion
    ddpm formulation of continuous diffusion

    and we also talk about like the score and we also talk about like the score and
    we also talk about like the score

    matching you know formulation of matching you know formulation of matching you
    know formulation of

    or equivalence of the uh discrete or equivalence of the uh discrete or equivalence
    of the uh discrete

    diffusion and uh we haven''t talked about diffusion and uh we haven''t talked
    about diffusion and uh we haven''t talked about

    the flow matching equivalence Uh so this the flow matching equivalence Uh so this
    the flow matching equivalence Uh so this

    is what we''re going to talk about today. is what we''re going to talk about today.
    is what we''re going to talk about today.

    Okay. And then you may have noticed that Okay. And then you may have noticed that
    Okay. And then you may have noticed that

    I wear the meta shirt again and meta I wear the meta shirt again and meta I wear
    the meta shirt again and meta

    hat. Uh well this is because the this hat. Uh well this is because the this hat.
    Uh well this is because the this

    thing well some of it come from meta thing well some of it come from meta thing
    well some of it come from meta

    again from the same flow matching team. again from the same flow matching team.
    again from the same flow matching team.

    Okay. Uh so this is just like a quick Okay. Uh so this is just like a quick'
  concept_slugs:
  - discrete-diffusion
  - flow-matching
  - rectified-flow
- idx: 1
  start_sec: 48.079
  end_sec: 99.749
  text: 'Okay. Uh so this is just like a quick

    like reminder of like like reminder of like like reminder of like

    what happened next last class. So what happened next last class. So what happened
    next last class. So

    basically we talked about how to add basically we talked about how to add basically
    we talked about how to add

    noise to text and how to represent it in noise to text and how to represent it
    in noise to text and how to represent it in

    like a vector slash uh matrix form and like a vector slash uh matrix form and
    like a vector slash uh matrix form and

    how we can build a diffusionesque uh how we can build a diffusionesque uh how
    we can build a diffusionesque uh

    forward process with this like you know forward process with this like you know
    forward process with this like you know

    vector and matrix representation of the vector and matrix representation of the
    vector and matrix representation of the

    text and trans transformation. Uh and text and trans transformation. Uh and text
    and trans transformation. Uh and

    then we can train it using the same uh then we can train it using the same uh
    then we can train it using the same uh

    you know elbow loss from uh DDPM you know elbow loss from uh DDPM you know elbow
    loss from uh DDPM

    essentially. And uh we also talked about essentially. And uh we also talked about
    essentially. And uh we also talked about

    how we can define the discrete score how we can define the discrete score how
    we can define the discrete score

    which is the concrete score and which is the concrete score and which is the concrete
    score and

    essentially how we can learn it uh you essentially how we can learn it uh you
    essentially how we can learn it uh you

    know using a better or like more stable know using a better or like more stable
    know using a better or like more stable

    um like loss function which is called um like loss function which is called um
    like loss function which is called

    the score entropy loss over here. And the score entropy loss over here. And the
    score entropy loss over here. And

    lastly we talked about like the easiest'
  concept_slugs:
  - discrete-diffusion
  - flow-matching
  - rectified-flow
- idx: 2
  start_sec: 99.749
  end_sec: 166.959
  text: 'lastly we talked about like the easiest lastly we talked about like the easiest

    way to do discrete diffusion which is way to do discrete diffusion which is way
    to do discrete diffusion which is

    mass diffusion uh language modeling. So mass diffusion uh language modeling. So
    mass diffusion uh language modeling. So

    basically you always you try to basically you always you try to basically you
    always you try to

    interpolate between your clean data and interpolate between your clean data and
    interpolate between your clean data and

    the full mask and then you just like try the full mask and then you just like
    try the full mask and then you just like try

    to construct a discrete diffusion model to construct a discrete diffusion model
    to construct a discrete diffusion model

    like that. Okay. So uh what is the so so like that. Okay. So uh what is the so
    so like that. Okay. So uh what is the so so

    so so far we talked about everything. Um so so far we talked about everything.
    Um so so far we talked about everything. Um

    so what is the analog analogy I guess to so what is the analog analogy I guess
    to so what is the analog analogy I guess to

    the the velocity uh in flow matching in the the velocity uh in flow matching in
    the the velocity uh in flow matching in

    our discrete setting. What do we think for real for real

    someone? someone? someone?

    >> Yeah. >> Yeah. >> Yeah.

    >> Probability part. >> Probability part. >> Probability part.

    >> The what? Sorry. >> The what? Sorry. >> The what? Sorry.

    >> The probability part. >> The probability part. >> The probability part.

    >> The the the what part? >> The the the what part? >> The the the what part?

    >> The probability part. >> The probability part.

    >> Probability part. >> Probability part.

    >> Um yeah, like on on Yes. So basically >> Um yeah, like on on Yes. So basically
    >> Um yeah, like on on Yes. So basically

    you will try you want to somehow form a you will try you want to somehow form
    a you will try you want to somehow form a

    probability path, right? to go from like probability path, right? to go from like'
  concept_slugs:
  - discrete-diffusion
  - flow-matching
  - rectified-flow
- idx: 3
  start_sec: 166.959
  end_sec: 212.879
  text: 'probability path, right? to go from like

    some noise or like some the full mass to some noise or like some the full mass
    to some noise or like some the full mass to

    clean data, right? Yeah, basically that clean data, right? Yeah, basically that
    clean data, right? Yeah, basically that

    uh and uh but yeah, let''s talk about how uh and uh but yeah, let''s talk about
    how uh and uh but yeah, let''s talk about how

    we build it, right? So, let''s first we build it, right? So, let''s first we build
    it, right? So, let''s first

    recall how we build a flow model first. recall how we build a flow model first.
    recall how we build a flow model first.

    Uh so, basically uh to build a flow Uh so, basically uh to build a flow Uh so,
    basically uh to build a flow

    model, we need uh essentially two things model, we need uh essentially two things
    model, we need uh essentially two things

    to happen, right? Basically this flow of to happen, right? Basically this flow
    of to happen, right? Basically this flow of

    probability need to conserve the mass probability need to conserve the mass probability
    need to conserve the mass

    which means that the probability should which means that the probability should
    which means that the probability should

    always add up to one right and we should always add up to one right and we should
    always add up to one right and we should

    also satisfy the continuity equation also satisfy the continuity equation also
    satisfy the continuity equation

    which means that the probability can which means that the probability can which
    means that the probability can

    only flow or change continuously but only flow or change continuously but only
    flow or change continuously but

    like these two things are kind of like like these two things are kind of like
    like these two things are kind of like

    weird right when you think about um weird right when you think about um weird
    right when you think about um

    discrete settings uh or maybe not but discrete settings uh or maybe not but discrete
    settings uh or maybe not but

    let let''s look at them in a in the let let''s look at them in a in the'
  concept_slugs:
  - discrete-diffusion
  - flow-matching
  - rectified-flow
- idx: 4
  start_sec: 212.879
  end_sec: 263.36
  text: 'let let''s look at them in a in the

    discrete settings. So last time we kind discrete settings. So last time we kind
    discrete settings. So last time we kind

    of skipped through this part uh or of skipped through this part uh or of skipped
    through this part uh or

    didn''t really talk about it in detail didn''t really talk about it in detail
    didn''t really talk about it in detail

    but like the the continuous time but like the the continuous time but like the
    the continuous time

    formulation that correspond to you know formulation that correspond to you know
    formulation that correspond to you know

    this like uh this this transformation is this like uh this this transformation
    is this like uh this this transformation is

    what we call the continuous time markoff what we call the continuous time markoff
    what we call the continuous time markoff

    chain or CTMC. So CTMC is basically just chain or CTMC. So CTMC is basically just
    chain or CTMC. So CTMC is basically just

    like we we have this like uh transition like we we have this like uh transition
    like we we have this like uh transition

    matrix at time t or like parameterized matrix at time t or like parameterized
    matrix at time t or like parameterized

    by the continuous time t. uh and then we by the continuous time t. uh and then
    we by the continuous time t. uh and then we

    can have this essentially this um can have this essentially this um can have this
    essentially this um

    transformation of probability uh get transformation of probability uh get transformation
    of probability uh get

    being expressed in this way. This is being expressed in this way. This is being
    expressed in this way. This is

    what we have seen before uh from the what we have seen before uh from the what
    we have seen before uh from the

    SEDD uh paper, right? Um but basically SEDD uh paper, right? Um but basically
    SEDD uh paper, right? Um but basically

    what it means is that like because we what it means is that like because we what
    it means is that like because we

    know that it''s a probability know that it''s a probability know that it''s a
    probability

    distribution, right? So the probability distribution, right? So the probability'
  concept_slugs:
  - discrete-diffusion
  - flow-matching
  - rectified-flow
- idx: 5
  start_sec: 263.36
  end_sec: 313.28
  text: 'distribution, right? So the probability

    the sum of the probability over all the sum of the probability over all the sum
    of the probability over all

    possible states or all possible tokens possible states or all possible tokens
    possible states or all possible tokens

    uh should equal to one right. So like uh should equal to one right. So like uh
    should equal to one right. So like

    basically from any state the probability basically from any state the probability
    basically from any state the probability

    of transition like the sum of the of transition like the sum of the of transition
    like the sum of the

    probability to transition to any state probability to transition to any state
    probability to transition to any state

    any other states or like just any states any other states or like just any states
    any other states or like just any states

    I guess or all states uh should be one. I guess or all states uh should be one.
    I guess or all states uh should be one.

    So the the conservation of mass right So the the conservation of mass right So
    the the conservation of mass right

    here uh then basically if you plug in here uh then basically if you plug in here
    uh then basically if you plug in

    everything uh you should get like everything uh you should get like everything
    uh you should get like

    basically the transition rate. So the basically the transition rate. So the basically
    the transition rate. So the

    this transition matrix basically um all this transition matrix basically um all
    this transition matrix basically um all

    the columns or all the rows depending on the columns or all the rows depending
    on the columns or all the rows depending on

    which you know convention that you that which you know convention that you that
    which you know convention that you that

    you choose to to use but basically like you choose to to use but basically like
    you choose to to use but basically like

    um you like all the all the all the um you like all the all the all the um you
    like all the all the all the

    transitions should add up to zero. And transitions should add up to zero. And'
  concept_slugs:
  - discrete-diffusion
  - flow-matching
  - rectified-flow
- idx: 6
  start_sec: 313.28
  end_sec: 369.36
  text: 'transitions should add up to zero. And

    this is like and this is literally just this is like and this is literally just
    this is like and this is literally just

    a con conversation uh conservation of a con conversation uh conservation of a
    con conversation uh conservation of

    mass. So basically it just means that mass. So basically it just means that mass.
    So basically it just means that

    like the amount of like the amount of like the amount of like the amount of like
    the amount of like the amount of

    flow that flowing out of the certain flow that flowing out of the certain flow
    that flowing out of the certain

    state should equal to the all the amount state should equal to the all the amount
    state should equal to the all the amount

    of flow that''s flow in like basically or of flow that''s flow in like basically
    or of flow that''s flow in like basically or

    or like the the opposite of that or like the the opposite of that or like the
    the opposite of that

    essentially. Yeah. Yeah. Does it make essentially. Yeah. Yeah. Does it make essentially.
    Yeah. Yeah. Does it make

    sense for people? confusion. confusion.

    >> Yeah. >> Yeah.

    >> Nearly add noise kind of in discrete >> Nearly add noise kind of in discrete
    >> Nearly add noise kind of in discrete

    setting. Do you have like a fixed setting. Do you have like a fixed setting. Do
    you have like a fixed

    sequence of like jumping from word to sequence of like jumping from word to sequence
    of like jumping from word to

    word? word? word?

    >> Yeah. So this is not like so this this >> Yeah. So this is not like so this
    this >> Yeah. So this is not like so this this

    QT thing is like a transition mixtures QT thing is like a transition mixtures
    QT thing is like a transition mixtures

    that represent a jump essentially. So that represent a jump essentially. So that
    represent a jump essentially. So

    this is like basically how much more this is like basically how much more this
    is like basically how much more

    likely that you''re going to go basically likely that you''re going to go basically'
  concept_slugs:
  - discrete-diffusion
  - flow-matching
  - rectified-flow
- idx: 7
  start_sec: 369.36
  end_sec: 423.35
  text: 'likely that you''re going to go basically

    it''s like how how how likely that you''re it''s like how how how likely that
    you''re it''s like how how how likely that you''re

    going to go jump from this state to that going to go jump from this state to that
    going to go jump from this state to that

    state. Basically this is like an state. Basically this is like an state. Basically
    this is like an

    unnormalized version of that. unnormalized version of that. unnormalized version
    of that.

    Yeah. Does it make sense? Yeah. So Yeah. Does it make sense? Yeah. So Yeah. Does
    it make sense? Yeah. So

    basically basically basically

    this this transition matrix is a jump this this transition matrix is a jump this
    this transition matrix is a jump

    and then um like basically the the and then um like basically the the and then
    um like basically the the

    infinite testimonly like you can form infinite testimonly like you can form infinite
    testimonly like you can form

    this probability distribution like this this probability distribution like this
    this probability distribution like this

    and because we want it to be a valid and because we want it to be a valid and
    because we want it to be a valid

    probability distribution. So everything probability distribution. So everything
    probability distribution. So everything

    add up to one you the you will have this add up to one you the you will have this
    add up to one you the you will have this

    like property where literally just like like property where literally just like
    like property where literally just like

    every like just like like all the all every like just like like all the all every
    like just like like all the all

    the flows will add up to zero basically. Yeah. Yeah.

    >> Represent all the jumps that you >> Represent all the jumps that you >> Represent
    all the jumps that you

    contain. contain. contain.

    >> Yeah. >> Yeah.

    >> Yeah. >> Yeah.

    So basically just like no matter how So basically just like no matter how So basically
    just like no matter how

    like so so this this QT is is the flow. like so so this this QT is is the flow.
    like so so this this QT is is the flow.

    It''s a velocity, right? Essentially. So'
  concept_slugs:
  - discrete-diffusion
  - flow-matching
  - rectified-flow
- idx: 8
  start_sec: 423.35
  end_sec: 473.12
  text: 'It''s a velocity, right? Essentially. So It''s a velocity, right? Essentially.
    So

    it''s basically just saying that like um it''s basically just saying that like
    um it''s basically just saying that like um

    all the flows will like like you will all the flows will like like you will all
    the flows will like like you will

    not create new flows like that all the not create new flows like that all the
    not create new flows like that all the

    flows will just like add up to zero. flows will just like add up to zero. flows
    will just like add up to zero.

    They''ll all cancel out essentially. Yeah, Yeah,

    >> this is represented by a matrix like for >> this is represented by a matrix
    like for >> this is represented by a matrix like for

    state transitions. It already seems like state transitions. It already seems like
    state transitions. It already seems like

    a very big matrix. a very big matrix. a very big matrix.

    >> It is. It is but like I mean okay uh >> It is. It is but like I mean okay uh
    >> It is. It is but like I mean okay uh

    that''s actually a good question and and that''s actually a good question and
    and that''s actually a good question and and

    this is also why like you will see like this is also why like you will see like
    this is also why like you will see like

    before right everyone was trying to before right everyone was trying to before
    right everyone was trying to

    represent the what they''re trying to represent the what they''re trying to represent
    the what they''re trying to

    predict as like the logit instead of the predict as like the logit instead of
    the predict as like the logit instead of the

    actual rate matrix right because the actual rate matrix right because the actual
    rate matrix right because the

    rate matrix is like quadratics of the of rate matrix is like quadratics of the
    of rate matrix is like quadratics of the of

    the of of the logit dimension right so the of of the logit dimension right so
    the of of the logit dimension right so

    this is also why we''re trying to do this is also why we''re trying to do'
  concept_slugs:
  - discrete-diffusion
  - flow-matching
  - rectified-flow
- idx: 9
  start_sec: 473.12
  end_sec: 538.16
  text: 'this is also why we''re trying to do

    reparameterization trick yeah but that''s reparameterization trick yeah but that''s
    reparameterization trick yeah but that''s

    a great question. All right. Anything a great question. All right. Anything a
    great question. All right. Anything

    else? Anyone else question? else? Anyone else question? else? Anyone else question?

    All good. All right. All right. Okay. All good. All right. All right. Okay. All
    good. All right. All right. Okay.

    So, we have uh the conservation of mass. So, we have uh the conservation of mass.
    So, we have uh the conservation of mass.

    Now, uh what is the other thing that we Now, uh what is the other thing that we
    Now, uh what is the other thing that we

    need? >> The other thing >> The other thing

    >> continuity equation, right? Okay. So, >> continuity equation, right? Okay.
    So, >> continuity equation, right? Okay. So,

    what is the continuity equation in in in what is the continuity equation in in
    in what is the continuity equation in in in

    this CTMC? Well, this thing is called this CTMC? Well, this thing is called this
    CTMC? Well, this thing is called

    the Clomograph the Clomograph the Clomograph

    equation and I just I guess this is the equation and I just I guess this is the
    equation and I just I guess this is the

    information theory people would like the information theory people would like
    the information theory people would like the

    name and stuff. uh but but essentially name and stuff. uh but but essentially
    name and stuff. uh but but essentially

    is literally uh just means that the is literally uh just means that the is literally
    uh just means that the

    infinite decimal change in probability infinite decimal change in probability
    infinite decimal change in probability

    is equal to literally the the amount of is equal to literally the the amount of
    is equal to literally the the amount of

    probability that comes into this probability that comes into this probability
    that comes into this

    particular state particular state particular state

    minus the probability that go out of minus the probability that go out of minus
    the probability that go out of

    this state that''s it right this is like this state that''s it right this is like'
  concept_slugs:
  - discrete-diffusion
  - flow-matching
  - rectified-flow
- idx: 10
  start_sec: 538.16
  end_sec: 617.44
  text: 'this state that''s it right this is like

    super uh very intuitive I hope is super uh very intuitive I hope is super uh very
    intuitive I hope is

    All good. What can we observe here? Can we write What can we observe here? Can
    we write

    this in like a easier form essentially this in like a easier form essentially
    this in like a easier form essentially

    using the things that we learned just using the things that we learned just using
    the things that we learned just

    now? Yeah. now? Yeah. now? Yeah.

    And not yet conditional, but like can we And not yet conditional, but like can
    we And not yet conditional, but like can we

    simplify this a little bit using the simplify this a little bit using the simplify
    this a little bit using the

    conservation of mass that we just conservation of mass that we just conservation
    of mass that we just

    learned? It kind of looks like it, right? If you It kind of looks like it, right?
    If you

    think about it think about it think about it

    like what what is this part? What is like what what is this part? What is like
    what what is this part? What is

    this part? So this part plus this part is zero, So this part plus this part is
    zero,

    right? But what is this part? Let''s go back. Let''s go back. So what is Let''s
    go back. Let''s go back. So what is

    So this is this right? So this is this right? So this is this right?

    So can we write it in a better form? Yeah, it will Yeah, it will

    well basically all right because like well basically all right because like well
    basically all right because like

    this negative sum thing is just qxx. So this negative sum thing is just qxx. So
    this negative sum thing is just qxx. So

    this is literally just like qxx times this is literally just like qxx times this
    is literally just like qxx times

    px. So you don''t even need the the the px. So you don''t even need the the the
    px. So you don''t even need the the the

    not equal anymore. So just sum of all not equal anymore. So just sum of all'
  concept_slugs:
  - discrete-diffusion
  - flow-matching
  - rectified-flow
- idx: 11
  start_sec: 617.44
  end_sec: 681.04
  text: 'not equal anymore. So just sum of all

    the z all the possible z''s and then qzx the z all the possible z''s and then
    qzx the z all the possible z''s and then qzx

    ptz right and z could be equal to x as ptz right and z could be equal to x as
    ptz right and z could be equal to x as

    well. So this is just literally can be well. So this is just literally can be
    well. So this is just literally can be

    written as DPT uh DT equals to QP. written as DPT uh DT equals to QP. written
    as DPT uh DT equals to QP.

    Super simple, right? Make sense? Make sense?

    Okay, cool. Uh well, this is nice Okay, cool. Uh well, this is nice Okay, cool.
    Uh well, this is nice

    because this is a OD again, right? because this is a OD again, right? because
    this is a OD again, right?

    Amazing. Just like flow matching, we get Amazing. Just like flow matching, we
    get Amazing. Just like flow matching, we get

    a simple OD again, right? So all we need a simple OD again, right? So all we need
    a simple OD again, right? So all we need

    to do now is to simulate this OD, right? to do now is to simulate this OD, right?
    to do now is to simulate this OD, right?

    In order to in order to build a In order to in order to build a In order to in
    order to build a

    trajectory on this probability path. trajectory on this probability path. trajectory
    on this probability path.

    Does it make sense? Okay. Cool. All Does it make sense? Okay. Cool. All Does it
    make sense? Okay. Cool. All

    right. So now let''s simulate a right. So now let''s simulate a right. So now
    let''s simulate a

    trajectory on the probability path. trajectory on the probability path. trajectory
    on the probability path.

    Right. So then we can have literally Right. So then we can have literally Right.
    So then we can have literally

    so this is like basically just like so this is like basically just like so this
    is like basically just like

    oiler, right? So you just get you you oiler, right? So you just get you you'
  concept_slugs:
  - discrete-diffusion
  - flow-matching
  - rectified-flow
- idx: 12
  start_sec: 681.04
  end_sec: 735.839
  text: 'oiler, right? So you just get you you

    just literally plug everything in here just literally plug everything in here
    just literally plug everything in here

    and then you''ll get this thing and the and then you''ll get this thing and the
    and then you''ll get this thing and the

    most important part that I want to say most important part that I want to say
    most important part that I want to say

    is that so this is the only thing that is that so this is the only thing that
    is that so this is the only thing that

    we need to learn right the transition we need to learn right the transition we
    need to learn right the transition

    like the transition rate from like your like the transition rate from like your
    like the transition rate from like your

    current time step to next time step. So current time step to next time step. So
    current time step to next time step. So

    this is like the quoteunquote velocity this is like the quoteunquote velocity
    this is like the quoteunquote velocity

    that we''re that we should be learning. that we''re that we should be learning.
    that we''re that we should be learning.

    Make sense? So this is the the the Make sense? So this is the the the Make sense?
    So this is the the the

    correspondence correspondence correspondence

    of the velocity thing in the full of the velocity thing in the full of the velocity
    thing in the full

    matching. matching. matching.

    Okay. So now how do we learn this thing Okay. So now how do we learn this thing
    Okay. So now how do we learn this thing

    or how do we parameterize this thing? I or how do we parameterize this thing?
    I or how do we parameterize this thing? I

    guess guess guess

    we kind of talked about it already. All right, I''ll just tell you guys the All
    right, I''ll just tell you guys the

    answer. But basically you just like you answer. But basically you just like you
    answer. But basically you just like you

    just do reparameterization again. So just do reparameterization again. So just
    do reparameterization again. So

    like the the core of the the story in like the the core of the the story in'
  concept_slugs:
  - discrete-diffusion
  - flow-matching
  - rectified-flow
- idx: 13
  start_sec: 735.839
  end_sec: 783.04
  text: 'like the the core of the the story in

    all the discrete diffusion papers is all the discrete diffusion papers is all
    the discrete diffusion papers is

    that like no matter what you do try to that like no matter what you do try to
    that like no matter what you do try to

    reparameterize your thing into like like reparameterize your thing into like like
    reparameterize your thing into like like

    some something that you can directly get some something that you can directly
    get some something that you can directly get

    from the forward process and the clean from the forward process and the clean
    from the forward process and the clean

    data estimation. It''s actually not only data estimation. It''s actually not only
    data estimation. It''s actually not only

    uh the the discrete diffusion paper. uh the the discrete diffusion paper. uh the
    the discrete diffusion paper.

    It''s actually all diffusion paper. It''s actually all diffusion paper. It''s
    actually all diffusion paper.

    Right? Basically, you just apply Right? Basically, you just apply Right? Basically,
    you just apply

    reparameterization trick and then you''ll reparameterization trick and then you''ll
    reparameterization trick and then you''ll

    get something that is like nicer to to get something that is like nicer to to
    get something that is like nicer to to

    learn. For example, like the epsilon learn. For example, like the epsilon learn.
    For example, like the epsilon

    prediction and the the or the v prediction and the the or the v prediction and
    the the or the v

    prediction, right? And in this case, prediction, right? And in this case, prediction,
    right? And in this case,

    this is literally just the x0 prediction this is literally just the x0 prediction
    this is literally just the x0 prediction

    or like the clean data prediction. or like the clean data prediction. or like
    the clean data prediction.

    Does it make sense? And the reason why Does it make sense? And the reason why
    Does it make sense? And the reason why

    we''re doing that is because a it saves we''re doing that is because a it saves
    we''re doing that is because a it saves

    dimensionality and b we can literally dimensionality and b we can literally dimensionality
    and b we can literally

    just use cross entropy to learn this, just use cross entropy to learn this,'
  concept_slugs:
  - discrete-diffusion
  - flow-matching
  - rectified-flow
- idx: 14
  start_sec: 783.04
  end_sec: 841.269
  text: 'just use cross entropy to learn this,

    right? Because we have the ground truth right? Because we have the ground truth
    right? Because we have the ground truth

    clean data. So we just need to use cross clean data. So we just need to use cross
    clean data. So we just need to use cross

    entropy on every single token. Cool. Now you get discrete flow Cool. Now you get
    discrete flow

    matching. Yay. That''s it pretty much. So matching. Yay. That''s it pretty much.
    So matching. Yay. That''s it pretty much. So

    this is like kind of similar to what we this is like kind of similar to what we
    this is like kind of similar to what we

    have seen before, right? Yep. have seen before, right? Yep. have seen before,
    right? Yep.

    >> What does the prior distribution look >> What does the prior distribution look
    >> What does the prior distribution look

    like? Is it just uniform overall? like? Is it just uniform overall? like? Is it
    just uniform overall?

    >> You can you can choose, right? So you >> You can you can choose, right? So
    you >> You can you can choose, right? So you

    can choose uniform, you can choose all can choose uniform, you can choose all
    can choose uniform, you can choose all

    mask, you can choose anything just the mask, you can choose anything just the
    mask, you can choose anything just the

    same as the discrete diffusion thing. Okay. Uh but basically once we have Okay.
    Uh but basically once we have

    learned this uh network then we can try learned this uh network then we can try
    learned this uh network then we can try

    to sample from it. So how do you sample to sample from it. So how do you sample
    to sample from it. So how do you sample

    from? from? from?

    Right. So you basically first start from Right. So you basically first start from
    Right. So you basically first start from

    t equals z because you are doing full t equals z because you are doing full t
    equals z because you are doing full

    matching now. So the the time scale matching now. So the the time scale matching
    now. So the the time scale

    flips right. So you start from t t'
  concept_slugs:
  - discrete-diffusion
  - flow-matching
  - rectified-flow
- idx: 15
  start_sec: 841.269
  end_sec: 885.76
  text: 'flips right. So you start from t t flips right. So you start from t t

    equals z which and then you sample from equals z which and then you sample from
    equals z which and then you sample from

    your prior which could be uniform or all your prior which could be uniform or
    all your prior which could be uniform or all

    mask and then basically you just like mask and then basically you just like mask
    and then basically you just like

    try to integrate through the this OD or try to integrate through the this OD or
    try to integrate through the this OD or

    like just simulate try to simulate this like just simulate try to simulate this
    like just simulate try to simulate this

    OD simulate the particles on this OD simulate the particles on this OD simulate
    the particles on this

    probability path. Uh then you first probability path. Uh then you first probability
    path. Uh then you first

    calculate your uh transition rate by calculate your uh transition rate by calculate
    your uh transition rate by

    using your um by using your uh the using your um by using your uh the using your
    um by using your uh the

    learned uh uh cross entropy or logic learned uh uh cross entropy or logic learned
    uh uh cross entropy or logic

    prediction predictor you know so your prediction predictor you know so your prediction
    predictor you know so your

    model and then you can you can do that model and then you can you can do that
    model and then you can you can do that

    uh and then what you do is you sample uh and then what you do is you sample uh
    and then what you do is you sample

    you literally just sample from the you literally just sample from the you literally
    just sample from the

    categorical distribution um that is categorical distribution um that is categorical
    distribution um that is

    defined by you know the the the CTMC defined by you know the the the CTMC defined
    by you know the the the CTMC

    that we just saw before. Okay. And then that we just saw before. Okay. And then
    that we just saw before. Okay. And then

    you just increment the time and then you you just increment the time and then
    you'
  concept_slugs:
  - discrete-diffusion
  - flow-matching
  - rectified-flow
- idx: 16
  start_sec: 885.76
  end_sec: 942.079
  text: 'you just increment the time and then you

    do it over over again until you reach do it over over again until you reach do
    it over over again until you reach

    the end point. Okay, make sense? This this is actually Okay, make sense? This
    this is actually

    super similar to what we have seen super similar to what we have seen super similar
    to what we have seen

    before, right? To what we have seen last before, right? To what we have seen last
    before, right? To what we have seen last

    class. class. class.

    It''s it''s just that it''s like more It''s it''s just that it''s like more It''s
    it''s just that it''s like more

    straightforward essentially. straightforward essentially. straightforward essentially.

    >> Yeah. >> Yeah.

    >> You will still be quadratic the number >> You will still be quadratic the number
    >> You will still be quadratic the number

    of the vocabulary size, right? of the vocabulary size, right? of the vocabulary
    size, right?

    >> Yeah. >> Yeah.

    >> Does that make it difficult to predict >> Does that make it difficult to predict
    >> Does that make it difficult to predict

    such a large? No, because you are not such a large? No, because you are not such
    a large? No, because you are not

    predicting Q, right? You''re predicting predicting Q, right? You''re predicting
    predicting Q, right? You''re predicting

    P. You''re predicting Sx. And then you P. You''re predicting Sx. And then you
    P. You''re predicting Sx. And then you

    multiply by something that you can do in multiply by something that you can do
    in multiply by something that you can do in

    closed form. Yeah. Anything else? Anything else?

    Cool. You know, as you know, you guys Cool. You know, as you know, you guys Cool.
    You know, as you know, you guys

    already know this. This is the theme of already know this. This is the theme of
    already know this. This is the theme of

    gen modeling. the community just like gen modeling. the community just like gen
    modeling. the community just like

    seems to kind of you know converge on seems to kind of you know converge on seems
    to kind of you know converge on

    things that we developed somehow but things that we developed somehow but'
  concept_slugs:
  - discrete-diffusion
  - flow-matching
  - rectified-flow
- idx: 17
  start_sec: 942.079
  end_sec: 982.24
  text: 'things that we developed somehow but

    basically there are two discreful basically there are two discreful basically
    there are two discreful

    matching papers uh this time they are matching papers uh this time they are matching
    papers uh this time they are

    not published in the same conference but not published in the same conference
    but not published in the same conference but

    they''re pretty is very very similar so they''re pretty is very very similar so
    they''re pretty is very very similar so

    the ones that we were talking about was the ones that we were talking about was
    the ones that we were talking about was

    actually the first one uh so this guy is actually the first one uh so this guy
    is actually the first one uh so this guy is

    called Andrew Kempel this dude honestly called Andrew Kempel this dude honestly
    called Andrew Kempel this dude honestly

    is like so goatated he''s like he just is like so goatated he''s like he just
    is like so goatated he''s like he just

    graduated from his PhD or something and graduated from his PhD or something and
    graduated from his PhD or something and

    I really do not understand why he''s not I really do not understand why he''s
    not I really do not understand why he''s not

    like rich and famous yet. But like like rich and famous yet. But like like rich
    and famous yet. But like

    basically he um he wrote the the the basically he um he wrote the the the basically
    he um he wrote the the the

    CTMC paper that we were we''ve been CTMC paper that we were we''ve been CTMC paper
    that we were we''ve been

    talking about and he also wrote the one talking about and he also wrote the one
    talking about and he also wrote the one

    of the the discrete fo matching paper. of the the discrete fo matching paper.
    of the the discrete fo matching paper.

    Uh somehow right now he''s doing a Uh somehow right now he''s doing a Uh somehow
    right now he''s doing a

    startup or something. I I don''t really startup or something. I I don''t really
    startup or something. I I don''t really

    know but anyway it''s like really like I know but anyway it''s like really like
    I'
  concept_slugs:
  - discrete-diffusion
  - flow-matching
  - rectified-flow
- idx: 18
  start_sec: 982.24
  end_sec: 1025.27
  text: 'know but anyway it''s like really like I

    really hope this guy get rich and famous really hope this guy get rich and famous
    really hope this guy get rich and famous

    soon. Uh anyway and then the second one soon. Uh anyway and then the second one
    soon. Uh anyway and then the second one

    is the one from Meta. Um basically they is the one from Meta. Um basically they
    is the one from Meta. Um basically they

    propose something that is a little bit propose something that is a little bit
    propose something that is a little bit

    more uh gen uh like general and then more uh gen uh like general and then more
    uh gen uh like general and then

    they also do a lot more uh you know just they also do a lot more uh you know just
    they also do a lot more uh you know just

    like nice framework and then a lot of like nice framework and then a lot of like
    nice framework and then a lot of

    connections to you know the the existing connections to you know the the existing
    connections to you know the the existing

    models and stuff like that but basically models and stuff like that but basically
    models and stuff like that but basically

    there are two discrete flow matching there are two discrete flow matching there
    are two discrete flow matching

    papers that you can read and they''re all papers that you can read and they''re
    all papers that you can read and they''re all

    they''re both very nice. they''re both very nice. they''re both very nice.

    All right, cool. So we have talked about All right, cool. So we have talked about
    All right, cool. So we have talked about

    uh pretty much all three uh uh pretty much all three uh uh pretty much all three
    uh

    parameterizations today uh already. Uh parameterizations today uh already. Uh
    parameterizations today uh already. Uh

    so uh for flow matching what we do is we so uh for flow matching what we do is
    we so uh for flow matching what we do is we

    instead of learning the velocity we sort instead of learning the velocity we sort
    instead of learning the velocity we sort

    of learn the rate matrix but we don''t'
  concept_slugs:
  - discrete-diffusion
  - flow-matching
  - rectified-flow
- idx: 19
  start_sec: 1025.27
  end_sec: 1070.24
  text: 'of learn the rate matrix but we don''t of learn the rate matrix but we don''t

    actually learn the rate matrix directly actually learn the rate matrix directly
    actually learn the rate matrix directly

    we we do literally the same thing we we we do literally the same thing we we we
    do literally the same thing we

    learn the like the clean data prediction learn the like the clean data prediction
    learn the like the clean data prediction

    and then we trans and then we make it and then we trans and then we make it and
    then we trans and then we make it

    into the the rate matrix. Okay. So now into the the rate matrix. Okay. So now
    into the the rate matrix. Okay. So now

    uh are discrete diffusion models perfect uh are discrete diffusion models perfect
    uh are discrete diffusion models perfect

    now then like seems like it seems like now then like seems like it seems like
    now then like seems like it seems like

    they they they are so nice. Uh are they they they they are so nice. Uh are they
    they they they are so nice. Uh are they

    perfect? Yeah perfect? Yeah perfect? Yeah

    problem has been solved by fix. problem has been solved by fix. problem has been
    solved by fix.

    >> Yes. So I was going to get get you guys >> Yes. So I was going to get get you
    guys >> Yes. So I was going to get get you guys

    to discuss but I guess you don''t you to discuss but I guess you don''t you to
    discuss but I guess you don''t you

    don''t need time to think. Okay. Yes. Uh don''t need time to think. Okay. Yes.
    Uh don''t need time to think. Okay. Yes. Uh

    so it has fixed length problem. you you so it has fixed length problem. you you
    so it has fixed length problem. you you

    still need to like pred decide like how still need to like pred decide like how
    still need to like pred decide like how

    how long your sentence is or how long how long your sentence is or how long how
    long your sentence is or how long

    your par paragraph is in order to build your par paragraph is in order to build'
  concept_slugs:
  - discrete-diffusion
  - flow-matching
  - rectified-flow
- idx: 20
  start_sec: 1070.24
  end_sec: 1116.64
  text: 'your par paragraph is in order to build

    this model and this is just like super this model and this is just like super
    this model and this is just like super

    like not good right this is a very very like not good right this is a very very
    like not good right this is a very very

    not uh uh if like um realistic okay what not uh uh if like um realistic okay what
    not uh uh if like um realistic okay what

    else any anything else yeah else any anything else yeah else any anything else
    yeah

    >> I think they won''t handle temporal >> I think they won''t handle temporal
    >> I think they won''t handle temporal

    dependency as well as auto reggressive dependency as well as auto reggressive
    dependency as well as auto reggressive

    models because like random tokens at any models because like random tokens at
    any models because like random tokens at any

    point are getting like unmasked rather point are getting like unmasked rather
    point are getting like unmasked rather

    than than than

    >> so so the ordering like You don''t >> so so the ordering like You don''t >>
    so so the ordering like You don''t

    actually have an ordering of unmasking, actually have an ordering of unmasking,
    actually have an ordering of unmasking,

    right? Essentially. Yeah. Very good. right? Essentially. Yeah. Very good. right?
    Essentially. Yeah. Very good.

    What else? What else? What else?

    What about uh how about on like the What about uh how about on like the What about
    uh how about on like the

    efficient efficiency side? What do we efficient efficiency side? What do we efficient
    efficiency side? What do we

    think? It''s supposed to be very good, think? It''s supposed to be very good,
    think? It''s supposed to be very good,

    but would it be actually very good in but would it be actually very good in but
    would it be actually very good in

    real life? What do we think? real life? What do we think? real life? What do we
    think?

    >> Short answer. Yeah. Yeah. Yeah. So, so >> Short answer. Yeah. Yeah. Yeah. So,
    so >> Short answer. Yeah. Yeah. Yeah. So, so

    like it''s the same problem as the fixed like it''s the same problem as the fixed'
  concept_slugs:
  - discrete-diffusion
  - flow-matching
  - rectified-flow
- idx: 21
  start_sec: 1116.64
  end_sec: 1160.07
  text: 'like it''s the same problem as the fixed

    length thing, right? Yeah. length thing, right? Yeah. length thing, right? Yeah.

    >> I heard this from like who''s doing >> I heard this from like who''s doing
    >> I heard this from like who''s doing

    something in this. So, like if you want something in this. So, like if you want
    something in this. So, like if you want

    to generate two words at the same time. to generate two words at the same time.
    to generate two words at the same time.

    Then these ones can''t tell the Then these ones can''t tell the Then these ones
    can''t tell the

    difference between New York and San difference between New York and San difference
    between New York and San

    Francisco, New San Francisco. Francisco, New San Francisco. Francisco, New San
    Francisco.

    >> Ah, wait. That''s actually that''s >> Ah, wait. That''s actually that''s >>
    Ah, wait. That''s actually that''s

    actually so but this is kind of similar actually so but this is kind of similar
    actually so but this is kind of similar

    to like the unmasking ordering problem, to like the unmasking ordering problem,
    to like the unmasking ordering problem,

    right? That''s that''s a good one. Anyone right? That''s that''s a good one. Anyone
    right? That''s that''s a good one. Anyone

    else? else? else?

    There''s there''s one that is like I guess There''s there''s one that is like
    I guess There''s there''s one that is like I guess

    not very obvious, but it''s related to not very obvious, but it''s related to
    not very obvious, but it''s related to

    efficiency. And uh if you have you know efficiency. And uh if you have you know
    efficiency. And uh if you have you know

    ever implemented LM it''s like it''s like ever implemented LM it''s like it''s
    like ever implemented LM it''s like it''s like

    a very very important thing. YEAH. a very very important thing. YEAH. a very very
    important thing. YEAH.

    >> KV CACHING. >> KV CACHING. >> KV CACHING.

    >> YEAH. YEAH. KV caching right. It''s not >> YEAH. YEAH. KV caching right. It''s
    not >> YEAH. YEAH. KV caching right. It''s not

    possible to do KV caching right now. All possible to do KV caching right now.
    All possible to do KV caching right now. All

    right. So let''s take a look at it. Uh'
  concept_slugs:
  - discrete-diffusion
  - flow-matching
  - rectified-flow
- idx: 22
  start_sec: 1160.07
  end_sec: 1197.36
  text: 'right. So let''s take a look at it. Uh right. So let''s take a look at it.
    Uh

    yeah. So essentially variable length you yeah. So essentially variable length
    you yeah. So essentially variable length you

    still can''t do variable length still can''t do variable length still can''t do
    variable length

    generation. Uh the model has to use generation. Uh the model has to use generation.
    Uh the model has to use

    birectional attention because you do not birectional attention because you do
    not birectional attention because you do not

    know like where your context is right. know like where your context is right.
    know like where your context is right.

    It can come from before you. It come It can come from before you. It come It can
    come from before you. It come

    from after you. You don''t know. So you from after you. You don''t know. So you
    from after you. You don''t know. So you

    need a full attention. So you cannot do need a full attention. So you cannot do
    need a full attention. So you cannot do

    KV caching. Uh and then also you don''t KV caching. Uh and then also you don''t
    KV caching. Uh and then also you don''t

    really know well like basically you really know well like basically you really
    know well like basically you

    don''t really have like a ordering. So don''t really have like a ordering. So
    don''t really have like a ordering. So

    you kind of just like depending on uh you kind of just like depending on uh you
    kind of just like depending on uh

    the model to uh to kind of figure it out the model to uh to kind of figure it
    out the model to uh to kind of figure it out

    and it can h like basically things like and it can h like basically things like
    and it can h like basically things like

    new Francisco can happen, right? And new Francisco can happen, right? And new
    Francisco can happen, right? And

    then the last thing is like not then the last thing is like not then the last
    thing is like not

    necessarily like a drawback but more of necessarily like a drawback but more of
    necessarily like a drawback but more of

    like something that we can think about, like something that we can think about,'
  concept_slugs:
  - discrete-diffusion
  - flow-matching
  - rectified-flow
- idx: 23
  start_sec: 1197.36
  end_sec: 1256.23
  text: 'like something that we can think about,

    right? And it''s like now we have like right? And it''s like now we have like
    right? And it''s like now we have like

    two um like frameworks that like sort of two um like frameworks that like sort
    of two um like frameworks that like sort of

    like just like really really well like just like really really well like just
    like really really well

    connected. Uh can we make them together connected. Uh can we make them together
    connected. Uh can we make them together

    like can we merge them together? Can we like can we merge them together? Can we
    like can we merge them together? Can we

    make something that is like you know make something that is like you know make
    something that is like you know

    that''s naturally multimodel and stuff that''s naturally multimodel and stuff
    that''s naturally multimodel and stuff

    like that right? Uh okay so let''s fix like that right? Uh okay so let''s fix
    like that right? Uh okay so let''s fix

    them one by one essentially. them one by one essentially. them one by one essentially.

    All right how would you generate a All right how would you generate a All right
    how would you generate a

    variable length paragraph? Okay, so variable length paragraph? Okay, so variable
    length paragraph? Okay, so

    obviously you can use a lm to generate obviously you can use a lm to generate
    obviously you can use a lm to generate

    everything auto reggressively, right? So everything auto reggressively, right?
    So everything auto reggressively, right? So

    basically you just insert uh one token basically you just insert uh one token
    basically you just insert uh one token

    at a time at the end of the sentence, at a time at the end of the sentence, at
    a time at the end of the sentence,

    right? right? right?

    Is there any other way to do that? Oh, you can do multi token, but you Oh, you
    can do multi token, but you

    still insert like one at a time. Sorry still insert like one at a time. Sorry
    still insert like one at a time. Sorry

    insert at the end, right? insert at the end, right? insert at the end, right?

    >> Oh, you mean okay? >> Oh, you mean okay? >> Oh, you mean okay?

    >> Yeah. What else?'
  concept_slugs:
  - discrete-diffusion
  - flow-matching
  - rectified-flow
- idx: 24
  start_sec: 1256.23
  end_sec: 1289.83
  text: '>> Yeah. What else? >> Yeah. What else?

    >> Inserting at but I saw that you can do >> Inserting at but I saw that you can
    do >> Inserting at but I saw that you can do

    decoding in blocks like you can predict decoding in blocks like you can predict
    decoding in blocks like you can predict

    it is still like predicting a block at a it is still like predicting a block at
    a it is still like predicting a block at a

    time. time. time.

    >> If you predict endo string then you >> If you predict endo string then you
    >> If you predict endo string then you

    discard prediction on blocks. discard prediction on blocks. discard prediction
    on blocks.

    >> Okay. So you can do a block. So you guys >> Okay. So you can do a block. So
    you guys >> Okay. So you can do a block. So you guys

    are kind of like doing thinking about are kind of like doing thinking about are
    kind of like doing thinking about

    same thing, right? Basically instead of same thing, right? Basically instead of
    same thing, right? Basically instead of

    one token at a time you predict multiple one token at a time you predict multiple
    one token at a time you predict multiple

    tokens. Uh we''re going to talk about tokens. Uh we''re going to talk about tokens.
    Uh we''re going to talk about

    that later but not now. Yeah. just like that later but not now. Yeah. just like
    that later but not now. Yeah. just like

    tokens at the end. So then even if you tokens at the end. So then even if you
    tokens at the end. So then even if you

    have like some fixed block size, have like some fixed block size, have like some
    fixed block size,

    >> you don''t have to generate for all of >> you don''t have to generate for all
    of >> you don''t have to generate for all of

    them. You can just have like pad at the them. You can just have like pad at the
    them. You can just have like pad at the

    end. So then you end. So then you end. So then you

    >> Okay, so tatting at the end. So you can'
  concept_slugs:
  - discrete-diffusion
  - flow-matching
  - rectified-flow
- idx: 25
  start_sec: 1289.83
  end_sec: 1335.84
  text: '>> Okay, so tatting at the end. So you can >> Okay, so tatting at the end.
    So you can

    discard some of the tokens. Yeah, that discard some of the tokens. Yeah, that
    discard some of the tokens. Yeah, that

    makes sense too. What else? Yeah. makes sense too. What else? Yeah. makes sense
    too. What else? Yeah.

    >> Uh don''t unmask all the tokens. >> Uh don''t unmask all the tokens. >> Uh
    don''t unmask all the tokens.

    >> You don''t unmask all the tokens. Oh, so >> You don''t unmask all the tokens.
    Oh, so >> You don''t unmask all the tokens. Oh, so

    like I see I see I see that that''s also like I see I see I see that that''s also
    like I see I see I see that that''s also

    another way. Is there anyone else? One another way. Is there anyone else? One
    another way. Is there anyone else? One

    last one last chance. last one last chance. last one last chance.

    By the way, this is like you kind of By the way, this is like you kind of By the
    way, this is like you kind of

    need to think out of box a little bit. need to think out of box a little bit.
    need to think out of box a little bit.

    This is like something that like we have This is like something that like we have
    This is like something that like we have

    it''s like not like anything we have seen it''s like not like anything we have
    seen it''s like not like anything we have seen

    or like I guess it comes from like what or like I guess it comes from like what
    or like I guess it comes from like what

    we have seen but like the way of we have seen but like the way of we have seen
    but like the way of

    thinking is not >> sure what the noising in that will look >> sure what the noising
    in that will look

    like but some form of recursive like but some form of recursive like but some
    form of recursive

    diffusion. So first you generate a diffusion. So first you generate a diffusion.
    So first you generate a

    paragraph and for the next diffusion paragraph and for the next diffusion'
  concept_slugs:
  - discrete-diffusion
  - flow-matching
  - rectified-flow
- idx: 26
  start_sec: 1335.84
  end_sec: 1389.52
  text: 'paragraph and for the next diffusion

    process that paragraph is that one process that paragraph is that one process
    that paragraph is that one

    element for you. You noise the paragraph element for you. You noise the paragraph
    element for you. You noise the paragraph

    and there are multiple paragraphs being and there are multiple paragraphs being
    and there are multiple paragraphs being

    >> okay. So this is like kind of similar to >> okay. So this is like kind of similar
    to >> okay. So this is like kind of similar to

    what they said actually and then it''s what they said actually and then it''s
    what they said actually and then it''s

    it''s a little bit we''re going to talk it''s a little bit we''re going to talk
    it''s a little bit we''re going to talk

    about something like that later. Yeah. about something like that later. Yeah.
    about something like that later. Yeah.

    OD solvers OD solvers OD solvers

    >> different OD solvers >> different OD solvers >> different OD solvers

    uh of what >> like why why would it help with the >> like why why would it help
    with the

    variable length problem I guess >> we can use like discrete flow matching >> we
    can use like discrete flow matching

    and auto reggressive like generated in and auto reggressive like generated in
    and auto reggressive like generated in

    kind of an auto reggressive way like uh kind of an auto reggressive way like uh
    kind of an auto reggressive way like uh

    kind of d noiseis aer set of tokens and kind of d noiseis aer set of tokens and
    kind of d noiseis aer set of tokens and

    then use that to den noiseise the next then use that to den noiseise the next
    then use that to den noiseise the next

    set of tokens so that we can control the set of tokens so that we can control
    the set of tokens so that we can control the

    >> so this is like all of you kind of say >> so this is like all of you kind of
    say >> so this is like all of you kind of say

    the same thing and that this is like the same thing and that this is like'
  concept_slugs:
  - discrete-diffusion
  - flow-matching
  - rectified-flow
- idx: 27
  start_sec: 1389.52
  end_sec: 1429.36
  text: 'the same thing and that this is like

    this is corresponding to one paper that this is corresponding to one paper that
    this is corresponding to one paper that

    we''re going to talk about but not now we''re going to talk about but not now
    we''re going to talk about but not now

    this is this is something different okay this is this is something different okay
    this is this is something different okay

    uh anyone else anyone else want to try uh anyone else anyone else want to try
    uh anyone else anyone else want to try

    yeah yeah yeah

    >> start in the middle left and right >> start in the middle left and right >>
    start in the middle left and right

    okay this is the closest one okay okay this is the closest one okay okay this
    is the closest one okay

    basically basically

    why don''t we h why do we have to insert why don''t we h why do we have to insert
    why don''t we h why do we have to insert

    only at the end All right. Can we insert only at the end All right. Can we insert
    only at the end All right. Can we insert

    in the middle? Like that''s fine too, in the middle? Like that''s fine too, in
    the middle? Like that''s fine too,

    right? That''s still variable length, right? That''s still variable length, right?
    That''s still variable length,

    right? That''s still like Yeah. variable right? That''s still like Yeah. variable
    right? That''s still like Yeah. variable

    length generation, right? So what you length generation, right? So what you length
    generation, right? So what you

    can do is say I have like sentence like can do is say I have like sentence like
    can do is say I have like sentence like

    like a prompt or something I guess I like a prompt or something I guess I like
    a prompt or something I guess I

    don''t know like I love cat. All right. don''t know like I love cat. All right.
    don''t know like I love cat. All right.

    And now what I can do is I can insert And now what I can do is I can insert And
    now what I can do is I can insert

    different tokens in between tokens, different tokens in between tokens,'
  concept_slugs:
  - discrete-diffusion
  - flow-matching
  - rectified-flow
- idx: 28
  start_sec: 1429.36
  end_sec: 1471.679
  text: 'different tokens in between tokens,

    right? I don''t need to insert at the right? I don''t need to insert at the right?
    I don''t need to insert at the

    end. Why do I have to insert at the end? end. Why do I have to insert at the end?
    end. Why do I have to insert at the end?

    Doesn''t matter, right? like and then I Doesn''t matter, right? like and then
    I Doesn''t matter, right? like and then I

    can do like in I can insert more tokens can do like in I can insert more tokens
    can do like in I can insert more tokens

    you know like in the in the in in this you know like in the in the in in this
    you know like in the in the in in this

    iterations of tokens right so basically iterations of tokens right so basically
    iterations of tokens right so basically

    uh this is what we call like a insertion uh this is what we call like a insertion
    uh this is what we call like a insertion

    based generation where you basically you based generation where you basically
    you based generation where you basically you

    have some like you you have some have some like you you have some have some like
    you you have some

    sequences and then instead of like auto sequences and then instead of like auto
    sequences and then instead of like auto

    reggressively this is kind of still reggressively this is kind of still reggressively
    this is kind of still

    autogressive I guess but it''s like um autogressive I guess but it''s like um
    autogressive I guess but it''s like um

    instead of auto reggressively um like instead of auto reggressively um like instead
    of auto reggressively um like

    inserting at the end you insert you can inserting at the end you insert you can
    inserting at the end you insert you can

    insert anywhere you can insert be after insert anywhere you can insert be after
    insert anywhere you can insert be after

    any token not just the last token. Yeah. any token not just the last token. Yeah.
    any token not just the last token. Yeah.

    >> Does this work in the diffusion case? >> Does this work in the diffusion case?'
  concept_slugs:
  - discrete-diffusion
  - flow-matching
  - rectified-flow
- idx: 29
  start_sec: 1471.679
  end_sec: 1515.279
  text: '>> Does this work in the diffusion case?

    >> Good question. I I''m gonna talk about >> Good question. I I''m gonna talk
    about >> Good question. I I''m gonna talk about

    it. Okay. So, how do we even model this it. Okay. So, how do we even model this
    it. Okay. So, how do we even model this

    kind of generation? Right. Uh kind of generation? Right. Uh kind of generation?
    Right. Uh

    what do we think actually let''s what do we think actually let''s what do we think
    actually let''s

    brainstorm like if you were to design brainstorm like if you were to design brainstorm
    like if you were to design

    this kind of model how would you do it this kind of model how would you do it
    this kind of model how would you do it

    like what are the things that you need like what are the things that you need
    like what are the things that you need

    to predict in this case? to predict in this case? to predict in this case?

    >> Yeah. The simplest way is to have like >> Yeah. The simplest way is to have
    like >> Yeah. The simplest way is to have like

    really big like training your model on a really big like training your model on
    a really big like training your model on a

    really big >> you know what this is actually how how >> you know what this is
    actually how how

    they train it in practice. So in they train it in practice. So in they train it
    in practice. So in

    practice they just have very big and practice they just have very big and practice
    they just have very big and

    then they just like basically this is then they just like basically this is then
    they just like basically this is

    how they construct their supervision how they construct their supervision how
    they construct their supervision

    actually. So like basically if you have actually. So like basically if you have
    actually. So like basically if you have

    like empty tokens or mass tokens then like empty tokens or mass tokens then like
    empty tokens or mass tokens then

    you use it to to to essentially you use it to to to essentially'
  concept_slugs:
  - discrete-diffusion
  - flow-matching
  - rectified-flow
- idx: 30
  start_sec: 1515.279
  end_sec: 1557.919
  text: 'you use it to to to essentially

    construct construct the the ground truth construct construct the the ground truth
    construct construct the the ground truth

    of like what this like what the full of like what this like what the full of like
    what this like what the full

    quote unquote sequence should be but quote unquote sequence should be but quote
    unquote sequence should be but

    what is the this is a good this this is what is the this is a good this this is
    what is the this is a good this this is

    good but like we''re getting there but good but like we''re getting there but
    good but like we''re getting there but

    what is the what is the thing that we what is the what is the thing that we what
    is the what is the thing that we

    should predict at at least right from should predict at at least right from should
    predict at at least right from

    the model like what are the things that the model like what are the things that
    the model like what are the things that

    we''re predicting we''re predicting we''re predicting

    >> I was actually going to say something >> I was actually going to say something
    >> I was actually going to say something

    similar like in addition to predicting similar like in addition to predicting
    similar like in addition to predicting

    an actual English token predict a mass an actual English token predict a mass
    an actual English token predict a mass

    token that you and then further expand token that you and then further expand
    token that you and then further expand

    into either mask or another condition. into either mask or another condition.
    into either mask or another condition.

    >> Very very very close. Okay. Okay. Okay. >> Very very very close. Okay. Okay.
    Okay. >> Very very very close. Okay. Okay. Okay.

    Okay. Let''s So basically basically what Okay. Let''s So basically basically what
    Okay. Let''s So basically basically what

    we need to predict is like we need to predict is like we need to predict is like

    what is the token and another thing what is the token and another thing what is
    the token and another thing

    right? What is this other thing? right? What is this other thing?'
  concept_slugs:
  - discrete-diffusion
  - flow-matching
  - rectified-flow
- idx: 31
  start_sec: 1557.919
  end_sec: 1612.789
  text: 'right? What is this other thing?

    >> The position or the whether to generate >> The position or the whether to generate
    >> The position or the whether to generate

    it between these it between these it between these

    >> whether to to insert right. Yeah. >> whether to to insert right. Yeah. >> whether
    to to insert right. Yeah.

    Basically that. So at each token what Basically that. So at each token what Basically
    that. So at each token what

    you should do is you to like basically you should do is you to like basically
    you should do is you to like basically

    what we need to decide is like basically what we need to decide is like basically
    what we need to decide is like basically

    okay so I''m looking at I I think I''m okay so I''m looking at I I think I''m
    okay so I''m looking at I I think I''m

    missing one token after I uh and then missing one token after I uh and then missing
    one token after I uh and then

    the missing token is wood just like in the missing token is wood just like in
    the missing token is wood just like in

    comparison to my ground truth here and comparison to my ground truth here and
    comparison to my ground truth here and

    then uh for love uh I''m missing two then uh for love uh I''m missing two then
    uh for love uh I''m missing two

    tokens right and then like the missing tokens right and then like the missing
    tokens right and then like the missing

    tokens can be either a or tokens can be either a or tokens can be either a or

    both the missing tokens after after love both the missing tokens after after love
    both the missing tokens after after love

    before cat. Right? So basically what we before cat. Right? So basically what we
    before cat. Right? So basically what we

    need to do is essentially train need to do is essentially train need to do is
    essentially train

    model to predict what we''re missing and model to predict what we''re missing
    and model to predict what we''re missing and

    also like if we''re missing right so also like if we''re missing right so also
    like if we''re missing right so

    basically if we''re missing tokens and'
  concept_slugs:
  - discrete-diffusion
  - flow-matching
  - rectified-flow
- idx: 32
  start_sec: 1612.789
  end_sec: 1665.919
  text: 'basically if we''re missing tokens and basically if we''re missing tokens
    and

    like essentially like essentially like essentially

    note that like it''s more likely or like note that like it''s more likely or like
    note that like it''s more likely or like

    it''s like basically it''s more likely to it''s like basically it''s more likely
    to it''s like basically it''s more likely to

    add more tokens after love than I in add more tokens after love than I in add
    more tokens after love than I in

    this case. You see that? Because like this case. You see that? Because like this
    case. You see that? Because like

    basically um it''s like it''s like because basically um it''s like it''s like
    because basically um it''s like it''s like because

    like there are more tokens that can be like there are more tokens that can be
    like there are more tokens that can be

    missing like a after love than I. So you missing like a after love than I. So
    you missing like a after love than I. So you

    should have a better chance to you know should have a better chance to you know
    should have a better chance to you know

    insert a after love like you know like insert a after love like you know like
    insert a after love like you know like

    from your model''s prediction. Does it from your model''s prediction. Does it
    from your model''s prediction. Does it

    make sense? make sense? make sense?

    Okay. So what you should do is there are Okay. So what you should do is there
    are Okay. So what you should do is there are

    two things from your model that you two things from your model that you two things
    from your model that you

    should predict, right? One is predict should predict, right? One is predict should
    predict, right? One is predict

    how many tokens are missing or if how many tokens are missing or if how many tokens
    are missing or if

    there''s any token missing after each there''s any token missing after each there''s
    any token missing after each

    token right so for each token this is token right so for each token this is token
    right so for each token this is

    what you''re predicting and then the what you''re predicting and then the'
  concept_slugs:
  - discrete-diffusion
  - flow-matching
  - rectified-flow
- idx: 33
  start_sec: 1665.919
  end_sec: 1706.399
  text: 'what you''re predicting and then the

    second objective from your model is second objective from your model is second
    objective from your model is

    predict what tokens are missing so this predict what tokens are missing so this
    predict what tokens are missing so this

    is the same as LM right so basically for is the same as LM right so basically
    for is the same as LM right so basically for

    LM you only have objective two where LM you only have objective two where LM you
    only have objective two where

    like you know after what should I what like you know after what should I what
    like you know after what should I what

    should I insert after each token and should I insert after each token and should
    I insert after each token and

    then you pretend each token is the the then you pretend each token is the the
    then you pretend each token is the the

    last token Right. This is how you train last token Right. This is how you train
    last token Right. This is how you train

    it. And then for this you just add it. And then for this you just add it. And
    then for this you just add

    another objective. Yeah. another objective. Yeah. another objective. Yeah.

    >> But then this is predicting the tokens >> But then this is predicting the tokens
    >> But then this is predicting the tokens

    after I can see the love and cat has after I can see the love and cat has after
    I can see the love and cat has

    been generated. been generated. been generated.

    >> It cannot right like it can it can. >> It cannot right like it can it can.
    >> It cannot right like it can it can.

    Yeah. It can can see all the existing Yeah. It can can see all the existing Yeah.
    It can can see all the existing

    tokens. tokens. tokens.

    >> Yeah. So so it has to do it has to do >> Yeah. So so it has to do it has to
    do >> Yeah. So so it has to do it has to do

    insertion right and not end of things insertion right and not end of things insertion
    right and not end of things

    like I don''t know. like I don''t know.'
  concept_slugs:
  - discrete-diffusion
  - flow-matching
  - rectified-flow
- idx: 34
  start_sec: 1706.399
  end_sec: 1750.32
  text: 'like I don''t know.

    >> Yeah. >> Yeah.

    >> Yeah. But basically what Okay. So >> Yeah. But basically what Okay. So >> Yeah.
    But basically what Okay. So

    basically what happens in the model or basically what happens in the model or
    basically what happens in the model or

    actually do I have it here? I do. I do. actually do I have it here? I do. I do.
    actually do I have it here? I do. I do.

    Okay. So what what what''s happening here Okay. So what what what''s happening
    here Okay. So what what what''s happening here

    is that so this is like one token like is that so this is like one token like
    is that so this is like one token like

    one token in a sentence. This happens at one token in a sentence. This happens
    at one token in a sentence. This happens at

    every token. Okay. So one token in a every token. Okay. So one token in a every
    token. Okay. So one token in a

    sentence it goes into your transformers sentence it goes into your transformers
    sentence it goes into your transformers

    and then it predict two things. One is and then it predict two things. One is
    and then it predict two things. One is

    how many token that are missing. The how many token that are missing. The how
    many token that are missing. The

    second thing is like one possible tokens second thing is like one possible tokens
    second thing is like one possible tokens

    to insert. Okay. Does it make sense? to insert. Okay. Does it make sense? to insert.
    Okay. Does it make sense?

    >> Yeah. I mean how many terms are missing? >> Yeah. I mean how many terms are
    missing? >> Yeah. I mean how many terms are missing?

    You need the start and the end range, You need the start and the end range, You
    need the start and the end range,

    right? So like for example in the right? So like for example in the right? So
    like for example in the

    previous example, you need both I and previous example, you need both I and previous
    example, you need both I and

    the the the

    >> Yeah. Yeah. So basically what''s >> Yeah. Yeah. So basically what''s'
  concept_slugs:
  - discrete-diffusion
  - flow-matching
  - rectified-flow
- idx: 35
  start_sec: 1750.32
  end_sec: 1795.19
  text: '>> Yeah. Yeah. So basically what''s

    happening in what''s hap what''s happening happening in what''s hap what''s happening
    happening in what''s hap what''s happening

    in like implementation is that you are in like implementation is that you are
    in like implementation is that you are

    going to be counting how many pink going to be counting how many pink going to
    be counting how many pink

    tokens are there. That''s it. tokens are there. That''s it. tokens are there.
    That''s it.

    >> My question was that you would need both >> My question was that you would
    need both >> My question was that you would need both

    let''s say X1 and X2 as an input to be let''s say X1 and X2 as an input to be
    let''s say X1 and X2 as an input to be

    able to tell how many are. You don''t able to tell how many are. You don''t able
    to tell how many are. You don''t

    because it''s full attention. because it''s full attention. because it''s full
    attention.

    >> Yeah. Yeah. Yeah. So, so you only need >> Yeah. Yeah. Yeah. So, so you only
    need >> Yeah. Yeah. Yeah. So, so you only need

    basically the only thing you need is basically the only thing you need is basically
    the only thing you need is

    like okay after this token like add at like okay after this token like add at
    like okay after this token like add at

    this token. So remember how in this token. So remember how in this token. So remember
    how in

    transformer you''re predicting something transformer you''re predicting something
    transformer you''re predicting something

    that has the same size as your input, that has the same size as your input, that
    has the same size as your input,

    right? So like after this token, how right? So like after this token, how right?
    So like after this token, how

    many tokens are missing after this token many tokens are missing after this token
    many tokens are missing after this token

    and before my next existing token? And and before my next existing token? And
    and before my next existing token? And

    what what is the one possible token that what what is the one possible token that
    what what is the one possible token that

    is that is missing out of all the tokens'
  concept_slugs:
  - discrete-diffusion
  - flow-matching
  - rectified-flow
- idx: 36
  start_sec: 1795.19
  end_sec: 1848.0
  text: 'is that is missing out of all the tokens is that is missing out of all the
    tokens

    that are missing? Right. Okay. So these that are missing? Right. Okay. So these
    that are missing? Right. Okay. So these

    two. All right. So how do we train two. All right. So how do we train two. All
    right. So how do we train

    these? How do we train with the these two How do we train with the these two

    objectives? We should know by now, objectives? We should know by now, objectives?
    We should know by now,

    right? right?

    I I feel like I hope we should know at I I feel like I hope we should know at
    I I feel like I hope we should know at

    least one of them. I think least one of them. I think least one of them. I think

    >> yeah >> yeah >> yeah

    like like just say next token that is like like just say next token that is like
    like just say next token that is

    just one just one just one

    >> that will just be at the other >> that will just be at the other >> that will
    just be at the other

    regressive models. Yeah. Yeah. regressive models. Yeah. Yeah. regressive models.
    Yeah. Yeah.

    >> Yeah. Then you can do the same thing >> Yeah. Then you can do the same thing
    >> Yeah. Then you can do the same thing

    with with with

    >> Mhm. Uh well okay I''ll just tell you the >> Mhm. Uh well okay I''ll just tell
    you the >> Mhm. Uh well okay I''ll just tell you the

    answer. So the first thing is literally answer. So the first thing is literally
    answer. So the first thing is literally

    just the kale between two person right just the kale between two person right
    just the kale between two person right

    that makes sense right? So like the that makes sense right? So like the that makes
    sense right? So like the

    person between your actual missing token person between your actual missing token
    person between your actual missing token

    like how many tokens you''re actually like how many tokens you''re actually like
    how many tokens you''re actually

    missing versus you know how many tokens missing versus you know how many tokens'
  concept_slugs:
  - discrete-diffusion
  - flow-matching
  - rectified-flow
- idx: 37
  start_sec: 1848.0
  end_sec: 1908.08
  text: 'missing versus you know how many tokens

    you predict to be missing and then the you predict to be missing and then the
    you predict to be missing and then the

    second thing is uh like literally just second thing is uh like literally just
    second thing is uh like literally just

    cross entropy of all possible missing cross entropy of all possible missing cross
    entropy of all possible missing

    tokens. So you just sum over all the pos tokens. So you just sum over all the
    pos tokens. So you just sum over all the pos

    all the cross entropy of pos like all the cross entropy of pos like all the cross
    entropy of pos like

    missing tokens. missing tokens. missing tokens.

    That''s it. Yeah. That''s it. Yeah. That''s it. Yeah.

    I I don''t understand at all how lower I I don''t understand at all how lower
    I I don''t understand at all how lower

    diffusion is coming. diffusion is coming. diffusion is coming.

    >> So let me I I''ll I''ll show you I''ll show >> So let me I I''ll I''ll show
    you I''ll show >> So let me I I''ll I''ll show you I''ll show

    you. Uh so basically besides insertion you. Uh so basically besides insertion
    you. Uh so basically besides insertion

    uh you can also do other editing options uh you can also do other editing options
    uh you can also do other editing options

    uh other editing operations right so uh other editing operations right so uh other
    editing operations right so

    essentially what you can do is uh you essentially what you can do is uh you essentially
    what you can do is uh you

    can do deletion and substitution can do deletion and substitution can do deletion
    and substitution

    right does that make sense so besides right does that make sense so besides right
    does that make sense so besides

    insertion you can also do those things h insertion you can also do those things
    h insertion you can also do those things h

    if you add if you have all the all three if you add if you have all the all three
    if you add if you have all the all three

    operations you get something called edit operations you get something called edit
    operations you get something called edit

    flow flow'
  concept_slugs:
  - discrete-diffusion
  - flow-matching
  - rectified-flow
- idx: 38
  start_sec: 1908.08
  end_sec: 1955.11
  text: 'flow

    And why is it a flow model? Well, it''s And why is it a flow model? Well, it''s
    And why is it a flow model? Well, it''s

    actually because this thing like the actually because this thing like the actually
    because this thing like the

    theory of this is coming from discre matching. Uh and okay let let''s discre matching.
    Uh and okay let let''s

    just like take a step back and see like just like take a step back and see like
    just like take a step back and see like

    why it is the case. So just so you know why it is the case. So just so you know
    why it is the case. So just so you know

    this is like not a rigorous proof or this is like not a rigorous proof or this
    is like not a rigorous proof or

    anything. This is basically just like anything. This is basically just like anything.
    This is basically just like

    give you some intuitions but like give you some intuitions but like give you some
    intuitions but like

    basically this is what''s happening. Uh basically this is what''s happening. Uh
    basically this is what''s happening. Uh

    so remember how at the end of the the so remember how at the end of the the so
    remember how at the end of the the

    mass diffusion thing we we deduce mass diffusion thing we we deduce mass diffusion
    thing we we deduce

    something that looks like this right? So something that looks like this right?
    So something that looks like this right? So

    basically what what what is happening basically what what what is happening basically
    what what what is happening

    here what is the most important thing here what is the most important thing here
    what is the most important thing

    that happen here is that uh like this that happen here is that uh like this that
    happen here is that uh like this

    what this formula tells you is that if what this formula tells you is that if
    what this formula tells you is that if

    something is changing right so if you something is changing right so if you something
    is changing right so if you

    change from you know something to change from you know something to change from
    you know something to

    another thing then you should be doing'
  concept_slugs:
  - discrete-diffusion
  - flow-matching
  - rectified-flow
- idx: 39
  start_sec: 1955.11
  end_sec: 2003.039
  text: 'another thing then you should be doing another thing then you should be doing

    this operation where it''s a ratio or this operation where it''s a ratio or this
    operation where it''s a ratio or

    like a rate times the clean data like a rate times the clean data like a rate
    times the clean data

    estimation right and then this thing is estimation right and then this thing is
    estimation right and then this thing is

    like this particular ratio at t limit like this particular ratio at t limit like
    this particular ratio at t limit

    right So essentially what we can do is right So essentially what we can do is
    right So essentially what we can do is

    we can parameterize the edit like the we can parameterize the edit like the we
    can parameterize the edit like the

    the basically how many tokens are you the basically how many tokens are you the
    basically how many tokens are you

    editing or like basically how frequent editing or like basically how frequent
    editing or like basically how frequent

    are you editing it like basically for are you editing it like basically for are
    you editing it like basically for

    each operation whether it''s insertion or each operation whether it''s insertion
    or each operation whether it''s insertion or

    it''s deletion or it''s substitution you it''s deletion or it''s substitution
    you it''s deletion or it''s substitution you

    use this as your target for your person use this as your target for your person
    use this as your target for your person

    and then you use the same logic as your and then you use the same logic as your
    and then you use the same logic as your

    cross entropy and then you just train it cross entropy and then you just train
    it cross entropy and then you just train it

    with the person plus cross entropy loss with the person plus cross entropy loss
    with the person plus cross entropy loss

    and this is actually so the two things and this is actually so the two things
    and this is actually so the two things

    combined together uh is actually another combined together uh is actually another
    combined together uh is actually another

    divergence that is basically just a divergence that is basically just a'
  concept_slugs:
  - discrete-diffusion
  - flow-matching
  - rectified-flow
- idx: 40
  start_sec: 2003.039
  end_sec: 2051.28
  text: 'divergence that is basically just a

    generalized version of KL. Uh but this generalized version of KL. Uh but this
    generalized version of KL. Uh but this

    is like too complicated. We''re not going is like too complicated. We''re not
    going is like too complicated. We''re not going

    to talk about it, but this is kind of to talk about it, but this is kind of to
    talk about it, but this is kind of

    like the intuition of what''s happening. like the intuition of what''s happening.
    like the intuition of what''s happening.

    And like in like one specific um special And like in like one specific um special
    And like in like one specific um special

    case is that the deletion because you case is that the deletion because you case
    is that the deletion because you

    don''t really need to predict another don''t really need to predict another don''t
    really need to predict another

    token after deletion, right? Because token after deletion, right? Because token
    after deletion, right? Because

    deletion literally just flip it to mask. deletion literally just flip it to mask.
    deletion literally just flip it to mask.

    So deletion doesn''t need logic. So for So deletion doesn''t need logic. So for
    So deletion doesn''t need logic. So for

    deletion you only do the the person loss deletion you only do the the person loss
    deletion you only do the the person loss

    and that''s it. and that''s it. and that''s it.

    Okay, any questions? So basically the Okay, any questions? So basically the Okay,
    any questions? So basically the

    reason why it''s related to two reason why it''s related to two reason why it''s
    related to two

    diffusions because all of these is diffusions because all of these is diffusions
    because all of these is

    deduced from the discrete flow matching deduced from the discrete flow matching
    deduced from the discrete flow matching

    theory and uh the insertion based only theory and uh the insertion based only
    theory and uh the insertion based only

    the insertion only model is sort of like the insertion only model is sort of like
    the insertion only model is sort of like

    a special case of ediflow um which is a special case of ediflow um which is a
    special case of ediflow um which is

    actually like already good enough for actually like already good enough for'
  concept_slugs:
  - discrete-diffusion
  - flow-matching
  - rectified-flow
- idx: 41
  start_sec: 2051.28
  end_sec: 2096.56
  text: 'actually like already good enough for

    whatever you want to do. So you can whatever you want to do. So you can whatever
    you want to do. So you can

    literally just train a insertion based literally just train a insertion based
    literally just train a insertion based

    like insertion only at the flow and it''s like insertion only at the flow and
    it''s like insertion only at the flow and it''s

    it''s a valid language model. it''s a valid language model. it''s a valid language
    model.

    Yeah. Yeah.

    >> Are you assuming that the given the >> Are you assuming that the given the
    >> Are you assuming that the given the

    distribution of are like independent is distribution of are like independent is
    distribution of are like independent is

    >> oh why are you assuming the the the >> oh why are you assuming the the the
    >> oh why are you assuming the the the

    distribution of all the tokens distribution of all the tokens distribution of
    all the tokens

    independent you saying? independent you saying? independent you saying?

    >> Yeah. Yeah. This is just because it''s >> Yeah. Yeah. This is just because
    it''s >> Yeah. Yeah. This is just because it''s

    easy. It''s not really it''s not like a easy. It''s not really it''s not like
    a easy. It''s not really it''s not like a

    good inductive bias at all. This is this good inductive bias at all. This is this
    good inductive bias at all. This is this

    is like Yeah. Obviously, this is is like Yeah. Obviously, this is is like Yeah.
    Obviously, this is

    something that you should change or or something that you should change or or
    something that you should change or or

    you can change, right? Yeah. Yeah. Yeah. you can change, right? Yeah. Yeah. Yeah.
    you can change, right? Yeah. Yeah. Yeah.

    Okay. Actually, that''s a good good uh Okay. Actually, that''s a good good uh
    Okay. Actually, that''s a good good uh

    you know um leadway to to what we''re you know um leadway to to what we''re you
    know um leadway to to what we''re

    going to talk about next, right? So, now going to talk about next, right? So,
    now going to talk about next, right? So, now

    we kind of fixed a veryable we kind of fixed a veryable'
  concept_slugs:
  - discrete-diffusion
  - flow-matching
  - rectified-flow
- idx: 42
  start_sec: 2096.56
  end_sec: 2140.48
  text: 'we kind of fixed a veryable

    length uh problem with insertion based length uh problem with insertion based
    length uh problem with insertion based

    generation. Uh we have other things to generation. Uh we have other things to
    generation. Uh we have other things to

    fix, right? The first most prominent fix, right? The first most prominent fix,
    right? The first most prominent

    thing is that like uh like we can''t do thing is that like uh like we can''t do
    thing is that like uh like we can''t do

    KV caching. uh how can we enable KV caching. uh how can we enable KV caching.
    uh how can we enable

    caching and actually at the same time caching and actually at the same time caching
    and actually at the same time

    variable length generation. This is like variable length generation. This is like
    variable length generation. This is like

    literally what you guys just said, literally what you guys just said, literally
    what you guys just said,

    right? Basically what you can do is uh right? Basically what you can do is uh
    right? Basically what you can do is uh

    instead of like generating like a super instead of like generating like a super
    instead of like generating like a super

    large like p paragraph at once, what you large like p paragraph at once, what
    you large like p paragraph at once, what you

    can do is you can break it down into a can do is you can break it down into a
    can do is you can break it down into a

    lot of blocks and then each blocks are lot of blocks and then each blocks are
    lot of blocks and then each blocks are

    you know auto reggressive which with you know auto reggressive which with you
    know auto reggressive which with

    each other but within the blocks is like each other but within the blocks is like
    each other but within the blocks is like

    diffusion right. So this is what they diffusion right. So this is what they diffusion
    right. So this is what they

    called a block diffusion or called a block diffusion or called a block diffusion
    or

    semi-traggressive mass diffusion model. semi-traggressive mass diffusion model.
    semi-traggressive mass diffusion model.

    So like basically this thing is very So like basically this thing is very'
  concept_slugs:
  - discrete-diffusion
  - flow-matching
  - rectified-flow
- idx: 43
  start_sec: 2140.48
  end_sec: 2180.079
  text: 'So like basically this thing is very

    nice because you can um like essentially nice because you can um like essentially
    nice because you can um like essentially

    you can do paralyze generation like you can do paralyze generation like you can
    do paralyze generation like

    normal mass diffusion where you unmask normal mass diffusion where you unmask
    normal mass diffusion where you unmask

    like more than one token at a time. By like more than one token at a time. By
    like more than one token at a time. By

    the way um edit flow is also because all the way um edit flow is also because
    all the way um edit flow is also because all

    the tokens are independent. So you can the tokens are independent. So you can
    the tokens are independent. So you can

    unmask like or you can change you can unmask like or you can change you can unmask
    like or you can change you can

    edit uh you know each token edit uh you know each token edit uh you know each
    token

    independently. So you can you know you independently. So you can you know you
    independently. So you can you know you

    can also generate more than one token at can also generate more than one token
    at can also generate more than one token at

    a time. Uh but basically this thing is a time. Uh but basically this thing is
    a time. Uh but basically this thing is

    nice because it it preserve like the nice because it it preserve like the nice
    because it it preserve like the

    like a rough ordering like a rough auto like a rough ordering like a rough auto
    like a rough ordering like a rough auto

    reggressive ordering of your you know reggressive ordering of your you know reggressive
    ordering of your you know

    your your your your sentences. Um your your your your sentences. Um your your
    your your sentences. Um

    because of that it also enables KV because of that it also enables KV because
    of that it also enables KV

    caching. So you can cache all the things caching. So you can cache all the things
    caching. So you can cache all the things

    that you have generated like in your that you have generated like in your'
  concept_slugs:
  - discrete-diffusion
  - flow-matching
  - rectified-flow
- idx: 44
  start_sec: 2180.079
  end_sec: 2220.23
  text: 'that you have generated like in your

    previous blocks. The only thing you need previous blocks. The only thing you need
    previous blocks. The only thing you need

    to like do birectional attention to is to like do birectional attention to is
    to like do birectional attention to is

    your current block right? Uh and then your current block right? Uh and then your
    current block right? Uh and then

    you can also do like variable lines you can also do like variable lines you can
    also do like variable lines

    generation because you can have generation because you can have generation because
    you can have

    arbitrarily like arbitrary number of arbitrarily like arbitrary number of arbitrarily
    like arbitrary number of

    blocks and you can also predict more blocks and you can also predict more blocks
    and you can also predict more

    than one token at a time within your than one token at a time within your than
    one token at a time within your

    blocks. Uh so this thing is actually blocks. Uh so this thing is actually blocks.
    Uh so this thing is actually

    like a very good um like examples of like a very good um like examples of like
    a very good um like examples of

    like how you can sort of like like how you can sort of like like how you can sort
    of like

    interpolate uh you know two different interpolate uh you know two different interpolate
    uh you know two different

    models to get a better one. Um so yeah models to get a better one. Um so yeah
    models to get a better one. Um so yeah

    this is pretty cool. Uh so yeah so let''s this is pretty cool. Uh so yeah so let''s
    this is pretty cool. Uh so yeah so let''s

    just look at look at work in real time. just look at look at work in real time.
    just look at look at work in real time.

    Yeah, but uh but like yeah, I''m really Yeah, but uh but like yeah, I''m really
    Yeah, but uh but like yeah, I''m really

    glad that like kind of like a lot of glad that like kind of like a lot of glad
    that like kind of like a lot of

    people think about this. Um but yeah, so'
  concept_slugs:
  - discrete-diffusion
  - flow-matching
  - rectified-flow
- idx: 45
  start_sec: 2220.23
  end_sec: 2270.72
  text: 'people think about this. Um but yeah, so people think about this. Um but
    yeah, so

    this is like a nice way to do you know this is like a nice way to do you know
    this is like a nice way to do you know

    to combine the fusion model with LMS. to combine the fusion model with LMS. to
    combine the fusion model with LMS.

    Okay, any question? Yeah, Okay, any question? Yeah, Okay, any question? Yeah,

    >> the diagram. Okay, I thought they were >> the diagram. Okay, I thought they
    were >> the diagram. Okay, I thought they were

    generating two blocks at the same time, generating two blocks at the same time,
    generating two blocks at the same time,

    but I thought it''s all but I thought it''s all but I thought it''s all

    Yeah. Yeah. Yeah. Yeah. Yeah. Yeah.

    >> Yeah. So the blocks here are like the >> Yeah. So the blocks here are like
    the >> Yeah. So the blocks here are like the

    the the the orange thing. >> It will generate a block of this EOS. >> It will
    generate a block of this EOS.

    >> No no like the EOS will is a it''s a >> No no like the EOS will is a it''s
    a >> No no like the EOS will is a it''s a

    token that get generated in arbitrary token that get generated in arbitrary token
    that get generated in arbitrary

    one of the blocks and then you just do one of the blocks and then you just do
    one of the blocks and then you just do

    the same thing as what you would have the same thing as what you would have the
    same thing as what you would have

    done in the max diffusion just discard done in the max diffusion just discard
    done in the max diffusion just discard

    everything after that. everything after that. everything after that.

    >> Yeah. >> Yeah.

    K in that current block because we have K in that current block because we have
    K in that current block because we have

    >> we cannot >> we cannot >> we cannot

    >> not in the current block but but we can >> not in the current block but but
    we can'
  concept_slugs:
  - discrete-diffusion
  - flow-matching
  - rectified-flow
- idx: 46
  start_sec: 2270.72
  end_sec: 2309.76
  text: '>> not in the current block but but we can

    K catch all the previous blocks. >> No because we don''t we haven''t generated
    >> No because we don''t we haven''t generated

    that yet, right? So like the block are that yet, right? So like the block are
    that yet, right? So like the block are

    auto reggressive. So the blocks are auto reggressive. So the blocks are auto reggressive.
    So the blocks are

    causal. So we Yeah. causal. So we Yeah. causal. So we Yeah.

    >> So what''s generally like design choice >> So what''s generally like design
    choice >> So what''s generally like design choice

    for like the block size? Because if it''s for like the block size? Because if
    it''s for like the block size? Because if it''s

    smaller than the number of diffusion smaller than the number of diffusion smaller
    than the number of diffusion

    steps then it just defeats the purpose. steps then it just defeats the purpose.
    steps then it just defeats the purpose.

    Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah.

    >> So this is like a like a like a like a >> So this is like a like a like a like
    a >> So this is like a like a like a like a

    sort of like a oblation that you need to sort of like a oblation that you need
    to sort of like a oblation that you need to

    basically it''s like a hyperparameter basically it''s like a hyperparameter basically
    it''s like a hyperparameter

    that you kind of need to tune. Yeah. that you kind of need to tune. Yeah. that
    you kind of need to tune. Yeah.

    Yeah. You do also like basically if you Yeah. You do also like basically if you
    Yeah. You do also like basically if you

    have like a very large block then like have like a very large block then like
    have like a very large block then like

    obviously you need larger models and obviously you need larger models and obviously
    you need larger models and

    stuff like that, right? So this is kind stuff like that, right? So this is kind
    stuff like that, right? So this is kind

    of like also like but but but but if you of like also like but but but but if
    you'
  concept_slugs:
  - discrete-diffusion
  - flow-matching
  - rectified-flow
- idx: 47
  start_sec: 2309.76
  end_sec: 2356.87
  text: 'of like also like but but but but if you

    have too small of a blog then it just have too small of a blog then it just have
    too small of a blog then it just

    Yeah. It doesn''t really it just is just Yeah. It doesn''t really it just is just
    Yeah. It doesn''t really it just is just

    auto reggressive I guess. Yeah. Yeah. auto reggressive I guess. Yeah. Yeah. auto
    reggressive I guess. Yeah. Yeah.

    >> Is like the best on all four fronts. Why >> Is like the best on all four fronts.
    Why >> Is like the best on all four fronts. Why

    is it not been adopted so far? is it not been adopted so far? is it not been adopted
    so far?

    >> Because this thing got proposed like >> Because this thing got proposed like
    >> Because this thing got proposed like

    when when did it get proposed? like last when when did it get proposed? like last
    when when did it get proposed? like last

    year. year. year.

    So it''s pretty it''s a lot of time but So it''s pretty it''s a lot of time but
    So it''s pretty it''s a lot of time but

    the world really the world really the world really

    >> well actually >> well actually >> well actually

    they do have um like AB models like that they do have um like AB models like that
    they do have um like AB models like that

    right and another thing that is like right and another thing that is like right
    and another thing that is like

    kind of tricky to do like diffusion kind of tricky to do like diffusion kind of
    tricky to do like diffusion

    language model is that uh the RL is not language model is that uh the RL is not
    language model is that uh the RL is not

    as easy as as LMS but this is like still as easy as as LMS but this is like still
    as easy as as LMS but this is like still

    like a very active research direction like a very active research direction like
    a very active research direction

    that people are investing a lot of money that people are investing a lot of money
    that people are investing a lot of money

    in I think. Yeah.'
  concept_slugs:
  - discrete-diffusion
  - flow-matching
  - rectified-flow
- idx: 48
  start_sec: 2356.87
  end_sec: 2411.52
  text: 'in I think. Yeah. in I think. Yeah.

    >> Do you think the second one is >> Do you think the second one is >> Do you
    think the second one is

    um like it''s it''s the it''s a problem of um like it''s it''s the it''s a problem
    of um like it''s it''s the it''s a problem of

    scale then for the second one scale then for the second one scale then for the
    second one

    >> it is a problem of scale but the problem >> it is a problem of scale but the
    problem >> it is a problem of scale but the problem

    is to scale it up it''s like very very is to scale it up it''s like very very
    is to scale it up it''s like very very

    very difficult right because like you very difficult right because like you very
    difficult right because like you

    you need full attention of all lengths you need full attention of all lengths
    you need full attention of all lengths

    so it''s like quadratically hard the when so it''s like quadratically hard the
    when so it''s like quadratically hard the when

    you scale the the the the the length up you scale the the the the the length up
    you scale the the the the the length up

    right so this thing is just like so yeah right so this thing is just like so yeah
    right so this thing is just like so yeah

    so like discrete diffusion is actually so like discrete diffusion is actually
    so like discrete diffusion is actually

    pretty it''s not trivial to scale even pretty it''s not trivial to scale even
    pretty it''s not trivial to scale even

    though people claim that it has better though people claim that it has better
    though people claim that it has better

    scaling scaling scaling

    So I don''t know. >> the smallest block size is similar to >> the smallest block
    size is similar to

    >> Yeah. LM, right? It''s just one one token >> Yeah. LM, right? It''s just one
    one token >> Yeah. LM, right? It''s just one one token

    at a time. LM. Yeah. Yeah, that''s right. at a time. LM. Yeah. Yeah, that''s right.
    at a time. LM. Yeah. Yeah, that''s right.

    That''s correct. Yeah. That''s correct. Yeah.'
  concept_slugs:
  - discrete-diffusion
  - flow-matching
  - rectified-flow
- idx: 49
  start_sec: 2411.52
  end_sec: 2457.359
  text: 'That''s correct. Yeah.

    >> For the for the second case, the mass >> For the for the second case, the mass
    >> For the for the second case, the mass

    diffusion, why can''t we do something diffusion, why can''t we do something diffusion,
    why can''t we do something

    like sliding window to kind of like sliding window to kind of like sliding window
    to kind of

    Well, this is kind of sliding window, Well, this is kind of sliding window, Well,
    this is kind of sliding window,

    right? right?

    >> Without the kind of >> Without the kind of >> Without the kind of

    >> right. But like basically what you''re >> right. But like basically what you''re
    >> right. But like basically what you''re

    suggesting is basically block diffusion, suggesting is basically block diffusion,
    suggesting is basically block diffusion,

    right? It''s and like like what you''re right? It''s and like like what you''re
    right? It''s and like like what you''re

    suggesting is actually semi-auto suggesting is actually semi-auto suggesting is
    actually semi-auto

    reggressive. I showed you already, reggressive. I showed you already, reggressive.
    I showed you already,

    right? Last class after class. So it''s right? Last class after class. So it''s
    right? Last class after class. So it''s

    pretty much the same thing, right? It''s pretty much the same thing, right? It''s
    pretty much the same thing, right? It''s

    pretty much just sliding window. um pretty much just sliding window. um pretty
    much just sliding window. um

    except like you don''t really you don''t except like you don''t really you don''t
    except like you don''t really you don''t

    really have a window like you don''t really have a window like you don''t really
    have a window like you don''t

    change what you have generated but you change what you have generated but you
    change what you have generated but you

    could also just do sliding window that''s could also just do sliding window that''s
    could also just do sliding window that''s

    like not against the rule at all. Yeah, like not against the rule at all. Yeah,
    like not against the rule at all. Yeah,

    that''s totally fine and it''s it should that''s totally fine and it''s it should
    that''s totally fine and it''s it should

    work the same. work the same. work the same.

    Anything else? Yep. Anything else? Yep.'
  concept_slugs:
  - discrete-diffusion
  - flow-matching
  - rectified-flow
- idx: 50
  start_sec: 2457.359
  end_sec: 2509.2
  text: 'Anything else? Yep.

    >> Can you overhand why mass diffusion is >> Can you overhand why mass diffusion
    is >> Can you overhand why mass diffusion is

    lower? lower? lower?

    >> Uh okay. Who wants to tell who who wants >> Uh okay. Who wants to tell who
    who wants >> Uh okay. Who wants to tell who who wants

    to answer this question? Why why is mass to answer this question? Why why is mass
    to answer this question? Why why is mass

    diffusion can be lower quality can have diffusion can be lower quality can have
    diffusion can be lower quality can have

    lower quality or like more difficult to lower quality or like more difficult to
    lower quality or like more difficult to

    train or more difficult to generate a train or more difficult to generate a train
    or more difficult to generate a

    high quality data? high quality data? high quality data?

    We kind of went over that We kind of went over that We kind of went over that

    the the example that you you you showed, the the example that you you you showed,
    the the example that you you you showed,

    right? Okay. Oh, yeah. Yeah. Yeah. I got right? Okay. Oh, yeah. Yeah. Yeah. I
    got right? Okay. Oh, yeah. Yeah. Yeah. I got

    them. >> Yeah.

    >> Yeah. Right. So, basically like auto >> Yeah. Right. So, basically like auto
    >> Yeah. Right. So, basically like auto

    reggressiveness is like a very good reggressiveness is like a very good reggressiveness
    is like a very good

    inductive bias for tax. So it''s like inductive bias for tax. So it''s like inductive
    bias for tax. So it''s like

    very basically this is like the most very basically this is like the most very
    basically this is like the most

    naive way that you can it''s the safest naive way that you can it''s the safest
    naive way that you can it''s the safest

    way in a sense that you can generate a way in a sense that you can generate a
    way in a sense that you can generate a

    sequence right so basically this is why sequence right so basically this is why
    sequence right so basically this is why

    yeah yeah

    but it doesn''t mean that you you cannot but it doesn''t mean that you you cannot'
  concept_slugs:
  - discrete-diffusion
  - flow-matching
  - rectified-flow
- idx: 51
  start_sec: 2509.2
  end_sec: 2565.27
  text: 'but it doesn''t mean that you you cannot

    train a good enough diffusion model to train a good enough diffusion model to
    train a good enough diffusion model to

    blm that''s not the case it''s just that blm that''s not the case it''s just that
    blm that''s not the case it''s just that

    it''s harder yeah cool okay so we have talked about we cool okay so we have talked
    about we

    actually kind of solved the all three actually kind of solved the all three actually
    kind of solved the all three

    with the previous thing and uh just so with the previous thing and uh just so
    with the previous thing and uh just so

    you guys know for the unmask or ordering you guys know for the unmask or ordering
    you guys know for the unmask or ordering

    thing. So basically people also have thing. So basically people also have thing.
    So basically people also have

    been developing a method to like been developing a method to like been developing
    a method to like

    basically determine basically determine basically determine

    the best uh unmasking order at inference the best uh unmasking order at inference
    the best uh unmasking order at inference

    time using like a pre-trained mass time using like a pre-trained mass time using
    like a pre-trained mass

    diffusion models. And if you guys are diffusion models. And if you guys are diffusion
    models. And if you guys are

    interested like feel free to Google. Um interested like feel free to Google. Um
    interested like feel free to Google. Um

    but basically what people have found is but basically what people have found is
    but basically what people have found is

    that even with like a like a fully like that even with like a like a fully like
    that even with like a like a fully like

    birectional uh mass diffusion model the birectional uh mass diffusion model the
    birectional uh mass diffusion model the

    most like optimal way to unmask is still most like optimal way to unmask is still
    most like optimal way to unmask is still

    follow like a like a semi-auto follow like a like a semi-auto follow like a like
    a semi-auto

    reggressive ordering. So like basically reggressive ordering. So like basically
    reggressive ordering. So like basically

    the the optimal that you''re going to get'
  concept_slugs:
  - discrete-diffusion
  - flow-matching
  - rectified-flow
- idx: 52
  start_sec: 2565.27
  end_sec: 2612.96
  text: 'the the optimal that you''re going to get the the optimal that you''re going
    to get

    from whatever algorithm that they from whatever algorithm that they from whatever
    algorithm that they

    develop will look like semi-auto develop will look like semi-auto develop will
    look like semi-auto

    regggressive in a way. Yeah. So it''s regggressive in a way. Yeah. So it''s regggressive
    in a way. Yeah. So it''s

    like pretty interesting that like you like pretty interesting that like you like
    pretty interesting that like you

    know that that that that that is like know that that that that that is like know
    that that that that that is like

    you you still need to sort of respect you you still need to sort of respect you
    you still need to sort of respect

    this um like inductive bias for for for this um like inductive bias for for for
    this um like inductive bias for for for

    text. Okay. So the last thing that you text. Okay. So the last thing that you
    text. Okay. So the last thing that you

    know we have left is the continuous like know we have left is the continuous like
    know we have left is the continuous like

    basically how we can build a multimodel basically how we can build a multimodel
    basically how we can build a multimodel

    diffusion right. So anyone want to take diffusion right. So anyone want to take
    diffusion right. So anyone want to take

    a guess this is actually very very a guess this is actually very very a guess
    this is actually very very

    straightforward. >> Yeah. image tokens like wea just the >> Yeah. image tokens
    like wea just the

    same way we wish. same way we wish. same way we wish.

    >> Yeah. >> Yeah.

    >> Yeah. That''s a good but okay but I guess >> Yeah. That''s a good but okay
    but I guess >> Yeah. That''s a good but okay but I guess

    the question is like uh actually let''s the question is like uh actually let''s
    the question is like uh actually let''s

    let''s uh let''s look at this. Uh so so let''s uh let''s look at this. Uh so so
    let''s uh let''s look at this. Uh so so

    this is not image and text but like this is not image and text but like'
  concept_slugs:
  - discrete-diffusion
  - flow-matching
  - rectified-flow
- idx: 53
  start_sec: 2612.96
  end_sec: 2671.2
  text: 'this is not image and text but like

    we''re going to look at image and text we''re going to look at image and text
    we''re going to look at image and text

    later. But for those of you who are in later. But for those of you who are in
    later. But for those of you who are in

    compile I guess uh if you try to design compile I guess uh if you try to design
    compile I guess uh if you try to design

    a protein you need to design two things. a protein you need to design two things.
    a protein you need to design two things.

    one is the sequence of the the the the one is the sequence of the the the the
    one is the sequence of the the the the

    uh uh uh

    what is the name of the thing that the what is the name of the thing that the
    what is the name of the thing that the

    amino acid is that is that what it is? amino acid is that is that what it is?
    amino acid is that is that what it is?

    Oh, great. Thank you. I I I''m illiterate Oh, great. Thank you. I I I''m illiterate
    Oh, great. Thank you. I I I''m illiterate

    in in in bio. Anyway, and then the other in in in bio. Anyway, and then the other
    in in in bio. Anyway, and then the other

    thing that you need to design is like thing that you need to design is like thing
    that you need to design is like

    the the spatial structure of the of of the the spatial structure of the of of
    the the spatial structure of the of of

    of the protein, right? So, basically um of the protein, right? So, basically um
    of the protein, right? So, basically um

    the the sequence itself is discreet, but the the sequence itself is discreet,
    but the the sequence itself is discreet, but

    the spatial structure is continuous, the spatial structure is continuous, the
    spatial structure is continuous,

    right? So, how can we uh sort of right? So, how can we uh sort of right? So, how
    can we uh sort of

    co-generate these two things together? >> Yeah.

    >> What are we cogenerating? >> What are we cogenerating?'
  concept_slugs:
  - discrete-diffusion
  - flow-matching
  - rectified-flow
- idx: 54
  start_sec: 2671.2
  end_sec: 2715.589
  text: '>> What are we cogenerating?

    >> So, we''re co-generating something uh >> So, we''re co-generating something
    uh >> So, we''re co-generating something uh

    discreet and something uh continuous at discreet and something uh continuous at
    discreet and something uh continuous at

    the same time and they''re kind of the same time and they''re kind of the same
    time and they''re kind of

    correlated. >> Yeah. Yeah. Yeah. Yeah. Literally >> Yeah. Yeah. Yeah. Yeah. Literally

    exactly that. So, basically what all you exactly that. So, basically what all
    you exactly that. So, basically what all you

    need to do is you need to build kind of need to do is you need to build kind of
    need to do is you need to build kind of

    two models that kind of like Yeah. two models that kind of like Yeah. two models
    that kind of like Yeah.

    There''s like two models that takes each There''s like two models that takes each
    There''s like two models that takes each

    other as condition kind of and then for other as condition kind of and then for
    other as condition kind of and then for

    the for the continuous uh the thing you the for the continuous uh the thing you
    the for the continuous uh the thing you

    use flow matching loss for the discreing use flow matching loss for the discreing
    use flow matching loss for the discreing

    you use discrete flow matching loss you use discrete flow matching loss you use
    discrete flow matching loss

    that''s it basically uh and then you can that''s it basically uh and then you
    can that''s it basically uh and then you can

    just like interle the basically just just like interle the basically just just
    like interle the basically just

    like oh let''s d noiseise a little bit in like oh let''s d noiseise a little bit
    in like oh let''s d noiseise a little bit in

    the continuous space all right now let''s the continuous space all right now let''s
    the continuous space all right now let''s

    uh you know generate something in the uh you know generate something in the uh
    you know generate something in the

    discrete and let''s do that like alter discrete and let''s do that like alter
    discrete and let''s do that like alter

    like alternating between the two that''s'
  concept_slugs:
  - discrete-diffusion
  - flow-matching
  - rectified-flow
- idx: 55
  start_sec: 2715.589
  end_sec: 2763.349
  text: 'like alternating between the two that''s like alternating between the two
    that''s

    pretty much that right and like pretty much that right and like pretty much that
    right and like

    basically And then if you do basically basically And then if you do basically
    basically And then if you do basically

    and and you can also do like you first and and you can also do like you first
    and and you can also do like you first

    generate the sequence fully using the generate the sequence fully using the generate
    the sequence fully using the

    discrete model uh using discrete for discrete model uh using discrete for discrete
    model uh using discrete for

    matching and then you condition on the matching and then you condition on the
    matching and then you condition on the

    generated sequence and then generated generated sequence and then generated generated
    sequence and then generated

    the structure then this is what they the structure then this is what they the
    structure then this is what they

    call forfolding in call forfolding in call forfolding in

    in compile and likewise you can also in compile and likewise you can also in compile
    and likewise you can also

    first generate the what we call first first generate the what we call first first
    generate the what we call first

    generate the structure then predict the generate the structure then predict the
    generate the structure then predict the

    sequence then it''s called the inverse sequence then it''s called the inverse
    sequence then it''s called the inverse

    folding. So basically like you can just folding. So basically like you can just
    folding. So basically like you can just

    do or you can just alternate interle do or you can just alternate interle do or
    you can just alternate interle

    right that works too and um right that works too and um right that works too and
    um

    essentially what people have done essentially what people have done essentially
    what people have done

    actually let''s look at this yeah so you actually let''s look at this yeah so
    you actually let''s look at this yeah so you

    can also do this for image and text as can also do this for image and text as
    can also do this for image and text as

    well right so what you can do is you can'
  concept_slugs:
  - discrete-diffusion
  - flow-matching
  - rectified-flow
- idx: 56
  start_sec: 2763.349
  end_sec: 2810.87
  text: 'well right so what you can do is you can well right so what you can do is
    you can

    uh have like just like I think some uh have like just like I think some uh have
    like just like I think some

    someone already said it right basically someone already said it right basically
    someone already said it right basically

    you can have text token and image tokens you can have text token and image tokens
    you can have text token and image tokens

    and then you just learn like a and then you just learn like a and then you just
    learn like a

    birectional transformer and they they birectional transformer and they they birectional
    transformer and they they

    kind of yeah you can just like kind of yeah you can just like kind of yeah you
    can just like

    co-generate your text tokens and D co-generate your text tokens and D co-generate
    your text tokens and D

    noiseis image token at the same time noiseis image token at the same time noiseis
    image token at the same time

    this kind of thing. So you can build you this kind of thing. So you can build
    you this kind of thing. So you can build you

    basically just build a birectional basically just build a birectional basically
    just build a birectional

    transformer to predict both uh and uh transformer to predict both uh and uh transformer
    to predict both uh and uh

    the for the text part you use edit flow the for the text part you use edit flow
    the for the text part you use edit flow

    loss or like insertion based flow loss loss or like insertion based flow loss
    loss or like insertion based flow loss

    and then for the image part you just use and then for the image part you just
    use and then for the image part you just use

    flow matching. All right any question? flow matching. All right any question?
    flow matching. All right any question?

    Yeah Yeah Yeah

    >> better than >> better than >> better than

    >> uh transfusion >> uh transfusion >> uh transfusion

    >> like the normal may even know if this >> like the normal may even know if this
    >> like the normal may even know if this

    >> I mean the problem is like this is a'
  concept_slugs:
  - discrete-diffusion
  - flow-matching
  - rectified-flow
- idx: 57
  start_sec: 2810.87
  end_sec: 2857.04
  text: '>> I mean the problem is like this is a >> I mean the problem is like this
    is a

    research project right so it''s like very research project right so it''s like
    very research project right so it''s like very

    difficult for it to compare with I don''t difficult for it to compare with I don''t
    difficult for it to compare with I don''t

    know like like product I guess all this know like like product I guess all this
    know like like product I guess all this

    >> yeah but >> yeah but >> yeah but

    >> yeah I think they compared with >> yeah I think they compared with >> yeah
    I think they compared with

    uh I don''t remember the name of the uh I don''t remember the name of the uh I
    don''t remember the name of the

    thing but bases things like transfusion thing but bases things like transfusion
    thing but bases things like transfusion

    in the same size and then this is like in the same size and then this is like
    in the same size and then this is like

    better basically and also I think better basically and also I think better basically
    and also I think

    another interesting thing that they uh another interesting thing that they uh
    another interesting thing that they uh

    showed in the paper is that like the the showed in the paper is that like the
    the showed in the paper is that like the the

    the tokens that it gets generated at the the tokens that it gets generated at
    the the tokens that it gets generated at the

    beginning. It''s like oftentimes they''ll beginning. It''s like oftentimes they''ll
    beginning. It''s like oftentimes they''ll

    generate like a lot of the most common generate like a lot of the most common
    generate like a lot of the most common

    tokens first like the something and then tokens first like the something and then
    tokens first like the something and then

    and then and then they generate like the and then and then they generate like
    the and then and then they generate like the

    most like important tokens and then and most like important tokens and then and
    most like important tokens and then and

    and then the the the image for example and then the the the image for example'
  concept_slugs:
  - discrete-diffusion
  - flow-matching
  - rectified-flow
- idx: 58
  start_sec: 2857.04
  end_sec: 2893.03
  text: 'and then the the the image for example

    like flower or like cat and then and like flower or like cat and then and like
    flower or like cat and then and

    then the the the the image are going to then the the the the image are going to
    then the the the the image are going to

    start to show like the flower silhouette start to show like the flower silhouette
    start to show like the flower silhouette

    and then once you have like more details and then once you have like more details
    and then once you have like more details

    about the flowers for example the color about the flowers for example the color
    about the flowers for example the color

    or I I guess color is also pretty pretty or I I guess color is also pretty pretty
    or I I guess color is also pretty pretty

    pretty primal I guess but like basically pretty primal I guess but like basically
    pretty primal I guess but like basically

    like what kind of flower or like what like what kind of flower or like what like
    what kind of flower or like what

    are the what kind of cat like what what are the what kind of cat like what what
    are the what kind of cat like what what

    is the what is it like the eye the the is the what is it like the eye the the
    is the what is it like the eye the the

    color of the eyes or something right color of the eyes or something right color
    of the eyes or something right

    then then like basically the details in then then like basically the details in
    then then like basically the details in

    the image and the text are kind of the image and the text are kind of the image
    and the text are kind of

    showing up at the same time so it''s like showing up at the same time so it''s
    like showing up at the same time so it''s like

    kind of interesting yeah kind of interesting yeah kind of interesting yeah

    >> what''s the point of like generating both >> what''s the point of like generating
    both >> what''s the point of like generating both

    text and like image at the same time'
  concept_slugs:
  - discrete-diffusion
  - flow-matching
  - rectified-flow
- idx: 59
  start_sec: 2893.03
  end_sec: 2929.2
  text: 'text and like image at the same time text and like image at the same time

    because like you start from nothing and because like you start from nothing and
    because like you start from nothing and

    then you ask the model to like generate then you ask the model to like generate
    then you ask the model to like generate

    random thing instead of like giving it a random thing instead of like giving it
    a random thing instead of like giving it a

    prompt to generate is it trying do like prompt to generate is it trying do like
    prompt to generate is it trying do like

    VQA. VQA. VQA.

    >> No, it''s trying to generate based on >> No, it''s trying to generate based
    on >> No, it''s trying to generate based on

    prompt. So like the the the first few prompt. So like the the the first few prompt.
    So like the the the first few

    tokens are the prompts. tokens are the prompts. tokens are the prompts.

    >> Yeah. Yeah. Yeah. Yeah. So so yeah. So >> Yeah. Yeah. Yeah. Yeah. So so yeah.
    So >> Yeah. Yeah. Yeah. Yeah. So so yeah. So

    you you will have some prompts. You''ll you you will have some prompts. You''ll
    you you will have some prompts. You''ll

    even have VQA, right? So you can read even have VQA, right? So you can read even
    have VQA, right? So you can read

    the image and also read prompts and the image and also read prompts and the image
    and also read prompts and

    stuff like that, right? So this is like stuff like that, right? So this is like
    stuff like that, right? So this is like

    what people call omni model uh so to what people call omni model uh so to what
    people call omni model uh so to

    speak. This is not omni yet but this is speak. This is not omni yet but this is
    speak. This is not omni yet but this is

    like kind of om like this is a towards like kind of om like this is a towards
    like kind of om like this is a towards

    the way to become omni but this is like the way to become omni but this is like'
  concept_slugs:
  - discrete-diffusion
  - flow-matching
  - rectified-flow
- idx: 60
  start_sec: 2929.2
  end_sec: 2990.88
  text: 'the way to become omni but this is like

    just like two two modalities I guess. just like two two modalities I guess. just
    like two two modalities I guess.

    Yeah. Yeah. Omni model just means that Yeah. Yeah. Omni model just means that
    Yeah. Yeah. Omni model just means that

    anything to anything. Yeah. All right. Cool. So, uh congratulations. All right.
    Cool. So, uh congratulations.

    you made it through this class. you made it through this class. you made it through
    this class.

    Now you''re a diffusion expert. Now you''re a diffusion expert. Now you''re a
    diffusion expert.

    But uh basically yeah so at the But uh basically yeah so at the But uh basically
    yeah so at the

    beginning this is what we said we were beginning this is what we said we were
    beginning this is what we said we were

    going to learn you know. So hopefully going to learn you know. So hopefully going
    to learn you know. So hopefully

    you guys have learned you know enough you guys have learned you know enough you
    guys have learned you know enough

    knowledge to be you know comfortable knowledge to be you know comfortable knowledge
    to be you know comfortable

    with many of or all of these concepts. with many of or all of these concepts.
    with many of or all of these concepts.

    So like the intuition, the math, how to So like the intuition, the math, how to
    So like the intuition, the math, how to

    implement them, how to use GPU, uh you implement them, how to use GPU, uh you
    implement them, how to use GPU, uh you

    know, stuff like that. And uh just a know, stuff like that. And uh just a know,
    stuff like that. And uh just a

    couple of notes here. Basically, all the couple of notes here. Basically, all
    the couple of notes here. Basically, all the

    resources that we post for this class resources that we post for this class resources
    that we post for this class

    will remain available forever on the will remain available forever on the will
    remain available forever on the

    internet. So the recordings uh even if internet. So the recordings uh even if
    internet. So the recordings uh even if

    you cannot access the ponapto anymore, you cannot access the ponapto anymore,'
  concept_slugs:
  - discrete-diffusion
  - flow-matching
  - rectified-flow
- idx: 61
  start_sec: 2990.88
  end_sec: 3025.599
  text: 'you cannot access the ponapto anymore,

    it''s still going to be on YouTube. Uh I it''s still going to be on YouTube. Uh
    I it''s still going to be on YouTube. Uh I

    kind of do some editing uh for the kind of do some editing uh for the kind of
    do some editing uh for the

    YouTube part so to to cut out some of YouTube part so to to cut out some of YouTube
    part so to to cut out some of

    the announcement parts and stuff like the announcement parts and stuff like the
    announcement parts and stuff like

    that so that you don''t need to waste that so that you don''t need to waste that
    so that you don''t need to waste

    time. Um yeah lecture slides of course time. Um yeah lecture slides of course
    time. Um yeah lecture slides of course

    website will be there the homework will website will be there the homework will
    website will be there the homework will

    be there although I don''t know if I want be there although I don''t know if I
    want be there although I don''t know if I want

    to share answer publicly if I want to re to share answer publicly if I want to
    re to share answer publicly if I want to re

    this class maybe this is not a good idea this class maybe this is not a good idea
    this class maybe this is not a good idea

    um but yeah and discord will just be um but yeah and discord will just be um but
    yeah and discord will just be

    there I guess all live probably not there I guess all live probably not there
    I guess all live probably not

    going to be as active but you know all going to be as active but you know all
    going to be as active but you know all

    the resources that we posted here is the resources that we posted here is the
    resources that we posted here is

    going to be there okay and now it is going to be there okay and now it is going
    to be there okay and now it is

    your turn to take what you''ve learned your turn to take what you''ve learned'
  concept_slugs:
  - discrete-diffusion
  - flow-matching
  - rectified-flow
- idx: 62
  start_sec: 3025.599
  end_sec: 3065.43
  text: 'your turn to take what you''ve learned

    into the real world so I will highly into the real world so I will highly into
    the real world so I will highly

    recommend if you are proud of what recommend if you are proud of what recommend
    if you are proud of what

    you''ve done especially in your you know you''ve done especially in your you know
    you''ve done especially in your you know

    homeworks three and four uh you can open homeworks three and four uh you can open
    homeworks three and four uh you can open

    source your code by uh making your source your code by uh making your source your
    code by uh making your

    GitHub repo public basically this is GitHub repo public basically this is GitHub
    repo public basically this is

    like you know one way to help the world like you know one way to help the world
    like you know one way to help the world

    or your AI agent to become a better one or your AI agent to become a better one
    or your AI agent to become a better one

    I guess um yeah another thing or I guess um yeah another thing or I guess um yeah
    another thing or

    actually I don''t know because your thing actually I don''t know because your
    thing actually I don''t know because your thing

    is also generated by AI agent maybe is also generated by AI agent maybe is also
    generated by AI agent maybe

    anyway um but but it''s a bug free anyway um but but it''s a bug free anyway um
    but but it''s a bug free

    version anyway another thing that you version anyway another thing that you version
    anyway another thing that you

    can consider doing is to turn your can consider doing is to turn your can consider
    doing is to turn your

    homework into a real research project so homework into a real research project
    so homework into a real research project so

    either it''s like a full like numerous either it''s like a full like numerous
    either it''s like a full like numerous

    paper or like a new workshop paper or paper or like a new workshop paper or paper
    or like a new workshop paper or

    something like that. I think it could be'
  concept_slugs:
  - discrete-diffusion
  - flow-matching
  - rectified-flow
- idx: 63
  start_sec: 3065.43
  end_sec: 3099.92
  text: 'something like that. I think it could be something like that. I think it
    could be

    a good experience if you guys are a good experience if you guys are a good experience
    if you guys are

    interested in getting into research. And interested in getting into research.
    And interested in getting into research. And

    one thing that you can do at the poster one thing that you can do at the poster
    one thing that you can do at the poster

    session is that like basically you can session is that like basically you can
    session is that like basically you can

    go around and see if there''s any people go around and see if there''s any people
    go around and see if there''s any people

    who are like you know doing the same who are like you know doing the same who
    are like you know doing the same

    thing as you and uh if you''re interested thing as you and uh if you''re interested
    thing as you and uh if you''re interested

    you can like basically do joint effort. you can like basically do joint effort.
    you can like basically do joint effort.

    This way like nobody needs to do like This way like nobody needs to do like This
    way like nobody needs to do like

    like a lot of work and then you can like a lot of work and then you can like a
    lot of work and then you can

    still get like a relatively large still get like a relatively large still get
    like a relatively large

    project uh together if you guys are project uh together if you guys are project
    uh together if you guys are

    solving the same kind of problem and uh solving the same kind of problem and uh
    solving the same kind of problem and uh

    obviously uh this is what I hope that obviously uh this is what I hope that obviously
    uh this is what I hope that

    you could you know use what you have you could you know use what you have you
    could you know use what you have

    learned in this class in your own learned in this class in your own learned in
    this class in your own

    research slash you know when you go to research slash you know when you go to'
  concept_slugs:
  - discrete-diffusion
  - flow-matching
  - rectified-flow
- idx: 64
  start_sec: 3099.92
  end_sec: 3145.44
  text: 'research slash you know when you go to

    the AGI company you know make the AGI a the AGI company you know make the AGI
    a the AGI company you know make the AGI a

    diffusion model please we don''t want to diffusion model please we don''t want
    to diffusion model please we don''t want to

    lose to the to the LM AGI guys you know lose to the to the LM AGI guys you know
    lose to the to the LM AGI guys you know

    just yeah yeah yeah but let let''s hope just yeah yeah yeah but let let''s hope
    just yeah yeah yeah but let let''s hope

    that that it happens that that it happens that that it happens

    Okay. But uh yeah, last chance for Okay. But uh yeah, last chance for Okay. But
    uh yeah, last chance for

    questions. Is there any remaining questions. Is there any remaining questions.
    Is there any remaining

    questions that we have questions that we have questions that we have

    about anything? Yeah. about anything? Yeah. about anything? Yeah.

    >> Block diffusion. >> Block diffusion. >> Block diffusion.

    >> What? What did you say? >> What? What did you say? >> What? What did you say?

    >> Block diffusion. >> Block diffusion.

    >> Block diffusion. Did didn''t we just go >> Block diffusion. Did didn''t we
    just go >> Block diffusion. Did didn''t we just go

    through that? through that? through that?

    >> Yeah. >> Yeah.

    >> Oh, okay. Yeah. >> Question was that we said that it''s >> Question was that
    we said that it''s

    going to be we can have like variable going to be we can have like variable going
    to be we can have like variable

    length of block diffusion, but the length of block diffusion, but the length of
    block diffusion, but the

    length of the block itself is fixed. length of the block itself is fixed. length
    of the block itself is fixed.

    Does it mean that it''s always going to Does it mean that it''s always going to
    Does it mean that it''s always going to

    be multiple? be multiple? be multiple?

    >> No, because you can discard >> No, because you can discard >> No, because you
    can discard

    >> padding tokens and tokens after the OS, >> padding tokens and tokens after
    the OS,'
  concept_slugs:
  - discrete-diffusion
  - flow-matching
  - rectified-flow
- idx: 65
  start_sec: 3145.44
  end_sec: 3186.47
  text: '>> padding tokens and tokens after the OS,

    right? right?

    >> Yeah. >> Yeah.

    >> Uh so one thing I implemented for >> Uh so one thing I implemented for >> Uh
    so one thing I implemented for

    homework 3 and like thing that took the homework 3 and like thing that took the
    homework 3 and like thing that took the

    longest time was generating the public longest time was generating the public
    longest time was generating the public

    data that that took like 5 hours data that that took like 5 hours data that that
    took like 5 hours

    >> which is like training probably took >> which is like training probably took
    >> which is like training probably took

    just two hours. just two hours. just two hours.

    >> So so one of the things I noticed is >> So so one of the things I noticed is
    >> So so one of the things I noticed is

    like obviously your generated data set like obviously your generated data set
    like obviously your generated data set

    is constrained by how good your 1 RF is constrained by how good your 1 RF is constrained
    by how good your 1 RF

    model is. Mhm. model is. Mhm. model is. Mhm.

    >> If that gets like a bad f then your >> If that gets like a bad f then your
    >> If that gets like a bad f then your

    generated sample is also pretty bad. generated sample is also pretty bad. generated
    sample is also pretty bad.

    >> So I was just wondering why do we do it >> So I was just wondering why do we
    do it >> So I was just wondering why do we do it

    this way where we sample noise and then this way where we sample noise and then
    this way where we sample noise and then

    generate an image. Can''t we like take generate an image. Can''t we like take
    generate an image. Can''t we like take

    images from cell and it''s all backwards? images from cell and it''s all backwards?
    images from cell and it''s all backwards?

    >> Of course you can definitely do that and >> Of course you can definitely do
    that and >> Of course you can definitely do that and

    I thought that''s what they did in'
  concept_slugs:
  - discrete-diffusion
  - flow-matching
  - rectified-flow
- idx: 66
  start_sec: 3186.47
  end_sec: 3222.309
  text: 'I thought that''s what they did in I thought that''s what they did in

    refflow but maybe not. If it''s not then refflow but maybe not. If it''s not then
    refflow but maybe not. If it''s not then

    this is a good way to improve it right. this is a good way to improve it right.
    this is a good way to improve it right.

    Obviously because like you obviously Obviously because like you obviously Obviously
    because like you obviously

    want to learn from real data, right? want to learn from real data, right? want
    to learn from real data, right?

    That that is like and also actually That that is like and also actually That that
    is like and also actually

    people have found that like if you train people have found that like if you train
    people have found that like if you train

    your diffusion model on generated on your diffusion model on generated on your
    diffusion model on generated on

    images that generate by diffusion is images that generate by diffusion is images
    that generate by diffusion is

    actually going to degrade your diffusion actually going to degrade your diffusion
    actually going to degrade your diffusion

    model''s quality. Yeah. So yeah, if if model''s quality. Yeah. So yeah, if if
    model''s quality. Yeah. So yeah, if if

    the I thought I thought getting the the I thought I thought getting the the I
    thought I thought getting the

    noise correspondence to the real data is noise correspondence to the real data
    is noise correspondence to the real data is

    what they did in reflow. But if not then what they did in reflow. But if not then
    what they did in reflow. But if not then

    this is a good way to improve it. this is a good way to improve it. this is a
    good way to improve it.

    >> I think they said that yeah they do do >> I think they said that yeah they
    do do >> I think they said that yeah they do do

    it the forward way. That''s why like a it the forward way. That''s why like a
    it the forward way. That''s why like a

    three RF model actually performs worse three RF model actually performs worse
    three RF model actually performs worse

    than a 2 RF model because the only'
  concept_slugs:
  - discrete-diffusion
  - flow-matching
  - rectified-flow
- idx: 67
  start_sec: 3222.309
  end_sec: 3259.44
  text: 'than a 2 RF model because the only than a 2 RF model because the only

    errors accumulate. errors accumulate. errors accumulate.

    >> Yeah. No, that''s your homework. Four. >> Yeah. No, that''s your homework.
    Four. >> Yeah. No, that''s your homework. Four.

    Nice. Okay. Yeah. Yeah. Yeah. Totally. I Nice. Okay. Yeah. Yeah. Yeah. Totally.
    I Nice. Okay. Yeah. Yeah. Yeah. Totally. I

    think that that make make total sense. think that that make make total sense.
    think that that make make total sense.

    Yeah. You can also add some like Yeah. You can also add some like Yeah. You can
    also add some like

    Yeah. Basically, you you can I don''t I Yeah. Basically, you you can I don''t
    I Yeah. Basically, you you can I don''t I

    don''t know if like there''s going to be don''t know if like there''s going to
    be don''t know if like there''s going to be

    any issues because like the the like the any issues because like the the like
    the any issues because like the the like the

    like the the X0 that you get from a like the the X0 that you get from a like the
    the X0 that you get from a

    model may or may not be well may or may model may or may not be well may or may
    model may or may not be well may or may

    not be on the gausian manifold. like you not be on the gausian manifold. like
    you not be on the gausian manifold. like you

    may need some regularization there. may need some regularization there. may need
    some regularization there.

    >> It''s like easier to be on the Gausian >> It''s like easier to be on the Gausian
    >> It''s like easier to be on the Gausian

    than that''s very true. That''s very true. than that''s very true. That''s very
    true. than that''s very true. That''s very true.

    Yeah. Yeah. So So I''m just saying that Yeah. Yeah. So So I''m just saying that
    Yeah. Yeah. So So I''m just saying that

    like maybe you need some regularization like maybe you need some regularization
    like maybe you need some regularization

    but but but

    in general I think that''s a better idea in general I think that''s a better idea'
  concept_slugs:
  - discrete-diffusion
  - flow-matching
  - rectified-flow
- idx: 68
  start_sec: 3259.44
  end_sec: 3303.51
  text: 'in general I think that''s a better idea

    than the normal the the the way that than the normal the the the way that than
    the normal the the the way that

    they they did. Okay. Any other question? they they did. Okay. Any other question?
    they they did. Okay. Any other question?

    Anything? Anything? Anything?

    >> Yeah. >> Yeah.

    >> You were hoping that diffusion promotion >> You were hoping that diffusion
    promotion >> You were hoping that diffusion promotion

    may overtake auto. may overtake auto. may overtake auto.

    >> I don''t know what I said. No, I said >> I don''t know what I said. No, I said
    >> I don''t know what I said. No, I said

    well that''s kind of what I said. I guess well that''s kind of what I said. I
    guess well that''s kind of what I said. I guess

    this was what I said but yeah continue. this was what I said but yeah continue.
    this was what I said but yeah continue.

    >> One of the strongest parts about >> One of the strongest parts about >> One
    of the strongest parts about

    anything that''s generally auto testing anything that''s generally auto testing
    anything that''s generally auto testing

    right now is that RL part that you right now is that RL part that you right now
    is that RL part that you

    mentioned that mentioned that mentioned that

    >> what are like some active works that >> what are like some active works that
    >> what are like some active works that

    deal deal deal

    maybe more so flow matching because maybe more so flow matching because maybe
    more so flow matching because

    diffusion can apply RL to some extent. diffusion can apply RL to some extent.
    diffusion can apply RL to some extent.

    >> Are there like some recent or >> Are there like some recent or >> Are there
    like some recent or

    interesting works that you think apply interesting works that you think apply
    interesting works that you think apply

    RL through flow matching or even methods RL through flow matching or even methods
    RL through flow matching or even methods

    you spoke about today that is discreet you spoke about today that is discreet
    you spoke about today that is discreet

    diffusion discrete? diffusion discrete? diffusion discrete?

    >> Yeah. Yeah. So actually there multiple'
  concept_slugs:
  - discrete-diffusion
  - flow-matching
  - rectified-flow
- idx: 69
  start_sec: 3303.51
  end_sec: 3349.359
  text: '>> Yeah. Yeah. So actually there multiple >> Yeah. Yeah. So actually there
    multiple

    uh so the most famous one in the uh so the most famous one in the uh so the most
    famous one in the

    robotics world is probably like FO I robotics world is probably like FO I robotics
    world is probably like FO I

    guess flow policy guess flow policy guess flow policy

    >> optimization all yeah yeah yeah good go >> optimization all yeah yeah yeah
    good go >> optimization all yeah yeah yeah good go

    I don''t really know FO uh but um well I don''t really know FO uh but um well
    I don''t really know FO uh but um well

    this yeah and you know my opinion about this yeah and you know my opinion about
    this yeah and you know my opinion about

    it um so there''s another um uh line of it um so there''s another um uh line of
    it um so there''s another um uh line of

    work uh that is called adjoin matching work uh that is called adjoin matching
    work uh that is called adjoin matching

    or adjoin sampling so basically what or adjoin sampling so basically what or adjoin
    sampling so basically what

    they did is that um they sort of like uh they did is that um they sort of like
    uh they did is that um they sort of like uh

    it''s it''s like very very similar to like it''s it''s like very very similar
    to like it''s it''s like very very similar to like

    like a gpo type of thing where um you like a gpo type of thing where um you like
    a gpo type of thing where um you

    you you have a bunch of like buffer the you you have a bunch of like buffer the
    you you have a bunch of like buffer the

    data and then you kind of like calculate data and then you kind of like calculate
    data and then you kind of like calculate

    the reward with those buffer data and the reward with those buffer data and the
    reward with those buffer data and

    then you figure out like how much then you figure out like how much then you figure
    out like how much

    gradient you should apply from those gradient you should apply from those'
  concept_slugs:
  - discrete-diffusion
  - flow-matching
  - rectified-flow
- idx: 70
  start_sec: 3349.359
  end_sec: 3385.91
  text: 'gradient you should apply from those

    buffer data to your current time to one buffer data to your current time to one
    buffer data to your current time to one

    of the time that you sampled. Um so this of the time that you sampled. Um so this
    of the time that you sampled. Um so this

    is like also one of the ways to do that is like also one of the ways to do that
    is like also one of the ways to do that

    like a drawing sampling addin matching. like a drawing sampling addin matching.
    like a drawing sampling addin matching.

    So this is like very very principled and So this is like very very principled
    and So this is like very very principled and

    they kind of derived from like the the they kind of derived from like the the
    they kind of derived from like the the

    stoastic control theory. Uh but it''s stoastic control theory. Uh but it''s stoastic
    control theory. Uh but it''s

    like it''s pretty like the mass is a like it''s pretty like the mass is a like
    it''s pretty like the mass is a

    little bit more complicated and it''s little bit more complicated and it''s little
    bit more complicated and it''s

    also a little bit more complicated to also a little bit more complicated to also
    a little bit more complicated to

    implement. This is why and and and tune implement. This is why and and and tune
    implement. This is why and and and tune

    I guess. So but but they have like I guess. So but but they have like I guess.
    So but but they have like

    strong connection with RL. So this is strong connection with RL. So this is strong
    connection with RL. So this is

    why but but this is like a good line of why but but this is like a good line of
    why but but this is like a good line of

    work that people have done and uh they work that people have done and uh they
    work that people have done and uh they

    you you need you mainly need like an SDE you you need you mainly need like an
    SDE you you need you mainly need like an SDE

    in that framework but you can turn you'
  concept_slugs:
  - discrete-diffusion
  - flow-matching
  - rectified-flow
- idx: 71
  start_sec: 3385.91
  end_sec: 3426.48
  text: 'in that framework but you can turn you in that framework but you can turn
    you

    can essentially turn an S OD like a flow can essentially turn an S OD like a flow
    can essentially turn an S OD like a flow

    OD into a SD by yeah basically just like OD into a SD by yeah basically just like
    OD into a SD by yeah basically just like

    adding adding some noise at every time adding adding some noise at every time
    adding adding some noise at every time

    step and then you can do it. So this is step and then you can do it. So this is
    step and then you can do it. So this is

    also like kind of how uh like basically also like kind of how uh like basically
    also like kind of how uh like basically

    the like basically the uh like like the the like basically the uh like like the
    the like basically the uh like like the

    the the the trendy way of doing um you the the the trendy way of doing um you
    the the the trendy way of doing um you

    know RL fine-tuning for flow models is know RL fine-tuning for flow models is
    know RL fine-tuning for flow models is

    kind of just you add some noise in the kind of just you add some noise in the
    kind of just you add some noise in the

    middle and then it becomes soastic and middle and then it becomes soastic and
    middle and then it becomes soastic and

    then you use a gausian proxy as the as then you use a gausian proxy as the as
    then you use a gausian proxy as the as

    the lo likelihood and there''s another the lo likelihood and there''s another
    the lo likelihood and there''s another

    thing that like we like by we I mean thing that like we like by we I mean thing
    that like we like by we I mean

    like my collaborator like me and my like my collaborator like me and my like my
    collaborator like me and my

    collaborator are trying to do is collaborator are trying to do is collaborator
    are trying to do is

    basically is there any other ways that basically is there any other ways that'
  concept_slugs:
  - discrete-diffusion
  - flow-matching
  - rectified-flow
- idx: 72
  start_sec: 3426.48
  end_sec: 3478.72
  text: 'basically is there any other ways that

    we can do it besides turning into a SDE we can do it besides turning into a SDE
    we can do it besides turning into a SDE

    um yeah so like let''s hope we can get um yeah so like let''s hope we can get
    um yeah so like let''s hope we can get

    this done by nearest but uh yeah but this done by nearest but uh yeah but this
    done by nearest but uh yeah but

    this is like kind that''s this is like kind that''s this is like kind that''s

    our prior work on the fast likelihood uh our prior work on the fast likelihood
    uh our prior work on the fast likelihood uh

    estimation thing. Yeah. Yeah. So so that estimation thing. Yeah. Yeah. So so that
    estimation thing. Yeah. Yeah. So so that

    that may or may not be able to get done. that may or may not be able to get done.
    that may or may not be able to get done.

    Yeah. Yeah.

    Okay. Uh Okay. Uh Okay. Uh

    any other question? Yeah,

    >> we learned a lot about the onestep >> we learned a lot about the onestep >>
    we learned a lot about the onestep

    generation for images being done for generation for images being done for generation
    for images being done for

    like onestep like onestep like onestep

    >> text diffusion. >> text diffusion. >> text diffusion.

    >> Yes. Wow, that''s such a great question. >> Yes. Wow, that''s such a great
    question. >> Yes. Wow, that''s such a great question.

    Sorry. This is a very great question Sorry. This is a very great question Sorry.
    This is a very great question

    actually like three days ago. Um this is actually like three days ago. Um this
    is actually like three days ago. Um this is

    super exciting actually. So three days super exciting actually. So three days
    super exciting actually. So three days

    ago people on Twitter uh have posted a ago people on Twitter uh have posted a
    ago people on Twitter uh have posted a

    new paper called discrete flow maps. And new paper called discrete flow maps.
    And new paper called discrete flow maps. And

    essentially you just sort of like uh essentially you just sort of like uh'
  concept_slugs:
  - discrete-diffusion
  - flow-matching
  - rectified-flow
- idx: 73
  start_sec: 3478.72
  end_sec: 3517.68
  text: 'essentially you just sort of like uh

    they sort of extend the flow map uh uh they sort of extend the flow map uh uh
    they sort of extend the flow map uh uh

    what you call framework into the what you call framework into the what you call
    framework into the

    discrete case and then it has all the discrete case and then it has all the discrete
    case and then it has all the

    connection that we learned about today. connection that we learned about today.
    connection that we learned about today.

    And basically what they did is that like And basically what they did is that like
    And basically what they did is that like

    you can kind of convert everything into you can kind of convert everything into
    you can kind of convert everything into

    something cross entropy again and it''s something cross entropy again and it''s
    something cross entropy again and it''s

    like super super interesting. I highly like super super interesting. I highly
    like super super interesting. I highly

    recommend everyone to read it. Uh, and I recommend everyone to read it. Uh, and
    I recommend everyone to read it. Uh, and I

    don''t know if I can say this, but I hope don''t know if I can say this, but I
    hope don''t know if I can say this, but I hope

    at by the time that I post this online at by the time that I post this online
    at by the time that I post this online

    that it''s already out there, but Nick that it''s already out there, but Nick
    that it''s already out there, but Nick

    Nick Buffy, uh, the professor Nick Buffy Nick Buffy, uh, the professor Nick Buffy
    Nick Buffy, uh, the professor Nick Buffy

    from MLDD told me that he''s working on from MLDD told me that he''s working on
    from MLDD told me that he''s working on

    something that''s like super duper something that''s like super duper something
    that''s like super duper

    related to that as well. And they related to that as well. And they related to
    that as well. And they

    supposed to post it online this week. supposed to post it online this week. supposed
    to post it online this week.

    Uh, so let''s see if he actually post it Uh, so let''s see if he actually post
    it'
  concept_slugs:
  - discrete-diffusion
  - flow-matching
  - rectified-flow
- idx: 74
  start_sec: 3517.68
  end_sec: 3559.119
  text: 'Uh, so let''s see if he actually post it

    online this week. Uh, but yeah, I don''t online this week. Uh, but yeah, I don''t
    online this week. Uh, but yeah, I don''t

    actually know how how he did it, but actually know how how he did it, but actually
    know how how he did it, but

    apparently we have something coming out apparently we have something coming out
    apparently we have something coming out

    of CMU that is like related to that as of CMU that is like related to that as
    of CMU that is like related to that as

    well. Yeah. Any other questions? But well. Yeah. Any other questions? But well.
    Yeah. Any other questions? But

    yeah, great question. I forgot to yeah, great question. I forgot to yeah, great
    question. I forgot to

    mention that this is like I meant to mention that this is like I meant to mention
    that this is like I meant to

    make a slide for this but I forgot. make a slide for this but I forgot. make a
    slide for this but I forgot.

    Anyway, any other things? >> Recent drifting model. >> Recent drifting model.

    >> I think the drifting model is super >> I think the drifting model is super
    >> I think the drifting model is super

    novel. I think this is like an novel. I think this is like an novel. I think this
    is like an

    interesting way um to think about J interesting way um to think about J interesting
    way um to think about J

    modeling. But I don''t think this is like modeling. But I don''t think this is
    like modeling. But I don''t think this is like

    that closely related to diffusion or that closely related to diffusion or that
    closely related to diffusion or

    anything that we saw. I think it''s more anything that we saw. I think it''s more
    anything that we saw. I think it''s more

    related to I think um the luma talk related to I think um the luma talk related
    to I think um the luma talk

    actually talked about it, right? is kind actually talked about it, right? is kind
    actually talked about it, right? is kind

    of similar to uh one of the other of similar to uh one of the other'
  concept_slugs:
  - discrete-diffusion
  - flow-matching
  - rectified-flow
- idx: 75
  start_sec: 3559.119
  end_sec: 3602.88
  text: 'of similar to uh one of the other

    previous uh framework and equilibrium previous uh framework and equilibrium previous
    uh framework and equilibrium

    model. So equilibrium model is something model. So equilibrium model is something
    model. So equilibrium model is something

    that also CMU developed actually is from that also CMU developed actually is from
    that also CMU developed actually is from

    my lab. Um yeah but basically what you my lab. Um yeah but basically what you
    my lab. Um yeah but basically what you

    do is like you kind of treat um do is like you kind of treat um do is like you
    kind of treat um

    basically you just kind of have like a basically you just kind of have like a
    basically you just kind of have like a

    recurrent of model like oh actually this recurrent of model like oh actually this
    recurrent of model like oh actually this

    is not even equilibrium model I guess is not even equilibrium model I guess is
    not even equilibrium model I guess

    this is like equilibrium in a different this is like equilibrium in a different
    this is like equilibrium in a different

    dimension but like basically you''re dimension but like basically you''re dimension
    but like basically you''re

    trying to reach some sort of equilibrium trying to reach some sort of equilibrium
    trying to reach some sort of equilibrium

    in your training. Yeah, this I guess in your training. Yeah, this I guess in your
    training. Yeah, this I guess

    this is not even equilibrium model. Um, this is not even equilibrium model. Um,
    this is not even equilibrium model. Um,

    but yeah, I think this is like super but yeah, I think this is like super but
    yeah, I think this is like super

    novel. Not entirely sure if this is like novel. Not entirely sure if this is like
    novel. Not entirely sure if this is like

    super related to what we see, but I super related to what we see, but I super
    related to what we see, but I

    think the underlying uh, you know, vibe think the underlying uh, you know, vibe
    think the underlying uh, you know, vibe

    or the underlying uh, you know, uh, math or the underlying uh, you know, uh, math'
  concept_slugs:
  - discrete-diffusion
  - flow-matching
  - rectified-flow
- idx: 76
  start_sec: 3602.88
  end_sec: 3645.64
  text: 'or the underlying uh, you know, uh, math

    is a little bit related, but like this is a little bit related, but like this
    is a little bit related, but like this

    is definitely something new. I think is definitely something new. I think is definitely
    something new. I think

    drift model. Yeah. drift model. Yeah. drift model. Yeah.

    or or or something coming from some or or or something coming from some or or
    or something coming from some

    other 2015 paper as people have been on other 2015 paper as people have been on
    other 2015 paper as people have been on

    Twitter have you know have discussed. Twitter have you know have discussed. Twitter
    have you know have discussed.

    Yeah. Yeah.

    Any other thing? Nothing. Nothing.

    All right. Cool. Final reminder, come to All right. Cool. Final reminder, come
    to All right. Cool. Final reminder, come to

    poster sessions and everything. All poster sessions and everything. All poster
    sessions and everything. All

    right. Thanks everyone for joining me in right. Thanks everyone for joining me
    in right. Thanks everyone for joining me in

    this class. Now go explore the world. this class. Now go explore the world. this
    class. Now go explore the world.

    All right. That''s it. All right. That''s it. All right. That''s it.

    Okay. Thank you. Thank you.'
  concept_slugs:
  - discrete-diffusion
  - flow-matching
  - rectified-flow
---
# CMU 10799 S26: Lecture 13 - Discrete Flow Matching & Edit Flow - Diffusion & Flow Matching

See the structured chunks above.
