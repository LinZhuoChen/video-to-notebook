---
course_slug: cmu-10799-diffusion-flow
idx: 9
title: 'CMU 10799 S26: Lecture 10 - Distillation, Consistency Models & Flow Maps -
  Diffusion & Flow Matching'
video_url: https://www.youtube.com/watch?v=L9nsCHHMv-c
duration_sec: null
chunks:
- idx: 0
  start_sec: 4.309
  end_sec: 59.6
  text: 'Okay. So, previously uh we have learned Okay. So, previously uh we have learned

    about fast sampling techniques, right? about fast sampling techniques, right?
    about fast sampling techniques, right?

    And basically we just like do a bunch of And basically we just like do a bunch
    of And basically we just like do a bunch of

    things for example like DDIM like those things for example like DDIM like those
    things for example like DDIM like those

    sampling algorithm to make the inference sampling algorithm to make the inference
    sampling algorithm to make the inference

    of the diffusion model faster. Uh we can of the diffusion model faster. Uh we
    can of the diffusion model faster. Uh we can

    you we can also use a bunch of solvers you we can also use a bunch of solvers
    you we can also use a bunch of solvers

    right because now everything is ODS. Uh right because now everything is ODS. Uh
    right because now everything is ODS. Uh

    so we can just use different OD solvers so we can just use different OD solvers
    so we can just use different OD solvers

    to do sampling. Uh however is there to do sampling. Uh however is there to do
    sampling. Uh however is there

    anything else that we can do to anything else that we can do to anything else
    that we can do to

    accelerate inference? What do we think? So, previously we all talk about like
    So, previously we all talk about like

    sampling only method. What is it? What is it?

    We''re going to talk about this soon. Uh We''re going to talk about this soon.
    Uh We''re going to talk about this soon. Uh

    distillation, right? Something like so. distillation, right? Something like so.
    distillation, right? Something like so.

    Basically, it''s like is it possible to Basically, it''s like is it possible to
    Basically, it''s like is it possible to

    train a model such that it takes less train a model such that it takes less train
    a model such that it takes less

    time to inference rather than changing a time to inference rather than changing
    a time to inference rather than changing a

    pre-tra changing the sampling of a pre-tra changing the sampling of a pre-tra
    changing the sampling of a

    pre-trained model, right? So suppose we pre-trained model, right? So suppose we'
  concept_slugs:
  - consistency-models
  - ddim
  - rectified-flow
- idx: 1
  start_sec: 59.6
  end_sec: 120.32
  text: 'pre-trained model, right? So suppose we

    already have a pre-trained diffusion already have a pre-trained diffusion already
    have a pre-trained diffusion

    model like before. Um then what is the model like before. Um then what is the
    model like before. Um then what is the

    simplest way to train another model such simplest way to train another model such
    simplest way to train another model such

    that it can still sample from the same that it can still sample from the same
    that it can still sample from the same

    distribution but faster? Yes. >> The original model at like skipped time >> The
    original model at like skipped time

    steps rather like at every time step. steps rather like at every time step. steps
    rather like at every time step.

    >> Very close very close to to to what I''m >> Very close very close to to to
    what I''m >> Very close very close to to to what I''m

    thinking. But pretty much any other any thinking. But pretty much any other any
    thinking. But pretty much any other any

    other thought besides this one? This other thought besides this one? This other
    thought besides this one? This

    one''s very close already. Someone on Zoom. Someone on Zoom.

    >> Sorry. >> Sorry. >> Sorry.

    >> Oh, okay. Okay. Sorry. Sorry. >> Oh, okay. Okay. Sorry. Sorry. >> Oh, okay.
    Okay. Sorry. Sorry.

    I just realized I guess you normally I just realized I guess you normally I just
    realized I guess you normally

    nobody''s on Zoom. Okay. Never mind. nobody''s on Zoom. Okay. Never mind. nobody''s
    on Zoom. Okay. Never mind.

    Okay. Yeah. Okay. Yeah. Okay. Yeah.

    If we have a good model that has been If we have a good model that has been If
    we have a good model that has been

    trained for a thousand times, if we take trained for a thousand times, if we take
    trained for a thousand times, if we take

    another model and for this model we only another model and for this model we only
    another model and for this model we only

    train it for say three time steps in the train it for say three time steps in
    the train it for say three time steps in the

    second time step we do a loss comparison second time step we do a loss comparison'
  concept_slugs:
  - consistency-models
  - rectified-flow
- idx: 2
  start_sec: 120.32
  end_sec: 165.04
  text: 'second time step we do a loss comparison

    with the 500 time step. Hey yes very with the 500 time step. Hey yes very with
    the 500 time step. Hey yes very

    very good very good very very good very good very good very very good very good
    very good very very good

    basically that okay uh so what if like basically that okay uh so what if like
    basically that okay uh so what if like

    instead basically what Dvanchi just said instead basically what Dvanchi just said
    instead basically what Dvanchi just said

    but like say we have we have trained but like say we have we have trained but
    like say we have we have trained

    like like a 10,00 step model then uh like like a 10,00 step model then uh like
    like a 10,00 step model then uh

    like instead of taking two steps like like instead of taking two steps like like
    instead of taking two steps like

    let''s let''s just say like how about we let''s let''s just say like how about
    we let''s let''s just say like how about we

    train a new model such that taking one train a new model such that taking one
    train a new model such that taking one

    step in the new model is equivalent to step in the new model is equivalent to
    step in the new model is equivalent to

    taking two steps taking two steps taking two steps

    in the original model right so for in the original model right so for in the original
    model right so for

    example say like with DDIM let''s just example say like with DDIM let''s just
    example say like with DDIM let''s just

    say we use DDI right and then we take say we use DDI right and then we take say
    we use DDI right and then we take

    one step and then we take another step one step and then we take another step
    one step and then we take another step

    to get to here which is t minus 2 delta to get to here which is t minus 2 delta
    to get to here which is t minus 2 delta

    t and uh how about okay let''s just do a t and uh how about okay let''s just do
    a'
  concept_slugs:
  - consistency-models
  - ddim
  - rectified-flow
- idx: 3
  start_sec: 165.04
  end_sec: 224.879
  text: 't and uh how about okay let''s just do a

    few more steps right how about we''ll few more steps right how about we''ll few
    more steps right how about we''ll

    train a new model such that um like one train a new model such that um like one
    train a new model such that um like one

    step in the new model is equal to step in the new model is equal to step in the
    new model is equal to

    equivalent to two ddimm steps right in equivalent to two ddimm steps right in
    equivalent to two ddimm steps right in

    the original diffusion and similarly the original diffusion and similarly the
    original diffusion and similarly

    right so this is this is what we can do right so this is this is what we can do
    right so this is this is what we can do

    right super easy and Uh naively this right super easy and Uh naively this right
    super easy and Uh naively this

    will give you two times speed up right will give you two times speed up right
    will give you two times speed up right

    from DDI in very nice go from zero. Yes, exactly exactly go from zero. Yes, exactly
    exactly

    exactly corre correct. Yes. So why don''t exactly corre correct. Yes. So why don''t
    exactly corre correct. Yes. So why don''t

    you can also just uh have another new you can also just uh have another new you
    can also just uh have another new

    model. So new model V2 such that you model. So new model V2 such that you model.
    So new model V2 such that you

    know taking one step in the new model V2 know taking one step in the new model
    V2 know taking one step in the new model V2

    is equivalent to taking uh two steps in is equivalent to taking uh two steps in
    is equivalent to taking uh two steps in

    the new model V1. the new model V1. the new model V1.

    Right? Does it make sense? Right? Does it make sense? Right? Does it make sense?

    Okay. So now you have progressive Okay. So now you have progressive Okay. So now
    you have progressive

    distillation. distillation. distillation.

    A So this is like yep A So this is like yep'
  concept_slugs:
  - consistency-models
  - rectified-flow
- idx: 4
  start_sec: 224.879
  end_sec: 270.23
  text: 'A So this is like yep

    >> exact as >> exact as >> exact as

    many as you want essentially. So like many as you want essentially. So like many
    as you want essentially. So like

    log to t I guess. log to t I guess. log to t I guess.

    >> Yeah. >> Yeah. >> Yeah.

    >> Doing the first model doing the four >> Doing the first model doing the four
    >> Doing the first model doing the four

    step versus the first model doing the step versus the first model doing the step
    versus the first model doing the

    two step and then the next model doing two step and then the next model doing
    two step and then the next model doing

    the two step and the second one. the two step and the second one. the two step
    and the second one.

    >> I''m confused. What do you mean? What if >> I''m confused. What do you mean?
    What if >> I''m confused. What do you mean? What if

    you started at the the second new model you started at the the second new model
    you started at the the second new model

    and that was your start and then you and that was your start and then you and
    that was your start and then you

    went to the new model. So like what if went to the new model. So like what if
    went to the new model. So like what if

    you started with every other step first you started with every other step first
    you started with every other step first

    and then went to every fourth step and then went to every fourth step and then
    went to every fourth step

    second. second. second.

    >> Well I guess you will still want to be >> Well I guess you will still want
    to be >> Well I guess you will still want to be

    able to sample from it. So you should able to sample from it. So you should able
    to sample from it. So you should

    still start from like t or zero, right? still start from like t or zero, right?
    still start from like t or zero, right?

    I guess. Uh was that your question? No. I guess. Uh was that your question? No.
    I guess. Uh was that your question? No.

    Right.'
  concept_slugs:
  - consistency-models
  - rectified-flow
- idx: 5
  start_sec: 270.23
  end_sec: 311.28
  text: 'Right. Right.

    >> So if in the first example we took the >> So if in the first example we took
    the >> So if in the first example we took the

    two two two

    steps to V1 of my new models step and in steps to V1 of my new models step and
    in steps to V1 of my new models step and in

    the next V2 version we took two steps of the next V2 version we took two steps
    of the next V2 version we took two steps of

    the P. the P. the P.

    >> Yeah. Yeah. >> Yeah. Yeah. >> Yeah. Yeah.

    >> My is instead of the like if you >> My is instead of the like if you >> My
    is instead of the like if you

    completely skip the P model and you just completely skip the P model and you just
    completely skip the P model and you just

    do the four steps to be do the four steps to be do the four steps to be

    >> Yeah. Yeah. Okay. That''s a great >> Yeah. Yeah. Okay. That''s a great >> Yeah.
    Yeah. Okay. That''s a great

    question. Okay. Let''s how about I just question. Okay. Let''s how about I just
    question. Okay. Let''s how about I just

    move on to that. Um but but anyway, this move on to that. Um but but anyway, this
    move on to that. Um but but anyway, this

    is the the pseudo code for progressive is the the pseudo code for progressive
    is the the pseudo code for progressive

    distillation. Uh but basically you can distillation. Uh but basically you can
    distillation. Uh but basically you can

    you can read the paper. I just realized you can read the paper. I just realized
    you can read the paper. I just realized

    I didn''t put citation but if you Google I didn''t put citation but if you Google
    I didn''t put citation but if you Google

    progressive distillation this is what is progressive distillation this is what
    is progressive distillation this is what is

    going to like come up and also by the going to like come up and also by the going
    to like come up and also by the

    way this is the paper that tells you way this is the paper that tells you'
  concept_slugs:
  - consistency-models
  - rectified-flow
- idx: 6
  start_sec: 311.28
  end_sec: 359.67
  text: 'way this is the paper that tells you

    that you should do V prediction like V that you should do V prediction like V
    that you should do V prediction like V

    prediction is the best parameterization prediction is the best parameterization
    prediction is the best parameterization

    yeah so it''s pretty cool but anyway um yeah so it''s pretty cool but anyway um
    yeah so it''s pretty cool but anyway um

    yeah so why are we only matching two yeah so why are we only matching two yeah
    so why are we only matching two

    steps right what was asking why can''t we steps right what was asking why can''t
    we steps right what was asking why can''t we

    just directly match four steps right just directly match four steps right just
    directly match four steps right

    duh yeah why not and actually even duh yeah why not and actually even duh yeah
    why not and actually even

    better. Why can''t we just directly match better. Why can''t we just directly
    match better. Why can''t we just directly match

    t steps? Like why why why like dream t steps? Like why why why like dream t steps?
    Like why why why like dream

    bigger? If you''re dreaming already, why bigger? If you''re dreaming already,
    why bigger? If you''re dreaming already, why

    not dream bigger? Just like directly go not dream bigger? Just like directly go
    not dream bigger? Just like directly go

    to the end. You shouldn''t even jump four to the end. You shouldn''t even jump
    four to the end. You shouldn''t even jump four

    steps. Why are you jumping four steps steps. Why are you jumping four steps steps.
    Why are you jumping four steps

    only? Right. Um what could be a problem only? Right. Um what could be a problem
    only? Right. Um what could be a problem

    here? What could be a problem? here? What could be a problem? here? What could
    be a problem?

    >> Resolution. You just jump that far that >> Resolution. You just jump that far
    that >> Resolution. You just jump that far that

    fast. Maybe it just wouldn''t be as good fast. Maybe it just wouldn''t be as good
    fast. Maybe it just wouldn''t be as good

    of a model. of a model. of a model.

    >> Oh, why wouldn''t it be a good model? I'
  concept_slugs:
  - consistency-models
  - rectified-flow
  - v-prediction
- idx: 7
  start_sec: 359.67
  end_sec: 404.319
  text: '>> Oh, why wouldn''t it be a good model? I >> Oh, why wouldn''t it be a good
    model? I

    guess guess guess

    Marco, Marco, Marco,

    >> you still have to learn the same amount >> you still have to learn the same
    amount >> you still have to learn the same amount

    of jumps. You have to learn t steps from of jumps. You have to learn t steps from
    of jumps. You have to learn t steps from

    every tu every tu every tu

    >> that''s that that''s that''s one of the >> that''s that that''s that''s one
    of the >> that''s that that''s that''s one of the

    problem. Yep. problem. Yep. problem. Yep.

    >> Fail on our distribution. >> Fail on our distribution. >> Fail on our distribution.

    >> You may distribution >> You may distribution >> You may distribution

    >> everything in distribution here, right? >> everything in distribution here,
    right? >> everything in distribution here, right?

    >> We ask it something uh different. Oh, we >> We ask it something uh different.
    Oh, we >> We ask it something uh different. Oh, we

    are not doing conditional. are not doing conditional. are not doing conditional.

    >> No. >> No. >> No.

    >> Yeah. This is this is a new model >> Yeah. This is this is a new model >> Yeah.
    This is this is a new model

    completely, right? completely, right? completely, right?

    I I don''t know if it''s about to come in I I don''t know if it''s about to come
    in I I don''t know if it''s about to come in

    but if even in the two step or the four but if even in the two step or the four
    but if even in the two step or the four

    step or the full step if the final step or the full step if the final step or
    the full step if the final

    distribution is very complex distribution is very complex distribution is very
    complex

    >> and the original is always Gaussian. So >> and the original is always Gaussian.
    So >> and the original is always Gaussian. So

    if it''s then it''s just the neural if it''s then it''s just the neural if it''s
    then it''s just the neural

    network''s job to just take this teeny network''s job to just take this teeny'
  concept_slugs:
  - consistency-models
  - rectified-flow
- idx: 8
  start_sec: 404.319
  end_sec: 443.199
  text: 'network''s job to just take this teeny

    tiny Gaussian to that complex version tiny Gaussian to that complex version tiny
    Gaussian to that complex version

    without getting enough. So it''s very without getting enough. So it''s very without
    getting enough. So it''s very

    difficult essentially right I guess difficult essentially right I guess difficult
    essentially right I guess

    that''s the that''s the well I guess but that''s the that''s the well I guess
    but that''s the that''s the well I guess but

    yeah yeah yeah go ahead yeah yeah yeah go ahead yeah yeah yeah go ahead

    >> the output diversity would be limited >> the output diversity would be limited
    >> the output diversity would be limited

    because you''re just taking one because you''re just taking one because you''re
    just taking one

    >> without any steps >> without any steps >> without any steps

    >> well that''s definitely issue uh and >> well that''s definitely issue uh and
    >> well that''s definitely issue uh and

    that''s actually still an issue today um that''s actually still an issue today
    um that''s actually still an issue today um

    but it''s not going to get solved by any but it''s not going to get solved by
    any but it''s not going to get solved by any

    of the method that we''re going to talk of the method that we''re going to talk
    of the method that we''re going to talk

    about but that''s a great great problem about but that''s a great great problem
    about but that''s a great great problem

    this is the issue this is the issue this is the issue

    >> uh no no fine details because you''re >> uh no no fine details because you''re
    >> uh no no fine details because you''re

    kind of just like jumping to a point kind of just like jumping to a point kind
    of just like jumping to a point

    that''s why but you can reduce the error that''s why but you can reduce the error
    that''s why but you can reduce the error

    so much. so much. so much.

    >> Yeah. the quality may be great but like >> Yeah. the quality may be great but
    like >> Yeah. the quality may be great but like

    what about like the feasibility of what about like the feasibility of'
  concept_slugs:
  - consistency-models
  - rectified-flow
- idx: 9
  start_sec: 443.199
  end_sec: 497.84
  text: 'what about like the feasibility of

    training this kind of model like how training this kind of model like how training
    this kind of model like how

    about let''s just look at uh training a about let''s just look at uh training
    a about let''s just look at uh training a

    student model is four steps like what student model is four steps like what student
    model is four steps like what

    may be a problem here like in terms of may be a problem here like in terms of
    may be a problem here like in terms of

    feasibility like is this like actually feasibility like is this like actually
    feasibility like is this like actually

    feasible to train >> sampling take too long during training >> sampling take too
    long during training

    Yeah, right. Yeah, right. Yeah, right.

    >> You need to take four poor f for that >> You need to take four poor f for that
    >> You need to take four poor f for that

    four four passes at training time like four four passes at training time like
    four four passes at training time like

    so basically like in order to train to so basically like in order to train to
    so basically like in order to train to

    take one training step you need to first take one training step you need to first
    take one training step you need to first

    sample like take sampling step four sample like take sampling step four sample
    like take sampling step four

    times and then to and and then you can times and then to and and then you can
    times and then to and and then you can

    do the back propagation right so that''s do the back propagation right so that''s
    do the back propagation right so that''s

    like just like very very expensive even like just like very very expensive even
    like just like very very expensive even

    if you''re not back propping through your if you''re not back propping through
    your if you''re not back propping through your

    original diffusion model it''s just going original diffusion model it''s just
    going original diffusion model it''s just going

    to take a very long time and it''s like to take a very long time and it''s like'
  concept_slugs:
  - consistency-models
  - rectified-flow
- idx: 10
  start_sec: 497.84
  end_sec: 534.32
  text: 'to take a very long time and it''s like

    if you try to scale it up to t time if you try to scale it up to t time if you
    try to scale it up to t time

    steps, right? Uh let me finish maybe. Um steps, right? Uh let me finish maybe.
    Um steps, right? Uh let me finish maybe. Um

    so like so first of all like basically so like so first of all like basically
    so like so first of all like basically

    you''ll need to take t4 passes at each you''ll need to take t4 passes at each
    you''ll need to take t4 passes at each

    time steps. So this t it can be very time steps. So this t it can be very time
    steps. So this t it can be very

    large or can be very small and the most large or can be very small and the most
    large or can be very small and the most

    importantly is like it''s going to be importantly is like it''s going to be importantly
    is like it''s going to be

    very expensive if t is very large and very expensive if t is very large and very
    expensive if t is very large and

    also it''s going to be very hard to also it''s going to be very hard to also it''s
    going to be very hard to

    paralyze just like what Marco said, paralyze just like what Marco said, paralyze
    just like what Marco said,

    right? Like basically you like in the right? Like basically you like in the right?
    Like basically you like in the

    same batch they could be different keys same batch they could be different keys
    same batch they could be different keys

    like how how are you gonna like what are like how how are you gonna like what
    are like how how are you gonna like what are

    you going to do then you need to write a you going to do then you need to write
    a you going to do then you need to write a

    for loop over your batches and like this for loop over your batches and like this
    for loop over your batches and like this

    sounds kind of not great. Yeah hold on. sounds kind of not great. Yeah hold on.'
  concept_slugs:
  - consistency-models
  - rectified-flow
