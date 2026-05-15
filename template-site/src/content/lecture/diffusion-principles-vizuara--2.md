---
course_slug: diffusion-principles-vizuara
idx: 2
title: Lecture 9 - Introduction to Flow Models | Principles of Diffusion Models
video_url: https://www.youtube.com/watch?v=qwXaD03IHqw
duration_sec: null
chunks:
- idx: 0
  start_sec: 3.99
  end_sec: 70.39
  text: 'Good morning everyone. Good morning everyone.

    Today we are starting with the next Today we are starting with the next Today
    we are starting with the next

    lecture of our course which is lecture of our course which is lecture of our course
    which is

    introduction to flow models. introduction to flow models. introduction to flow
    models.

    I have decided to divide this topic into I have decided to divide this topic into
    I have decided to divide this topic into

    a series of three to four lectures a series of three to four lectures a series
    of three to four lectures

    so that I can cover the entire depth in so that I can cover the entire depth in
    so that I can cover the entire depth in

    a very comprehensive manner. a very comprehensive manner. a very comprehensive
    manner.

    One interesting thing about the theory One interesting thing about the theory
    One interesting thing about the theory

    behind flow models is that behind flow models is that behind flow models is that

    you can teach the same topic in two you can teach the same topic in two you can
    teach the same topic in two

    different ways. different ways. different ways.

    You can teach this entire topic within a You can teach this entire topic within
    a You can teach this entire topic within a

    span of one lecture span of one lecture span of one lecture

    or you can teach it within a span of or you can teach it within a span of or you
    can teach it within a span of

    four lectures. Now that is quite paradoxical that how Now that is quite paradoxical
    that how

    you can teach the same concept you can teach the same concept you can teach the
    same concept

    with these two format types. The main with these two format types. The main with
    these two format types. The main

    reason is that if you go through the reason is that if you go through the reason
    is that if you go through the

    difficult route of the four lectures, difficult route of the four lectures, difficult
    route of the four lectures,

    you end up at a place which is quite you end up at a place which is quite you
    end up at a place which is quite

    simple which you could have got in the'
  concept_slugs:
  - continuous-normalizing-flow
  - flow-matching
- idx: 1
  start_sec: 70.39
  end_sec: 126.24
  text: 'simple which you could have got in the simple which you could have got in
    the

    first lecture itself. first lecture itself. first lecture itself.

    But I don''t want to show you that route But I don''t want to show you that route
    But I don''t want to show you that route

    that easily because you won''t appreciate that easily because you won''t appreciate
    that easily because you won''t appreciate

    the the the

    work which has been put behind work which has been put behind work which has been
    put behind

    the easy route. So in essence flow model the easy route. So in essence flow model
    the easy route. So in essence flow model

    is a very very easy concept and it can is a very very easy concept and it can
    is a very very easy concept and it can

    be explained in a very simple and be explained in a very simple and be explained
    in a very simple and

    intuitive manner. intuitive manner. intuitive manner.

    But because But because But because

    reaching there is not that reaching there is not that reaching there is not that

    straightforward, we might have to spend straightforward, we might have to spend
    straightforward, we might have to spend

    some more time to understand the simple some more time to understand the simple
    some more time to understand the simple

    concept. concept. concept.

    In other words, imagine that we are In other words, imagine that we are In other
    words, imagine that we are

    going we want to go from point A to going we want to go from point A to going
    we want to go from point A to

    point B, but instead of going through point B, but instead of going through point
    B, but instead of going through

    the straight line, we are going to take the straight line, we are going to take
    the straight line, we are going to take

    a curve and reach point B. a curve and reach point B. a curve and reach point
    B.

    It will be slightly mathematical uh It will be slightly mathematical uh It will
    be slightly mathematical uh

    today''s lecture but uh I have tried to today''s lecture but uh I have tried to
    today''s lecture but uh I have tried to

    keep the mathematics as simple as keep the mathematics as simple as'
  concept_slugs:
  - continuous-normalizing-flow
  - flow-matching
- idx: 2
  start_sec: 126.24
  end_sec: 181.12
  text: 'keep the mathematics as simple as

    possible [snorts] and I have taken possible [snorts] and I have taken possible
    [snorts] and I have taken

    inspiration from an uh MIT course to inspiration from an uh MIT course to inspiration
    from an uh MIT course to

    structure these lectures. I will put the structure these lectures. I will put
    the structure these lectures. I will put the

    link to that course in the description link to that course in the description
    link to that course in the description

    and their lecture notes as well. and their lecture notes as well. and their lecture
    notes as well.

    So before we get started for those of So before we get started for those of So
    before we get started for those of

    you who haven''t heard of flow models and you who haven''t heard of flow models
    and you who haven''t heard of flow models and

    uh what these models represent uh what these models represent uh what these models
    represent

    first of all let us divide this two first of all let us divide this two first
    of all let us divide this two

    words into two distinct words. The first words into two distinct words. The first
    words into two distinct words. The first

    word is flow. Now what does flow mean? word is flow. Now what does flow mean?
    word is flow. Now what does flow mean?

    When I hear flow the first thing that When I hear flow the first thing that When
    I hear flow the first thing that

    comes to my mind is probably a fluid. comes to my mind is probably a fluid. comes
    to my mind is probably a fluid.

    Right? So let''s click on this and see Right? So let''s click on this and see
    Right? So let''s click on this and see

    something something moving in in space something something moving in in space
    something something moving in in space

    something like this something something something like this something something
    something like this something something

    like a fluid motion like a fluid motion like a fluid motion

    and model is of course we are aware a and model is of course we are aware a and
    model is of course we are aware a

    model is a representation of a phenomena model is a representation of a phenomena'
  concept_slugs:
  - continuous-normalizing-flow
  - flow-matching
- idx: 3
  start_sec: 181.12
  end_sec: 262.079
  text: 'model is a representation of a phenomena

    a neural network is an example of a a neural network is an example of a a neural
    network is an example of a

    model or any mathematical function which model or any mathematical function which
    model or any mathematical function which

    maps an input to an output is a model. maps an input to an output is a model.
    maps an input to an output is a model.

    [snorts] [snorts] [snorts]

    Now the question is how we are going to Now the question is how we are going to
    Now the question is how we are going to

    use these physical notions of the use these physical notions of the use these
    physical notions of the

    concept of flow and concept of flow and concept of flow and

    u solve the problem that we have set out u solve the problem that we have set
    out u solve the problem that we have set out

    to solve at the beginning of this to solve at the beginning of this to solve at
    the beginning of this

    series. If you remember the problem that series. If you remember the problem that
    series. If you remember the problem that

    we have is we have is we have is

    called as deep generative modeling. >> Now what does this mean? >> Now what does
    this mean?

    We are given a bunch of data. Let''s say we are given these images of Let''s say
    we are given these images of

    cats cats cats

    and we want to find a distribution using and we want to find a distribution using
    and we want to find a distribution using

    which we can sample images which look which we can sample images which look which
    we can sample images which look

    exactly like these images of cats. So exactly like these images of cats. So exactly
    like these images of cats. So

    from data from data from data

    We want to move to distribution and that is the broad problem that we and that
    is the broad problem that we

    want to solve want to solve want to solve

    in in this whole whole series and so far in in this whole whole series and so
    far in in this whole whole series and so far

    we have looked at different techniques we have looked at different techniques'
  concept_slugs:
  - continuous-normalizing-flow
  - flow-matching
- idx: 4
  start_sec: 262.079
  end_sec: 334.4
  text: 'we have looked at different techniques

    to solve this broader problem. It to solve this broader problem. It to solve this
    broader problem. It

    started out with variational started out with variational started out with variational

    autoenccoders. Then we move to diffusion autoenccoders. Then we move to diffusion
    autoenccoders. Then we move to diffusion

    models and now we are discussing another models and now we are discussing another
    models and now we are discussing another

    type of deep generative models which are type of deep generative models which
    are type of deep generative models which are

    called as flow models. So we discussed VAS, So we discussed VAS,

    we discussed diffusion models we discussed diffusion models we discussed diffusion
    models

    [clears throat] [clears throat] [clears throat]

    and now we are going to discuss flow and now we are going to discuss flow and
    now we are going to discuss flow

    models. So in our mind we know that okay models So in our mind we know that okay
    models

    probably represent deep generative probably represent deep generative probably
    represent deep generative

    models and models and models and

    flow is something like a fluid which flow is something like a fluid which flow
    is something like a fluid which

    transports particles from one initial transports particles from one initial transports
    particles from one initial

    location to a final location. So so location to a final location. So so location
    to a final location. So so

    there is a movement of particles in there is a movement of particles in there
    is a movement of particles in

    space space space

    and something is changing with time and something is changing with time and something
    is changing with time

    also. So we want to combine these also. So we want to combine these also. So we
    want to combine these

    physical intuitions into a deep physical intuitions into a deep physical intuitions
    into a deep

    generative model that helps us map a generative model that helps us map a generative
    model that helps us map a

    data to a probability distribution. So let''s understand uh before we dive So
    let''s understand uh before we dive

    deep into the theory. Flow models are deep into the theory. Flow models are deep
    into the theory. Flow models are

    one of the most consequential techniques one of the most consequential techniques'
  concept_slugs:
  - continuous-normalizing-flow
  - flow-matching
- idx: 5
  start_sec: 334.4
  end_sec: 393.6
  text: 'one of the most consequential techniques

    in modern [snorts] in modern [snorts] in modern [snorts]

    generative modeling. And the reason it generative modeling. And the reason it
    generative modeling. And the reason it

    is very consequential it is it is used is very consequential it is it is used
    is very consequential it is it is used

    in a lot of image generation models. Lot in a lot of image generation models.
    Lot in a lot of image generation models. Lot

    of state-of-the-art image generation of state-of-the-art image generation of state-of-the-art
    image generation

    tools use flow models. It is also used tools use flow models. It is also used
    tools use flow models. It is also used

    in robotics. There is a policy which is in robotics. There is a policy which is
    in robotics. There is a policy which is

    called as pi zero foundational model. Now this is a policy which is a robotics
    Now this is a policy which is a robotics

    foundational model which means that foundational model which means that foundational
    model which means that

    similar to how LLMs are trained on similar to how LLMs are trained on similar
    to how LLMs are trained on

    massive amounts of web corpus data these massive amounts of web corpus data these
    massive amounts of web corpus data these

    models are trained on massive amounts of models are trained on massive amounts
    of models are trained on massive amounts of

    videos. So the robot learns from these videos. So the robot learns from these
    videos. So the robot learns from these

    static or static videos and learns to static or static videos and learns to static
    or static videos and learns to

    perform actions in the real world by perform actions in the real world by perform
    actions in the real world by

    learning from these trajectories which learning from these trajectories which
    learning from these trajectories which

    have been recorded. have been recorded. have been recorded.

    Now this policy uses something called as Now this policy uses something called
    as Now this policy uses something called as

    a flow model u in in the architecture a flow model u in in the architecture a
    flow model u in in the architecture

    and it works exceptionally well. You can and it works exceptionally well. You
    can'
  concept_slugs:
  - continuous-normalizing-flow
  - flow-matching
