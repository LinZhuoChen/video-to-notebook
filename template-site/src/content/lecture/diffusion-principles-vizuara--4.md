---
course_slug: diffusion-principles-vizuara
idx: 4
title: Lecture 7 - Noise Conditional Score Networks | Principles of Diffusion Models
video_url: https://www.youtube.com/watch?v=ej7LfQyKXec
duration_sec: null
chunks:
- idx: 0
  start_sec: 4.71
  end_sec: 67.2
  text: 'Hello everyone, welcome to the next Hello everyone, welcome to the next

    lecture of the course principles of lecture of the course principles of lecture
    of the course principles of

    diffusion models. diffusion models. diffusion models.

    In the last lecture, we looked at In the last lecture, we looked at In the last
    lecture, we looked at

    dnoising score matching dnoising score matching dnoising score matching

    and let''s again try to understand it and let''s again try to understand it and
    let''s again try to understand it

    with the help of an analogy. Imagine with the help of an analogy. Imagine with
    the help of an analogy. Imagine

    that there are a bunch of magnets kept that there are a bunch of magnets kept
    that there are a bunch of magnets kept

    on a table on a table on a table

    and you have access to only a few of and you have access to only a few of and
    you have access to only a few of

    those magnets. Many of the other magnets those magnets. Many of the other magnets
    those magnets. Many of the other magnets

    are hidden from you. are hidden from you. are hidden from you.

    Now the idea or the objective is to Now the idea or the objective is to Now the
    idea or the objective is to

    calculate calculate calculate

    given any point on this table given any point on this table given any point on
    this table

    what is the direction in which the what is the direction in which the what is
    the direction in which the

    nearest magnet is pulling you. nearest magnet is pulling you. nearest magnet is
    pulling you.

    This is what we want to calculate. This is what we want to calculate. This is
    what we want to calculate.

    Now, inherently this is a very hard Now, inherently this is a very hard Now, inherently
    this is a very hard

    problem because problem because problem because

    we do not know the exact location of the we do not know the exact location of
    the we do not know the exact location of the

    magnets. If we knew that we would magnets. If we knew that we would magnets. If
    we knew that we would

    calculate the magnetic field for all the calculate the magnetic field for all
    the'
  concept_slugs:
  - noise-schedule
  - score-function
  - score-matching
- idx: 1
  start_sec: 67.2
  end_sec: 133.67
  text: 'calculate the magnetic field for all the

    magnets and superimpose them together so magnets and superimpose them together
    so magnets and superimpose them together so

    that we have a cumulative universal that we have a cumulative universal that we
    have a cumulative universal

    magnetic field on the table. magnetic field on the table. magnetic field on the
    table.

    But the problem is that we do not know But the problem is that we do not know
    But the problem is that we do not know

    the number of magnets which are there the number of magnets which are there the
    number of magnets which are there

    since many of them are hidden. To solve this problem, we do a simple To solve
    this problem, we do a simple

    trick. trick. trick.

    What we do is we place a metal ball on What we do is we place a metal ball on
    What we do is we place a metal ball on

    top of one magnet. top of one magnet. top of one magnet.

    We flick the metal ball and it goes and We flick the metal ball and it goes and
    We flick the metal ball and it goes and

    lands at a specific position. lands at a specific position. lands at a specific
    position.

    Okay. Now Okay. Now Okay. Now

    we ask one student to come in. The we ask one student to come in. The we ask one
    student to come in. The

    student only sees the new location of student only sees the new location of student
    only sees the new location of

    the ball which has been flicked. And we the ball which has been flicked. And we
    the ball which has been flicked. And we

    ask the student try to guess ask the student try to guess ask the student try
    to guess

    where did this ball come from. Guess the where did this ball come from. Guess
    the where did this ball come from. Guess the

    vector which pulls the magnet or the vector which pulls the magnet or the vector
    which pulls the magnet or the

    ball back to its original position. ball back to its original position. ball back
    to its original position.

    Naturally the student has absolutely no Naturally the student has absolutely no
    Naturally the student has absolutely no

    idea where this ball came from.'
  concept_slugs:
  - noise-schedule
  - score-function
  - score-matching
- idx: 2
  start_sec: 133.67
  end_sec: 211.2
  text: 'idea where this ball came from. idea where this ball came from.

    But we have an idea where it came from. But we have an idea where it came from.
    But we have an idea where it came from.

    And essentially what we are trying to do And essentially what we are trying to
    do And essentially what we are trying to do

    is is is

    this is the vector which is the noise vector. This is what we is the noise vector.
    This is what we

    have added have added have added

    and this is the vector which the student and this is the vector which the student
    and this is the vector which the student

    is predicting. is predicting. is predicting.

    And we want to make these two vectors as And we want to make these two vectors
    as And we want to make these two vectors as

    close as possible. close as possible. close as possible.

    This is exactly what dnoising score This is exactly what dnoising score This is
    exactly what dnoising score

    matching does. matching does. matching does.

    Because it is not possible to calculate Because it is not possible to calculate
    Because it is not possible to calculate

    the score of the true data distribution, the score of the true data distribution,
    the score of the true data distribution,

    something magical happens in the noisy something magical happens in the noisy
    something magical happens in the noisy

    world that suddenly things become more world that suddenly things become more
    world that suddenly things become more

    tractable. tractable. tractable.

    And in this example, these magnets And in this example, these magnets And in this
    example, these magnets

    represent the data points which are represent the data points which are represent
    the data points which are

    available to us. Magnetic field available to us. Magnetic field available to us.
    Magnetic field

    represents the score vector which we are represents the score vector which we
    are represents the score vector which we are

    trying to predict at every single point trying to predict at every single point
    trying to predict at every single point

    on the table. on the table. on the table.

    The new position of the flicked ball, it The new position of the flicked ball,
    it The new position of the flicked ball, it

    represents the noisy data point. Okay. And'
  concept_slugs:
  - noise-schedule
  - score-function
  - score-matching
- idx: 3
  start_sec: 211.2
  end_sec: 274.0
  text: 'Okay. And

    the force required to pull the ball back the force required to pull the ball back
    the force required to pull the ball back

    to the start is the score field for the to the start is the score field for the
    to the start is the score field for the

    noisy data which we are trying to noisy data which we are trying to noisy data
    which we are trying to

    predict. predict. predict.

    Because of which the objective function Because of which the objective function
    Because of which the objective function

    looks like this. This is the vector looks like this. This is the vector looks
    like this. This is the vector

    which is predicted by the student which is predicted by the student which is predicted
    by the student

    and this is the and this is the and this is the

    true vector. true vector. true vector.

    >> [snorts] >> [snorts] >> [snorts]

    >> Now intuitively we know this is >> Now intuitively we know this is >> Now intuitively
    we know this is

    proportional to xhat minus x right. proportional to xhat minus x right. proportional
    to xhat minus x right.

    It turns out that if you consider a It turns out that if you consider a It turns
    out that if you consider a

    gshian distribution this is exactly gshian distribution this is exactly gshian
    distribution this is exactly

    equal to the difference equal to the difference equal to the difference

    divided by the standard deviation. So divided by the standard deviation. So divided
    by the standard deviation. So

    this is what we calculated. this is what we calculated. this is what we calculated.

    [snorts] It turns out that it turns out [snorts] It turns out that it turns out
    [snorts] It turns out that it turns out

    to be the to be the to be the

    vector from the noisy data to the true vector from the noisy data to the true
    vector from the noisy data to the true

    data divided by the square of the data divided by the square of the data divided
    by the square of the

    standard deviations which is the standard deviations which is the standard deviations
    which is the

    variance itself. variance itself. variance itself.

    Now this can also be represented as a Now this can also be represented as a'
  concept_slugs:
  - noise-schedule
  - score-function
  - score-matching
- idx: 4
  start_sec: 274.0
  end_sec: 335.11
  text: 'Now this can also be represented as a

    noise vector. Right? noise vector. Right? noise vector. Right?

    [snorts] This is our flick. So [snorts] This is our flick. So [snorts] This is
    our flick. So

    essentially we are trying to predict the essentially we are trying to predict
    the essentially we are trying to predict the

    flick flick flick

    and we are trying to predict how much and we are trying to predict how much and
    we are trying to predict how much

    noise we have added to the system and in noise we have added to the system and
    in noise we have added to the system and in

    that process we are predicting the score that process we are predicting the score
    that process we are predicting the score

    field itself. field itself. field itself.

    [snorts] Now you might be wondering that [snorts] Now you might be wondering that
    [snorts] Now you might be wondering that

    Rajat we are predicting the score field Rajat we are predicting the score field
    Rajat we are predicting the score field

    but aren''t we predicting the score for but aren''t we predicting the score for
    but aren''t we predicting the score for

    the noisy data? Aren''t we predicting it? the noisy data? Aren''t we predicting
    it? the noisy data? Aren''t we predicting it?

    we are not predicting it for our we are not predicting it for our we are not predicting
    it for our

    original data. original data. original data.

    Well, the idea is that if Well, the idea is that if Well, the idea is that if

    the noise imparted to this is very the noise imparted to this is very the noise
    imparted to this is very

    small. Now you can actually express this small. Now you can actually express this
    small. Now you can actually express this

    in terms of noise x - xhat is equal to in terms of noise x - xhat is equal to
    in terms of noise x - xhat is equal to

    from this formula from this formula from this formula

    x - xhat is equal to minus sigma * x - xhat is equal to minus sigma * x - xhat
    is equal to minus sigma *

    epsilon. epsilon. epsilon.

    So this whole thing becomes minus So this whole thing becomes minus So this whole
    thing becomes minus

    [snorts] epsilon by sigma.'
  concept_slugs:
  - noise-schedule
  - score-function
  - score-matching