- idx: 11
  start_sec: 534.32
  end_sec: 571.12
  text: 'sounds kind of not great. Yeah hold on.

    Yeah, Yeah, Yeah,

    >> I think the four power could only be for >> I think the four power could only
    be for >> I think the four power could only be for

    the teacher model, right? Because the the teacher model, right? Because the the
    teacher model, right? Because the

    student model is likely going to teach. student model is likely going to teach.
    student model is likely going to teach.

    >> Yeah, but like think about it like the >> Yeah, but like think about it like
    the >> Yeah, but like think about it like the

    teacher model could be something that is teacher model could be something that
    is teacher model could be something that is

    like larger, right? And like like I mean like larger, right? And like like I mean
    like larger, right? And like like I mean

    you could still do four steps. That''s you could still do four steps. That''s
    you could still do four steps. That''s

    fine. But like this this kind of like I fine. But like this this kind of like
    I fine. But like this this kind of like I

    guess this kind of algorithm doesn''t guess this kind of algorithm doesn''t guess
    this kind of algorithm doesn''t

    really scale beyond like say you do four really scale beyond like say you do four
    really scale beyond like say you do four

    times. Oh, you could also do eight, you times. Oh, you could also do eight, you
    times. Oh, you could also do eight, you

    can also 16, right? then it just get can also 16, right? then it just get can
    also 16, right? then it just get

    like really really large the the number like really really large the the number
    like really really large the the number

    of like the the the amount of time that of like the the the amount of time that
    of like the the the amount of time that

    you need to spend on sampling during you need to spend on sampling during you
    need to spend on sampling during

    your training and then your training your training and then your training your
    training and then your training

    just going to become very slow. just going to become very slow.'
  concept_slugs:
  - consistency-models
  - rectified-flow
- idx: 12
  start_sec: 571.12
  end_sec: 618.72
  text: 'just going to become very slow.

    So, so do you think that like five total So, so do you think that like five total
    So, so do you think that like five total

    four of the teacher student four of the teacher student four of the teacher student

    >> uh >> uh >> uh

    are you saying that is there a sweet are you saying that is there a sweet are
    you saying that is there a sweet

    spot basically is that what you''re spot basically is that what you''re spot basically
    is that what you''re

    trying to say or trying to say or trying to say or

    >> methodologically here uh there are four >> methodologically here uh there are
    four >> methodologically here uh there are four

    forward passes for each time step model. forward passes for each time step model.
    forward passes for each time step model.

    >> Yeah. And would you say there''s another >> Yeah. And would you say there''s
    another >> Yeah. And would you say there''s another

    one for the for the student model and one for the for the student model and one
    for the for the student model and

    then you calculate the diver then you calculate the diver then you calculate the
    diver

    >> divergence >> divergence >> divergence

    >> for the student model for the >> for the student model for the >> for the student
    model for the

    >> why calculating the divergence >> why calculating the divergence >> why calculating
    the divergence

    >> the loss >> the loss >> the loss

    >> oh the loss okay I see >> oh the loss okay I see >> oh the loss okay I see

    >> any loss >> any loss >> any loss

    >> okay okay uh so I''m not sure what if I >> okay okay uh so I''m not sure what
    if I >> okay okay uh so I''m not sure what if I

    follow so you take four uh student uh follow so you take four uh student uh follow
    so you take four uh student uh

    you take four teacher steps so basically you take four teacher steps so basically
    you take four teacher steps so basically

    just like describing what we''re doing just like describing what we''re doing
    just like describing what we''re doing

    here here'
  concept_slugs:
  - consistency-models
  - rectified-flow
- idx: 13
  start_sec: 618.72
  end_sec: 662.47
  text: 'here

    >> um and what was the question >> um and what was the question >> um and what
    was the question

    step. step. step.

    >> Yeah. >> Yeah.

    >> You said you require like four forward >> You said you require like four forward
    >> You said you require like four forward

    passes. passes. passes.

    >> Oh, the teacher model. >> Oh, the teacher model. >> Oh, the teacher model.

    >> The teacher model. >> The teacher model. >> The teacher model.

    >> Yeah. >> Yeah.

    >> And one for the student model, right? >> And one for the student model, right?
    >> And one for the student model, right?

    >> And one for the student model too. And >> And one for the student model too.
    And >> And one for the student model too. And

    you backward only through the student you backward only through the student you
    backward only through the student

    model. But even that the four four model. But even that the four four model. But
    even that the four four

    passes of the teacher. This taking how passes of the teacher. This taking how
    passes of the teacher. This taking how

    many steps here doesn''t scale, right? many steps here doesn''t scale, right?
    many steps here doesn''t scale, right?

    because like other like the time they because like other like the time they because
    like other like the time they

    require for each training step will require for each training step will require
    for each training step will

    scale linearly depending on how many scale linearly depending on how many scale
    linearly depending on how many

    steps you are going to take there. So steps you are going to take there. So steps
    you are going to take there. So

    that''s what I meant by it doesn''t scale. that''s what I meant by it doesn''t
    scale. that''s what I meant by it doesn''t scale.

    >> Okay. Yeah. >> Okay. Yeah. >> Okay. Yeah.

    >> How do you like create this data set >> How do you like create this data set
    >> How do you like create this data set

    offline and then just offline and then just offline and then just

    >> well you have a data set offline right? >> well you have a data set offline
    right? >> well you have a data set offline right?

    That''s your forward pass.'
  concept_slugs:
  - consistency-models
  - rectified-flow
- idx: 14
  start_sec: 662.47
  end_sec: 697.279
  text: 'That''s your forward pass. That''s your forward pass.

    >> Yeah but just create a new data set with >> Yeah but just create a new data
    set with >> Yeah but just create a new data set with

    this feature model. this feature model. this feature model.

    >> Uh I mean yeah yeah. So if you can you >> Uh I mean yeah yeah. So if you can
    you >> Uh I mean yeah yeah. So if you can you

    can like Yeah. Yeah. I mean that that can like Yeah. Yeah. I mean that that can
    like Yeah. Yeah. I mean that that

    could work. That could work. Um, yeah, could work. That could work. Um, yeah,
    could work. That could work. Um, yeah,

    that could definitely work for sure. But that could definitely work for sure.
    But that could definitely work for sure. But

    we actually have a smart like a like a we actually have a smart like a like a
    we actually have a smart like a like a

    like a like a Yeah, like a more like a like a Yeah, like a more like a like a
    Yeah, like a more

    paralyzable way to do it. Yeah, but that paralyzable way to do it. Yeah, but that
    paralyzable way to do it. Yeah, but that

    that''s very expens Well, you just kind that''s very expens Well, you just kind
    that''s very expens Well, you just kind

    of trade a training time with storage. I of trade a training time with storage.
    I of trade a training time with storage. I

    guess that''s like a like a different guess that''s like a like a different guess
    that''s like a like a different

    trade-off that we''re looking at here. Or trade-off that we''re looking at here.
    Or trade-off that we''re looking at here. Or

    Oh, yeah. Yeah. Yeah. Yeah. Yeah. That Oh, yeah. Yeah. Yeah. Yeah. Yeah. That
    Oh, yeah. Yeah. Yeah. Yeah. Yeah. That

    that''s a good good thinking though. that''s a good good thinking though. that''s
    a good good thinking though.

    Thinking out of the box here. Okay. But Thinking out of the box here. Okay. But
    Thinking out of the box here. Okay. But

    yeah. Um, so what do we think? Is it yeah. Um, so what do we think? Is it'
  concept_slugs:
  - consistency-models
  - rectified-flow
- idx: 15
  start_sec: 697.279
  end_sec: 750.639
  text: 'yeah. Um, so what do we think? Is it

    possible to train a model that goes from possible to train a model that goes from
    possible to train a model that goes from

    t directly xt directly to x0? What do we t directly xt directly to x0? What do
    we t directly xt directly to x0? What do we

    think? I clearly it''s possible. So like what I clearly it''s possible. So like
    what

    well I''m not I guess it''s not so clear well I''m not I guess it''s not so clear
    well I''m not I guess it''s not so clear

    at this point but it is possible. What at this point but it is possible. What
    at this point but it is possible. What

    do we think? Any idea maybe question question

    >> just to understand how would the loss >> just to understand how would the loss
    >> just to understand how would the loss

    look like in this case? What are we so look like in this case? What are we so
    look like in this case? What are we so

    when we''re doing this feature student? when we''re doing this feature student?
    when we''re doing this feature student?

    >> Yeah. Right. So the loss function is >> Yeah. Right. So the loss function is
    >> Yeah. Right. So the loss function is

    going to be very very very ugly. Right. going to be very very very ugly. Right.
    going to be very very very ugly. Right.

    So it''s just going to be uh predicting So it''s just going to be uh predicting
    So it''s just going to be uh predicting

    from so fxt t to zero and then you''re from so fxt t to zero and then you''re
    from so fxt t to zero and then you''re

    going to be matching like a chain of going to be matching like a chain of going
    to be matching like a chain of

    four passes of the of the teacher right four passes of the of the teacher right
    four passes of the of the teacher right

    so that just like not it''s just not good so that just like not it''s just not
    good so that just like not it''s just not good

    right even even if you stop red over right even even if you stop red over'
  concept_slugs:
  - consistency-models
  - rectified-flow
- idx: 16
  start_sec: 750.639
  end_sec: 795.92
  text: 'right even even if you stop red over

    there it''s not good right okay so anyway there it''s not good right okay so anyway
    there it''s not good right okay so anyway

    let''s take a look at this uh problem let''s take a look at this uh problem let''s
    take a look at this uh problem

    from like a different angle so the new from like a different angle so the new
    from like a different angle so the new

    model that we''re trying to learn here model that we''re trying to learn here
    model that we''re trying to learn here

    besides like you can uh jump essentially besides like you can uh jump essentially
    besides like you can uh jump essentially

    right from xt to x0 you should be right from xt to x0 you should be right from
    xt to x0 you should be

    because this t is arbitrary so you''re because this t is arbitrary so you''re
    because this t is arbitrary so you''re

    also also also

    going to be able to jump from like any going to be able to jump from like any
    going to be able to jump from like any

    other t essentially to x0 zero right so other t essentially to x0 zero right so
    other t essentially to x0 zero right so

    essentially this is the model we''re essentially this is the model we''re essentially
    this is the model we''re

    looking at so it''s not really it''s not looking at so it''s not really it''s
    not looking at so it''s not really it''s not

    completely related to the like it completely related to the like it completely
    related to the like it

    doesn''t really matter what kind of t doesn''t really matter what kind of t doesn''t
    really matter what kind of t

    we''re we''re getting here so like what we we''re we''re getting here so like
    what we we''re we''re getting here so like what we

    really want here is a new model that is really want here is a new model that is
    really want here is a new model that is

    what we call self-con consistent. Um what we call self-con consistent. Um what
    we call self-con consistent. Um

    yeah, what does it mean is that yeah, what does it mean is that'
  concept_slugs:
  - consistency-models
  - rectified-flow
- idx: 17
  start_sec: 795.92
  end_sec: 866.399
  text: 'yeah, what does it mean is that

    basically for any two points like any basically for any two points like any basically
    for any two points like any

    arbitrary two points on the same OD arbitrary two points on the same OD arbitrary
    two points on the same OD

    trajectory um that is provided by the trajectory um that is provided by the trajectory
    um that is provided by the

    pre-trained diffusion model here. Um so pre-trained diffusion model here. Um so
    pre-trained diffusion model here. Um so

    the new model should predict the same the new model should predict the same the
    new model should predict the same

    clean data output. So as long as they''re clean data output. So as long as they''re
    clean data output. So as long as they''re

    on the same sampling trajectory of your on the same sampling trajectory of your
    on the same sampling trajectory of your

    original model, your new model should original model, your new model should original
    model, your new model should

    predict the same x0 at the end. Um so in predict the same x0 at the end. Um so
    in predict the same x0 at the end. Um so in

    math it look like the prediction from XT math it look like the prediction from
    XT math it look like the prediction from XT

    t is equivalent the prediction of uh t is equivalent the prediction of uh t is
    equivalent the prediction of uh

    from from time s essentially. from from time s essentially. from from time s essentially.

    Okay, any question? I feel like there Okay, any question? I feel like there Okay,
    any question? I feel like there

    should be some question here, right? Is should be some question here, right? Is
    should be some question here, right? Is

    this like sufficient for example? >> Oh, yeah. Yeah. Yeah. Yeah. We haven''t >>
    Oh, yeah. Yeah. Yeah. Yeah. We haven''t

    get there yet. Yeah. Yeah. That''s but get there yet. Yeah. Yeah. That''s but
    get there yet. Yeah. Yeah. That''s but

    that''s a great question too. Um but like that''s a great question too. Um but
    like that''s a great question too. Um but like

    is this the only criteria that we need is this the only criteria that we need'
  concept_slugs:
  - consistency-models
  - rectified-flow
- idx: 18
  start_sec: 866.399
  end_sec: 913.44
  text: 'is this the only criteria that we need

    for this new model to generate something for this new model to generate something
    for this new model to generate something

    to to generate the correct thing? to to generate the correct thing? to to generate
    the correct thing?

    What do we think or other questions? >> Yeah.

    >> Does sample diversity come from for this >> Does sample diversity come from
    for this >> Does sample diversity come from for this

    one? Because then if all the steps in one? Because then if all the steps in one?
    Because then if all the steps in

    between you''re trying to make them all between you''re trying to make them all
    between you''re trying to make them all

    the same at the end. the same at the end. the same at the end.

    >> Okay. So what does sample diversity come >> Okay. So what does sample diversity
    come >> Okay. So what does sample diversity come

    from? Not not even diversity. I feel from? Not not even diversity. I feel from?
    Not not even diversity. I feel

    diversity is like a higher level diversity is like a higher level diversity is
    like a higher level

    question. Yeah. But yeah, what is that? question. Yeah. But yeah, what is that?
    question. Yeah. But yeah, what is that?

    >> Like this is no influence on the >> Like this is no influence on the >> Like
    this is no influence on the

    teacher. teacher. teacher.

    >> Yeah. Right. Like like well there''s no >> Yeah. Right. Like like well there''s
    no >> Yeah. Right. Like like well there''s no

    influence. Well there is some influence influence. Well there is some influence
    influence. Well there is some influence

    on the teacher because you need to come on the teacher because you need to come
    on the teacher because you need to come

    from the same OD from the teacher but from the same OD from the teacher but from
    the same OD from the teacher but

    essentially I get I think you guys are essentially I get I think you guys are
    essentially I get I think you guys are

    getting there. Essentially getting there. Essentially getting there. Essentially

    like there it says nothing about the like there it says nothing about the'
  concept_slugs:
  - consistency-models
  - rectified-flow
- idx: 19
  start_sec: 913.44
  end_sec: 963.43
  text: 'like there it says nothing about the

    output, right? Like we have no guarantee output, right? Like we have no guarantee
    output, right? Like we have no guarantee

    about what the output should look like about what the output should look like
    about what the output should look like

    here. like the we we''re only talking here. like the we we''re only talking here.
    like the we we''re only talking

    about how like we should be consistent about how like we should be consistent
    about how like we should be consistent

    within ourselves but like it could be within ourselves but like it could be within
    ourselves but like it could be

    very consistent and generate something very consistent and generate something
    very consistent and generate something

    that is completely garbage right so um that is completely garbage right so um
    that is completely garbage right so um

    what what we can do here is like very what what we can do here is like very what
    what we can do here is like very

    curiously curiously curiously

    when t is very close to zero this new when t is very close to zero this new when
    t is very close to zero this new

    model should be directly predicting the model should be directly predicting the
    model should be directly predicting the

    input so it should just like input so it should just like input so it should just
    like

    be a identity function right so be a identity function right so be a identity
    function right so

    basically we''re saying that like oh if basically we''re saying that like oh if
    basically we''re saying that like oh if

    you''re like essentially if you''re close you''re like essentially if you''re
    close you''re like essentially if you''re close

    enough to zero you''re just predicting enough to zero you''re just predicting
    enough to zero you''re just predicting

    whatever it is in the input and this is whatever it is in the input and this is
    whatever it is in the input and this is

    going to help us to basically uh so this going to help us to basically uh so this
    going to help us to basically uh so this

    thing is what we call a boundary thing is what we call a boundary thing is what
    we call a boundary

    condition essentially so this is the'
  concept_slugs:
  - consistency-models
  - rectified-flow
- idx: 20
  start_sec: 963.43
  end_sec: 1008.55
  text: 'condition essentially so this is the condition essentially so this is the

    thing that''s going to like basically thing that''s going to like basically thing
    that''s going to like basically

    just like make sure that everything is just like make sure that everything is
    just like make sure that everything is

    like valid essentially okay so boundary like valid essentially okay so boundary
    like valid essentially okay so boundary

    condition is just saying that when x or condition is just saying that when x or
    condition is just saying that when x or

    sorry when t is close to zero or when t sorry when t is close to zero or when
    t sorry when t is close to zero or when t

    is zero exactly you should just output is zero exactly you should just output
    is zero exactly you should just output

    put the input put the input put the input

    um yeah so in practice we do not take um yeah so in practice we do not take um
    yeah so in practice we do not take

    zero directly this this is not zero sorry this is this this is not zero sorry
    this is

    delta we we do not take zero directly delta we we do not take zero directly delta
    we we do not take zero directly

    because of the problem that you guys because of the problem that you guys because
    of the problem that you guys

    have encountered in the homework too so have encountered in the homework too so
    have encountered in the homework too so

    like it has the same problem as like it has the same problem as like it has the
    same problem as

    singularity right because you''re trying singularity right because you''re trying
    singularity right because you''re trying

    to match everything to the to like one to match everything to the to like one
    to match everything to the to like one

    point so you have the singularity point so you have the singularity point so you
    have the singularity

    problem uh the singularity problem is I problem uh the singularity problem is
    I problem uh the singularity problem is I

    think it''s like homework two question 2 think it''s like homework two question
    2 think it''s like homework two question 2

    B or something. It''s like the when when'
  concept_slugs:
  - consistency-models
  - rectified-flow
- idx: 21
  start_sec: 1008.55
  end_sec: 1062.799
  text: 'B or something. It''s like the when when B or something. It''s like the when
    when

    your gradient of the the loss spikes up. your gradient of the the loss spikes
    up. your gradient of the the loss spikes up.

    Um but anyway, um yeah, so you you can Um but anyway, um yeah, so you you can
    Um but anyway, um yeah, so you you can

    just take a small enough number that is just take a small enough number that is
    just take a small enough number that is

    very close to zero. very close to zero. very close to zero.

    Okay, any question? Okay, any question? Okay, any question?

    If not, we now have consistency model. If not, we now have consistency model.
    If not, we now have consistency model.

    Okay. So, consistency model is uh like Okay. So, consistency model is uh like
    Okay. So, consistency model is uh like

    pretty much like the first um one-step pretty much like the first um one-step
    pretty much like the first um one-step

    generation model that got like generation model that got like generation model
    that got like

    mainstream well when I say mainstream mainstream well when I say mainstream mainstream
    well when I say mainstream

    it''s mainstream in the diffusion it''s mainstream in the diffusion it''s mainstream
    in the diffusion

    community okay mainstream success uh community okay mainstream success uh community
    okay mainstream success uh

    like from like a like and get a lot of like from like a like and get a lot of
    like from like a like and get a lot of

    attention from people and this um model attention from people and this um model
    attention from people and this um model

    is developed by the same person who is developed by the same person who is developed
    by the same person who

    developed the whole like scorebased SDE developed the whole like scorebased SDE
    developed the whole like scorebased SDE

    model stuff. Um, Yangsung the guy and model stuff. Um, Yangsung the guy and model
    stuff. Um, Yangsung the guy and

    then he is when he developed then he is when he developed then he is when he developed

    consistency model he was at open eye and consistency model he was at open eye
    and'
  concept_slugs:
  - consistency-models
  - rectified-flow
