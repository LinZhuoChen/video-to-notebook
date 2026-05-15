---
course_slug: cmu-10799-diffusion-flow
idx: 5
title: 'CMU 10799 S26: Lecture 5 - Flow Matching - Diffusion & Flow Matching'
video_url: https://www.youtube.com/watch?v=_OOITDB2VCY
duration_sec: null
chunks:
- idx: 0
  start_sec: 2.4699999999999998
  end_sec: 52.559
  text: 'So last time we learned about how So last time we learned about how

    diffusion turn noise into data by diffusion turn noise into data by diffusion
    turn noise into data by

    gradually adding noise and gradually gradually adding noise and gradually gradually
    adding noise and gradually

    denoising. denoising. denoising.

    H and then we learned another family of H and then we learned another family of
    H and then we learned another family of

    model called a scorebased models which model called a scorebased models which
    model called a scorebased models which

    is uh doing very very similar things and is uh doing very very similar things
    and is uh doing very very similar things and

    it turns out that they''re they''re pretty it turns out that they''re they''re
    pretty it turns out that they''re they''re pretty

    much the same. Um if you especially uh much the same. Um if you especially uh
    much the same. Um if you especially uh

    if you scale the number of time steps to if you scale the number of time steps
    to if you scale the number of time steps to

    infinite and then they all they both infinite and then they all they both infinite
    and then they all they both

    becomes this thing called stochastic becomes this thing called stochastic becomes
    this thing called stochastic

    process a continuous time stoastic process a continuous time stoastic process
    a continuous time stoastic

    process which can be sort of formulated process which can be sort of formulated
    process which can be sort of formulated

    into stoastic differential equations. into stoastic differential equations. into
    stoastic differential equations.

    All right. So and if you have a forward All right. So and if you have a forward
    All right. So and if you have a forward

    SDE uh then you actually directly have a SDE uh then you actually directly have
    a SDE uh then you actually directly have a

    formula to uh tell you what your reverse formula to uh tell you what your reverse
    formula to uh tell you what your reverse

    process should be which is also defined process should be which is also defined
    process should be which is also defined

    by an SDE with this score function and by an SDE with this score function and'
  concept_slugs:
  - continuous-normalizing-flow
  - flow-matching
  - velocity-field
- idx: 1
  start_sec: 52.559
  end_sec: 101.68
  text: 'by an SDE with this score function and

    then we can just do score matching to then we can just do score matching to then
    we can just do score matching to

    learn uh how to solve the uh the learn uh how to solve the uh the learn uh how
    to solve the uh the

    reversed SDE. reversed SDE. reversed SDE.

    All right. So, that was like the last All right. So, that was like the last All
    right. So, that was like the last

    question question question

    that we had in class. It''s like, is that we had in class. It''s like, is that
    we had in class. It''s like, is

    there a simpler way to do this? And I there a simpler way to do this? And I there
    a simpler way to do this? And I

    think someone after they took the quiz, think someone after they took the quiz,
    think someone after they took the quiz,

    they were already be like, "Oh, I I feel they were already be like, "Oh, I I feel
    they were already be like, "Oh, I I feel

    like I feel like there should be an like I feel like there should be an like I
    feel like there should be an

    easier way." Um, yeah. So, this is what easier way." Um, yeah. So, this is what
    easier way." Um, yeah. So, this is what

    we''re going to learn today. Okay. So, uh we''re going to learn today. Okay. So,
    uh we''re going to learn today. Okay. So, uh

    let''s think about this question. Let''s let''s think about this question. Let''s
    let''s think about this question. Let''s

    say we''re given a data point. So, we we say we''re given a data point. So, we
    we say we''re given a data point. So, we we

    only have like one image, right? What only have like one image, right? What only
    have like one image, right? What

    would be the simplest way to construct a would be the simplest way to construct
    a would be the simplest way to construct a

    trajectory from noise to this data trajectory from noise to this data trajectory
    from noise to this data

    point? Yeah, point? Yeah, point? Yeah,

    linear combination. linear combination. linear combination.

    That''s exactly correct. Okay. Why don''t That''s exactly correct. Okay. Why don''t'
  concept_slugs:
  - continuous-normalizing-flow
  - flow-matching
  - velocity-field
- idx: 2
  start_sec: 101.68
  end_sec: 146.4
  text: 'That''s exactly correct. Okay. Why don''t

    we just do linear interpolation of the we just do linear interpolation of the
    we just do linear interpolation of the

    two things, right? Um so exact how two things, right? Um so exact how two things,
    right? Um so exact how

    exactly you can do it is basically um exactly you can do it is basically um exactly
    you can do it is basically um

    say like bas you just like at the say like bas you just like at the say like bas
    you just like at the

    beginning of time you''ll have like it''s beginning of time you''ll have like
    it''s beginning of time you''ll have like it''s

    so this noise is fixed and then you have so this noise is fixed and then you have
    so this noise is fixed and then you have

    like a large portion of noise mixed with like a large portion of noise mixed with
    like a large portion of noise mixed with

    some portion of data and then you get a some portion of data and then you get
    a some portion of data and then you get a

    very noisy data and then as you go on very noisy data and then as you go on very
    noisy data and then as you go on

    the portion of the noise become fewer the portion of the noise become fewer the
    portion of the noise become fewer

    like less and less and then the portion like less and less and then the portion
    like less and less and then the portion

    of data become more and more uh and then of data become more and more uh and then
    of data become more and more uh and then

    you just construct a chain of you just construct a chain of you just construct
    a chain of

    the very noisy to slightly no to the very noisy to slightly no to the very noisy
    to slightly no to

    slightly less noisy to very very clean slightly less noisy to very very clean
    slightly less noisy to very very clean

    data. Right? So you could just construct data. Right? So you could just construct
    data. Right? So you could just construct

    this trajectory in this way. Um yeah so this trajectory in this way. Um yeah so'
  concept_slugs:
  - continuous-normalizing-flow
  - flow-matching
  - velocity-field
- idx: 3
  start_sec: 146.4
  end_sec: 208.309
  text: 'this trajectory in this way. Um yeah so

    remember the same noise same data. remember the same noise same data. remember
    the same noise same data.

    Then learning the transformation along Then learning the transformation along
    Then learning the transformation along

    this linear trajectory is super easy, this linear trajectory is super easy, this
    linear trajectory is super easy,

    right? Because literally what we can do right? Because literally what we can do
    right? Because literally what we can do

    is say now we want to uh now we want to is say now we want to uh now we want to
    is say now we want to uh now we want to

    um transfer transform from uh time 25% um transfer transform from uh time 25%
    um transfer transform from uh time 25%

    to time 50%. uh then what can we do is to time 50%. uh then what can we do is
    to time 50%. uh then what can we do is

    we can we literally just have you just we can we literally just have you just
    we can we literally just have you just

    need to add 25% more of data and then need to add 25% more of data and then need
    to add 25% more of data and then

    minus 25% minus 25% minus 25%

    uh of of the noise right um so basically uh of of the noise right um so basically
    uh of of the noise right um so basically

    and because the delta t is the same so and because the delta t is the same so
    and because the delta t is the same so

    you can write it in this way basically you can write it in this way basically
    you can write it in this way basically

    just like the just like the just like the

    uh the the noisy sample at time uh 0.5 uh the the noisy sample at time uh 0.5
    uh the the noisy sample at time uh 0.5

    is equal to uh the noisy sample at time is equal to uh the noisy sample at time
    is equal to uh the noisy sample at time

    0.25 plus how much time you want to 0.25 plus how much time you want to 0.25 plus
    how much time you want to

    progress. So like 0.25 time um times uh'
  concept_slugs:
  - continuous-normalizing-flow
  - flow-matching
  - velocity-field
- idx: 4
  start_sec: 208.309
  end_sec: 260.069
  text: 'progress. So like 0.25 time um times uh progress. So like 0.25 time um times
    uh

    data minus noise, right? Uh so basically data minus noise, right? Uh so basically
    data minus noise, right? Uh so basically

    uh generalizing it into t and delta t. uh generalizing it into t and delta t.
    uh generalizing it into t and delta t.

    This is like what you should get. And uh This is like what you should get. And
    uh This is like what you should get. And uh

    literally when the delta t goes to zero literally when the delta t goes to zero
    literally when the delta t goes to zero

    then you will have this velocity thing then you will have this velocity thing
    then you will have this velocity thing

    right. Basically this is just like tells right. Basically this is just like tells
    right. Basically this is just like tells

    the velocity thing. just tells you the velocity thing. just tells you the velocity
    thing. just tells you

    infinite testimony infinite testimony infinite testimony

    uh if you take infinite testimony small uh if you take infinite testimony small
    uh if you take infinite testimony small

    steps like what is the direction that steps like what is the direction that steps
    like what is the direction that

    you should go and no matter what t you should go and no matter what t you should
    go and no matter what t

    you''re at no matter which time step you''re at no matter which time step you''re
    at no matter which time step

    you''re at you''re always going like the you''re at you''re always going like
    the you''re at you''re always going like the

    same speed same direction right so it same speed same direction right so it same
    speed same direction right so it

    just like always going to be the just like always going to be the just like always
    going to be the

    difference between the data and noise difference between the data and noise difference
    between the data and noise

    which is x1 minus minus x0 which is x1 minus minus x0 which is x1 minus minus
    x0

    okay any questions okay any questions okay any questions

    pretty straightforward right okay So pretty straightforward right okay So pretty
    straightforward right okay So

    this is literally what we need to learn,'
  concept_slugs:
  - continuous-normalizing-flow
  - flow-matching
  - velocity-field
- idx: 5
  start_sec: 260.069
  end_sec: 317.6
  text: 'this is literally what we need to learn, this is literally what we need to
    learn,

    right? This is like literally the only right? This is like literally the only
    right? This is like literally the only

    thing that that''s stopping us from thing that that''s stopping us from thing
    that that''s stopping us from

    directly getting from noise to data. So directly getting from noise to data. So
    directly getting from noise to data. So

    basically the simplest way essentially basically the simplest way essentially
    basically the simplest way essentially

    to transform noise straight into data to transform noise straight into data to
    transform noise straight into data

    will be at training time. will be at training time. will be at training time.

    You first sample a noise and then you You first sample a noise and then you You
    first sample a noise and then you

    sample a data and then you uniformly sample a data and then you uniformly sample
    a data and then you uniformly

    sample a time step and then you compute sample a time step and then you compute
    sample a time step and then you compute

    a noisy sample by doing this linear a noisy sample by doing this linear a noisy
    sample by doing this linear

    interpolation interpolation interpolation

    and then you compute the velocity which and then you compute the velocity which
    and then you compute the velocity which

    is x1 - x0 just data minus noise and is x1 - x0 just data minus noise and is x1
    - x0 just data minus noise and

    then you learn a then you learn a then you learn a

    to match this velocity to match this velocity to match this velocity

    and at sampling time after you learn and at sampling time after you learn and
    at sampling time after you learn

    this literally you can just start from t this literally you can just start from
    t this literally you can just start from t

    equals z and then sample a noise at time equals z and then sample a noise at time
    equals z and then sample a noise at time

    zero zero zero

    and then progress through the chain. and then progress through the chain. and
    then progress through the chain.

    Right? How do you progress through the Right? How do you progress through the'
  concept_slugs:
  - continuous-normalizing-flow
  - flow-matching
  - velocity-field
- idx: 6
  start_sec: 317.6
  end_sec: 386.16
  text: 'Right? How do you progress through the

    chain? You just compute the displacement chain? You just compute the displacement
    chain? You just compute the displacement

    for x and then directly apply the for x and then directly apply the for x and
    then directly apply the

    displacement to your x to progress on displacement to your x to progress on displacement
    to your x to progress on

    the chain and then also progress in time the chain and then also progress in time
    the chain and then also progress in time

    steps and at the end just output x1. steps and at the end just output x1. steps
    and at the end just output x1.

    Okay. Question. Okay. Question. Okay. Question.

    somewhere and I''m concerned that this noise has no and I''m concerned that this
    noise has no

    semantic meaning. So would it get like semantic meaning. So would it get like
    semantic meaning. So would it get like

    like there''s no reason why a particular like there''s no reason why a particular
    like there''s no reason why a particular

    gausian noise shouldn''t amount to the gausian noise shouldn''t amount to the
    gausian noise shouldn''t amount to the

    rather than the house? rather than the house? rather than the house?

    >> Cool question. We''re going to we''re >> Cool question. We''re going to we''re
    >> Cool question. We''re going to we''re

    going to learn that today. Uh first of going to learn that today. Uh first of
    going to learn that today. Uh first of

    all, we''re not trying to get any all, we''re not trying to get any all, we''re
    not trying to get any

    semantic meaning here. We''re just trying semantic meaning here. We''re just trying
    semantic meaning here. We''re just trying

    to transform noise into data. But second to transform noise into data. But second
    to transform noise into data. But second

    of all, uh I think we''re going to like of all, uh I think we''re going to like
    of all, uh I think we''re going to like

    answer your question um later today. answer your question um later today. answer
    your question um later today.

    Okay, any other questions? Ah, now you have flow matching. This is Ah, now you
    have flow matching. This is

    full matching. Class is over. Hey, full matching. Class is over. Hey,'
  concept_slugs:
  - continuous-normalizing-flow
  - flow-matching
  - velocity-field
- idx: 7
  start_sec: 386.16
  end_sec: 430.0
  text: 'full matching. Class is over. Hey,

    no, not really. Okay, fine. Uh but no, not really. Okay, fine. Uh but no, not
    really. Okay, fine. Uh but

    basically the the question that we''re basically the the question that we''re
    basically the the question that we''re

    gonna ask is that like this is so gonna ask is that like this is so gonna ask
    is that like this is so

    simple, right? Like no math, no nothing. simple, right? Like no math, no nothing.
    simple, right? Like no math, no nothing.

    Like why do we like why do we need all Like why do we like why do we need all
    Like why do we like why do we need all

    those previous diffusion math like those previous diffusion math like those previous
    diffusion math like

    stoastic differential equations? Why do stoastic differential equations? Why do
    stoastic differential equations? Why do

    we need this? Like also why is this even we need this? Like also why is this even
    we need this? Like also why is this even

    valid? Why why why is this the same? Why valid? Why why why is this the same?
    Why valid? Why why why is this the same? Why

    can we even do this? Right? If we can can we even do this? Right? If we can can
    we even do this? Right? If we can

    just do this, why do we need to do all just do this, why do we need to do all
    just do this, why do we need to do all

    the math? Uh well, turns out that thing the math? Uh well, turns out that thing
    the math? Uh well, turns out that thing

    also come from math. So we''re going to also come from math. So we''re going to
    also come from math. So we''re going to

    learn about the math now. And to understand why this is a proper And to understand
    why this is a proper

    um probabilistic gener model we need to um probabilistic gener model we need to
    um probabilistic gener model we need to

    go back in time into the time when go back in time into the time when go back
    in time into the time when

    people start to de develop this thing. people start to de develop this thing.'
  concept_slugs:
  - continuous-normalizing-flow
  - flow-matching
  - velocity-field