- idx: 5
  start_sec: 337.51
  end_sec: 393.039
  text: 'And if this perturbed noise is very And if this perturbed noise is very

    small, you could assume that whatever small, you could assume that whatever small,
    you could assume that whatever

    score my I am going to learn for one my score my I am going to learn for one my
    score my I am going to learn for one my

    noisy data is going to be very similar noisy data is going to be very similar
    noisy data is going to be very similar

    to the score which I''m going to learn to the score which I''m going to learn
    to the score which I''m going to learn

    for the true data. for the true data. for the true data.

    So there will be some amount of noise in So there will be some amount of noise
    in So there will be some amount of noise in

    the prediction. that it is it is the prediction. that it is it is the prediction.
    that it is it is

    something which can be neglected. It something which can be neglected. It something
    which can be neglected. It

    will be negligible. Later we took a very interesting Later we took a very interesting

    practical example where we saw that this practical example where we saw that this
    practical example where we saw that this

    exact same formula is used. This is the exact same formula is used. This is the
    exact same formula is used. This is the

    Google collab notebook for that example Google collab notebook for that example
    Google collab notebook for that example

    where we considered a data having two where we considered a data having two where
    we considered a data having two

    peaks peaks peaks

    and the objective was to do score and the objective was to do score and the objective
    was to do score

    matching. matching. matching.

    >> [snorts] >> [snorts]

    >> Now you see the simplicity of this loss >> Now you see the simplicity of this
    loss >> Now you see the simplicity of this loss

    function. The target score is simply function. The target score is simply function.
    The target score is simply

    minus noise divided by sigma which is minus noise divided by sigma which is minus
    noise divided by sigma which is

    exactly what we saw here. Minus noise exactly what we saw here. Minus noise'
  concept_slugs:
  - noise-schedule
  - score-function
  - score-matching
- idx: 6
  start_sec: 393.039
  end_sec: 461.36
  text: 'exactly what we saw here. Minus noise

    divided by sigma. divided by sigma. divided by sigma.

    And the predicted score is what our And the predicted score is what our And the
    predicted score is what our

    model predicts. So [snorts] this formulation is So [snorts] this formulation is

    incredibly simple compared to the incredibly simple compared to the incredibly
    simple compared to the

    formulation that we looked at before formulation that we looked at before formulation
    that we looked at before

    which includes the trace and the which includes the trace and the which includes
    the trace and the

    magnitude of the individual element magnitude of the individual element magnitude
    of the individual element

    squared. squared. squared.

    In fact, that is also a possible In fact, that is also a possible In fact, that
    is also a possible

    formulation for score matching. But it formulation for score matching. But it
    formulation for score matching. But it

    turns out that the computational turns out that the computational turns out that
    the computational

    complexity increases as the square of complexity increases as the square of complexity
    increases as the square of

    the dimensions. Hence, we do not opt for the dimensions. Hence, we do not opt
    for the dimensions. Hence, we do not opt for

    that method. And this is something which that method. And this is something which
    that method. And this is something which

    is much more simpler. The simplicity is is much more simpler. The simplicity is
    is much more simpler. The simplicity is

    quite apparent in this code cell. Now we look back and we ask the Now we look
    back and we ask the

    question, okay fine, can we do something question, okay fine, can we do something
    question, okay fine, can we do something

    better than this? better than this? better than this?

    And that is exactly the point of today''s And that is exactly the point of today''s
    And that is exactly the point of today''s

    lecture. We are going to discuss a lecture. We are going to discuss a lecture.
    We are going to discuss a

    technique which is called as noise technique which is called as noise technique
    which is called as noise

    conditioned score networks or NCSN. Now Now

    as I said before uh the field of score as I said before uh the field of score'
  concept_slugs:
  - noise-schedule
  - score-function
  - score-matching
- idx: 7
  start_sec: 461.36
  end_sec: 529.36
  text: 'as I said before uh the field of score

    matching has evolved matching has evolved matching has evolved

    through years. So in 2005 was the proof through years. So in 2005 was the proof
    through years. So in 2005 was the proof

    given by URN where they showed that the given by URN where they showed that the
    given by URN where they showed that the

    score matching objective can be score matching objective can be score matching
    objective can be

    tractable and this is where it included tractable and this is where it included
    tractable and this is where it included

    two terms with the trace term and the two terms with the trace term and the two
    terms with the trace term and the

    magnitude of the element square term. magnitude of the element square term. magnitude
    of the element square term.

    Then 2010 we had that paper by Pascal Then 2010 we had that paper by Pascal Then
    2010 we had that paper by Pascal

    which introduced dinoising score which introduced dinoising score which introduced
    dinoising score

    matching which is exactly what we matching which is exactly what we matching which
    is exactly what we

    discussed in the last lecture. And the most important paper which And the most
    important paper which

    summarized everything that had been done summarized everything that had been done
    summarized everything that had been done

    before came out in 2019. This paper was written by Song and This paper was written
    by Song and

    Armon. And this is what the paper looks like. And this is what the paper looks
    like.

    It''s an excellent read. If you can just It''s an excellent read. If you can just
    It''s an excellent read. If you can just

    take a print out of this and try to read take a print out of this and try to read
    take a print out of this and try to read

    it. It summarizes the paper of Vincent it. It summarizes the paper of Vincent
    it. It summarizes the paper of Vincent

    as well. as well. as well.

    The drawbacks of this paper and what The drawbacks of this paper and what The
    drawbacks of this paper and what

    they are doing which is new compared to they are doing which is new compared to
    they are doing which is new compared to

    that. that.'
  concept_slugs:
  - noise-schedule
  - score-function
  - score-matching
- idx: 8
  start_sec: 529.36
  end_sec: 583.2
  text: 'that.

    It''s a very beautifully written paper It''s a very beautifully written paper
    It''s a very beautifully written paper

    and in fact the textbook which I''m and in fact the textbook which I''m and in
    fact the textbook which I''m

    referring to make this course is also referring to make this course is also referring
    to make this course is also

    written by Stfano Armon. So written by Stfano Armon. So written by Stfano Armon.
    So

    uh he is one of the pioneers in in this uh he is one of the pioneers in in this
    uh he is one of the pioneers in in this

    field and the paper is very nicely field and the paper is very nicely field and
    the paper is very nicely

    written. written. written.

    So it has been 14 years of progress So it has been 14 years of progress So it
    has been 14 years of progress

    which has [snorts] led us to this moment which has [snorts] led us to this moment
    which has [snorts] led us to this moment

    where we have these noise condition where we have these noise condition where
    we have these noise condition

    score vectors. score vectors. score vectors.

    So let''s let''s try to build an intuition So let''s let''s try to build an intuition
    So let''s let''s try to build an intuition

    as to what is explained in this paper. as to what is explained in this paper.
    as to what is explained in this paper.

    Remember I have been mentioning from the Remember I have been mentioning from
    the Remember I have been mentioning from the

    last lecture that adding noise does last lecture that adding noise does last lecture
    that adding noise does

    something magical. something magical. something magical.

    It''s it it looks like it''s too easy and It''s it it looks like it''s too easy
    and It''s it it looks like it''s too easy and

    it''s always being done. Even in it''s always being done. Even in it''s always
    being done. Even in

    diffusion we saw the same thing diffusion we saw the same thing diffusion we saw
    the same thing

    uh that we first converted every single uh that we first converted every single
    uh that we first converted every single

    image or data sample into noise and then image or data sample into noise and then'
  concept_slugs:
  - noise-schedule
  - score-function
  - score-matching