- idx: 22
  start_sec: 1062.799
  end_sec: 1106.87
  text: 'consistency model he was at open eye and

    then now he''s apparently some big name then now he''s apparently some big name
    then now he''s apparently some big name

    in meta super intelligence lab or in meta super intelligence lab or in meta super
    intelligence lab or

    something but anyway yeah so this is something but anyway yeah so this is something
    but anyway yeah so this is

    what like if you do good research you what like if you do good research you what
    like if you do good research you

    get money basically anyway um but yeah get money basically anyway um but yeah
    get money basically anyway um but yeah

    any questions about consistency model any questions about consistency model any
    questions about consistency model

    >> so the problem we were discussing of >> so the problem we were discussing of
    >> so the problem we were discussing of

    doing having that four forward process doing having that four forward process
    doing having that four forward process

    or something or something or something

    Oh, that still haven''t yet solved Oh, that still haven''t yet solved Oh, that
    still haven''t yet solved

    actually. Yes. Yes. Okay. Let''s just actually. Yes. Yes. Okay. Let''s just actually.
    Yes. Yes. Okay. Let''s just

    solve it now, I guess. solve it now, I guess. solve it now, I guess.

    >> So, the original progressive >> So, the original progressive >> So, the original
    progressive

    distillation paper that suffered from distillation paper that suffered from distillation
    paper that suffered from

    the problem. They had to do four four the problem. They had to do four four the
    problem. They had to do four four

    passes per training. passes per training. passes per training.

    >> Um, no. So, the cons progressive >> Um, no. So, the cons progressive >> Um,
    no. So, the cons progressive

    distillation only do two forward passes. distillation only do two forward passes.
    distillation only do two forward passes.

    They only jump two steps. Oh, by the They only jump two steps. Oh, by the They
    only jump two steps. Oh, by the

    way, progressive dissolation is way, progressive dissolation is way, progressive
    dissolation is

    developed by the same guy who developed developed by the same guy who developed
    developed by the same guy who developed

    DDPM. Yeah. Yeah. So, that guy is also a'
  concept_slugs:
  - consistency-models
  - ddpm
  - rectified-flow
- idx: 23
  start_sec: 1106.87
  end_sec: 1155.76
  text: 'DDPM. Yeah. Yeah. So, that guy is also a DDPM. Yeah. Yeah. So, that guy is
    also a

    genius and he''s now has his own startup. genius and he''s now has his own startup.
    genius and he''s now has his own startup.

    So, you can get rich if you get if you So, you can get rich if you get if you
    So, you can get rich if you get if you

    do research. Anyway um but yeah that do research. Anyway um but yeah that do research.
    Anyway um but yeah that

    that project I that paper I believe is that project I that paper I believe is
    that project I that paper I believe is

    the first dissolation paper on diffusion the first dissolation paper on diffusion
    the first dissolation paper on diffusion

    anyway um yeah so we haven''t really anyway um yeah so we haven''t really anyway
    um yeah so we haven''t really

    solved the problem actually right so solved the problem actually right so solved
    the problem actually right so

    like essentially like essentially like essentially

    like how exactly do you get like you like how exactly do you get like you like
    how exactly do you get like you

    know two different data points on the know two different data points on the know
    two different data points on the

    same OD trajectory without having a same OD trajectory without having a same OD
    trajectory without having a

    cached offline data set essentially cached offline data set essentially cached
    offline data set essentially

    right so if we look at this Right, we right so if we look at this Right, we right
    so if we look at this Right, we

    will see basically the red like the red will see basically the red like the red
    will see basically the red like the red

    ones are the ones that correspond to ones are the ones that correspond to ones
    are the ones that correspond to

    more than one forward passes of uh more than one forward passes of uh more than
    one forward passes of uh

    training time from XT and then the only training time from XT and then the only
    training time from XT and then the only

    green one which is like only one step green one which is like only one step'
  concept_slugs:
  - consistency-models
  - ddpm
  - rectified-flow
- idx: 24
  start_sec: 1155.76
  end_sec: 1201.919
  text: 'green one which is like only one step

    away is the one that we''re going to use away is the one that we''re going to
    use away is the one that we''re going to use

    here. So essentially basically what''s here. So essentially basically what''s
    here. So essentially basically what''s

    happening here is that like let''s just happening here is that like let''s just
    happening here is that like let''s just

    say we have a pre-train model and we say we have a pre-train model and we say
    we have a pre-train model and we

    randomly sample a time t and then randomly sample a time t and then randomly sample
    a time t and then

    essentially um from xt we are going to essentially um from xt we are going to
    essentially um from xt we are going to

    solve like one step with the teacher solve like one step with the teacher solve
    like one step with the teacher

    with some solver. So this solver can be with some solver. So this solver can be
    with some solver. So this solver can be

    anything. It can be oiler. It can be anything. It can be oiler. It can be anything.
    It can be oiler. It can be

    like uh whatever midpoint. It can be a like uh whatever midpoint. It can be a
    like uh whatever midpoint. It can be a

    hume. Whatever you want basically. So we hume. Whatever you want basically. So
    we hume. Whatever you want basically. So we

    solve it uh with the solver of our solve it uh with the solver of our solve it
    uh with the solver of our

    choice so that it''s accurate. It stays choice so that it''s accurate. It stays
    choice so that it''s accurate. It stays

    on the same OD trajectory. Um and then on the same OD trajectory. Um and then
    on the same OD trajectory. Um and then

    we match the prediction from both XT we match the prediction from both XT we match
    the prediction from both XT

    which is our input and the the the the which is our input and the the the the
    which is our input and the the the the

    next time step that is getting on the next time step that is getting on the'
  concept_slugs:
  - consistency-models
  - rectified-flow
- idx: 25
  start_sec: 1201.919
  end_sec: 1247.52
  text: 'next time step that is getting on the

    same trajectory solved by our solver. same trajectory solved by our solver. same
    trajectory solved by our solver.

    and the original teacher model. So this and the original teacher model. So this
    and the original teacher model. So this

    becomes loss function becomes this and becomes loss function becomes this and
    becomes loss function becomes this and

    particularly the things that we don''t particularly the things that we don''t
    particularly the things that we don''t

    know yet is that the lambda is the loss know yet is that the lambda is the loss
    know yet is that the lambda is the loss

    waiting is the same thing as the EDM waiting is the same thing as the EDM waiting
    is the same thing as the EDM

    paper and then the uh the the D here is paper and then the uh the the D here is
    paper and then the uh the the D here is

    a distance. Um so essentially in this a distance. Um so essentially in this a
    distance. Um so essentially in this

    paper they also talk about how maybe L2 paper they also talk about how maybe L2
    paper they also talk about how maybe L2

    is not really the best distance that you is not really the best distance that
    you is not really the best distance that you

    should be optimizing for. Uh you know it should be optimizing for. Uh you know
    it should be optimizing for. Uh you know it

    could be like perceptual distance for could be like perceptual distance for could
    be like perceptual distance for

    example something called L pips. So it''s example something called L pips. So
    it''s example something called L pips. So it''s

    like a distance between like the like a distance between like the like a distance
    between like the

    perceptual features from like some perceptual features from like some perceptual
    features from like some

    pre-trained CNN essentially. Um so yeah pre-trained CNN essentially. Um so yeah
    pre-trained CNN essentially. Um so yeah

    so you can use diff different uh so you can use diff different uh so you can use
    diff different uh

    distance. Obviously this theory is going distance. Obviously this theory is going
    distance. Obviously this theory is going

    just going to become a little bit just going to become a little bit'
  concept_slugs:
  - consistency-models
  - rectified-flow
- idx: 26
  start_sec: 1247.52
  end_sec: 1301.99
  text: 'just going to become a little bit

    messier if you if you do not use L2 but messier if you if you do not use L2 but
    messier if you if you do not use L2 but

    in practice in practice in practice

    uh perceptual distance uh looks um gives uh perceptual distance uh looks um gives
    uh perceptual distance uh looks um gives

    you the better result here. And here we you the better result here. And here we
    you the better result here. And here we

    also have a stock graph. So this also have a stock graph. So this also have a
    stock graph. So this

    basically this is just saying that we basically this is just saying that we basically
    this is just saying that we

    are only optimizing the jumping the like are only optimizing the jumping the like
    are only optimizing the jumping the like

    the the larger jump sorry the larger the the larger jump sorry the larger the
    the larger jump sorry the larger

    jump here. So the ones that jump here. So the ones that jump here. So the ones
    that

    everything that involves with the everything that involves with the everything
    that involves with the

    teacher we just we do not take gradient teacher we just we do not take gradient
    teacher we just we do not take gradient

    from that input. from that input. from that input.

    Okay. Any question? Okay. Any question? Okay. Any question?

    >> Yes. >> Yes. >> Yes.

    >> Do we really need a pre-trained >> Do we really need a pre-trained >> Do we
    really need a pre-trained

    diffusion model to train? diffusion model to train? diffusion model to train?

    >> Yeah yeah yeah. That''s a great question. >> Yeah yeah yeah. That''s a great
    question. >> Yeah yeah yeah. That''s a great question.

    We''re going to answer it later. Yes. Um, We''re going to answer it later. Yes.
    Um, We''re going to answer it later. Yes. Um,

    great question. great question. great question.

    Any other question? Any other question? Any other question?

    >> Yeah. >> Yeah.

    >> So, the target is like the final x0 or >> So, the target is like the final
    x0 or >> So, the target is like the final x0 or

    is it like x is it like x is it like x

    plus delta t?'
  concept_slugs:
  - consistency-models
  - rectified-flow
- idx: 27
  start_sec: 1301.99
  end_sec: 1344.4
  text: 'plus delta t? plus delta t?

    >> Ah, that''s also another great question. >> Ah, that''s also another great
    question. >> Ah, that''s also another great question.

    So, uh here everything so this f theta So, uh here everything so this f theta
    So, uh here everything so this f theta

    here is predicting always x0. Yeah. here is predicting always x0. Yeah. here is
    predicting always x0. Yeah.

    Yeah. But later this question is going Yeah. But later this question is going
    Yeah. But later this question is going

    to become very relevant later on. Yeah, to become very relevant later on. Yeah,
    to become very relevant later on. Yeah,

    >> you would still have to do multiple >> you would still have to do multiple
    >> you would still have to do multiple

    forward passes through the teacher forward passes through the teacher forward
    passes through the teacher

    model. model. model.

    >> No, like the the solver can take you >> No, like the the solver can take you
    >> No, like the the solver can take you

    like you only need to do one step of like you only need to do one step of like
    you only need to do one step of

    solver, right? So depending on which solver, right? So depending on which solver,
    right? So depending on which

    kind of solver that you take. If you kind of solver that you take. If you kind
    of solver that you take. If you

    take oiler for example, that''s only one take oiler for example, that''s only
    one take oiler for example, that''s only one

    for pass. If it''s second order oil or for pass. If it''s second order oil or
    for pass. If it''s second order oil or

    solver, then it''s two forward passes, solver, then it''s two forward passes,
    solver, then it''s two forward passes,

    right? So it''s every always like pretty right? So it''s every always like pretty
    right? So it''s every always like pretty

    manageable. It doesn''t scale that the manageable. It doesn''t scale that the
    manageable. It doesn''t scale that the

    the key point is the number of steps the key point is the number of steps the
    key point is the number of steps

    that you need to take from the t-shirt that you need to take from the t-shirt'
  concept_slugs:
  - consistency-models
  - rectified-flow
- idx: 28
  start_sec: 1344.4
  end_sec: 1393.11
  text: 'that you need to take from the t-shirt

    doesn''t scale with t. Yeah. Uh, okay. Do doesn''t scale with t. Yeah. Uh, okay.
    Do doesn''t scale with t. Yeah. Uh, okay. Do

    you want your first you want your first you want your first

    >> here? We only enforce that condition, >> here? We only enforce that condition,
    >> here? We only enforce that condition,

    right? We still don''t have the boundary right? We still don''t have the boundary
    right? We still don''t have the boundary

    condition. condition. condition.

    >> Uh, boundary next. Boundary next slide. >> Uh, boundary next. Boundary next
    slide. >> Uh, boundary next. Boundary next slide.

    Yeah. >> Can you just explain again how the stop >> Can you just explain again
    how the stop

    gra is working? gra is working? gra is working?

    >> Oh yeah. So stop gra is literally uh in >> Oh yeah. So stop gra is literally
    uh in >> Oh yeah. So stop gra is literally uh in

    PyTorch you just detach. Basically you PyTorch you just detach. Basically you
    PyTorch you just detach. Basically you

    just detach everything. Um so what it t just detach everything. Um so what it
    t just detach everything. Um so what it t

    what it does here is that basically you what it does here is that basically you
    what it does here is that basically you

    see how like we actually have two see how like we actually have two see how like
    we actually have two

    like we have one theta with the larger like we have one theta with the larger
    like we have one theta with the larger

    jump and one theta with the shorter jump and one theta with the shorter jump and
    one theta with the shorter

    jump. Um so the shorter jump is jumping jump. Um so the shorter jump is jumping
    jump. Um so the shorter jump is jumping

    from the point where you first take one from the point where you first take one
    from the point where you first take one

    step with teacher. Right? So basically step with teacher. Right? So basically
    step with teacher. Right? So basically

    we''re saying that we only take gradient we''re saying that we only take gradient
    we''re saying that we only take gradient

    with the larger jump. We do not update'
  concept_slugs:
  - consistency-models
  - rectified-flow
- idx: 29
  start_sec: 1393.11
  end_sec: 1471.279
  text: 'with the larger jump. We do not update with the larger jump. We do not update

    our model with the with the shorter our model with the with the shorter our model
    with the with the shorter

    jump. jump. jump.

    >> That''s it. That''s that that''s that''s >> That''s it. That''s that that''s
    that''s >> That''s it. That''s that that''s that''s

    really it. Yeah. really it. Yeah. really it. Yeah.

    >> And uh I I I''ll talk about why uh like >> And uh I I I''ll talk about why
    uh like >> And uh I I I''ll talk about why uh like

    Yeah. Like basically the the why we''re Yeah. Like basically the the why we''re
    Yeah. Like basically the the why we''re

    predicting essentially yeah predicting predicting essentially yeah predicting
    predicting essentially yeah predicting

    x0 is making a lot of sense in the x0 is making a lot of sense in the x0 is making
    a lot of sense in the

    distance sense as well but like we''re distance sense as well but like we''re
    distance sense as well but like we''re

    going to talk about later. Uh any other going to talk about later. Uh any other
    going to talk about later. Uh any other

    questions? Okay cool. Let''s answer the question of Okay cool. Let''s answer the
    question of

    so how do we satisfy boundary condition? so how do we satisfy boundary condition?
    so how do we satisfy boundary condition?

    Uh what do we think? There''s a very very Uh what do we think? There''s a very
    very Uh what do we think? There''s a very very

    simple answer to this nobody remember what EDM is. No, no, no. nobody remember
    what EDM is. No, no, no.

    No one really No one really No one really

    okay from EDM right we have the okay from EDM right we have the okay from EDM
    right we have the

    preconditioning preconditioning preconditioning

    um so this is the thing right this is um so this is the thing right this is um
    so this is the thing right this is

    the thing that kind of like the thing that kind of like the thing that kind of
    like

    parameterizes like that we''re we''re the parameterizes like that we''re we''re
    the parameterizes like that we''re we''re the

    parameterization that we''re using sort parameterization that we''re using sort'
  concept_slugs:
  - consistency-models
  - rectified-flow
- idx: 30
  start_sec: 1471.279
  end_sec: 1539.029
  text: 'parameterization that we''re using sort

    of and uh so we are trying to predict of and uh so we are trying to predict of
    and uh so we are trying to predict

    the clean data and um usually it the clean data and um usually it the clean data
    and um usually it

    consists of a skip connection weight a consists of a skip connection weight a
    consists of a skip connection weight a

    output uh the network output weight and output uh the network output weight and
    output uh the network output weight and

    the network output, right? So, if we''re the network output, right? So, if we''re
    the network output, right? So, if we''re

    using this particular uh you know using this particular uh you know using this
    particular uh you know

    preconditioning or like preconditioning or like preconditioning or like

    parameterization, parameterization, parameterization,

    what do we need to do here? What do we need to do here? What what do What do we
    need to do here? What what do

    we need to do here? >> Yep. >> Yep.

    You said it was like when tals just You said it was like when tals just You said
    it was like when tals just

    xpolation. >> Yeah. Yeah. So, so, so which term do we >> Yeah. Yeah. So, so, so
    which term do we

    need to take care of or which two terms need to take care of or which two terms
    need to take care of or which two terms

    I guess do we need to take care of the I guess do we need to take care of the
    I guess do we need to take care of the

    most? most? most?

    >> And then output weight, right? Yeah. >> And then output weight, right? Yeah.
    >> And then output weight, right? Yeah.

    Yeah. Exactly. Exactly. So essentially Yeah. Exactly. Exactly. So essentially
    Yeah. Exactly. Exactly. So essentially

    what we need to do is like as long as uh what we need to do is like as long as
    uh what we need to do is like as long as uh

    like when t is very close to zero or like when t is very close to zero or like
    when t is very close to zero or

    when t is zero the skip connection is'
  concept_slugs:
  - consistency-models
  - rectified-flow
- idx: 31
  start_sec: 1539.029
  end_sec: 1586.08
  text: 'when t is zero the skip connection is when t is zero the skip connection
    is

    one and then the output the weight is one and then the output the weight is one
    and then the output the weight is

    zero right then we''re just outputting zero right then we''re just outputting
    zero right then we''re just outputting

    then then this is just an identity then then this is just an identity then then
    this is just an identity

    function doesn''t really take any it function doesn''t really take any it function
    doesn''t really take any it

    doesn''t really care about the output at doesn''t really care about the output
    at doesn''t really care about the output at

    all like the network output at all right all like the network output at all right
    all like the network output at all right

    it only just like skip connect from it only just like skip connect from it only
    just like skip connect from

    input to output okay any question. okay any question.

    >> Yeah, >> Yeah, >> Yeah,

    >> need to handle this separately. Can''t >> need to handle this separately. Can''t
    >> need to handle this separately. Can''t

    the model just like learn condition on D the model just like learn condition on
    D the model just like learn condition on D

    to direct the output? to direct the output? to direct the output?

    >> Because if you do not have this boundary >> Because if you do not have this
    boundary >> Because if you do not have this boundary

    condition, then you do not really like condition, then you do not really like
    condition, then you do not really like

    basically you have like no way to know basically you have like no way to know
    basically you have like no way to know

    like basically um like like like it like like basically um like like like it like
    like basically um like like like it like

    like I said before, right? Your model like I said before, right? Your model like
    I said before, right? Your model

    can be like very self-consistent, but it can be like very self-consistent, but
    it can be like very self-consistent, but it

    can be producing garbage. Right now all can be producing garbage. Right now all'
  concept_slugs:
  - consistency-models
  - rectified-flow
