---
course_slug: diffusion-principles-vizuara
idx: 1
title: Lecture 10 - Constructing Training Target for Flow Models | Principles of Diffusion
  Models
video_url: https://www.youtube.com/watch?v=JyblttMM9-c
duration_sec: null
chunks:
- idx: 0
  start_sec: 4.95
  end_sec: 87.04
  text: 'Hello everyone and welcome to the next Hello everyone and welcome to the
    next

    lecture of the course principles of lecture of the course principles of lecture
    of the course principles of

    diffusion models. diffusion models. diffusion models.

    In the last lecture we started by In the last lecture we started by In the last
    lecture we started by

    introducing flow models. introducing flow models. introducing flow models.

    In particular we first understood the In particular we first understood the In
    particular we first understood the

    meaning of flow itself and later we meaning of flow itself and later we meaning
    of flow itself and later we

    moved on to understanding what is the moved on to understanding what is the moved
    on to understanding what is the

    meaning of flow modeling. meaning of flow modeling. meaning of flow modeling.

    Let us do a brief recap. Let us do a brief recap. Let us do a brief recap.

    of what we covered in the last lecture. of what we covered in the last lecture.
    of what we covered in the last lecture.

    Before we move ahead to this lecture, and this box includes a lot of tiny and
    this box includes a lot of tiny

    particles. particles. particles.

    So this is particle P1. Let''s focus on So this is particle P1. Let''s focus on
    So this is particle P1. Let''s focus on

    that particle. that particle. that particle.

    Now imagine that for some reason these Now imagine that for some reason these
    Now imagine that for some reason these

    particles are moving inside the box. particles are moving inside the box. particles
    are moving inside the box.

    So the particles are following specific So the particles are following specific
    So the particles are following specific

    trajectories. trajectories. trajectories.

    For example, this is the trajectory For example, this is the trajectory For example,
    this is the trajectory

    which is followed by P1. Then we take another point P2 Then we take another point
    P2

    and we find that this is the trajectory and we find that this is the trajectory
    and we find that this is the trajectory

    which is followed by the point P2. which is followed by the point P2. which is
    followed by the point P2.

    Similarly, every single point in the box Similarly, every single point in the
    box'
  concept_slugs:
  - flow-matching
  - velocity-field
- idx: 1
  start_sec: 87.04
  end_sec: 169.11
  text: 'Similarly, every single point in the box

    is following a specific trajectory is following a specific trajectory is following
    a specific trajectory

    and the particles are moving as and the particles are moving as and the particles
    are moving as

    [clears throat] time is progressing [clears throat] time is progressing [clears
    throat] time is progressing

    ahead. ahead. ahead.

    You can imagine this to be like a fluid You can imagine this to be like a fluid
    You can imagine this to be like a fluid

    which is moving with time. which is moving with time. which is moving with time.

    [snorts] Okay. Now [snorts] Okay. Now [snorts] Okay. Now

    we ask a simple question. What is making these particles move What is making these
    particles move

    according to the specific trajectories? For example, For example,

    at every point, at every point, at every point,

    [snorts] we know that there is a [snorts] we know that there is a [snorts] we
    know that there is a

    velocity vector which is causing the velocity vector which is causing the velocity
    vector which is causing the

    particle to move in that direction. >> [snorts] >> [snorts]

    >> So we try to think about >> So we try to think about >> So we try to think
    about

    what is what is responsible for the what is what is responsible for the what is
    what is responsible for the

    trajectories of the particles to behave trajectories of the particles to behave
    trajectories of the particles to behave

    in a certain way. in a certain way. in a certain way.

    It''s almost like a detective who is It''s almost like a detective who is It''s
    almost like a detective who is

    trying to find out the reason behind a trying to find out the reason behind a
    trying to find out the reason behind a

    mysterious behavior. mysterious behavior. mysterious behavior.

    Now our detective tells us that the Now our detective tells us that the Now our
    detective tells us that the

    reason the particles move in this way is reason the particles move in this way
    is reason the particles move in this way is

    because because because

    there is a velocity field which is there is a velocity field which is there is
    a velocity field which is

    changing changing changing

    with not just space but it is changing'
  concept_slugs:
  - flow-matching
  - velocity-field
- idx: 2
  start_sec: 169.11
  end_sec: 224.71
  text: 'with not just space but it is changing with not just space but it is changing

    with time also. [snorts] Why it is with time also. [snorts] Why it is with time
    also. [snorts] Why it is

    changing with space? It''s because the changing with space? It''s because the
    changing with space? It''s because the

    trajectories for all all the particles trajectories for all all the particles
    trajectories for all all the particles

    in the box are different. So it has to in the box are different. So it has to
    in the box are different. So it has to

    change with space. change with space. change with space.

    Well, it is not completely necessary Well, it is not completely necessary Well,
    it is not completely necessary

    that it changes with time as well. But that it changes with time as well. But
    that it changes with time as well. But

    we''ll consider a more general case where we''ll consider a more general case
    where we''ll consider a more general case where

    the velocity field [snorts] which is the the velocity field [snorts] which is
    the the velocity field [snorts] which is the

    culprit which the the detective has culprit which the the detective has culprit
    which the the detective has

    found out is changing with both space found out is changing with both space found
    out is changing with both space

    and with time as well. [snorts] and with time as well. [snorts] and with time
    as well. [snorts]

    Let us denote this velocity field as u Let us denote this velocity field as u
    Let us denote this velocity field as u

    of of of

    x t. x t. x t.

    [snorts] The detective has done its job. The The detective has done its job. The

    detective has found that uh there is a detective has found that uh there is a
    detective has found that uh there is a

    velocity field which is um responsible velocity field which is um responsible
    velocity field which is um responsible

    for the movement of the trajectories or for the movement of the trajectories or
    for the movement of the trajectories or

    the movement of the particles and the the movement of the particles and the the
    movement of the particles and the

    generation of these trajectories. generation of these trajectories. generation
    of these trajectories.

    Now we approach another person. Let''s'
  concept_slugs:
  - flow-matching
  - velocity-field
- idx: 3
  start_sec: 224.71
  end_sec: 276.31
  text: 'Now we approach another person. Let''s Now we approach another person. Let''s

    call that person uh detective number call that person uh detective number call
    that person uh detective number

    two. And we ask the question well uh two. And we ask the question well uh two.
    And we ask the question well uh

    let''s say I give you a velocity field. let''s say I give you a velocity field.
    let''s say I give you a velocity field.

    [snorts] [snorts] [snorts]

    Can you tell me the trajectories of all Can you tell me the trajectories of all
    Can you tell me the trajectories of all

    the particles in the box and how exactly the particles in the box and how exactly
    the particles in the box and how exactly

    they will move? they will move? they will move?

    The detective thinks and says um okay so The detective thinks and says um okay
    so The detective thinks and says um okay so

    this looks like a different problem now this looks like a different problem now
    this looks like a different problem now

    that you have used the services of that you have used the services of that you
    have used the services of

    detective one and understood that there detective one and understood that there
    detective one and understood that there

    is an underlying velocity field which is is an underlying velocity field which
    is is an underlying velocity field which is

    responsible for the movement of these responsible for the movement of these responsible
    for the movement of these

    particles now you''re trying to find out particles now you''re trying to find
    out particles now you''re trying to find out

    [snorts] given the velocity field can I [snorts] given the velocity field can
    I [snorts] given the velocity field can I

    generate the trajectory so essentially generate the trajectory so essentially
    generate the trajectory so essentially

    you''re trying to solve the reverse you''re trying to solve the reverse you''re
    trying to solve the reverse

    problem problem problem

    [snorts] uh so detective one first [snorts] uh so detective one first [snorts]
    uh so detective one first

    detective two thinks that okay initially detective two thinks that okay initially
    detective two thinks that okay initially

    These people are thinking about going These people are thinking about going These
    people are thinking about going

    from trajectories and then calculating'
  concept_slugs:
  - flow-matching
  - velocity-field
- idx: 4
  start_sec: 276.31
  end_sec: 364.829
  text: 'from trajectories and then calculating from trajectories and then calculating

    the velocity field. [snorts] Now they the velocity field. [snorts] Now they the
    velocity field. [snorts] Now they

    are thinking in the reverse way from are thinking in the reverse way from are
    thinking in the reverse way from

    given the velocity field can I calculate given the velocity field can I calculate
    given the velocity field can I calculate

    the trajectories of these particles. [snorts] The detective too remembers uh [snorts]
    The detective too remembers uh

    some of the some of the some of the

    theory he had learned in mathematics in theory he had learned in mathematics in
    theory he had learned in mathematics in

    college. and comes up with an ordinary college. and comes up with an ordinary
    college. and comes up with an ordinary

    differential equation and thinks that differential equation and thinks that differential
    equation and thinks that

    okay this is straightforward. We can okay this is straightforward. We can okay
    this is straightforward. We can

    simply write down dx of t of t

    dt dt dt

    is equal to u of x t. is equal to u of x t. is equal to u of x t.

    [snorts] [snorts]

    A simple differential equation which is A simple differential equation which is
    A simple differential equation which is

    an ordinary differential equation is an ordinary differential equation is an ordinary
    differential equation is

    written to written to written to

    [snorts] calculate the trajectories. [snorts] calculate the trajectories. [snorts]
    calculate the trajectories.

    But then how do we go from here to But then how do we go from here to But then
    how do we go from here to

    calculating the trajectories in the calculating the trajectories in the calculating
    the trajectories in the

    first place? Well, what you do is you first place? Well, what you do is you first
    place? Well, what you do is you

    discretise this discretise this discretise this

    by saying delta x by delta t is equal to by saying delta x by delta t is equal
    to by saying delta x by delta t is equal to

    mu of u of x t >> [snorts]

    >> So let''s say you start at >> So let''s say you start at >> So let''s say you
    start at

    x0 x0 x0

    which is a specific point in space.'
  concept_slugs:
  - flow-matching
  - velocity-field
- idx: 5
  start_sec: 364.829
  end_sec: 431.51
  text: 'which is a specific point in space. which is a specific point in space.

    [snorts] Let''s say this is x0. Now what is x1? X1 is equal to Now what is x1?
    X1 is equal to

    X0 + delta X X0 + delta X X0 + delta X

    and delta X can be written as and delta X can be written as and delta X can be
    written as

    delta T * delta T * delta T *

    U of the velocity at that point X0 and U of the velocity at that point X0 and
    U of the velocity at that point X0 and

    the initial time stamp. So let''s call it the initial time stamp. So let''s call
    it the initial time stamp. So let''s call it

    zero. zero. zero.

    So now you get X1. So now you get X1. So now you get X1.

    So the particle has moved from X0 to X1. So the particle has moved from X0 to
    X1. So the particle has moved from X0 to X1.

    Similarly, you can calculate x2 Similarly, you can calculate x2 Similarly, you
    can calculate x2

    x3 and you can get the entire trajectory x3 and you can get the entire trajectory
    x3 and you can get the entire trajectory

    of the particle. [snorts] of the particle. [snorts] of the particle. [snorts]

    Why are we doing this? Well, this means Why are we doing this? Well, this means
    Why are we doing this? Well, this means

    that if I know the velocity field and that if I know the velocity field and that
    if I know the velocity field and

    how it changes with space and time, I how it changes with space and time, I how
    it changes with space and time, I

    can exactly pinpoint the trajectories of can exactly pinpoint the trajectories
    of can exactly pinpoint the trajectories of

    all the single part all the particles in all the single part all the particles
    in all the single part all the particles in

    the box. the box. the box.

    So, okay fine. So, that is great. Now so So, okay fine. So, that is great. Now
    so So, okay fine. So, that is great. Now so

    far we have looked at individual far we have looked at individual far we have
    looked at individual

    particles. We have looked at their'
  concept_slugs:
  - flow-matching
  - velocity-field