- idx: 9
  start_sec: 583.2
  end_sec: 656.949
  text: 'image or data sample into noise and then

    we predicted the reverse distribution we predicted the reverse distribution we
    predicted the reverse distribution

    from the noise back to the data. from the noise back to the data. from the noise
    back to the data.

    So what is so special about adding noise So what is so special about adding noise
    So what is so special about adding noise

    and why does it help us so much? In in and why does it help us so much? In in
    and why does it help us so much? In in

    this paper they this paper they this paper they

    explain that explain that explain that

    it is like we are artificially creating it is like we are artificially creating
    it is like we are artificially creating

    chaos which is going to help us do chaos which is going to help us do chaos which
    is going to help us do

    better. better. better.

    So in in this paper they talk about So in in this paper they talk about So in
    in this paper they talk about

    something which is called as manifold something which is called as manifold something
    which is called as manifold

    hypothesis. The manifold hypothesis states that The manifold hypothesis states
    that

    data in the real world tends to data in the real world tends to data in the real
    world tends to

    concentrate on concentrate on concentrate on

    lowdimensional manifolds embedded in lowdimensional manifolds embedded in lowdimensional
    manifolds embedded in

    higher dimensional space. higher dimensional space. higher dimensional space.

    What does this mean? I have a nice What does this mean? I have a nice What does
    this mean? I have a nice

    diagram here for you. You can see here diagram here for you. You can see here
    diagram here for you. You can see here

    that there is there are a lot of wires that there is there are a lot of wires
    that there is there are a lot of wires

    going around here and there. But focus going around here and there. But focus
    going around here and there. But focus

    your attention on this part. your attention on this part. your attention on this
    part.

    This is where the data lies. This is where the data lies. This is where the data
    lies.

    This is also called as a manifold.'
  concept_slugs:
  - noise-schedule
  - score-function
  - score-matching
- idx: 10
  start_sec: 659.91
  end_sec: 728.88
  text: 'Now look at what is happening here. Your Now look at what is happening here.
    Your

    space is huge. This is the your entire space is huge. This is the your entire
    space is huge. This is the your entire

    space. space. space.

    But your data lies on a structure which But your data lies on a structure which
    But your data lies on a structure which

    is very low dimensional. Right? is very low dimensional. Right? is very low dimensional.
    Right?

    So your data is occupying a very tiny So your data is occupying a very tiny So
    your data is occupying a very tiny

    part of the entire higher dimensional part of the entire higher dimensional part
    of the entire higher dimensional

    space space space

    and that is exactly the problem which we and that is exactly the problem which
    we and that is exactly the problem which we

    are trying to solve. are trying to solve. are trying to solve.

    So here this is called higher So here this is called higher So here this is called
    higher

    dimensional space and the structure on dimensional space and the structure on
    dimensional space and the structure on

    which the data lies is called as the which the data lies is called as the which
    the data lies is called as the

    manifold. [snorts] [snorts]

    Okay. So now once we understand the Okay. So now once we understand the Okay.
    So now once we understand the

    manifold hypothesis manifold hypothesis manifold hypothesis

    uh the scorebased generative model uh the scorebased generative model uh the scorebased
    generative model

    we''ll face two key difficulties. What is we''ll face two key difficulties. What
    is we''ll face two key difficulties. What is

    a score based generative model? a score based generative model? a score based
    generative model?

    It is where we are not doing any kind of It is where we are not doing any kind
    of It is where we are not doing any kind of

    noise addition but we are simply noise addition but we are simply noise addition
    but we are simply

    matching the matching the matching the

    predicted score with the true score. This was the paper which came out into This
    was the paper which came out into

    2005 which we explained and this is the 2005 which we explained and this is the'
  concept_slugs:
  - noise-schedule
  - score-function
  - score-matching
- idx: 11
  start_sec: 728.88
  end_sec: 809.76
  text: '2005 which we explained and this is the

    loss that we try to minimize. Okay. Now

    this score is given by gradient of this score is given by gradient of this score
    is given by gradient of

    log of p of x. This gradient is taken in the ambient This gradient is taken in
    the ambient

    space which is in the higher dimensional space which is in the higher dimensional
    space which is in the higher dimensional

    space. Now the problem is that there is space. Now the problem is that there is
    space. Now the problem is that there is

    no data point which is lying in the no data point which is lying in the no data
    point which is lying in the

    higher dimensional space. higher dimensional space.

    So this gradient with respect to your So this gradient with respect to your So
    this gradient with respect to your

    data it becomes undefined because there is nothing lying in this because there
    is nothing lying in this

    space. It''s completely empty. space. It''s completely empty. space. It''s completely
    empty.

    So since the score is taken as a So since the score is taken as a So since the
    score is taken as a

    gradient in the ambient space, it is gradient in the ambient space, it is gradient
    in the ambient space, it is

    undefined when x is confined to a low undefined when x is confined to a low undefined
    when x is confined to a low

    dimensional manifold. dimensional manifold. dimensional manifold.

    So we will try to imagine this. Imagine So we will try to imagine this. Imagine
    So we will try to imagine this. Imagine

    that that that

    your data is confined to your data is confined to your data is confined to

    this this this

    sheet of paper. sheet of paper. sheet of paper.

    Imagine Imagine Imagine

    you''re holding a sheet of paper in your you''re holding a sheet of paper in your
    you''re holding a sheet of paper in your

    hand and that that is where your data hand and that that is where your data hand
    and that that is where your data

    lies. lies. lies.

    So on the sheet of paper it is So on the sheet of paper it is So on the sheet
    of paper it is

    completely fine. Everything is defined. completely fine. Everything is defined.'
  concept_slugs:
  - noise-schedule
  - score-function
  - score-matching
- idx: 12
  start_sec: 809.76
  end_sec: 867.35
  text: 'completely fine. Everything is defined.

    This the slope is defined right? You This the slope is defined right? You This
    the slope is defined right? You

    know exactly how your data changes as know exactly how your data changes as know
    exactly how your data changes as

    you move from one point to another. you move from one point to another. you move
    from one point to another.

    Now move away from your sheet of paper Now move away from your sheet of paper
    Now move away from your sheet of paper

    and look at the room around you. and look at the room around you. and look at
    the room around you.

    Let''s say we take a point here at the edge of the paper. at the edge of the paper.

    Now the gradient at the edge of the Now the gradient at the edge of the Now the
    gradient at the edge of the

    paper is not defined because there is no paper is not defined because there is
    no paper is not defined because there is no

    data over here. And this is something which is a big And this is something which
    is a big

    issue, right? Your data is occupying issue, right? Your data is occupying issue,
    right? Your data is occupying

    such a small space such a small space such a small space

    and the gradients are not defined. So if and the gradients are not defined. So
    if and the gradients are not defined. So if

    you calculate the score vector for your you calculate the score vector for your
    you calculate the score vector for your

    entire geometry, entire geometry, entire geometry,

    it is likely that the there there will it is likely that the there there will
    it is likely that the there there will

    be many spots which will be empty in be many spots which will be empty in be many
    spots which will be empty in

    your score field. The score field will your score field. The score field will
    your score field. The score field will

    not appear continuous. There will be not appear continuous. There will be not
    appear continuous. There will be

    many places which will be hollow. The many places which will be hollow. The many
    places which will be hollow. The

    score vector will not be defined.'
  concept_slugs:
  - noise-schedule
  - score-function
  - score-matching
- idx: 13
  start_sec: 867.35
  end_sec: 928.079
  text: 'score vector will not be defined. score vector will not be defined.

    And imagine that you''re going with a And imagine that you''re going with a And
    imagine that you''re going with a

    compass in your hand trying to locate compass in your hand trying to locate compass
    in your hand trying to locate

    where the data is. and you appear at a where the data is. and you appear at a
    where the data is. and you appear at a

    place where since the score is place where since the score is place where since
    the score is

    undefined, the needle in your compost undefined, the needle in your compost undefined,
    the needle in your compost

    just shifts here and there. It it it just shifts here and there. It it it just
    shifts here and there. It it it

    does not know what to do. This is the problem that we face with This is the problem
    that we face with

    uh uh uh

    generative score based generative generative score based generative generative
    score based generative

    models. models. models.

    Now, how does adding noise help? This is Now, how does adding noise help? This
    is Now, how does adding noise help? This is

    exactly why Vincent''s denoising score exactly why Vincent''s denoising score
    exactly why Vincent''s denoising score

    matching that is adding noise is so matching that is adding noise is so matching
    that is adding noise is so

    important. important. important.

    By adding noise, you actually fluff up By adding noise, you actually fluff up
    By adding noise, you actually fluff up

    that tiny sheet of paper into a cloud that tiny sheet of paper into a cloud that
    tiny sheet of paper into a cloud

    that fills up the room. [snorts] So that fills up the room. [snorts] So that fills
    up the room. [snorts] So

    imagine that uh you know this was before imagine that uh you know this was before
    imagine that uh you know this was before

    and this is after. and this is after. and this is after.

    When you flick the data, what you''re When you flick the data, what you''re When
    you flick the data, what you''re

    doing is that the data is being doing is that the data is being doing is that
    the data is being

    transformed from a low dimensional transformed from a low dimensional'
  concept_slugs:
  - noise-schedule
  - score-function
  - score-matching