- idx: 32
  start_sec: 1586.08
  end_sec: 1629.76
  text: 'can be producing garbage. Right now all

    this saying is that if my model sees a this saying is that if my model sees a
    this saying is that if my model sees a

    very good image already and also is the very good image already and also is the
    very good image already and also is the

    time is very close to zero then I just time is very close to zero then I just
    time is very close to zero then I just

    don''t change anything. So basically this don''t change anything. So basically
    this don''t change anything. So basically this

    is like pushing like the the output is like pushing like the the output is like
    pushing like the the output

    basically it just like if your output is basically it just like if your output
    is basically it just like if your output is

    good enough don''t change it kind of good enough don''t change it kind of good
    enough don''t change it kind of

    >> not handle that already. >> not handle that already. >> not handle that already.

    >> Well but this is not even loss right >> Well but this is not even loss right
    >> Well but this is not even loss right

    this is also not se like handling this is also not se like handling this is also
    not se like handling

    anything separately. This is literally anything separately. This is literally
    anything separately. This is literally

    just like your model like this is like just like your model like this is like
    just like your model like this is like

    not like an additional loss at all. This not like an additional loss at all. This
    not like an additional loss at all. This

    is just like you just need to add a skip is just like you just need to add a skip
    is just like you just need to add a skip

    connection and that''s it. connection and that''s it. connection and that''s it.

    Yeah. So this is like simpler I guess Yeah. So this is like simpler I guess Yeah.
    So this is like simpler I guess

    than having another loss function. I than having another loss function. I than
    having another loss function. I

    think I don''t I I agree with the thing think I don''t I I agree with the thing'
  concept_slugs:
  - consistency-models
  - rectified-flow
- idx: 33
  start_sec: 1629.76
  end_sec: 1673.2
  text: 'think I don''t I I agree with the thing

    that like the loss function on the last that like the loss function on the last
    that like the loss function on the last

    line can if you just do training with line can if you just do training with line
    can if you just do training with

    the loss function won''t this be like the loss function won''t this be like the
    loss function won''t this be like

    anything the model naturally learns to anything the model naturally learns to
    anything the model naturally learns to

    produce real images at the end won''t produce real images at the end won''t produce
    real images at the end won''t

    that happen even if you don''t do this that happen even if you don''t do this
    that happen even if you don''t do this

    >> I''m like pretty sure it may like it it >> I''m like pretty sure it may like
    it it >> I''m like pretty sure it may like it it

    may or may not like I actually never may or may not like I actually never may
    or may not like I actually never

    tried it so I can''t really tell you for tried it so I can''t really tell you
    for tried it so I can''t really tell you for

    sure maybe you should try it but the pro sure maybe you should try it but the
    pro sure maybe you should try it but the pro

    the point is it''s Like it may be very the point is it''s Like it may be very
    the point is it''s Like it may be very

    unstable to learn. I think that''s what''s unstable to learn. I think that''s
    what''s unstable to learn. I think that''s what''s

    happening. Like it this still it may happening. Like it this still it may happening.
    Like it this still it may

    still be possible but may not be good still be possible but may not be good still
    be possible but may not be good

    enough. Yeah. Yeah. enough. Yeah. Yeah. enough. Yeah. Yeah.

    >> It just should not it just impossibly >> It just should not it just impossibly
    >> It just should not it just impossibly

    should not because if we just ask it to should not because if we just ask it to'
  concept_slugs:
  - consistency-models
  - rectified-flow
- idx: 34
  start_sec: 1673.2
  end_sec: 1717.679
  text: 'should not because if we just ask it to

    do the same thing at S and T that same do the same thing at S and T that same
    do the same thing at S and T that same

    thing could just be end up predicting thing could just be end up predicting thing
    could just be end up predicting

    zero at all points. No, I mean I guess zero at all points. No, I mean I guess
    zero at all points. No, I mean I guess

    what they meant was that like without what they meant was that like without what
    they meant was that like without

    even parameterizing this if you train even parameterizing this if you train even
    parameterizing this if you train

    long enough it may still like learn the long enough it may still like learn the
    long enough it may still like learn the

    same skip connection essentially like same skip connection essentially like same
    skip connection essentially like

    this skip connection can be learned it this skip connection can be learned it
    this skip connection can be learned it

    it''s not necessarily need to be it''s not necessarily need to be it''s not necessarily
    need to be

    parameterized right is that what you''re parameterized right is that what you''re
    parameterized right is that what you''re

    saying yeah which is technically kind of saying yeah which is technically kind
    of saying yeah which is technically kind of

    true but it may be more difficult to true but it may be more difficult to true
    but it may be more difficult to

    learn right something like that yeah >> that the skip connection weight is like
    >> that the skip connection weight is like

    the identity matrix or do you let that the identity matrix or do you let that
    the identity matrix or do you let that

    be trained remember this one? be trained remember this one? be trained remember
    this one?

    >> No. So the the skip connection. So this >> No. So the the skip connection.
    So this >> No. So the the skip connection. So this

    thing is kind of like a scheduler like thing is kind of like a scheduler like
    thing is kind of like a scheduler like

    this. Sorry. The the skip connection this. Sorry. The the skip connection'
  concept_slugs:
  - consistency-models
  - rectified-flow
- idx: 35
  start_sec: 1717.679
  end_sec: 1773.11
  text: 'this. Sorry. The the skip connection

    weight is kind of like a schedule. It weight is kind of like a schedule. It weight
    is kind of like a schedule. It

    has a scheduling. It''s only one when has a scheduling. It''s only one when has
    a scheduling. It''s only one when

    you''re very very close at zero. Yeah. you''re very very close at zero. Yeah.
    you''re very very close at zero. Yeah.

    Yeah. Yeah. Yeah.

    >> That''s like actually part of the >> That''s like actually part of the >> That''s
    like actually part of the

    modeling. modeling. modeling.

    >> No no no. Yeah. Yeah. Yeah. Yeah. So >> No no no. Yeah. Yeah. Yeah. Yeah. So
    >> No no no. Yeah. Yeah. Yeah. Yeah. So

    well like basically it''s in like in your well like basically it''s in like in
    your well like basically it''s in like in your

    implementation, right? It''s like in your implementation, right? It''s like in
    your implementation, right? It''s like in your

    four like like function you do like four like like function you do like four like
    like function you do like

    output equals x plus something and then output equals x plus something and then
    output equals x plus something and then

    this x you like times like a scheduled this x you like times like a scheduled
    this x you like times like a scheduled

    weight essentially. Yeah. All right. So, uh we had this question All right. So,
    uh we had this question

    before, right? Does he actually need a before, right? Does he actually need a
    before, right? Does he actually need a

    pre-trained diffusion model? Does it pre-trained diffusion model? Does it pre-trained
    diffusion model? Does it

    really? Uh well, what do we think it uh it uh

    how about we just do not we just don''t how about we just do not we just don''t
    how about we just do not we just don''t

    we just don''t do it? We just don''t have we just don''t do it? We just don''t
    have we just don''t do it? We just don''t have

    a like the pre-trained diffusion model. a like the pre-trained diffusion model.
    a like the pre-trained diffusion model.

    We just somehow construct a OD We just somehow construct a OD We just somehow
    construct a OD

    trajectory that''s like kind of similar'
  concept_slugs:
  - consistency-models
  - rectified-flow
- idx: 36
  start_sec: 1773.11
  end_sec: 1825.669
  text: 'trajectory that''s like kind of similar trajectory that''s like kind of similar

    to what we what we would have got from a to what we what we would have got from
    a to what we what we would have got from a

    diffusion model, right? And then what diffusion model, right? And then what diffusion
    model, right? And then what

    you can do is you somehow produce a pair you can do is you somehow produce a pair
    you can do is you somehow produce a pair

    of the data from the same OD trajectory. of the data from the same OD trajectory.
    of the data from the same OD trajectory.

    Uh and then the easiest way to do it Uh and then the easiest way to do it Uh and
    then the easiest way to do it

    would be to fix a noise Z. So basically would be to fix a noise Z. So basically
    would be to fix a noise Z. So basically

    you like just imagine that you kind of you like just imagine that you kind of
    you like just imagine that you kind of

    having like a like a linear having like a like a linear having like a like a linear

    interpolation again, right, of the noise interpolation again, right, of the noise
    interpolation again, right, of the noise

    and the data. So now what you do, now and the data. So now what you do, now and
    the data. So now what you do, now

    what you do is like you just kind of what you do is like you just kind of what
    you do is like you just kind of

    have your uh xt equals to the data that have your uh xt equals to the data that
    have your uh xt equals to the data that

    you sample plus a scaled version of the you sample plus a scaled version of the
    you sample plus a scaled version of the

    the noise and then uh xt minus delta t the noise and then uh xt minus delta t
    the noise and then uh xt minus delta t

    equal to the same data plus uh the same equal to the same data plus uh the same
    equal to the same data plus uh the same

    noise but noise but noise but

    scale differently essentially. So that'
  concept_slugs:
  - consistency-models
  - rectified-flow
- idx: 37
  start_sec: 1825.669
  end_sec: 1880.08
  text: 'scale differently essentially. So that scale differently essentially. So
    that

    so that it''s like slightly less noisy. so that it''s like slightly less noisy.
    so that it''s like slightly less noisy.

    Uh then you just match the the the the Uh then you just match the the the the
    Uh then you just match the the the the

    the prediction and that''s it. the prediction and that''s it. the prediction and
    that''s it.

    Any question apparently? Okay. So you could do that apparently? Okay. So you could
    do that

    but you could do this and they show very but you could do this and they show very
    but you could do this and they show very

    good result uh from the paper but good result uh from the paper but good result
    uh from the paper but

    apparently this is this thing is apparently this is this thing is apparently this
    is this thing is

    actually actually actually

    pretty unstable to train actually. So uh pretty unstable to train actually. So
    uh pretty unstable to train actually. So uh

    they actually had a follow-up paper that they actually had a follow-up paper that
    they actually had a follow-up paper that

    is called they improve the technique of is called they improve the technique of
    is called they improve the technique of

    consistency training or something and consistency training or something and consistency
    training or something and

    where they kind of have like a EDM style where they kind of have like a EDM style
    where they kind of have like a EDM style

    paper that they just list all the tricks paper that they just list all the tricks
    paper that they just list all the tricks

    that they did to make this thing stable. that they did to make this thing stable.
    that they did to make this thing stable.

    Um but yeah but this is that this is how Um but yeah but this is that this is
    how Um but yeah but this is that this is how

    you could do it. you could do it. you could do it.

    Yeah, Yeah,

    >> I might be misunderstanding something >> I might be misunderstanding something
    >> I might be misunderstanding something

    about the previous uh slide, but about the previous uh slide, but'
  concept_slugs:
  - consistency-models
  - rectified-flow
- idx: 38
  start_sec: 1880.08
  end_sec: 1919.84
  text: 'about the previous uh slide, but

    >> uh so if we if we already know that the >> uh so if we if we already know that
    the >> uh so if we if we already know that the

    image is close enough to x0 where it''s image is close enough to x0 where it''s
    image is close enough to x0 where it''s

    like it''s good enough that we don''t want like it''s good enough that we don''t
    want like it''s good enough that we don''t want

    to pass it through the model anymore. to pass it through the model anymore. to
    pass it through the model anymore.

    >> Mhm. >> Mhm. >> Mhm.

    >> Why don''t we just like stop there? Why >> Why don''t we just like stop there?
    Why >> Why don''t we just like stop there? Why

    do we have to pass it? do we have to pass it? do we have to pass it?

    >> This is literally just stop there, >> This is literally just stop there, >>
    This is literally just stop there,

    right? This is literally just telling right? This is literally just telling right?
    This is literally just telling

    you that you stop there. Yeah. Yeah. you that you stop there. Yeah. Yeah. you
    that you stop there. Yeah. Yeah.

    Yeah, Yeah,

    >> then doesn''t even seem like a problem >> then doesn''t even seem like a problem
    >> then doesn''t even seem like a problem

    because you never reach the boundary to because you never reach the boundary to
    because you never reach the boundary to

    even activate the boundary. even activate the boundary. even activate the boundary.

    >> You will reach the boundary if you do >> You will reach the boundary if you
    do >> You will reach the boundary if you do

    not have this right. That''s the thing not have this right. That''s the thing
    not have this right. That''s the thing

    like if you really try to just learn like if you really try to just learn like
    if you really try to just learn

    everything that you do reach the everything that you do reach the everything that
    you do reach the

    boundary and it may not satisfy the boundary and it may not satisfy the boundary
    and it may not satisfy the

    boundary condition. Yeah. Okay. All boundary condition. Yeah. Okay. All'
  concept_slugs:
  - consistency-models
  - rectified-flow
- idx: 39
  start_sec: 1919.84
  end_sec: 1970.72
  text: 'boundary condition. Yeah. Okay. All

    right. Any any questions about training right. Any any questions about training
    right. Any any questions about training

    consistency model from scratch? consistency model from scratch? consistency model
    from scratch?

    >> Uh yes. >> Uh yes. >> Uh yes.

    >> The stock >> The stock >> The stock

    >> uh do we still need the stock grad? Yes, >> uh do we still need the stock grad?
    Yes, >> uh do we still need the stock grad? Yes,

    because you have two sta here. So if you because you have two sta here. So if
    you because you have two sta here. So if you

    do not have the sw, imagine that you''re do not have the sw, imagine that you''re
    do not have the sw, imagine that you''re

    like basically you have a changing like basically you have a changing like basically
    you have a changing

    target to match, right? And that doesn''t target to match, right? And that doesn''t
    target to match, right? And that doesn''t

    make sense. So you want your target to make sense. So you want your target to
    make sense. So you want your target to

    be not changing. Yeah. be not changing. Yeah. be not changing. Yeah.

    All right. Any more question? All right. Any more question? All right. Any more
    question?

    Cool. All right. So what what is the Cool. All right. So what what is the Cool.
    All right. So what what is the

    problem? Like do do we think the problem? Like do do we think the problem? Like
    do do we think the

    consistency model is perfect now? What consistency model is perfect now? What
    consistency model is perfect now? What

    do we think? Uh I think some people do we think? Uh I think some people do we
    think? Uh I think some people

    already said already said already said

    like oh it''s uh very difficult to like like oh it''s uh very difficult to like
    like oh it''s uh very difficult to like

    the the the sample like diversity can be the the the sample like diversity can
    be the the the sample like diversity can be

    impacted right that''s definitely true. impacted right that''s definitely true.
    impacted right that''s definitely true.

    Um and we''re not trying to solve it Um and we''re not trying to solve it'
  concept_slugs:
  - consistency-models
  - rectified-flow
- idx: 40
  start_sec: 1970.72
  end_sec: 2027.12
  text: 'Um and we''re not trying to solve it

    here. Well we kind of are trying to here. Well we kind of are trying to here.
    Well we kind of are trying to

    solve it here actually. Um solve it here actually. Um solve it here actually.
    Um

    uh wait yeah actually we do we could try uh wait yeah actually we do we could
    try uh wait yeah actually we do we could try

    yeah yeah with the with the next uh yeah yeah with the with the next uh yeah yeah
    with the with the next uh

    method we could solve partially the the method we could solve partially the the
    method we could solve partially the the

    diversity problem. But what else do we diversity problem. But what else do we
    diversity problem. But what else do we

    think that the consistency model that think that the consistency model that think
    that the consistency model that

    the that problem the consistency model the that problem the consistency model
    the that problem the consistency model

    has? Yeah. has? Yeah. has? Yeah.

    >> Question. Are you sampling from like a >> Question. Are you sampling from like
    a >> Question. Are you sampling from like a

    distribution like so wouldn''t wouldn''t distribution like so wouldn''t wouldn''t
    distribution like so wouldn''t wouldn''t

    like be dependent on XT? >> Uh oh. Okay. So how do you sample from a >> Uh oh.
    Okay. So how do you sample from a

    consensity model? Um yeah. So consensity model? Um yeah. So consensity model?
    Um yeah. So

    essentially that''s a great question essentially that''s a great question essentially
    that''s a great question

    actually and that ties into one of the actually and that ties into one of the
    actually and that ties into one of the

    problems. Uh so consistency model is problems. Uh so consistency model is problems.
    Uh so consistency model is

    great at doing one step generation which great at doing one step generation which
    great at doing one step generation which

    means that you directly go from a means that you directly go from a means that
    you directly go from a

    gausian to a sample. gausian to a sample. gausian to a sample.

    So one step but how do you do multi-step So one step but how do you do multi-step'
  concept_slugs:
  - consistency-models
  - rectified-flow
- idx: 41
  start_sec: 2027.12
  end_sec: 2060.879
  text: 'So one step but how do you do multi-step

    right? Can you even do multi-step? right? Can you even do multi-step? right? Can
    you even do multi-step?

    >> Yeah like we''re turning on a lot of like >> Yeah like we''re turning on a
    lot of like >> Yeah like we''re turning on a lot of like

    the other. the other. the other.

    >> Yeah. Why are we even doing that? Right. >> Yeah. Why are we even doing that?
    Right. >> Yeah. Why are we even doing that? Right.

    It doesn''t doesn''t really make sense. It doesn''t doesn''t really make sense.
    It doesn''t doesn''t really make sense.

    And like also how do you like how do you And like also how do you like how do
    you And like also how do you like how do you

    do multi-step? It''s not that clear, do multi-step? It''s not that clear, do multi-step?
    It''s not that clear,

    right? Because you can only go to the right? Because you can only go to the right?
    Because you can only go to the

    endpoint. You can''t really go to any endpoint. You can''t really go to any endpoint.
    You can''t really go to any

    intermediate point, right? So I mean you intermediate point, right? So I mean
    you intermediate point, right? So I mean you

    could go to the endpoint and then do could go to the endpoint and then do could
    go to the endpoint and then do

    DDIM, right? Then you add noise back and DDIM, right? Then you add noise back
    and DDIM, right? Then you add noise back and

    do this and that, but that''s not like do this and that, but that''s not like
    do this and that, but that''s not like

    that''s a second thought, right? So it''s that''s a second thought, right? So
    it''s that''s a second thought, right? So it''s

    like it''s really weird there. Yeah. And like it''s really weird there. Yeah.
    And like it''s really weird there. Yeah. And

    >> why do you want to do what? >> why do you want to do what? >> why do you want
    to do what?

    >> Why do you want to do that''s a great >> Why do you want to do that''s a great'
  concept_slugs:
  - consistency-models
  - ddim
  - rectified-flow
- idx: 42
  start_sec: 2060.879
  end_sec: 2104.72
  text: '>> Why do you want to do that''s a great

    question. The next slide is going to question. The next slide is going to question.
    The next slide is going to

    answer that. Yeah. answer that. Yeah. answer that. Yeah.

    This sort of model doesn''t seem like This sort of model doesn''t seem like This
    sort of model doesn''t seem like

    we''re exploiting the fact that it''s the we''re exploiting the fact that it''s
    the we''re exploiting the fact that it''s the

    task difficulty is not the same task difficulty is not the same task difficulty
    is not the same

    throughout all time. throughout all time. throughout all time.

    >> Yeah. Yeah. Yeah. Exactly. Exactly. >> Yeah. Yeah. Yeah. Exactly. Exactly.
    >> Yeah. Yeah. Yeah. Exactly. Exactly.

    Okay. Okay. This is why you want to do Okay. Okay. This is why you want to do
    Okay. Okay. This is why you want to do

    multi-step by the way. Okay. So the the multi-step by the way. Okay. So the the
    multi-step by the way. Okay. So the the

    the like basically the model is only the like basically the model is only the
    like basically the model is only

    trained to predict the clean data which trained to predict the clean data which
    trained to predict the clean data which

    means that it doesn''t it cannot do means that it doesn''t it cannot do means
    that it doesn''t it cannot do

    multi-step and basically it just means multi-step and basically it just means
    multi-step and basically it just means

    that it cannot it''s like very difficult that it cannot it''s like very difficult
    that it cannot it''s like very difficult

    to trade off quality and speed. So to trade off quality and speed. So to trade
    off quality and speed. So

    basically say you have like you don''t basically say you have like you don''t
    basically say you have like you don''t

    necessarily want one step generation necessarily want one step generation necessarily
    want one step generation

    right like for example you have a right like for example you have a right like
    for example you have a

    slightly more budget in terms of time slightly more budget in terms of time slightly
    more budget in terms of time

    or compute that you can afford to do or compute that you can afford to do'
  concept_slugs:
  - consistency-models
  - rectified-flow