- idx: 6
  start_sec: 393.6
  end_sec: 446.639
  text: 'and it works exceptionally well. You can

    see here they have this action expert see here they have this action expert see
    here they have this action expert

    and this action expert is built [snorts] and this action expert is built [snorts]
    and this action expert is built [snorts]

    on top of a flow model. So understanding on top of a flow model. So understanding
    on top of a flow model. So understanding

    flow model is extremely critical for us flow model is extremely critical for us
    flow model is extremely critical for us

    to understand all these applications of to understand all these applications of
    to understand all these applications of

    uh these models in different domains uh these models in different domains uh these
    models in different domains

    including robotics including uh image including robotics including uh image including
    robotics including uh image

    generation and video generation as well. generation and video generation as well.
    generation and video generation as well.

    [snorts] In fact a lot of protein [snorts] In fact a lot of protein [snorts] In
    fact a lot of protein

    synthesis synthesis of protein molecules synthesis synthesis of protein molecules
    synthesis synthesis of protein molecules

    uh or drug discovery is now being done uh or drug discovery is now being done
    uh or drug discovery is now being done

    using flow models. So there are using flow models. So there are using flow models.
    So there are

    innumerable number of applications and innumerable number of applications and
    innumerable number of applications and

    as I said in the beginning the final as I said in the beginning the final as I
    said in the beginning the final

    formulation is so simple that we''ll formulation is so simple that we''ll formulation
    is so simple that we''ll

    think back and say why did we spend think back and say why did we spend think
    back and say why did we spend

    three lectures on this this could have three lectures on this this could have
    three lectures on this this could have

    been maybe done in half an hour but we been maybe done in half an hour but we
    been maybe done in half an hour but we

    really want to appreciate how this really want to appreciate how this really want
    to appreciate how this

    formula comes about which is very formula comes about which is very'
  concept_slugs:
  - continuous-normalizing-flow
  - flow-matching
- idx: 7
  start_sec: 446.639
  end_sec: 525.35
  text: 'formula comes about which is very

    simple. So flow modeling at the heart of simple. So flow modeling at the heart
    of simple. So flow modeling at the heart of

    it is very simple and it has huge number it is very simple and it has huge number
    it is very simple and it has huge number

    of applications. of applications. of applications.

    But surprisingly this is the model which But surprisingly this is the model which
    But surprisingly this is the model which

    came out the came out the came out the

    uh came out late compared to other uh came out late compared to other uh came
    out late compared to other

    models. For example score based models, models. For example score based models,
    models. For example score based models,

    diffusion models all these models came diffusion models all these models came
    diffusion models all these models came

    early and then flow models came after early and then flow models came after early
    and then flow models came after

    that. [snorts]

    Okay. So first let''s start with a simple Okay. So first let''s start with a simple
    Okay. So first let''s start with a simple

    mathematical description mathematical description mathematical description

    [snorts] [snorts]

    where where where

    we are looking at something called as we are looking at something called as we
    are looking at something called as

    time dependent vector fields. [snorts]

    First let us understand what is a vector First let us understand what is a vector
    First let us understand what is a vector

    field. Okay. So imagine that you have field. Okay. So imagine that you have field.
    Okay. So imagine that you have

    this 2D two-dimensional grid x-axis and y-axis. two-dimensional grid x-axis and
    y-axis.

    [snorts] A vector field is something [snorts] A vector field is something [snorts]
    A vector field is something

    where given any point where given any point where given any point

    it gives a vector as an output. it gives a vector as an output. it gives a vector
    as an output.

    So for example, this is a vector field. So for example, this is a vector field.
    So for example, this is a vector field.

    [snorts] [snorts]

    So let''s take an example. Imagine that So let''s take an example. Imagine that
    So let''s take an example. Imagine that

    maybe you''re sitting on a table right'
  concept_slugs:
  - continuous-normalizing-flow
  - flow-matching
- idx: 8
  start_sec: 525.35
  end_sec: 591.76
  text: 'maybe you''re sitting on a table right maybe you''re sitting on a table right

    now or you have a table in front of you. now or you have a table in front of you.
    now or you have a table in front of you.

    Uh you place a bunch of magnets on the Uh you place a bunch of magnets on the
    Uh you place a bunch of magnets on the

    table and the magnets table and the magnets table and the magnets

    create a vector field all around them. create a vector field all around them.
    create a vector field all around them.

    Uh or the magnets create a magnetic Uh or the magnets create a magnetic Uh or
    the magnets create a magnetic

    field all around them and you take any field all around them and you take any
    field all around them and you take any

    point on the table and you ask what is point on the table and you ask what is
    point on the table and you ask what is

    the magnetic field at that location. the magnetic field at that location. the
    magnetic field at that location.

    That [snorts] is an example of a vector That [snorts] is an example of a vector
    That [snorts] is an example of a vector

    field. Given any point in space, it field. Given any point in space, it field.
    Given any point in space, it

    gives you a magnitude and a direction. Now here what we are considering is a Now
    here what we are considering is a

    timed dependent vector field. timed dependent vector field. timed dependent vector
    field.

    So what does a timed dependent vector So what does a timed dependent vector So
    what does a timed dependent vector

    field do? Instead of looking at one field do? Instead of looking at one field
    do? Instead of looking at one

    single snapshot, so this is maybe a single snapshot, so this is maybe a single
    snapshot, so this is maybe a

    snapshot at time t equal to0. snapshot at time t equal to0. snapshot at time t
    equal to0.

    This vector field is going to change This vector field is going to change This
    vector field is going to change

    with time. So the magnets that we have with time. So the magnets that we have'
  concept_slugs:
  - continuous-normalizing-flow
  - flow-matching
- idx: 9
  start_sec: 591.76
  end_sec: 659.36
  text: 'with time. So the magnets that we have

    placed on the table, what if these placed on the table, what if these placed on
    the table, what if these

    magnets are constantly moving? magnets are constantly moving? magnets are constantly
    moving?

    Then the magnetic field created by them Then the magnetic field created by them
    Then the magnetic field created by them

    will also change with time, right? And will also change with time, right? And
    will also change with time, right? And

    because of that you will have these because of that you will have these because
    of that you will have these

    vector fields which are also now vector fields which are also now vector fields
    which are also now

    changing with time. depends on two things. depends on two things.

    [snorts] [snorts]

    It depends on first space It depends on first space It depends on first space

    which is at at what point in this which is at at what point in this which is at
    at what point in this

    cartian grid you are looking at and cartian grid you are looking at and cartian
    grid you are looking at and

    second it depends on time as well. So [snorts] whatever I have shown here So [snorts]
    whatever I have shown here

    it''s this is like a single snapshot. it''s this is like a single snapshot. it''s
    this is like a single snapshot.

    So imagine the magnetic field on your So imagine the magnetic field on your So
    imagine the magnetic field on your

    table is varying with time. You take a table is varying with time. You take a
    table is varying with time. You take a

    camera and you take a photo of the camera and you take a photo of the camera and
    you take a photo of the

    magnetic field. So you freeze time and magnetic field. So you freeze time and
    magnetic field. So you freeze time and

    then the magnetic field will only vary then the magnetic field will only vary
    then the magnetic field will only vary

    with space. Now these photos you can with space. Now these photos you can with
    space. Now these photos you can

    take at multiple time steps and hence take at multiple time steps and hence'
  concept_slugs:
  - continuous-normalizing-flow
  - flow-matching
- idx: 10
  start_sec: 659.36
  end_sec: 732.72
  text: 'take at multiple time steps and hence

    you will get a vector field which is you will get a vector field which is you
    will get a vector field which is

    changing with time. So now we are discussing time dependent So now we are discussing
    time dependent

    vector fields. vector fields. vector fields.

    A time dependent vector field maps a A time dependent vector field maps a A time
    dependent vector field maps a

    point x in space point x in space point x in space

    and time t to a velocity vector. and time t to a velocity vector. and time t to
    a velocity vector.

    And mathematically we define such a And mathematically we define such a And mathematically
    we define such a

    field of as u of x t. For example, if I field of as u of x t. For example, if
    I field of as u of x t. For example, if I

    say u of say u of say u of

    um um um

    let''s say this x is a vector. So I point let''s say this x is a vector. So I
    point let''s say this x is a vector. So I point

    it as 5 it as 5 it as 5

    e ex let''s say it''s a vector only in the e ex let''s say it''s a vector only
    in the e ex let''s say it''s a vector only in the

    x direction, x direction, x direction,

    0. 0. 0.

    This means that I''m taking a snapshot at This means that I''m taking a snapshot
    at This means that I''m taking a snapshot at

    time t=0 time t=0 time t=0

    and I am asking what is the velocity and I am asking what is the velocity and
    I am asking what is the velocity

    field at this point field at this point field at this point

    and and and

    this is given by a vector which can this is given by a vector which can this is
    given by a vector which can

    point in any direction. point in any direction. point in any direction.

    So the notation u u is a vector which So the notation u u is a vector which So
    the notation u u is a vector which

    depends on not just the position in depends on not just the position in'
  concept_slugs:
  - continuous-normalizing-flow
  - flow-matching
- idx: 11
  start_sec: 732.72
  end_sec: 787.91
  text: 'depends on not just the position in

    space but also it depends on the time space but also it depends on the time space
    but also it depends on the time

    snapshot. So it is a timed dependent snapshot. So it is a timed dependent snapshot.
    So it is a timed dependent

    vector field. This is something which is vector field. This is something which
    is vector field. This is something which is

    new for some people and it takes a bit new for some people and it takes a bit
    new for some people and it takes a bit

    of a time to understand it. But you can of a time to understand it. But you can
    of a time to understand it. But you can

    imagine something like imagine something like imagine something like

    let''s say you have a u let''s say you have a u let''s say you have a u

    you have a bank or let''s say a container you have a bank or let''s say a container
    you have a bank or let''s say a container

    in which you pour water in which you pour water in which you pour water

    and this water is and you are moving the and this water is and you are moving
    the and this water is and you are moving the

    container left and right. So the water container left and right. So the water
    container left and right. So the water

    is also moving left and right. Now you is also moving left and right. Now you
    is also moving left and right. Now you

    take any point in the container, the take any point in the container, the take
    any point in the container, the

    velocity at that point is going to velocity at that point is going to velocity
    at that point is going to

    change with time because the container change with time because the container
    change with time because the container

    itself is moving and every point in the itself is moving and every point in the
    itself is moving and every point in the

    container is going to have different container is going to have different container
    is going to have different

    velocities. So this is an example of a velocities. So this is an example of a
    velocities. So this is an example of a

    timed dependent vector field.'
  concept_slugs:
  - continuous-normalizing-flow
  - flow-matching
- idx: 12
  start_sec: 787.92
  end_sec: 851.199
  text: 'timed dependent vector field.

    So another way of defining this is So another way of defining this is So another
    way of defining this is

    people usually write this t as a people usually write this t as a people usually
    write this t as a

    subscript and x is written in the subscript and x is written in the subscript
    and x is written in the

    bracket. So this means that the velocity bracket. So this means that the velocity
    bracket. So this means that the velocity

    field at time snapshot t and at a space field at time snapshot t and at a space
    field at time snapshot t and at a space

    position which is denoted as x. position which is denoted as x. position which
    is denoted as x.

    Okay. So now the Okay. So now the Okay. So now the

    interesting part about this velocity interesting part about this velocity interesting
    part about this velocity

    field or the vector field is that the field or the vector field is that the field
    or the vector field is that the

    trajectories of the points are changing trajectories of the points are changing
    trajectories of the points are changing

    according to it. according to it. according to it.

    So up until now what I have said is that So up until now what I have said is that
    So up until now what I have said is that

    all the points in space are having some all the points in space are having some
    all the points in space are having some

    vector. vector. vector.

    Okay. Now I''m saying something else. I''m Okay. Now I''m saying something else.
    I''m Okay. Now I''m saying something else. I''m

    saying that these vectors represent the saying that these vectors represent the
    saying that these vectors represent the

    velocities of these particles which velocities of these particles which velocities
    of these particles which

    means that the means that the means that the

    position of this particle is going to position of this particle is going to position
    of this particle is going to

    change because of these velocities. change because of these velocities. change
    because of these velocities.

    So for example, if we take this example So for example, if we take this example'
  concept_slugs:
  - continuous-normalizing-flow
  - flow-matching