- idx: 6
  start_sec: 431.51
  end_sec: 488.24
  text: 'particles. We have looked at their particles. We have looked at their

    trajectories. We have looked at the trajectories. We have looked at the trajectories.
    We have looked at the

    mysterious force that is causing these mysterious force that is causing these
    mysterious force that is causing these

    trajectories. Then we looked at the trajectories. Then we looked at the trajectories.
    Then we looked at the

    reverse problem. If we know this reverse problem. If we know this reverse problem.
    If we know this

    mysterious force, can we calculate the mysterious force, can we calculate the
    mysterious force, can we calculate the

    trajectories? And the answer is yes. trajectories? And the answer is yes. trajectories?
    And the answer is yes.

    Now let''s come to the main part of uh Now let''s come to the main part of uh
    Now let''s come to the main part of uh

    the discussion which is flow. And now the discussion which is flow. And now the
    discussion which is flow. And now

    once we understand this understanding once we understand this understanding once
    we understand this understanding

    flow is fairly straightforward. Flow is flow is fairly straightforward. Flow is
    flow is fairly straightforward. Flow is

    defined as a collection of the defined as a collection of the defined as a collection
    of the

    trajectories of all these particles. trajectories of all these particles. trajectories
    of all these particles.

    Every single particle moves in a certain Every single particle moves in a certain
    Every single particle moves in a certain

    way, right? So you aggregate the way, right? So you aggregate the way, right?
    So you aggregate the

    trajectories of all the particles and trajectories of all the particles and trajectories
    of all the particles and

    you call that to be flow. you call that to be flow. you call that to be flow.

    So it''s fairly intuitive what flow So it''s fairly intuitive what flow So it''s
    fairly intuitive what flow

    means. means. means.

    So a visual description of the flow for So a visual description of the flow for
    So a visual description of the flow for

    this same box would look as something this same box would look as something this
    same box would look as something

    like follows. like follows. like follows.

    you have uh all the particles following you have uh all the particles following
    you have uh all the particles following

    their trajectories their trajectories'
  concept_slugs:
  - flow-matching
  - velocity-field
- idx: 7
  start_sec: 488.24
  end_sec: 541.67
  text: 'their trajectories

    and you collect all these trajectories and you collect all these trajectories
    and you collect all these trajectories

    and you call them as a flow map or just and you call them as a flow map or just
    and you call them as a flow map or just

    flow. flow. flow.

    A very [snorts] intuitive way to A very [snorts] intuitive way to A very [snorts]
    intuitive way to

    visualize this is to um take a square visualize this is to um take a square visualize
    this is to um take a square

    grid, put the square grid on the box and grid, put the square grid on the box
    and grid, put the square grid on the box and

    then see how the square grid deforms then see how the square grid deforms then
    see how the square grid deforms

    with time. We actually saw this in the with time. We actually saw this in the
    with time. We actually saw this in the

    uh last lecture uh last lecture uh last lecture

    where uh the square grid is nothing but where uh the square grid is nothing but
    where uh the square grid is nothing but

    a representation of let''s say it''s a 4x4 a representation of let''s say it''s
    a 4x4 a representation of let''s say it''s a 4x4

    grid 16 points in space and then the grid 16 points in space and then the grid
    16 points in space and then the

    points deform but then you exactly see points deform but then you exactly see
    points deform but then you exactly see

    how the grid deforms with time. So it it how the grid deforms with time. So it
    it how the grid deforms with time. So it it

    helps you to visually understand what helps you to visually understand what helps
    you to visually understand what

    the flow is doing. Is it a spiral flow? the flow is doing. Is it a spiral flow?
    the flow is doing. Is it a spiral flow?

    Is it a flow which is um you know Is it a flow which is um you know Is it a flow
    which is um you know

    converging towards a sink etc. So you converging towards a sink etc. So you converging
    towards a sink etc. So you

    can get a fair idea about what the flow'
  concept_slugs:
  - flow-matching
  - velocity-field
- idx: 8
  start_sec: 541.67
  end_sec: 590.64
  text: 'can get a fair idea about what the flow can get a fair idea about what the
    flow

    is representing is representing is representing

    by by by

    having this square grid and having this square grid and having this square grid
    and

    understanding how individual points in understanding how individual points in
    understanding how individual points in

    this square grid are deforming with this square grid are deforming with this square
    grid are deforming with

    time. We saw a very nice example of this time. We saw a very nice example of this
    time. We saw a very nice example of this

    in the last lecture. Let me just show in the last lecture. Let me just show in
    the last lecture. Let me just show

    that to you. that to you. that to you.

    Yeah, we saw this example where this is Yeah, we saw this example where this is
    Yeah, we saw this example where this is

    the square grid. Imagine you immerse the the square grid. Imagine you immerse
    the the square grid. Imagine you immerse the

    square grid in the box and then see how square grid in the box and then see how
    square grid in the box and then see how

    it deforms with time. So [snorts] this it deforms with time. So [snorts] this
    it deforms with time. So [snorts] this

    is exactly how you can visualize the is exactly how you can visualize the is exactly
    how you can visualize the

    flow. flow.

    Okay. Now this is great. Uh we have Okay. Now this is great. Uh we have Okay.
    Now this is great. Uh we have

    understood what flow is. Now the understood what flow is. Now the understood what
    flow is. Now the

    question is what is the meaning of a question is what is the meaning of a question
    is what is the meaning of a

    flow model? [snorts] flow model? [snorts] flow model? [snorts]

    Uh and this this brings us to the whole Uh and this this brings us to the whole
    Uh and this this brings us to the whole

    objective of why we are focusing on flow objective of why we are focusing on flow
    objective of why we are focusing on flow

    flow models in the first place. So far flow models in the first place. So far'
  concept_slugs:
  - flow-matching
  - velocity-field
- idx: 9
  start_sec: 590.64
  end_sec: 647.92
  text: 'flow models in the first place. So far

    whatever we have discussed can be whatever we have discussed can be whatever we
    have discussed can be

    understood by a physics student easily understood by a physics student easily
    understood by a physics student easily

    with absolutely no background in AI or with absolutely no background in AI or
    with absolutely no background in AI or

    ML right because this is fairly ML right because this is fairly ML right because
    this is fairly

    intuitive stuff in the field of fluid intuitive stuff in the field of fluid intuitive
    stuff in the field of fluid

    mechanics or physics or [snorts] even mechanics or physics or [snorts] even mechanics
    or physics or [snorts] even

    basic for that matter. Now we relate basic for that matter. Now we relate basic
    for that matter. Now we relate

    this to the broader problem which we are this to the broader problem which we
    are this to the broader problem which we are

    trying to solve. Remember the broader trying to solve. Remember the broader trying
    to solve. Remember the broader

    problem that we are trying to solve is problem that we are trying to solve is
    problem that we are trying to solve is

    we want to calculate the probability we want to calculate the probability we want
    to calculate the probability

    distribution of the underlying data so distribution of the underlying data so
    distribution of the underlying data so

    that we can sample from it. So that we can sample from it. So that we can sample
    from it. So

    essentially we are in the domain of deep essentially we are in the domain of deep
    essentially we are in the domain of deep

    generative modeling. So [snorts] what we are trying to do So [snorts] what we
    are trying to do

    let''s say you are given images of cats let''s say you are given images of cats
    let''s say you are given images of cats

    you are given one to 100 images of cats you are given one to 100 images of cats
    you are given one to 100 images of cats

    and someone tells you and someone tells you and someone tells you

    okay generate a new image of a cat. okay generate a new image of a cat.'
  concept_slugs:
  - flow-matching
  - velocity-field
- idx: 10
  start_sec: 647.92
  end_sec: 710.8
  text: 'okay generate a new image of a cat.

    Now the way you solve this problem is Now the way you solve this problem is Now
    the way you solve this problem is

    you try to find a distribution you try to find a distribution you try to find
    a distribution

    which which which

    governs the behavior or the properties governs the behavior or the properties
    governs the behavior or the properties

    of all these images of cats and later of all these images of cats and later of
    all these images of cats and later

    you just sample from that distribution. So [snorts] the biggest challenge that
    So [snorts] the biggest challenge that

    we are trying to solve is we want to go we are trying to solve is we want to go
    we are trying to solve is we want to go

    from data to distribution which is not from data to distribution which is not
    from data to distribution which is not

    easy because we have absolutely no idea easy because we have absolutely no idea
    easy because we have absolutely no idea

    what the underlying distribution is what the underlying distribution is what the
    underlying distribution is

    going to look like. [snorts]

    Okay. Now uh we have seen how to solve Okay. Now uh we have seen how to solve
    Okay. Now uh we have seen how to solve

    this classes of problems. We have the this classes of problems. We have the this
    classes of problems. We have the

    first model which we used to solve this first model which we used to solve this
    first model which we used to solve this

    was variational autoenccoders. was variational autoenccoders. was variational
    autoenccoders.

    Then we looked at diffusion models which Then we looked at diffusion models which
    Then we looked at diffusion models which

    is another class of models to solve this is another class of models to solve this
    is another class of models to solve this

    problem. What typically happens in problem. What typically happens in problem.
    What typically happens in

    diffusion models is diffusion models is diffusion models is

    to find this distribution you start with to find this distribution you start with
    to find this distribution you start with

    a gshian distribution that is noise and a gshian distribution that is noise and'
  concept_slugs:
  - flow-matching
  - velocity-field
- idx: 11
  start_sec: 710.8
  end_sec: 775.43
  text: 'a gshian distribution that is noise and

    you end up with the actual distribution. you end up with the actual distribution.
    you end up with the actual distribution.

    So the path that we are going to follow So the path that we are going to follow
    So the path that we are going to follow

    here is that in in flow models is here is that in in flow models is here is that
    in in flow models is

    [snorts] [snorts]

    um we are going to assume that we have um we are going to assume that we have
    um we are going to assume that we have

    an initial distribution which is denoted an initial distribution which is denoted
    an initial distribution which is denoted

    by x of0 by x of0 by x of0

    which is given by pinet. which is given by pinet. which is given by pinet.

    This is the distribution that we are This is the distribution that we are This
    is the distribution that we are

    aware about. It is probably a gshian aware about. It is probably a gshian aware
    about. It is probably a gshian

    distribution which is uniformly distribution which is uniformly distribution which
    is uniformly

    distributed in space distributed in space distributed in space

    [snorts] and we want to end up [snorts] and we want to end up [snorts] and we
    want to end up

    at the distribution of the data that we at the distribution of the data that we
    at the distribution of the data that we

    want to predict. want to predict. want to predict.

    Here 0 represents the time step t=0 and Here 0 represents the time step t=0 and
    Here 0 represents the time step t=0 and

    1 represents the time t= 1. [snorts] So 1 represents the time t= 1. [snorts] So
    1 represents the time t= 1. [snorts] So

    we want to do something which changes we want to do something which changes we
    want to do something which changes

    the initial distribution to the final the initial distribution to the final the
    initial distribution to the final

    distribution. distribution. distribution.

    >> [snorts] >> [snorts]

    >> Now >> Now >> Now

    people thought of casting this problem people thought of casting this problem
    people thought of casting this problem

    in a way which is similar to how the'
  concept_slugs:
  - flow-matching
  - velocity-field
- idx: 12
  start_sec: 775.43
  end_sec: 840.8
  text: 'in a way which is similar to how the in a way which is similar to how the

    particles are moving in space and time. particles are moving in space and time.
    particles are moving in space and time.

    What do I mean by that? Well, imagine What do I mean by that? Well, imagine What
    do I mean by that? Well, imagine

    that that that

    your pinet which is the initial your pinet which is the initial your pinet which
    is the initial

    distribution distribution distribution

    is just given by a bunch of particles is just given by a bunch of particles is
    just given by a bunch of particles

    which are arranged uniformly which are arranged uniformly which are arranged uniformly

    symmetrically in space like this. symmetrically in space like this. symmetrically
    in space like this.

    uniform, completely uniform. uniform, completely uniform. uniform, completely
    uniform.

    And then you make these particles, let''s And then you make these particles, let''s
    And then you make these particles, let''s

    say there are thousand of these say there are thousand of these say there are
    thousand of these

    particles, you make these particles move particles, you make these particles move
    particles, you make these particles move

    in such a way that you change it to the distribution that you change it to the
    distribution that

    you want to predict. So this is a spiral you want to predict. So this is a spiral
    you want to predict. So this is a spiral

    distribution, let''s say. distribution, let''s say. distribution, let''s say.

    So let''s let''s look at a figure to So let''s let''s look at a figure to So let''s
    let''s look at a figure to

    understand this or a animation. So you understand this or a animation. So you
    understand this or a animation. So you

    see here we are initially starting with see here we are initially starting with
    see here we are initially starting with

    a gshian distribution and we slowly move a gshian distribution and we slowly move
    a gshian distribution and we slowly move

    to the distribution of a heart shape to the distribution of a heart shape to the
    distribution of a heart shape

    that we want to predict. that we want to predict. that we want to predict.

    So we are casting the deep generative So we are casting the deep generative'
  concept_slugs:
  - flow-matching
  - velocity-field