- idx: 43
  start_sec: 2104.72
  end_sec: 2144.95
  text: 'or compute that you can afford to do

    four step generation say but like this four step generation say but like this
    four step generation say but like this

    model is not trained for that it doesn''t model is not trained for that it doesn''t
    model is not trained for that it doesn''t

    really make sense and for example say really make sense and for example say really
    make sense and for example say

    you want to prioritize like the middle you want to prioritize like the middle
    you want to prioritize like the middle

    part of the generation a little bit more part of the generation a little bit more
    part of the generation a little bit more

    right then this model is like not right then this model is like not right then
    this model is like not

    natural in doing that and in other words natural in doing that and in other words
    natural in doing that and in other words

    this model doesn''t really scale that this model doesn''t really scale that this
    model doesn''t really scale that

    well at inference time so like it''s not well at inference time so like it''s
    not well at inference time so like it''s not

    good at inference scaling and that''s a good at inference scaling and that''s
    a good at inference scaling and that''s a

    big issue, right? And then another thing big issue, right? And then another thing
    big issue, right? And then another thing

    that you guys probably already forgotten that you guys probably already forgotten
    that you guys probably already forgotten

    is that diffusion model can do exact log is that diffusion model can do exact
    log is that diffusion model can do exact log

    likelihood estimation. And if you do likelihood estimation. And if you do likelihood
    estimation. And if you do

    this kind of jumping, you completely this kind of jumping, you completely this
    kind of jumping, you completely

    lost the ability to calculate uh log lost the ability to calculate uh log lost
    the ability to calculate uh log

    likelihood. So now you kind of just likelihood. So now you kind of just likelihood.
    So now you kind of just

    become something like GAN. You just like become something like GAN. You just like
    become something like GAN. You just like

    do whatever I guess. Yeah, doesn''t'
  concept_slugs:
  - consistency-models
  - rectified-flow
- idx: 44
  start_sec: 2144.95
  end_sec: 2210.79
  text: 'do whatever I guess. Yeah, doesn''t do whatever I guess. Yeah, doesn''t

    really matter anymore. Um yeah so really matter anymore. Um yeah so really matter
    anymore. Um yeah so

    essentially essentially essentially

    um consistency model is not so perfect. um consistency model is not so perfect.
    um consistency model is not so perfect.

    Um then how can we fix it? >> Yeah like multiple boundary conditions >> Yeah like
    multiple boundary conditions

    types of like I don''t know. >> Very close. Very close. Good answer. >> Very close.
    Very close. Good answer.

    Good thinking. What about Yeah. Good thinking. What about Yeah. Good thinking.
    What about Yeah.

    >> Do we have to do linear jumps only? Like >> Do we have to do linear jumps only?
    Like >> Do we have to do linear jumps only? Like

    said like said like said like

    >> we don''t. Yeah. Yeah. Why are we even >> we don''t. Yeah. Yeah. Why are we
    even >> we don''t. Yeah. Yeah. Why are we even

    doing linear jumps? That''s a great doing linear jumps? That''s a great doing
    linear jumps? That''s a great

    question too. Like uh actually in the question too. Like uh actually in the question
    too. Like uh actually in the

    original uh consistency models the jumps original uh consistency models the jumps
    original uh consistency models the jumps

    are not really linear. So they do are not really linear. So they do are not really
    linear. So they do

    prioritize like some part of the prioritize like some part of the prioritize like
    some part of the

    trajectory a little bit more but they trajectory a little bit more but they trajectory
    a little bit more but they

    are doing a preset of uh like they do are doing a preset of uh like they do are
    doing a preset of uh like they do

    have a preset of discretized steps which have a preset of discretized steps which
    have a preset of discretized steps which

    is not necessarily is not necessarily is not necessarily

    you know which is not really necessary I you know which is not really necessary
    I you know which is not really necessary I

    guess what what this yeah yeah guess what what this yeah yeah guess what what
    this yeah yeah

    >> instead of doing like this one step to'
  concept_slugs:
  - consistency-models
  - rectified-flow
- idx: 45
  start_sec: 2210.79
  end_sec: 2247.68
  text: '>> instead of doing like this one step to >> instead of doing like this one
    step to

    the final noise you can do it like two the final noise you can do it like two
    the final noise you can do it like two

    steps and learn any intermediate step steps and learn any intermediate step steps
    and learn any intermediate step

    and that intermediate step can lie and that intermediate step can lie and that
    intermediate step can lie

    anywhere on the anywhere on the anywhere on the

    >> Yeah Yeah. Yeah. Yeah. Amazing. This is >> Yeah Yeah. Yeah. Yeah. Amazing.
    This is >> Yeah Yeah. Yeah. Yeah. Amazing. This is

    this is exactly correct. Yeah. So like this is exactly correct. Yeah. So like
    this is exactly correct. Yeah. So like

    how about learn instead of only learning how about learn instead of only learning
    how about learn instead of only learning

    jumping to the end, you learn to jump jumping to the end, you learn to jump jumping
    to the end, you learn to jump

    from anywhere to anywhere, right? So from anywhere to anywhere, right? So from
    anywhere to anywhere, right? So

    like you can learn like you know it like you can learn like you know it like you
    can learn like you know it

    doesn''t really need to be, you know, doesn''t really need to be, you know, doesn''t
    really need to be, you know,

    from only to the to the to the to the from only to the to the to the to the from
    only to the to the to the to the

    end point. What''s better is that you end point. What''s better is that you end
    point. What''s better is that you

    don''t even need to have like a linear don''t even need to have like a linear
    don''t even need to have like a linear

    schedule, right? you can have like schedule, right? you can have like schedule,
    right? you can have like

    arbitrarily like you can just be arbitrarily like you can just be arbitrarily
    like you can just be

    arbitrarily far away and then you should arbitrarily far away and then you should
    arbitrarily far away and then you should

    be able to jump to any point from any be able to jump to any point from any'
  concept_slugs:
  - consistency-models
  - rectified-flow
- idx: 46
  start_sec: 2247.68
  end_sec: 2300.88
  text: 'be able to jump to any point from any

    point to any point. Um so yeah so this point to any point. Um so yeah so this
    point to any point. Um so yeah so this

    xt is also arbitrary so you should be xt is also arbitrary so you should be xt
    is also arbitrary so you should be

    able to jump from xu to xs and stuff able to jump from xu to xs and stuff able
    to jump from xu to xs and stuff

    like that as well. Okay. Any question? like that as well. Okay. Any question?
    like that as well. Okay. Any question?

    >> Yeah. >> Yeah.

    >> How do you do this in practice? You >> How do you do this in practice? You
    >> How do you do this in practice? You

    >> h like it''s I''ll explain later. But this >> h like it''s I''ll explain later.
    But this >> h like it''s I''ll explain later. But this

    is a consistency trajectory model. So is a consistency trajectory model. So is
    a consistency trajectory model. So

    this is the thing that we developed at this is the thing that we developed at
    this is the thing that we developed at

    Sony. Um yeah, I was a part of this Sony. Um yeah, I was a part of this Sony.
    Um yeah, I was a part of this

    project very uh proudly a seventh author project very uh proudly a seventh author
    project very uh proudly a seventh author

    or something. Anyway, um but yeah, but or something. Anyway, um but yeah, but
    or something. Anyway, um but yeah, but

    yeah, this is consistency uh trajectory yeah, this is consistency uh trajectory
    yeah, this is consistency uh trajectory

    model. Okay. So, how do we train a model. Okay. So, how do we train a model. Okay.
    So, how do we train a

    consistency trajectory model? Any idea? consistency trajectory model? Any idea?
    consistency trajectory model? Any idea?

    Let''s first match with the Let''s first match with the Let''s first match with
    the

    self-consistency thing I guess from the self-consistency thing I guess from the
    self-consistency thing I guess from the

    consistency model. consistency model. consistency model.

    >> Yeah. >> Yeah.

    >> Like two points on the trajectory then >> Like two points on the trajectory
    then'
  concept_slugs:
  - consistency-models
  - rectified-flow
- idx: 47
  start_sec: 2300.88
  end_sec: 2344.72
  text: '>> Like two points on the trajectory then

    you saw the you saw the OD between them you saw the you saw the OD between them
    you saw the you saw the OD between them

    and then you essentially just take them. and then you essentially just take them.
    and then you essentially just take them.

    >> Yeah. Basically that basically that >> Yeah. Basically that basically that
    >> Yeah. Basically that basically that

    right. So essentially say you want to right. So essentially say you want to right.
    So essentially say you want to

    jump from XT to XS what you can do you jump from XT to XS what you can do you
    jump from XT to XS what you can do you

    can sample one point between them say can sample one point between them say can
    sample one point between them say

    that mean that''s XU right and then you that mean that''s XU right and then you
    that mean that''s XU right and then you

    you get to XU by using a solver with you get to XU by using a solver with you
    get to XU by using a solver with

    your uh teacher model and then you do your uh teacher model and then you do your
    uh teacher model and then you do

    another jump from the from your new another jump from the from your new another
    jump from the from your new

    model it just without gradient so stop model it just without gradient so stop
    model it just without gradient so stop

    gr right um so this is the part where uh gr right um so this is the part where
    uh gr right um so this is the part where uh

    it gets slightly more complicated but it gets slightly more complicated but it
    gets slightly more complicated but

    not really so essentially what''s not really so essentially what''s not really
    so essentially what''s

    happening is that Both L2 and perceptual happening is that Both L2 and perceptual
    happening is that Both L2 and perceptual

    loss are more meaningful especially loss are more meaningful especially loss are
    more meaningful especially

    perceptual loss actually it''s like more perceptual loss actually it''s like more
    perceptual loss actually it''s like more

    meaningful when you''re dealing with meaningful when you''re dealing with'
  concept_slugs:
  - consistency-models
  - rectified-flow
- idx: 48
  start_sec: 2344.72
  end_sec: 2392.79
  text: 'meaningful when you''re dealing with

    clean data. So think about it right the clean data. So think about it right the
    clean data. So think about it right the

    perceptual loss is like something like a perceptual loss is like something like
    a perceptual loss is like something like a

    Alex net or like inception net or Alex net or like inception net or Alex net or
    like inception net or

    something that is trained on imaget something that is trained on imaget something
    that is trained on imaget

    stuff like that. So they the the the stuff like that. So they the the the stuff
    like that. So they the the the

    feature extractor that you''re dealing feature extractor that you''re dealing
    feature extractor that you''re dealing

    with uh with this perceptual distance with uh with this perceptual distance with
    uh with this perceptual distance

    only have only seen clean data. So it only have only seen clean data. So it only
    have only seen clean data. So it

    has never seen uh noisy data before. So has never seen uh noisy data before. So
    has never seen uh noisy data before. So

    if you try to apply perceptual loss if you try to apply perceptual loss if you
    try to apply perceptual loss

    here, it''s actually really problematic. here, it''s actually really problematic.
    here, it''s actually really problematic.

    And similarly for L2, L2 is actually And similarly for L2, L2 is actually And
    similarly for L2, L2 is actually

    more meaningful uh when you are when more meaningful uh when you are when more
    meaningful uh when you are when

    you''re dealing with clean data. Uh so you''re dealing with clean data. Uh so
    you''re dealing with clean data. Uh so

    what we can do here is we can actually what we can do here is we can actually
    what we can do here is we can actually

    just take another jump uh from the just take another jump uh from the just take
    another jump uh from the

    middle to the end actually and then you middle to the end actually and then you
    middle to the end actually and then you

    you sort of you try to calculate the you sort of you try to calculate the you
    sort of you try to calculate the

    perceptual distance between the final X0'
  concept_slugs:
  - consistency-models
  - rectified-flow
- idx: 49
  start_sec: 2392.79
  end_sec: 2430.24
  text: 'perceptual distance between the final X0 perceptual distance between the
    final X0

    output. Um the only thing that you need output. Um the only thing that you need
    output. Um the only thing that you need

    to take care of is that we only want to to take care of is that we only want to
    to take care of is that we only want to

    take gradient through this one jump. So take gradient through this one jump. So
    take gradient through this one jump. So

    from t to s we only want to take from t to s we only want to take from t to s
    we only want to take

    gradient from this one jump and all the gradient from this one jump and all the
    gradient from this one jump and all the

    other jumps whether it''s from the other jumps whether it''s from the other jumps
    whether it''s from the

    teacher model or from the student model teacher model or from the student model
    teacher model or from the student model

    you know just like in order to go to the you know just like in order to go to
    the you know just like in order to go to the

    x0 everything is stop gra like x0 everything is stop gra like x0 everything is
    stop gra like

    everything has stop gradient. Okay. everything has stop gradient. Okay. everything
    has stop gradient. Okay.

    Yeah. Yeah.

    >> Why do we use like the solver for the >> Why do we use like the solver for
    the >> Why do we use like the solver for the

    first part and the new model for the first part and the new model for the first
    part and the new model for the

    second part? There could be so many second part? There could be so many second
    part? There could be so many

    choices for this, right? Like could you choices for this, right? Like could you
    choices for this, right? Like could you

    swap them or just use a solver both swap them or just use a solver both swap them
    or just use a solver both

    times? times? times?

    >> Yeah. Yeah. So like basically so the >> Yeah. Yeah. So like basically so the'
  concept_slugs:
  - consistency-models
  - rectified-flow
- idx: 50
  start_sec: 2430.24
  end_sec: 2478.319
  text: '>> Yeah. Yeah. So like basically so the

    this the first part uses solvers so that this the first part uses solvers so that
    this the first part uses solvers so that

    this thing this part is actually on the this thing this part is actually on the
    this thing this part is actually on the

    same trajectory essentially. Um and then same trajectory essentially. Um and then
    same trajectory essentially. Um and then

    but yes that''s actually a great great but yes that''s actually a great great
    but yes that''s actually a great great

    thing and then we''re we''re going to look thing and then we''re we''re going
    to look thing and then we''re we''re going to look

    at Yeah. Yeah. Yeah. But but it doesn''t at Yeah. Yeah. Yeah. But but it doesn''t
    at Yeah. Yeah. Yeah. But but it doesn''t

    need to be in the solver actually. Okay. need to be in the solver actually. Okay.
    need to be in the solver actually. Okay.

    Yeah. Yeah.

    >> To learn from like XTS. Can we learn the >> To learn from like XTS. Can we
    learn the >> To learn from like XTS. Can we learn the

    revers as well and like do from noise revers as well and like do from noise revers
    as well and like do from noise

    more like for example if we are getting more like for example if we are getting
    more like for example if we are getting

    more reconstruction errors we can like more reconstruction errors we can like
    more reconstruction errors we can like

    revert back is that possible revert back is that possible revert back is that
    possible

    >> yes yes yes it is possible >> yes yes yes it is possible >> yes yes yes it
    is possible

    actually um so basically uh in the paper actually um so basically uh in the paper
    actually um so basically uh in the paper

    they only learn to jump forward but you they only learn to jump forward but you
    they only learn to jump forward but you

    can still do like DD uh what we call DDI can still do like DD uh what we call
    DDI can still do like DD uh what we call DDI

    im style at at noise bag thing right and im style at at noise bag thing right
    and'
  concept_slugs:
  - consistency-models
  - rectified-flow
- idx: 51
  start_sec: 2478.319
  end_sec: 2522.319
  text: 'im style at at noise bag thing right and

    and that''s still valid actually in the and that''s still valid actually in the
    and that''s still valid actually in the

    in the paper like we have this thing in the paper like we have this thing in the
    paper like we have this thing

    called gamma sampling or something. So called gamma sampling or something. So
    called gamma sampling or something. So

    it''s kind of like a DDIM style sampling it''s kind of like a DDIM style sampling
    it''s kind of like a DDIM style sampling

    to both I think increase the diversity to both I think increase the diversity
    to both I think increase the diversity

    and also uh increase the uh sample and also uh increase the uh sample and also
    uh increase the uh sample

    quality. Yeah. But anyway but the quality. Yeah. But anyway but the quality. Yeah.
    But anyway but the

    problem here is that what is the problem here is that what is the problem here
    is that what is the

    boundary condition here right it did the boundary condition here right it did
    the boundary condition here right it did the

    like uh yeah sorry yeah go ahead. like uh yeah sorry yeah go ahead. like uh yeah
    sorry yeah go ahead.

    >> Okay. Yeah. >> Okay. Yeah.

    >> So you mentioned here we use the solver >> So you mentioned here we use the
    solver >> So you mentioned here we use the solver

    at the start to remain on that OD or we at the start to remain on that OD or we
    at the start to remain on that OD or we

    can say remain on the manifold of noise can say remain on the manifold of noise
    can say remain on the manifold of noise

    >> but then when we try to train our new >> but then when we try to train our
    new >> but then when we try to train our new

    model is it doesn''t it start from noise. model is it doesn''t it start from noise.
    model is it doesn''t it start from noise.

    So when we like get kicked off that or So when we like get kicked off that or
    So when we like get kicked off that or

    kicked off that kicked off that'
  concept_slugs:
  - consistency-models
  - ddim
  - rectified-flow
- idx: 52
  start_sec: 2522.319
  end_sec: 2579.99
  text: 'kicked off that

    >> uh what do you mean? Oh you mean like >> uh what do you mean? Oh you mean like
    >> uh what do you mean? Oh you mean like

    the the Oh yeah. So so like you mean the the Oh yeah. So so like you mean the
    the Oh yeah. So so like you mean

    like these parts right are not going to like these parts right are not going to
    like these parts right are not going to

    be accurate from the beginning? Yeah be accurate from the beginning? Yeah be accurate
    from the beginning? Yeah

    that is very true. But like if you train that is very true. But like if you train
    that is very true. But like if you train

    it long enough, it''s it''s actually going it long enough, it''s it''s actually
    going it long enough, it''s it''s actually going

    to be okay. Actually, the next thing is to be okay. Actually, the next thing is
    to be okay. Actually, the next thing is

    going to help with that too. So like going to help with that too. So like going
    to help with that too. So like

    what is the the boundary conditions is what is the the boundary conditions is
    what is the the boundary conditions is

    going to help with that. Um and what going to help with that. Um and what going
    to help with that. Um and what

    should a boundary condition be in this should a boundary condition be in this
    should a boundary condition be in this

    case? case? case?

    Because we do not have an actual Because we do not have an actual Because we do
    not have an actual

    boundary anymore, right? We do not have boundary anymore, right? We do not have
    boundary anymore, right? We do not have

    like an endpoint that we''re trying to go like an endpoint that we''re trying
    to go like an endpoint that we''re trying to go

    to anymore. to anymore. to anymore.

    So what is the new boundary here or what So what is the new boundary here or what
    So what is the new boundary here or what

    is the new edge case here? >> Yes. Exactly correct. Oh, so good. Okay. >> Yes.
    Exactly correct. Oh, so good. Okay.

    Yeah. But basically because we do not'
  concept_slugs:
  - consistency-models
  - rectified-flow