- idx: 13
  start_sec: 851.199
  end_sec: 916.399
  text: 'So for example, if we take this example

    at at the top at time t equal to0, this at at the top at time t equal to0, this
    at at the top at time t equal to0, this

    is what my velocity field looks like. is what my velocity field looks like. is
    what my velocity field looks like.

    And because of these this velocity field And because of these this velocity field
    And because of these this velocity field

    my particles which is let''s say I focus my particles which is let''s say I focus
    my particles which is let''s say I focus

    on this green particle right now the on this green particle right now the on this
    green particle right now the

    position of this particle is going to position of this particle is going to

    change because this velocity vector is change because this velocity vector is
    change because this velocity vector is

    acts upon it. So maybe at the next time acts upon it. So maybe at the next time
    acts upon it. So maybe at the next time

    step this particle moves here this step this particle moves here this step this
    particle moves here this

    particle moves here. This particle moves particle moves here. This particle moves
    particle moves here. This particle moves

    here. here. here.

    So the location of all the particles is So the location of all the particles is
    So the location of all the particles is

    going to change because of the velocity going to change because of the velocity
    going to change because of the velocity

    which acts upon them and then we move to the next time and then we move to the
    next time

    snapshot. Now here again there might be snapshot. Now here again there might be
    snapshot. Now here again there might be

    some other velocity field vector which some other velocity field vector which
    some other velocity field vector which

    is imposed on these points. So again the is imposed on these points. So again
    the is imposed on these points. So again the

    position of these points will change. position of these points will change. position
    of these points will change.

    So now we are asking the question how do So now we are asking the question how
    do'
  concept_slugs:
  - continuous-normalizing-flow
  - flow-matching
- idx: 14
  start_sec: 916.399
  end_sec: 984.8
  text: 'So now we are asking the question how do

    the position of particles which are the position of particles which are the position
    of particles which are

    inside the space change according to inside the space change according to inside
    the space change according to

    this velocity vector field this velocity vector field this velocity vector field

    and that is given by an equation which and that is given by an equation which
    and that is given by an equation which

    looks like this. looks like this. looks like this.

    [snorts] Now this is very similar to the velocity Now this is very similar to
    the velocity

    formula. All of us know that velocity is formula. All of us know that velocity
    is formula. All of us know that velocity is

    given by given by given by

    distance upon time which can also be written as change in which can also be written
    as change in

    the position of the particle the position of the particle the position of the
    particle

    divided by change in time which is delta divided by change in time which is delta
    divided by change in time which is delta

    x divided by delta t. And if these x divided by delta t. And if these x divided
    by delta t. And if these

    changes are small enough this can be changes are small enough this can be changes
    are small enough this can be

    approximated as dx by dt. approximated as dx by dt. approximated as dx by dt.

    So given a velocity vector field at any So given a velocity vector field at any
    So given a velocity vector field at any

    point if I know a small incremental point if I know a small incremental point
    if I know a small incremental

    change in the time I can predict by how change in the time I can predict by how
    change in the time I can predict by how

    much the particle is going to move in much the particle is going to move in much
    the particle is going to move in

    space. space. space.

    So I can predict the displacement of the So I can predict the displacement of
    the So I can predict the displacement of the

    particle if I know the velocity vector particle if I know the velocity vector'
  concept_slugs:
  - continuous-normalizing-flow
  - flow-matching
- idx: 15
  start_sec: 984.8
  end_sec: 1079.039
  text: 'particle if I know the velocity vector

    field. This is exactly what this formula field. This is exactly what this formula
    field. This is exactly what this formula

    says. says. says.

    So if I have a particle located at So if I have a particle located at So if I
    have a particle located at

    position x at time t, position x at time t, position x at time t,

    then the change in the location of that then the change in the location of that
    then the change in the location of that

    particle is given by is given by

    the velocity vector field at that same the velocity vector field at that same
    the velocity vector field at that same

    point and at time t. This is what this point and at time t. This is what this
    point and at time t. This is what this

    formula represents. and we have schematically drawn it in in and we have schematically
    drawn it in in

    this figure itself. If we want to this figure itself. If we want to this figure
    itself. If we want to

    exactly calculate this displacement, exactly calculate this displacement, exactly
    calculate this displacement,

    let [snorts] us do that using this let [snorts] us do that using this let [snorts]
    us do that using this

    formula. Let''s let''s focus on this formula. Let''s let''s focus on this formula.
    Let''s let''s focus on this

    point. So let''s say this velocity is u point. So let''s say this velocity is
    u point. So let''s say this velocity is u

    and now the velocity u of x comma 0. and now the velocity u of x comma 0. and
    now the velocity u of x comma 0.

    Okay. So let''s say this velocity is Okay. So let''s say this velocity is Okay.
    So let''s say this velocity is

    given by given by

    3. Okay. Now I''m interested to find the Okay. Now I''m interested to find the

    [clears throat] dx by dt [clears throat] dx by dt [clears throat] dx by dt

    the change in velo the change in the the change in velo the change in the the
    change in velo the change in the

    position of this point with time and I know this is equal to u with time and I
    know this is equal to u

    of x0 of x0'
  concept_slugs:
  - continuous-normalizing-flow
  - flow-matching
- idx: 16
  start_sec: 1079.039
  end_sec: 1148.87
  text: 'of x0

    okay so now this if I write as delta x okay so now this if I write as delta x
    okay so now this if I write as delta x

    by delta t by delta t by delta t

    is equal to mu of u of x0. is equal to mu of u of x0. is equal to mu of u of x0.

    Now if let''s say delta t is equal to 1 Now if let''s say delta t is equal to
    1 Now if let''s say delta t is equal to 1

    then delta x is equal to u which is 3 e then delta x is equal to u which is 3
    e then delta x is equal to u which is 3 e

    x + 4 ey. Now this is of course an approximate Now this is of course an approximate

    usually delta t will be very small in usually delta t will be very small in usually
    delta t will be very small in

    magnitude. So what that means is that magnitude. So what that means is that magnitude.
    So what that means is that

    this particle will move three places in the x direction and four three places
    in the x direction and four

    places in the y direction. places in the y direction. places in the y direction.

    So if we know the velocity field at all So if we know the velocity field at all
    So if we know the velocity field at all

    points at all times snapshots points at all times snapshots points at all times
    snapshots

    theoretically we can calculate the exact theoretically we can calculate the exact
    theoretically we can calculate the exact

    trajectories of each and every particle trajectories of each and every particle
    trajectories of each and every particle

    in the fluid. in the fluid. in the fluid.

    So imagine that you have a river and you So imagine that you have a river and
    you So imagine that you have a river and you

    place a small box in the river place a small box in the river place a small box
    in the river

    and you ask the question where will this and you ask the question where will this
    and you ask the question where will this

    box end up at time t equal to 10 let''s'
  concept_slugs:
  - continuous-normalizing-flow
  - flow-matching
- idx: 17
  start_sec: 1148.87
  end_sec: 1202.789
  text: 'box end up at time t equal to 10 let''s box end up at time t equal to 10
    let''s

    say. Now if you know the exact velocity say. Now if you know the exact velocity
    say. Now if you know the exact velocity

    at all points in the river at all times at all points in the river at all times
    at all points in the river at all times

    you can map the trajectory of this box you can map the trajectory of this box
    you can map the trajectory of this box

    and how it moves with time and where it and how it moves with time and where it
    and how it moves with time and where it

    ends up at time t equal to 10. That is ends up at time t equal to 10. That is
    ends up at time t equal to 10. That is

    exactly what we are saying in this exactly what we are saying in this exactly
    what we are saying in this

    mathematical description. mathematical description. mathematical description.

    and uh this is represented by this and uh this is represented by this and uh this
    is represented by this

    simple formula which is also a simple formula which is also a simple formula which
    is also a

    differential equation. Now the central question that we want to Now the central
    question that we want to

    ask is if a point starts at x0 ask is if a point starts at x0 ask is if a point
    starts at x0

    at time t =0 at time t =0 at time t =0

    and follows the vector field then where and follows the vector field then where
    and follows the vector field then where

    does the particle end up at a later does the particle end up at a later does the
    particle end up at a later

    time? So time? So time? So

    if if [snorts] I have a box and I place if if [snorts] I have a box and I place
    if if [snorts] I have a box and I place

    it in the river at time t equal to0, the it in the river at time t equal to0,
    the it in the river at time t equal to0, the

    box follows the vector field and the'
  concept_slugs:
  - continuous-normalizing-flow
  - flow-matching
- idx: 18
  start_sec: 1202.789
  end_sec: 1266.88
  text: 'box follows the vector field and the box follows the vector field and the

    question I''m trying to address is where question I''m trying to address is where
    question I''m trying to address is where

    does the box end up later in time does the box end up later in time does the box
    end up later in time

    because of the flow of the river. Now this is nicely illustrated in this Now this
    is nicely illustrated in this

    uh image. uh image. uh image.

    So we start at x x0 and you can see how So we start at x x0 and you can see how
    So we start at x x0 and you can see how

    the particle moves. the particle moves. the particle moves.

    Now you can see two things here. The Now you can see two things here. The Now
    you can see two things here. The

    green dot is the particle and the white green dot is the particle and the white
    green dot is the particle and the white

    line is the trajectory followed by that line is the trajectory followed by that
    line is the trajectory followed by that

    particle. particle. particle.

    But in the background what do we see? We But in the background what do we see?
    We But in the background what do we see? We

    see these arrows are constantly changing see these arrows are constantly changing
    see these arrows are constantly changing

    with time. This is because with time. This is because with time. This is because

    as the particle moves the time is also as the particle moves the time is also
    as the particle moves the time is also

    changing and the velocity vector field changing and the velocity vector field
    changing and the velocity vector field

    at every time is different. So these at every time is different. So these at every
    time is different. So these

    arrows represent the vector field. arrows represent the vector field. arrows represent
    the vector field.

    Maybe I can uh denote it using a label Maybe I can uh denote it using a label
    Maybe I can uh denote it using a label

    over here. So these arrows over here. So these arrows over here. So these arrows

    they represent the vector field which is they represent the vector field which
    is'
  concept_slugs:
  - continuous-normalizing-flow
  - flow-matching
- idx: 19
  start_sec: 1266.88
  end_sec: 1341.029
  text: 'they represent the vector field which is

    time dependent. That is why the arrows time dependent. That is why the arrows
    time dependent. That is why the arrows

    are changing with time. And if we know are changing with time. And if we know
    are changing with time. And if we know

    the time dependent vector field by using the time dependent vector field by using
    the time dependent vector field by using

    the above differential equation, we can the above differential equation, we can
    the above differential equation, we can

    exactly pinpoint how each particle will exactly pinpoint how each particle will
    exactly pinpoint how each particle will

    move according to these time dependent move according to these time dependent
    move according to these time dependent

    vector fields. So to answer this question, we need to So to answer this question,
    we need to

    solve the above differential equation. solve the above differential equation.
    solve the above differential equation.

    Now the idea is simple. We use velocity Now the idea is simple. We use velocity
    Now the idea is simple. We use velocity

    vectors to advance the point in small vectors to advance the point in small vectors
    to advance the point in small

    time increments. This is something we time increments. This is something we time
    increments. This is something we

    saw in the previous example also that if saw in the previous example also that
    if saw in the previous example also that if

    we have the velocity vector [snorts] uh we have the velocity vector [snorts] uh
    we have the velocity vector [snorts] uh

    we use we we use we we use we

    convert dx by dt as delta x by delta t convert dx by dt as delta x by delta t
    convert dx by dt as delta x by delta t

    and then we can calculate the individual and then we can calculate the individual
    and then we can calculate the individual

    displacements of each point because of displacements of each point because of
    displacements of each point because of

    these vector fields. the white line is something that we have the white line is
    something that we have

    got as the trajectory of the particle got as the trajectory of the particle got
    as the trajectory of the particle

    but it is not quite correct because at'
  concept_slugs:
  - continuous-normalizing-flow
  - flow-matching