- idx: 13
  start_sec: 840.8
  end_sec: 905.04
  text: 'So we are casting the deep generative

    modeling problem modeling problem modeling problem

    as a problem where we are trying to as a problem where we are trying to as a problem
    where we are trying to

    predict the flow map from the initial predict the flow map from the initial predict
    the flow map from the initial

    distribution of the particles to the distribution of the particles to the distribution
    of the particles to the

    final distribution of the particles. final distribution of the particles. final
    distribution of the particles.

    [snorts] Now from the initial discussion [snorts] Now from the initial discussion
    [snorts] Now from the initial discussion

    we had your question might be okay how we had your question might be okay how
    we had your question might be okay how

    how do I generate this map in the first how do I generate this map in the first
    how do I generate this map in the first

    place? How do I generate this flow? And place? How do I generate this flow? And
    place? How do I generate this flow? And

    we just discussed that the trajectories we just discussed that the trajectories
    we just discussed that the trajectories

    of the particles of the particles of the particles

    completely depend on the velocity field. completely depend on the velocity field.
    completely depend on the velocity field.

    Right? So what if you write down the Right? So what if you write down the Right?
    So what if you write down the

    equation as dx by dt. equation as dx by dt. equation as dx by dt.

    Now here x represents the evolution of Now here x represents the evolution of
    Now here x represents the evolution of

    the probability field the probability field the probability field

    which is similar to the trajecolution of which is similar to the trajecolution
    of which is similar to the trajecolution of

    the trajectories followed by every the trajectories followed by every the trajectories
    followed by every

    single particle which are representing single particle which are representing
    single particle which are representing

    that field according to a that field according to a that field according to a

    velocity field which depends on x velocity field which depends on x velocity field
    which depends on x

    [snorts] and it depends on time as well. [snorts] and it depends on time as well.'
  concept_slugs:
  - flow-matching
  - velocity-field
- idx: 14
  start_sec: 905.04
  end_sec: 954.8
  text: '[snorts] and it depends on time as well.

    So this is exactly the same equation So this is exactly the same equation So this
    is exactly the same equation

    that we looked at before. that we looked at before. that we looked at before.

    Now this is something if we know this Now this is something if we know this Now
    this is something if we know this

    velocity field we can calculate exactly velocity field we can calculate exactly
    velocity field we can calculate exactly

    how the trajectories will move and we how the trajectories will move and we how
    the trajectories will move and we

    want to find the field which can take us want to find the field which can take
    us want to find the field which can take us

    from the initial distribution to the from the initial distribution to the from
    the initial distribution to the

    final data distribution. final data distribution. final data distribution.

    So [snorts] we have cast the problem of So [snorts] we have cast the problem of
    So [snorts] we have cast the problem of

    deep generative modeling into a problem deep generative modeling into a problem
    deep generative modeling into a problem

    where we want to predict the velocity where we want to predict the velocity where
    we want to predict the velocity

    field which governs the trajectories of field which governs the trajectories of
    field which governs the trajectories of

    these particles. these particles. these particles.

    Now this is exactly what is called as a Now this is exactly what is called as
    a Now this is exactly what is called as a

    flow model. The name is slightly misleading because The name is slightly misleading
    because

    I think this should be called as a I think this should be called as a I think
    this should be called as a

    velocity field model because in the end velocity field model because in the end
    velocity field model because in the end

    what people do is that they approximate what people do is that they approximate
    what people do is that they approximate

    this with a neural network and they try this with a neural network and they try
    this with a neural network and they try

    to predict this. So this is approximated to predict this. So this is approximated'
  concept_slugs:
  - flow-matching
  - velocity-field
- idx: 15
  start_sec: 954.8
  end_sec: 1016.959
  text: 'to predict this. So this is approximated

    by a neural network. by a neural network. by a neural network.

    Okay. And these are the conditions we Okay. And these are the conditions we Okay.
    And these are the conditions we

    want to satisfy. X of0 is the initial want to satisfy. X of0 is the initial want
    to satisfy. X of0 is the initial

    gshian distribution and we want to move gshian distribution and we want to move
    gshian distribution and we want to move

    to our actual data distribution. to our actual data distribution. to our actual
    data distribution.

    If you want to revise this properly, If you want to revise this properly, If you
    want to revise this properly,

    please go ahead and refer to the please go ahead and refer to the please go ahead
    and refer to the

    previous lecture where I have discussed previous lecture where I have discussed
    previous lecture where I have discussed

    this in complete detail. this in complete detail. this in complete detail.

    [snorts] [snorts]

    Okay. So, uh now the question is Okay. So, uh now the question is Okay. So, uh
    now the question is

    [snorts] [snorts]

    we want to simulate an OD which looks as we want to simulate an OD which looks
    as we want to simulate an OD which looks as

    follows. follows. follows.

    dxt by dt is equal to dxt by dt is equal to dxt by dt is equal to

    the velocity field the velocity field the velocity field

    >> [snorts] >> [snorts]

    >> uh at at that time and at the location >> uh at at that time and at the location
    >> uh at at that time and at the location

    in space. in space. in space.

    [snorts] Conceptually this looks [snorts] Conceptually this looks [snorts] Conceptually
    this looks

    excellent but the main question is that excellent but the main question is that
    excellent but the main question is that

    how do we go ahead and find this ideal how do we go ahead and find this ideal
    how do we go ahead and find this ideal

    velocity field that transports our velocity field that transports our velocity
    field that transports our

    initial probability distribution to the initial probability distribution to the
    initial probability distribution to the

    distribution that we want to predict in distribution that we want to predict in'
  concept_slugs:
  - flow-matching
  - velocity-field
- idx: 16
  start_sec: 1016.959
  end_sec: 1072.07
  text: 'distribution that we want to predict in

    the first place. the first place. the first place.

    And it turns out that this is at the end And it turns out that this is at the
    end And it turns out that this is at the end

    you will see this is very very easy and you will see this is very very easy and
    you will see this is very very easy and

    straightforward. straightforward. straightforward.

    But as I said in the first lecture we But as I said in the first lecture we But
    as I said in the first lecture we

    are going to take a path which is going are going to take a path which is going
    are going to take a path which is going

    to help us understand and appreciate the to help us understand and appreciate
    the to help us understand and appreciate the

    final easy formulation of this in a much final easy formulation of this in a much
    final easy formulation of this in a much

    better way. Okay. So the first thing that we think Okay. So the first thing that
    we think

    about is let''s say we u about is let''s say we u about is let''s say we u

    use a neural network to approximate this use a neural network to approximate this
    use a neural network to approximate this

    velocity field and we randomly velocity field and we randomly velocity field and
    we randomly

    initialize the parameters theta of the initialize the parameters theta of the
    initialize the parameters theta of the

    neural network. neural network. neural network.

    Well then the OD will just produce Well then the OD will just produce Well then
    the OD will just produce

    nonsense. You will start with a washian nonsense. You will start with a washian
    nonsense. You will start with a washian

    distribution but you might end up with distribution but you might end up with
    distribution but you might end up with

    something which is completely random. something which is completely random. something
    which is completely random.

    So you''re trying to flow the So you''re trying to flow the So you''re trying
    to flow the

    distribution in a specific way, right? distribution in a specific way, right?
    distribution in a specific way, right?

    But what if you start with a gshian'
  concept_slugs:
  - flow-matching
  - velocity-field
- idx: 17
  start_sec: 1072.07
  end_sec: 1125.029
  text: 'But what if you start with a gshian But what if you start with a gshian

    distribution and you end up with distribution and you end up with distribution
    and you end up with

    something that does not represent your something that does not represent your
    something that does not represent your

    data at all. So you can''t init randomly data at all. So you can''t init randomly
    data at all. So you can''t init randomly

    initialize the weights. initialize the weights. initialize the weights.

    This is where we come to the main This is where we come to the main This is where
    we come to the main

    concept in machine learning that we need concept in machine learning that we need
    concept in machine learning that we need

    a t we need a target to train our neural a t we need a target to train our neural
    a t we need a target to train our neural

    network. network. network.

    Now usually the target in let''s say Now usually the target in let''s say Now
    usually the target in let''s say

    supervised learning task is known to us. supervised learning task is known to
    us. supervised learning task is known to us.

    For example, if we are trying to uh For example, if we are trying to uh For example,
    if we are trying to uh

    predict predict predict

    the house prices which are going to the house prices which are going to the house
    prices which are going to

    change in the coming years. We generally change in the coming years. We generally
    change in the coming years. We generally

    use a regression model to solve this use a regression model to solve this use
    a regression model to solve this

    problem where we have a previous set of problem where we have a previous set of
    problem where we have a previous set of

    data and we extrapolate to understand data and we extrapolate to understand data
    and we extrapolate to understand

    what happens in the next 5 years. what happens in the next 5 years. what happens
    in the next 5 years.

    So the target is very clear. The target So the target is very clear. The target
    So the target is very clear. The target

    is the price of the house. In this case,'
  concept_slugs:
  - flow-matching
  - velocity-field
- idx: 18
  start_sec: 1125.029
  end_sec: 1182.96
  text: 'is the price of the house. In this case, is the price of the house. In this
    case,

    we want to minimize the loss function so we want to minimize the loss function
    so we want to minimize the loss function so

    that that

    the predicted velocity vector field the predicted velocity vector field the predicted
    velocity vector field

    matches the target velocity vector matches the target velocity vector matches
    the target velocity vector

    field. field. field.

    [snorts] All of us intuitively [snorts] All of us intuitively [snorts] All of
    us intuitively

    understand this. This is very similar to understand this. This is very similar
    to understand this. This is very similar to

    what we do in all types of machine what we do in all types of machine what we
    do in all types of machine

    learning problems where we are trying to learning problems where we are trying
    to learning problems where we are trying to

    predict the parameters of a network and predict the parameters of a network and
    predict the parameters of a network and

    there is a target which we are trying to there is a target which we are trying
    to there is a target which we are trying to

    match. So in most of the cases in match. So in most of the cases in match. So
    in most of the cases in

    supervised learning tasks this target is supervised learning tasks this target
    is supervised learning tasks this target is

    absolutely known to us. So it becomes absolutely known to us. So it becomes absolutely
    known to us. So it becomes

    easy to find the parameter so that the easy to find the parameter so that the
    easy to find the parameter so that the

    loss between our model and the target is loss between our model and the target
    is loss between our model and the target is

    minimized. minimized. minimized.

    Now as a mathematical formulation this Now as a mathematical formulation this
    Now as a mathematical formulation this

    looks very clean but let us come to the looks very clean but let us come to the
    looks very clean but let us come to the

    core problem. The core problem here is that predicting The core problem here is
    that predicting

    this target is not very easy. In fact we this target is not very easy. In fact
    we'
  concept_slugs:
  - flow-matching
  - velocity-field