- idx: 8
  start_sec: 430.0
  end_sec: 485.99
  text: 'people start to de develop this thing.

    Okay. So basically back in 2018 there Okay. So basically back in 2018 there Okay.
    So basically back in 2018 there

    this like pretty seminal paper um uh this like pretty seminal paper um uh this
    like pretty seminal paper um uh

    called continuous normalizing or or like called continuous normalizing or or like
    called continuous normalizing or or like

    neuro neuroordinary differential neuro neuroordinary differential neuro neuroordinary
    differential

    equation and then basically um this guy equation and then basically um this guy
    equation and then basically um this guy

    Ricky who was my uh meta intermentor Ricky who was my uh meta intermentor Ricky
    who was my uh meta intermentor

    actually super legendary guy but actually super legendary guy but actually super
    legendary guy but

    basically he was like um proposed this basically he was like um proposed this
    basically he was like um proposed this

    thing called continuous normalizing thing called continuous normalizing thing
    called continuous normalizing

    flows and it''s basically just like uh flows and it''s basically just like uh
    flows and it''s basically just like uh

    formulated a general model such that formulated a general model such that formulated
    a general model such that

    transform uh the samples from an initial transform uh the samples from an initial
    transform uh the samples from an initial

    distribution such as like a gausian to a distribution such as like a gausian to
    a distribution such as like a gausian to a

    target distribution such as the image target distribution such as the image target
    distribution such as the image

    distribution that we want by integrating distribution that we want by integrating
    distribution that we want by integrating

    through an OD through an OD through an OD

    and this OD is literally just the you and this OD is literally just the you and
    this OD is literally just the you

    know the infinite decimal uh change of know the infinite decimal uh change of
    know the infinite decimal uh change of

    your data should follow the velocity and your data should follow the velocity
    and your data should follow the velocity and

    at sampling time what you can do is you at sampling time what you can do is you
    at sampling time what you can do is you

    can just solve this OD by integrating'
  concept_slugs:
  - continuous-normalizing-flow
  - flow-matching
  - velocity-field
- idx: 9
  start_sec: 485.99
  end_sec: 535.839
  text: 'can just solve this OD by integrating can just solve this OD by integrating

    through uh the velocity and then you through uh the velocity and then you through
    uh the velocity and then you

    you''ll be able to get a sample or like a you''ll be able to get a sample or like
    a you''ll be able to get a sample or like a

    trajectory of samples. Uh trajectory of samples. Uh trajectory of samples. Uh

    so basically this is like literally what so basically this is like literally what
    so basically this is like literally what

    we just did, right? So you have some we just did, right? So you have some we just
    did, right? So you have some

    velocity and then you just like velocity and then you just like velocity and then
    you just like

    numerically is solve the OD at sampling numerically is solve the OD at sampling
    numerically is solve the OD at sampling

    time. time. time.

    Okay. So like how to interpret this, Okay. So like how to interpret this, Okay.
    So like how to interpret this,

    right? So basically just like think of right? So basically just like think of
    right? So basically just like think of

    it as like the wind flow transport some it as like the wind flow transport some
    it as like the wind flow transport some

    like water some amount of water from the like water some amount of water from
    the like water some amount of water from the

    west coast to the east coast or from west coast to the east coast or from west
    coast to the east coast or from

    like the Pacific Ocean to the uh to the like the Pacific Ocean to the uh to the
    like the Pacific Ocean to the uh to the

    east coast let''s just say and um the east coast let''s just say and um the east
    coast let''s just say and um the

    question here is that why this is a question here is that why this is a question
    here is that why this is a

    normalizing flow normalizing flow normalizing flow

    first of all like what is a normalizing first of all like what is a normalizing
    first of all like what is a normalizing

    flow? Anyone else I haven''t talked to today?'
  concept_slugs:
  - continuous-normalizing-flow
  - flow-matching
  - velocity-field
- idx: 10
  start_sec: 535.839
  end_sec: 590.949
  text: 'Anyone else I haven''t talked to today?

    Nobody remember what is normalizing Nobody remember what is normalizing Nobody
    remember what is normalizing

    flow? >> You can reconstruct the process. >> You can reconstruct the process.

    >> Yes. So it''s a invertible uh generate >> Yes. So it''s a invertible uh generate
    >> Yes. So it''s a invertible uh generate

    model, right? Yes. And the reason why model, right? Yes. And the reason why model,
    right? Yes. And the reason why

    this is a normalizing flow is because this is a normalizing flow is because this
    is a normalizing flow is because

    the streams never cross. So imagine how the streams never cross. So imagine how
    the streams never cross. So imagine how

    like you''re following a stream of river like you''re following a stream of river
    like you''re following a stream of river

    or like water or like the stream of the or like water or like the stream of the
    or like water or like the stream of the

    wind, right? Like if you just follow the wind, right? Like if you just follow
    the wind, right? Like if you just follow the

    stream, the stream will never like it stream, the stream will never like it stream,
    the stream will never like it

    will always point to one direction. So will always point to one direction. So
    will always point to one direction. So

    it will never like just get get it will never like just get get it will never
    like just get get

    if you just like follow the wind, you''re if you just like follow the wind, you''re
    if you just like follow the wind, you''re

    able to basically get from one point to able to basically get from one point to
    able to basically get from one point to

    the other point guaranteed. the other point guaranteed. the other point guaranteed.

    So like deterministically and because So like deterministically and because So
    like deterministically and because

    this process is deterministic, if you this process is deterministic, if you this
    process is deterministic, if you

    follow this wind, if you follow this follow this wind, if you follow this follow
    this wind, if you follow this

    flow, you''re actually going to get an flow, you''re actually going to get an
    flow, you''re actually going to get an

    invertible transformation because'
  concept_slugs:
  - continuous-normalizing-flow
  - flow-matching
  - velocity-field
- idx: 11
  start_sec: 590.949
  end_sec: 661.279
  text: 'invertible transformation because invertible transformation because

    everything is deterministic. everything is deterministic. everything is deterministic.

    Okay, any question? Okay, any question? Okay, any question?

    Cool. You have a question. Okay. Are we Cool. You have a question. Okay. Are we
    Cool. You have a question. Okay. Are we

    saying that it''s actually saying that it''s actually saying that it''s actually

    >> uh the way that we construct it is is it the way that we construct it is is
    it

    yeah it is invertible. Yeah the way that yeah it is invertible. Yeah the way that
    yeah it is invertible. Yeah the way that

    we construct it. Okay. we construct it. Okay. we construct it. Okay.

    Any more question? Cool. All right. Cool. All right.

    Uh okay. Okay. So how does this connect Uh okay. Okay. So how does this connect
    Uh okay. Okay. So how does this connect

    to probability? to probability? to probability?

    Well, basically in order to for this Well, basically in order to for this Well,
    basically in order to for this

    kind of like continuous flow thing model kind of like continuous flow thing model
    kind of like continuous flow thing model

    to transport between one probability to transport between one probability to transport
    between one probability

    distribution to another we need to have distribution to another we need to have
    distribution to another we need to have

    the following assumptions. The first the following assumptions. The first the
    following assumptions. The first

    thing is what we call the conservation thing is what we call the conservation
    thing is what we call the conservation

    of mass. Basically just imagine that the of mass. Basically just imagine that
    the of mass. Basically just imagine that the

    the wind carried a certain amount of the wind carried a certain amount of the
    wind carried a certain amount of

    water and this certain amount of water water and this certain amount of water
    water and this certain amount of water

    never change like the amount of water never change like the amount of water never
    change like the amount of water

    that you transporting never change. So that you transporting never change. So
    that you transporting never change. So

    no new mass uh is is going to get added no new mass uh is is going to get added'
  concept_slugs:
  - continuous-normalizing-flow
  - flow-matching
  - velocity-field
- idx: 12
  start_sec: 661.279
  end_sec: 710.959
  text: 'no new mass uh is is going to get added

    and no mass is going to disappear and no mass is going to disappear and no mass
    is going to disappear

    getting dropped. So like translate it getting dropped. So like translate it getting
    dropped. So like translate it

    into probabilistic statement just means into probabilistic statement just means
    into probabilistic statement just means

    that the probability should always add that the probability should always add
    that the probability should always add

    up to one because otherwise it won''t be up to one because otherwise it won''t
    be up to one because otherwise it won''t be

    a valid probability distribution. And a valid probability distribution. And a
    valid probability distribution. And

    then second thing is what we call the then second thing is what we call the then
    second thing is what we call the

    continuity equation which is like not continuity equation which is like not continuity
    equation which is like not

    only that the mass is conserved it''s only that the mass is conserved it''s only
    that the mass is conserved it''s

    also not you cannot teleport them uh also not you cannot teleport them uh also
    not you cannot teleport them uh

    which means that everything need to move which means that everything need to move
    which means that everything need to move

    smoothly everything should move like smoothly everything should move like smoothly
    everything should move like

    continuously continuously continuously

    okay so basically just means that the okay so basically just means that the okay
    so basically just means that the

    probability can only get changed probability can only get changed probability
    can only get changed

    continuously you cannot just like jump continuously you cannot just like jump
    continuously you cannot just like jump

    from from point to point because it''s from from point to point because it''s
    from from point to point because it''s

    it''s a river okay any question it''s a river okay any question it''s a river
    okay any question

    cool all right Um so because of this we cool all right Um so because of this we
    cool all right Um so because of this we

    get to define something called a get to define something called a get to define
    something called a

    probability flux. So imagine a flux is probability flux. So imagine a flux is'
  concept_slugs:
  - continuous-normalizing-flow
  - flow-matching
  - velocity-field
- idx: 13
  start_sec: 710.959
  end_sec: 775.19
  text: 'probability flux. So imagine a flux is

    like the amount of flow the amount of like the amount of flow the amount of like
    the amount of flow the amount of

    water uh per unit per time that''s going water uh per unit per time that''s going
    water uh per unit per time that''s going

    through a certain a certain uh unit through a certain a certain uh unit through
    a certain a certain uh unit

    space. So if you''re thinking about like space. So if you''re thinking about like
    space. So if you''re thinking about like

    how the probability flows is a how the probability flows is a how the probability
    flows is a

    probability flux is equal to the probability flux is equal to the probability
    flux is equal to the

    velocity times the the the density sort velocity times the the the density sort
    velocity times the the the density sort

    of. So the velocity is giving you where of. So the velocity is giving you where
    of. So the velocity is giving you where

    and how fast the probability flows and and how fast the probability flows and
    and how fast the probability flows and

    then the density is telling you how much then the density is telling you how much
    then the density is telling you how much

    probability there was so that probability there was so that probability there
    was so that

    it flows out right um okay so this is it flows out right um okay so this is it
    flows out right um okay so this is

    like a like a like a

    um visualization generated by vo I um visualization generated by vo I um visualization
    generated by vo I

    already tried but let''s just uh look at already tried but let''s just uh look
    at already tried but let''s just uh look at

    it okay okay

    maybe I should put on okay do that maybe I should put on okay do that maybe I
    should put on okay do that

    All right. Okay. So, as you can see, as the thing Okay. So, as you can see, as
    the thing

    as the water flows, first of all, it''s as the water flows, first of all, it''s
    as the water flows, first of all, it''s

    in a container. It''s in like a contained'
  concept_slugs:
  - continuous-normalizing-flow
  - flow-matching
  - velocity-field
- idx: 14
  start_sec: 775.19
  end_sec: 840.069
  text: 'in a container. It''s in like a contained in a container. It''s in like a
    contained

    tank. So, the probability mass never tank. So, the probability mass never tank.
    So, the probability mass never

    change. And second, like basically based change. And second, like basically based
    change. And second, like basically based

    on how fast the particle flows um like on how fast the particle flows um like
    on how fast the particle flows um like

    the probability density, which is like the probability density, which is like
    the probability density, which is like

    the water amount at this particular the water amount at this particular the water
    amount at this particular

    location, also changes. location, also changes. location, also changes.

    Okay, any questions? >> Flux in this case like similar to like >> Flux in this
    case like similar to like

    magnetic flu magnetic flu magnetic flu

    like it''s like the amount of like like it''s like the amount of like like it''s
    like the amount of like

    >> Nope. >> Nope. >> Nope.

    >> It''s a it just I think water is a better >> It''s a it just I think water
    is a better >> It''s a it just I think water is a better

    um um um

    I I mean I I mean I I mean

    >> like >> like >> like

    >> Yeah. Yeah. Kind of >> Yeah. Yeah. Kind of >> Yeah. Yeah. Kind of

    >> kind of. Yeah. It''s like amount of flows >> kind of. Yeah. It''s like amount
    of flows >> kind of. Yeah. It''s like amount of flows

    that goes through a certain place within that goes through a certain place within
    that goes through a certain place within

    a within a unit unit amount of time. a within a unit unit amount of time. a within
    a unit unit amount of time.

    >> A sphere >> A sphere >> A sphere

    0. 0. 0.

    >> Yeah. Yeah. Kind of kind. Okay. But >> Yeah. Yeah. Kind of kind. Okay. But
    >> Yeah. Yeah. Kind of kind. Okay. But

    anyway basically uh because of this we anyway basically uh because of this we
    anyway basically uh because of this we

    can actually write the probability flux can actually write the probability flux
    can actually write the probability flux

    in math in this way. So this is like'
  concept_slugs:
  - continuous-normalizing-flow
  - flow-matching
  - velocity-field
- idx: 15
  start_sec: 840.069
  end_sec: 912.72
  text: 'in math in this way. So this is like in math in this way. So this is like

    basically like how much probability gets basically like how much probability gets
    basically like how much probability gets

    changed um infinite uh through time and changed um infinite uh through time and
    changed um infinite uh through time and

    then this is what we call the divergence then this is what we call the divergence
    then this is what we call the divergence

    of velocity times density and what is of velocity times density and what is of
    velocity times density and what is

    divergence divergence is what we have divergence divergence is what we have divergence
    divergence is what we have

    seen actually uh last class it''s the seen actually uh last class it''s the seen
    actually uh last class it''s the

    trace of the jacobian what what it means trace of the jacobian what what it means
    trace of the jacobian what what it means

    is basically like how much um how like is basically like how much um how like
    is basically like how much um how like

    how much do you change in every how much do you change in every how much do you
    change in every

    direction direction direction

    um of the of the flow o of the of the um of the of the flow o of the of the um
    of the of the flow o of the of the

    data space. data space. data space.

    Okay, any questions? Okay, any questions? Okay, any questions?

    Everyone understand this? Yay. Yeah, this is like very physics Yay. Yeah, this
    is like very physics

    coded. Okay, any any more questions? Direction. Direction.

    >> Oh, D is dimension. Sorry. Yeah. So, in >> Oh, D is dimension. Sorry. Yeah.
    So, in >> Oh, D is dimension. Sorry. Yeah. So, in

    every dimension, how does this thing every dimension, how does this thing every
    dimension, how does this thing

    change? basically. Oh, uh I think uh there''s a P here that Oh, uh I think uh
    there''s a P here that

    is got getting uh um missed. is got getting uh um missed. is got getting uh um
    missed.

    >> Yeah. >> Yeah. >> Yeah.

    >> What''s the second assumption? There''s >> What''s the second assumption? There''s
    >> What''s the second assumption? There''s

    two assumptions. two assumptions.'
  concept_slugs:
  - continuous-normalizing-flow
  - flow-matching
  - velocity-field