- idx: 20
  start_sec: 1341.029
  end_sec: 1418.39
  text: 'but it is not quite correct because at but it is not quite correct because
    at

    the end of it we are doing an the end of it we are doing an the end of it we are
    doing an

    approximation. approximation. approximation.

    We are not calculating the exact vector We are not calculating the exact vector
    We are not calculating the exact vector

    field but we are replacing dx by dt by field but we are replacing dx by dt by
    field but we are replacing dx by dt by

    delta x by delta t. delta x by delta t. delta x by delta t.

    And that is why we are calculating an And that is why we are calculating an And
    that is why we are calculating an

    approximate approximate approximate

    trajectory of the particle. So you can trajectory of the particle. So you can
    trajectory of the particle. So you can

    see the difference between these white see the difference between these white
    see the difference between these white

    lines and the gray lines. lines and the gray lines. lines and the gray lines.

    And this discrepancy appears because of And this discrepancy appears because of
    And this discrepancy appears because of

    the way we have discretized the the way we have discretized the the way we have
    discretized the

    differential equation. Okay. So this is the first part which is Okay. So this
    is the first part which is

    understanding time dependent vector understanding time dependent vector understanding
    time dependent vector

    fields. fields. fields.

    Understanding how these vector fields Understanding how these vector fields Understanding
    how these vector fields

    can be used to find the trajectories of can be used to find the trajectories of
    can be used to find the trajectories of

    all the particles in space using a all the particles in space using a all the
    particles in space using a

    simple ordinary differential equation. Okay, let''s move ahead now and we will
    Okay, let''s move ahead now and we will

    define [snorts] what is flow. define [snorts] what is flow. define [snorts] what
    is flow.

    In the literature, you will see flow In the literature, you will see flow In the
    literature, you will see flow

    models as the terminology used models as the terminology used models as the terminology
    used

    everywhere in a lot of papers. But flow'
  concept_slugs:
  - continuous-normalizing-flow
  - flow-matching
- idx: 21
  start_sec: 1418.39
  end_sec: 1474.0
  text: 'everywhere in a lot of papers. But flow everywhere in a lot of papers. But
    flow

    means something very specific. In our means something very specific. In our means
    something very specific. In our

    mind, we know flow means something is mind, we know flow means something is mind,
    we know flow means something is

    moving. But we will moving. But we will moving. But we will

    u try to understand it in a bit more u try to understand it in a bit more u try
    to understand it in a bit more

    rigorous manner to understand what rigorous manner to understand what rigorous
    manner to understand what

    exactly is flow. it will turn out that exactly is flow. it will turn out that
    exactly is flow. it will turn out that

    it is exactly the same. Uh it it really it is exactly the same. Uh it it really
    it is exactly the same. Uh it it really

    matches our physical intuition. matches our physical intuition. matches our physical
    intuition.

    So what my physical intuition tells me So what my physical intuition tells me
    So what my physical intuition tells me

    is that let''s say is that let''s say is that let''s say

    um you have um you have um you have

    a collection of thousand particles and a collection of thousand particles and
    a collection of thousand particles and

    these thousand particles are moving in these thousand particles are moving in
    these thousand particles are moving in

    space. So the flow is something which space. So the flow is something which space.
    So the flow is something which

    tells you the trajectories of these tells you the trajectories of these tells
    you the trajectories of these

    thousand particles and it it''s it''s thousand particles and it it''s it''s thousand
    particles and it it''s it''s

    basically a collection of the basically a collection of the basically a collection
    of the

    trajectories of all of these particles trajectories of all of these particles
    trajectories of all of these particles

    in in space and that is exactly true in in space and that is exactly true in in
    space and that is exactly true

    according to the formal definition the according to the formal definition the
    according to the formal definition the

    flow is a collection of trajectories flow is a collection of trajectories'
  concept_slugs:
  - continuous-normalizing-flow
  - flow-matching
- idx: 22
  start_sec: 1474.0
  end_sec: 1530.559
  text: 'flow is a collection of trajectories

    which evolve according to the velocity which evolve according to the velocity
    which evolve according to the velocity

    field. We have just seen that if we know field. We have just seen that if we know
    field. We have just seen that if we know

    the velocity vector field a time the velocity vector field a time the velocity
    vector field a time

    dependent velocity vector field we can dependent velocity vector field we can
    dependent velocity vector field we can

    calculate the trajectories of every calculate the trajectories of every calculate
    the trajectories of every

    individual particle. Now if we do this individual particle. Now if we do this
    individual particle. Now if we do this

    for all the particles in the space for all the particles in the space for all
    the particles in the space

    we will get the collective motion of the we will get the collective motion of
    the we will get the collective motion of the

    object which is called as flow. object which is called as flow. object which is
    called as flow.

    Let us understand this using a Let us understand this using a Let us understand
    this using a

    visualization. So visualization. So visualization. So

    here at the background in in gray what here at the background in in gray what
    here at the background in in gray what

    you see is the vector field which is you see is the vector field which is you
    see is the vector field which is

    marked in gray. Now I have taken a marked in gray. Now I have taken a marked in
    gray. Now I have taken a

    snapshot of one single time. Let''s say snapshot of one single time. Let''s say
    snapshot of one single time. Let''s say

    this is at time t equal to0. I have this is at time t equal to0. I have this is
    at time t equal to0. I have

    taken a snapshot. taken a snapshot. taken a snapshot.

    As time changes the gray velocity vector As time changes the gray velocity vector
    As time changes the gray velocity vector

    field is also going to change. But for field is also going to change. But for
    field is also going to change. But for

    now let us look at one single snapshot now let us look at one single snapshot'
  concept_slugs:
  - continuous-normalizing-flow
  - flow-matching
- idx: 23
  start_sec: 1530.559
  end_sec: 1581.679
  text: 'now let us look at one single snapshot

    because we have we have restricted with because we have we have restricted with
    because we have we have restricted with

    the screen in in front of us. Now you the screen in in front of us. Now you the
    screen in in front of us. Now you

    can see there are these blue dots. can see there are these blue dots. can see
    there are these blue dots.

    These blue dots are particles. These blue dots are particles. These blue dots
    are particles.

    Now I have for simplicity denoted a Now I have for simplicity denoted a Now I
    have for simplicity denoted a

    collection of 20 particles over here. collection of 20 particles over here. collection
    of 20 particles over here.

    But you can imagine these particles to But you can imagine these particles to
    But you can imagine these particles to

    be much much more. be much much more. be much much more.

    Now every particle starts at the blue Now every particle starts at the blue Now
    every particle starts at the blue

    point and it it evolves. This is the point and it it evolves. This is the point
    and it it evolves. This is the

    trajectory the way the particle moves trajectory the way the particle moves trajectory
    the way the particle moves

    with time. Now this trajectory is given with time. Now this trajectory is given
    with time. Now this trajectory is given

    or we can calculate this trajectory or we can calculate this trajectory or we
    can calculate this trajectory

    because we know the vector field. So for because we know the vector field. So
    for because we know the vector field. So for

    every single particle we know how the every single particle we know how the every
    single particle we know how the

    trajectory changes with time because we trajectory changes with time because we
    trajectory changes with time because we

    know the velocity vector field. And now know the velocity vector field. And now
    know the velocity vector field. And now

    you see we have collected all these you see we have collected all these you see
    we have collected all these

    trajectories and we get a overall sense trajectories and we get a overall sense'
  concept_slugs:
  - continuous-normalizing-flow
  - flow-matching
- idx: 24
  start_sec: 1581.679
  end_sec: 1629.76
  text: 'trajectories and we get a overall sense

    of the flow. You can see that this this of the flow. You can see that this this
    of the flow. You can see that this this

    is probably something which is swirling. is probably something which is swirling.
    is probably something which is swirling.

    It''s like a vortex. Um let''s say you It''s like a vortex. Um let''s say you
    It''s like a vortex. Um let''s say you

    take a bucket of water and you put your take a bucket of water and you put your
    take a bucket of water and you put your

    hand inside and you make a swirl. Then hand inside and you make a swirl. Then
    hand inside and you make a swirl. Then

    you will see something like this. Now you will see something like this. Now you
    will see something like this. Now

    it''s it it''s very simple to visualize it''s it it''s very simple to visualize
    it''s it it''s very simple to visualize

    what flow is. But if someone asks you what flow is. But if someone asks you what
    flow is. But if someone asks you

    how do you define flow more rigorously, how do you define flow more rigorously,
    how do you define flow more rigorously,

    you can say that flow is a collection of you can say that flow is a collection
    of you can say that flow is a collection of

    all trajectories for all particles which all trajectories for all particles which
    all trajectories for all particles which

    are there in that bucket of water. are there in that bucket of water. are there
    in that bucket of water.

    Okay. So uh another interesting way to Okay. So uh another interesting way to
    Okay. So uh another interesting way to

    visualize how flow is is to place a visualize how flow is is to place a visualize
    how flow is is to place a

    small grid on space and see how it small grid on space and see how it small grid
    on space and see how it

    deforms. So for this same above example, deforms. So for this same above example,
    deforms. So for this same above example,

    let''s let''s see how the grid deforms. let''s let''s see how the grid deforms.'
  concept_slugs:
  - continuous-normalizing-flow
  - flow-matching
- idx: 25
  start_sec: 1629.76
  end_sec: 1689.52
  text: 'let''s let''s see how the grid deforms.

    Now note that the grid is going to Now note that the grid is going to Now note
    that the grid is going to

    deform in a way that the vector field deform in a way that the vector field deform
    in a way that the vector field

    exists in the space. So because we have exists in the space. So because we have
    exists in the space. So because we have

    a swirling flow, every single point in a swirling flow, every single point in
    a swirling flow, every single point in

    the grid is going to move according to a the grid is going to move according to
    a the grid is going to move according to a

    swirling trajectory. swirling trajectory. swirling trajectory.

    And uh we see a cumulative And uh we see a cumulative And uh we see a cumulative

    deformation of the grid. It looks kind deformation of the grid. It looks kind
    deformation of the grid. It looks kind

    of weird here right now, but that is of weird here right now, but that is of weird
    here right now, but that is

    what flow is. A flow is something which what flow is. A flow is something which
    what flow is. A flow is something which

    deforms a uniformly placed grid into deforms a uniformly placed grid into deforms
    a uniformly placed grid into

    something else because of which is something else because of which is something
    else because of which is

    governed by the velocity vector field. So this is a technique which uh is So this
    is a technique which uh is

    generally used to visualize the flows. generally used to visualize the flows.
    generally used to visualize the flows.

    If if we place a square grid, so square If if we place a square grid, so square
    If if we place a square grid, so square

    grid is nothing but just uniformly grid is nothing but just uniformly grid is
    nothing but just uniformly

    placed points in in the space and every placed points in in the space and every
    placed points in in the space and every

    single point is going to evolve single point is going to evolve single point is
    going to evolve

    according to a trajectory which is according to a trajectory which is'
  concept_slugs:
  - continuous-normalizing-flow
  - flow-matching
- idx: 26
  start_sec: 1689.52
  end_sec: 1766.32
  text: 'according to a trajectory which is

    governed by an ordinary differential governed by an ordinary differential governed
    by an ordinary differential

    equation and if we collect all these equation and if we collect all these equation
    and if we collect all these

    trajectories together we get the flow. trajectories together we get the flow.
    trajectories together we get the flow.

    Now uh Now uh Now uh

    let''s look at an example to visualize let''s look at an example to visualize
    let''s look at an example to visualize

    this. So in this example we are going to So in this example we are going to

    visualize the flow using code. visualize the flow using code. visualize the flow
    using code.

    So I''ll just run this piece of cell and So I''ll just run this piece of cell
    and So I''ll just run this piece of cell and

    u this is exactly the same animation which I had shown me. So this animation which
    I had shown me. So this

    is the flow field and uh here is the is the flow field and uh here is the is the
    flow field and uh here is the

    code where I have defined the velocity code where I have defined the velocity
    code where I have defined the velocity

    vector field and the particles are vector field and the particles are vector field
    and the particles are

    evolving according to that velocity evolving according to that velocity evolving
    according to that velocity

    vector field over here. vector field over here. vector field over here.

    And then uh if you run the second piece And then uh if you run the second piece
    And then uh if you run the second piece

    of cell you''ll be able to see the of cell you''ll be able to see the of cell
    you''ll be able to see the

    deformation of the square grid as well. deformation of the square grid as well.
    deformation of the square grid as well.

    Probably this might not work. So I will Probably this might not work. So I will
    Probably this might not work. So I will

    u run the third piece of cell to u run the third piece of cell to u run the third
    piece of cell to

    understand how the grid deforms. Yeah. understand how the grid deforms. Yeah.'
  concept_slugs:
  - continuous-normalizing-flow
  - flow-matching