- idx: 53
  start_sec: 2579.99
  end_sec: 2632.56
  text: 'Yeah. But basically because we do not Yeah. But basically because we do not

    always match the end point now we we always match the end point now we we always
    match the end point now we we

    instead of a boundary condition we sort instead of a boundary condition we sort
    instead of a boundary condition we sort

    of have like a tangent condition where of have like a tangent condition where
    of have like a tangent condition where

    essentially if we''re trying to jump from essentially if we''re trying to jump
    from essentially if we''re trying to jump from

    t to t so that becomes the instantaneous t to t so that becomes the instantaneous
    t to t so that becomes the instantaneous

    change right so that should just be the change right so that should just be the
    change right so that should just be the

    score function which is literally the score function which is literally the score
    function which is literally the

    instantaneous change in the pfod right instantaneous change in the pfod right
    instantaneous change in the pfod right

    or the velocity essentially right so uh or the velocity essentially right so uh
    or the velocity essentially right so uh

    in other words we just need to add a a in other words we just need to add a a
    in other words we just need to add a a

    like just just the the regular score like just just the the regular score like
    just just the the regular score

    matching or diffusion loss matching or diffusion loss matching or diffusion loss

    and that''s it. And this is how you can and that''s it. And this is how you can
    and that''s it. And this is how you can

    satisfy a boundary condition with loss satisfy a boundary condition with loss
    satisfy a boundary condition with loss

    function too. You don''t need to encode function too. You don''t need to encode
    function too. You don''t need to encode

    it into your model either. Okay. So because you actually learn the Okay. So because
    you actually learn the

    score function. So now you can get your score function. So now you can get your
    score function. So now you can get your

    score right from jumping from T. Now um score right from jumping from T. Now um'
  concept_slugs:
  - consistency-models
  - rectified-flow
- idx: 54
  start_sec: 2632.56
  end_sec: 2683.599
  text: 'score right from jumping from T. Now um

    you you get your exact log likelihood you you get your exact log likelihood you
    you get your exact log likelihood

    back by because you can take the back by because you can take the back by because
    you can take the

    divergence and everything now divergence and everything now divergence and everything
    now

    right right right

    okay any question yeah yeah

    >> why why should it match the the score >> why why should it match the the score
    >> why why should it match the the score

    function like isn''t it just finding you function like isn''t it just finding
    you function like isn''t it just finding you

    can go back slide can go back slide can go back slide

    >> isn''t that the same oh okay you mean the >> isn''t that the same oh okay you
    mean the >> isn''t that the same oh okay you mean the

    the the diagram okay the the diagram okay the the diagram okay

    >> I Tell me about go from like t to like s >> I Tell me about go from like t
    to like s >> I Tell me about go from like t to like s

    for example with the model. for example with the model. for example with the model.

    >> Mhm. >> Mhm.

    >> Uh are we still doing this like like >> Uh are we still doing this like like
    >> Uh are we still doing this like like

    this interpolation thing with like stop this interpolation thing with like stop
    this interpolation thing with like stop

    or I don''t know if or I don''t know if or I don''t know if

    >> so essentially so this jump thing is >> so essentially so this jump thing is
    >> so essentially so this jump thing is

    different from the boundary condition different from the boundary condition different
    from the boundary condition

    laws that we are trying to or the laws that we are trying to or the laws that
    we are trying to or the

    tangent condition law. So tangent tangent condition law. So tangent tangent condition
    law. So tangent

    condition is like the instantaneous condition is like the instantaneous condition
    is like the instantaneous

    change that you''re going from a that change that you''re going from a that'
  concept_slugs:
  - consistency-models
  - rectified-flow
- idx: 55
  start_sec: 2683.599
  end_sec: 2730.55
  text: 'change that you''re going from a that

    you''re going from any point should you''re going from any point should you''re
    going from any point should

    follow the instant like the tangent line follow the instant like the tangent line
    follow the instant like the tangent line

    of the trajectory essentially. And then of the trajectory essentially. And then
    of the trajectory essentially. And then

    they''re not the same. they''re not the same. they''re not the same.

    They''re not the same. Are you also given They''re not the same. Are you also
    given They''re not the same. Are you also given

    this? this? this?

    >> No. If the two points are not the same, >> No. If the two points are not the
    same, >> No. If the two points are not the same,

    then you follow this diagram. So the two then you follow this diagram. So the
    two then you follow this diagram. So the two

    point not same, follow this diagram. The point not same, follow this diagram.
    The point not same, follow this diagram. The

    two points are the same, you follow the two points are the same, you follow the
    two points are the same, you follow the

    tangent line of the trajectory, which is tangent line of the trajectory, which
    is tangent line of the trajectory, which is

    just score matching or yeah or if you''re just score matching or yeah or if you''re
    just score matching or yeah or if you''re

    doing follow flow model flow matching, doing follow flow model flow matching,
    doing follow flow model flow matching,

    right? right? right?

    Okay. Uh so tangent condition. All Okay. Uh so tangent condition. All Okay. Uh
    so tangent condition. All

    right. So actually the way that the right. So actually the way that the right.
    So actually the way that the

    authors train the CTM is actually a authors train the CTM is actually a authors
    train the CTM is actually a

    combination of the CTM loss which is combination of the CTM loss which is combination
    of the CTM loss which is

    when you go trying to go from T to S when you go trying to go from T to S when
    you go trying to go from T to S

    when S is not equal to T and then score'
  concept_slugs:
  - consistency-models
  - rectified-flow
- idx: 56
  start_sec: 2730.55
  end_sec: 2773.99
  text: 'when S is not equal to T and then score when S is not equal to T and then
    score

    matching loss which is just go from T to matching loss which is just go from T
    to matching loss which is just go from T to

    T. So you just do diffusion loss T. So you just do diffusion loss T. So you just
    do diffusion loss

    normally and they actually also add a normally and they actually also add a normally
    and they actually also add a

    GAN loss. So you see like everything we GAN loss. So you see like everything we
    GAN loss. So you see like everything we

    learn is usable like everything we learn learn is usable like everything we learn
    learn is usable like everything we learn

    is like useful here. Okay. So adding the is like useful here. Okay. So adding
    the is like useful here. Okay. So adding the

    GAN loss actually gives a lot of GAN loss actually gives a lot of GAN loss actually
    gives a lot of

    improvement uh of the FID. So this is improvement uh of the FID. So this is improvement
    uh of the FID. So this is

    sort of a trick that you can do. So if sort of a trick that you can do. So if
    sort of a trick that you can do. So if

    you when in doubt just add the GAN loss you when in doubt just add the GAN loss
    you when in doubt just add the GAN loss

    if you know how to train again it''s if you know how to train again it''s if you
    know how to train again it''s

    going to boost your performance going to boost your performance going to boost
    your performance

    basically. basically. basically.

    >> Yeah. >> Yeah.

    >> The is the input to the discriminator >> The is the input to the discriminator
    >> The is the input to the discriminator

    like the noisy image at time step t or like the noisy image at time step t or
    like the noisy image at time step t or

    is it like the repredicted image at like is it like the repredicted image at like
    is it like the repredicted image at like

    x0? x0? x0?

    >> Uh which one? Uh you''re saying that we'
  concept_slugs:
  - consistency-models
  - rectified-flow
- idx: 57
  start_sec: 2773.99
  end_sec: 2837.52
  text: '>> Uh which one? Uh you''re saying that we >> Uh which one? Uh you''re saying
    that we

    add like a discriminator to improve FID add like a discriminator to improve FID
    add like a discriminator to improve FID

    score. score. score.

    >> Ah yes yes >> Ah yes yes >> Ah yes yes

    >> the end point everything is uh evaluated >> the end point everything is uh
    evaluated >> the end point everything is uh evaluated

    at the end point at the end point we at the end point at the end point we at the
    end point at the end point we

    apply like a stop gradient right apply like a stop gradient right apply like a
    stop gradient right

    >> oh that''s right actually I''m not sure maybe that''s right actually I''m not
    sure maybe

    it''s not on the endpoint I''ll double it''s not on the endpoint I''ll double
    it''s not on the endpoint I''ll double

    check on this sorry I''m I''m supposed to check on this sorry I''m I''m supposed
    to check on this sorry I''m I''m supposed to

    be one of the authors but I don''t be one of the authors but I don''t be one of
    the authors but I don''t

    remember what exactly we Yeah. Anyway, remember what exactly we Yeah. Anyway,
    remember what exactly we Yeah. Anyway,

    yeah. >> Yeah.

    >> Would you remember the CTM losses from >> Would you remember the CTM losses
    from >> Would you remember the CTM losses from

    DS and score DS and score DS and score

    >> C see this is this part is the CTM loss. >> C see this is this part is the
    CTM loss. >> C see this is this part is the CTM loss.

    This part is the score matching loss. This part is the score matching loss. This
    part is the score matching loss.

    Yeah. Yeah.

    And then again loss is just something to And then again loss is just something
    to And then again loss is just something to

    boost performance. Yeah, maybe they are boost performance. Yeah, maybe they are
    boost performance. Yeah, maybe they are

    doing a noise condition again then doing a noise condition again then doing a
    noise condition again then

    otherwise it doesn''t make sense I guess. otherwise it doesn''t make sense I guess.'
  concept_slugs:
  - consistency-models
  - rectified-flow
- idx: 58
  start_sec: 2837.52
  end_sec: 2896.15
  text: 'otherwise it doesn''t make sense I guess.

    Yeah. >> Yeah. Oh sorry. Yeah. >> Yeah. Oh sorry. Yeah.

    >> How do you weigh the different loss >> How do you weigh the different loss
    >> How do you weigh the different loss

    transm Yeah. So, so, so Yeah. So, so, so

    these different terms I in the paper these different terms I in the paper these
    different terms I in the paper

    like they actually did a they we like they actually did a they we like they actually
    did a they we

    actually did a uh ablation study and actually did a uh ablation study and actually
    did a uh ablation study and

    then basically um you''ll see I think um then basically um you''ll see I think
    um then basically um you''ll see I think um

    the ratio was 1 to 0.1 or something like the ratio was 1 to 0.1 or something like
    the ratio was 1 to 0.1 or something like

    that is the the the the CTM to DSM uh that is the the the the CTM to DSM uh that
    is the the the the CTM to DSM uh

    the score matching loss. Um but I think the score matching loss. Um but I think
    the score matching loss. Um but I think

    it''s like pretty robust like in in terms it''s like pretty robust like in in
    terms it''s like pretty robust like in in terms

    of the the waiting. So like if you if of the the waiting. So like if you if of
    the the waiting. So like if you if

    you add the score matching loss is you add the score matching loss is you add
    the score matching loss is

    always improving essentially or maybe always improving essentially or maybe always
    improving essentially or maybe

    yeah actually I I don''t remember what yeah actually I I don''t remember what
    yeah actually I I don''t remember what

    exactly is the ratio but yeah like and exactly is the ratio but yeah like and
    exactly is the ratio but yeah like and

    the GAN loss is also the same like you the GAN loss is also the same like you
    the GAN loss is also the same like you

    you almost always improve the you almost always improve the you almost always
    improve the

    performance yeah'
  concept_slugs:
  - consistency-models
  - rectified-flow
  - score-matching
- idx: 59
  start_sec: 2904.95
  end_sec: 2960.16
  text: 'so I guess someone asked right do Do you so I guess someone asked right do
    Do you

    even need a solver here? Uh the answer even need a solver here? Uh the answer
    even need a solver here? Uh the answer

    is not really honestly, right? Because is not really honestly, right? Because
    is not really honestly, right? Because

    you can literally replace this with any you can literally replace this with any
    you can literally replace this with any

    other things. For example, your new other things. For example, your new other
    things. For example, your new

    model because your new model actually model because your new model actually model
    because your new model actually

    has a score function with it, right? has a score function with it, right? has
    a score function with it, right?

    When you do T2T. So you can just do When you do T2T. So you can just do When you
    do T2T. So you can just do

    normal like solver solving normal like solver solving normal like solver solving

    diffusion model except the diffusion diffusion model except the diffusion diffusion
    model except the diffusion

    model is actually your new model, your model is actually your new model, your
    model is actually your new model, your

    CTM model. And then you do the same CTM model. And then you do the same CTM model.
    And then you do the same

    thing and then now you get a consistency thing and then now you get a consistency
    thing and then now you get a consistency

    trajectory model trained from scratch. trajectory model trained from scratch.
    trajectory model trained from scratch.

    This is very nice. Okay. Any other questions about Okay. Any other questions about

    consistency trajectory models? >> Yeah.

    >> Can you do these things? >> Can you do these things? >> Can you do these things?

    >> Yeah. Very nice. Very nice. Okay. Let''s >> Yeah. Very nice. Very nice. Okay.
    Let''s >> Yeah. Very nice. Very nice. Okay. Let''s

    let''s let''s get started with this. Okay. let''s let''s get started with this.
    Okay. let''s let''s get started with this. Okay.

    So I wa today the questions are so nice. So I wa today the questions are so nice.
    So I wa today the questions are so nice.

    Is it just like all the questions are Is it just like all the questions are'
  concept_slugs:
  - consistency-models
  - rectified-flow
- idx: 60
  start_sec: 2960.16
  end_sec: 3004.079
  text: 'Is it just like all the questions are

    like, "Oh, the thing that we''re going to like, "Oh, the thing that we''re going
    to like, "Oh, the thing that we''re going to

    talk about next." Very nice. Okay. talk about next." Very nice. Okay. talk about
    next." Very nice. Okay.

    Anyway, um so why does it work, right? Anyway, um so why does it work, right?
    Anyway, um so why does it work, right?

    Like why why why is this thing even Like why why why is this thing even Like why
    why why is this thing even

    legit? It turns out as per usual, you legit? It turns out as per usual, you legit?
    It turns out as per usual, you

    know, the physics people have already know, the physics people have already know,
    the physics people have already

    give us the answer a long time ago and I give us the answer a long time ago and
    I give us the answer a long time ago and I

    really appreciate this meme. This is a really appreciate this meme. This is a
    really appreciate this meme. This is a

    great meme. Um but anyway um but yeah great meme. Um but anyway um but yeah great
    meme. Um but anyway um but yeah

    basically there''s this notion called basically there''s this notion called basically
    there''s this notion called

    flow map in math slash physics and uh flow map in math slash physics and uh flow
    map in math slash physics and uh

    essentially what a flow map in diffusion essentially what a flow map in diffusion
    essentially what a flow map in diffusion

    terms or like in in in the in the OD is terms or like in in in the in the OD is
    terms or like in in in the in the OD is

    that okay so flow map in physics is like that okay so flow map in physics is like
    that okay so flow map in physics is like

    trying to solve some like complex trying to solve some like complex trying to
    solve some like complex

    dynamic systems that can be described by dynamic systems that can be described
    by dynamic systems that can be described by

    OD or PD or whatever um and then the OD or PD or whatever um and then the'
  concept_slugs:
  - consistency-models
  - rectified-flow
- idx: 61
  start_sec: 3004.079
  end_sec: 3063.28
  text: 'OD or PD or whatever um and then the

    flow maps because we also look at ODEs flow maps because we also look at ODEs
    flow maps because we also look at ODEs

    right especially if If you''re doing flow right especially if If you''re doing
    flow right especially if If you''re doing flow

    matching um then we can also learn flow matching um then we can also learn flow
    matching um then we can also learn flow

    maps for the probability flow OD or the maps for the probability flow OD or the
    maps for the probability flow OD or the

    flow matching OD right so essentially flow matching OD right so essentially flow
    matching OD right so essentially

    this is what''s happening so a flow map this is what''s happening so a flow map
    this is what''s happening so a flow map

    is literally just a function to tell you is literally just a function to tell
    you is literally just a function to tell you

    to jump like essentially this is like to jump like essentially this is like to
    jump like essentially this is like

    you if you want to jump from xt from t you if you want to jump from xt from t
    you if you want to jump from xt from t

    to s then your flow map literally just to s then your flow map literally just
    to s then your flow map literally just

    like literally predict the displacement like literally predict the displacement
    like literally predict the displacement

    for you so that you can jump for you so that you can jump for you so that you
    can jump

    like this. Okay. Okay.

    Question. Question. Question.

    Yeah. Yeah.

    >> X >> X >> X

    from there. from there. from there.

    >> Yeah. Yeah. How? Great, great, great >> Yeah. Yeah. How? Great, great, great
    >> Yeah. Yeah. How? Great, great, great

    question. How do you build a valid flow question. How do you build a valid flow
    question. How do you build a valid flow

    map? I forgot to add animation here. map? I forgot to add animation here. map?
    I forgot to add animation here.

    It''s very sad. Anyway, um but how do you It''s very sad. Anyway, um but how do
    you'
  concept_slugs:
  - consistency-models
  - probability-flow-ode
  - rectified-flow
- idx: 62
  start_sec: 3063.28
  end_sec: 3109.27
  text: 'It''s very sad. Anyway, um but how do you

    uh build a valid flow map? Actually the uh build a valid flow map? Actually the
    uh build a valid flow map? Actually the

    answer to this question uh can be found answer to this question uh can be found
    answer to this question uh can be found

    in a paper that''s written by our in a paper that''s written by our in a paper
    that''s written by our

    own CMU professor Nicholas Buffy. Um own CMU professor Nicholas Buffy. Um own
    CMU professor Nicholas Buffy. Um

    yeah so this is Nick''s paper called how yeah so this is Nick''s paper called
    how yeah so this is Nick''s paper called how

    to build a consistency model learning to build a consistency model learning to
    build a consistency model learning

    flow mass via self dissolation. Okay. flow mass via self dissolation. Okay. flow
    mass via self dissolation. Okay.

    Yeah. So basically uh how to build full Yeah. So basically uh how to build full
    Yeah. So basically uh how to build full

    map is it literally just uh let let''s map is it literally just uh let let''s
    map is it literally just uh let let''s

    just say this u thing is like the just say this u thing is like the just say this
    u thing is like the

    displacement between uh xt and xs from t displacement between uh xt and xs from
    t displacement between uh xt and xs from t

    to s uh and then the v is the to s uh and then the v is the to s uh and then the
    v is the

    instantaneous velocity that we learn instantaneous velocity that we learn instantaneous
    velocity that we learn

    from like a flow matching model say uh from like a flow matching model say uh
    from like a flow matching model say uh

    or or just the tangent of the od or or just the tangent of the od or or just the
    tangent of the od

    trajectories and then uh this thing is trajectories and then uh this thing is
    trajectories and then uh this thing is

    the flow map. So basically this is the the flow map. So basically this is the
    the flow map. So basically this is the

    prediction of XS. Okay. So flow map is'
  concept_slugs:
  - consistency-models
  - rectified-flow
- idx: 63
  start_sec: 3109.27
  end_sec: 3150.16
  text: 'prediction of XS. Okay. So flow map is prediction of XS. Okay. So flow map
    is

    the predict prediction of XS the the predict prediction of XS the the predict
    prediction of XS the

    endpoint of the jump. Okay. So what you endpoint of the jump. Okay. So what you
    endpoint of the jump. Okay. So what you

    need to do is you need to satisfy two need to do is you need to satisfy two need
    to do is you need to satisfy two

    things. One is the tangent condition things. One is the tangent condition things.
    One is the tangent condition

    which is the same thing that we have which is the same thing that we have which
    is the same thing that we have

    seen in the uh CTM model. And then uh seen in the uh CTM model. And then uh seen
    in the uh CTM model. And then uh

    the second thing is you need to satisfy the second thing is you need to satisfy
    the second thing is you need to satisfy

    one of the following three conditions. one of the following three conditions.
    one of the following three conditions.

    What are these conditions anyway? They What are these conditions anyway? They
    What are these conditions anyway? They

    they all look so fancy. They all look they all look so fancy. They all look they
    all look so fancy. They all look

    have some great like lrangei and the have some great like lrangei and the have
    some great like lrangei and the

    oiler and semi group. What do they even oiler and semi group. What do they even
    oiler and semi group. What do they even

    mean? Like why are you doing this to us? mean? Like why are you doing this to
    us? mean? Like why are you doing this to us?

    Right. Okay. We''re going to talk about Right. Okay. We''re going to talk about
    Right. Okay. We''re going to talk about

    what it means. Um but basically what it means. Um but basically what it means.
    Um but basically

    uh like to understand what it means I uh like to understand what it means I uh
    like to understand what it means I

    guess. Uh let''s just like take this guess. Uh let''s just like take this'
  concept_slugs:
  - consistency-models
  - rectified-flow