- idx: 19
  start_sec: 1182.96
  end_sec: 1246.39
  text: 'this target is not very easy. In fact we

    have absolutely no idea what this target have absolutely no idea what this target
    have absolutely no idea what this target

    is. is. is.

    And that is going to be the focus of And that is going to be the focus of And
    that is going to be the focus of

    this lecture is to make it somewhat easy this lecture is to make it somewhat easy
    this lecture is to make it somewhat easy

    for us to identify this target. Now Now

    at the end you will see that the final at the end you will see that the final
    at the end you will see that the final

    training target is just a linear training target is just a linear training target
    is just a linear

    equation. It is very easy but we are equation. It is very easy but we are equation.
    It is very easy but we are

    going to take some time to come to that going to take some time to come to that
    going to take some time to come to that

    training target. training target. training target.

    So in this lecture our goal is to find So in this lecture our goal is to find
    So in this lecture our goal is to find

    an equation for the training target. an equation for the training target. an equation
    for the training target.

    Maybe we''ll not be able to complete it Maybe we''ll not be able to complete it
    Maybe we''ll not be able to complete it

    in this specific lecture but by the next in this specific lecture but by the next
    in this specific lecture but by the next

    lecture we will have the complete flow lecture we will have the complete flow
    lecture we will have the complete flow

    modeling pipeline ready. Before we get to the training target and Before we get
    to the training target and

    uh how we predict the training target, uh how we predict the training target,
    uh how we predict the training target,

    we need to understand some terminologies we need to understand some terminologies
    we need to understand some terminologies

    which are very critical to understand which are very critical to understand which
    are very critical to understand

    this this this

    uh how the training target is predicted'
  concept_slugs:
  - flow-matching
  - velocity-field
- idx: 20
  start_sec: 1246.39
  end_sec: 1311.6
  text: 'uh how the training target is predicted uh how the training target is predicted

    in the first place. in the first place. in the first place.

    And whatever I''m going to discuss next And whatever I''m going to discuss next
    And whatever I''m going to discuss next

    is going to form the critical piece of is going to form the critical piece of
    is going to form the critical piece of

    training flow models which is used in training flow models which is used in training
    flow models which is used in

    most of the modern uh diffusion models most of the modern uh diffusion models
    most of the modern uh diffusion models

    or flow-based models which are either or flow-based models which are either or
    flow-based models which are either

    used for image generation, video used for image generation, video used for image
    generation, video

    generation or even in robotics for that generation or even in robotics for that
    generation or even in robotics for that

    matter. matter. matter.

    [snorts] [snorts]

    Okay. So remember our goal is to convert Okay. So remember our goal is to convert
    Okay. So remember our goal is to convert

    the initial probability distribution to a final data distribution. So here to
    a final data distribution. So here

    [snorts] [snorts]

    this is the initial distribution which this is the initial distribution which
    this is the initial distribution which

    is uh noise. This is simply noise. It is uh noise. This is simply noise. It is
    uh noise. This is simply noise. It

    does not have any structure to it. does not have any structure to it. does not
    have any structure to it.

    But uh for the example of cats that we But uh for the example of cats that we
    But uh for the example of cats that we

    have referred to several times in this have referred to several times in this
    have referred to several times in this

    series, series, series,

    we want to get to a distribution which we want to get to a distribution which
    we want to get to a distribution which

    looks like this where you pick any point and you get a where you pick any point
    and you get a

    cat which is maybe specific to that cat which is maybe specific to that cat which
    is maybe specific to that

    breed. breed.'
  concept_slugs:
  - flow-matching
  - velocity-field
- idx: 21
  start_sec: 1311.6
  end_sec: 1366.64
  text: 'breed.

    So we have different So we have different So we have different

    we have a probability distribution that we have a probability distribution that
    we have a probability distribution that

    you know that is grounded in data which you know that is grounded in data which
    you know that is grounded in data which

    actually makes sense which you can actually makes sense which you can actually
    makes sense which you can

    sample from and generate images of cats. sample from and generate images of cats.
    sample from and generate images of cats.

    Now a naive thinking would tell you that Now a naive thinking would tell you that
    Now a naive thinking would tell you that

    well to go from noise to data somewhere well to go from noise to data somewhere
    well to go from noise to data somewhere

    we need we need to use the data right we need we need to use the data right we
    need we need to use the data right

    otherwise and that has to be a big part otherwise and that has to be a big part
    otherwise and that has to be a big part

    of our training target otherwise how of our training target otherwise how of our
    training target otherwise how

    will our model know that the final will our model know that the final will our
    model know that the final

    distribution that we want to morph the distribution that we want to morph the
    distribution that we want to morph the

    initial noisy distribution to represents initial noisy distribution to represents
    initial noisy distribution to represents

    the distribution of cats in this case. the distribution of cats in this case.
    the distribution of cats in this case.

    So uh okay so here we will use a So uh okay so here we will use a So uh okay so
    here we will use a

    [snorts] most general and most simple [snorts] most general and most simple [snorts]
    most general and most simple

    technique which is in line with most of technique which is in line with most of
    technique which is in line with most of

    the state-of-the-art models what is the state-of-the-art models what is the state-of-the-art
    models what is

    going to follow next and uh we are going going to follow next and uh we are going'
  concept_slugs:
  - flow-matching
  - velocity-field
- idx: 22
  start_sec: 1366.64
  end_sec: 1416.149
  text: 'going to follow next and uh we are going

    to go through a little bit of to go through a little bit of to go through a little
    bit of

    mathematics right now so please don''t be mathematics right now so please don''t
    be mathematics right now so please don''t be

    repelled by the maths which you are repelled by the maths which you are repelled
    by the maths which you are

    about to see it is very intuitive I''m about to see it is very intuitive I''m
    about to see it is very intuitive I''m

    not going to introduce any equations not going to introduce any equations not
    going to introduce any equations

    it''s just going to be some terminologies it''s just going to be some terminologies
    it''s just going to be some terminologies

    which I''m going to introduce which I''m going to introduce which I''m going to
    introduce

    but once we understand these but once we understand these but once we understand
    these

    terminologies it will help us understand terminologies it will help us understand
    terminologies it will help us understand

    flow models in a much better way and in flow models in a much better way and in
    flow models in a much better way and in

    fact we''ll also be drawing some fact we''ll also be drawing some fact we''ll
    also be drawing some

    parallels with the diffusion models parallels with the diffusion models parallels
    with the diffusion models

    which we have looked at before in the which we have looked at before in the which
    we have looked at before in the

    previous lectures. previous lectures. previous lectures.

    [snorts] So if you are new to the field [snorts] So if you are new to the field
    [snorts] So if you are new to the field

    of deep generative modeling um don''t of deep generative modeling um don''t of
    deep generative modeling um don''t

    worry about diffusion models for now. We worry about diffusion models for now.
    We worry about diffusion models for now. We

    will make sure that the following will make sure that the following will make
    sure that the following

    terminologies can be understood by terminologies can be understood by terminologies
    can be understood by

    everyone who is new to the field as everyone who is new to the field as everyone
    who is new to the field as

    well.'
  concept_slugs:
  - flow-matching
  - velocity-field
- idx: 23
  start_sec: 1418.789
  end_sec: 1491.76
  text: 'Okay. So, first concept that we will Okay. So, first concept that we will

    discuss is called as So let''s let''s try to understand what is So let''s let''s
    try to understand what is

    the meaning of [snorts] conditional the meaning of [snorts] conditional the meaning
    of [snorts] conditional

    probability path. probability path. probability path.

    Conditional probability path simply Conditional probability path simply Conditional
    probability path simply

    means that given a point zed. means that given a point zed. means that given a
    point zed.

    We define the conditional probability We define the conditional probability We
    define the conditional probability

    path as a transformation from the path as a transformation from the path as a
    transformation from the

    initial distri the initial distribution initial distri the initial distribution
    initial distri the initial distribution

    pinet pinet pinet

    to the point zed. to the point zed. to the point zed.

    So we are not trying here to morph the So we are not trying here to morph the
    So we are not trying here to morph the

    initial distribution to the final initial distribution to the final initial distribution
    to the final

    unknown distribution that we have no unknown distribution that we have no unknown
    distribution that we have no

    idea about. What we have idea about is idea about. What we have idea about is
    idea about. What we have idea about is

    the data. I know individual images of the data. I know individual images of the
    data. I know individual images of

    the cats, right? the cats, right? the cats, right?

    So there is some data which is given to So there is some data which is given to
    So there is some data which is given to

    me and the first thought that comes to me and the first thought that comes to
    me and the first thought that comes to

    my mind is instead of taking the initial my mind is instead of taking the initial
    my mind is instead of taking the initial

    gshian distribution to a distribution gshian distribution to a distribution gshian
    distribution to a distribution

    which I do not know. What if I take it which I do not know. What if I take it
    which I do not know. What if I take it

    to something I do know even if it is to something I do know even if it is'
  concept_slugs:
  - flow-matching
  - velocity-field
- idx: 24
  start_sec: 1491.76
  end_sec: 1551.6
  text: 'to something I do know even if it is

    like just one simple single data point like just one simple single data point
    like just one simple single data point

    [snorts] and that is exactly what [snorts] and that is exactly what [snorts] and
    that is exactly what

    conditional probability path means. Why conditional probability path means. Why
    conditional probability path means. Why

    conditional? because it is conditional. conditional? because it is conditional.
    conditional? because it is conditional.

    It is conditioned on that data sample. It is conditioned on that data sample.
    It is conditioned on that data sample.

    We are not predicting the We are not predicting the We are not predicting the

    complete probability distribution or the complete probability distribution or
    the complete probability distribution or the

    complete path but we are pro we are complete path but we are pro we are complete
    path but we are pro we are

    predicting the path which is conditioned predicting the path which is conditioned
    predicting the path which is conditioned

    on the point Z. on the point Z. on the point Z.

    [snorts] Let''s try to visualize this to [snorts] Let''s try to visualize this
    to [snorts] Let''s try to visualize this to

    make sure we understand this properly. make sure we understand this properly.
    make sure we understand this properly.

    Now in the figure you can see that Now in the figure you can see that Now in the
    figure you can see that

    the big circle is the initial the big circle is the initial the big circle is
    the initial

    distribution and the green is the point distribution and the green is the point
    distribution and the green is the point

    where we want to move the initial where we want to move the initial where we want
    to move the initial

    distribution towards. distribution towards. distribution towards.

    Okay. So this is how our transformation is going this is how our transformation
    is going

    to look like. [snorts] And the good part to look like. [snorts] And the good part
    to look like. [snorts] And the good part

    about this is that we know point Z. We about this is that we know point Z. We
    about this is that we know point Z. We

    know the data which is given to us. We know the data which is given to us. We'
  concept_slugs:
  - flow-matching
  - velocity-field
- idx: 25
  start_sec: 1551.6
  end_sec: 1625.44
  text: 'know the data which is given to us. We

    know this initial distribution also. know this initial distribution also. know
    this initial distribution also.

    So it is very rational to think that we So it is very rational to think that we
    So it is very rational to think that we

    can probably predict this we can probably predict the velocity we can probably
    predict the velocity

    field that field that field that

    transforms this initial distribution and transforms this initial distribution
    and transforms this initial distribution and

    takes it to the final point Z. So how how do we construct this path? So how how
    do we construct this path?

    Let''s first talk about the probability Let''s first talk about the probability
    Let''s first talk about the probability

    path. What do I mean by a probability path. What do I mean by a probability path.
    What do I mean by a probability

    path? Well, let''s see. path? Well, let''s see. path? Well, let''s see.

    The probability at time t =0, the The probability at time t =0, the The probability
    at time t =0, the

    probability distribution is let''s say probability distribution is let''s say
    probability distribution is let''s say

    uniform. uniform. uniform.

    And at time t = 1, there is no distribution. It is just one there is no distribution.
    It is just one

    single point zed. Right? single point zed. Right? single point zed. Right?

    Now what probability path tells us is Now what probability path tells us is Now
    what probability path tells us is

    that at every time step in this that at every time step in this that at every
    time step in this

    transformation transformation transformation

    can you generate a probability can you generate a probability can you generate
    a probability

    distribution for me. That is the meaning distribution for me. That is the meaning
    distribution for me. That is the meaning

    of probability path. And why conditional of probability path. And why conditional
    of probability path. And why conditional

    probability path? Because we have probability path? Because we have probability
    path? Because we have

    already know that the finally it should already know that the finally it should
    already know that the finally it should

    go to the point Z. So it is conditioned go to the point Z. So it is conditioned'
  concept_slugs:
  - flow-matching
  - velocity-field