- idx: 27
  start_sec: 1766.32
  end_sec: 1834.399
  text: 'understand how the grid deforms. Yeah.

    So this this does work. So this this does work. So this this does work.

    Okay. So you can actually change these Okay. So you can actually change these
    Okay. So you can actually change these

    velocity vector fields uh in the velocity vector fields uh in the velocity vector
    fields uh in the

    description and uh you can you know play description and uh you can you know play
    description and uh you can you know play

    around with it and see how the flow around with it and see how the flow around
    with it and see how the flow

    changes according to the velocity vector changes according to the velocity vector
    changes according to the velocity vector

    fields which is rightly so because the fields which is rightly so because the
    fields which is rightly so because the

    velocity vector fields are governing the velocity vector fields are governing
    the velocity vector fields are governing the

    trajectories which are in turn governing trajectories which are in turn governing
    trajectories which are in turn governing

    the flow. So if you were to you know uh the flow. So if you were to you know uh
    the flow. So if you were to you know uh

    draw a sequence you can say that the draw a sequence you can say that the draw
    a sequence you can say that the

    sequence looks as follows. sequence looks as follows. sequence looks as follows.

    First is a velocity field. From the velocity field velocity field. From the velocity
    field

    you get trajectories and from the trajectories you get the and from the trajectories
    you get the

    flow. flow. flow.

    All these three things are related to All these three things are related to All
    these three things are related to

    each other. Okay. So this is the first step. Okay. So this is the first step.

    All of us at this point should All of us at this point should All of us at this
    point should

    understand three things. First is the understand three things. First is the understand
    three things. First is the

    velocity field which I''m interchangeably velocity field which I''m interchangeably
    velocity field which I''m interchangeably

    using the word vector field also. Second using the word vector field also. Second'
  concept_slugs:
  - continuous-normalizing-flow
  - flow-matching
- idx: 28
  start_sec: 1834.399
  end_sec: 1906.24
  text: 'using the word vector field also. Second

    is the trajectories which are calculated is the trajectories which are calculated
    is the trajectories which are calculated

    from the velocity field using the simple from the velocity field using the simple
    from the velocity field using the simple

    ordinary differential equation. And the ordinary differential equation. And the
    ordinary differential equation. And the

    third is flow which is the collection of third is flow which is the collection
    of third is flow which is the collection of

    all the trajectories in space. all the trajectories in space. all the trajectories
    in space.

    These three concepts are going to be These three concepts are going to be These
    three concepts are going to be

    very fundamental for us as we understand very fundamental for us as we understand
    very fundamental for us as we understand

    uh uh uh

    flow models in more depth. So once we flow models in more depth. So once we flow
    models in more depth. So once we

    understand this everything is built on understand this everything is built on
    understand this everything is built on

    top of these three concepts. Okay. Now let us take an example Okay. Now let us
    take an example

    and uh try to understand the flow in and uh try to understand the flow in and
    uh try to understand the flow in

    more depth using some practical more depth using some practical more depth using
    some practical

    examples. Okay. Okay. So the example that we will Okay. Okay. So the example that
    we will

    take is suppose we have a velocity field take is suppose we have a velocity field
    take is suppose we have a velocity field

    which is given by So first thing we can see is this So first thing we can see
    is this

    velocity field is dependent on velocity field is dependent on velocity field is
    dependent on

    um it''s it''s just a one-dimensional um it''s it''s just a one-dimensional um
    it''s it''s just a one-dimensional

    velocity field. In the above example we velocity field. In the above example we
    velocity field. In the above example we

    were considering two dimensions X and Y. were considering two dimensions X and
    Y. were considering two dimensions X and Y.

    It is only one dimensional minus theta x It is only one dimensional minus theta
    x'
  concept_slugs:
  - continuous-normalizing-flow
  - flow-matching
- idx: 29
  start_sec: 1906.24
  end_sec: 1972.48
  text: 'It is only one dimensional minus theta x

    and it is independent of time. So at and it is independent of time. So at and
    it is independent of time. So at

    every time snapshot you take a camera every time snapshot you take a camera every
    time snapshot you take a camera

    you take a photo of the space the you take a photo of the space the you take a
    photo of the space the

    velocity field will be exactly the same velocity field will be exactly the same
    velocity field will be exactly the same

    in all the photos which you have taken. in all the photos which you have taken.
    in all the photos which you have taken.

    Now uh [snorts] Now uh [snorts] Now uh [snorts]

    okay so okay so okay so

    we have to check whether the flow field we have to check whether the flow field
    we have to check whether the flow field

    is given by this formula. is given by this formula. is given by this formula.

    So given the velocity field then the So given the velocity field then the So given
    the velocity field then the

    flow field is given by this formula. But let us see whether that is actually But
    let us see whether that is actually

    true or not. true or not. true or not.

    Okay. So what do we know? Because the Okay. So what do we know? Because the Okay.
    So what do we know? Because the

    velocity field is given by this formula, velocity field is given by this formula,
    velocity field is given by this formula,

    we can use the differential equation we can use the differential equation we can
    use the differential equation

    that we have been talking about in this that we have been talking about in this
    that we have been talking about in this

    lecture multiple times. So that lecture multiple times. So that lecture multiple
    times. So that

    differential equation simply says dx by differential equation simply says dx by
    differential equation simply says dx by

    dt is equal to the velocity field which dt is equal to the velocity field which
    dt is equal to the velocity field which

    is dxt by dt is equal to minus theta of is dxt by dt is equal to minus theta of'
  concept_slugs:
  - continuous-normalizing-flow
  - flow-matching
- idx: 30
  start_sec: 1972.48
  end_sec: 2046.72
  text: 'is dxt by dt is equal to minus theta of

    xt. xt. xt.

    Now let''s see if this is indeed the Now let''s see if this is indeed the Now
    let''s see if this is indeed the

    flow. flow.

    If we substitute this in xt, it should If we substitute this in xt, it should
    If we substitute this in xt, it should

    satisfy this equation. So let us see if satisfy this equation. So let us see if
    satisfy this equation. So let us see if

    that actually happens or not. If xt is that actually happens or not. If xt is
    that actually happens or not. If xt is

    equal to equal to equal to

    e^ minus theta tx0, then dxt by dt then dxt by dt

    [clears throat] [clears throat]

    is equal to minus theta e raus theta t is equal to minus theta e raus theta t
    is equal to minus theta e raus theta t

    x0 x0 x0

    which is equal to minus theta xt. which is equal to minus theta xt. which is equal
    to minus theta xt.

    So it does satisfy the differential So it does satisfy the differential So it
    does satisfy the differential

    equation. equation. equation.

    Now remember we said that the flow is a Now remember we said that the flow is
    a Now remember we said that the flow is a

    collection of trajectories. This is the collection of trajectories. This is the
    collection of trajectories. This is the

    collection of trajectories. Depending on the initial position Depending on the
    initial position

    you exactly get how the particle changes you exactly get how the particle changes
    you exactly get how the particle changes

    or moves with time. Let''s see how to or moves with time. Let''s see how to or
    moves with time. Let''s see how to

    visualize this. It''s it''s very visualize this. It''s it''s very visualize this.
    It''s it''s very

    interesting. So if x0 is 0, interesting. So if x0 is 0, interesting. So if x0
    is 0,

    you simply get a straight line because you simply get a straight line because
    you simply get a straight line because

    theta is equal to zero or this this this theta is equal to zero or this this this
    theta is equal to zero or this this this

    is itself completely zero. So the is itself completely zero. So the'
  concept_slugs:
  - continuous-normalizing-flow
  - flow-matching
- idx: 31
  start_sec: 2046.72
  end_sec: 2112.48
  text: 'is itself completely zero. So the

    position stays zero. But position stays zero. But position stays zero. But

    let''s look at yeah if x0 is any any any let''s look at yeah if x0 is any any
    any let''s look at yeah if x0 is any any any

    positive number then it will simply look positive number then it will simply look
    positive number then it will simply look

    like an exponential curve. For example, like an exponential curve. For example,
    like an exponential curve. For example,

    if x0 is 3, then it will be 3 e to minus if x0 is 3, then it will be 3 e to minus
    if x0 is 3, then it will be 3 e to minus

    theta t. theta t. theta t.

    So it will decrease like this. And So it will decrease like this. And So it will
    decrease like this. And

    similarly for positive and negative x we similarly for positive and negative x
    we similarly for positive and negative x we

    can check. So this is how the flow looks can check. So this is how the flow looks
    can check. So this is how the flow looks

    like for a simple linear ordinary like for a simple linear ordinary like for a
    simple linear ordinary

    differential equation. differential equation. differential equation.

    Now why is this a flow? Because this is Now why is this a flow? Because this is
    Now why is this a flow? Because this is

    a collection of trajectories. Given the a collection of trajectories. Given the
    a collection of trajectories. Given the

    initial position of my particle, I can initial position of my particle, I can
    initial position of my particle, I can

    exactly pinpoint how the particle moves exactly pinpoint how the particle moves
    exactly pinpoint how the particle moves

    with time. and a collection of all these with time. and a collection of all these
    with time. and a collection of all these

    trajectories is going to help me trajectories is going to help me trajectories
    is going to help me

    identify what my flow is. So we can uh visualize this using the So we can uh visualize
    this using the

    same Google collab notebook and um you can see here I have taken the same you
    can see here I have taken the same

    example example'
  concept_slugs:
  - continuous-normalizing-flow
  - flow-matching
- idx: 32
  start_sec: 2112.48
  end_sec: 2163.839
  text: 'example

    x0 into e to minus theta t and we get the exact same plot. and we get the exact
    same plot.

    So we can actually play this and see how So we can actually play this and see
    how So we can actually play this and see how

    the uh particles move with time. So the the uh particles move with time. So the
    the uh particles move with time. So the

    particles start at so all these particles start at so all these particles start
    at so all these

    particles are let''s say attached on a particles are let''s say attached on a
    particles are let''s say attached on a

    string they start at a different string they start at a different string they
    start at a different

    location and all of them are moving and location and all of them are moving and
    location and all of them are moving and

    um going towards [clears throat] zero um going towards [clears throat] zero um
    going towards [clears throat] zero

    finally all of them are going to end up finally all of them are going to end up
    finally all of them are going to end up

    at zero. So this is almost like a sink. at zero. So this is almost like a sink.
    at zero. So this is almost like a sink.

    Imagine you have a sink and you start Imagine you have a sink and you start Imagine
    you have a sink and you start

    the particles anywhere. Every particle the particles anywhere. Every particle
    the particles anywhere. Every particle

    moves towards the sink and ends up in moves towards the sink and ends up in moves
    towards the sink and ends up in

    the sink. So that is the flow. the sink. So that is the flow. the sink. So that
    is the flow.

    Okay. So now with this example uh I hope Okay. So now with this example uh I hope
    Okay. So now with this example uh I hope

    we have understood what flow is how the we have understood what flow is how the
    we have understood what flow is how the

    flow is related to the velocity vector flow is related to the velocity vector
    flow is related to the velocity vector

    field and how the flow is a collection field and how the flow is a collection'
  concept_slugs:
  - continuous-normalizing-flow
  - flow-matching