- idx: 64
  start_sec: 3150.16
  end_sec: 3201.27
  text: 'guess. Uh let''s just like take this

    analogy. Okay. Yes. analogy. Okay. Yes. analogy. Okay. Yes.

    >> Call it progressive. Is that the same >> Call it progressive. Is that the same
    >> Call it progressive. Is that the same

    call in group? call in group? call in group?

    >> Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. >> Yeah. Yeah. Yeah. Yeah. Yeah. Yeah.
    >> Yeah. Yeah. Yeah. Yeah. Yeah. Yeah.

    We''re going to talk about this. Yeah. We''re going to talk about this. Yeah.
    We''re going to talk about this. Yeah.

    But yes, that''s exactly correct. the the But yes, that''s exactly correct. the
    the But yes, that''s exactly correct. the the

    the intuition is exactly correct. Um but the intuition is exactly correct. Um
    but the intuition is exactly correct. Um but

    what what do I say? Okay. So um let''s what what do I say? Okay. So um let''s
    what what do I say? Okay. So um let''s

    just like absorb this analogy here just like absorb this analogy here just like
    absorb this analogy here

    first. Okay. Uh so let''s say we''re we''re first. Okay. Uh so let''s say we''re
    we''re first. Okay. Uh so let''s say we''re we''re

    we''re looking at some rubber ducks we''re looking at some rubber ducks we''re
    looking at some rubber ducks

    flowing down the river where this river flowing down the river where this river
    flowing down the river where this river

    is your flow matching field. Okay. And is your flow matching field. Okay. And
    is your flow matching field. Okay. And

    the rubber duck is your ax basically. the rubber duck is your ax basically. the
    rubber duck is your ax basically.

    Okay. So suppose I am a magician where I Okay. So suppose I am a magician where
    I Okay. So suppose I am a magician where I

    can teleport the rubber duck in this one can teleport the rubber duck in this
    one can teleport the rubber duck in this one

    particular river. So I am the flow map. particular river. So I am the flow map.
    particular river. So I am the flow map.

    Okay. Uh in other words for the duck Okay. Uh in other words for the duck Okay.
    Uh in other words for the duck

    that is flowing down this one river. I'
  concept_slugs:
  - consistency-models
  - rectified-flow
- idx: 65
  start_sec: 3201.27
  end_sec: 3240.96
  text: 'that is flowing down this one river. I that is flowing down this one river.
    I

    can teleport the duck so that the duck''s can teleport the duck so that the duck''s
    can teleport the duck so that the duck''s

    location in the river will be the same location in the river will be the same
    location in the river will be the same

    after I teleported as if it has followed after I teleported as if it has followed
    after I teleported as if it has followed

    the normal river flow. Okay. So the normal river flow. Okay. So the normal river
    flow. Okay. So

    basically just no matter the the duck is basically just no matter the the duck
    is basically just no matter the the duck is

    I can like magically predict where the I can like magically predict where the
    I can like magically predict where the

    flow is going to go and just like bing flow is going to go and just like bing
    flow is going to go and just like bing

    bing and then the the duck is just going bing and then the the duck is just going
    bing and then the the duck is just going

    to be right there. to be right there. to be right there.

    All right. Does this make sense to two All right. Does this make sense to two
    All right. Does this make sense to two

    people? people? people?

    >> Yeah. >> Yeah.

    >> What about like the time duration? >> What about like the time duration? >>
    What about like the time duration?

    >> Ah yeah good great question. So the time >> Ah yeah good great question. So
    the time >> Ah yeah good great question. So the time

    is like where like the time is just is like where like the time is just is like
    where like the time is just

    imagine um the bank like the location on imagine um the bank like the location
    on imagine um the bank like the location on

    the bank is your your time. Uh so let''s the bank is your your time. Uh so let''s
    the bank is your your time. Uh so let''s

    get like basically okay. So I guess this get like basically okay. So I guess this'
  concept_slugs:
  - consistency-models
  - rectified-flow
- idx: 66
  start_sec: 3240.96
  end_sec: 3279.839
  text: 'get like basically okay. So I guess this

    is a better uh uh visualization. So this is a better uh uh visualization. So this
    is a better uh uh visualization. So this

    is generated by nano banana the thing is generated by nano banana the thing is
    generated by nano banana the thing

    that we learned the last time. Um anyway that we learned the last time. Um anyway
    that we learned the last time. Um anyway

    but basically what we do is like I can but basically what we do is like I can
    but basically what we do is like I can

    do a magic jump from time s to time t do a magic jump from time s to time t do
    a magic jump from time s to time t

    and lrunion is basically just say that and lrunion is basically just say that
    and lrunion is basically just say that

    think like say you have a cop at at time think like say you have a cop at at time
    think like say you have a cop at at time

    at time. So say we''re jumping from s to at time. So say we''re jumping from s
    to at time. So say we''re jumping from s to

    t. the the the notation is a little bit t. the the the notation is a little bit
    t. the the the notation is a little bit

    messy, but say we''re jumping from S to T messy, but say we''re jumping from S
    to T messy, but say we''re jumping from S to T

    and Lren is saying that we have a cop at and Lren is saying that we have a cop
    at and Lren is saying that we have a cop at

    time t. It''s like, you know, those cops time t. It''s like, you know, those cops
    time t. It''s like, you know, those cops

    at the at the highway, you know, they''re at the at the highway, you know, they''re
    at the at the highway, you know, they''re

    just like trying to like like do speed just like trying to like like do speed
    just like trying to like like do speed

    check for you. And then and then the the check for you. And then and then the
    the'
  concept_slugs:
  - consistency-models
  - rectified-flow
- idx: 67
  start_sec: 3279.839
  end_sec: 3324.64
  text: 'check for you. And then and then the the

    cop be like, huh, let''s see if there''s cop be like, huh, let''s see if there''s
    cop be like, huh, let''s see if there''s

    any duck that is like suspicious. Like, any duck that is like suspicious. Like,
    any duck that is like suspicious. Like,

    let''s see if there''s any duck that is let''s see if there''s any duck that is
    let''s see if there''s any duck that is

    using teleportation. using teleportation. using teleportation.

    Okay. So basically the goal of us as a Okay. So basically the goal of us as a
    Okay. So basically the goal of us as a

    lrungian is to make sure that no cop can lrungian is to make sure that no cop
    can lrungian is to make sure that no cop can

    caught us. So basically the speed that caught us. So basically the speed that
    caught us. So basically the speed that

    you going through it at time t um should you going through it at time t um should
    you going through it at time t um should

    be the same as as if you''re like be the same as as if you''re like be the same
    as as if you''re like

    following the normal flow. So what it following the normal flow. So what it following
    the normal flow. So what it

    means is that what do you mean by the means is that what do you mean by the means
    is that what do you mean by the

    speed that we''re going is speed that we''re going is speed that we''re going
    is

    it''s basically just like the it''s basically just like the it''s basically just
    like the

    instantaneous flow map jump which should instantaneous flow map jump which should
    instantaneous flow map jump which should

    match the the velocity, right? It should match the the velocity, right? It should
    match the the velocity, right? It should

    be so like if the cop is like trying to be so like if the cop is like trying to
    be so like if the cop is like trying to

    catch you there, you just do an catch you there, you just do an catch you there,
    you just do an

    instantaneous jump so that you can fold instantaneous jump so that you can fold'
  concept_slugs:
  - consistency-models
  - rectified-flow
- idx: 68
  start_sec: 3324.64
  end_sec: 3385.75
  text: 'instantaneous jump so that you can fold

    the cop and then and then be like, "Oh, the cop and then and then be like, "Oh,
    the cop and then and then be like, "Oh,

    okay. This is a normal duck." Basically, okay. This is a normal duck." Basically,
    okay. This is a normal duck." Basically,

    that does it make sense. Uh I''m very happy I I spent so much time Uh I''m very
    happy I I spent so much time

    coming up with this an analogy. Anyway, coming up with this an analogy. Anyway,
    coming up with this an analogy. Anyway,

    good stuff. Okay, but basically in a good stuff. Okay, but basically in a good
    stuff. Okay, but basically in a

    more more more

    obractive way. So say you''re jumping obractive way. So say you''re jumping obractive
    way. So say you''re jumping

    from t to s uh and you have like a from t to s uh and you have like a from t to
    s uh and you have like a

    instantaneous velocity you have an instantaneous velocity you have an instantaneous
    velocity you have an

    instantaneous flow map jump here from s instantaneous flow map jump here from
    s instantaneous flow map jump here from s

    to like dt where dt is like to like dt where dt is like to like dt where dt is
    like

    instantaneously small and uh sorry and instantaneously small and uh sorry and
    instantaneously small and uh sorry and

    then basically this this like then basically this this like then basically this
    this like

    instantaneous jump should match the instantaneous jump should match the instantaneous
    jump should match the

    instantaneous velocity of the instantaneous velocity of the instantaneous velocity
    of the

    trajectory. Yeah,

    >> you use the lrangian method to go from T >> you use the lrangian method to
    go from T >> you use the lrangian method to go from T

    to S to S to S

    >> and then when you''re saying that from S >> and then when you''re saying that
    from S >> and then when you''re saying that from S

    to S plus DT, it should be the same as to S plus DT, it should be the same as
    to S plus DT, it should be the same as

    the instantaneous. the instantaneous. the instantaneous.

    >> Yes.'
  concept_slugs:
  - consistency-models
  - rectified-flow
- idx: 69
  start_sec: 3385.76
  end_sec: 3457.119
  text: '>> Yes.

    >> So if you take a langian from S to S >> So if you take a langian from S to
    S >> So if you take a langian from S to S

    plus DT, it should be the same as the is plus DT, it should be the same as the
    is plus DT, it should be the same as the is

    that that that

    >> the math a little bit. >> the math a little bit. >> the math a little bit.

    So essentially it''s like you take the So essentially it''s like you take the
    So essentially it''s like you take the

    lrundrian or sorry you take the flow lrundrian or sorry you take the flow lrundrian
    or sorry you take the flow

    mapap jump from t to s and then if you mapap jump from t to s and then if you
    mapap jump from t to s and then if you

    if you''re cop if you''re cop if you''re cop

    if you''re basically if you take the time if you''re basically if you take the
    time if you''re basically if you take the time

    derivative here it would be the same as derivative here it would be the same as
    derivative here it would be the same as

    if you''re doing a instantaneous time if you''re doing a instantaneous time if
    you''re doing a instantaneous time

    jump with your full map there. Okay, any more questions? Okay, any more questions?

    >> Yeah. S= Z in this is it the consistency >> Yeah. S= Z in this is it the consistency
    >> Yeah. S= Z in this is it the consistency

    mode is it let me think is it let me think

    uh uh uh

    not exactly I guess um because it not exactly I guess um because it not exactly
    I guess um because it

    doesn''t doesn''t doesn''t

    because we don''t really match like for because we don''t really match like for
    because we don''t really match like for

    consistency. Oh, I uh I I I guess kind consistency. Oh, I uh I I I guess kind
    consistency. Oh, I uh I I I guess kind

    of because like I it''s not consistent. of because like I it''s not consistent.
    of because like I it''s not consistent.

    It''s it''s more well for consistency model we don''t'
  concept_slugs:
  - consistency-models
  - rectified-flow
- idx: 70
  start_sec: 3457.119
  end_sec: 3513.04
  text: 'well for consistency model we don''t

    really match the the the derivative. I really match the the the derivative. I
    really match the the the derivative. I

    guess that''s the problem. guess that''s the problem. guess that''s the problem.

    But the next thing is actually CTN. So But the next thing is actually CTN. So
    But the next thing is actually CTN. So

    let''s let''s take a look at it. Uh oh, do let''s let''s take a look at it. Uh
    oh, do let''s let''s take a look at it. Uh oh, do

    I have it? Okay, cool. I have it? Okay, cool. I have it? Okay, cool.

    All right. So, Oilerian All right. So, Oilerian All right. So, Oilerian

    um is basically let''s say we don''t have um is basically let''s say we don''t
    have um is basically let''s say we don''t have

    this co-op anymore. Um but but basically this co-op anymore. Um but but basically
    this co-op anymore. Um but but basically

    what we''re doing is um what we''re doing is um what we''re doing is um

    say we have a magic jump from S to T and say we have a magic jump from S to T
    and say we have a magic jump from S to T and

    uh we have a like observer here uh uh we have a like observer here uh uh we have
    a like observer here uh

    observer on the shore and basically what observer on the shore and basically what
    observer on the shore and basically what

    is happening here is that no matter is happening here is that no matter is happening
    here is that no matter

    which part of the river do I start like which part of the river do I start like
    which part of the river do I start like

    so I don''t necessarily need to start at so I don''t necessarily need to start
    at so I don''t necessarily need to start at

    S as long as I''m following the same flow S as long as I''m following the same
    flow S as long as I''m following the same flow

    I can do I can be a little bit like I I can do I can be a little bit like I'
  concept_slugs:
  - consistency-models
  - rectified-flow
- idx: 71
  start_sec: 3513.04
  end_sec: 3597.43
  text: 'I can do I can be a little bit like I

    can essentially be a a little bit um can essentially be a a little bit um can
    essentially be a a little bit um

    like late. I can I I can start the jump like late. I can I I can start the jump
    like late. I can I I can start the jump

    a little bit later and I will still get a little bit later and I will still get
    a little bit later and I will still get

    to the same key position. to the same key position. to the same key position.

    Does it make sense? the total derivative of your starting the total derivative
    of your starting

    time is zero is basically what we meant time is zero is basically what we meant
    time is zero is basically what we meant

    here. So you can also sort of imagine this So you can also sort of imagine this

    thing to be like say I am standing on thing to be like say I am standing on thing
    to be like say I am standing on

    the shore of the river over here and the shore of the river over here and the
    shore of the river over here and

    then I''m trying to observe the duck then I''m trying to observe the duck then
    I''m trying to observe the duck

    getting jumped and basically what this getting jumped and basically what this
    getting jumped and basically what this

    is saying is that I can be standing at is saying is that I can be standing at
    is saying is that I can be standing at

    here or I can be standing at here. It here or I can be standing at here. It here
    or I can be standing at here. It

    doesn''t really matter. As long as the doesn''t really matter. As long as the
    doesn''t really matter. As long as the

    duck that I put in here is following the duck that I put in here is following
    the duck that I put in here is following the

    flow until it gets here and then do the flow until it gets here and then do the
    flow until it gets here and then do the

    jumping, they should end up at the same'
  concept_slugs:
  - consistency-models
  - rectified-flow
- idx: 72
  start_sec: 3597.43
  end_sec: 3659.109
  text: 'jumping, they should end up at the same jumping, they should end up at the
    same

    place. So, as long as they''re following place. So, as long as they''re following
    place. So, as long as they''re following

    the same flow, they should go to the the same flow, they should go to the the
    same flow, they should go to the

    same place. same place. same place.

    Does it make sense? Okay, cool. Okay, cool.

    one one interesting thing is that one one interesting thing is that one one interesting
    thing is that

    Orurian flow map has a very very uh Orurian flow map has a very very uh Orurian
    flow map has a very very uh

    famous member and it''s called Meanflow. famous member and it''s called Meanflow.
    famous member and it''s called Meanflow.

    Uh so Meanflow was developed by this Uh so Meanflow was developed by this Uh so
    Meanflow was developed by this

    like very famous lab in uh in MIT. So like very famous lab in uh in MIT. So like
    very famous lab in uh in MIT. So

    the PI in the lab is the guy who the PI in the lab is the guy who the PI in the
    lab is the guy who

    invented ResNet basically that''s why invented ResNet basically that''s why invented
    ResNet basically that''s why

    it''s very famous. It''s a legendary guy it''s very famous. It''s a legendary
    guy it''s very famous. It''s a legendary guy

    basically. one of the gods. His name is basically. one of the gods. His name is
    basically. one of the gods. His name is

    Kaiming. Uh and actually the first Kaiming. Uh and actually the first Kaiming.
    Uh and actually the first

    author is my labmate. His name is author is my labmate. His name is author is
    my labmate. His name is

    Chungyang. Legendary guy too. Anyway, uh Chungyang. Legendary guy too. Anyway,
    uh Chungyang. Legendary guy too. Anyway, uh

    the point being uh so basically what the point being uh so basically what the
    point being uh so basically what

    meanflow is saying is that ah so we know meanflow is saying is that ah so we know
    meanflow is saying is that ah so we know

    that well they they actually didn''t that well they they actually didn''t that
    well they they actually didn''t

    really mention the flow map thing in'
  concept_slugs:
  - consistency-models
  - rectified-flow
- idx: 73
  start_sec: 3659.109
  end_sec: 3703.92
  text: 'really mention the flow map thing in really mention the flow map thing in

    their in their paper. We by we I mean their in their paper. We by we I mean their
    in their paper. We by we I mean

    one of my paper actually proved that one of my paper actually proved that one
    of my paper actually proved that

    they''re or flow map but doesn''t matter. they''re or flow map but doesn''t matter.
    they''re or flow map but doesn''t matter.

    The point being um like so what they''re The point being um like so what they''re
    The point being um like so what they''re

    doing here is that uh so like we''re like doing here is that uh so like we''re
    like doing here is that uh so like we''re like

    to in order to jump right in order to do to in order to jump right in order to
    do to in order to jump right in order to do

    the jump that we want uh we are actually the jump that we want uh we are actually
    the jump that we want uh we are actually

    trying to learn a trying to learn a trying to learn a

    velocity here. So that''s why they name velocity here. So that''s why they name
    velocity here. So that''s why they name

    it mean flow because it''s the mean of it mean flow because it''s the mean of
    it mean flow because it''s the mean of

    the velocity right why is the average the velocity right why is the average the
    velocity right why is the average

    velocity is because like so this is like velocity is because like so this is like
    velocity is because like so this is like

    the total displacement that you''re going the total displacement that you''re
    going the total displacement that you''re going

    to get from your uh h integration right to get from your uh h integration right
    to get from your uh h integration right

    and this is equivalent to how many time and this is equivalent to how many time
    and this is equivalent to how many time

    that you''re skipping and what is the that you''re skipping and what is the that
    you''re skipping and what is the

    displacement that you''re predicting displacement that you''re predicting'
  concept_slugs:
  - consistency-models
  - rectified-flow
- idx: 74
  start_sec: 3703.92
  end_sec: 3756.15
  text: 'displacement that you''re predicting

    right so this is like so the right so this is like so the right so this is like
    so the

    displacement that you''re predicting is displacement that you''re predicting is
    displacement that you''re predicting is

    literally your literally your literally your

    mean like the average velocity mean like the average velocity mean like the average
    velocity

    So the mean flow right. So what we do So the mean flow right. So what we do So
    the mean flow right. So what we do

    here is essentially if you take the if here is essentially if you take the if
    here is essentially if you take the if

    you differentiate through both because you differentiate through both because
    you differentiate through both because

    we have a in integral here. So this we have a in integral here. So this we have
    a in integral here. So this

    integral is kind of getting in the way integral is kind of getting in the way
    integral is kind of getting in the way

    of all the analysis we''re going to do. of all the analysis we''re going to do.
    of all the analysis we''re going to do.

    So we just get rid of the integral we So we just get rid of the integral we So
    we just get rid of the integral we

    get we get uh so so we take derivative get we get uh so so we take derivative
    get we get uh so so we take derivative

    differentiate both sides and then we''re differentiate both sides and then we''re
    differentiate both sides and then we''re

    going to get this thing. And then if you going to get this thing. And then if
    you going to get this thing. And then if you

    rearrange the term, you''re going to get rearrange the term, you''re going to
    get rearrange the term, you''re going to get

    basically your average velocity. It''s basically your average velocity. It''s
    basically your average velocity. It''s

    equal to your instantaneous velocity equal to your instantaneous velocity equal
    to your instantaneous velocity

    minus the time the time difference times minus the time the time difference times
    minus the time the time difference times

    the time derivative. So this is what the time derivative. So this is what the
    time derivative. So this is what

    they call a mean flow identity.'
  concept_slugs:
  - consistency-models
  - rectified-flow