- idx: 16
  start_sec: 912.72
  end_sec: 964.24
  text: 'two assumptions.

    >> Uh two assumptions. One is that >> Uh two assumptions. One is that >> Uh two
    assumptions. One is that

    add up to one. The second one is that add up to one. The second one is that add
    up to one. The second one is that

    the the thing changes uh continuously. the the thing changes uh continuously.
    the the thing changes uh continuously.

    But how is the first one encoded in But how is the first one encoded in But how
    is the first one encoded in

    this? this? this?

    >> Uh it >> Uh it >> Uh it

    I I guess just the first one is not I I guess just the first one is not I I guess
    just the first one is not

    really encoded in this but like you just really encoded in this but like you just
    really encoded in this but like you just

    need to have a probability that add up need to have a probability that add up
    need to have a probability that add up

    to one. Yeah. >> Flux is a weird word for me. Would it be >> Flux is a weird word
    for me. Would it be

    weird to think of it as like viscosity weird to think of it as like viscosity
    weird to think of it as like viscosity

    like the amount of flow period of time like the amount of flow period of time
    like the amount of flow period of time

    and you''re counting for density to like and you''re counting for density to like
    and you''re counting for density to like

    >> I mean the changes in space right and >> I mean the changes in space right
    and >> I mean the changes in space right and

    the viscosity should be uniform. Sure. the viscosity should be uniform. Sure.
    the viscosity should be uniform. Sure.

    But like viscosity with the thing moving But like viscosity with the thing moving
    But like viscosity with the thing moving

    over time. >> Um now flux is actually also a physics >> Um now flux is actually
    also a physics

    term and it means like the amount of term and it means like the amount of term
    and it means like the amount of

    thing that like flow out thing that like flow out'
  concept_slugs:
  - continuous-normalizing-flow
  - flow-matching
  - velocity-field
- idx: 17
  start_sec: 964.24
  end_sec: 1028.63
  text: 'thing that like flow out

    >> as physically inclined. >> as physically inclined. >> as physically inclined.

    >> It is okay. >> It is okay. >> It is okay.

    >> I''m just a civil engineer. >> I''m just a civil engineer. >> I''m just a civil
    engineer.

    >> I''m also not a physics major but uh you >> I''m also not a physics major but
    uh you >> I''m also not a physics major but uh you

    know this is like it''s not really >> um I mean just a term. It''s not really
    >> um I mean just a term. It''s not really

    like um Yeah. Yeah. But but but like you like um Yeah. Yeah. But but but like
    you like um Yeah. Yeah. But but but like you

    can you can imagine it however way you can you can imagine it however way you
    can you can imagine it however way you

    want but that''s what it means basically want but that''s what it means basically
    want but that''s what it means basically

    just the amount of things that it just the amount of things that it just the amount
    of things that it

    outflows in a unit time basically. outflows in a unit time basically. outflows
    in a unit time basically.

    >> Yeah, >> why is it noisy? system external noise >> why is it noisy? system
    external noise

    >> uh depending on what kind of things that >> uh depending on what kind of things
    that >> uh depending on what kind of things that

    you are. So basically if you''re thinking you are. So basically if you''re thinking
    you are. So basically if you''re thinking

    about the path that we just constructed about the path that we just constructed
    about the path that we just constructed

    then yes each XT is noisy but this is a then yes each XT is noisy but this is
    a then yes each XT is noisy but this is a

    generalized um um like notion it it''s generalized um um like notion it it''s
    generalized um um like notion it it''s

    like just any flow this is the this is like just any flow this is the this is
    like just any flow this is the this is

    the the definition any other question any other question

    yes yes yes

    the divergence connection again'
  concept_slugs:
  - continuous-normalizing-flow
  - flow-matching
  - velocity-field
- idx: 18
  start_sec: 1028.63
  end_sec: 1101.909
  text: 'the divergence connection again the divergence connection again

    >> yes I I think I missed a P here actually >> yes I I think I missed a P here
    actually >> yes I I think I missed a P here actually

    by the way uh but basically by the way uh but basically by the way uh but basically

    The divergence means that like how much The divergence means that like how much
    The divergence means that like how much

    uh probability do you change in every uh probability do you change in every uh
    probability do you change in every

    direction of the data space. Yeah. So direction of the data space. Yeah. So direction
    of the data space. Yeah. So

    that''s why it''s the trace of the that''s why it''s the trace of the that''s
    why it''s the trace of the

    Jacobian in every direction, every Jacobian in every direction, every Jacobian
    in every direction, every

    dimension here. Yeah. I I miss a P here. because like this case, right? because
    like this case, right?

    >> We don''t we haven''t talked about flow >> We don''t we haven''t talked about
    flow >> We don''t we haven''t talked about flow

    matching yet. >> All right. Any more question? >> All right. Any more question?

    Cool. All right. Yeah. So, this is Cool. All right. Yeah. So, this is Cool. All
    right. Yeah. So, this is

    divergence. How much probability that divergence. How much probability that divergence.
    How much probability that

    outflows from a given point per unit outflows from a given point per unit outflows
    from a given point per unit

    time in every direction? time in every direction? time in every direction?

    Okay. Okay. Okay.

    Cool. All right. All right. So uh like a Cool. All right. All right. So uh like
    a Cool. All right. All right. So uh like a

    good thing about um this thing is that good thing about um this thing is that
    good thing about um this thing is that

    we can actually transform this PDE into we can actually transform this PDE into
    we can actually transform this PDE into

    an OD. All right. So what it means is an OD. All right. So what it means is an
    OD. All right. So what it means is

    that like so this is the correct'
  concept_slugs:
  - continuous-normalizing-flow
  - flow-matching
  - velocity-field
- idx: 19
  start_sec: 1101.909
  end_sec: 1153.039
  text: 'that like so this is the correct that like so this is the correct

    divergence. Sorry that that that one I divergence. Sorry that that that one I
    divergence. Sorry that that that one I

    missed P. Um but basically we can go missed P. Um but basically we can go missed
    P. Um but basically we can go

    from here uh and basically you do the from here uh and basically you do the from
    here uh and basically you do the

    greatest uh mathematical trick of all greatest uh mathematical trick of all greatest
    uh mathematical trick of all

    time. You multiply time. You multiply time. You multiply

    two things at the same time from the two things at the same time from the two
    things at the same time from the

    left hand side to the right hand side left hand side to the right hand side left
    hand side to the right hand side

    and uh basically this thing because the and uh basically this thing because the
    and uh basically this thing because the

    because the the the the derivative of because the the the the derivative of because
    the the the the derivative of

    log is equal to 1 /x. So it becomes the log is equal to 1 /x. So it becomes the
    log is equal to 1 /x. So it becomes the

    derivative of the uh the log and then um derivative of the uh the log and then
    um derivative of the uh the log and then um

    basically you just apply the same thing basically you just apply the same thing
    basically you just apply the same thing

    applying the same trick here and then it applying the same trick here and then
    it applying the same trick here and then it

    becomes something like this. Um and then like essentially you basically and then
    like essentially you basically

    just do a lot of like calculus and then just do a lot of like calculus and then
    just do a lot of like calculus and then

    you''re actually able to get uh an OD of you''re actually able to get uh an OD
    of you''re actually able to get uh an OD of

    the log probability of of the log the log probability of of the log'
  concept_slugs:
  - continuous-normalizing-flow
  - flow-matching
  - velocity-field
- idx: 20
  start_sec: 1153.039
  end_sec: 1252.4
  text: 'the log probability of of the log

    density. Okay. And this OD is actually density. Okay. And this OD is actually
    density. Okay. And this OD is actually

    equal to so the derivative of the total equal to so the derivative of the total
    equal to so the derivative of the total

    derivative of log probability is equal derivative of log probability is equal
    derivative of log probability is equal

    to the divergence of the velocity to the divergence of the velocity to the divergence
    of the velocity

    period. Okay. Any questions here? Okay. Any questions here?

    >> Yes. >> Yes. >> Yes.

    >> PFS to be zero. >> PFS to be zero. >> PFS to be zero.

    >> Yes. Yes. That''s a that''s a that''s a >> Yes. Yes. That''s a that''s a that''s
    a >> Yes. Yes. That''s a that''s a that''s a

    great uh question. Yes. PFS is greater great uh question. Yes. PFS is greater
    great uh question. Yes. PFS is greater

    than zero everywhere. Yeah. Basically, you just do a lot of Yeah. Basically, you
    just do a lot of

    calculus and then you get this. >> No question. >> No question.

    >> Yes. >> Yes.

    >> Because it''s still depending on the >> Because it''s still depending on the
    >> Because it''s still depending on the

    variable. variable. variable.

    No, basically from this line, I don''t No, basically from this line, I don''t
    No, basically from this line, I don''t

    know if you can see my cursor. This line know if you can see my cursor. This line
    know if you can see my cursor. This line

    is literally the formula for the total is literally the formula for the total
    is literally the formula for the total

    derivative, right? derivative, right? derivative, right?

    Yeah. No more question. No more question.

    Okay, cool. Uh so basically then you can Okay, cool. Uh so basically then you
    can Okay, cool. Uh so basically then you can

    calculus then you can calculate your calculus then you can calculate your calculus
    then you can calculate your

    likelihood, right? because now you have likelihood, right? because now you have
    likelihood, right? because now you have

    a another OD that you can directly solve a another OD that you can directly solve
    a another OD that you can directly solve

    by doing numerical integration. So exactly so so'
  concept_slugs:
  - continuous-normalizing-flow
  - flow-matching
  - velocity-field
- idx: 21
  start_sec: 1252.4
  end_sec: 1324.159
  text: 'So exactly so so

    how do you train your continuous how do you train your continuous how do you train
    your continuous

    normalizing flow from here? What do we normalizing flow from here? What do we
    normalizing flow from here? What do we

    think jumping ahead. Jumping ahead. What is jumping ahead. Jumping ahead. What
    is

    the Now we have a formula for the the Now we have a formula for the the Now we
    have a formula for the

    likelihood log likelihood you can do for the the most naive thing you can do for
    the the most naive thing

    to think right is the maximum log to think right is the maximum log to think right
    is the maximum log

    likelihood. So basically uh yeah so likelihood. So basically uh yeah so likelihood.
    So basically uh yeah so

    because you have a formula to calculate because you have a formula to calculate
    because you have a formula to calculate

    the log likelihood at any point of the the log likelihood at any point of the
    the log likelihood at any point of the

    trajectory obviously you can also trajectory obviously you can also trajectory
    obviously you can also

    calculate the log likelihood of the end calculate the log likelihood of the end
    calculate the log likelihood of the end

    point right so you just do arg max of point right so you just do arg max of point
    right so you just do arg max of

    the likelihood what could be a problem the likelihood what could be a problem
    the likelihood what could be a problem

    here >> yeah yeah >> yeah yeah

    >> don''t have access to p 0 >> don''t have access to p 0 >> don''t have access
    to p 0

    >> you we can define that we define p 0 to >> you we can define that we define
    p 0 to >> you we can define that we define p 0 to

    be a gausian for example that''s fine be a gausian for example that''s fine be
    a gausian for example that''s fine

    Very very good. So basically in order to very good. So basically in order to

    calculate the log likelihood of the data calculate the log likelihood of the data
    calculate the log likelihood of the data

    we actually need to do numerical we actually need to do numerical'
  concept_slugs:
  - continuous-normalizing-flow
  - flow-matching
  - velocity-field
- idx: 22
  start_sec: 1324.159
  end_sec: 1387.039
  text: 'we actually need to do numerical

    integration right. But this is at integration right. But this is at integration
    right. But this is at

    training time. So that just means that training time. So that just means that
    training time. So that just means that

    we need to do many many many many steps we need to do many many many many steps
    we need to do many many many many steps

    of integration at training time and that of integration at training time and that
    of integration at training time and that

    thing is really really expensive. thing is really really expensive. thing is really
    really expensive.

    Right. Right. Right.

    Okay. What what would be a better way to Okay. What what would be a better way
    to Okay. What what would be a better way to

    do this? do this? do this?

    >> Yeah. >> If we take the if we take the gradient >> If we take the if we take
    the gradient

    of the left hand side, we get a score of the left hand side, we get a score of
    the left hand side, we get a score

    and the left hand side removes, and the left hand side removes, and the left hand
    side removes,

    >> right? >> right? >> right?

    >> Uh >> Uh >> Uh

    even if you do that right, the even if you do that right, the even if you do that
    right, the

    divergence is still pretty difficult to divergence is still pretty difficult to
    divergence is still pretty difficult to

    calculate. calculate. calculate.

    >> Okay. But what else? Yes, >> we can we can use this numerator or we >> we can
    we can use this numerator or we

    can just directly sample can just directly sample can just directly sample

    so that it''ll be uh we we''ll end up like so that it''ll be uh we we''ll end
    up like so that it''ll be uh we we''ll end up like

    uh we''ll end up with the summation. >> You you mean you change the integration
    >> You you mean you change the integration

    into summation? into summation? into summation?

    >> Yeah. Yeah. Yeah. But that''s just >> Yeah. Yeah. Yeah. But that''s just >>
    Yeah. Yeah. Yeah. But that''s just

    numerical integration, right? So it numerical integration, right? So it'
  concept_slugs:
  - continuous-normalizing-flow
  - flow-matching
  - velocity-field
- idx: 23
  start_sec: 1387.039
  end_sec: 1451.279
  text: 'numerical integration, right? So it

    still has a lot of steps. Can we do still has a lot of steps. Can we do still
    has a lot of steps. Can we do

    something that doesn''t require a lot of something that doesn''t require a lot
    of something that doesn''t require a lot of

    steps? Like we just have one four pass steps? Like we just have one four pass
    steps? Like we just have one four pass

    during the training time. I think during the training time. I think during the
    training time. I think

    someone said it before. Who said velocity before? Who did it? Who said velocity
    before? Who did it?

    Oh, you did? Oh, you did? Oh, you did?

    >> Oh, someone who said velocity. >> Oh, okay. Why? Why did you say velocity?
    >> Oh, okay. Why? Why did you say velocity?

    >> Because >> Because >> Because

    the model''s learning velocity. Okay, it actually Okay, it actually

    basically if you think about it right basically if you think about it right basically
    if you think about it right

    both sampling like in order to sample or both sampling like in order to sample
    or both sampling like in order to sample or

    calculate the log likelihood you you calculate the log likelihood you you calculate
    the log likelihood you you

    pretty much only need to parameterize pretty much only need to parameterize pretty
    much only need to parameterize

    the velocity right so if you have a the velocity right so if you have a the velocity
    right so if you have a

    model for the velocity then you can model for the velocity then you can model
    for the velocity then you can

    calculate then you can do both sampling calculate then you can do both sampling
    calculate then you can do both sampling

    and calculate the log log likelihood so and calculate the log log likelihood so
    and calculate the log log likelihood so

    why don''t we we just need to make sure why don''t we we just need to make sure
    why don''t we we just need to make sure

    that the velocity is correct right so we that the velocity is correct right so
    we that the velocity is correct right so we

    just need to make sure that the velocity just need to make sure that the velocity'
  concept_slugs:
  - continuous-normalizing-flow
  - flow-matching
  - velocity-field