- idx: 33
  start_sec: 2163.839
  end_sec: 2226.0
  text: 'field and how the flow is a collection

    of the trajectories. of the trajectories. of the trajectories.

    [snorts] Okay. Now uh once we are getting Okay. Now uh once we are getting

    confident with the definitions of confident with the definitions of confident
    with the definitions of

    velocity fields and flow let us move on. velocity fields and flow let us move
    on. velocity fields and flow let us move on.

    So the question is and we have already So the question is and we have already
    So the question is and we have already

    looked at this briefly. If we have a OD looked at this briefly. If we have a OD
    looked at this briefly. If we have a OD

    which is an ordinary differential which is an ordinary differential which is an
    ordinary differential

    equation, how do we simulate it and find equation, how do we simulate it and find
    equation, how do we simulate it and find

    the trajectories? I have said before that um once you have I have said before
    that um once you have

    the vector field you''ll be able to find the vector field you''ll be able to find
    the vector field you''ll be able to find

    the trajectories and I have briefly the trajectories and I have briefly the trajectories
    and I have briefly

    explained it here as well how that can explained it here as well how that can
    explained it here as well how that can

    be done but maybe we can uh explain it a be done but maybe we can uh explain it
    a be done but maybe we can uh explain it a

    bit more formally. bit more formally. bit more formally.

    So the method to do that is called as So the method to do that is called as So
    the method to do that is called as

    the oiler method. the oiler method. the oiler method.

    And what I oiler method says is we And what I oiler method says is we And what
    I oiler method says is we

    simply take steps in the direction of simply take steps in the direction of simply
    take steps in the direction of

    the velocity field. the velocity field. the velocity field.

    We take small steps in the direction of We take small steps in the direction of'
  concept_slugs:
  - continuous-normalizing-flow
  - flow-matching
- idx: 34
  start_sec: 2226.0
  end_sec: 2276.56
  text: 'We take small steps in the direction of

    the velocity field and we see how the the velocity field and we see how the the
    velocity field and we see how the

    particle trajectory changes with time. particle trajectory changes with time.
    particle trajectory changes with time.

    So for example, if we start here, we So for example, if we start here, we So for
    example, if we start here, we

    take a tiny step, we go here. We take take a tiny step, we go here. We take take
    a tiny step, we go here. We take

    another tiny step, we go here. We take another tiny step, we go here. We take
    another tiny step, we go here. We take

    another tiny step, we go here. We take another tiny step, we go here. We take

    another tiny step, we go here. So the another tiny step, we go here. So the another
    tiny step, we go here. So the

    velocity field will help us to take velocity field will help us to take velocity
    field will help us to take

    these tiny steps. these tiny steps. these tiny steps.

    And this is the same thing which we have And this is the same thing which we have
    And this is the same thing which we have

    outlined here. It looks slightly outlined here. It looks slightly outlined here.
    It looks slightly

    detailed, but let''s understand this. detailed, but let''s understand this. detailed,
    but let''s understand this.

    Okay. So as an input, we have a vector Okay. So as an input, we have a vector
    Okay. So as an input, we have a vector

    field which changes with time. We have field which changes with time. We have
    field which changes with time. We have

    initial condition x0 initial condition x0 initial condition x0

    and uh we have the number of steps n and uh we have the number of steps n and
    uh we have the number of steps n

    which is how many times you are going to which is how many times you are going
    to which is how many times you are going to

    update the particle trajectory for how update the particle trajectory for how
    update the particle trajectory for how

    long is your simulation carried on. long is your simulation carried on.'
  concept_slugs:
  - continuous-normalizing-flow
  - flow-matching
- idx: 35
  start_sec: 2276.56
  end_sec: 2336.48
  text: 'long is your simulation carried on.

    Okay. So we initialize time as t equal Okay. So we initialize time as t equal
    Okay. So we initialize time as t equal

    to0. The step size which is delta t is 1 to0. The step size which is delta t is
    1 to0. The step size which is delta t is 1

    by n. by n. by n.

    And uh the basic idea is which is given And uh the basic idea is which is given
    And uh the basic idea is which is given

    here. dx by dt is equal to mu here. dx by dt is equal to mu here. dx by dt is
    equal to mu

    u rather. So delta x by delta t is equal u rather. So delta x by delta t is equal
    u rather. So delta x by delta t is equal

    to d u. So we can write delta x as u * to d u. So we can write delta x as u *
    to d u. So we can write delta x as u *

    delta t. delta t. delta t.

    Okay. And delta x is x t + delta t minus Okay. And delta x is x t + delta t minus
    Okay. And delta x is x t + delta t minus

    xt is equal to u * delta t. xt is equal to u * delta t. xt is equal to u * delta
    t.

    Now here delta t is replaced by h. Now here delta t is replaced by h. Now here
    delta t is replaced by h.

    So x of t + h is equal to xt + h into u So x of t + h is equal to xt + h into
    u So x of t + h is equal to xt + h into u

    which is what is mentioned over here. which is what is mentioned over here. which
    is what is mentioned over here.

    This is how we update the position of This is how we update the position of This
    is how we update the position of

    the particle to calculate the next the particle to calculate the next the particle
    to calculate the next

    position. That is all is mentioned in position. That is all is mentioned in'
  concept_slugs:
  - continuous-normalizing-flow
  - flow-matching
- idx: 36
  start_sec: 2336.48
  end_sec: 2385.68
  text: 'position. That is all is mentioned in

    the flowchart. So basically the flowchart. So basically the flowchart. So basically

    if we have a particle and if we know the if we have a particle and if we know
    the if we have a particle and if we know the

    velocity vector field we take small velocity vector field we take small velocity
    vector field we take small

    increments in time we change this delta increments in time we change this delta
    increments in time we change this delta

    x this moves here now now we again x this moves here now now we again x this moves
    here now now we again

    change it we again change it we again change it we again change it we again change
    it we again change it we again

    change it and we do it till the time we change it and we do it till the time we
    change it and we do it till the time we

    are ending the simulation are ending the simulation are ending the simulation

    this is also called as the oiler method this is also called as the oiler method
    this is also called as the oiler method

    so the reason why we are describing this so the reason why we are describing this
    so the reason why we are describing this

    is if we know the velocity vector field is if we know the velocity vector field
    is if we know the velocity vector field

    at every time we can calculate the at every time we can calculate the at every
    time we can calculate the

    trajectories of the particles very trajectories of the particles very trajectories
    of the particles very

    precisely precisely precisely

    and this is something we should keep in and this is something we should keep in
    and this is something we should keep in

    mind. We are going to utilize this mind. We are going to utilize this mind. We
    are going to utilize this

    later. This is what is being used in the later. This is what is being used in
    the later. This is what is being used in the

    inference for the flow models. inference for the flow models. inference for the
    flow models.

    For example, when we are using flow For example, when we are using flow'
  concept_slugs:
  - continuous-normalizing-flow
  - flow-matching
- idx: 37
  start_sec: 2385.68
  end_sec: 2446.15
  text: 'For example, when we are using flow

    models for robotics or protein models for robotics or protein models for robotics
    or protein

    synthesis, synthesis, synthesis,

    people calculate the flow which is the people calculate the flow which is the
    people calculate the flow which is the

    trajectories of the particles but or the trajectories of the particles but or
    the trajectories of the particles but or the

    velocity vector field which governs the velocity vector field which governs the
    velocity vector field which governs the

    trajectories of the particles. But from trajectories of the particles. But from
    trajectories of the particles. But from

    there, how do you calculate the there, how do you calculate the there, how do
    you calculate the

    trajectories itself? trajectories itself? trajectories itself?

    Then you have to solve that differential Then you have to solve that differential
    Then you have to solve that differential

    equation which gives you the equation which gives you the equation which gives
    you the

    trajectories of these individual trajectories of these individual trajectories
    of these individual

    particles. particles. particles.

    So the inference happens by solving an So the inference happens by solving an
    So the inference happens by solving an

    ordinary differential equation which is ordinary differential equation which is
    ordinary differential equation which is

    a very unique property of the flow a very unique property of the flow a very unique
    property of the flow

    models. models. models.

    Remember this never happened in Remember this never happened in Remember this
    never happened in

    diffusion. This never happened in VA. diffusion. This never happened in VA. diffusion.
    This never happened in VA.

    In diffusion the inference happened by In diffusion the inference happened by
    In diffusion the inference happened by

    repeated sampling from noise to data. We repeated sampling from noise to data.
    We repeated sampling from noise to data. We

    did not sample a differential equation. did not sample a differential equation.
    did not sample a differential equation.

    In uh variational autoenccoders we In uh variational autoenccoders we In uh variational
    autoenccoders we

    trained a neural network to predict trained a neural network to predict trained
    a neural network to predict

    images. There also we did not have a images. There also we did not have a images.
    There also we did not have a

    differential equation. This is what differential equation. This is what differential
    equation. This is what

    makes flow models unique.'
  concept_slugs:
  - continuous-normalizing-flow
  - flow-matching
- idx: 38
  start_sec: 2449.589
  end_sec: 2501.589
  text: 'Now we have defined the word flow in the Now we have defined the word flow
    in the

    initial part of the lecture. We will initial part of the lecture. We will initial
    part of the lecture. We will

    understand what is the meaning of flow understand what is the meaning of flow
    understand what is the meaning of flow

    models models models

    which is the whole title of today''s which is the whole title of today''s which
    is the whole title of today''s

    lecture is flow models. Right? We have lecture is flow models. Right? We have
    lecture is flow models. Right? We have

    just looked at the meaning of the word just looked at the meaning of the word
    just looked at the meaning of the word

    flow. flow.

    So let''s start with our original goal of So let''s start with our original goal
    of So let''s start with our original goal of

    deep generative models. deep generative models. deep generative models.

    Given we have let''s say images of cats. Given we have let''s say images of cats.
    Given we have let''s say images of cats.

    We want to find the distribution which We want to find the distribution which
    We want to find the distribution which

    governs these images. governs these images. governs these images.

    So our goal is to find a complex So our goal is to find a complex So our goal
    is to find a complex

    distribution which is P data. But we do distribution which is P data. But we do
    distribution which is P data. But we do

    not have P data. All we have is a simple not have P data. All we have is a simple
    not have P data. All we have is a simple

    distribution which is P init which maybe distribution which is P init which maybe
    distribution which is P init which maybe

    it is a Gshian distribution. it is a Gshian distribution. it is a Gshian distribution.

    Remember what we did in diffusion Remember what we did in diffusion Remember what
    we did in diffusion

    models. We started with noise and we models. We started with noise and we models.
    We started with noise and we

    ended with the data distribution. ended with the data distribution. ended with
    the data distribution.

    So this is exactly what we are going to'
  concept_slugs:
  - continuous-normalizing-flow
  - flow-matching