- idx: 75
  start_sec: 3756.15
  end_sec: 3811.599
  text: 'they call a mean flow identity. they call a mean flow identity.

    Okay, that does it make sense for people? that does it make sense for people?

    Good. Okay. So why is mean flow a oiler Good. Okay. So why is mean flow a oiler
    Good. Okay. So why is mean flow a oiler

    flow map? Let''s look at it. Well, this flow map? Let''s look at it. Well, this
    flow map? Let''s look at it. Well, this

    is mean flow identity written in the is mean flow identity written in the is mean
    flow identity written in the

    flow matching term. The before they were flow matching term. The before they were
    flow matching term. The before they were

    using diffusion convention. So zero is using diffusion convention. So zero is
    using diffusion convention. So zero is

    data, one is noise. Here zero is noise, data, one is noise. Here zero is noise,
    data, one is noise. Here zero is noise,

    one is data. Okay. And then what you can one is data. Okay. And then what you
    can one is data. Okay. And then what you can

    do is you can just expand the total do is you can just expand the total do is
    you can just expand the total

    derivative into all the partials. Then derivative into all the partials. Then
    derivative into all the partials. Then

    you get this. And then you basically you get this. And then you basically you
    get this. And then you basically

    just uh rearrange the term. and then you just uh rearrange the term. and then
    you just uh rearrange the term. and then you

    rearrange more terms and then you rearrange more terms and then you rearrange
    more terms and then you

    rearrange more terms and then you''ll get rearrange more terms and then you''ll
    get rearrange more terms and then you''ll get

    exactly the oran condition back from exactly the oran condition back from exactly
    the oran condition back from

    your mean flow identity. So the point is your mean flow identity. So the point
    is your mean flow identity. So the point is

    mean flow identity equals oran condition mean flow identity equals oran condition
    mean flow identity equals oran condition

    that''s it. Um and one nice thing about that''s it. Um and one nice thing about'
  concept_slugs:
  - consistency-models
  - rectified-flow
- idx: 76
  start_sec: 3811.599
  end_sec: 3887.599
  text: 'that''s it. Um and one nice thing about

    the mean flow identity is that uh so in the mean flow identity is that uh so in
    the mean flow identity is that uh so in

    the middle here if you take s equals t the middle here if you take s equals t
    the middle here if you take s equals t

    or when t is approaching s I guess uh or when t is approaching s I guess uh or
    when t is approaching s I guess uh

    then this whole thing so this this whole then this whole thing so this this whole
    then this whole thing so this this whole

    this first part will cancel out. So this first part will cancel out. So this first
    part will cancel out. So

    you''re just going to get u xt equals you''re just going to get u xt equals you''re
    just going to get u xt equals

    vxt. So you uh immediately uh satisfy vxt. So you uh immediately uh satisfy vxt.
    So you uh immediately uh satisfy

    the tangent condition automatically. You the tangent condition automatically.
    You the tangent condition automatically. You

    don''t even need another loss term here. don''t even need another loss term here.
    don''t even need another loss term here.

    Okay. Any question? All right. So if you think about it, All right. So if you
    think about it,

    right, the the the the CTM is actually right, the the the the CTM is actually
    right, the the the the CTM is actually

    sort of Oiler, right? Because we''re sort of Oiler, right? Because we''re sort
    of Oiler, right? Because we''re

    matching endpoints here, right? matching endpoints here, right? matching endpoints
    here, right?

    Essentially, we''re we''re sort of Essentially, we''re we''re sort of Essentially,
    we''re we''re sort of

    matching endpoints. Does it make sense? So it''s kind of Does it make sense? So
    it''s kind of

    giving or in here. And more importantly, giving or in here. And more importantly,
    giving or in here. And more importantly,

    the score matching loss is literally the score matching loss is literally the
    score matching loss is literally

    just tangent condition. So this is why just tangent condition. So this is why
    just tangent condition. So this is why

    like but an interesting thing is that like but an interesting thing is that'
  concept_slugs:
  - consistency-models
  - rectified-flow
- idx: 77
  start_sec: 3887.599
  end_sec: 3943.039
  text: 'like but an interesting thing is that

    CTN was developed in 2023 CTN was developed in 2023 CTN was developed in 2023

    and um the the how to train your like and um the the how to train your like and
    um the the how to train your like

    the how to train a flow map uh paper was the how to train a flow map uh paper
    was the how to train a flow map uh paper was

    like new earth last year or something so like new earth last year or something
    so like new earth last year or something so

    new 2025. So essentially it takes a new 2025. So essentially it takes a new 2025.
    So essentially it takes a

    while for people to you know come up while for people to you know come up while
    for people to you know come up

    with like a generalizable framework for with like a generalizable framework for
    with like a generalizable framework for

    all the things that works um like that all the things that works um like that
    all the things that works um like that

    that has like um like slightly Yeah. that has like um like slightly Yeah. that
    has like um like slightly Yeah.

    Yeah. But basically this is like yeah so Yeah. But basically this is like yeah
    so Yeah. But basically this is like yeah so

    now you can generalize CT ctm to the now you can generalize CT ctm to the now
    you can generalize CT ctm to the

    flow mapap framework as well. cool. All right so let''s look at the cool. All
    right so let''s look at the

    most intuitive. I think this is the most most intuitive. I think this is the most
    most intuitive. I think this is the most

    intuitive one. I know that max said that intuitive one. I know that max said that
    intuitive one. I know that max said that

    lrangeian is the most intuitive one. I lrangeian is the most intuitive one. I
    lrangeian is the most intuitive one. I

    have no idea how his intuition works. I have no idea how his intuition works.
    I have no idea how his intuition works. I

    think this is the most intuitive one. So think this is the most intuitive one.
    So'
  concept_slugs:
  - consistency-models
  - rectified-flow
- idx: 78
  start_sec: 3943.039
  end_sec: 4004.319
  text: 'think this is the most intuitive one. So

    this is literally just saying that uh this is literally just saying that uh this
    is literally just saying that uh

    basically if your flow map jump from S basically if your flow map jump from S
    basically if your flow map jump from S

    to U and then U to T, it should be the to U and then U to T, it should be the
    to U and then U to T, it should be the

    same as jumping from S to T directly. So same as jumping from S to T directly.
    So same as jumping from S to T directly. So

    taking two jumps is equivalent to taking taking two jumps is equivalent to taking
    taking two jumps is equivalent to taking

    one large jump, super intuitive in my opinion. Um but super intuitive in my opinion.
    Um but

    basically yeah so what you''re doing is basically yeah so what you''re doing is
    basically yeah so what you''re doing is

    like basically you can either do one like basically you can either do one like
    basically you can either do one

    large jump or you can take a break in large jump or you can take a break in large
    jump or you can take a break in

    the middle and then jump again and then the middle and then jump again and then
    the middle and then jump again and then

    your flow map should match the same your flow map should match the same your flow
    map should match the same

    point whether you''re taking one jump or point whether you''re taking one jump
    or point whether you''re taking one jump or

    two jumps. two jumps. two jumps.

    Yeah. So this is why they call it like Yeah. So this is why they call it like
    Yeah. So this is why they call it like

    progressive something something as well. progressive something something as well.
    progressive something something as well.

    Yeah. Cool. Cool.

    No question. Okay. So for those of you who are in Okay. So for those of you who
    are in

    robotics, you may have seen this model. robotics, you may have seen this model.
    robotics, you may have seen this model.

    How many any of you guys have seen this How many any of you guys have seen this'
  concept_slugs:
  - consistency-models
  - rectified-flow
- idx: 79
  start_sec: 4004.319
  end_sec: 4053.599
  text: 'How many any of you guys have seen this

    model? Shortcut model. No one. No. I model? Shortcut model. No one. No. I model?
    Shortcut model. No one. No. I

    think this is a Peter Ail or something. think this is a Peter Ail or something.
    think this is a Peter Ail or something.

    I don''t know. Anyway, uh not in the I don''t know. Anyway, uh not in the I don''t
    know. Anyway, uh not in the

    point is uh so basically there this point is uh so basically there this point
    is uh so basically there this

    robotics lab in Berkeley. I believe it''s robotics lab in Berkeley. I believe
    it''s robotics lab in Berkeley. I believe it''s

    Peterville, Peterville, Peterville,

    but I can''t distinguish between Peter but I can''t distinguish between Peter
    but I can''t distinguish between Peter

    Peterville and Sergey Leavine, so it Peterville and Sergey Leavine, so it Peterville
    and Sergey Leavine, so it

    could be either of them. could be either of them. could be either of them.

    Yeah, actually I''m not sure anymore. Yeah, actually I''m not sure anymore. Yeah,
    actually I''m not sure anymore.

    Anyway, not important. The point being Anyway, not important. The point being
    Anyway, not important. The point being

    uh like so basically they developed this uh like so basically they developed this
    uh like so basically they developed this

    uh method like the this self uh method like the this self uh method like the this
    self

    distillation method if you will and distillation method if you will and distillation
    method if you will and

    their training is actually um can be their training is actually um can be their
    training is actually um can be

    separated into two parts. Uh so the separated into two parts. Uh so the separated
    into two parts. Uh so the

    first part is what they call they do first part is what they call they do first
    part is what they call they do

    flow matching just normal flow matching flow matching just normal flow matching
    flow matching just normal flow matching

    training and this is literally just training and this is literally just training
    and this is literally just

    making sure that your flow oh my god I''m making sure that your flow oh my god
    I''m'
  concept_slugs:
  - consistency-models
  - rectified-flow
- idx: 80
  start_sec: 4053.599
  end_sec: 4111.199
  text: 'making sure that your flow oh my god I''m

    so sorry we''re running out of time but so sorry we''re running out of time but
    so sorry we''re running out of time but

    let''s get let''s finish everything uh the let''s get let''s finish everything
    uh the let''s get let''s finish everything uh the

    to make sure that your tangent condition to make sure that your tangent condition
    to make sure that your tangent condition

    holds for your model and then the second holds for your model and then the second
    holds for your model and then the second

    part is literally just like making sure part is literally just like making sure
    part is literally just like making sure

    that your semigroup property holds. making sure that your uh your making making
    sure that your uh your making

    sure that your your your semi-roup sure that your your your semi-roup sure that
    your your your semi-roup

    property holds. Uh yeah, and that''s property holds. Uh yeah, and that''s property
    holds. Uh yeah, and that''s

    pretty much it. pretty much it. pretty much it.

    Okay, any question? I guess no question. Okay, any question? I guess no question.
    Okay, any question? I guess no question.

    Okay, we''re going to just Yeah, feel Okay, we''re going to just Yeah, feel Okay,
    we''re going to just Yeah, feel

    free to go if you need to, but we''re free to go if you need to, but we''re free
    to go if you need to, but we''re

    going to like just finish everything. Um going to like just finish everything.
    Um going to like just finish everything. Um

    so yeah is flowmat perfect now? No. Why so yeah is flowmat perfect now? No. Why
    so yeah is flowmat perfect now? No. Why

    is because uh so the likelihood is because uh so the likelihood is because uh
    so the likelihood

    evaluation is actually still very very evaluation is actually still very very
    evaluation is actually still very very

    slow right because we''re only learning slow right because we''re only learning
    slow right because we''re only learning

    the displacement in sampling and not in the displacement in sampling and not in
    the displacement in sampling and not in

    likelihood. Uh so why why is that? Well, likelihood. Uh so why why is that? Well,'
  concept_slugs:
  - consistency-models
  - rectified-flow
- idx: 81
  start_sec: 4111.199
  end_sec: 4153.04
  text: 'likelihood. Uh so why why is that? Well,

    it''s basically because yeah because it''s it''s basically because yeah because
    it''s it''s basically because yeah because it''s

    only jump to in the sampling space and only jump to in the sampling space and
    only jump to in the sampling space and

    completely forget about likelihood. So completely forget about likelihood. So
    completely forget about likelihood. So

    in order to calculate the likelihood we in order to calculate the likelihood we
    in order to calculate the likelihood we

    still need to take the instantaneous still need to take the instantaneous still
    need to take the instantaneous

    divergence of divergence of divergence of

    the OD and then do numerical integration the OD and then do numerical integration
    the OD and then do numerical integration

    which takes like 100 to thousand steps which takes like 100 to thousand steps
    which takes like 100 to thousand steps

    and that''s like very slow but what you and that''s like very slow but what you
    and that''s like very slow but what you

    can actually do is if you think about it can actually do is if you think about
    it can actually do is if you think about it

    uh you know calculate like sampling is uh you know calculate like sampling is
    uh you know calculate like sampling is

    solving an OD uh uh solving the log solving an OD uh uh solving the log solving
    an OD uh uh solving the log

    likelihood is also solving OD. So why likelihood is also solving OD. So why likelihood
    is also solving OD. So why

    can''t you just like you know use the can''t you just like you know use the can''t
    you just like you know use the

    same flow map trick and solve another OD same flow map trick and solve another
    OD same flow map trick and solve another OD

    right so if you''re solving the sampling right so if you''re solving the sampling
    right so if you''re solving the sampling

    OD if you know how to sample one OD you OD if you know how to sample one OD you
    OD if you know how to sample one OD you

    can use the same algorithms to solve can use the same algorithms to solve'
  concept_slugs:
  - consistency-models
  - rectified-flow
- idx: 82
  start_sec: 4153.04
  end_sec: 4193.199
  text: 'can use the same algorithms to solve

    another OD right so this is what we''re another OD right so this is what we''re
    another OD right so this is what we''re

    doing so this is like my new paper doing so this is like my new paper doing so
    this is like my new paper

    actually uh oh another thing is that if actually uh oh another thing is that if
    actually uh oh another thing is that if

    you can solve two separate ODEs and you can solve two separate ODEs and you can
    solve two separate ODEs and

    these two separate OD''s are actually can these two separate OD''s are actually
    can these two separate OD''s are actually can

    be like coupled into a OD system then be like coupled into a OD system then be
    like coupled into a OD system then

    you can literally just use the same you can literally just use the same you can
    literally just use the same

    technique to solve this coupled the technique to solve this coupled the technique
    to solve this coupled the

    system of OD, right? Uh so just learn to system of OD, right? Uh so just learn
    to system of OD, right? Uh so just learn to

    jump together essentially in both the jump together essentially in both the jump
    together essentially in both the

    sampling trajectory and the log sampling trajectory and the log sampling trajectory
    and the log

    likelihood trajectory or the divergence likelihood trajectory or the divergence
    likelihood trajectory or the divergence

    trajectory, right? So essentially what trajectory, right? So essentially what
    trajectory, right? So essentially what

    you do is literally you just this is our you do is literally you just this is
    our you do is literally you just this is our

    new paper from iclair. Uh so you can new paper from iclair. Uh so you can new
    paper from iclair. Uh so you can

    literally just like the the the main literally just like the the the main literally
    just like the the the main

    moral of the story here is that you can moral of the story here is that you can
    moral of the story here is that you can

    use the same full map method to distill use the same full map method to distill'
  concept_slugs:
  - consistency-models
  - rectified-flow
- idx: 83
  start_sec: 4193.199
  end_sec: 4240.95
  text: 'use the same full map method to distill

    any OD. So if you have like you know an any OD. So if you have like you know an
    any OD. So if you have like you know an

    interesting OD that is associated with interesting OD that is associated with
    interesting OD that is associated with

    your diffusion model and you want to your diffusion model and you want to your
    diffusion model and you want to

    distill you can use flow map because distill you can use flow map because distill
    you can use flow map because

    they''re like pretty you because this is they''re like pretty you because this
    is they''re like pretty you because this is

    a method for OD. Okay cool. So like how a method for OD. Okay cool. So like how
    a method for OD. Okay cool. So like how

    do you train a joint uh distillation do you train a joint uh distillation do you
    train a joint uh distillation

    method? Literally you just need to make method? Literally you just need to make
    method? Literally you just need to make

    sure that it''s a valid flow map for both sure that it''s a valid flow map for
    both sure that it''s a valid flow map for both

    sampling and likelihood and that''s it. sampling and likelihood and that''s it.
    sampling and likelihood and that''s it.

    Okay. Uh so now we''re done with the Okay. Uh so now we''re done with the Okay.
    Uh so now we''re done with the

    state-of-the-art method. Uh weeks can state-of-the-art method. Uh weeks can state-of-the-art
    method. Uh weeks can

    well not really done. We have one more well not really done. We have one more
    well not really done. We have one more

    uh guest lectures next class from Alex uh guest lectures next class from Alex
    uh guest lectures next class from Alex

    in Luma AI and we shall have pizza in in Luma AI and we shall have pizza in in
    Luma AI and we shall have pizza in

    person. Let''s hope. Um but basically person. Let''s hope. Um but basically person.
    Let''s hope. Um but basically

    Alex uh is a research scientist at Luma. Alex uh is a research scientist at Luma.
    Alex uh is a research scientist at Luma.

    He was a PhD student at Stanford. Uh he'
  concept_slugs:
  - consistency-models
  - rectified-flow
- idx: 84
  start_sec: 4240.95
  end_sec: 4276.679
  text: 'He was a PhD student at Stanford. Uh he He was a PhD student at Stanford.
    Uh he

    co-founded something and then got co-founded something and then got co-founded
    something and then got

    acquired by Luma. So that''s how he got acquired by Luma. So that''s how he got
    acquired by Luma. So that''s how he got

    there. Uh but but basically he''s the there. Uh but but basically he''s the there.
    Uh but but basically he''s the

    thing that he''s going to be talking thing that he''s going to be talking thing
    that he''s going to be talking

    about is going to be very very very about is going to be very very very about
    is going to be very very very

    closely related from what we learned closely related from what we learned closely
    related from what we learned

    today. and you should ask questions like today. and you should ask questions like
    today. and you should ask questions like

    basically I don''t think he''s going to basically I don''t think he''s going to
    basically I don''t think he''s going to

    position his talk like from the full map position his talk like from the full
    map position his talk like from the full map

    perspective. So, make sure to ask him perspective. So, make sure to ask him perspective.
    So, make sure to ask him

    questions about, oh, how do you think questions about, oh, how do you think questions
    about, oh, how do you think

    your thing connect to this other thing? your thing connect to this other thing?
    your thing connect to this other thing?

    Right? That would be interesting things Right? That would be interesting things
    Right? That would be interesting things

    to ask. Okay, that''s it for the class. to ask. Okay, that''s it for the class.
    to ask. Okay, that''s it for the class.

    Sorry that we''re running a little bit Sorry that we''re running a little bit
    Sorry that we''re running a little bit

    late, but uh yeah, see you uh on late, but uh yeah, see you uh on late, but uh
    yeah, see you uh on

    Thursday.'
  concept_slugs:
  - consistency-models
  - rectified-flow
---
# CMU 10799 S26: Lecture 10 - Distillation, Consistency Models & Flow Maps - Diffusion & Flow Matching

See the structured chunks above.