- idx: 14
  start_sec: 928.079
  end_sec: 1020.23
  text: 'transformed from a low dimensional

    manifold to a higher dimensional space. manifold to a higher dimensional space.
    manifold to a higher dimensional space.

    It''s taking up the space It''s taking up the space It''s taking up the space

    even beyond the confines of the initial even beyond the confines of the initial
    even beyond the confines of the initial

    manifold and it''s spreading all over. manifold and it''s spreading all over.
    manifold and it''s spreading all over.

    This is what makes This is what makes This is what makes

    allows the math to work again. It allows allows the math to work again. It allows
    allows the math to work again. It allows

    the gradient calculations to be the gradient calculations to be the gradient calculations
    to be

    possible. And this is the intuition that I want And this is the intuition that
    I want

    all of you to [snorts] really understand all of you to [snorts] really understand
    all of you to [snorts] really understand

    at a very deep level. It is astonishing to see how many It is astonishing to see
    how many

    problems scientists have solved by problems scientists have solved by problems
    scientists have solved by

    adding noise. adding noise. adding noise.

    It somehow makes things more easy. Okay. So, Song and Armon in in this Okay. So,
    Song and Armon in in this

    paper, this was already done in the paper, this was already done in the paper,
    this was already done in the

    paper by Vincent in 2010. paper by Vincent in 2010. paper by Vincent in 2010.

    So, what what was the main contribution So, what what was the main contribution
    So, what what was the main contribution

    of this paper? of this paper? of this paper?

    Well, what they did was instead of Well, what they did was instead of Well, what
    they did was instead of

    perturbing the data by just one noise, perturbing the data by just one noise,
    perturbing the data by just one noise,

    they started to perturb the data by they started to perturb the data by they started
    to perturb the data by

    various levels of noise and they simultaneously estimated the and they simultaneously
    estimated the

    scores corresponding to all these noise scores corresponding to all these noise
    scores corresponding to all these noise

    levels. levels. levels.

    Remember in the previous formulation by'
  concept_slugs:
  - noise-schedule
  - score-function
  - score-matching
- idx: 15
  start_sec: 1020.23
  end_sec: 1104.48
  text: 'Remember in the previous formulation by Remember in the previous formulation
    by

    Vincent, we just had one noise. Vincent, we just had one noise. Vincent, we just
    had one noise.

    We we added one noise with a flick. We we added one noise with a flick. We we
    added one noise with a flick.

    Right? Right? Right?

    This is how we built our intuition by This is how we built our intuition by This
    is how we built our intuition by

    adding this flick over here. adding this flick over here. adding this flick over
    here.

    Now it it turns out that just adding one Now it it turns out that just adding
    one Now it it turns out that just adding one

    level of noise is not enough because you level of noise is not enough because
    you level of noise is not enough because you

    won''t be able to capture the entire data won''t be able to capture the entire
    data won''t be able to capture the entire data

    and if you add multiple levels of noise and if you add multiple levels of noise
    and if you add multiple levels of noise

    it allows you to fill up the entire it allows you to fill up the entire it allows
    you to fill up the entire

    space nicely. space nicely. space nicely.

    So let''s understand how the architecture So let''s understand how the architecture
    So let''s understand how the architecture

    proposed proposed proposed

    by Song and Armon exactly look like. Okay. So Okay. So

    [snorts] [snorts]

    this is your original data and and

    this is the first perturbation. this is the first perturbation. this is the first
    perturbation.

    You add some noise sigma 1 You add some noise sigma 1 You add some noise sigma
    1

    again you perturb. So you add another again you perturb. So you add another again
    you perturb. So you add another

    noise level sigma 2 again you perturb. noise level sigma 2 again you perturb.
    noise level sigma 2 again you perturb.

    So this is up to sigma lus 2 So this is up to sigma lus 2 So this is up to sigma
    lus 2

    sigma l -1 and sigma l. So in in the magnet analogy, So in in the magnet analogy,

    you are flicking the magnet you are flicking the magnet'
  concept_slugs:
  - noise-schedule
  - score-function
  - score-matching
- idx: 16
  start_sec: 1104.48
  end_sec: 1182.07
  text: 'you are flicking the magnet

    not just once with one level, but you''re not just once with one level, but you''re
    not just once with one level, but you''re

    flicking it with multiple levels. flicking it with multiple levels. flicking it
    with multiple levels.

    Sometimes you you have a very hard flick Sometimes you you have a very hard flick
    Sometimes you you have a very hard flick

    which probably moves it farther away which probably moves it farther away which
    probably moves it farther away

    from from from

    where your original data lies and where your original data lies and where your
    original data lies and

    sometimes you have a softer flick which sometimes you have a softer flick which
    sometimes you have a softer flick which

    moves it closer to where your original moves it closer to where your original
    moves it closer to where your original

    data lies. So there are L different noise levels So there are L different noise
    levels

    and the important fact is that the noise and the important fact is that the noise
    and the important fact is that the noise

    levels decrease as you move from left to levels decrease as you move from left
    to levels decrease as you move from left to

    right. right. right.

    So this is the highest So in a way uh we could say that the So in a way uh we
    could say that the

    pioneer of this architecture was pioneer of this architecture was pioneer of this
    architecture was

    proposed proposed

    by Pascal Vincent itself but they were by Pascal Vincent itself but they were
    by Pascal Vincent itself but they were

    the ones who thought of conditioning the the ones who thought of conditioning
    the the ones who thought of conditioning the

    noise on or adding multiple levels of noise on or adding multiple levels of noise
    on or adding multiple levels of

    noise noise noise

    which is probably not very intuitive which is probably not very intuitive which
    is probably not very intuitive

    right now but we''ll we''ll try to see why right now but we''ll we''ll try to
    see why right now but we''ll we''ll try to see why

    does that make sense. Why do you add does that make sense. Why do you add does
    that make sense. Why do you add

    multiple levels of noise?'
  concept_slugs:
  - noise-schedule
  - score-function
  - score-matching
- idx: 17
  start_sec: 1182.07
  end_sec: 1248.88
  text: 'multiple levels of noise? multiple levels of noise?

    We don''t do this in diffusion also. In We don''t do this in diffusion also. In
    We don''t do this in diffusion also. In

    diffusion there is one constant level of diffusion there is one constant level
    of diffusion there is one constant level of

    noise which is added in the forward noise which is added in the forward noise
    which is added in the forward

    diffusion process. Okay. So for each of these distribution Okay. So for each of
    these distribution

    we try to estimate the strength of the we try to estimate the strength of the
    we try to estimate the strength of the

    flick how much you''re flicking the flick how much you''re flicking the flick
    how much you''re flicking the

    magnet by. magnet by. magnet by.

    So this is the loss function for each So essentially what we are doing is we So
    essentially what we are doing is we

    are adding noise and then and and then are adding noise and then and and then
    are adding noise and then and and then

    we are trying to predict a score we are trying to predict a score we are trying
    to predict a score

    function function function

    which can predict how much what is the which can predict how much what is the
    which can predict how much what is the

    degree of that noise being added. degree of that noise being added. degree of
    that noise being added.

    This is exactly what we saw in the den This is exactly what we saw in the den
    This is exactly what we saw in the den

    noising score matching. noising score matching. noising score matching.

    Now you might be thinking that uh Raj Now you might be thinking that uh Raj Now
    you might be thinking that uh Raj

    this is fine but aren''t there L this is fine but aren''t there L this is fine
    but aren''t there L

    different loss functions here? So how do different loss functions here? So how
    do different loss functions here? So how do

    we combine all those loss functions and we combine all those loss functions and
    we combine all those loss functions and

    is it a single neural network which is is it a single neural network which is'
  concept_slugs:
  - noise-schedule
  - score-function
  - score-matching
- idx: 18
  start_sec: 1248.88
  end_sec: 1333.669
  text: 'is it a single neural network which is

    trained on trained on trained on

    uh for all these losses and if it''s a uh for all these losses and if it''s a
    uh for all these losses and if it''s a

    single neural network then single neural network then single neural network then

    the input to the neural network is not the input to the neural network is not
    the input to the neural network is not

    just the data but also the noise right just the data but also the noise right
    just the data but also the noise right

    because because because

    the final output depends on not just the the final output depends on not just
    the the final output depends on not just the

    data but the noise level that we are data but the noise level that we are data
    but the noise level that we are

    adding adding adding

    and that is exactly what happens. What we do is we What we do is we

    [snorts] let''s say this first loss is [snorts] let''s say this first loss is
    [snorts] let''s say this first loss is

    L1, second loss is L2 etc. We assign a L1, second loss is L2 etc. We assign a
    L1, second loss is L2 etc. We assign a

    strength of lambda 1, lambda 2, strength of lambda 1, lambda 2, strength of lambda
    1, lambda 2,

    lambda lus 2, lambda lus1 lambda lus 2, lambda lus1 lambda lus 2, lambda lus1

    and lambda l to all of these losses and lambda l to all of these losses and lambda
    l to all of these losses

    and then we simply take a weighted and then we simply take a weighted and then
    we simply take a weighted

    average of these losses so that we get a average of these losses so that we get
    a average of these losses so that we get a

    final combined loss at the end. This is the loss function that we want This is
    the loss function that we want

    to minimize. to minimize. to minimize.

    Okay. So now uh let''s say we have optimized this loss let''s say we have optimized
    this loss

    function and we have found the score. function and we have found the score. function
    and we have found the score.

    Remember now the score does not just'
  concept_slugs:
  - noise-schedule
  - score-function
  - score-matching