- idx: 39
  start_sec: 2501.589
  end_sec: 2585.589
  text: 'So this is exactly what we are going to So this is exactly what we are going
    to

    do in flow models. Also our goal is to do in flow models. Also our goal is to
    do in flow models. Also our goal is to

    convert a simple distribution pinet to a convert a simple distribution pinet to
    a convert a simple distribution pinet to a

    complex distribution which is P data. complex distribution which is P data. complex
    distribution which is P data.

    But we do not know what is P data. Okay. So now let us understand how we Okay.
    So now let us understand how we

    are going to convert the simple are going to convert the simple are going to convert
    the simple

    distribution to a complex distribution distribution to a complex distribution
    distribution to a complex distribution

    and the simulation of a ordinary and the simulation of a ordinary and the simulation
    of a ordinary

    differential equation is a natural differential equation is a natural differential
    equation is a natural

    choice for this transformation. A flow model is described by the A flow model
    is described by the

    following ordinary differential following ordinary differential following ordinary
    differential

    equation. Okay. So Okay. So

    how the ordinary differential is how the ordinary differential is how the ordinary
    differential is

    equation is given by is equation is given by is equation is given by is

    x0 is the initial distribution that we x0 is the initial distribution that we
    x0 is the initial distribution that we

    start out with. It can be complete start out with. It can be complete start out
    with. It can be complete

    noise. It can be a gshian distribution. noise. It can be a gshian distribution.
    noise. It can be a gshian distribution.

    And And And

    now instead of making the particles now instead of making the particles now instead
    of making the particles

    evolve with time according to evolve with time according to evolve with time according
    to

    differential equation. differential equation.

    Now the main difference here is that we Now the main difference here is that we
    Now the main difference here is that we

    make the probability distribution itself make the probability distribution itself
    make the probability distribution itself

    change with time. change with time. change with time.

    So we use the same ordinary differential'
  concept_slugs:
  - continuous-normalizing-flow
  - flow-matching
- idx: 40
  start_sec: 2585.589
  end_sec: 2638.79
  text: 'So we use the same ordinary differential So we use the same ordinary differential

    equation dx by dt is equal to u. But equation dx by dt is equal to u. But equation
    dx by dt is equal to u. But

    this time the main difference is that so this time the main difference is that
    so this time the main difference is that so

    far we have been looking at individual far we have been looking at individual
    far we have been looking at individual

    particles right. We have been looking at particles right. We have been looking
    at particles right. We have been looking at

    the movement of those particles. the movement of those particles. the movement
    of those particles.

    Now what we are doing is Now what we are doing is Now what we are doing is

    we still have particles but these we still have particles but these we still have
    particles but these

    particles are a part of a distribution particles are a part of a distribution
    particles are a part of a distribution

    of a probability distribution. of a probability distribution. of a probability
    distribution.

    So we are still evolving the So we are still evolving the So we are still evolving
    the

    trajectories of the particles but now trajectories of the particles but now trajectories
    of the particles but now

    these particles as a unit are these particles as a unit are these particles as
    a unit are

    representing something. representing something. representing something.

    For example let''s say we have 100 For example let''s say we have 100 For example
    let''s say we have 100

    particles in a space in a box. Okay. And particles in a space in a box. Okay.
    And particles in a space in a box. Okay. And

    these particles are evolving with time. these particles are evolving with time.
    these particles are evolving with time.

    they are going in space according to the they are going in space according to
    the they are going in space according to the

    velocity field. We have just understood velocity field. We have just understood
    velocity field. We have just understood

    how that works. Now the only thing which how that works. Now the only thing which
    how that works. Now the only thing which

    we have added in flow model is that the'
  concept_slugs:
  - continuous-normalizing-flow
  - flow-matching
- idx: 41
  start_sec: 2638.79
  end_sec: 2694.39
  text: 'we have added in flow model is that the we have added in flow model is that
    the

    collection of these particles represent collection of these particles represent
    collection of these particles represent

    a distribution. a distribution. a distribution.

    So initially we start with a normal So initially we start with a normal So initially
    we start with a normal

    distribution which is a gshian distribution which is a gshian distribution which
    is a gshian

    distribution and then we have to make distribution and then we have to make distribution
    and then we have to make

    the particles flow such that from the the particles flow such that from the the
    particles flow such that from the

    normal distribution you move to the normal distribution you move to the normal
    distribution you move to the

    distribution that you want to calculate. distribution that you want to calculate.
    distribution that you want to calculate.

    That is why it is called a flow model. A That is why it is called a flow model.
    A That is why it is called a flow model. A

    flow is a collection of particles flow is a collection of particles flow is a
    collection of particles

    evolving according to trajectories. A evolving according to trajectories. A evolving
    according to trajectories. A

    flow model is a collection of particles flow model is a collection of particles
    flow model is a collection of particles

    which take the initial distribution and which take the initial distribution and
    which take the initial distribution and

    convert it into the actual probability convert it into the actual probability
    convert it into the actual probability

    distribution which we want to predict. distribution which we want to predict.
    distribution which we want to predict.

    So this is what I have mentioned here. So this is what I have mentioned here.
    So this is what I have mentioned here.

    Our goal is to make the end point x1 of Our goal is to make the end point x1 of
    Our goal is to make the end point x1 of

    the trajectory have the distribution p the trajectory have the distribution p
    the trajectory have the distribution p

    data. data. data.

    In all of these models, the time always In all of these models, the time always
    In all of these models, the time always

    evolves from t =0 to t = 1.'
  concept_slugs:
  - continuous-normalizing-flow
  - flow-matching
- idx: 42
  start_sec: 2694.39
  end_sec: 2757.68
  text: 'evolves from t =0 to t = 1. evolves from t =0 to t = 1.

    So this is sort of what we want. We want So this is sort of what we want. We want
    So this is sort of what we want. We want

    to start from the initial distribution to start from the initial distribution
    to start from the initial distribution

    and we want to move at x1. We want to and we want to move at x1. We want to and
    we want to move at x1. We want to

    move to the data distribution. move to the data distribution. move to the data
    distribution.

    Now all of you might have some ideas in Now all of you might have some ideas in
    Now all of you might have some ideas in

    your mind related to flow models and you your mind related to flow models and
    you your mind related to flow models and you

    might have visualized this in a certain might have visualized this in a certain
    might have visualized this in a certain

    way in your mind but we cannot truly way in your mind but we cannot truly way
    in your mind but we cannot truly

    understand this unless we look at some understand this unless we look at some
    understand this unless we look at some

    practical examples. practical examples. practical examples.

    So there is an extremely interesting So there is an extremely interesting So there
    is an extremely interesting

    Google collab notebook which uh Google collab notebook which uh Google collab
    notebook which uh

    I have opened up I have opened up I have opened up

    here. Now here the interesting thing is here. Now here the interesting thing is
    here. Now here the interesting thing is

    first let us run the first cell. So I''m going to show you how to convert So I''m
    going to show you how to convert

    probability distributions from an probability distributions from an probability
    distributions from an

    initial distribution to a final initial distribution to a final initial distribution
    to a final

    distribution which you want to predict. Okay. So now here you can see this is
    Okay. So now here you can see this is

    the start distribution which is a simple the start distribution which is a simple'
  concept_slugs:
  - continuous-normalizing-flow
  - flow-matching
- idx: 43
  start_sec: 2757.68
  end_sec: 2807.52
  text: 'the start distribution which is a simple

    gshian. It is uniformly distributed. gshian. It is uniformly distributed. gshian.
    It is uniformly distributed.

    There are maybe around 2,000 particles There are maybe around 2,000 particles
    There are maybe around 2,000 particles

    here. So there are 2,000 particles in here. So there are 2,000 particles in here.
    So there are 2,000 particles in

    the space. And these particles represent the space. And these particles represent
    the space. And these particles represent

    a distribution. They represent a uniform a distribution. They represent a uniform
    a distribution. They represent a uniform

    distribution. distribution. distribution.

    Okay. And now Okay. And now Okay. And now

    let us say the distribution that we want let us say the distribution that we want
    let us say the distribution that we want

    to predict which is X1. It looks like to predict which is X1. It looks like to
    predict which is X1. It looks like

    this. It is the shape of a heart. Now this. It is the shape of a heart. Now this.
    It is the shape of a heart. Now

    this also has 200 points. But it has a this also has 200 points. But it has a
    this also has 200 points. But it has a

    very specific distribution, right? It is very specific distribution, right? It
    is very specific distribution, right? It is

    it it is not like uniform distribution it it is not like uniform distribution
    it it is not like uniform distribution

    but it is our data distribution. but it is our data distribution. but it is our
    data distribution.

    In reality we will not be knowing this In reality we will not be knowing this
    In reality we will not be knowing this

    also but now I''m assuming that we know also but now I''m assuming that we know
    also but now I''m assuming that we know

    the start distribution and we know the the start distribution and we know the
    the start distribution and we know the

    end distribution and we are going to end distribution and we are going to end
    distribution and we are going to

    understand how a flow model takes you understand how a flow model takes you understand
    how a flow model takes you

    from the start distribution to the end from the start distribution to the end'
  concept_slugs:
  - continuous-normalizing-flow
  - flow-matching
- idx: 44
  start_sec: 2807.52
  end_sec: 2862.23
  text: 'from the start distribution to the end

    distribution. Now here there are a lot of options. We Now here there are a lot
    of options. We

    can convert can convert can convert

    we can change the end distribution to we can change the end distribution to we
    can change the end distribution to

    maybe a spiral data also. We can change maybe a spiral data also. We can change
    maybe a spiral data also. We can change

    it to uh goshian data. But again gshian it to uh goshian data. But again gshian
    it to uh goshian data. But again gshian

    data will not make sense. So we have two data will not make sense. So we have
    two data will not make sense. So we have two

    options maybe spiral data and hard data options maybe spiral data and hard data
    options maybe spiral data and hard data

    over here. over here. over here.

    Now uh there are some parts here which Now uh there are some parts here which
    Now uh there are some parts here which

    will become clear as we go along in the will become clear as we go along in the
    will become clear as we go along in the

    next two lectures. next two lectures. next two lectures.

    For now here I have defined the flow For now here I have defined the flow For
    now here I have defined the flow

    model by a neural network which takes a model by a neural network which takes
    a model by a neural network which takes a

    position x and time t and outputs a position x and time t and outputs a position
    x and time t and outputs a

    velocity vector. This is the velocity velocity vector. This is the velocity velocity
    vector. This is the velocity

    vector field which we have been talking vector field which we have been talking
    vector field which we have been talking

    about since the start of the lecture. about since the start of the lecture. about
    since the start of the lecture.

    Now one crucial thing we have done here Now one crucial thing we have done here
    Now one crucial thing we have done here

    is the velocity vector field has been is the velocity vector field has been is
    the velocity vector field has been

    replaced by a neural network.'
  concept_slugs:
  - continuous-normalizing-flow
  - flow-matching
- idx: 45
  start_sec: 2862.23
  end_sec: 2909.28
  text: 'replaced by a neural network. replaced by a neural network.

    So there is another word for this in So there is another word for this in So there
    is another word for this in

    literature which is also called as a literature which is also called as a literature
    which is also called as a

    neural OD neural OD neural OD

    which is a neural ordinary differential which is a neural ordinary differential
    which is a neural ordinary differential

    equation. equation.

    It is very similar to what we discussed It is very similar to what we discussed
    It is very similar to what we discussed

    before. The only thing is that the input before. The only thing is that the input
    before. The only thing is that the input

    is the same X and T. The output is still is the same X and T. The output is still
    is the same X and T. The output is still

    the velocity vector but inside you have the velocity vector but inside you have
    the velocity vector but inside you have

    a bunch of neurons. Now this velocity field is defined here. Now this velocity
    field is defined here.

    So let me run this. Um and then we carry So let me run this. Um and then we carry
    So let me run this. Um and then we carry

    the training process. The training the training process. The training the training
    process. The training

    process is very interesting and it''s process is very interesting and it''s process
    is very interesting and it''s

    extremely simple but as I said before to extremely simple but as I said before
    to extremely simple but as I said before to

    reach this simple point is going to take reach this simple point is going to take
    reach this simple point is going to take

    us some time. So right now I don''t us some time. So right now I don''t us some
    time. So right now I don''t

    expect you to understand the training expect you to understand the training expect
    you to understand the training

    process but here you can see the flow process but here you can see the flow process
    but here you can see the flow

    model is being trained and the loss is model is being trained and the loss is'
  concept_slugs:
  - continuous-normalizing-flow
  - flow-matching