- idx: 26
  start_sec: 1625.44
  end_sec: 1726.23
  text: 'go to the point Z. So it is conditioned

    on the point Z. on the point Z.

    So what can I do so that each individual So what can I do so that each individual
    So what can I do so that each individual

    distribution I know and I can take from distribution I know and I can take from
    distribution I know and I can take from

    the initial distribution to the final the initial distribution to the final

    distribution and what we do is very simple in in and what we do is very simple
    in in

    reality what is done is let''s say the initial distribution is let''s say the
    initial distribution is

    such that the mean is zero such that the mean is zero such that the mean is zero

    and the standard deviation is And now the final distribution is such that now
    the final distribution is such that

    the mean is zed the mean is zed the mean is zed

    and the deviation is zero because every and the deviation is zero because every
    and the deviation is zero because every

    time you sample you should get zed. It''s time you sample you should get zed.
    It''s time you sample you should get zed. It''s

    a fixed point. Right? [snorts] a fixed point. Right? [snorts] a fixed point. Right?
    [snorts]

    Now what if I define Now what if I define Now what if I define

    every single every single every single

    time step to be a gshian such that the time step to be a gshian such that the
    time step to be a gshian such that the

    mu starts from zero and it ends up with mu starts from zero and it ends up with
    mu starts from zero and it ends up with

    zed zed zed

    at time t = 1. at time t = 1. at time t = 1.

    This is time t equal to0 and uh this is z and uh this is z

    and the variance starts with one one

    and the variance ends at zero. What this will do is that it will What this will
    do is that it will

    provide me with the probability path provide me with the probability path provide
    me with the probability path

    such that at every time step I will have'
  concept_slugs:
  - flow-matching
  - velocity-field
- idx: 27
  start_sec: 1726.23
  end_sec: 1779.83
  text: 'such that at every time step I will have such that at every time step I will
    have

    a gshian and a gshian and a gshian and

    the probability distribution will change the probability distribution will change
    the probability distribution will change

    in such a way that the gshian will in such a way that the gshian will in such
    a way that the gshian will

    slowly contract and be displaced towards slowly contract and be displaced towards
    slowly contract and be displaced towards

    the point z. the point z. the point z.

    I can visualize this very nicely here. I can visualize this very nicely here.
    I can visualize this very nicely here.

    Initially it starts like this with a Initially it starts like this with a Initially
    it starts like this with a

    mean zero and a deviation of one. mean zero and a deviation of one. mean zero
    and a deviation of one.

    [snorts] Now this is the point which I [snorts] Now this is the point which I
    [snorts] Now this is the point which I

    have conditioned on. I have to move the have conditioned on. I have to move the
    have conditioned on. I have to move the

    distribution finally to this point. So distribution finally to this point. So
    distribution finally to this point. So

    you can see the mean is shifting as we you can see the mean is shifting as we
    you can see the mean is shifting as we

    go from time step t=0 to time step t= 1. go from time step t=0 to time step t=
    1. go from time step t=0 to time step t= 1.

    The mean is slowly shifting towards the The mean is slowly shifting towards the
    The mean is slowly shifting towards the

    right and it''s becoming narrow and right and it''s becoming narrow and right
    and it''s becoming narrow and

    narrower and narrower. So the deviation narrower and narrower. So the deviation
    narrower and narrower. So the deviation

    is reducing and finally I get a single is reducing and finally I get a single
    is reducing and finally I get a single

    point which is zed. point which is zed. point which is zed.

    So I have defined a conditional So I have defined a conditional So I have defined
    a conditional

    probability path which is linear in'
  concept_slugs:
  - flow-matching
  - velocity-field
- idx: 28
  start_sec: 1779.83
  end_sec: 1839.039
  text: 'probability path which is linear in probability path which is linear in

    time. time. time.

    So the mean increases from zero to the So the mean increases from zero to the
    So the mean increases from zero to the

    value of zed and the deviation decreases value of zed and the deviation decreases
    value of zed and the deviation decreases

    from 1 to 0. So [snorts] this can be visualized as So [snorts] this can be visualized
    as

    follows. Here also we have taken the follows. Here also we have taken the follows.
    Here also we have taken the

    example of Z= 3. The mean increases from example of Z= 3. The mean increases from
    example of Z= 3. The mean increases from

    0 to 3 and the variance decreases from 1 0 to 3 and the variance decreases from
    1 0 to 3 and the variance decreases from 1

    to 0. to 0. to 0.

    So now you know I am I know the So now you know I am I know the So now you know
    I am I know the

    trajectories which are followed by every trajectories which are followed by every
    trajectories which are followed by every

    single particle. single particle. single particle.

    And uh And uh And uh

    because I know the trajectories which because I know the trajectories which because
    I know the trajectories which

    are followed by every single particle, are followed by every single particle,
    are followed by every single particle,

    you might refer to our discussion about you might refer to our discussion about
    you might refer to our discussion about

    the detectives and say that well then the detectives and say that well then the
    detectives and say that well then

    maybe I can predict the velocity field maybe I can predict the velocity field
    maybe I can predict the velocity field

    here, right? here, right? here, right?

    [snorts] Maybe I know the velocity field [snorts] Maybe I know the velocity field
    [snorts] Maybe I know the velocity field

    because since I know the trajectories because since I know the trajectories because
    since I know the trajectories

    very clearly, very clearly, very clearly,

    I can find the velocity field which is I can find the velocity field which is
    I can find the velocity field which is

    going to generate those trajectories. going to generate those trajectories.'
  concept_slugs:
  - flow-matching
  - velocity-field
- idx: 29
  start_sec: 1839.039
  end_sec: 1883.84
  text: 'going to generate those trajectories.

    uh and this is exactly what we are going uh and this is exactly what we are going
    uh and this is exactly what we are going

    to do next. But before we move, I want to do next. But before we move, I want
    to do next. But before we move, I want

    you to clearly understand what we have you to clearly understand what we have
    you to clearly understand what we have

    done so far. This does not mean we have done so far. This does not mean we have
    done so far. This does not mean we have

    solved the problem. We have simply let''s solved the problem. We have simply let''s
    solved the problem. We have simply let''s

    say there are thousand images of cats, say there are thousand images of cats,
    say there are thousand images of cats,

    right? That are given to us. Now for right? That are given to us. Now for right?
    That are given to us. Now for

    every single image, we can construct a every single image, we can construct a
    every single image, we can construct a

    probability path which transforms the probability path which transforms the probability
    path which transforms the

    initial gshian distribution and takes it initial gshian distribution and takes
    it initial gshian distribution and takes it

    to that single image. We do this for all to that single image. We do this for
    all to that single image. We do this for all

    the thousand images. So far we have only the thousand images. So far we have only
    the thousand images. So far we have only

    discussed this much. We have nowhere discussed this much. We have nowhere discussed
    this much. We have nowhere

    discussed about discussed about discussed about

    uh how to construct a training target. uh how to construct a training target.
    uh how to construct a training target.

    But it turns out that this is exactly But it turns out that this is exactly But
    it turns out that this is exactly

    what we use for the training target. But what we use for the training target.
    But what we use for the training target. But

    anyways uh for now just think about this anyways uh for now just think about this'
  concept_slugs:
  - flow-matching
  - velocity-field
- idx: 30
  start_sec: 1883.84
  end_sec: 1935.919
  text: 'anyways uh for now just think about this

    as being a conditional probability path as being a conditional probability path
    as being a conditional probability path

    which is conditioned on the point Z which is conditioned on the point Z which
    is conditioned on the point Z

    head. head. head.

    Now this technique of conditioning is at Now this technique of conditioning is
    at Now this technique of conditioning is at

    the heart of deep generative modeling the heart of deep generative modeling the
    heart of deep generative modeling

    which I''m also realizing as I''m which I''m also realizing as I''m which I''m
    also realizing as I''m

    researching this topic. It is coming up researching this topic. It is coming up
    researching this topic. It is coming up

    everywhere to design training targets everywhere to design training targets everywhere
    to design training targets

    even for score based models diffusion even for score based models diffusion even
    for score based models diffusion

    models. Wherever we are not able to models. Wherever we are not able to models.
    Wherever we are not able to

    construct a training target people construct a training target people construct
    a training target people

    condition it on the data sample and then condition it on the data sample and then
    condition it on the data sample and then

    magically we can construct the training magically we can construct the training
    magically we can construct the training

    target. target. target.

    We will come to that how the We will come to that how the We will come to that
    how the

    construction appears but for now just construction appears but for now just construction
    appears but for now just

    make sure you understand the conditional make sure you understand the conditional
    make sure you understand the conditional

    probability path and understand the the probability path and understand the the
    probability path and understand the the

    terms probability path why because terms probability path why because terms probability
    path why because

    probability path is nothing but a probability path is nothing but a probability
    path is nothing but a

    trajectory. We are transforming the trajectory. We are transforming the trajectory.
    We are transforming the

    initial gshian distribution to the final initial gshian distribution to the final
    initial gshian distribution to the final

    single point that is the probability single point that is the probability'
  concept_slugs:
  - flow-matching
  - velocity-field
- idx: 31
  start_sec: 1935.919
  end_sec: 1997.43
  text: 'single point that is the probability

    path and we want to know at every single path and we want to know at every single
    path and we want to know at every single

    time step in this transition how does time step in this transition how does time
    step in this transition how does

    the probability distribution look like. the probability distribution look like.
    the probability distribution look like.

    Why conditional is because this is not Why conditional is because this is not
    Why conditional is because this is not

    the actual probability path. It is the actual probability path. It is the actual
    probability path. It is

    conditioned on the point''s head. conditioned on the point''s head. conditioned
    on the point''s head.

    [snorts] [snorts]

    Okay. Now as we discussed before because Okay. Now as we discussed before because
    Okay. Now as we discussed before because

    now we know the trajectories of each now we know the trajectories of each now
    we know the trajectories of each

    particle we we know that there should be particle we we know that there should
    be particle we we know that there should be

    a velocity field associated with it a velocity field associated with it a velocity
    field associated with it

    right. right. right.

    So for any conditional probability path So for any conditional probability path
    So for any conditional probability path

    there exists an equivalent vector field. [snorts] So instead of [snorts] So instead
    of

    sampling from probabilities at each time sampling from probabilities at each time
    sampling from probabilities at each time

    step, we can simply sample a point from step, we can simply sample a point from
    step, we can simply sample a point from

    P in it and we can just follow the P in it and we can just follow the P in it
    and we can just follow the

    vector field. This is exactly what we vector field. This is exactly what we vector
    field. This is exactly what we

    discussed at the beginning of the discussed at the beginning of the discussed
    at the beginning of the

    lecture. Remember if we want to go from lecture. Remember if we want to go from
    lecture. Remember if we want to go from

    the velocity vector field to the the velocity vector field to the the velocity
    vector field to the

    trajectories the reverse problem'
  concept_slugs:
  - flow-matching
  - velocity-field
- idx: 32
  start_sec: 1997.43
  end_sec: 2046.64
  text: 'trajectories the reverse problem trajectories the reverse problem

    we simply sample the initial point which we simply sample the initial point which
    we simply sample the initial point which

    was x0 in our case and we use the oiler was x0 in our case and we use the oiler
    was x0 in our case and we use the oiler

    discretization to discretization to discretization to

    find the next point x1 then we go to x2 find the next point x1 then we go to x2
    find the next point x1 then we go to x2

    and similarly we can we know the entire and similarly we can we know the entire
    and similarly we can we know the entire

    trajectory of the particle. trajectory of the particle. trajectory of the particle.

    [snorts] So that''s what we are trying to [snorts] So that''s what we are trying
    to [snorts] So that''s what we are trying to

    say in this piece of text that once you say in this piece of text that once you
    say in this piece of text that once you

    know the velocity field you can use that know the velocity field you can use that
    know the velocity field you can use that

    velocity field to get the entire velocity field to get the entire velocity field
    to get the entire

    trajectory of a particle trajectory of a particle trajectory of a particle

    and uh here you can actually see the and uh here you can actually see the and
    uh here you can actually see the

    conditional probability path and the conditional probability path and the conditional
    probability path and the

    conditional vector field. [snorts] So conditional vector field. [snorts] So conditional
    vector field. [snorts] So

    first let''s look at the conditional first let''s look at the conditional first
    let''s look at the conditional

    probability path. Every single particle probability path. Every single particle
    probability path. Every single particle

    is being [snorts] transformed from the is being [snorts] transformed from the
    is being [snorts] transformed from the

    initial distribution uh to the final initial distribution uh to the final initial
    distribution uh to the final

    point zed. Now who is responsible for point zed. Now who is responsible for point
    zed. Now who is responsible for

    this transformation? There is a vector this transformation? There is a vector'
  concept_slugs:
  - flow-matching
  - velocity-field