- idx: 24
  start_sec: 1451.279
  end_sec: 1512.159
  text: 'just need to make sure that the velocity

    actually match with the ground truth actually match with the ground truth actually
    match with the ground truth

    velocity. velocity. velocity.

    So you just do L2 to match with the So you just do L2 to match with the So you
    just do L2 to match with the

    ground truth velocity. ground truth velocity. ground truth velocity.

    Easy, right? Easy, right? Easy, right?

    What is the problem? Yeah. In order to do either sampling or like In order to
    do either sampling or like

    critical estimation, we just need a critical estimation, we just need a critical
    estimation, we just need a

    velocity. So if we have a model for velocity. So if we have a model for velocity.
    So if we have a model for

    velocity, then we could can do velocity, then we could can do velocity, then we
    could can do

    integration at inference time. We don''t integration at inference time. We don''t
    integration at inference time. We don''t

    need to do integration at training time need to do integration at training time
    need to do integration at training time

    anymore, right? But what what is the anymore, right? But what what is the anymore,
    right? But what what is the

    problem here? The ground truth, right? We don''t have The ground truth, right?
    We don''t have

    the ground truth. If we have the ground the ground truth. If we have the ground
    the ground truth. If we have the ground

    truth, we would know that a winter storm truth, we would know that a winter storm
    truth, we would know that a winter storm

    is coming. Apparently, it''s a Saturday. is coming. Apparently, it''s a Saturday.
    is coming. Apparently, it''s a Saturday.

    It''s a very cold day. So be prepared. It''s a very cold day. So be prepared.
    It''s a very cold day. So be prepared.

    Okay, winter''s coming. Uh anyway, so Okay, winter''s coming. Uh anyway, so Okay,
    winter''s coming. Uh anyway, so

    yeah, but we do we do not know. So yeah, but we do we do not know. So yeah, but
    we do we do not know. So

    that''s why the meteorologists are that''s why the meteorologists are that''s
    why the meteorologists are

    changing every day be like actually I changing every day be like actually I'
  concept_slugs:
  - continuous-normalizing-flow
  - flow-matching
  - velocity-field
- idx: 25
  start_sec: 1512.159
  end_sec: 1558.08
  text: 'changing every day be like actually I

    think that the the storm is moving north think that the the storm is moving north
    think that the the storm is moving north

    or maybe not. We don''t know, right? So or maybe not. We don''t know, right? So
    or maybe not. We don''t know, right? So

    we do not know the ground velocity. How should we solve this? Well, How should
    we solve this? Well,

    basically say we don''t care about basically say we don''t care about basically
    say we don''t care about

    everywhere else. We just care about how everywhere else. We just care about how
    everywhere else. We just care about how

    the storm is going to move to the storm is going to move to the storm is going
    to move to

    Pittsburgh. Let''s just say and say now Pittsburgh. Let''s just say and say now
    Pittsburgh. Let''s just say and say now

    you just want to like say you now you''re you just want to like say you now you''re
    you just want to like say you now you''re

    Poseidon. Okay, whatever. And then you Poseidon. Okay, whatever. And then you
    Poseidon. Okay, whatever. And then you

    you want to transform a bunch of water you want to transform a bunch of water
    you want to transform a bunch of water

    or a bunch of like humidity to or a bunch of like humidity to or a bunch of like
    humidity to

    Pittsburgh so that Pittsburgh would Pittsburgh so that Pittsburgh would Pittsburgh
    so that Pittsburgh would

    snow. snow. snow.

    What would you do? What is the easiest What would you do? What is the easiest
    What would you do? What is the easiest

    way? What is the fastest way for you to way? What is the fastest way for you to
    way? What is the fastest way for you to

    do it? How how would you do that? do it? How how would you do that? do it? How
    how would you do that?

    >> You just Yeah. >> You just Yeah. >> You just Yeah.

    >> Just go straight there. >> Just go straight there. >> Just go straight there.

    >> Just go straight there. Yeah. Yeah. >> Just go straight there. Yeah. Yeah.
    >> Just go straight there. Yeah. Yeah.

    Yeah. That''s right. That''s right. You Yeah. That''s right. That''s right. You'
  concept_slugs:
  - continuous-normalizing-flow
  - flow-matching
  - velocity-field
- idx: 26
  start_sec: 1558.08
  end_sec: 1617.83
  text: 'Yeah. That''s right. That''s right. You

    just go straight. just go straight. just go straight.

    Yeah, exactly. Uh so basically this is Yeah, exactly. Uh so basically this is
    Yeah, exactly. Uh so basically this is

    what we''re going to do as well. Uh so what we''re going to do as well. Uh so
    what we''re going to do as well. Uh so

    let''s say we fix a data point. We don''t let''s say we fix a data point. We don''t
    let''s say we fix a data point. We don''t

    care about everywhere else. We just care care about everywhere else. We just care
    care about everywhere else. We just care

    about one data point. And then it''s about one data point. And then it''s about
    one data point. And then it''s

    usually uh very easy to define a what we usually uh very easy to define a what
    we usually uh very easy to define a what we

    call continuous velocity field which uh call continuous velocity field which uh
    call continuous velocity field which uh

    sorry a conditional velocity field which sorry a conditional velocity field which
    sorry a conditional velocity field which

    means that means that means that

    basically it just basically it just basically it just

    velocity is depending on the end point velocity is depending on the end point
    velocity is depending on the end point

    right and then we call the trajectory of right and then we call the trajectory
    of right and then we call the trajectory of

    the probability distribution that gen the probability distribution that gen the
    probability distribution that gen

    get generated along the get generated along the get generated along the

    way of that uh velocity field the way of that uh velocity field the way of that
    uh velocity field the

    conditional probability path. So the conditional probability path. So the conditional
    probability path. So the

    conditional probability path is consists conditional probability path is consists
    conditional probability path is consists

    of like all the uh all the pts along the of like all the uh all the pts along
    the of like all the uh all the pts along the

    way. Okay. And here the conditional way. Okay. And here the conditional way. Okay.
    And here the conditional

    probability path will probability path will probability path will

    just start from some prior which we can'
  concept_slugs:
  - continuous-normalizing-flow
  - flow-matching
  - velocity-field
- idx: 27
  start_sec: 1617.83
  end_sec: 1663.919
  text: 'just start from some prior which we can just start from some prior which
    we can

    choose. So it doesn''t matter we can choose. So it doesn''t matter we can choose.
    So it doesn''t matter we can

    choose the prior and then we will always choose the prior and then we will always
    choose the prior and then we will always

    end up either directly at Pittsburgh or end up either directly at Pittsburgh or
    end up either directly at Pittsburgh or

    somewhere around Pittsburgh. So like we somewhere around Pittsburgh. So like we
    somewhere around Pittsburgh. So like we

    just like always end up at x1 or a small just like always end up at x1 or a small
    just like always end up at x1 or a small

    small gausian that concentrate around small gausian that concentrate around small
    gausian that concentrate around

    x1. Okay. And uh by the way so this x1. Okay. And uh by the way so this x1. Okay.
    And uh by the way so this

    thing is called direct delta. So it just thing is called direct delta. So it just
    thing is called direct delta. So it just

    means that it''s a point mass at at x1. means that it''s a point mass at at x1.
    means that it''s a point mass at at x1.

    Okay. Then uh the marginal probability Okay. Then uh the marginal probability
    Okay. Then uh the marginal probability

    path can be written in this way, right? path can be written in this way, right?
    path can be written in this way, right?

    Basically just like sum up all the Basically just like sum up all the Basically
    just like sum up all the

    possible uh sum up all the possible uh possible uh sum up all the possible uh
    possible uh sum up all the possible uh

    uh like data points and then basically uh like data points and then basically
    uh like data points and then basically

    just like yeah like and and times the just like yeah like and and times the just
    like yeah like and and times the

    the the conditional probability given the the conditional probability given the
    the conditional probability given

    the the data point then you can get a the the data point then you can get a'
  concept_slugs:
  - continuous-normalizing-flow
  - flow-matching
  - velocity-field
- idx: 28
  start_sec: 1663.919
  end_sec: 1743.669
  text: 'the the data point then you can get a

    marginal marginal marginal

    uh yeah and also uh just the boundary uh yeah and also uh just the boundary uh
    yeah and also uh just the boundary

    condition essentially uh the probability condition essentially uh the probability
    condition essentially uh the probability

    uh at time uh at time uh at time

    should recover the data probability. should recover the data probability. should
    recover the data probability.

    This is basically what we''re trying to This is basically what we''re trying to
    This is basically what we''re trying to

    construct. construct. construct.

    Okay. >> All right. Cool. Um so say now we have a >> All right. Cool. Um so say
    now we have a

    conditional velocity here. uh then we conditional velocity here. uh then we conditional
    velocity here. uh then we

    can also define a marginal velocity. can also define a marginal velocity. can
    also define a marginal velocity.

    What does what does this mean? So What does what does this mean? So What does
    what does this mean? So

    basically this just means that uh we are basically this just means that uh we
    are basically this just means that uh we are

    sort of like we''re like sort of like sort of like we''re like sort of like sort
    of like we''re like sort of like

    apply a bay theorem on on your uh apply a bay theorem on on your uh apply a bay
    theorem on on your uh

    conditional velocity. So that basically conditional velocity. So that basically
    conditional velocity. So that basically

    it''s like reweighted it''s like reweighted it''s like reweighted

    uh like um taking account into like uh like um taking account into like uh like
    um taking account into like

    basically um how likely is your current basically um how likely is your current
    basically um how likely is your current

    uh noisy point like your intermediate uh noisy point like your intermediate uh
    noisy point like your intermediate

    data point along the the the conditional data point along the the the conditional
    data point along the the the conditional

    probability path. How likely is the data probability path. How likely is the data
    probability path. How likely is the data

    point that defined this conditional point that defined this conditional point
    that defined this conditional

    probability path and also just like how'
  concept_slugs:
  - continuous-normalizing-flow
  - flow-matching
  - velocity-field
- idx: 29
  start_sec: 1743.669
  end_sec: 1838.549
  text: 'probability path and also just like how probability path and also just like
    how

    like and reweed by how likely in general like and reweed by how likely in general
    like and reweed by how likely in general

    of this current intermediate point. Does of this current intermediate point. Does
    of this current intermediate point. Does

    this make sense? All right. So basically you can sort of All right. So basically
    you can sort of

    like intuitively understand this as like like intuitively understand this as like
    like intuitively understand this as like

    this is the average conditional velocity this is the average conditional velocity
    this is the average conditional velocity

    at this current location in this current at this current location in this current
    at this current location in this current

    time weighted by how likely uh is the time weighted by how likely uh is the time
    weighted by how likely uh is the

    data point for this current location in data point for this current location in
    data point for this current location in

    time. part. Then in the next slide when we''re part. Then in the next slide when
    we''re

    doing it for the velocity, is it doing it for the velocity, is it doing it for
    the velocity, is it

    something we''re doing from that step or something we''re doing from that step
    or something we''re doing from that step or

    is it just like separate entirely? is it just like separate entirely? is it just
    like separate entirely?

    >> Separate. I''ll go level resurrected. Uh yeah. So, I''ll go level resurrected.
    Uh yeah. So,

    so, so this is kind of like what we so, so this is kind of like what we so, so
    this is kind of like what we

    defined. It''s not like it''s two defined. It''s not like it''s two defined. It''s
    not like it''s two

    different notions different notions different notions

    and like you can intuitively understand and like you can intuitively understand
    and like you can intuitively understand

    it as like sort of like the um like the it as like sort of like the um like the
    it as like sort of like the um like the

    average uh conditional velocity and then average uh conditional velocity and then
    average uh conditional velocity and then

    this average is like averaging by like'
  concept_slugs:
  - continuous-normalizing-flow
  - flow-matching
  - velocity-field
- idx: 30
  start_sec: 1838.549
  end_sec: 1904.96
  text: 'this average is like averaging by like this average is like averaging by
    like

    how likely is the data point given your how likely is the data point given your
    how likely is the data point given your

    current position and the data points are available. and the data points are available.

    All right, does this make sense? we''ll get to it. We''ll get to it. Um all we''ll
    get to it. We''ll get to it. Um all

    right. Uh and a very interesting thing right. Uh and a very interesting thing
    right. Uh and a very interesting thing

    here is that the marginal velocity we here is that the marginal velocity we here
    is that the marginal velocity we

    just saw actually generates the marginal just saw actually generates the marginal
    just saw actually generates the marginal

    probability path that we want. Okay. So what it means is what it means by So what
    it means is what it means by

    generate is basically just means that generate is basically just means that generate
    is basically just means that

    like the the continuity equation is like the the continuity equation is like the
    the continuity equation is

    satisfies the the PTE is satisfied and satisfies the the PTE is satisfied and
    satisfies the the PTE is satisfied and

    why does it satisfy is because if you why does it satisfy is because if you why
    does it satisfy is because if you

    just break everything down uh and then just break everything down uh and then
    just break everything down uh and then

    you are able to get basically the the you are able to get basically the the you
    are able to get basically the the

    divergence back. Uh so this is just divergence back. Uh so this is just divergence
    back. Uh so this is just

    like step by step how you will get a like step by step how you will get a like
    step by step how you will get a

    divergence back. Uh so you first um swap divergence back. Uh so you first um swap
    divergence back. Uh so you first um swap

    in the the the derivative with some in the the the derivative with some in the
    the the derivative with some

    regularization condition. This can can regularization condition. This can can'
  concept_slugs:
  - continuous-normalizing-flow
  - flow-matching
  - velocity-field
- idx: 31
  start_sec: 1904.96
  end_sec: 1966.399
  text: 'regularization condition. This can can

    can be done. Uh and then uh basically can be done. Uh and then uh basically can
    be done. Uh and then uh basically

    you uh input your um because we know you uh input your um because we know you
    uh input your um because we know

    that the marginal sorry the conditional that the marginal sorry the conditional
    that the marginal sorry the conditional

    velocity generates the conditional path. velocity generates the conditional path.
    velocity generates the conditional path.

    So we can uh input the continuity So we can uh input the continuity So we can
    uh input the continuity

    equation there and then it becomes this equation there and then it becomes this
    equation there and then it becomes this

    whole thing with divergence. Uh and then whole thing with divergence. Uh and then
    whole thing with divergence. Uh and then

    plug in the definition that we just saw plug in the definition that we just saw
    plug in the definition that we just saw

    before we can actually get something before we can actually get something before
    we can actually get something

    like this and again pulling out the the like this and again pulling out the the
    like this and again pulling out the the

    the the derivative here because because the the derivative here because because
    the the derivative here because because

    of some regularization condition that we of some regularization condition that
    we of some regularization condition that we

    can satisfy it. uh and this thing is can satisfy it. uh and this thing is can
    satisfy it. uh and this thing is

    literally just the divergence of the literally just the divergence of the literally
    just the divergence of the

    marginal uh velocity times the marginal marginal uh velocity times the marginal
    marginal uh velocity times the marginal

    density. density. density.

    So all in all this is to say that the So all in all this is to say that the So
    all in all this is to say that the

    marginal velocity that we defined before marginal velocity that we defined before
    marginal velocity that we defined before

    from the conditional velocity that we from the conditional velocity that we from
    the conditional velocity that we

    can construct can generate the marginal can construct can generate the marginal'
  concept_slugs:
  - continuous-normalizing-flow
  - flow-matching
  - velocity-field