- idx: 19
  start_sec: 1333.669
  end_sec: 1407.59
  text: 'Remember now the score does not just Remember now the score does not just

    depend on X depend on X depend on X

    but it depends on X comma sigma where but it depends on X comma sigma where but
    it depends on X comma sigma where

    sigma is the noise level. Okay. Now imagine a scenario where we Okay. Now imagine
    a scenario where we

    have trained the score network have trained the score network have trained the
    score network

    and we know exactly the score for the and we know exactly the score for the and
    we know exactly the score for the

    data and data and data and

    the noisy data. So this is actually x the noisy data. So this is actually x the
    noisy data. So this is actually x

    tilda the noisy data and the amount of tilda the noisy data and the amount of
    tilda the noisy data and the amount of

    noise which has been added. noise which has been added. noise which has been added.

    So how do you sample from the score So how do you sample from the score So how
    do you sample from the score

    function? Then in in this case if you remember we have always done the if you
    remember we have always done the

    sampling from the score using a method sampling from the score using a method
    sampling from the score using a method

    called lang dynamics. called lang dynamics. called lang dynamics.

    What the lang dynamics method does is What the lang dynamics method does is What
    the lang dynamics method does is

    let''s say you have the score defined at let''s say you have the score defined
    at let''s say you have the score defined at

    all these places in this 2D grid. You all these places in this 2D grid. You all
    these places in this 2D grid. You

    start with one point which is let''s say start with one point which is let''s
    say start with one point which is let''s say

    x0. x0. x0.

    Land dynamics gives you a path so that Land dynamics gives you a path so that
    Land dynamics gives you a path so that

    you move according to the score function you move according to the score function
    you move according to the score function

    and land as close as possible to the'
  concept_slugs:
  - noise-schedule
  - score-function
  - score-matching
- idx: 20
  start_sec: 1407.59
  end_sec: 1498.72
  text: 'and land as close as possible to the and land as close as possible to the

    data point. Now the interesting thing is that I have Now the interesting thing
    is that I have

    a score function for a score function for a score function for

    let''s say this we call this as one score let''s say this we call this as one
    score let''s say this we call this as one score

    map. map. map.

    Now I have L different score maps Now I have L different score maps Now I have
    L different score maps

    which is going to move my data in which is going to move my data in which is going
    to move my data in

    different ways. So first is sigma 1 sigma 2 sigma l So first is sigma 1 sigma
    2 sigma l

    minus one minus one minus one

    sigma 3 up to sigma l. sigma 3 up to sigma l. sigma 3 up to sigma l.

    So which which maps do I use and how do So which which maps do I use and how do
    So which which maps do I use and how do

    I use them sequentially and this is exactly where the second key and this is exactly
    where the second key

    innovation in this paper comes. They use innovation in this paper comes. They
    use innovation in this paper comes. They use

    a process called anal lang dynamics. Now this words this word sounds a little
    Now this words this word sounds a little

    bit complex but it''s actually very bit complex but it''s actually very bit complex
    but it''s actually very

    intuitive what they have done in this intuitive what they have done in this intuitive
    what they have done in this

    process. process. process.

    This is very similar to languin This is very similar to languin This is very similar
    to languin

    dynamics. If you are not familiar with dynamics. If you are not familiar with
    dynamics. If you are not familiar with

    this please have a look at our lecture this please have a look at our lecture
    this please have a look at our lecture

    on energy based models which is two on energy based models which is two on energy
    based models which is two

    lectures before this lecture. The only difference is that it is'
  concept_slugs:
  - noise-schedule
  - score-function
  - score-matching
- idx: 21
  start_sec: 1498.72
  end_sec: 1581.84
  text: 'The only difference is that it is

    performed sequentially performed sequentially performed sequentially

    multiple times. Let us understand how we multiple times. Let us understand how
    we multiple times. Let us understand how we

    do that. First we start with do that. First we start with do that. First we start
    with

    just noise. just noise. just noise.

    [snorts] Okay. And let''s say we also [snorts] Okay. And let''s say we also [snorts]
    Okay. And let''s say we also

    copy this map. First we start with noise and we use the First we start with noise
    and we use the

    first score function first score function first score function

    to move. [snorts] Okay. So first we start from [snorts] Okay. So first we start
    from

    noise. This is completely noise as you noise. This is completely noise as you
    noise. This is completely noise as you

    can see. can see. can see.

    And then remember the first variation is And then remember the first variation
    is And then remember the first variation is

    very high or the noise is very high. very high or the noise is very high. very
    high or the noise is very high.

    So you''re probably going to end up at So you''re probably going to end up at
    So you''re probably going to end up at

    data samples which are very far off from data samples which are very far off from
    data samples which are very far off from

    the data because we are finally the data because we are finally the data because
    we are finally

    predicting the noisy data. Right? So you predicting the noisy data. Right? So
    you predicting the noisy data. Right? So you

    are using languin dynamics are using languin dynamics are using languin dynamics

    to get to the next sample but you''re using it only for the first but you''re
    using it only for the first

    noise level which is the highest sigma 1 noise level which is the highest sigma
    1 noise level which is the highest sigma 1

    so [snorts] that you explore the low so [snorts] that you explore the low so [snorts]
    that you explore the low

    density regions of the data well. density regions of the data well. density regions
    of the data well.

    Okay. So you are purposely deliberately Okay. So you are purposely deliberately'
  concept_slugs:
  - noise-schedule
  - score-function
  - score-matching
- idx: 22
  start_sec: 1581.84
  end_sec: 1637.919
  text: 'Okay. So you are purposely deliberately

    inputting a very high noise level so inputting a very high noise level so inputting
    a very high noise level so

    that that

    uh you move to areas where you probably uh you move to areas where you probably
    uh you move to areas where you probably

    don''t find a lot of data but then you don''t find a lot of data but then you
    don''t find a lot of data but then you

    still have access to those points. still have access to those points. still have
    access to those points.

    Now what is langu dynamics? Well the Now what is langu dynamics? Well the Now
    what is langu dynamics? Well the

    formula is very simple. It goes formula is very simple. It goes formula is very
    simple. It goes

    something like xt + 1 something like xt + 1 something like xt + 1

    is equal to xt + n * which is the step is equal to xt + n * which is the step
    is equal to xt + n * which is the step

    size the score function here I''ll just size the score function here I''ll just
    size the score function here I''ll just

    substitute substitute substitute

    plus <unk>2n times a noise level epsilon plus <unk>2n times a noise level epsilon
    plus <unk>2n times a noise level epsilon

    this is what causes the path to look this is what causes the path to look this
    is what causes the path to look

    like a random path it almost looks like like a random path it almost looks like
    like a random path it almost looks like

    a drunken hiker a drunken hiker a drunken hiker

    and uh yeah so this is a terminology and uh yeah so this is a terminology and
    uh yeah so this is a terminology

    which is which is very commonly used which is which is very commonly used which
    is which is very commonly used

    it''s a zigzag path path before you it''s a zigzag path path before you it''s
    a zigzag path path before you

    finally reach to your destination. And finally reach to your destination. And
    finally reach to your destination. And

    here [snorts] the destination is not our here [snorts] the destination is not
    our'
  concept_slugs:
  - noise-schedule
  - score-function
  - score-matching
- idx: 23
  start_sec: 1637.919
  end_sec: 1690.96
  text: 'here [snorts] the destination is not our

    data but it''s far away from our data data but it''s far away from our data data
    but it''s far away from our data

    because we are adding so much noise. So because we are adding so much noise. So
    because we are adding so much noise. So

    it''s it''s going to reach to places where it''s it''s going to reach to places
    where it''s it''s going to reach to places where

    you have the original data plus the you have the original data plus the you have
    the original data plus the

    noise added. So it''s going to reach noise added. So it''s going to reach noise
    added. So it''s going to reach

    these areas. X data plus sigma 1 * these areas. X data plus sigma 1 * these areas.
    X data plus sigma 1 *

    epsilon. This is where we will reach. We epsilon. This is where we will reach.
    We epsilon. This is where we will reach. We

    will reach to areas which are away from will reach to areas which are away from
    will reach to areas which are away from

    our original data. But that is our original data. But that is our original data.
    But that is

    completely fine because we are not yet completely fine because we are not yet
    completely fine because we are not yet

    done here. done here. done here.

    Note that here we are using score Note that here we are using score Note that
    here we are using score

    function which has the highest variance. function which has the highest variance.
    function which has the highest variance.

    This is because we want to cover the low This is because we want to cover the
    low This is because we want to cover the low

    density regions as well. Then you go density regions as well. Then you go density
    regions as well. Then you go

    ahead and you add another noise level. ahead and you add another noise level.
    ahead and you add another noise level.

    This time sigma 2. This time sigma 2. This time sigma 2.

    So again we have our map over here. So again we have our map over here. So again
    we have our map over here.

    Again Again Again

    we are moving according to the lang we are moving according to the lang'
  concept_slugs:
  - noise-schedule
  - score-function
  - score-matching