- idx: 33
  start_sec: 2046.64
  end_sec: 2106.4
  text: 'this transformation? There is a vector

    field which is responsible for this field which is responsible for this field
    which is responsible for this

    transformation transformation

    and [snorts] and [snorts] and [snorts]

    rightfully so the vector field is rightfully so the vector field is rightfully
    so the vector field is

    pointing you can see if I zoom in here pointing you can see if I zoom in here
    pointing you can see if I zoom in here

    this is the vector field all the vector this is the vector field all the vector
    this is the vector field all the vector

    points all the vectors are pointing points all the vectors are pointing points
    all the vectors are pointing

    towards the direction of zed because towards the direction of zed because towards
    the direction of zed because

    this is what we want to move the points this is what we want to move the points
    this is what we want to move the points

    towards. towards. towards.

    [snorts] So these are the vector field [snorts] So these are the vector field
    [snorts] So these are the vector field

    lines and the white lines are the lines and the white lines are the lines and
    the white lines are the

    trajectories which are followed by the trajectories which are followed by the
    trajectories which are followed by the

    individual green particles. Now here is another example where this Now here is
    another example where this

    is the target. So we want to move our is the target. So we want to move our is
    the target. So we want to move our

    distribution which is uh shown over here distribution which is uh shown over here
    distribution which is uh shown over here

    to this target. to this target. to this target.

    And you can see as time proceeds the And you can see as time proceeds the And
    you can see as time proceeds the

    distribution slowly moves towards the distribution slowly moves towards the distribution
    slowly moves towards the

    target. But I want you to focus on these target. But I want you to focus on these
    target. But I want you to focus on these

    arrows which are the velocity vectors. [snorts] First of all note that how [snorts]
    First of all note that how

    every single point the velocity vector every single point the velocity vector'
  concept_slugs:
  - flow-matching
  - velocity-field
- idx: 34
  start_sec: 2106.4
  end_sec: 2165.75
  text: 'every single point the velocity vector

    is pointed towards them. And And

    for points which are far away the for points which are far away the for points
    which are far away the

    vectors are longer in magnitude. As you vectors are longer in magnitude. As you
    vectors are longer in magnitude. As you

    move closer the vectors are reducing in move closer the vectors are reducing in
    move closer the vectors are reducing in

    in in magnitude. in in magnitude. in in magnitude.

    And the formula for this is actually And the formula for this is actually And
    the formula for this is actually

    given very simply by this. given very simply by this. given very simply by this.

    So zed is our point which is our target. So zed is our point which is our target.
    So zed is our point which is our target.

    If x is very far from zed the magnitude If x is very far from zed the magnitude
    If x is very far from zed the magnitude

    is very high. If x is very close to zed is very high. If x is very close to zed
    is very high. If x is very close to zed

    it''s almost zero. You can see here. it''s almost zero. You can see here. it''s
    almost zero. You can see here.

    But not just that there is a variation But not just that there is a variation
    But not just that there is a variation

    with time also. As as time goes close to with time also. As as time goes close
    to with time also. As as time goes close to

    one as you go towards the final one as you go towards the final one as you go
    towards the final

    distribution you can see the magnitude distribution you can see the magnitude
    distribution you can see the magnitude

    increases. So [snorts] increases. So [snorts] increases. So [snorts]

    from here to here you can see the arrows from here to here you can see the arrows
    from here to here you can see the arrows

    increasing in the magnitude increasing in the magnitude increasing in the magnitude

    from left to right from left to right from left to right

    and [snorts] uh and [snorts] uh and [snorts] uh

    this is because as as as time proceeds'
  concept_slugs:
  - flow-matching
  - velocity-field
- idx: 35
  start_sec: 2165.75
  end_sec: 2216.16
  text: 'this is because as as as time proceeds this is because as as as time proceeds

    we probably want to uh move the velocity we probably want to uh move the velocity
    we probably want to uh move the velocity

    field in a more aggressive manner field in a more aggressive manner field in a
    more aggressive manner

    towards our target. So first of all the towards our target. So first of all the
    towards our target. So first of all the

    first observation is that wherever your first observation is that wherever your
    first observation is that wherever your

    point is the velocity field is targeted point is the velocity field is targeted
    point is the velocity field is targeted

    towards the location''s head and the towards the location''s head and the towards
    the location''s head and the

    magnitude is proportional to how far magnitude is proportional to how far magnitude
    is proportional to how far

    your point is from the target your point is from the target your point is from
    the target

    which probably makes sense because the which probably makes sense because the
    which probably makes sense because the

    further your point is from the target further your point is from the target further
    your point is from the target

    you want to push the particle more with you want to push the particle more with
    you want to push the particle more with

    with more force. So in reality what with more force. So in reality what with more
    force. So in reality what

    happens is that every single particle is happens is that every single particle
    is happens is that every single particle is

    is pushed towards your target. So that''s is pushed towards your target. So that''s
    is pushed towards your target. So that''s

    why you get this conditional probability why you get this conditional probability
    why you get this conditional probability

    path [snorts] and this this formula for path [snorts] and this this formula for
    path [snorts] and this this formula for

    the velocity field is is uh once we know the velocity field is is uh once we know
    the velocity field is is uh once we know

    this velocity field formula this velocity field formula this velocity field formula

    we don''t need anything else using this we don''t need anything else using this'
  concept_slugs:
  - flow-matching
  - velocity-field
- idx: 36
  start_sec: 2216.16
  end_sec: 2266.31
  text: 'we don''t need anything else using this

    formula we can simply calculate the formula we can simply calculate the formula
    we can simply calculate the

    trajectories of each and every point so trajectories of each and every point so
    trajectories of each and every point so

    [snorts] that every single point goes [snorts] that every single point goes [snorts]
    that every single point goes

    from the initial gshian distribution to from the initial gshian distribution to
    from the initial gshian distribution to

    your point Z. your point Z. your point Z.

    So the velocity field is given by the So the velocity field is given by the So
    the velocity field is given by the

    ratio of two quantities. The numerator ratio of two quantities. The numerator
    ratio of two quantities. The numerator

    is simply a vector from the point to the is simply a vector from the point to
    the is simply a vector from the point to the

    target and the denominator captures the target and the denominator captures the
    target and the denominator captures the

    evolution of time. evolution of time. evolution of time.

    So you observe something very critical So you observe something very critical
    So you observe something very critical

    here. Uh as we move forward in time the here. Uh as we move forward in time the
    here. Uh as we move forward in time the

    value of denominator decreases which value of denominator decreases which value
    of denominator decreases which

    means the magnitude of the velocity means the magnitude of the velocity means
    the magnitude of the velocity

    field lines increase as as we go forward field lines increase as as we go forward
    field lines increase as as we go forward

    in time. This can be seen from the above in time. This can be seen from the above
    in time. This can be seen from the above

    figures as the arrows get bigger and figures as the arrows get bigger and figures
    as the arrows get bigger and

    bigger as time proceeds. So this this bigger as time proceeds. So this this bigger
    as time proceeds. So this this

    this overall intuition will be critical this overall intuition will be critical
    this overall intuition will be critical

    for us as we move ahead. for us as we move ahead. for us as we move ahead.

    Now this u of t is is called as'
  concept_slugs:
  - flow-matching
  - velocity-field
- idx: 37
  start_sec: 2266.31
  end_sec: 2320.0
  text: 'Now this u of t is is called as Now this u of t is is called as

    conditional So you you might look at this and think So you you might look at this
    and think

    uh well if you look at the training uh well if you look at the training uh well
    if you look at the training

    target target target

    wasn''t our training target also a wasn''t our training target also a wasn''t
    our training target also a

    velocity field so can we directly use velocity field so can we directly use velocity
    field so can we directly use

    this as a training target [snorts] well this as a training target [snorts] well
    this as a training target [snorts] well

    my first answer to that is you can''t my first answer to that is you can''t my
    first answer to that is you can''t

    directly use it because this is not our directly use it because this is not our
    directly use it because this is not our

    training target remember it is training target remember it is training target
    remember it is

    conditioned on the data z conditioned on the data z conditioned on the data z

    uh so at a first glance it looks like uh so at a first glance it looks like uh
    so at a first glance it looks like

    okay this is very different from the okay this is very different from the okay
    this is very different from the

    actual velocity field because there the actual velocity field because there the
    actual velocity field because there the

    the target which I looked at before that the target which I looked at before that
    the target which I looked at before that

    is not conditioned on the point Z head is not conditioned on the point Z head
    is not conditioned on the point Z head

    but here we know the exact formula for but here we know the exact formula for
    but here we know the exact formula for

    this condition velocity field. So this condition velocity field. So this condition
    velocity field. So

    ideally we can we can replace this in in ideally we can we can replace this in
    in ideally we can we can replace this in in

    our target and train our neural network our target and train our neural network'
  concept_slugs:
  - flow-matching
  - velocity-field
- idx: 38
  start_sec: 2320.0
  end_sec: 2377.52
  text: 'our target and train our neural network

    to predict it for every single point to predict it for every single point to predict
    it for every single point

    zed. zed. zed.

    It turns out that what we will do is It turns out that what we will do is It turns
    out that what we will do is

    exactly that. But then let me not exactly that. But then let me not exactly that.
    But then let me not

    explain to you right now why that explain to you right now why that explain to
    you right now why that

    happens. And that''s why this formulation happens. And that''s why this formulation
    happens. And that''s why this formulation

    is very easy. But for now for our is very easy. But for now for our is very easy.
    But for now for our

    where we are right now in terms of where we are right now in terms of where we
    are right now in terms of

    accessing this material is that we know accessing this material is that we know
    accessing this material is that we know

    that this is the conditional vector that this is the conditional vector that this
    is the conditional vector

    field and we can completely predict this field and we can completely predict this
    field and we can completely predict this

    conditional vector field. Okay, so now so far we have looked at Okay, so now so
    far we have looked at

    the conditional probability path and the the conditional probability path and
    the the conditional probability path and the

    conditional vector field and [snorts] we conditional vector field and [snorts]
    we conditional vector field and [snorts] we

    can predict the conditional probability can predict the conditional probability
    can predict the conditional probability

    path as a sequence of gshians which path as a sequence of gshians which path as
    a sequence of gshians which

    takes us from the initial gshian takes us from the initial gshian takes us from
    the initial gshian

    distribution to a final point and what distribution to a final point and what
    distribution to a final point and what

    is responsible for this path is the is responsible for this path is the is responsible
    for this path is the

    velocity vector field which is pointed velocity vector field which is pointed'
  concept_slugs:
  - flow-matching
  - velocity-field
- idx: 39
  start_sec: 2377.52
  end_sec: 2432.0
  text: 'velocity vector field which is pointed

    from our data to the data point where we from our data to the data point where
    we from our data to the data point where we

    want to go. So it''s it''s a it''s arrow want to go. So it''s it''s a it''s arrow
    want to go. So it''s it''s a it''s arrow

    which directly goes from where we are which directly goes from where we are which
    directly goes from where we are

    right now x and where we want to go that right now x and where we want to go that
    right now x and where we want to go that

    is zed. Okay. So now we will go to marginal Okay. So now we will go to marginal

    probability path. probability path.

    So now marginal is exactly the opposite So now marginal is exactly the opposite
    So now marginal is exactly the opposite

    of conditional. Imagine that instead of of conditional. Imagine that instead of
    of conditional. Imagine that instead of

    a single point zed we have a complex a single point zed we have a complex a single
    point zed we have a complex

    data distribution p data. And for every data distribution p data. And for every
    data distribution p data. And for every

    point in this distribution which is point in this distribution which is point
    in this distribution which is

    given to us, we can build a conditional given to us, we can build a conditional
    given to us, we can build a conditional

    probability path. And a collection of probability path. And a collection of probability
    path. And a collection of

    all the conditional probability path all the conditional probability path all
    the conditional probability path

    gives us the marginal probability path. gives us the marginal probability path.
    gives us the marginal probability path.

    So it''s like once we understand So it''s like once we understand So it''s like
    once we understand

    conditional probability path we can conditional probability path we can conditional
    probability path we can

    think in this direction that if you think in this direction that if you think
    in this direction that if you

    aggregate all these paths together the aggregate all these paths together the
    aggregate all these paths together the

    final flow that you get the the final final flow that you get the the final'
  concept_slugs:
  - flow-matching
  - velocity-field