- idx: 32
  start_sec: 1966.399
  end_sec: 2028.549
  text: 'can construct can generate the marginal

    property path which is what we want. property path which is what we want. property
    path which is what we want.

    Oh, I saw so many confusion. Oh, I saw so many confusion. Oh, I saw so many confusion.

    All good. All good. We''re getting there. All good. All good. We''re getting there.
    All good. All good. We''re getting there.

    We''re getting there. I promise. Ah, We''re getting there. I promise. Ah, We''re
    getting there. I promise. Ah,

    okay. The other thing which is the most okay. The other thing which is the most
    okay. The other thing which is the most

    important thing and the most magical important thing and the most magical important
    thing and the most magical

    part is that actually part is that actually part is that actually

    so this is the the the the equation that so this is the the the the equation that
    so this is the the the the equation that

    we want, right? So this is the equation we want, right? So this is the equation
    we want, right? So this is the equation

    that we that that that we came up with. that we that that that we came up with.
    that we that that that we came up with.

    You just need to match the ground truth You just need to match the ground truth
    You just need to match the ground truth

    marginal velocity. But we do not have marginal velocity. But we do not have marginal
    velocity. But we do not have

    the groundous marginal velocity, right? the groundous marginal velocity, right?
    the groundous marginal velocity, right?

    And it actually turns out that if you And it actually turns out that if you And
    it actually turns out that if you

    just match the conditional velocity, just match the conditional velocity, just
    match the conditional velocity,

    you''re actually going to end up with the you''re actually going to end up with
    the you''re actually going to end up with the

    same uh global optimal. You''re like same uh global optimal. You''re like same
    uh global optimal. You''re like

    basically just like matching the ground basically just like matching the ground
    basically just like matching the ground

    truth marginal velocity is equivalent to truth marginal velocity is equivalent
    to truth marginal velocity is equivalent to

    ma matching the conditional velocity.'
  concept_slugs:
  - continuous-normalizing-flow
  - flow-matching
  - velocity-field
- idx: 33
  start_sec: 2030.789
  end_sec: 2086.95
  text: 'Think about that. Isn''t that pretty Think about that. Isn''t that pretty

    cool? Okay. Why? Why? Why is that? Okay. cool? Okay. Why? Why? Why is that? Okay.
    cool? Okay. Why? Why? Why is that? Okay.

    So, the reason why is because we can So, the reason why is because we can So,
    the reason why is because we can

    break the two L2 down into this thing, break the two L2 down into this thing,
    break the two L2 down into this thing,

    right? We we saw this yesterday, not right? We we saw this yesterday, not right?
    We we saw this yesterday, not

    yesterday, on Tuesday already, right? yesterday, on Tuesday already, right? yesterday,
    on Tuesday already, right?

    And the first term for both equation are And the first term for both equation
    are And the first term for both equation are

    constant with respect to our learn constant with respect to our learn constant
    with respect to our learn

    parameter. So, we''re just going to parameter. So, we''re just going to parameter.
    So, we''re just going to

    cancel it out, right? cancel it out, right? cancel it out, right?

    Uh and then now we get to two equations Uh and then now we get to two equations
    Uh and then now we get to two equations

    each with two components. Right? So each with two components. Right? So each with
    two components. Right? So

    we''re going to look at the first we''re going to look at the first we''re going
    to look at the first

    components together first. All right. So components together first. All right.
    So components together first. All right. So

    the first component if you if you look the first component if you if you look
    the first component if you if you look

    at the conditional flow matching uh at the conditional flow matching uh at the
    conditional flow matching uh

    equation here uh basically this thing equation here uh basically this thing equation
    here uh basically this thing

    you can um decompose it into two you can um decompose it into two you can um decompose
    it into two

    integrals and then the these two integrals and then the these two integrals and
    then the these two

    integrals integrals integrals

    um can be um can be um can be

    uh uh uh

    Like basically you if you swap uh the'
  concept_slugs:
  - continuous-normalizing-flow
  - flow-matching
  - velocity-field
- idx: 34
  start_sec: 2086.95
  end_sec: 2150.16
  text: 'Like basically you if you swap uh the Like basically you if you swap uh the

    dx1 term inside so you swap the order of dx1 term inside so you swap the order
    of dx1 term inside so you swap the order of

    the integration you''re actually going to the integration you''re actually going
    to the integration you''re actually going to

    get the first term of the first equation get the first term of the first equation
    get the first term of the first equation

    back. All right. This part is clear. Cool. All right. All right. Now look at Cool.
    All right. All right. Now look at

    the second part. The second part is the second part. The second part is the second
    part. The second part is

    pretty The second part is pretty pretty The second part is pretty pretty The second
    part is pretty

    similar. Basically what you do is you similar. Basically what you do is you similar.
    Basically what you do is you

    just uh starting from the second part of just uh starting from the second part
    of just uh starting from the second part of

    the first the first the first

    uh equation and then you just um plug in uh equation and then you just um plug
    in uh equation and then you just um plug in

    what we have as definition and then you what we have as definition and then you
    what we have as definition and then you

    do a lot of integrals in between and do a lot of integrals in between and do a
    lot of integrals in between and

    then you''re actually going to wind up then you''re actually going to wind up
    then you''re actually going to wind up

    at the second part of the second at the second part of the second at the second
    part of the second

    equation. equation. equation.

    Any question? Yes. No. No. Okay. understand everything Yes. No. No. Okay. understand
    everything

    everyone. everyone. everyone.

    >> It''s not so it''s not even that we''re >> It''s not so it''s not even that
    we''re >> It''s not so it''s not even that we''re

    sort of having a elbow type thing where sort of having a elbow type thing where
    sort of having a elbow type thing where

    we''re compressing the bullet. we''re compressing the bullet.'
  concept_slugs:
  - continuous-normalizing-flow
  - flow-matching
  - velocity-field
- idx: 35
  start_sec: 2150.16
  end_sec: 2213.04
  text: 'we''re compressing the bullet.

    >> It''s literally the same. It''s literally >> It''s literally the same. It''s
    literally >> It''s literally the same. It''s literally

    the same. It''s equivalent. It''s not even the same. It''s equivalent. It''s not
    even the same. It''s equivalent. It''s not even

    elbow. No question. All right. No question. All right.

    So, this just means that like we don''t So, this just means that like we don''t
    So, this just means that like we don''t

    need to match to the thing that we don''t need to match to the thing that we don''t
    need to match to the thing that we don''t

    know. we actually can match something know. we actually can match something know.
    we actually can match something

    that we do know and do know how to that we do know and do know how to that we
    do know and do know how to

    construct which is the conditional construct which is the conditional construct
    which is the conditional

    velocity. velocity.

    Okay. >> Yes, pretty much right. And then you >> Yes, pretty much right. And then
    you

    average out and then it is actually the average out and then it is actually the
    average out and then it is actually the

    same. Um so uh now let''s just look at same. Um so uh now let''s just look at
    same. Um so uh now let''s just look at

    the example that we have right. So now the example that we have right. So now
    the example that we have right. So now

    let''s suppose our conditional let''s suppose our conditional let''s suppose our
    conditional

    probability path is to transport uh probability path is to transport uh probability
    path is to transport uh

    trans transform a gausian a standard trans transform a gausian a standard trans
    transform a gausian a standard

    normal gausian straight to a single normal gausian straight to a single normal
    gausian straight to a single

    point with constant speed. So this is a point with constant speed. So this is
    a point with constant speed. So this is a

    conditional right. So that''s why we can conditional right. So that''s why we
    can conditional right. So that''s why we can

    have a single point here. What do we do? Well we first have the the the endpoint'
  concept_slugs:
  - continuous-normalizing-flow
  - flow-matching
  - velocity-field
- idx: 36
  start_sec: 2213.04
  end_sec: 2272.48
  text: 'Well we first have the the the endpoint

    distribution and because we''re distribution and because we''re distribution and
    because we''re

    transforming it straight to the point transforming it straight to the point transforming
    it straight to the point

    with constant speed right? So just with constant speed right? So just with constant
    speed right? So just

    linearly very straight. Um so we can linearly very straight. Um so we can linearly
    very straight. Um so we can

    literally have a formula for each literally have a formula for each literally
    have a formula for each

    intermediate point as a linear intermediate point as a linear intermediate point
    as a linear

    combination of uh of the data and the combination of uh of the data and the combination
    of uh of the data and the

    noise and this linear combination will noise and this linear combination will
    noise and this linear combination will

    add up to one right and uh the add up to one right and uh the add up to one right
    and uh the

    probability path can be written in this probability path can be written in this
    probability path can be written in this

    way. And most importantly, way. And most importantly, way. And most importantly,

    the velocity is literally just xt taking the velocity is literally just xt taking
    the velocity is literally just xt taking

    derivative of t, which is equal to theta derivative of t, which is equal to theta
    derivative of t, which is equal to theta

    minus noise. That''s it. And this is what we''re That''s it. And this is what
    we''re

    matching to at training time, which we matching to at training time, which we
    matching to at training time, which we

    have already seen. >> Yeah.

    >> First question. So this us >> First question. So this us >> First question.
    So this us

    parameterizing it as this linear parameterizing it as this linear parameterizing
    it as this linear

    combination that fact is not used really combination that fact is not used really
    combination that fact is not used really

    in any of the other. in any of the other. in any of the other.

    >> Yeah. No no this is what we chose. This >> Yeah. No no this is what we chose.
    This'
  concept_slugs:
  - continuous-normalizing-flow
  - flow-matching
  - velocity-field
- idx: 37
  start_sec: 2272.48
  end_sec: 2349.68
  text: '>> Yeah. No no this is what we chose. This

    is a design choice. So that so this is a design choice. So that so this is a design
    choice. So that so this

    thing is generalizable to any kind of thing is generalizable to any kind of thing
    is generalizable to any kind of

    path. Yeah. path. Yeah. path. Yeah.

    >> How is the ptxt given x1 that >> How is the ptxt given x1 that >> How is the
    ptxt given x1 that

    >> how is what >> how is what >> how is what

    >> the third length? How is the third? >> the third length? How is the third?
    >> the third length? How is the third?

    Oh, here. Oh, here. Oh, here.

    >> Well, because x0 is zero mean gausian. >> Well, because x0 is zero mean gausian.
    >> Well, because x0 is zero mean gausian.

    >> Yeah. >> Yeah.

    All right. Any other? Yeah. All right. Any other? Yeah. All right. Any other?
    Yeah.

    >> I don''t see any like >> I don''t see any like >> I don''t see any like

    gausian assumption. gausian assumption. gausian assumption.

    >> Oh, there''s no gausian assumption. You >> Oh, there''s no gausian assumption.
    You >> Oh, there''s no gausian assumption. You

    don''t need gian assumption. don''t need gian assumption. don''t need gian assumption.

    >> Just assume that the noise is any >> Just assume that the noise is any >> Just
    assume that the noise is any

    distribution. It still works. distribution. It still works. distribution. It still
    works.

    >> Yes. Well, um, well, Well, um, well,

    yeah, pretty much. Yeah, you you don''t yeah, pretty much. Yeah, you you don''t
    yeah, pretty much. Yeah, you you don''t

    you don''t really need Gausian here. >> Any reason other than simplicity for >>
    Any reason other than simplicity for

    choosing? choosing? choosing?

    Um Um Um

    here here here

    not really like but like what what is not really like but like what what is not
    really like but like what what is

    the other uh uh what is the other the other uh uh what is the other the other
    uh uh what is the other

    distribution that you can think of that distribution that you can think of that
    distribution that you can think of that

    we can directly sample from we can directly sample from'
  concept_slugs:
  - continuous-normalizing-flow
  - flow-matching
  - velocity-field
- idx: 38
  start_sec: 2349.68
  end_sec: 2422.48
  text: 'we can directly sample from

    >> therefor you >> like previous lectures like gausian >> like previous lectures
    like gausian

    assumption is used like this closure on assumption is used like this closure on
    assumption is used like this closure on

    the gian used in the derivation but in the gian used in the derivation but in
    the gian used in the derivation but in

    flow matching nowhere is flow matching nowhere is flow matching nowhere is

    >> yeah >> yeah >> yeah

    it''s just here it''s just that basically >> like we have previously seen that
    we can >> like we have previously seen that we can

    get some kind of stoastic differential get some kind of stoastic differential
    get some kind of stoastic differential

    equation for the equation for the equation for the

    for our scores. So here, don''t we just for our scores. So here, don''t we just
    for our scores. So here, don''t we just

    have like a parameterization of that have like a parameterization of that have
    like a parameterization of that

    same equation that will get us the same same equation that will get us the same
    same equation that will get us the same

    result? result? result?

    >> Great question. We''re going to talk >> Great question. We''re going to talk
    >> Great question. We''re going to talk

    about it later. about it later. about it later.

    >> Yeah. >> Yeah.

    >> Assuming that there''s an assumption that >> Assuming that there''s an assumption
    that >> Assuming that there''s an assumption that

    I think we assumed earlier to the come I think we assumed earlier to the come
    I think we assumed earlier to the come

    earlier that the you said the velocity earlier that the you said the velocity
    earlier that the you said the velocity

    is constant. So is constant. So is constant. So

    >> yeah, the velocity yes is constant >> yeah, the velocity yes is constant >>
    yeah, the velocity yes is constant

    speed. Yeah. But is it actually speed. Yeah. But is it actually speed. Yeah. But
    is it actually

    constant? Because last lecture I think constant? Because last lecture I think
    constant? Because last lecture I think

    we talked about stuff when we u when we we talked about stuff when we u when we'
  concept_slugs:
  - continuous-normalizing-flow
  - flow-matching
  - velocity-field
- idx: 39
  start_sec: 2422.48
  end_sec: 2486.95
  text: 'we talked about stuff when we u when we

    actually uh decrease the the velocity at actually uh decrease the the velocity
    at actually uh decrease the the velocity at

    which we adding noise. which we adding noise. which we adding noise.

    >> Here the velocity is different from >> Here the velocity is different from
    >> Here the velocity is different from

    previous class. previous class. previous class.

    So this is two different models. Um and So this is two different models. Um and
    So this is two different models. Um and

    the reason why this the reason why this the reason why this

    constant speed is because literally you constant speed is because literally you
    constant speed is because literally you

    have the t there, right? And then like have the t there, right? And then like
    have the t there, right? And then like

    literally if you derive the velocity is literally if you derive the velocity is
    literally if you derive the velocity is

    literally a constant literally a constant literally a constant

    right you have question. you have question.

    >> Oh, okay. Cool. Uh yes. Can >> Oh, okay. Cool. Uh yes. Can >> Oh, okay. Cool.
    Uh yes. Can

    >> we use this to do likelihood estimation >> we use this to do likelihood estimation
    >> we use this to do likelihood estimation

    as well or? as well or? as well or?

    >> Yes. We''re going to talk about it later. >> Yes. We''re going to talk about
    it later. >> Yes. We''re going to talk about it later.

    Yeah. Yeah. Yeah.

    Anyone else? Anyone else? Anyone else?

    Cool. Yeah. And this is the this is the Cool. Yeah. And this is the this is the
    Cool. Yeah. And this is the this is the

    uh the loss function. Literally uh the loss function. Literally uh the loss function.
    Literally

    literally just you learn the model literally just you learn the model literally
    just you learn the model

    should predict data minus noise. Yeah. should predict data minus noise. Yeah.
    should predict data minus noise. Yeah.

    >> The velocity stays constant. >> The velocity stays constant. >> The velocity
    stays constant.

    >> Um the the velocity is constant only on >> Um the the velocity is constant
    only on >> Um the the velocity is constant only on

    this particular path. Only on this'
  concept_slugs:
  - continuous-normalizing-flow
  - flow-matching
  - velocity-field