- idx: 46
  start_sec: 2909.28
  end_sec: 2965.2
  text: 'model is being trained and the loss is

    going down. What is the meaning of this going down. What is the meaning of this
    going down. What is the meaning of this

    statement? The flow model is going to be statement? The flow model is going to
    be statement? The flow model is going to be

    trained. The meaning is that we are trained. The meaning is that we are trained.
    The meaning is that we are

    training the neural network given by the training the neural network given by
    the training the neural network given by the

    velocity vector field which are going to velocity vector field which are going
    to velocity vector field which are going to

    take these 2,000 particles in the take these 2,000 particles in the take these
    2,000 particles in the

    initial uniform shape. They are going to initial uniform shape. They are going
    to initial uniform shape. They are going to

    evolve the trajectories according to our evolve the trajectories according to
    our evolve the trajectories according to our

    differential equation such that the differential equation such that the differential
    equation such that the

    final shape will be the heart shape. Next step is to simulate the OD. Now Next
    step is to simulate the OD. Now

    this is where it gets very interesting this is where it gets very interesting
    this is where it gets very interesting

    and we use the uler step here. You see and we use the uler step here. You see
    and we use the uler step here. You see

    here how we are changing the here how we are changing the here how we are changing
    the

    uh trajectories of the particles uh trajectories of the particles uh trajectories
    of the particles

    according to the oiler step according to the oiler step according to the oiler
    step

    and we can see the real data and the and we can see the real data and the and
    we can see the real data and the

    generated data. A great way to visualize generated data. A great way to visualize
    generated data. A great way to visualize

    this is to see the animation and we can this is to see the animation and we can
    this is to see the animation and we can

    see the animation over here once this see the animation over here once this'
  concept_slugs:
  - continuous-normalizing-flow
  - flow-matching
- idx: 47
  start_sec: 2965.2
  end_sec: 3030.96
  text: 'see the animation over here once this

    code runs. Yeah. So let''s see uh as expected we Yeah. So let''s see uh as expected
    we

    start with the initial gshian start with the initial gshian start with the initial
    gshian

    distribution and then slowly the distribution and then slowly the distribution
    and then slowly the

    particles evolve and we start to she see particles evolve and we start to she
    see particles evolve and we start to she see

    the heart-shaped the heart-shaped the heart-shaped

    structure. So structure. So structure. So

    you can see how the particles are slowly you can see how the particles are slowly
    you can see how the particles are slowly

    compressing inside moving in and then compressing inside moving in and then compressing
    inside moving in and then

    also changing their shape or or moving also changing their shape or or moving
    also changing their shape or or moving

    according to lines where they start to according to lines where they start to
    according to lines where they start to

    resemble a heart shape. resemble a heart shape. resemble a heart shape.

    So this is this is very interesting and So this is this is very interesting and
    So this is this is very interesting and

    it''s almost like what we have done here it''s almost like what we have done here
    it''s almost like what we have done here

    is we have predicted a velocity field is we have predicted a velocity field is
    we have predicted a velocity field

    which can take a uniform distribution to which can take a uniform distribution
    to which can take a uniform distribution to

    a predicted distribution which we want a predicted distribution which we want
    a predicted distribution which we want

    and we can imagine the flow. The and we can imagine the flow. The and we can imagine
    the flow. The

    particles are flowing in in time. particles are flowing in in time. particles
    are flowing in in time.

    In variation autoenccoders we had an In variation autoenccoders we had an In variation
    autoenccoders we had an

    encoder we had a decoder. In diffusion encoder we had a decoder. In diffusion
    encoder we had a decoder. In diffusion

    models we had a number of encoders and a models we had a number of encoders and
    a'
  concept_slugs:
  - continuous-normalizing-flow
  - flow-matching
- idx: 48
  start_sec: 3030.96
  end_sec: 3123.599
  text: 'models we had a number of encoders and a

    number of decoders. number of decoders. number of decoders.

    So they were discrete. Here something a So they were discrete. Here something
    a So they were discrete. Here something a

    process happens which is continuous. So process happens which is continuous. So
    process happens which is continuous. So

    I find this transformation from the I find this transformation from the I find
    this transformation from the

    discrete process to a continuous process discrete process to a continuous process
    discrete process to a continuous process

    very very interesting in these flow very very interesting in these flow very very
    interesting in these flow

    models. models.

    And uh now what we''ll do is let''s change And uh now what we''ll do is let''s
    change And uh now what we''ll do is let''s change

    this target distribution and we''ll see this target distribution and we''ll see
    this target distribution and we''ll see

    what happens with the spiral data. Yeah. So now the end distribution is a Yeah.
    So now the end distribution is a

    spiral data. We''ll again define the spiral data. We''ll again define the spiral
    data. We''ll again define the

    neural vector field. We''ll train this neural vector field. We''ll train this
    neural vector field. We''ll train this

    velocity field now. velocity field now. velocity field now.

    And uh we will see the loss decreases as And uh we will see the loss decreases
    as And uh we will see the loss decreases as

    the number of epochs increase. The training is complete. Now we will The training
    is complete. Now we will

    simulate the OD simulate the OD simulate the OD

    using the oiler method. And let''s see using the oiler method. And let''s see
    using the oiler method. And let''s see

    the animation. [snorts]

    Let''s see. Let''s see. Let''s see.

    So now you see the particles are So now you see the particles are So now you see
    the particles are

    revolving and slowly moving into a shape revolving and slowly moving into a shape
    revolving and slowly moving into a shape

    which represents a spiral. which represents a spiral. which represents a spiral.

    Instead of the heart-shaped uh there are Instead of the heart-shaped uh there
    are Instead of the heart-shaped uh there are

    the particles who are compressing inside the particles who are compressing inside'
  concept_slugs:
  - continuous-normalizing-flow
  - flow-matching
- idx: 49
  start_sec: 3123.599
  end_sec: 3176.069
  text: 'the particles who are compressing inside

    here they are moving out and here they are moving out and here they are moving
    out and

    slowly resembling that spiral shape. So slowly resembling that spiral shape. So
    slowly resembling that spiral shape. So

    this is exactly what we mean by flow this is exactly what we mean by flow this
    is exactly what we mean by flow

    models. models.

    Okay. Let us recap what we did in Okay. Let us recap what we did in Okay. Let
    us recap what we did in

    today''s lecture. today''s lecture. today''s lecture.

    In today''s lecture, we first started In today''s lecture, we first started In
    today''s lecture, we first started

    with the concept of time dependent with the concept of time dependent with the
    concept of time dependent

    velocity fields. Why we started with the velocity fields. Why we started with
    the velocity fields. Why we started with the

    concept of that? Because once we have a concept of that? Because once we have
    a concept of that? Because once we have a

    timed dependent velocity field, we can timed dependent velocity field, we can
    timed dependent velocity field, we can

    calculate the trajectories of all the calculate the trajectories of all the calculate
    the trajectories of all the

    particles in space according to that particles in space according to that particles
    in space according to that

    velocity field. How do we do that? We velocity field. How do we do that? We velocity
    field. How do we do that? We

    use the the oiler method to do that use the the oiler method to do that use the
    the oiler method to do that

    where we discretize the differential where we discretize the differential where
    we discretize the differential

    equation and we see how the particles equation and we see how the particles equation
    and we see how the particles

    move in time. move in time. move in time.

    Now the question is okay this is fine we Now the question is okay this is fine
    we Now the question is okay this is fine we

    have defined the velocity vector field have defined the velocity vector field
    have defined the velocity vector field

    but how how do we solve our problem but how how do we solve our problem but how
    how do we solve our problem

    initial problem of converting the uh'
  concept_slugs:
  - continuous-normalizing-flow
  - flow-matching
- idx: 50
  start_sec: 3176.069
  end_sec: 3230.559
  text: 'initial problem of converting the uh initial problem of converting the uh

    gshian distribution to our actual gshian distribution to our actual gshian distribution
    to our actual

    distribution. What we say is that we use distribution. What we say is that we
    use distribution. What we say is that we use

    the same concept of a velocity field the same concept of a velocity field the
    same concept of a velocity field

    and instead of changing the trajectories and instead of changing the trajectories
    and instead of changing the trajectories

    of the particles here we will change the of the particles here we will change
    the of the particles here we will change the

    trajectories of particles but we will trajectories of particles but we will trajectories
    of particles but we will

    transform the original distribution to a transform the original distribution to
    a transform the original distribution to a

    final distribution final distribution final distribution

    according to the trajectories of the according to the trajectories of the according
    to the trajectories of the

    particles which govern that particles which govern that particles which govern
    that

    distribution. distribution.

    And we have a technical word for this And we have a technical word for this And
    we have a technical word for this

    which governs the trajectories of all which governs the trajectories of all which
    governs the trajectories of all

    these particles which is called as a these particles which is called as a these
    particles which is called as a

    flow. flow.

    And what is a flow model? A flow model And what is a flow model? A flow model
    And what is a flow model? A flow model

    is a model which gives us the velocity is a model which gives us the velocity
    is a model which gives us the velocity

    vector field vector field vector field

    that will be used to calculate the that will be used to calculate the that will
    be used to calculate the

    trajectories of all the particles trajectories of all the particles trajectories
    of all the particles

    and this velocity vector field is often and this velocity vector field is often
    and this velocity vector field is often

    times a neural network. times a neural network. times a neural network.

    So the differential equation is also So the differential equation is also'
  concept_slugs:
  - continuous-normalizing-flow
  - flow-matching
- idx: 51
  start_sec: 3230.559
  end_sec: 3283.03
  text: 'So the differential equation is also

    termed as a neural ordinary differential termed as a neural ordinary differential
    termed as a neural ordinary differential

    equation. So the terms that I have equation. So the terms that I have equation.
    So the terms that I have

    introduced in this lecture are first is introduced in this lecture are first is
    introduced in this lecture are first is

    ordinary differential equation, neural ordinary differential equation, neural
    ordinary differential equation, neural

    ordinary differential equation, vector ordinary differential equation, vector
    ordinary differential equation, vector

    field, velocity vector field, timed field, velocity vector field, timed field,
    velocity vector field, timed

    dependent velocity vector field, flow dependent velocity vector field, flow dependent
    velocity vector field, flow

    and flow models. All of these terms mean and flow models. All of these terms mean
    and flow models. All of these terms mean

    something very specific and I want you something very specific and I want you
    something very specific and I want you

    to understand these terminologies in to understand these terminologies in to understand
    these terminologies in

    detail. detail. detail.

    Also to give you a vision of where we Also to give you a vision of where we Also
    to give you a vision of where we

    are heading something happened in this are heading something happened in this
    are heading something happened in this

    training step which allowed us to and training step which allowed us to and training
    step which allowed us to and

    this is so simple you can see it''s this is so simple you can see it''s this is
    so simple you can see it''s

    hardly 20 lines hardly 20 lines hardly 20 lines

    and that is exactly the simplicity of and that is exactly the simplicity of and
    that is exactly the simplicity of

    the flow modeling approach which we will the flow modeling approach which we will
    the flow modeling approach which we will

    get at slowly but we will do it in a get at slowly but we will do it in a get
    at slowly but we will do it in a

    very step-by-step manner. very step-by-step manner. very step-by-step manner.

    Thank you very much everyone and uh this Thank you very much everyone and uh this
    Thank you very much everyone and uh this

    ends our first lecture and in the next'
  concept_slugs:
  - continuous-normalizing-flow
  - flow-matching
- idx: 52
  start_sec: 3283.03
  end_sec: 3292.68
  text: 'ends our first lecture and in the next ends our first lecture and in the
    next

    lecture we will understand what is the lecture we will understand what is the
    lecture we will understand what is the

    target of our flow model. How do we target of our flow model. How do we target
    of our flow model. How do we

    define the target and how do we train define the target and how do we train define
    the target and how do we train

    the flow models as well.'
  concept_slugs:
  - continuous-normalizing-flow
  - flow-matching
---
# Lecture 9 - Introduction to Flow Models | Principles of Diffusion Models

See the structured chunks above.