- idx: 24
  start_sec: 1690.96
  end_sec: 1747.669
  text: 'we are moving according to the lang

    dynamics update rule. This time the dynamics update rule. This time the dynamics
    update rule. This time the

    variance is a bit lower and um variance is a bit lower and um variance is a bit
    lower and um

    we continue this process we continue this process we continue this process

    utilizing all the score functions utilizing all the score functions utilizing
    all the score functions

    estimators. estimators. estimators.

    Note that the variance is going down as Note that the variance is going down as
    Note that the variance is going down as

    we are proceeding because we are we are proceeding because we are we are proceeding
    because we are

    recovering the final details. recovering the final details. recovering the final
    details.

    So that''s why they have this noise So that''s why they have this noise So that''s
    why they have this noise

    condition and score networks in the condition and score networks in the condition
    and score networks in the

    title because title because title because

    uh actually it''s not in the title of the uh actually it''s not in the title of
    the uh actually it''s not in the title of the

    paper but the the main idea is that they paper but the the main idea is that they
    paper but the the main idea is that they

    are doing noise conditioning. Initially are doing noise conditioning. Initially
    are doing noise conditioning. Initially

    they want to explore the low density they want to explore the low density they
    want to explore the low density

    areas and then slowly and steadily move areas and then slowly and steadily move
    areas and then slowly and steadily move

    towards the data. If you just have one towards the data. If you just have one
    towards the data. If you just have one

    noise level, you will probably noise level, you will probably noise level, you
    will probably

    not sample areas where the data only not sample areas where the data only not
    sample areas where the data only

    appears once or twice, which are the low appears once or twice, which are the
    low appears once or twice, which are the low

    density regions. But you do want to density regions. But you do want to density
    regions. But you do want to

    sample the entire data, right? Even if,'
  concept_slugs:
  - noise-schedule
  - score-function
  - score-matching
- idx: 25
  start_sec: 1747.669
  end_sec: 1800.559
  text: 'sample the entire data, right? Even if, sample the entire data, right? Even
    if,

    let''s say, you have handwritten digits let''s say, you have handwritten digits
    let''s say, you have handwritten digits

    and the number 1 2 3 4 5 appears and the number 1 2 3 4 5 appears and the number
    1 2 3 4 5 appears

    thousands of times, but the number nine thousands of times, but the number nine
    thousands of times, but the number nine

    only appears two times in the data. You only appears two times in the data. You
    only appears two times in the data. You

    still want to sample it sometimes, still want to sample it sometimes, still want
    to sample it sometimes,

    right? That is exactly why we are doing right? That is exactly why we are doing
    right? That is exactly why we are doing

    it because you have to cover these low it because you have to cover these low
    it because you have to cover these low

    density density density

    points as well. And after you do this points as well. And after you do this points
    as well. And after you do this

    several times, you can see that slowly several times, you can see that slowly
    several times, you can see that slowly

    the the the

    act the the real data emerges at the end act the the real data emerges at the
    end act the the real data emerges at the end

    [snorts] which is excellent. It it it [snorts] which is excellent. It it it [snorts]
    which is excellent. It it it

    almost looks like the reverse diffusion almost looks like the reverse diffusion
    almost looks like the reverse diffusion

    process, right? Where we get the true process, right? Where we get the true process,
    right? Where we get the true

    data just from noise itself. data just from noise itself. data just from noise
    itself.

    And [snorts] in fact there is a very And [snorts] in fact there is a very And
    [snorts] in fact there is a very

    close parallel between score matching close parallel between score matching close
    parallel between score matching

    and diffusion which we saw in the score and diffusion which we saw in the score
    and diffusion which we saw in the score

    matching formula that it it it finally matching formula that it it it finally'
  concept_slugs:
  - noise-schedule
  - score-function
  - score-matching
- idx: 26
  start_sec: 1800.559
  end_sec: 1861.43
  text: 'matching formula that it it it finally

    tries to predict the noise itself and tries to predict the noise itself and tries
    to predict the noise itself and

    that that is exactly what the diffusion that that is exactly what the diffusion
    that that is exactly what the diffusion

    process also tries to do which is what process also tries to do which is what
    process also tries to do which is what

    we get towards the end of it we get towards the end of it we get towards the end
    of it

    and that''s why this looks very similar and that''s why this looks very similar
    and that''s why this looks very similar

    starting from pure noise starting from pure noise starting from pure noise

    we actually recover our data uh but this we actually recover our data uh but this
    we actually recover our data uh but this

    time we are calculating the score time we are calculating the score time we are
    calculating the score

    vectors. We are not calculating the reverse transition calculating the reverse
    transition

    kernels like we do in the diffusion kernels like we do in the diffusion kernels
    like we do in the diffusion

    process. process.

    So [snorts] this is extremely So [snorts] this is extremely So [snorts] this is
    extremely

    interesting and it''s it''s amazing to see interesting and it''s it''s amazing
    to see interesting and it''s it''s amazing to see

    how two different parts how two different parts how two different parts

    finally finally finally

    you know they they can be linked to each you know they they can be linked to each
    you know they they can be linked to each

    other and this link is given by other and this link is given by other and this
    link is given by

    something known as twid''s formula something known as twid''s formula something
    known as twid''s formula

    although we have intuitively understood although we have intuitively understood
    although we have intuitively understood

    the link there is a mathematical way to the link there is a mathematical way to
    the link there is a mathematical way to

    understand it I will share the link in understand it I will share the link in
    understand it I will share the link in

    the description the description the description

    please go through this for people who'
  concept_slugs:
  - noise-schedule
  - score-function
  - score-matching
- idx: 27
  start_sec: 1861.43
  end_sec: 1934.64
  text: 'please go through this for people who please go through this for people who

    like to see how both are connected and like to see how both are connected and
    like to see how both are connected and

    it''s it''s very simple. There is a there it''s it''s very simple. There is a
    there it''s it''s very simple. There is a there

    is a paper which talks about it and if is a paper which talks about it and if
    is a paper which talks about it and if

    you read the first three pages of that you read the first three pages of that
    you read the first three pages of that

    paper let me actually see if I can find paper let me actually see if I can find
    paper let me actually see if I can find

    it out. Tweed''s formula and selection bias. Tweed''s formula and selection bias.

    This this paper itself is not written by This this paper itself is not written
    by This this paper itself is not written by

    Tweedy but the actual uh formula was Tweedy but the actual uh formula was Tweedy
    but the actual uh formula was

    first reported by Robins Twiddi in 1956 first reported by Robins Twiddi in 1956
    first reported by Robins Twiddi in 1956

    and the formula is written over here. So uh this this might sound a little bit
    So uh this this might sound a little bit

    off track right now but you see here off track right now but you see here off
    track right now but you see here

    this ldash of zed this represents the this ldash of zed this represents the this
    ldash of zed this represents the

    score function exactly we are taking score function exactly we are taking score
    function exactly we are taking

    gradient of the logarithm of the gradient of the logarithm of the gradient of
    the logarithm of the

    probability. probability. probability.

    So this is the score function here and So this is the score function here and
    So this is the score function here and

    [snorts] uh here we are finding the [snorts] uh here we are finding the [snorts]
    uh here we are finding the

    expected value of the mean. expected value of the mean. expected value of the
    mean.

    uh and then uh and then'
  concept_slugs:
  - noise-schedule
  - score-function
  - score-matching
- idx: 28
  start_sec: 1934.64
  end_sec: 1992.47
  text: 'uh and then

    which is exactly what which is exactly what which is exactly what

    we want to predict right we want to we want to predict right we want to we want
    to predict right we want to

    understand that we are adding this noise understand that we are adding this noise
    understand that we are adding this noise

    Z but what was the distribution of the Z but what was the distribution of the
    Z but what was the distribution of the

    means of the actual data that''s what we means of the actual data that''s what
    we means of the actual data that''s what we

    want to predict and you can see that the want to predict and you can see that
    the want to predict and you can see that the

    expected value of this mean turns out to expected value of this mean turns out
    to expected value of this mean turns out to

    be a summation of the noise level which be a summation of the noise level which
    be a summation of the noise level which

    has been added and some constant times has been added and some constant times
    has been added and some constant times

    the score. the score. the score.

    Uh and Uh and Uh and

    this is a amazing way to understand how this is a amazing way to understand how
    this is a amazing way to understand how

    the score finally when we are estimating the score finally when we are estimating
    the score finally when we are estimating

    the score we are essentially estimating the score we are essentially estimating
    the score we are essentially estimating

    how much noise we are reducing from the how much noise we are reducing from the
    how much noise we are reducing from the

    mean of the data. Uh and this is exactly mean of the data. Uh and this is exactly
    mean of the data. Uh and this is exactly

    what diffusion process also does. what diffusion process also does. what diffusion
    process also does.

    Remember what diffusion process does is Remember what diffusion process does is
    Remember what diffusion process does is

    in the DDPM paper all we are doing in in the DDPM paper all we are doing in in
    the DDPM paper all we are doing in

    the reverse transition kernel is we are'
  concept_slugs:
  - noise-schedule
  - score-function
  - score-matching