- idx: 40
  start_sec: 2486.95
  end_sec: 2544.15
  text: 'this particular path. Only on this this particular path. Only on this

    particular x0 to x1 path. But it''s not particular x0 to x1 path. But it''s not
    particular x0 to x1 path. But it''s not

    in general. in general it''s not actually in general. in general it''s not actually
    in general. in general it''s not actually

    I think this may answer your question I think this may answer your question I
    think this may answer your question

    yeah so basically in like so the left yeah so basically in like so the left yeah
    so basically in like so the left

    hand side is like the the path that you hand side is like the the path that you
    hand side is like the the path that you

    construct at training time so everything construct at training time so everything
    construct at training time so everything

    is straight right everything is straight is straight right everything is straight
    is straight right everything is straight

    but the learn the function will you have but the learn the function will you have
    but the learn the function will you have

    this averaging effect right so you learn this averaging effect right so you learn
    this averaging effect right so you learn

    the the the the entire field so you the the the the entire field so you the the
    the the entire field so you

    don''t don''t don''t

    have this straight line anymore actually have this straight line anymore actually
    have this straight line anymore actually

    but you have this like curve curve the but you have this like curve curve the
    but you have this like curve curve the

    slightly curved average field still normalizing flow right yeah still normalizing
    flow right yeah

    because because you have the one to one because because you have the one to one
    because because you have the one to one

    you have the the the invertible you have the the the invertible you have the the
    the invertible

    invertability invertability invertability

    okay any question okay any question okay any question

    >> yes >> yes >> yes

    >> why is it slightly collapsing in the >> why is it slightly collapsing in the
    >> why is it slightly collapsing in the

    middle middle middle

    >> because if you look at the if you look'
  concept_slugs:
  - continuous-normalizing-flow
  - flow-matching
  - velocity-field
- idx: 41
  start_sec: 2544.15
  end_sec: 2596.96
  text: '>> because if you look at the if you look >> because if you look at the if
    you look

    at the this the the left hand side right at the this the the left hand side right
    at the this the the left hand side right

    so like you can see how the field is not so like you can see how the field is
    not so like you can see how the field is not

    like the field has a collapsing. So like like the field has a collapsing. So like
    like the field has a collapsing. So like

    the the the margin so we''re later on the the the margin so we''re later on the
    the the margin so we''re later on

    when when when

    sampling we''re using it as if it''s the sampling we''re using it as if it''s
    the sampling we''re using it as if it''s the

    marginal and the marginal has this like marginal and the marginal has this like
    marginal and the marginal has this like

    slight slight concentration in the in slight slight concentration in the in slight
    slight concentration in the in

    the middle. Yep. the middle. Yep. the middle. Yep.

    >> So in this case if I were to pass the >> So in this case if I were to pass
    the >> So in this case if I were to pass the

    same gshian input twice to the model I same gshian input twice to the model I
    same gshian input twice to the model I

    get the same image out. get the same image out. get the same image out.

    >> Yes. It''s deterministic completely which >> Yes. It''s deterministic completely
    which >> Yes. It''s deterministic completely which

    is different from diffusion right? is different from diffusion right? is different
    from diffusion right?

    >> Yes. >> Yes.

    Okay, any more question? Cool. Actually, this thing is like super Cool. Actually,
    this thing is like super

    cool because the same algorithm was cool because the same algorithm was cool because
    the same algorithm was

    developed by three different group of developed by three different group of developed
    by three different group of

    people at literally the same time like people at literally the same time like
    people at literally the same time like

    literally the same conference and they literally the same conference and they'
  concept_slugs:
  - continuous-normalizing-flow
  - flow-matching
  - velocity-field
- idx: 42
  start_sec: 2596.96
  end_sec: 2640.079
  text: 'literally the same conference and they

    all got into the same conference. all got into the same conference. all got into
    the same conference.

    So yeah, so the first group is a group So yeah, so the first group is a group
    So yeah, so the first group is a group

    in Metafair and in Metafair and in Metafair and

    this is the group that I interned at this is the group that I interned at this
    is the group that I interned at

    actually. Um and then the second group I actually. Um and then the second group
    I actually. Um and then the second group I

    believe is a group from UT Austin and believe is a group from UT Austin and believe
    is a group from UT Austin and

    then the third group is a group from uh then the third group is a group from uh
    then the third group is a group from uh

    NYU and they all derive the same NYU and they all derive the same NYU and they
    all derive the same

    algorithm from different uh theoretical algorithm from different uh theoretical
    algorithm from different uh theoretical

    perspective and all submit to the same perspective and all submit to the same
    perspective and all submit to the same

    conference and all got in. conference and all got in. conference and all got in.

    So this is like sort of like a beautiful So this is like sort of like a beautiful
    So this is like sort of like a beautiful

    moment of science where you just kind of moment of science where you just kind
    of moment of science where you just kind of

    have like a collapsing ideas but like have like a collapsing ideas but like have
    like a collapsing ideas but like

    they''re from different points you know they''re from different points you know
    they''re from different points you know

    it''s just like our you know flow it''s just like our you know flow it''s just
    like our you know flow

    matching everyone goes to the same point matching everyone goes to the same point
    matching everyone goes to the same point

    anyway. Yeah, pretty pretty magical. Um, anyway. Yeah, pretty pretty magical.
    Um, anyway. Yeah, pretty pretty magical. Um,

    but you may have this question, right? I but you may have this question, right?
    I'
  concept_slugs:
  - continuous-normalizing-flow
  - flow-matching
  - velocity-field
- idx: 43
  start_sec: 2640.079
  end_sec: 2698.8
  text: 'but you may have this question, right? I

    feel like some people are having this feel like some people are having this feel
    like some people are having this

    question but they didn''t ask. So like question but they didn''t ask. So like
    question but they didn''t ask. So like

    the marginal flow has some dips to it, the marginal flow has some dips to it,
    the marginal flow has some dips to it,

    right? So it doesn''t it''s not completely right? So it doesn''t it''s not completely
    right? So it doesn''t it''s not completely

    straight. It''s not the straightest. So straight. It''s not the straightest. So
    straight. It''s not the straightest. So

    is there a way that we can like let''s is there a way that we can like let''s
    is there a way that we can like let''s

    say now we have trained a flow matching say now we have trained a flow matching
    say now we have trained a flow matching

    model now. So now we have this this this model now. So now we have this this this
    model now. So now we have this this this

    um like this invertability this coupling um like this invertability this coupling
    um like this invertability this coupling

    already. Is there a way to already. Is there a way to already. Is there a way
    to

    make this even straighter? Is it make this even straighter? Is it make this even
    straighter? Is it

    possible directly move from your P 0 to directly move from your P 0 to

    >> Yeah, pretty much. Pretty much. Um, so >> Yeah, pretty much. Pretty much. Um,
    so >> Yeah, pretty much. Pretty much. Um, so

    this thing is what we call reflow. So this thing is what we call reflow. So this
    thing is what we call reflow. So

    this is a technique that developed by by this is a technique that developed by
    by this is a technique that developed by by

    the second group of people who proposed the second group of people who proposed
    the second group of people who proposed

    the same thing. Uh so basically what you the same thing. Uh so basically what
    you the same thing. Uh so basically what you

    do is now let''s say you you after do is now let''s say you you after'
  concept_slugs:
  - continuous-normalizing-flow
  - flow-matching
  - velocity-field
- idx: 44
  start_sec: 2698.8
  end_sec: 2750.79
  text: 'do is now let''s say you you after

    training with the linear interpolation training with the linear interpolation
    training with the linear interpolation

    you already got this coupling. So the you already got this coupling. So the you
    already got this coupling. So the

    blue coupling and the the green coupling blue coupling and the the green coupling
    blue coupling and the the green coupling

    and then what you can do is you can just and then what you can do is you can just
    and then what you can do is you can just

    like use this coupling as your new like use this coupling as your new like use
    this coupling as your new

    ground truth and then instead of like ground truth and then instead of like ground
    truth and then instead of like

    randomly sampling from a gausian you randomly sampling from a gausian you randomly
    sampling from a gausian you

    sample from the coupling and then you sample from the coupling and then you sample
    from the coupling and then you

    can get the straight points can get the straight points can get the straight points

    and then it become more straight. Let me explain again. Let me explain again.

    >> Oh, okay. One more time. One more time. >> Oh, okay. One more time. One more
    time. >> Oh, okay. One more time. One more time.

    So, basically this is like your first So, basically this is like your first So,
    basically this is like your first

    time uh flow matching. So, basically time uh flow matching. So, basically time
    uh flow matching. So, basically

    after computing all the the the the in after computing all the the the the in
    after computing all the the the the in

    the uh linear interpolations, you get the uh linear interpolations, you get the
    uh linear interpolations, you get

    this like slightly dipped um marginals, this like slightly dipped um marginals,
    this like slightly dipped um marginals,

    right? You get this slightly dipped right? You get this slightly dipped right?
    You get this slightly dipped

    version, but now you have a a coupling version, but now you have a a coupling
    version, but now you have a a coupling

    because the thing is deterministic, because the thing is deterministic, because
    the thing is deterministic,

    right? So you can map from one point in'
  concept_slugs:
  - continuous-normalizing-flow
  - flow-matching
  - velocity-field
- idx: 45
  start_sec: 2750.79
  end_sec: 2794.88
  text: 'right? So you can map from one point in right? So you can map from one point
    in

    P 0 to another point in P1 and then you P 0 to another point in P1 and then you
    P 0 to another point in P1 and then you

    just use that coupling as your new just use that coupling as your new just use
    that coupling as your new

    ground truth. So instead of like ground truth. So instead of like ground truth.
    So instead of like

    randomly sampling your your your randomly sampling your your your randomly sampling
    your your your

    coupling like what we do what we did in coupling like what we do what we did in
    coupling like what we do what we did in

    the original flow matching you just use the original flow matching you just use
    the original flow matching you just use

    that coupling as your ground truth and that coupling as your ground truth and
    that coupling as your ground truth and

    train for matching again and then it''s train for matching again and then it''s
    train for matching again and then it''s

    going to get straightened up. >> Yeah. Go ahead. Because when you sample >> Yeah.
    Go ahead. Because when you sample

    um the more the more linear your clothes um the more the more linear your clothes
    um the more the more linear your clothes

    are, the less test. are, the less test. are, the less test.

    >> Yes, exactly. So, think about it, right? >> Yes, exactly. So, think about it,
    right? >> Yes, exactly. So, think about it, right?

    Um like if you have say if you have this Um like if you have say if you have this
    Um like if you have say if you have this

    dip, right? You have you have this dip dip, right? You have you have this dip
    dip, right? You have you have this dip

    then like like the safer bet for you to then like like the safer bet for you to
    then like like the safer bet for you to

    sample is to take two steps, right? sample is to take two steps, right? sample
    is to take two steps, right?

    because you don''t know like basically if because you don''t know like basically
    if'
  concept_slugs:
  - continuous-normalizing-flow
  - flow-matching
  - velocity-field
- idx: 46
  start_sec: 2794.88
  end_sec: 2856.23
  text: 'because you don''t know like basically if

    you if you only do one step there can be you if you only do one step there can
    be you if you only do one step there can be

    like a lot of um uh uh like like like a lot of um uh uh like like like a lot of
    um uh uh like like

    discretization error that is happening discretization error that is happening
    discretization error that is happening

    because of this dip. But if you have a because of this dip. But if you have a
    because of this dip. But if you have a

    very straight line then you can just do very straight line then you can just do
    very straight line then you can just do

    one step and it''s straight. So one step one step and it''s straight. So one step
    one step and it''s straight. So one step

    is fine right? So straighter you are uh is fine right? So straighter you are uh
    is fine right? So straighter you are uh

    the better you are at this like few step the better you are at this like few step
    the better you are at this like few step

    sampling. How do you decide what to cover? How do you decide what to cover?

    >> By your previous model, right? By the >> By your previous model, right? By
    the >> By your previous model, right? By the

    model that you learned. So, model that you learned. So, model that you learned.
    So,

    so this blue this this this blue and so this blue this this this blue and so this
    blue this this this blue and

    green are the coupling induced by your green are the coupling induced by your
    green are the coupling induced by your

    learn the flow matching model and then learn the flow matching model and then
    learn the flow matching model and then

    you just use this this coupling and then you just use this this coupling and then
    you just use this this coupling and then

    do flow matching again on the new model. do flow matching again on the new model.
    do flow matching again on the new model.

    Yeah. >> It won''t collide because it''s >> It won''t collide because it''s

    It''s a flow. It never cross. Yeah.'
  concept_slugs:
  - continuous-normalizing-flow
  - flow-matching
  - velocity-field
- idx: 47
  start_sec: 2857.67
  end_sec: 2897.99
  text: '>> The third image is the linear >> The third image is the linear

    interpolation of the new coupling. interpolation of the new coupling. interpolation
    of the new coupling.

    >> That what is that doing? >> That what is that doing? >> That what is that doing?

    >> Oh, this thing is just like show you the >> Oh, this thing is just like show
    you the >> Oh, this thing is just like show you the

    marginal kind of. marginal kind of. marginal kind of.

    >> Yeah. >> Yeah.

    >> The green is going up. But so on the >> The green is going up. But so on the
    >> The green is going up. But so on the

    >> Yeah. Yeah. Yeah. No. Remember how this >> Yeah. Yeah. Yeah. No. Remember how
    this >> Yeah. Yeah. Yeah. No. Remember how this

    you have a you have a concentration in you have a you have a concentration in
    you have a you have a concentration in

    the middle. you have a dip, right? So, the middle. you have a dip, right? So,
    the middle. you have a dip, right? So,

    it''s sort of the same thing here. it''s sort of the same thing here. it''s sort
    of the same thing here.

    >> Is it when you''re doing the sampling? >> Is it when you''re doing the sampling?
    >> Is it when you''re doing the sampling?

    >> No, no. Linear interpolation is just >> No, no. Linear interpolation is just
    >> No, no. Linear interpolation is just

    coupling. So, like you you you choose coupling. So, like you you you choose coupling.
    So, like you you you choose

    you you choose a you you choose a sample you you choose a you you choose a sample
    you you choose a you you choose a sample

    here, you choose a sample here and then here, you choose a sample here and then
    here, you choose a sample here and then

    you straight line and then you connect you straight line and then you connect
    you straight line and then you connect

    them with a straight line. them with a straight line. them with a straight line.

    >> Sample from both side. We mostly >> Sample from both side. We mostly >> Sample
    from both side. We mostly

    connected this side to that side and'
  concept_slugs:
  - continuous-normalizing-flow
  - flow-matching
  - velocity-field