- idx: 40
  start_sec: 2432.0
  end_sec: 2484.39
  text: 'final flow that you get the the final

    trajectories that you get those are the trajectories that you get those are the
    trajectories that you get those are the

    marginal probability paths. marginal probability paths. marginal probability paths.

    We have in fact defined this as flow in We have in fact defined this as flow in
    We have in fact defined this as flow in

    the last lecture but now we are giving the last lecture but now we are giving
    the last lecture but now we are giving

    it another name which is a marginal it another name which is a marginal it another
    name which is a marginal

    probability path. probability path.

    So you can imagine the distribution to So you can imagine the distribution to
    So you can imagine the distribution to

    be made up of a collection of zeds and a be made up of a collection of zeds and
    a be made up of a collection of zeds and a

    marginal path is a set of distributions marginal path is a set of distributions
    marginal path is a set of distributions

    which transforms the initial which transforms the initial which transforms the
    initial

    distribution pinet to P data. distribution pinet to P data. distribution pinet
    to P data.

    And if you recall this is exactly what And if you recall this is exactly what
    And if you recall this is exactly what

    we want to predict. we want to predict. we want to predict.

    [snorts] But here the interesting thing [snorts] But here the interesting thing
    [snorts] But here the interesting thing

    is that P data is not known to us. So we is that P data is not known to us. So
    we is that P data is not known to us. So we

    are just discussing this for a are just discussing this for a are just discussing
    this for a

    conceptual understanding of the conceptual understanding of the conceptual understanding
    of the

    difference between uh conditional difference between uh conditional difference
    between uh conditional

    probability path and marginal probability path and marginal probability path and
    marginal

    probability path probability path probability path

    but in reality the p data is not known but in reality the p data is not known
    but in reality the p data is not known

    to us. So here if you see'
  concept_slugs:
  - flow-matching
  - velocity-field
- idx: 41
  start_sec: 2484.39
  end_sec: 2570.0
  text: 'to us. So here if you see to us. So here if you see

    the final distribution that we get which the final distribution that we get which
    the final distribution that we get which

    is which are these um is which are these um is which are these um

    eight clusters right that is the eight clusters right that is the eight clusters
    right that is the

    distribution that we want to predict. If distribution that we want to predict.
    If distribution that we want to predict. If

    that was known to us, we could directly that was known to us, we could directly
    that was known to us, we could directly

    construct this marginal probability construct this marginal probability construct
    this marginal probability

    path. path. path.

    But all we know is probably just But all we know is probably just But all we know
    is probably just

    thousand points within that thousand points within that thousand points within
    that

    distribution. We don''t know the final distribution. We don''t know the final
    distribution. We don''t know the final

    overall distribution yet. overall distribution yet. overall distribution yet.

    And similarly, uh we can actually And similarly, uh we can actually And similarly,
    uh we can actually

    understand this. Let''s let''s understand this. Let''s let''s understand this.
    Let''s let''s

    go to this Google Collab notebook. >> Okay. So >> Okay. So

    I''m going to run this piece of code so I''m going to run this piece of code so
    I''m going to run this piece of code so

    that we understand what is the meaning that we understand what is the meaning
    that we understand what is the meaning

    of a marginal probability path. of a marginal probability path. of a marginal
    probability path.

    So we''ll run this first piece of code So we''ll run this first piece of code
    So we''ll run this first piece of code

    over here. So this is very similar to the final So this is very similar to the
    final

    animation which I showed you. Uh animation which I showed you. Uh animation which
    I showed you. Uh

    so here this is the target data where we so here this is the target data where
    we so here this is the target data where we

    want to reach which is a sample of eight want to reach which is a sample of eight'
  concept_slugs:
  - flow-matching
  - velocity-field
- idx: 42
  start_sec: 2570.0
  end_sec: 2625.839
  text: 'want to reach which is a sample of eight

    washians washians washians

    and initially we start with a random and initially we start with a random and
    initially we start with a random

    noise. noise. noise.

    So here you see the animation is now So here you see the animation is now So here
    you see the animation is now

    available to us. available to us. available to us.

    So we go from the initial distribution So we go from the initial distribution
    So we go from the initial distribution

    of random noise to a final distribution of random noise to a final distribution
    of random noise to a final distribution

    where these eight gshians are where these eight gshians are where these eight
    gshians are

    distributed in space. distributed in space. distributed in space.

    Now that is this is exactly what we want Now that is this is exactly what we want
    Now that is this is exactly what we want

    to predict the marginal probability path to predict the marginal probability path
    to predict the marginal probability path

    in in reality the distribution of cats in in reality the distribution of cats
    in in reality the distribution of cats

    will also be very complex right will also be very complex right will also be very
    complex right

    and uh along with the marginal and uh along with the marginal and uh along with
    the marginal

    probability path now you know that there probability path now you know that there
    probability path now you know that there

    will be a field also associated with it will be a field also associated with it
    will be a field also associated with it

    similar to how there was a vector field similar to how there was a vector field
    similar to how there was a vector field

    associated with the conditional associated with the conditional associated with
    the conditional

    probability path. Similarly for marginal probability path. Similarly for marginal
    probability path. Similarly for marginal

    probability path there will be a vector probability path there will be a vector
    probability path there will be a vector

    field associated and ideally this vector field associated and ideally this vector
    field associated and ideally this vector

    field is our training target. field is our training target. field is our training
    target.

    Now uh here let''s play this Now uh here let''s play this'
  concept_slugs:
  - flow-matching
  - velocity-field
- idx: 43
  start_sec: 2625.839
  end_sec: 2679.68
  text: 'Now uh here let''s play this

    piece of code to understand this piece of code to understand this piece of code
    to understand this

    u and you''ll probably get something like and you''ll probably get something like

    this at the end. So here you see the this at the end. So here you see the this
    at the end. So here you see the

    velocity vector field. How they change velocity vector field. How they change
    velocity vector field. How they change

    with time, how they evolve with time. So with time, how they evolve with time.
    So with time, how they evolve with time. So

    it''s a vector field which is dependent it''s a vector field which is dependent
    it''s a vector field which is dependent

    on space and time. But it is marginal on space and time. But it is marginal on
    space and time. But it is marginal

    vector field because we are not just vector field because we are not just vector
    field because we are not just

    finding a vector field for one single finding a vector field for one single finding
    a vector field for one single

    point which takes from a distribution to point which takes from a distribution
    to point which takes from a distribution to

    that point but rather we have a that point but rather we have a that point but
    rather we have a

    collection of points in space. So and we collection of points in space. So and
    we collection of points in space. So and we

    are we are calculating the vector field are we are calculating the vector field
    are we are calculating the vector field

    for all those points which make them for all those points which make them for
    all those points which make them

    evolve according to their probability evolve according to their probability evolve
    according to their probability

    paths. [snorts] paths. [snorts] paths. [snorts]

    So if we had access to this there would So if we had access to this there would
    So if we had access to this there would

    not be any question that we replace this not be any question that we replace this
    not be any question that we replace this

    in our target. But uh the the issue is in our target. But uh the the issue is'
  concept_slugs:
  - flow-matching
  - velocity-field
- idx: 44
  start_sec: 2679.68
  end_sec: 2739.886
  text: 'in our target. But uh the the issue is

    that we do not have access to this that we do not have access to this that we
    do not have access to this

    because we only have access to our because we only have access to our because
    we only have access to our

    individual data points. Okay. Okay. So here is another example Okay. Okay. So
    here is another example

    to understand the difference between to understand the difference between to understand
    the difference between

    conditional and marginal paths. So here conditional and marginal paths. So here
    conditional and marginal paths. So here

    you see you see you see

    u u u

    our actual distribution is are these our actual distribution is are these our
    actual distribution is are these

    five spheres that I want to go to right five spheres that I want to go to right
    five spheres that I want to go to right

    which which are shown in these circles. which which are shown in these circles.
    which which are shown in these circles.

    This is the distribution which is a This is the distribution which is a This is
    the distribution which is a

    collection of these five spheres. But collection of these five spheres. But collection
    of these five spheres. But

    I''m not aware of these distributions. I I''m not aware of these distributions.
    I I''m not aware of these distributions. I

    I I just know a single point zed. I I just know a single point zed. I I just know
    a single point zed.

    So I take my original gshian and I move So I take my original gshian and I move
    So I take my original gshian and I move

    it towards this single point zed it towards this single point zed it towards this
    single point zed

    according to these trajectories according to these trajectories according to these
    trajectories

    which I get by solving this conditional which I get by solving this conditional
    which I get by solving this conditional

    distribution uh this this conditional od distribution uh this this conditional
    od distribution uh this this conditional od

    where we have seen that this mu is given where we have seen that this mu is given
    where we have seen that this mu is given

    by z minus x divided by 1 minus t.'
  concept_slugs:
  - flow-matching
  - velocity-field
- idx: 45
  start_sec: 2739.886
  end_sec: 2790.96
  text: 'by z minus x divided by 1 minus t. by z minus x divided by 1 minus t.

    [snorts] So these these these field [snorts] So these these these field [snorts]
    So these these these field

    lines are almost linear from the source lines are almost linear from the source
    lines are almost linear from the source

    to the target over here. to the target over here. to the target over here.

    So we are calculating the trajectories So we are calculating the trajectories
    So we are calculating the trajectories

    from the original gshian to the single from the original gshian to the single
    from the original gshian to the single

    point Z which has been sampled from our point Z which has been sampled from our
    point Z which has been sampled from our

    distribution. distribution.

    This is what is the meaning of a This is what is the meaning of a This is what
    is the meaning of a

    conditional probability path. conditional probability path. conditional probability
    path.

    Whereas [snorts] Whereas [snorts] Whereas [snorts]

    marginal probability path is something marginal probability path is something
    marginal probability path is something

    very different. Marginal probability very different. Marginal probability very
    different. Marginal probability

    path is uh something which takes us from path is uh something which takes us from
    path is uh something which takes us from

    our original uh our original uh our original uh

    distribution which is the gshian distribution which is the gshian distribution
    which is the gshian

    distribution over here and then you see distribution over here and then you see
    distribution over here and then you see

    how we are learning all these how we are learning all these how we are learning
    all these

    trajectories. So basically you sample a trajectories. So basically you sample
    a trajectories. So basically you sample a

    lot of zed from the uh and and if you lot of zed from the uh and and if you lot
    of zed from the uh and and if you

    have access to infinite samples then have access to infinite samples then have
    access to infinite samples then

    obviously you will go down this path but obviously you will go down this path
    but obviously you will go down this path but

    we do not have access to infinite we do not have access to infinite'
  concept_slugs:
  - flow-matching
  - velocity-field