- idx: 29
  start_sec: 1992.47
  end_sec: 2049.589
  text: 'the reverse transition kernel is we are the reverse transition kernel is
    we are

    trying to predict how much noise was trying to predict how much noise was trying
    to predict how much noise was

    added in the forward process which is added in the forward process which is added
    in the forward process which is

    the just this symbol Z itself that is the just this symbol Z itself that is the
    just this symbol Z itself that is

    exactly what score matching also does exactly what score matching also does exactly
    what score matching also does

    please read the first two two pages of please read the first two two pages of
    please read the first two two pages of

    this paper that''s all you don''t need to this paper that''s all you don''t need
    to this paper that''s all you don''t need to

    uh you won''t need to read the proof but uh you won''t need to read the proof
    but uh you won''t need to read the proof but

    just read this and uh it it''ll be just read this and uh it it''ll be just read
    this and uh it it''ll be

    apparent to you why both are related to apparent to you why both are related to
    apparent to you why both are related to

    each other very nicely Okay. So this is how the process of Okay. So this is how
    the process of

    [snorts] uh any langu dynamics looks [snorts] uh any langu dynamics looks [snorts]
    uh any langu dynamics looks

    like. like. like.

    So the the entire flow looks like this. So the the entire flow looks like this.
    So the the entire flow looks like this.

    Let''s try to understand this. Let''s try to understand this. Let''s try to understand
    this.

    First what we do is we initialize the First what we do is we initialize the First
    what we do is we initialize the

    noisy image which is the gshian noise noisy image which is the gshian noise noisy
    image which is the gshian noise

    completely completely completely

    goshian. Then there are l different goshian. Then there are l different goshian.
    Then there are l different

    noise levels right. So noise levels right. So noise levels right. So

    when we are inferring we do it n uh we'
  concept_slugs:
  - noise-schedule
  - score-function
  - score-matching
- idx: 30
  start_sec: 2049.589
  end_sec: 2096.96
  text: 'when we are inferring we do it n uh we when we are inferring we do it n uh
    we

    do it l times as as we saw here there do it l times as as we saw here there do
    it l times as as we saw here there

    are l different steps involved in the are l different steps involved in the are
    l different steps involved in the

    inference process. So if we are finished inference process. So if we are finished
    inference process. So if we are finished

    we just output the sample but if we are we just output the sample but if we are
    we just output the sample but if we are

    not yet done with the l steps uh we not yet done with the l steps uh we not yet
    done with the l steps uh we

    first calculate this alpha i which is first calculate this alpha i which is first
    calculate this alpha i which is

    here which is the n in this formula the here which is the n in this formula the
    here which is the n in this formula the

    step size. step size. step size.

    So they have a specific way of designing So they have a specific way of designing
    So they have a specific way of designing

    the step size which is related to the step size which is related to the step size
    which is related to

    epsilon and also the noise level divided epsilon and also the noise level divided
    epsilon and also the noise level divided

    by sigma l sigma l² sigma i² divided by by sigma l sigma l² sigma i² divided by
    by sigma l sigma l² sigma i² divided by

    sigma l² [snorts] okay then what you do sigma l² [snorts] okay then what you do
    sigma l² [snorts] okay then what you do

    is if you are not done with the lang is if you are not done with the lang is if
    you are not done with the lang

    dynamics remember you go in a path like dynamics remember you go in a path like
    dynamics remember you go in a path like

    this and you do it for some specific this and you do it for some specific'
  concept_slugs:
  - noise-schedule
  - score-function
  - score-matching
- idx: 31
  start_sec: 2096.96
  end_sec: 2159.51
  text: 'this and you do it for some specific

    time steps t so if the time step is time steps t so if the time step is time steps
    t so if the time step is

    greater than t you just stop this greater than t you just stop this greater than
    t you just stop this

    process. But if it is less than t it process. But if it is less than t it process.
    But if it is less than t it

    means you want to do the walk you want means you want to do the walk you want
    means you want to do the walk you want

    to do the drunken hiker walk. So you to do the drunken hiker walk. So you to do
    the drunken hiker walk. So you

    sample this uh random variable which is sample this uh random variable which is
    sample this uh random variable which is

    the epsilon in this formula and then you simply take a walk using and then you
    simply take a walk using

    lang dynamics. This is the score for that specific This is the score for that
    specific

    noise level. This is the random step noise level. This is the random step noise
    level. This is the random step

    which you take and uh then you proceed which you take and uh then you proceed
    which you take and uh then you proceed

    ahead. You do time t is is equal to t + ahead. You do time t is is equal to t
    + ahead. You do time t is is equal to t +

    1 1 1

    and then you simply repeat this whole and then you simply repeat this whole and
    then you simply repeat this whole

    process until and unless the time step is over until and unless the time step
    is over

    then you sample again. Uh then then you then you sample again. Uh then then you
    then you sample again. Uh then then you

    go to the next noise level. You do this go to the next noise level. You do this
    go to the next noise level. You do this

    times and then you go out of the loop. times and then you go out of the loop.
    times and then you go out of the loop.

    So this is exactly how the anal'
  concept_slugs:
  - noise-schedule
  - score-function
  - score-matching
- idx: 32
  start_sec: 2159.51
  end_sec: 2221.92
  text: 'So this is exactly how the anal So this is exactly how the anal

    land dynamics loop looks like. land dynamics loop looks like. land dynamics loop
    looks like.

    Let''s take a look at a practical example Let''s take a look at a practical example
    Let''s take a look at a practical example

    to understand to understand to understand

    how the noise conditioned score vectors how the noise conditioned score vectors
    how the noise conditioned score vectors

    work in practice. So here uh I have taken CR10 images. I So here uh I have taken
    CR10 images. I

    wanted to work with a real data set, wanted to work with a real data set, wanted
    to work with a real data set,

    interesting data set and uh I I wanted interesting data set and uh I I wanted
    interesting data set and uh I I wanted

    to use this to use this to use this

    technique of noise condition score technique of noise condition score technique
    of noise condition score

    vectors to see how well uh am I able to vectors to see how well uh am I able to
    vectors to see how well uh am I able to

    generate the data. So let''s load the notebook. So let''s load the notebook.

    Yeah. So the the first step is the data Yeah. So the the first step is the data
    Yeah. So the the first step is the data

    loading where you actually load all the loading where you actually load all the
    loading where you actually load all the

    data. And this is how our data looks data. And this is how our data looks data.
    And this is how our data looks

    like. like.

    Uh you can see there are different Uh you can see there are different Uh you can
    see there are different

    shapes here. There is a cat. There is a shapes here. There is a cat. There is
    a shapes here. There is a cat. There is a

    truck. truck. truck.

    There is a There is a There is a

    again a cat. This probably looks like a again a cat. This probably looks like
    a again a cat. This probably looks like a

    horse. And [snorts] then this is where horse. And [snorts] then this is where
    horse. And [snorts] then this is where

    you you'
  concept_slugs:
  - noise-schedule
  - score-function
  - score-matching
- idx: 33
  start_sec: 2221.92
  end_sec: 2288.48
  text: 'you

    uh define your score network which is uh define your score network which is uh
    define your score network which is

    typically a conditional unit. typically a conditional unit. typically a conditional
    unit.

    We saw that in the diffusion practical We saw that in the diffusion practical
    We saw that in the diffusion practical

    example also we use a unit and in fact example also we use a unit and in fact
    example also we use a unit and in fact

    in most of the lectures in principles of in most of the lectures in principles
    of in most of the lectures in principles of

    diffusion models we see that units have diffusion models we see that units have
    diffusion models we see that units have

    become a standard become a standard become a standard

    for predicting noise estimating noise. So that is exactly what uh we are using
    So that is exactly what uh we are using

    here. We are using a unit here here. We are using a unit here here. We are using
    a unit here

    and uh the loss function for each noise and uh the loss function for each noise
    and uh the loss function for each noise

    level simply appears to be like this level simply appears to be like this level
    simply appears to be like this

    which is something we have already which is something we have already which is
    something we have already

    looked at. So the target score is minus noise So the target score is minus noise

    divided by sigma. We we saw the same for divided by sigma. We we saw the same
    for divided by sigma. We we saw the same for

    um the first lecture also which is minus um the first lecture also which is minus
    um the first lecture also which is minus

    noise divided by sigma. noise divided by sigma. noise divided by sigma.

    So I will show you the formula over So I will show you the formula over So I will
    show you the formula over

    here. It looks like this minus noise here. It looks like this minus noise here.
    It looks like this minus noise

    divided by sigma. divided by sigma.

    And that is exactly what we see in the And that is exactly what we see in the'
  concept_slugs:
  - noise-schedule
  - score-function
  - score-matching