- idx: 48
  start_sec: 2897.99
  end_sec: 2936.559
  text: 'connected this side to that side and connected this side to that side and

    that side to this side. There''s no that side to this side. There''s no that side
    to this side. There''s no

    there''s no this anymore because because there''s no this anymore because because
    there''s no this anymore because because

    it won''t be basically the the the it won''t be basically the the the it won''t
    be basically the the the

    coupling tells you that you will not go coupling tells you that you will not go
    coupling tells you that you will not go

    to the other side anymore because to the other side anymore because to the other
    side anymore because

    otherwise it will cross and then your otherwise it will cross and then your otherwise
    it will cross and then your

    stream will never cross. stream will never cross. stream will never cross.

    >> Yeah. >> Yeah.

    >> You have a data set that you know has >> You have a data set that you know
    has >> You have a data set that you know has

    multiple classes. Could you use this to multiple classes. Could you use this to
    multiple classes. Could you use this to

    disentangle them? disentangle them? disentangle them?

    >> Yes. And also actually um there''s >> Yes. And also actually um there''s >>
    Yes. And also actually um there''s

    another paper I didn''t put it here that another paper I didn''t put it here that
    another paper I didn''t put it here that

    if you already have a coupling in your if you already have a coupling in your
    if you already have a coupling in your

    data set you can just directly use it to data set you can just directly use it
    to data set you can just directly use it to

    train flow matching. You don''t have to train flow matching. You don''t have to
    train flow matching. You don''t have to

    do random sampling. Yeah, I think do random sampling. Yeah, I think do random
    sampling. Yeah, I think

    someone has Yeah. someone has Yeah. someone has Yeah.

    >> If your flow matching model is not >> If your flow matching model is not >>
    If your flow matching model is not

    perfectly trained into this process, perfectly trained into this process,'
  concept_slugs:
  - continuous-normalizing-flow
  - flow-matching
  - velocity-field
- idx: 49
  start_sec: 2936.559
  end_sec: 2984.24
  text: 'perfectly trained into this process,

    >> then you do it again. Yeah. Yeah. So, >> then you do it again. Yeah. Yeah.
    So, >> then you do it again. Yeah. Yeah. So,

    this is just you you get it this is just you you get it this is just you you get
    it

    straightened. It''s not guaranteed that straightened. It''s not guaranteed that
    straightened. It''s not guaranteed that

    you''re going to get straight uh like you''re going to get straight uh like you''re
    going to get straight uh like

    path on on on the on one go. Just like path on on on the on one go. Just like
    path on on on the on one go. Just like

    you''re just going to get straighter and you''re just going to get straighter
    and you''re just going to get straighter and

    straighter kind of. Yeah, it it''s straighter kind of. Yeah, it it''s straighter
    kind of. Yeah, it it''s

    definitely possible. Yeah. Oh. No. Okay. No, nobody. No. Okay. No, nobody.

    Cool. All right. So, just to summarize Cool. All right. So, just to summarize
    Cool. All right. So, just to summarize

    everything. So, just what''s the everything. So, just what''s the everything.
    So, just what''s the

    difference between diffusion and flow difference between diffusion and flow difference
    between diffusion and flow

    matching in this context, right? So, matching in this context, right? So, matching
    in this context, right? So,

    diffusion is sort of like you are diffusion is sort of like you are diffusion
    is sort of like you are

    wandering in the wood and with a compass wandering in the wood and with a compass
    wandering in the wood and with a compass

    uh like in your hand. So, you know like uh like in your hand. So, you know like
    uh like in your hand. So, you know like

    you kind of know which direction you''re you kind of know which direction you''re
    you kind of know which direction you''re

    going, but you''re still like you''re kind going, but you''re still like you''re
    kind going, but you''re still like you''re kind

    of just like exploring a little bit as of just like exploring a little bit as
    of just like exploring a little bit as

    well. you''re just like kind of random well. you''re just like kind of random'
  concept_slugs:
  - continuous-normalizing-flow
  - flow-matching
  - velocity-field
- idx: 50
  start_sec: 2984.24
  end_sec: 3027.349
  text: 'well. you''re just like kind of random

    random walking a little bit. Whereas for random walking a little bit. Whereas
    for random walking a little bit. Whereas for

    flow matching, you don''t really do flow matching, you don''t really do flow matching,
    you don''t really do

    random walking anymore. You just like random walking anymore. You just like random
    walking anymore. You just like

    sit on the boat and then go go down the sit on the boat and then go go down the
    sit on the boat and then go go down the

    stream uh on the river. So this is kind stream uh on the river. So this is kind
    stream uh on the river. So this is kind

    of what like to conceptually what is of what like to conceptually what is of what
    like to conceptually what is

    happening. Yeah. happening. Yeah. happening. Yeah.

    >> Like is this used now? Like if it''s so >> Like is this used now? Like if it''s
    so >> Like is this used now? Like if it''s so

    good this good this good this

    >> great question. >> great question. >> great question.

    >> Do you know flux? Do you know the the >> Do you know flux? Do you know the
    the >> Do you know flux? Do you know the the

    black for that''s full matching? Yeah. black for that''s full matching? Yeah.
    black for that''s full matching? Yeah.

    This is like the state of the art This is like the state of the art This is like
    the state of the art

    basically. It''s actually crazy good and basically. It''s actually crazy good
    and basically. It''s actually crazy good and

    it''s so simple, right? Okay. So, so far it''s so simple, right? Okay. So, so
    far it''s so simple, right? Okay. So, so far

    we have seen so many gen models and we we have seen so many gen models and we
    we have seen so many gen models and we

    know that the diffusion model and know that the diffusion model and know that
    the diffusion model and

    scorebased model are same thing and scorebased model are same thing and scorebased
    model are same thing and

    today we learned flow matching. Now the today we learned flow matching. Now the
    today we learned flow matching. Now the

    question is is flow matching also the'
  concept_slugs:
  - continuous-normalizing-flow
  - flow-matching
  - velocity-field
- idx: 51
  start_sec: 3027.349
  end_sec: 3072.47
  text: 'question is is flow matching also the question is is flow matching also the

    same thing because if you think about it same thing because if you think about
    it same thing because if you think about it

    you''re also like adding a lot of noise you''re also like adding a lot of noise
    you''re also like adding a lot of noise

    like and then d noiseis is kind of like and then d noiseis is kind of like and
    then d noiseis is kind of

    dinoising right you''re just like a lot dinoising right you''re just like a lot
    dinoising right you''re just like a lot

    of noisy samples in the middle is are of noisy samples in the middle is are of
    noisy samples in the middle is are

    they the same thing? they the same thing? they the same thing?

    What do we think kind of actually? So basically what you kind of actually? So
    basically what you

    can do so this is what we had before can do so this is what we had before can
    do so this is what we had before

    right uh we have this like very straight right uh we have this like very straight
    right uh we have this like very straight

    line but what if you define something line but what if you define something line
    but what if you define something

    because the flow matching theory can be because the flow matching theory can be
    because the flow matching theory can be

    applied to any path right like what applied to any path right like what applied
    to any path right like what

    Dwanch was asking so we can also define Dwanch was asking so we can also define
    Dwanch was asking so we can also define

    a path from what we just learned uh on a path from what we just learned uh on
    a path from what we just learned uh on

    Tuesday right so you can define a a v Tuesday right so you can define a a v Tuesday
    right so you can define a a v

    path a v uh like diffusion path and you path a v uh like diffusion path and you
    path a v uh like diffusion path and you

    can write everything as if it is flow'
  concept_slugs:
  - continuous-normalizing-flow
  - flow-matching
  - velocity-field
- idx: 52
  start_sec: 3072.47
  end_sec: 3123.04
  text: 'can write everything as if it is flow can write everything as if it is flow

    matching as well and then you can matching as well and then you can matching as
    well and then you can

    actually just recover for V SD with actually just recover for V SD with actually
    just recover for V SD with

    obviously obviously obviously

    with with the noise adding to it. with with the noise adding to it. with with
    the noise adding to it.

    And what about if we do what can can And what about if we do what can can And
    what about if we do what can can

    what about the other way around, right? what about the other way around, right?
    what about the other way around, right?

    Can we do score SDE Can we do score SDE Can we do score SDE

    transform into an OD a flow OD? Can we transform into an OD a flow OD? Can we
    transform into an OD a flow OD? Can we

    do that? What do we think by looking at do that? What do we think by looking at
    do that? What do we think by looking at

    this this this

    formula? Okay, just get rid of the the G part, Okay, just get rid of the the G
    part,

    right? Is that what you said? All right. right? Is that what you said? All right.
    right? Is that what you said? All right.

    So, basically at this part look like a So, basically at this part look like a
    So, basically at this part look like a

    velocity, right? velocity, right? velocity, right?

    But the problem is like the G part, the But the problem is like the G part, the
    But the problem is like the G part, the

    the brown in motion part, this part the brown in motion part, this part the brown
    in motion part, this part

    actually induce some probability because actually induce some probability because
    actually induce some probability because

    it''s a gausian, right? So, we still it''s a gausian, right? So, we still it''s
    a gausian, right? So, we still

    induce some probability there. So, we induce some probability there. So, we induce
    some probability there. So, we

    still need to take care of that part. still need to take care of that part.'
  concept_slugs:
  - continuous-normalizing-flow
  - flow-matching
  - velocity-field
- idx: 53
  start_sec: 3123.04
  end_sec: 3164.95
  text: 'still need to take care of that part.

    But it turns out that we actually do But it turns out that we actually do But
    it turns out that we actually do

    know how to take care of that part. And know how to take care of that part. And
    know how to take care of that part. And

    this thing is called focal plank PDE. this thing is called focal plank PDE. this
    thing is called focal plank PDE.

    All right? uh the the name is really All right? uh the the name is really All
    right? uh the the name is really

    fancy but basically what it means is fancy but basically what it means is fancy
    but basically what it means is

    that like if you if you have some that like if you if you have some that like
    if you if you have some

    probability in it the focal point PTE um probability in it the focal point PTE
    um probability in it the focal point PTE um

    it''s going to tell you it''s going to tell you it''s going to tell you

    how your probability changes through how your probability changes through how
    your probability changes through

    this through this PTE that you can this through this PTE that you can this through
    this PTE that you can

    derive uh and if you''re interested in derive uh and if you''re interested in
    derive uh and if you''re interested in

    the derivation of this PD for the the derivation of this PD for the the derivation
    of this PD for the

    interest of time we''re not going to go interest of time we''re not going to go
    interest of time we''re not going to go

    over it but it''s in the in the the over it but it''s in the in the the over it
    but it''s in the in the the

    principle of diffusion model book so you principle of diffusion model book so
    you principle of diffusion model book so you

    can take a look at it um but basically can take a look at it um but basically
    can take a look at it um but basically

    Okay. And now we have probability flow Okay. And now we have probability flow
    Okay. And now we have probability flow

    OD, right? So this is the just um say we'
  concept_slugs:
  - continuous-normalizing-flow
  - flow-matching
  - velocity-field
- idx: 54
  start_sec: 3164.95
  end_sec: 3210.0
  text: 'OD, right? So this is the just um say we OD, right? So this is the just um
    say we

    have this particular OD and it turns out have this particular OD and it turns
    out have this particular OD and it turns out

    that it''s contin continuity equation that it''s contin continuity equation that
    it''s contin continuity equation

    which is like the the PD of the change which is like the the PD of the change
    which is like the the PD of the change

    of um probability which is what we of um probability which is what we of um probability
    which is what we

    learned today by using the divergence is learned today by using the divergence
    is learned today by using the divergence is

    actually so if you just like plug actually so if you just like plug actually so
    if you just like plug

    everything in and then you do a lot of everything in and then you do a lot of
    everything in and then you do a lot of

    algebra and and calculus uh you are algebra and and calculus uh you are algebra
    and and calculus uh you are

    actually going to get the same thing actually going to get the same thing actually
    going to get the same thing

    literally the same thing. So this is literally the same thing. So this is literally
    the same thing. So this is

    just saying that the rate of like the just saying that the rate of like the just
    saying that the rate of like the

    rate of change in probability rate of change in probability rate of change in
    probability

    from this score SD or from this 4 SD from this score SD or from this 4 SD from
    this score SD or from this 4 SD

    they share the same uh which is the same they share the same uh which is the same
    they share the same uh which is the same

    as this probability flow OD as this probability flow OD as this probability flow
    OD

    this and the same PD for the rate of this and the same PD for the rate of this
    and the same PD for the rate of

    change for the probability means that change for the probability means that'
  concept_slugs:
  - continuous-normalizing-flow
  - flow-matching
  - velocity-field
- idx: 55
  start_sec: 3210.0
  end_sec: 3276.309
  text: 'change for the probability means that

    the marginalss are all the same. So this the marginalss are all the same. So this
    the marginalss are all the same. So this

    just means that now if you have your just means that now if you have your just
    means that now if you have your

    score function instead of sampling from score function instead of sampling from
    score function instead of sampling from

    an SD you can do OD samples now. Yay. Yay. Yay. Yay.

    Well, no excitement. It''s okay. Um what Well, no excitement. It''s okay. Um what
    Well, no excitement. It''s okay. Um what

    else can you else can you else can you

    with OD? Right. I think someone someone with OD? Right. I think someone someone
    with OD? Right. I think someone someone

    said before that like we can do density said before that like we can do density
    said before that like we can do density

    estimation with this, right? So estimation with this, right? So estimation with
    this, right? So

    literally this is true, right? So you literally this is true, right? So you literally
    this is true, right? So you

    can literally just um um swap in the the can literally just um um swap in the
    the can literally just um um swap in the the

    velocity here and then you just like go velocity here and then you just like go
    velocity here and then you just like go

    back in time through your OD and then back in time through your OD and then back
    in time through your OD and then

    you''re able to calculate the log density you''re able to calculate the log density
    you''re able to calculate the log density

    of your data point. of your data point. of your data point.

    Cool. And Cool. And Cool. And

    what about density estimation for what about density estimation for what about
    density estimation for

    diffusion, right? diffusion, right? diffusion, right?

    Oh, density estimation means that like Oh, density estimation means that like
    Oh, density estimation means that like

    just like to calculate uh the likelihood just like to calculate uh the likelihood
    just like to calculate uh the likelihood

    of the the the the day. of the the the the day. of the the the the day.

    >> That''s a great question. Um so for'
  concept_slugs:
  - continuous-normalizing-flow
  - flow-matching
  - velocity-field