- idx: 46
  start_sec: 2790.96
  end_sec: 2838.8
  text: 'we do not have access to infinite

    samples. we have access to finite samples. we have access to finite samples. we
    have access to finite

    samples samples samples

    and uh this this uh credit goes to uh and uh this this uh credit goes to uh and
    uh this this uh credit goes to uh

    the MIT course by Peter Bodarit. I have the MIT course by Peter Bodarit. I have
    the MIT course by Peter Bodarit. I have

    link this in in the original flow model link this in in the original flow model
    link this in in the original flow model

    lecture also. So this this makes the lecture also. So this this makes the lecture
    also. So this this makes the

    difference between the conditional paths difference between the conditional paths
    difference between the conditional paths

    and the marginal paths very clear. and the marginal paths very clear. and the
    marginal paths very clear.

    Now uh the reason why we went into Now uh the reason why we went into Now uh the
    reason why we went into

    conditional and marginal paths is conditional and marginal paths is conditional
    and marginal paths is

    because it will help us understand the because it will help us understand the
    because it will help us understand the

    training target and what compromise we training target and what compromise we
    training target and what compromise we

    have done to to get to the training have done to to get to the training have done
    to to get to the training

    target. The ideal training target should target. The ideal training target should
    target. The ideal training target should

    be the marginal vector field but uh we be the marginal vector field but uh we
    be the marginal vector field but uh we

    will understand that we make a will understand that we make a will understand
    that we make a

    compromise to it and we use a very compromise to it and we use a very compromise
    to it and we use a very

    different type of training target. different type of training target. different
    type of training target.

    So now uh let''s let''s try to broadly So now uh let''s let''s try to broadly
    So now uh let''s let''s try to broadly

    understand what we are doing here. understand what we are doing here.'
  concept_slugs:
  - flow-matching
  - velocity-field
- idx: 47
  start_sec: 2838.8
  end_sec: 2897.28
  text: 'understand what we are doing here.

    Essentially we are treating data Essentially we are treating data Essentially
    we are treating data

    generation as a flow problem. We know generation as a flow problem. We know generation
    as a flow problem. We know

    mathematically that mathematically that mathematically that

    for any complex data set whether it''s for any complex data set whether it''s
    for any complex data set whether it''s

    pictures of cats, robotics policies or pictures of cats, robotics policies or
    pictures of cats, robotics policies or

    Giblly scenes there exists a vector Giblly scenes there exists a vector Giblly
    scenes there exists a vector

    field that connects a cloud of random field that connects a cloud of random field
    that connects a cloud of random

    noise directly to that data and this is noise directly to that data and this is
    noise directly to that data and this is

    the marginal vector field. Okay. Now if we had a map of this Okay. Now if we had
    a map of this

    current uh generating a new image would current uh generating a new image would
    current uh generating a new image would

    be simple and deterministic. So we be simple and deterministic. So we be simple
    and deterministic. So we

    already know this if we have access to already know this if we have access to
    already know this if we have access to

    this vector field uh we we simply use this vector field uh we we simply use this
    vector field uh we we simply use

    this vector field and uh we calculate this vector field and uh we calculate this
    vector field and uh we calculate

    the trajectory using this vector field the trajectory using this vector field
    the trajectory using this vector field

    using the oiler method. This is what using the oiler method. This is what using
    the oiler method. This is what

    detective 2 said at the start of today''s detective 2 said at the start of today''s
    detective 2 said at the start of today''s

    lecture. lecture. lecture.

    But the biggest problem is that we do But the biggest problem is that we do But
    the biggest problem is that we do

    not have the formula for this vector not have the formula for this vector not
    have the formula for this vector

    field is impossibly complex. field is impossibly complex.'
  concept_slugs:
  - flow-matching
  - velocity-field
- idx: 48
  start_sec: 2897.28
  end_sec: 2946.79
  text: 'field is impossibly complex.

    You cannot write down an equation that You cannot write down an equation that
    You cannot write down an equation that

    defines what a Giblly movie looks like. defines what a Giblly movie looks like.
    defines what a Giblly movie looks like.

    So we we cannot calculate the vector So we we cannot calculate the vector So we
    we cannot calculate the vector

    field but we can approximate it. And uh field but we can approximate it. And uh
    field but we can approximate it. And uh

    in today''s lecture we are not going to in today''s lecture we are not going to
    in today''s lecture we are not going to

    look at how exactly the target of the look at how exactly the target of the look
    at how exactly the target of the

    velocity field is constructed. But from velocity field is constructed. But from
    velocity field is constructed. But from

    a mathematical point of view if you look a mathematical point of view if you look
    a mathematical point of view if you look

    at it today''s lecture was a bit involved at it today''s lecture was a bit involved
    at it today''s lecture was a bit involved

    into condition and marginal path. The into condition and marginal path. The into
    condition and marginal path. The

    next lecture is going to be very easy next lecture is going to be very easy next
    lecture is going to be very easy

    for us because it is simply going to for us because it is simply going to for
    us because it is simply going to

    build upon today''s lecture and in fact build upon today''s lecture and in fact
    build upon today''s lecture and in fact

    we will understand how easy it is to we will understand how easy it is to we will
    understand how easy it is to

    construct the training target. Uh and construct the training target. Uh and construct
    the training target. Uh and

    and you might think okay so does this and you might think okay so does this and
    you might think okay so does this

    actually work? It it sounds too good to actually work? It it sounds too good to
    actually work? It it sounds too good to

    be true and it does actually work. We we'
  concept_slugs:
  - flow-matching
  - velocity-field
- idx: 49
  start_sec: 2946.79
  end_sec: 2994.319
  text: 'be true and it does actually work. We we be true and it does actually work.
    We we

    have seen this in other uh aspects of have seen this in other uh aspects of have
    seen this in other uh aspects of

    deep generative models like diffusion deep generative models like diffusion deep
    generative models like diffusion

    models and uh uh score based models and uh uh score based models and uh uh score
    based

    generative models that conditional generative models that conditional generative
    models that conditional

    models or if you condition it on the models or if you condition it on the models
    or if you condition it on the

    data you you get a training target which data you you get a training target which
    data you you get a training target which

    is feasible and magically it just it is feasible and magically it just it is feasible
    and magically it just it

    just works. So we are going to just works. So we are going to just works. So we
    are going to

    understand how to construct this understand how to construct this understand how
    to construct this

    training target which is going to be training target which is going to be training
    target which is going to be

    exceedingly simple and then we are going exceedingly simple and then we are going
    exceedingly simple and then we are going

    to understand how to set up our whole to understand how to set up our whole to
    understand how to set up our whole

    flow pipeline and uh we will also look flow pipeline and uh we will also look
    flow pipeline and uh we will also look

    at a practical example of how to at a practical example of how to at a practical
    example of how to

    generate a flow model uh how to train a generate a flow model uh how to train
    a generate a flow model uh how to train a

    flow model using uh the training target flow model using uh the training target
    flow model using uh the training target

    and how to sample from it. [snorts] So and how to sample from it. [snorts] So
    and how to sample from it. [snorts] So

    uh I I hope this lecture was interesting uh I I hope this lecture was interesting'
  concept_slugs:
  - flow-matching
  - velocity-field
- idx: 50
  start_sec: 2994.319
  end_sec: 3045.67
  text: 'uh I I hope this lecture was interesting

    for all of you. I haven''t yet given the for all of you. I haven''t yet given
    the for all of you. I haven''t yet given the

    final reveal. Uh I''m I''m delaying it final reveal. Uh I''m I''m delaying it
    final reveal. Uh I''m I''m delaying it

    purposefully. As I said at the start of purposefully. As I said at the start of
    purposefully. As I said at the start of

    the first lecture in the flow series, I the first lecture in the flow series,
    I the first lecture in the flow series, I

    could have wrapped this entire series in could have wrapped this entire series
    in could have wrapped this entire series in

    just maybe 40 minutes. But then you will just maybe 40 minutes. But then you will
    just maybe 40 minutes. But then you will

    not appreciate the kind of thinking not appreciate the kind of thinking not appreciate
    the kind of thinking

    which has gone into constructing this which has gone into constructing this which
    has gone into constructing this

    training target. And uh today''s lecture training target. And uh today''s lecture
    training target. And uh today''s lecture

    I wanted to specifically devote to that I wanted to specifically devote to that
    I wanted to specifically devote to that

    so that all of you understand uh how so that all of you understand uh how so that
    all of you understand uh how

    these targets are constructed. Before we these targets are constructed. Before
    we these targets are constructed. Before we

    go ahead, I just want to uh motivate all go ahead, I just want to uh motivate
    all go ahead, I just want to uh motivate all

    of you by showing this paper pi 0.5 of you by showing this paper pi 0.5 of you
    by showing this paper pi 0.5

    or let''s look at pi 0. or let''s look at pi 0. or let''s look at pi 0.

    So this is a robotics foundational model So this is a robotics foundational model
    So this is a robotics foundational model

    and uh the reason I''m showing this to and uh the reason I''m showing this to
    and uh the reason I''m showing this to

    you right now is you right now is you right now is

    this this came out last year'
  concept_slugs:
  - flow-matching
  - velocity-field
- idx: 51
  start_sec: 3045.67
  end_sec: 3092.559
  text: 'this this came out last year this this came out last year

    and this is based on uh flow matching. and this is based on uh flow matching.
    and this is based on uh flow matching.

    So here essentially what we are doing is So here essentially what we are doing
    is So here essentially what we are doing is

    uh when you see flow matching now all of uh when you see flow matching now all
    of uh when you see flow matching now all of

    you can understand that we are trying to you can understand that we are trying
    to you can understand that we are trying to

    find the trajectories from the initial find the trajectories from the initial
    find the trajectories from the initial

    gshian distribution to a final gshian distribution to a final gshian distribution
    to a final

    distribution and we [snorts] are trying distribution and we [snorts] are trying
    distribution and we [snorts] are trying

    to find a velocity field that takes us to find a velocity field that takes us
    to find a velocity field that takes us

    from the initial to the final from the initial to the final from the initial to
    the final

    distribution. The only thing to think distribution. The only thing to think distribution.
    The only thing to think

    about is what is this distribution about is what is this distribution about is
    what is this distribution

    representing. So, so far we have seen representing. So, so far we have seen representing.
    So, so far we have seen

    distributions representing images. But distributions representing images. But
    distributions representing images. But

    distributions can also represent robotic distributions can also represent robotic
    distributions can also represent robotic

    actions which is exactly what is actions which is exactly what is actions which
    is exactly what is

    happening in this in this paper which is happening in this in this paper which
    is happening in this in this paper which is

    amazing. If you see the applications of amazing. If you see the applications of
    amazing. If you see the applications of

    flow they they have a flow expert which flow they they have a flow expert which
    flow they they have a flow expert which

    is which is the action expert here which is which is the action expert here which'
  concept_slugs:
  - flow-matching
  - velocity-field
- idx: 52
  start_sec: 3092.559
  end_sec: 3129.76
  text: 'is which is the action expert here which

    is a it''s based on flow matching and uh is a it''s based on flow matching and
    uh is a it''s based on flow matching and uh

    the training target that you see here is the training target that you see here
    is the training target that you see here is

    exceedingly simple. Maybe I can show exceedingly simple. Maybe I can show exceedingly
    simple. Maybe I can show

    that to you uh which is written in in in that to you uh which is written in in
    in that to you uh which is written in in in

    in this section. We will we will look at in this section. We will we will look
    at in this section. We will we will look at

    this in detail in the next lecture. But this in detail in the next lecture. But
    this in detail in the next lecture. But

    once you go through the next lecture, once you go through the next lecture, once
    you go through the next lecture,

    you will be able to understand these you will be able to understand these you
    will be able to understand these

    sections which are coming in any paper. sections which are coming in any paper.
    sections which are coming in any paper.

    So that whenever you see flow matching, So that whenever you see flow matching,
    So that whenever you see flow matching,

    it will suddenly not be very it will suddenly not be very it will suddenly not
    be very

    inaccessible field to you, but you can inaccessible field to you, but you can
    inaccessible field to you, but you can

    relate to what we have seen in the relate to what we have seen in the relate to
    what we have seen in the

    lecture and build a very strong lecture and build a very strong lecture and build
    a very strong

    intuition for it. Thank you very much intuition for it. Thank you very much intuition
    for it. Thank you very much

    everyone and I will see you in the next everyone and I will see you in the next
    everyone and I will see you in the next

    lecture which is going to be like a lecture which is going to be like a'
  concept_slugs:
  - flow-matching
  - velocity-field
- idx: 53
  start_sec: 3129.76
  end_sec: 3134.119
  text: 'lecture which is going to be like a

    magician''s reveal. Thank you.'
  concept_slugs:
  - flow-matching
  - velocity-field
---
# Lecture 10 - Constructing Training Target for Flow Models | Principles of Diffusion Models

See the structured chunks above.