- idx: 34
  start_sec: 2288.48
  end_sec: 2355.119
  text: 'And that is exactly what we see in the

    practical U notebook as well. practical U notebook as well. practical U notebook
    as well.

    [snorts] But this is done for different [snorts] But this is done for different
    [snorts] But this is done for different

    noise levels. Okay. Now I have trained this for I Okay. Now I have trained this
    for I

    think think think

    500 or something number of epochs. 500 or something number of epochs. 500 or something
    number of epochs.

    It''s it''s not a lot. Usually people It''s it''s not a lot. Usually people It''s
    it''s not a lot. Usually people

    train on order of magnitude of train on order of magnitude of train on order of
    magnitude of

    thousands. thousands. thousands.

    So I have trained this on uh So I have trained this on uh So I have trained this
    on uh

    and yeah thousand epochs and you can see and yeah thousand epochs and you can
    see and yeah thousand epochs and you can see

    the loss goes down like this. the loss goes down like this. the loss goes down
    like this.

    And finally you can sample from And finally you can sample from And finally you
    can sample from

    uh this using anal lang dynamics. And uh this using anal lang dynamics. And uh
    this using anal lang dynamics. And

    you can see these are some of the you can see these are some of the you can see
    these are some of the

    samples which were created but I did not samples which were created but I did
    not samples which were created but I did not

    uh sample it at the end of the last uh sample it at the end of the last uh sample
    it at the end of the last

    epoch. I think I this this sampling was epoch. I think I this this sampling was
    epoch. I think I this this sampling was

    done before when I ran it only for 200 done before when I ran it only for 200
    done before when I ran it only for 200

    epochs. But my my prediction is that if epochs. But my my prediction is that if
    epochs. But my my prediction is that if

    if I run this inference for this epox if I run this inference for this epox'
  concept_slugs:
  - noise-schedule
  - score-function
  - score-matching
- idx: 35
  start_sec: 2355.119
  end_sec: 2406.079
  text: 'if I run this inference for this epox

    where the loss is very low, you can see where the loss is very low, you can see
    where the loss is very low, you can see

    it''s almost 554, it''s almost 554, it''s almost 554,

    I''ll get something which is much better. I''ll get something which is much better.
    I''ll get something which is much better.

    You can see here it''s trying to predict You can see here it''s trying to predict
    You can see here it''s trying to predict

    the shape somewhat the shape somewhat the shape somewhat

    but uh it is not very clear what these but uh it is not very clear what these
    but uh it is not very clear what these

    shapes look like. shapes look like. shapes look like.

    Yeah. But uh overall this is the Yeah. But uh overall this is the Yeah. But uh
    overall this is the

    notebook which uh it will be great if notebook which uh it will be great if notebook
    which uh it will be great if

    you can run this and experiment the you can run this and experiment the you can
    run this and experiment the

    epochs the noise levels by yourself to epochs the noise levels by yourself to
    epochs the noise levels by yourself to

    understand how it works. I will upload understand how it works. I will upload
    understand how it works. I will upload

    this link also in the chat section. this link also in the chat section. this link
    also in the chat section.

    And just to summarize And just to summarize And just to summarize

    in this lecture we built upon the in this lecture we built upon the in this lecture
    we built upon the

    previous lecture by first explaining why previous lecture by first explaining
    why previous lecture by first explaining why

    adding noise makes such a big adding noise makes such a big adding noise makes
    such a big

    difference. We looked at a manifold difference. We looked at a manifold difference.
    We looked at a manifold

    hypothesis where we saw that the entire hypothesis where we saw that the entire
    hypothesis where we saw that the entire

    data resides on a very lowdimensional data resides on a very lowdimensional data
    resides on a very lowdimensional

    manifold manifold'
  concept_slugs:
  - noise-schedule
  - score-function
  - score-matching
- idx: 36
  start_sec: 2406.079
  end_sec: 2448.8
  text: 'manifold

    and by adding noise we are spreading it and by adding noise we are spreading it
    and by adding noise we are spreading it

    so that it occupies the entire space. so that it occupies the entire space. so
    that it occupies the entire space.

    And why does that help us? Because the And why does that help us? Because the
    And why does that help us? Because the

    data now occupies the entire space. We data now occupies the entire space. We
    data now occupies the entire space. We

    can calculate the gradients of the data can calculate the gradients of the data
    can calculate the gradients of the data

    at every single point in the space which at every single point in the space which
    at every single point in the space which

    is what we need to estimate the score is what we need to estimate the score is
    what we need to estimate the score

    function. If we have some gaps in the function. If we have some gaps in the function.
    If we have some gaps in the

    space where the gradient is not defined, space where the gradient is not defined,
    space where the gradient is not defined,

    you go with a compass and you encounter you go with a compass and you encounter
    you go with a compass and you encounter

    a region where the compass does not tell a region where the compass does not tell
    a region where the compass does not tell

    you where to go. It just flickers left you where to go. It just flickers left
    you where to go. It just flickers left

    and right. And that is the problem, and right. And that is the problem, and right.
    And that is the problem,

    right? You need your score function to right? You need your score function to
    right? You need your score function to

    be well defined at all the places not be well defined at all the places not be
    well defined at all the places not

    just near the data but also in areas just near the data but also in areas just
    near the data but also in areas

    which have very low density of of the which have very low density of of the'
  concept_slugs:
  - noise-schedule
  - score-function
  - score-matching
- idx: 37
  start_sec: 2448.8
  end_sec: 2501.27
  text: 'which have very low density of of the

    data. And adding noise helps us to do data. And adding noise helps us to do data.
    And adding noise helps us to do

    that. It helps us to have the gradient that. It helps us to have the gradient
    that. It helps us to have the gradient

    defined in all the points in the space. Okay. So now this is what we did in the
    Okay. So now this is what we did in the

    Vincent''s paper where we just gave a Vincent''s paper where we just gave a Vincent''s
    paper where we just gave a

    flick and we tried to predict how much flick and we tried to predict how much
    flick and we tried to predict how much

    flick we have given to the data and in flick we have given to the data and in
    flick we have given to the data and in

    that process we were able to learn the that process we were able to learn the
    that process we were able to learn the

    score function score function score function

    and in the paper by song and Arman we and in the paper by song and Arman we and
    in the paper by song and Arman we

    are also doing a flick but instead of are also doing a flick but instead of are
    also doing a flick but instead of

    one flick we are doing l different one flick we are doing l different one flick
    we are doing l different

    flicks and these flicks have different flicks and these flicks have different
    flicks and these flicks have different

    strength. We start with a very high strength. We start with a very high strength.
    We start with a very high

    flick which will deliberately move us flick which will deliberately move us flick
    which will deliberately move us

    away from the data so that we take care away from the data so that we take care
    away from the data so that we take care

    of the low density regions also. And of the low density regions also. And of the
    low density regions also. And

    then we also have flicks of different then we also have flicks of different then
    we also have flicks of different

    strength of low strength also. And once'
  concept_slugs:
  - noise-schedule
  - score-function
  - score-matching
- idx: 38
  start_sec: 2501.27
  end_sec: 2556.15
  text: 'strength of low strength also. And once strength of low strength also. And
    once

    we train the network to understand all we train the network to understand all
    we train the network to understand all

    these flicks when we are actually doing these flicks when we are actually doing
    these flicks when we are actually doing

    the inference we use language dynamics the inference we use language dynamics
    the inference we use language dynamics

    and initially we use the score network and initially we use the score network
    and initially we use the score network

    with a high variance so that we go to with a high variance so that we go to with
    a high variance so that we go to

    data points which are further away from data points which are further away from
    data points which are further away from

    our true data our true data our true data

    and then that is deliberate because we and then that is deliberate because we
    and then that is deliberate because we

    want to sample these low density regions want to sample these low density regions
    want to sample these low density regions

    also. Then we slowly reduce the variance also. Then we slowly reduce the variance
    also. Then we slowly reduce the variance

    so that we move closer and closer to the so that we move closer and closer to
    the so that we move closer and closer to the

    original data as much as possible original data as much as possible original data
    as much as possible

    and it it it works out brilliantly this and it it it works out brilliantly this
    and it it it works out brilliantly this

    analy dynamics. It''s it was one of the analy dynamics. It''s it was one of the
    analy dynamics. It''s it was one of the

    cornerstone in deep generative modeling cornerstone in deep generative modeling
    cornerstone in deep generative modeling

    and it is something which has it is and it is something which has it is and it
    is something which has it is

    still being used in modern generative AI still being used in modern generative
    AI still being used in modern generative AI

    pipelines where we are either generating pipelines where we are either generating
    pipelines where we are either generating

    images, videos or audio. As an homework,'
  concept_slugs:
  - noise-schedule
  - score-function
  - score-matching
- idx: 39
  start_sec: 2556.15
  end_sec: 2571.56
  text: 'images, videos or audio. As an homework, images, videos or audio. As an homework,

    I want you to play around with this I want you to play around with this I want
    you to play around with this

    notebook. Tweak a number of parameters notebook. Tweak a number of parameters
    notebook. Tweak a number of parameters

    to make sure that the final images that to make sure that the final images that
    to make sure that the final images that

    we are getting, they look right and they we are getting, they look right and they
    we are getting, they look right and they

    make sense. Thank you everyone and uh make sense. Thank you everyone and uh make
    sense. Thank you everyone and uh

    we''ll meet again in the next lecture.'
  concept_slugs:
  - noise-schedule
  - score-function
  - score-matching
---
# Lecture 7 - Noise Conditional Score Networks | Principles of Diffusion Models

See the structured chunks above.