- idx: 56
  start_sec: 3276.309
  end_sec: 3340.95
  text: '>> That''s a great question. Um so for >> That''s a great question. Um so
    for

    example, I don''t know if you guys example, I don''t know if you guys example,
    I don''t know if you guys

    familiar with the RL. familiar with the RL. familiar with the RL.

    >> All right, cool. Anyway, >> All right, cool. Anyway, >> All right, cool. Anyway,

    and so for density estimation for and so for density estimation for and so for
    density estimation for

    diffusion, uh the easiest thing is that diffusion, uh the easiest thing is that
    diffusion, uh the easiest thing is that

    because the loss function that we because the loss function that we because the
    loss function that we

    derived from two lectures ago is a derived from two lectures ago is a derived
    from two lectures ago is a

    elbow, right? So we can just directly elbow, right? So we can just directly elbow,
    right? So we can just directly

    use this elbow as an estimate of the use this elbow as an estimate of the use
    this elbow as an estimate of the

    likelihood. That''s fine. But this is not likelihood. That''s fine. But this is
    not likelihood. That''s fine. But this is not

    accurate because it''s a elbow. It''s a accurate because it''s a elbow. It''s
    a accurate because it''s a elbow. It''s a

    lower bound. It''s it''s not really the lower bound. It''s it''s not really the
    lower bound. It''s it''s not really the

    the real log log likelihood, right? So the real log log likelihood, right? So
    the real log log likelihood, right? So

    is there another way to do it? I feel like someone someone here knows I feel like
    someone someone here knows

    already. Okay. What do we think? What do we Okay. What do we think? What do we

    think? We know we know how to calculate the We know we know how to calculate the

    exact log likelihood from OD. What do we exact log likelihood from OD. What do
    we exact log likelihood from OD. What do we

    do if we have a score SDE? What do we do if we have a score SDE? What do we do
    if we have a score SDE? What do we

    do? do? do?

    Use the use the corresponding PF OD of'
  concept_slugs:
  - continuous-normalizing-flow
  - flow-matching
  - velocity-field
- idx: 57
  start_sec: 3340.95
  end_sec: 3427.28
  text: 'Use the use the corresponding PF OD of Use the use the corresponding PF OD
    of

    the SDE. Right? So you just plug it in the SDE. Right? So you just plug it in
    the SDE. Right? So you just plug it in

    and then it''s the same and then it''s the same and then it''s the same

    as for matching. Yes, Yes,

    >> it''s like that. >> it''s like that. >> it''s like that.

    >> Um, >> Um, >> Um,

    one one one

    one one

    >> Okay. >> Okay. >> Okay.

    >> Yeah, >> Yeah, >> Yeah,

    you can sample with an OD. What is like you can sample with an OD. What is like
    you can sample with an OD. What is like

    sampling? sampling? sampling?

    >> Oh, yes. Yes. So you can sample with >> Oh, yes. Yes. So you can sample with
    >> Oh, yes. Yes. So you can sample with

    this OD meaning that like you can you this OD meaning that like you can you this
    OD meaning that like you can you

    can literally do uh let''s see you can can literally do uh let''s see you can
    can literally do uh let''s see you can

    you can literally just do numerical you can literally just do numerical you can
    literally just do numerical

    integration from x0 and then you do x0 integration from x0 and then you do x0
    integration from x0 and then you do x0

    plus um integrate from zero to one plus um integrate from zero to one plus um
    integrate from zero to one

    velocity and this velocity is just this velocity and this velocity is just this
    velocity and this velocity is just this

    odz >> uh what do you mean the sampling is only >> uh what do you mean the sampling
    is only

    x0 oh you mean like to sample from a x0 oh you mean like to sample from a x0 oh
    you mean like to sample from a

    distribution yes that''s right Yeah. distribution yes that''s right Yeah. distribution
    yes that''s right Yeah.

    Cool. Cool. Oh, yeah. Yeah. Yeah. Oh, yeah. Yeah. Yeah.

    >> Yeah. >> Yeah.

    >> A lot of uh uh lot of PD getting >> A lot of uh uh lot of PD getting'
  concept_slugs:
  - continuous-normalizing-flow
  - flow-matching
  - velocity-field
- idx: 58
  start_sec: 3427.28
  end_sec: 3473.44
  text: '>> A lot of uh uh lot of PD getting

    converted to OD. Is it are we just doing converted to OD. Is it are we just doing
    converted to OD. Is it are we just doing

    it because it''s simpler or do we you it because it''s simpler or do we you it
    because it''s simpler or do we you

    want a better velocity? want a better velocity? want a better velocity?

    >> Uh no you mean here here it''s because >> Uh no you mean here here it''s because
    >> Uh no you mean here here it''s because

    it''s exact. So in in uh in comparison to it''s exact. So in in uh in comparison
    to it''s exact. So in in uh in comparison to

    the elbow right if you compare to the the elbow right if you compare to the the
    elbow right if you compare to the

    elbow the elbow is a lower bound of your elbow the elbow is a lower bound of your
    elbow the elbow is a lower bound of your

    um of your lo likelihood which is not um of your lo likelihood which is not um
    of your lo likelihood which is not

    exact but here we can actually get an exact but here we can actually get an exact
    but here we can actually get an

    exact log likelihood. exact log likelihood. exact log likelihood.

    Yeah. Yeah.

    >> Intrinsically Asian suffer from >> Intrinsically Asian suffer from >> Intrinsically
    Asian suffer from

    diversity, right? Because diversity, right? Because diversity, right? Because

    >> it suffers from uh discretization error. >> it suffers from uh discretization
    error. >> it suffers from uh discretization error.

    Is that what you mean? Like basically if Is that what you mean? Like basically
    if Is that what you mean? Like basically if

    you take the step and then you take the step and then you take the step and then

    because uh because uh because uh

    >> ah uh well well here you''re calculating >> ah uh well well here you''re calculating
    >> ah uh well well here you''re calculating

    the the the log likelihood. So it''s not the the the log likelihood. So it''s
    not the the the log likelihood. So it''s not

    diversity but but yes so like diversity but but yes so like'
  concept_slugs:
  - continuous-normalizing-flow
  - flow-matching
  - velocity-field
- idx: 59
  start_sec: 3473.44
  end_sec: 3546.309
  text: 'diversity but but yes so like

    essentially um if you''re sampling from a essentially um if you''re sampling from
    a essentially um if you''re sampling from a

    SDE then it''s going to be yeah because SDE then it''s going to be yeah because
    SDE then it''s going to be yeah because

    you have exploration right so it''s more you have exploration right so it''s more
    you have exploration right so it''s more

    diverse than sampling from OD which is diverse than sampling from OD which is
    diverse than sampling from OD which is

    completely deterministic completely deterministic completely deterministic

    >> yeah that''s right Cool. Cool.

    Not cool. Okay. Not cool. Okay. Not cool. Okay.

    >> So, if if I want to calculate the >> So, if if I want to calculate the >> So,
    if if I want to calculate the

    likelihood of X1, likelihood of X1, likelihood of X1,

    >> I first need to find the corresponding >> I first need to find the corresponding
    >> I first need to find the corresponding

    X0 for me to start integrating. And X0 for me to start integrating. And X0 for
    me to start integrating. And

    >> hey, you have everyone you should know >> hey, you have everyone you should
    know >> hey, you have everyone you should know

    this. But anyway, continue. Yeah. Yeah. this. But anyway, continue. Yeah. Yeah.
    this. But anyway, continue. Yeah. Yeah.

    Yeah. Yeah.

    Oh yeah. So yeah. So essentially what Oh yeah. So yeah. So essentially what Oh
    yeah. So yeah. So essentially what

    you do is you you remember how you you you do is you you remember how you you
    you do is you you remember how you you

    you reverse the chain, right? >> Yeah, that is right. >> Yeah, that is right.

    >> That is right. And which is why this x0 >> That is right. And which is why
    this x0 >> That is right. And which is why this x0

    k has a hat on it. So this is a reverse k has a hat on it. So this is a reverse
    k has a hat on it. So this is a reverse

    the x0. So you first reverse your the x0. So you first reverse your the x0. So
    you first reverse your

    sampling chain through your by by by'
  concept_slugs:
  - continuous-normalizing-flow
  - flow-matching
  - velocity-field
- idx: 60
  start_sec: 3546.309
  end_sec: 3612.96
  text: 'sampling chain through your by by by sampling chain through your by by by

    backward integrating your velocity and backward integrating your velocity and
    backward integrating your velocity and

    then during the backward integration you then during the backward integration
    you then during the backward integration you

    can alo calculate the divergence at the can alo calculate the divergence at the
    can alo calculate the divergence at the

    same time. Yeah. So you you need to find the Yeah. So you you need to find the

    corresponding chain which is corresponding chain which is corresponding chain
    which is

    deterministic. But uh But uh

    >> p of x0 should be constant. >> p of x0 should be constant. >> p of x0 should
    be constant.

    >> Oh, you mean p of x? Yeah, p 0 is >> Oh, you mean p of x? Yeah, p 0 is >> Oh,
    you mean p of x? Yeah, p 0 is

    constant. Yeah, that''s right. Yeah. constant. Yeah, that''s right. Yeah. constant.
    Yeah, that''s right. Yeah.

    Yeah. If if if it''s a uniform. Yeah. If if if it''s a uniform. Yeah. If if if
    it''s a uniform.

    All right. All right. All right.

    More question. More question. More question.

    All good. All right. All good. All right. All good. All right.

    Okay. So Okay. So Okay. So

    to summarize everything and we have seen to summarize everything and we have seen
    to summarize everything and we have seen

    three models so far. Uh diffusion model, three models so far. Uh diffusion model,
    three models so far. Uh diffusion model,

    squarebased models, flow matching all squarebased models, flow matching all squarebased
    models, flow matching all

    model. They are more or less all the model. They are more or less all the model.
    They are more or less all the

    same thing. Same same different. same thing. Same same different. same thing.
    Same same different.

    I feel like saying this I''m going to I feel like saying this I''m going to I
    feel like saying this I''m going to

    offend a lot of people but but yeah know offend a lot of people but but yeah know
    offend a lot of people but but yeah know

    you know just like you know you just add you know just like you know you just
    add'
  concept_slugs:
  - continuous-normalizing-flow
  - flow-matching
  - velocity-field
- idx: 61
  start_sec: 3612.96
  end_sec: 3661.76
  text: 'you know just like you know you just add

    something divide something you it''s the something divide something you it''s
    the something divide something you it''s the

    same thing. Okay. same thing. Okay. same thing. Okay.

    >> Yeah everything is the same thing. Uh >> Yeah everything is the same thing.
    Uh >> Yeah everything is the same thing. Uh

    but yeah um so yeah congrat oh okay we but yeah um so yeah congrat oh okay we
    but yeah um so yeah congrat oh okay we

    haven''t congrat Okay. haven''t congrat Okay. haven''t congrat Okay.

    >> Uh so if we can still compute the >> Uh so if we can still compute the >> Uh
    so if we can still compute the

    likelihood using flow matching why does likelihood using flow matching why does
    likelihood using flow matching why does

    it come under likelihood free like it come under likelihood free like it come
    under likelihood free like

    what''s the classification? Oh here what''s the classification? Oh here what''s
    the classification? Oh here

    likelihood of free means that the likelihood of free means that the likelihood
    of free means that the

    training loss doesn''t have likelihood training loss doesn''t have likelihood
    training loss doesn''t have likelihood

    it''s not maximizing the likelihood but it''s not maximizing the likelihood but
    it''s not maximizing the likelihood but

    you can still compute likelihood right you can still compute likelihood right
    you can still compute likelihood right

    score same for scorebased model you can score same for scorebased model you can
    score same for scorebased model you can

    compute the likelihood compute the likelihood compute the likelihood

    through the same o pfod thing right yeah through the same o pfod thing right yeah
    through the same o pfod thing right yeah

    all right all right so congratulations all right all right so congratulations
    all right all right so congratulations

    we gone through the basics now yay now we gone through the basics now yay now
    we gone through the basics now yay now

    we know what is diffusion one is full we know what is diffusion one is full we
    know what is diffusion one is full

    matching yay um yeah so starting from matching yay um yeah so starting from matching
    yay um yeah so starting from

    next week we''re gonna be able to see next week we''re gonna be able to see'
  concept_slugs:
  - continuous-normalizing-flow
  - flow-matching
  - velocity-field
- idx: 62
  start_sec: 3661.76
  end_sec: 3701.76
  text: 'next week we''re gonna be able to see

    like like like

    uh different options to further uh different options to further uh different options
    to further

    improve what we have learned. Um so for improve what we have learned. Um so for
    improve what we have learned. Um so for

    example like I I guess you guys have if example like I I guess you guys have if
    example like I I guess you guys have if

    you guys have done the homework you you guys have done the homework you you guys
    have done the homework you

    should know this by now there''s so many should know this by now there''s so many
    should know this by now there''s so many

    knobs that you can tune right for knobs that you can tune right for knobs that
    you can tune right for

    diffusion models like what are you use diffusion models like what are you use
    diffusion models like what are you use

    how many number of steps and stuff like how many number of steps and stuff like
    how many number of steps and stuff like

    that right so you know we''re gonna we''re that right so you know we''re gonna
    we''re that right so you know we''re gonna we''re

    going to learn about that like basically going to learn about that like basically
    going to learn about that like basically

    uh there''s a paper that like just uh there''s a paper that like just uh there''s
    a paper that like just

    systematically study this uh and we are systematically study this uh and we are
    systematically study this uh and we are

    like for those of you who did uh the like for those of you who did uh the like
    for those of you who did uh the

    homework you should also notice that homework you should also notice that homework
    you should also notice that

    diffusion models sample really really diffusion models sample really really diffusion
    models sample really really

    slowly and it''s like just like slowly and it''s like just like slowly and it''s
    like just like

    It takes so much time. So how do we make It takes so much time. So how do we make
    It takes so much time. So how do we make

    the generation faster? And we''re going the generation faster? And we''re going'
  concept_slugs:
  - continuous-normalizing-flow
  - flow-matching
  - velocity-field
- idx: 63
  start_sec: 3701.76
  end_sec: 3730.68
  text: 'the generation faster? And we''re going

    to learn uh to do it with or without to learn uh to do it with or without to learn
    uh to do it with or without

    training retraining of the model. And training retraining of the model. And training
    retraining of the model. And

    lastly, right now we all the thing that lastly, right now we all the thing that
    lastly, right now we all the thing that

    we learn are unconditional generations. we learn are unconditional generations.
    we learn are unconditional generations.

    So how can we make the generation more So how can we make the generation more
    So how can we make the generation more

    controllable or conditional, right? And controllable or conditional, right? And
    controllable or conditional, right? And

    we are actually going to learn it uh to we are actually going to learn it uh to
    we are actually going to learn it uh to

    do it with training and also without do it with training and also without do it
    with training and also without

    training which is very interesting. All training which is very interesting. All
    training which is very interesting. All

    right. Uh that''s it for today. I''ll see right. Uh that''s it for today. I''ll
    see right. Uh that''s it for today. I''ll see

    you next week. Uh stay warm this uh this you next week. Uh stay warm this uh this
    you next week. Uh stay warm this uh this

    uh this this uh weekend. There''s a lot uh this this uh weekend. There''s a lot
    uh this this uh weekend. There''s a lot

    of flow going on.'
  concept_slugs:
  - continuous-normalizing-flow
  - flow-matching
  - velocity-field
---
# CMU 10799 S26: Lecture 5 - Flow Matching - Diffusion & Flow Matching

See the structured chunks above.
