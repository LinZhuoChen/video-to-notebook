---
course_slug: diffusion-principles-vizuara
idx: 5
title: Lecture 6 - Denoising Score Matching | Principles of Diffusion Models
video_url: https://www.youtube.com/watch?v=6ELzfPXUqps
duration_sec: null
chunks:
- idx: 0
  start_sec: 3.669
  end_sec: 75.2
  text: 'Hello everyone, welcome to the next Hello everyone, welcome to the next

    lecture of the course principles of lecture of the course principles of lecture
    of the course principles of

    diffusion models. diffusion models. diffusion models.

    We have come quite far in this course. We have come quite far in this course.
    We have come quite far in this course.

    If you remember we started out with deep If you remember we started out with deep
    If you remember we started out with deep

    generative modeling. generative modeling. generative modeling.

    Then we covered variation autoenccoders. Then we covered variation autoenccoders.
    Then we covered variation autoenccoders.

    Then we looked at diffusion models. Then we looked at diffusion models. Then we
    looked at diffusion models.

    In the last lecture we looked at a In the last lecture we looked at a In the last
    lecture we looked at a

    different class of models called energy different class of models called energy
    different class of models called energy

    based models based models based models

    and within that we looked at a technique and within that we looked at a technique
    and within that we looked at a technique

    which is called as score matching. which is called as score matching. which is
    called as score matching.

    Energy based models appears to be a Energy based models appears to be a Energy
    based models appears to be a

    separate track using which we can separate track using which we can separate track
    using which we can

    predict the underlying true probability predict the underlying true probability
    predict the underlying true probability

    distribution distribution distribution

    for a given set of data samples to use the energy based models. However, to use
    the energy based models. However,

    we need a technique called score we need a technique called score we need a technique
    called score

    matching. matching. matching.

    What is a score? A score is like a What is a score? A score is like a What is
    a score? A score is like a

    compass which points towards the data. compass which points towards the data.
    compass which points towards the data.

    So let''s say you have data lying around So let''s say you have data lying around
    So let''s say you have data lying around

    in space and you go in that space with a in space and you go in that space with
    a'
  concept_slugs:
  - score-matching
  - tweedies-formula
- idx: 1
  start_sec: 75.2
  end_sec: 165.519
  text: 'in space and you go in that space with a

    compass which tells you which direction compass which tells you which direction
    compass which tells you which direction

    should I move so that I move closer to should I move so that I move closer to
    should I move so that I move closer to

    the data the data the data

    that is called as the score function. that is called as the score function. that
    is called as the score function.

    Now if you have the score function at Now if you have the score function at Now
    if you have the score function at

    every single point you can sample you every single point you can sample you every
    single point you can sample you

    using langin dynamics and you can using langin dynamics and you can using langin
    dynamics and you can

    predict samples from the true data predict samples from the true data predict
    samples from the true data

    distribution distribution

    which is a alternative path for which is a alternative path for which is a alternative
    path for

    predicting the true probability predicting the true probability predicting the
    true probability

    distribution given the data samples. Now the formula for the score was given Now
    the formula for the score was given

    as this. This is the true data distribution which This is the true data distribution
    which

    we don''t know. All we have is we have we don''t know. All we have is we have
    we don''t know. All we have is we have

    access to these samples. access to these samples. access to these samples.

    So what we do is we find the neural So what we do is we find the neural So what
    we do is we find the neural

    network which matches this score as close as which matches this score as close
    as

    possible. possible. possible.

    That is why this technique is called That is why this technique is called That
    is why this technique is called

    score matching. The problem that we encountered with The problem that we encountered
    with

    this technique was this technique was this technique was

    we do not have access to the true we do not have access to the true we do not
    have access to the true

    probability distribution. Right? So we probability distribution. Right? So we'
  concept_slugs:
  - score-matching
  - tweedies-formula
- idx: 2
  start_sec: 165.519
  end_sec: 234.07
  text: 'probability distribution. Right? So we

    do not know this term. do not know this term. do not know this term.

    In supervised machine learning, we often In supervised machine learning, we often
    In supervised machine learning, we often

    predict the predict the predict the

    target Y target Y target Y

    which is predicted by a model and we which is predicted by a model and we which
    is predicted by a model and we

    have the true target have the true target have the true target

    and then we do a mean square error and then we do a mean square error and then
    we do a mean square error

    between the prediction and the true. between the prediction and the true. between
    the prediction and the true.

    But this is always known But this is always known But this is always known

    in a lot of cases. We have seen before in a lot of cases. We have seen before
    in a lot of cases. We have seen before

    in machine learning. However, this is a in machine learning. However, this is
    a in machine learning. However, this is a

    very special type of a problem where we very special type of a problem where we
    very special type of a problem where we

    do not know the target do not know the target do not know the target

    and we encountered this problem in the and we encountered this problem in the
    and we encountered this problem in the

    last lecture and we were thinking of last lecture and we were thinking of last
    lecture and we were thinking of

    ways to circumvent it. ways to circumvent it. ways to circumvent it.

    Gladly this paper came to the rescue Gladly this paper came to the rescue Gladly
    this paper came to the rescue

    which was written in the year 2005 which was written in the year 2005 which was
    written in the year 2005

    which is 20 years which is 20 years which is 20 years

    before this lecture is being recorded. This paper found an alternative loss This
    paper found an alternative loss

    function that only requires the data function that only requires the data function
    that only requires the data

    samples that is it circumvents the samples that is it circumvents the samples
    that is it circumvents the

    requirement of this entire probability'
  concept_slugs:
  - score-matching
  - tweedies-formula
- idx: 3
  start_sec: 234.07
  end_sec: 307.6
  text: 'requirement of this entire probability requirement of this entire probability

    distribution which we have no idea distribution which we have no idea distribution
    which we have no idea

    about. about. about.

    This is where the beauty of the stream This is where the beauty of the stream
    This is where the beauty of the stream

    of statistics lies in. of statistics lies in. of statistics lies in.

    Using statistics, people are able to Using statistics, people are able to Using
    statistics, people are able to

    conveniently conveniently conveniently

    express objective functions so that the express objective functions so that the
    express objective functions so that the

    meaning of that objective function is is meaning of that objective function is
    is meaning of that objective function is is

    is not lost and at the same time it is not lost and at the same time it is not
    lost and at the same time it

    suddenly becomes trackable which means suddenly becomes trackable which means
    suddenly becomes trackable which means

    we can calculate it. Now uh the loss function look as Now uh the loss function
    look as

    follows. So you can see first of all that So you can see first of all that

    this is our predicted score this is our predicted score this is our predicted
    score

    and the entire loss function only and the entire loss function only and the entire
    loss function only

    depends on the predicted score. We do depends on the predicted score. We do depends
    on the predicted score. We do

    not see s of x in this expression which not see s of x in this expression which
    not see s of x in this expression which

    is the true score is the true score is the true score

    and these x are data samples which are and these x are data samples which are
    and these x are data samples which are

    provided to us which is available to us. provided to us which is available to
    us. provided to us which is available to us.

    This means that this entire loss This means that this entire loss This means that
    this entire loss

    function can be calculated using the function can be calculated using the function
    can be calculated using the

    data which is available to us which is data which is available to us which is'
  concept_slugs:
  - score-matching
  - tweedies-formula
- idx: 4
  start_sec: 307.6
  end_sec: 368.95
  text: 'data which is available to us which is

    what makes it incredibly powerful. So we are grateful to this author to So we
    are grateful to this author to

    have made the stream of score matching have made the stream of score matching
    have made the stream of score matching

    accessible for everyone so that it can accessible for everyone so that it can
    accessible for everyone so that it can

    be used for deep generative modeling. be used for deep generative modeling. be
    used for deep generative modeling.

    Now we looked at the meaning of these Now we looked at the meaning of these Now
    we looked at the meaning of these

    two terms which means something very two terms which means something very two
    terms which means something very

    specific. The first is the trace of a specific. The first is the trace of a specific.
    The first is the trace of a

    matrix. What is a trace of a matrix? matrix. What is a trace of a matrix? matrix.
    What is a trace of a matrix?

    Let''s say you have a matrix which looks Let''s say you have a matrix which looks
    Let''s say you have a matrix which looks

    like this. A b c d. The trace is the like this. A b c d. The trace is the like
    this. A b c d. The trace is the

    summation of the diagonal elements which summation of the diagonal elements which
    summation of the diagonal elements which

    is a plus b. is a plus b. is a plus b.

    Now the first term in the loss function Now the first term in the loss function
    Now the first term in the loss function

    is the trace which means that ideally we is the trace which means that ideally
    we is the trace which means that ideally we

    want the trace to go down as much as want the trace to go down as much as want
    the trace to go down as much as

    possible. possible.

    This means that we are creating sinks in This means that we are creating sinks
    in This means that we are creating sinks in

    the data. What is a sync? Anything that the data. What is a sync? Anything that
    the data. What is a sync? Anything that

    is close to the sink is pulled inwards.'
  concept_slugs:
  - score-matching
  - tweedies-formula
- idx: 5
  start_sec: 368.95
  end_sec: 411.52
  text: 'is close to the sink is pulled inwards. is close to the sink is pulled inwards.

    It''s like a black hole. If you go near a It''s like a black hole. If you go near
    a It''s like a black hole. If you go near a

    black hole, you are pulled inwards, black hole, you are pulled inwards, black
    hole, you are pulled inwards,

    right? It''s exactly like that. Which right? It''s exactly like that. Which right?
    It''s exactly like that. Which

    means that if you are navigating with means that if you are navigating with means
    that if you are navigating with

    the compass in your hand and you go the compass in your hand and you go the compass
    in your hand and you go

    close to the data, you''ll be pulled close to the data, you''ll be pulled close
    to the data, you''ll be pulled

    inside the data which is exactly what we inside the data which is exactly what
    we inside the data which is exactly what we

    want. And the second term is where you want. And the second term is where you
    want. And the second term is where you

    are forcing the magnitude of the score are forcing the magnitude of the score
    are forcing the magnitude of the score

    to be zero especially at the points to be zero especially at the points to be
    zero especially at the points

    where the true data lies. where the true data lies. where the true data lies.

    So this term will be minimum only when So this term will be minimum only when
    So this term will be minimum only when

    the magnitude is zero. Right? the magnitude is zero. Right? the magnitude is zero.
    Right?

    So what does that mean? Let''s say you go So what does that mean? Let''s say you
    go So what does that mean? Let''s say you go

    with the compass and you with the trace with the compass and you with the trace
    with the compass and you with the trace

    term you are pulled close to the data. term you are pulled close to the data.
    term you are pulled close to the data.

    Now assume that you you are close to the Now assume that you you are close to
    the'
  concept_slugs:
  - score-matching
  - tweedies-formula
- idx: 6
  start_sec: 411.52
  end_sec: 468.39
  text: 'Now assume that you you are close to the

    data. Assume that you are the data data. Assume that you are the data data. Assume
    that you are the data

    itself. Then you don''t need to move itself. Then you don''t need to move itself.
    Then you don''t need to move

    around right because you have already around right because you have already around
    right because you have already

    reached the right location. reached the right location. reached the right location.

    That''s why at that point you need those That''s why at that point you need those
    That''s why at that point you need those

    points to be stationary points to be stationary points to be stationary

    which is exactly what this term forces which is exactly what this term forces
    which is exactly what this term forces

    the score function at the true data the score function at the true data the score
    function at the true data

    points to be. A combination of this points to be. A combination of this points
    to be. A combination of this

    means the loss function will try to take means the loss function will try to take
    means the loss function will try to take

    or try to predict the score function or try to predict the score function or try
    to predict the score function

    such that when you set out with a such that when you set out with a such that
    when you set out with a

    compass in the data field you will reach compass in the data field you will reach
    compass in the data field you will reach

    the true data samples as much as the true data samples as much as the true data
    samples as much as

    possible. possible.

    We looked at as at at at an example in We looked at as at at at an example in
    We looked at as at at at an example in

    the last lecture where this was our the last lecture where this was our the last
    lecture where this was our

    training data and very smartly we training data and very smartly we training data
    and very smartly we

    learned to predict the score function learned to predict the score function learned
    to predict the score function

    for this training data at every single'
  concept_slugs:
  - score-matching
  - tweedies-formula
- idx: 7
  start_sec: 468.39
  end_sec: 530.959
  text: 'for this training data at every single for this training data at every single

    point in the space. You can see the point in the space. You can see the point
    in the space. You can see the

    score function is depicted by arrows score function is depicted by arrows score
    function is depicted by arrows

    over here. over here. over here.

    So look at the points which are close to So look at the points which are close
    to So look at the points which are close to

    the data. Let''s say we look at this the data. Let''s say we look at this the
    data. Let''s say we look at this

    point. The score pulls me inwards. The point. The score pulls me inwards. The
    point. The score pulls me inwards. The

    score pulls me inwards. The score pulls score pulls me inwards. The score pulls
    score pulls me inwards. The score pulls

    me inwards. me inwards. me inwards.

    So intuitively it looks like everything So intuitively it looks like everything
    So intuitively it looks like everything

    is pointed towards the true data is pointed towards the true data is pointed towards
    the true data

    samples, right? Which is exactly what we samples, right? Which is exactly what
    we samples, right? Which is exactly what we

    want our score to do. want our score to do. want our score to do.

    So this is like a compass. If you set So this is like a compass. If you set So
    this is like a compass. If you set

    out with a compass, you will eventually out with a compass, you will eventually
    out with a compass, you will eventually

    go like this. If you start in this go like this. If you start in this go like
    this. If you start in this

    direction, direction, direction,

    if you start in this direction, you will if you start in this direction, you will
    if you start in this direction, you will

    go like this. If you start here, then you''ll probably If you start here, then
    you''ll probably

    go like this. go like this. go like this.

    If you start here, then you''ll probably go like this.

    So just if you look at this visually you So just if you look at this visually
    you'
  concept_slugs:
  - score-matching
  - tweedies-formula
- idx: 8
  start_sec: 530.959
  end_sec: 602.24
  text: 'So just if you look at this visually you

    can see that wherever I start in the can see that wherever I start in the can
    see that wherever I start in the

    field and I follow the score function I field and I follow the score function
    I field and I follow the score function I

    am led to am led to am led to

    points which lie very close to the points which lie very close to the points which
    lie very close to the

    actual data samples. This this almost looks like magic and This this almost looks
    like magic and

    people don''t discuss about score people don''t discuss about score people don''t
    discuss about score

    function enough but we will see in one function enough but we will see in one
    function enough but we will see in one

    of the subsequent lectures that it forms of the subsequent lectures that it forms
    of the subsequent lectures that it forms

    the foundation behind score-based the foundation behind score-based the foundation
    behind score-based

    diffusion models which is used in modern diffusion models which is used in modern
    diffusion models which is used in modern

    generative AI pipelines. Okay, let''s go ahead. Okay, let''s go ahead.

    Okay, so this is excellent. But uh Okay, so this is excellent. But uh Okay, so
    this is excellent. But uh

    the problem is that this technique is the problem is that this technique is the
    problem is that this technique is

    not used in practice. People don''t use this score matching People don''t use
    this score matching

    technique using this formula in technique using this formula in technique using
    this formula in

    practice. practice. practice.

    And some of you might be wondering why And some of you might be wondering why
    And some of you might be wondering why

    is that the case? Haven''t we derived a is that the case? Haven''t we derived
    a is that the case? Haven''t we derived a

    formula which only depends on the data formula which only depends on the data
    formula which only depends on the data

    samples and the predicted score samples and the predicted score samples and the
    predicted score

    function? So and even we have looked at function? So and even we have looked at'
  concept_slugs:
  - score-matching
  - tweedies-formula
- idx: 9
  start_sec: 602.24
  end_sec: 679.03
  text: 'function? So and even we have looked at

    one example where uh the loss function one example where uh the loss function
    one example where uh the loss function

    actually works. actually works. actually works.

    The the main problem is that if you look The the main problem is that if you look
    The the main problem is that if you look

    at at at

    the trace of a matrix of dimension D. So the trace of a matrix of dimension D.
    So the trace of a matrix of dimension D. So

    for example here the dimensions was two and the number of elements in this and
    the number of elements in this

    matrix is matrix is matrix is

    2 into 2 which is four. So to calculate the trace we need to So to calculate the
    trace we need to

    calculate all these elements in the calculate all these elements in the calculate
    all these elements in the

    matrix so that we have all the diagonal matrix so that we have all the diagonal
    matrix so that we have all the diagonal

    elements ready. elements ready. elements ready.

    Now imagine that instead of the number Now imagine that instead of the number
    Now imagine that instead of the number

    of dimensions being two, you have the of dimensions being two, you have the of
    dimensions being two, you have the

    number of dimensions as n. So you have a large n dimensional So you have a large
    n dimensional

    matrix, right? How many elements will matrix, right? How many elements will matrix,
    right? How many elements will

    this matrix contain? You have n rows and this matrix contain? You have n rows
    and this matrix contain? You have n rows and

    n columns. So totally there will be n n columns. So totally there will be n n
    columns. So totally there will be n

    into n which is n² elements. into n which is n² elements. into n which is n² elements.

    And you cannot calculate the trace And you cannot calculate the trace And you
    cannot calculate the trace

    unless you predict the entire matrix unless you predict the entire matrix unless
    you predict the entire matrix

    because that''s when you will know all because that''s when you will know all
    because that''s when you will know all

    the diagonal elements. You can''t'
  concept_slugs:
  - score-matching
  - tweedies-formula
- idx: 10
  start_sec: 679.03
  end_sec: 757.519
  text: 'the diagonal elements. You can''t the diagonal elements. You can''t

    individually calculate the diagonal individually calculate the diagonal individually
    calculate the diagonal

    elements. elements. elements.

    That is why the order of computation That is why the order of computation That
    is why the order of computation

    for this loss function becomes n². for this loss function becomes n². for this
    loss function becomes n².

    In real life, n is a very large number. In real life, n is a very large number.
    In real life, n is a very large number.

    For example, let''s take an example of For example, let''s take an example of
    For example, let''s take an example of

    the image of cats and you have a matrix the image of cats and you have a matrix
    the image of cats and you have a matrix

    which is 28 by 28, right? which is 28 by 28, right? which is 28 by 28, right?

    So there are 784 pixel values. So there are 784 pixel values. So there are 784
    pixel values.

    So n is 784 and n byn then becomes 784 So n is 784 and n byn then becomes 784
    So n is 784 and n byn then becomes 784

    squared squared squared

    which is huge. which is huge. which is huge.

    So So So

    this loss function is not used in this loss function is not used in this loss
    function is not used in

    practice simply because practice simply because practice simply because

    the computational complexity the computational complexity the computational complexity

    increases as the square of the number of increases as the square of the number
    of increases as the square of the number of

    dimensions dimensions dimensions

    of the data. of the data. of the data.

    And most of the real life data And most of the real life data And most of the
    real life data

    lies in spaces which cover a lot of lies in spaces which cover a lot of lies in
    spaces which cover a lot of

    dimensions. dimensions. dimensions.

    And it becomes impractical to use this And it becomes impractical to use this
    And it becomes impractical to use this

    formulation in real life formulation in real life formulation in real life

    in in real life use cases. And that is in in real life use cases. And that is'
  concept_slugs:
  - score-matching
  - tweedies-formula
- idx: 11
  start_sec: 757.519
  end_sec: 840.72
  text: 'in in real life use cases. And that is

    why for a lot of for many years actually why for a lot of for many years actually
    why for a lot of for many years actually

    uh uh uh

    the score matching technique only existed as a theoretical construct only existed
    as a theoretical construct

    which can be used to solve toy problems. which can be used to solve toy problems.
    which can be used to solve toy problems.

    It was never really considered seriously It was never really considered seriously
    It was never really considered seriously

    for actual practical problems and where for actual practical problems and where
    for actual practical problems and where

    you are given data sets which you are given data sets which you are given data
    sets which

    represented some uh represented some uh represented some uh

    complex spatial information. complex spatial information. complex spatial information.

    So even though this paper came out in So even though this paper came out in So
    even though this paper came out in

    2015 or 2005, 2015 or 2005, 2015 or 2005,

    the next important paper came in 2019 the next important paper came in 2019 the
    next important paper came in 2019

    which was which was which was

    14 years gap after the development of 14 years gap after the development of 14
    years gap after the development of

    this paper. So let''s try to understand what people So let''s try to understand
    what people

    did to circumvent this issue. did to circumvent this issue. did to circumvent
    this issue.

    And this is what leads us to the main And this is what leads us to the main And
    this is what leads us to the main

    title of this chapter which is called as title of this chapter which is called
    as title of this chapter which is called as

    dnoising score matching. You might dnoising score matching. You might dnoising
    score matching. You might

    relate this to our diffusion lecture relate this to our diffusion lecture relate
    this to our diffusion lecture

    which was titled as dnoising diffusion which was titled as dnoising diffusion
    which was titled as dnoising diffusion

    probabilistic models. So here we have probabilistic models. So here we have probabilistic
    models. So here we have

    the same word dn noising right and in the same word dn noising right and in'
  concept_slugs:
  - score-matching
  - tweedies-formula
- idx: 12
  start_sec: 840.72
  end_sec: 910.639
  text: 'the same word dn noising right and in

    diffusion that made sense because we diffusion that made sense because we diffusion
    that made sense because we

    started from a noisy image and then we started from a noisy image and then we
    started from a noisy image and then we

    removed noise in a stepbystep manner to removed noise in a stepbystep manner to
    removed noise in a stepbystep manner to

    reach the original image. That is why it reach the original image. That is why
    it reach the original image. That is why it

    was called as dnoising. was called as dnoising. was called as dnoising.

    But in the field of energy based models But in the field of energy based models
    But in the field of energy based models

    or if we use the term score matching or if we use the term score matching or if
    we use the term score matching

    what does this dnoising exactly mean? what does this dnoising exactly mean? what
    does this dnoising exactly mean?

    Let us try to understand that in detail. Okay. So this connection between score
    Okay. So this connection between score

    matching and matching and matching and

    dinoising autoenccoders actually came in dinoising autoenccoders actually came
    in dinoising autoenccoders actually came in

    the year the year the year

    2010. 2010. 2010.

    So in this lecture we are going to see So in this lecture we are going to see
    So in this lecture we are going to see

    three evolutions from 2005 which is three evolutions from 2005 which is three
    evolutions from 2005 which is

    something we have already seen. Then we something we have already seen. Then we
    something we have already seen. Then we

    look at this paper by Pascal Vincent look at this paper by Pascal Vincent look
    at this paper by Pascal Vincent

    which came out in 2010. which came out in 2010. which came out in 2010.

    And then finally we look at another And then finally we look at another And then
    finally we look at another

    paper by Song and Armon which came out paper by Song and Armon which came out
    paper by Song and Armon which came out

    in 2019. in 2019. in 2019.

    These three papers are going to form the These three papers are going to form
    the'
  concept_slugs:
  - score-matching
  - tweedies-formula
- idx: 13
  start_sec: 910.639
  end_sec: 982.399
  text: 'These three papers are going to form the

    foundation of the theory of denoising foundation of the theory of denoising foundation
    of the theory of denoising

    score matching. Okay. So this technique was introduced Okay. So this technique
    was introduced

    by Pascal Vincent in 2010. It is quite by Pascal Vincent in 2010. It is quite
    by Pascal Vincent in 2010. It is quite

    interesting that so many of these papers interesting that so many of these papers
    interesting that so many of these papers

    are actually single author papers. are actually single author papers. are actually
    single author papers.

    It it seemed like at that time 10 15 It it seemed like at that time 10 15 It it
    seemed like at that time 10 15

    years back people working as single years back people working as single years
    back people working as single

    authors in the field of IML was quite authors in the field of IML was quite authors
    in the field of IML was quite

    common and they were actually very common and they were actually very common and
    they were actually very

    efficient as well. efficient as well. efficient as well.

    Okay. So what Pascal Vincent said was Okay. So what Pascal Vincent said was Okay.
    So what Pascal Vincent said was

    very interesting. very interesting. very interesting.

    He said that first let us look at He said that first let us look at He said that
    first let us look at

    our score matching objective. This is the original score matching This is the
    original score matching

    objective right where this is the objective right where this is the objective
    right where this is the

    predicted score and this is the true score. and this is the true score.

    Now remember we started out with this Now remember we started out with this Now
    remember we started out with this

    exact same formulation where we said exact same formulation where we said exact
    same formulation where we said

    that the true score is not accessible to that the true score is not accessible
    to that the true score is not accessible to

    us. That is why we created a different us. That is why we created a different
    us. That is why we created a different

    formulation which was trackable. But formulation which was trackable. But'
  concept_slugs:
  - score-matching
  - tweedies-formula
- idx: 14
  start_sec: 982.399
  end_sec: 1062.08
  text: 'formulation which was trackable. But

    that did not make sense because the that did not make sense because the that did
    not make sense because the

    complexity of computations squared complexity of computations squared complexity
    of computations squared

    increases as the square of the increases as the square of the increases as the
    square of the

    dimensions. dimensions.

    So uh what Pascal Vincent said can be So uh what Pascal Vincent said can be So
    uh what Pascal Vincent said can be

    understood with a practical analogy understood with a practical analogy understood
    with a practical analogy

    which I have constructed. I''ll be which I have constructed. I''ll be which I
    have constructed. I''ll be

    explaining that analogy first to you and explaining that analogy first to you
    and explaining that analogy first to you and

    then we''ll be going at understanding then we''ll be going at understanding then
    we''ll be going at understanding

    what Pascal Vincent said. what Pascal Vincent said. what Pascal Vincent said.

    So let us focus our attention now on So let us focus our attention now on So let
    us focus our attention now on

    understanding that analogy. Okay. So imagine that uh you have a Okay. So imagine
    that uh you have a

    tabletop. tabletop. tabletop.

    So this is the tabletop and uh there are and uh there are

    invisible magnets which are hidden at invisible magnets which are hidden at invisible
    magnets which are hidden at

    specific spots on this table specific spots on this table specific spots on this
    table

    and these magnets they represent your and these magnets they represent your and
    these magnets they represent your

    real data. real data. real data.

    So for example you can see this is one So for example you can see this is one
    So for example you can see this is one

    magnet. This is one magnet. This is magnet. This is one magnet. This is magnet.
    This is one magnet. This is

    another magnet. So you have a lot of another magnet. So you have a lot of another
    magnet. So you have a lot of

    magnets which are spread around on the magnets which are spread around on the
    magnets which are spread around on the

    table table table

    and you do have access to some of them. and you do have access to some of them.'
  concept_slugs:
  - score-matching
  - tweedies-formula
- idx: 15
  start_sec: 1062.08
  end_sec: 1128.96
  text: 'and you do have access to some of them.

    So let''s say you have access to 15 or 20 So let''s say you have access to 15
    or 20 So let''s say you have access to 15 or 20

    of these magnets but many others are of these magnets but many others are of these
    magnets but many others are

    actually hidden. You don''t have access actually hidden. You don''t have access
    actually hidden. You don''t have access

    to all the magnets which are there on to all the magnets which are there on to
    all the magnets which are there on

    the table but you have access to some the table but you have access to some the
    table but you have access to some

    magnets. So ignore these blue lines at the moment So ignore these blue lines at
    the moment

    and just focus your attention on these and just focus your attention on these
    and just focus your attention on these

    black balls which represent the magnets black balls which represent the magnets
    black balls which represent the magnets

    which are put on the table. Now our goal is to draw a map of the Now our goal
    is to draw a map of the

    magnetic field magnetic field magnetic field

    that tells you for any point on the that tells you for any point on the that tells
    you for any point on the

    table which direction is the nearest table which direction is the nearest table
    which direction is the nearest

    magnetic magnet is pulling. magnetic magnet is pulling. magnetic magnet is pulling.

    So So

    let''s say I pick a point here let''s say I pick a point here let''s say I pick
    a point here

    and if I knew the magnetic field on this and if I knew the magnetic field on this
    and if I knew the magnetic field on this

    table I could point I could say that oh table I could point I could say that oh
    table I could point I could say that oh

    this is the direction in which the this is the direction in which the this is
    the direction in which the

    nearest magnet is pulling me. If I take nearest magnet is pulling me. If I take'
  concept_slugs:
  - score-matching
  - tweedies-formula
- idx: 16
  start_sec: 1128.96
  end_sec: 1185.27
  text: 'nearest magnet is pulling me. If I take

    a point here I could say that this is a point here I could say that this is a
    point here I could say that this is

    the direction in which the nearest the direction in which the nearest the direction
    in which the nearest

    magnet is pulling me. magnet is pulling me. magnet is pulling me.

    The issue is that you cannot construct The issue is that you cannot construct
    The issue is that you cannot construct

    this magnetic field very easily because this magnetic field very easily because
    this magnetic field very easily because

    many of the magnets are hidden. You do many of the magnets are hidden. You do
    many of the magnets are hidden. You do

    not have access to all the magnets not have access to all the magnets not have
    access to all the magnets

    on the table. You have access to only on the table. You have access to only on
    the table. You have access to only

    some specific magnets and many others some specific magnets and many others some
    specific magnets and many others

    are actually hidden. are actually hidden. are actually hidden.

    So now we try to understand how do we So now we try to understand how do we So
    now we try to understand how do we

    construct this magnetic field in the construct this magnetic field in the construct
    this magnetic field in the

    first place so that wherever we are we first place so that wherever we are we
    first place so that wherever we are we

    are pulled in the direction of the are pulled in the direction of the are pulled
    in the direction of the

    nearest magnet that is what we want. Now if you think about this problem from
    Now if you think about this problem from

    a physics lens, you might think that a physics lens, you might think that a physics
    lens, you might think that

    okay my first job is to find all these okay my first job is to find all these
    okay my first job is to find all these

    magnets and then I will construct a map magnets and then I will construct a map
    magnets and then I will construct a map

    using using using

    uh I will I will superimpose the'
  concept_slugs:
  - score-matching
  - tweedies-formula
- idx: 17
  start_sec: 1185.27
  end_sec: 1251.75
  text: 'uh I will I will superimpose the uh I will I will superimpose the

    magnetic fields for all these different magnetic fields for all these different
    magnetic fields for all these different

    magnets. magnets. magnets.

    But that is not a very practical But that is not a very practical But that is
    not a very practical

    approach because you do not know all approach because you do not know all approach
    because you do not know all

    these points where the magnets are these points where the magnets are these points
    where the magnets are

    actually located because many of them actually located because many of them actually
    located because many of them

    are hidden. So it''s very hard to are hidden. So it''s very hard to are hidden.
    So it''s very hard to

    pinpoint these locations. pinpoint these locations. pinpoint these locations.

    So let''s understand another alternative So let''s understand another alternative
    So let''s understand another alternative

    trick which you could do. trick which you could do. trick which you could do.

    If you just look at the empty table, you If you just look at the empty table,
    you If you just look at the empty table, you

    can''t calculate the magnetic field. You can''t calculate the magnetic field.
    You can''t calculate the magnetic field. You

    don''t know where the magnets are or how don''t know where the magnets are or
    how don''t know where the magnets are or how

    strong they are. strong they are. strong they are.

    For example, there might be more magnets For example, there might be more magnets
    For example, there might be more magnets

    than you see and you do not know the than you see and you do not know the than
    you see and you do not know the

    magnetic field at all places. So we magnetic field at all places. So we magnetic
    field at all places. So we

    understand the problem statement which understand the problem statement which
    understand the problem statement which

    we have at our hands right now. Okay. So now we do a small trick. Okay. So now
    we do a small trick.

    The trick that we do is The trick that we do is The trick that we do is

    we take a magnet. we take a magnet. we take a magnet.

    We take any magnet on the table and we'
  concept_slugs:
  - score-matching
  - tweedies-formula
- idx: 18
  start_sec: 1251.75
  end_sec: 1309.84
  text: 'We take any magnet on the table and we We take any magnet on the table and
    we

    flick it with a hand just like this. I''m flick it with a hand just like this.
    I''m flick it with a hand just like this. I''m

    doing right now. I use my wrists and I doing right now. I use my wrists and I
    doing right now. I use my wrists and I

    flick the magnet. flick the magnet. flick the magnet.

    So the magnet So the magnet So the magnet

    goes around this and then stop goes around this and then stop goes around this
    and then stop

    somewhere, right? Which is what you see somewhere, right? Which is what you see
    somewhere, right? Which is what you see

    here. This is where the magnet stops. Okay. So uh Okay. So uh

    when I flick it, I can exactly see where when I flick it, I can exactly see where
    when I flick it, I can exactly see where

    the magnet has stopped. Right? the magnet has stopped. Right? the magnet has stopped.
    Right?

    So we start at a magnet. So we start at a magnet. So we start at a magnet.

    We place a metal ball exactly on the top We place a metal ball exactly on the
    top We place a metal ball exactly on the top

    of a hidden magnet and we flick the ball of a hidden magnet and we flick the ball
    of a hidden magnet and we flick the ball

    in a random direction. It rolls away and in a random direction. It rolls away
    and in a random direction. It rolls away and

    stops at a new point. stops at a new point. stops at a new point.

    And this is the new point that we have. And this is the new point that we have.
    And this is the new point that we have.

    Okay, this is step number one. What do Okay, this is step number one. What do
    Okay, this is step number one. What do

    we do next? we do next? we do next?

    Next, we bring in a student and we show Next, we bring in a student and we show
    Next, we bring in a student and we show

    the student, look, this is the ball''s the student, look, this is the ball''s'
  concept_slugs:
  - score-matching
  - tweedies-formula
- idx: 19
  start_sec: 1309.84
  end_sec: 1382.0
  text: 'the student, look, this is the ball''s

    new location. new location. new location.

    and we hide the original uh magnet and we hide the original uh magnet and we hide
    the original uh magnet

    location. So we just show the student location. So we just show the student location.
    So we just show the student

    this is the new location. The student is just shown this new The student is just
    shown this new

    location and we ask the student draw the location and we ask the student draw
    the location and we ask the student draw the

    force to pull the magnet or or to pull force to pull the magnet or or to pull
    force to pull the magnet or or to pull

    this ball back to the start. So what the student sees is the students So what
    the student sees is the students

    only sees the ball at the new location. only sees the ball at the new location.
    only sees the ball at the new location.

    The student has absolutely no idea where The student has absolutely no idea where
    The student has absolutely no idea where

    this ball has started from. But the this ball has started from. But the this ball
    has started from. But the

    student is drawing is is trying to draw student is drawing is is trying to draw
    student is drawing is is trying to draw

    a force arrow a force arrow a force arrow

    which will pull the ball back to the which will pull the ball back to the which
    will pull the ball back to the

    start. And you might say that okay the student And you might say that okay the
    student

    is going to make a lot of mistakes right is going to make a lot of mistakes right
    is going to make a lot of mistakes right

    because the student has absolutely no because the student has absolutely no because
    the student has absolutely no

    idea where the ball started from before idea where the ball started from before
    idea where the ball started from before

    it was flicked. it was flicked. it was flicked.

    But that is exactly the point. The But that is exactly the point. The But that
    is exactly the point. The

    student has no idea where this student has no idea where this'
  concept_slugs:
  - score-matching
  - tweedies-formula
- idx: 20
  start_sec: 1382.0
  end_sec: 1442.71
  text: 'student has no idea where this

    new ball position came from. But we know new ball position came from. But we know
    new ball position came from. But we know

    where it came from. where it came from. where it came from.

    So So

    if we can give the student feedback if we can give the student feedback if we
    can give the student feedback

    based on the student''s prediction and based on the student''s prediction and
    based on the student''s prediction and

    our knowledge, we can teach the student our knowledge, we can teach the student
    our knowledge, we can teach the student

    how to draw the force to pull the ball how to draw the force to pull the ball
    how to draw the force to pull the ball

    back to the starting point for every back to the starting point for every back
    to the starting point for every

    possible noisy data in the field. possible noisy data in the field. possible noisy
    data in the field.

    Let''s take another example. Let''s say we Let''s take another example. Let''s
    say we Let''s take another example. Let''s say we

    flick a ball and it reaches over here. flick a ball and it reaches over here.
    flick a ball and it reaches over here.

    You ask the student draw a vector You ask the student draw a vector You ask the
    student draw a vector

    to pull the ball back to the start. to pull the ball back to the start. to pull
    the ball back to the start.

    Let''s say the student draws this vector. But you know exactly that you have But
    you know exactly that you have

    started from here. So this is the true started from here. So this is the true
    started from here. So this is the true

    vector. Then you tell the student that vector. Then you tell the student that
    vector. Then you tell the student that

    look this is wrong. I started from here. look this is wrong. I started from here.
    look this is wrong. I started from here.

    Improve your prediction the next time. Improve your prediction the next time.
    Improve your prediction the next time.

    Similarly, you do it for all these Similarly, you do it for all these Similarly,
    you do it for all these

    balls, all these magnets that you know'
  concept_slugs:
  - score-matching
  - tweedies-formula
- idx: 21
  start_sec: 1442.71
  end_sec: 1502.96
  text: 'balls, all these magnets that you know balls, all these magnets that you
    know

    that the magnets are placed there. You that the magnets are placed there. You
    that the magnets are placed there. You

    place you uh you do it for all the place you uh you do it for all the place you
    uh you do it for all the

    points in the space. You flick it. You points in the space. You flick it. You
    points in the space. You flick it. You

    see where it has reached. You ask the see where it has reached. You ask the see
    where it has reached. You ask the

    student to draw a vector which can pull student to draw a vector which can pull
    student to draw a vector which can pull

    it back to the start and then you give a it back to the start and then you give
    a it back to the start and then you give a

    feedback to the student that no this is feedback to the student that no this is
    feedback to the student that no this is

    right this is wrong and the student will right this is wrong and the student will
    right this is wrong and the student will

    correct itself slowly and steadily what correct itself slowly and steadily what
    correct itself slowly and steadily what

    will happen is that the student will will happen is that the student will will
    happen is that the student will

    learn to pull the ball back learn to pull the ball back learn to pull the ball
    back

    from any position on the table from any position on the table from any position
    on the table

    to the position it started before it was to the position it started before it
    was to the position it started before it was

    flicked. And through this process, wouldn''t the And through this process, wouldn''t
    the

    student learn the magnetic field at all student learn the magnetic field at all
    student learn the magnetic field at all

    points in the field? The student is essentially learning the The student is essentially
    learning the

    direction in which this data should be direction in which this data should be
    direction in which this data should be

    this point should be should move so that this point should be should move so that'
  concept_slugs:
  - score-matching
  - tweedies-formula
- idx: 22
  start_sec: 1502.96
  end_sec: 1579.99
  text: 'this point should be should move so that

    it goes back to the original position it goes back to the original position it
    goes back to the original position

    and that is exactly the direction of the and that is exactly the direction of
    the and that is exactly the direction of the

    magnetic field at that point. Okay. So now let''s understand how this Okay. So
    now let''s understand how this

    analogy relates to Vincent''s ideas in analogy relates to Vincent''s ideas in
    analogy relates to Vincent''s ideas in

    his paper. So the hidden magnets in the analogy So the hidden magnets in the analogy

    represents the clean data points. This represents the clean data points. This
    represents the clean data points. This

    is denoted by the following symbol. So this probably you might have guessed So
    this probably you might have guessed

    already because I think I had written already because I think I had written already
    because I think I had written

    data somewhere. So these magnets which data somewhere. So these magnets which
    data somewhere. So these magnets which

    you see those are the clean data points you see those are the clean data points
    you see those are the clean data points

    and the unknown magnetic field actually and the unknown magnetic field actually
    and the unknown magnetic field actually

    represents the unknown probability represents the unknown probability represents
    the unknown probability

    distribution of this clean data. Okay. So you do not know the unknown Okay. So
    you do not know the unknown

    magnetic field just as you do not know magnetic field just as you do not know
    magnetic field just as you do not know

    this unknown probability distribution. this unknown probability distribution.
    this unknown probability distribution.

    Now you flick the ball right and it goes Now you flick the ball right and it goes
    Now you flick the ball right and it goes

    to a position. The flick represents the to a position. The flick represents the
    to a position. The flick represents the

    noise which is added to the clean data noise which is added to the clean data
    noise which is added to the clean data

    points. points. points.

    Okay. So you add some noise and it goes Okay. So you add some noise and it goes
    Okay. So you add some noise and it goes

    to a new location.'
  concept_slugs:
  - score-matching
  - tweedies-formula
- idx: 23
  start_sec: 1579.99
  end_sec: 1642.24
  text: 'to a new location. to a new location.

    So the noisy new spot is represented as So the noisy new spot is represented as
    So the noisy new spot is represented as

    xhat. xhat. xhat.

    Uh this is I have actually denoted this Uh this is I have actually denoted this
    Uh this is I have actually denoted this

    over here as xhat. So you probably might over here as xhat. So you probably might
    over here as xhat. So you probably might

    have guessed it when you look saw that have guessed it when you look saw that
    have guessed it when you look saw that

    figure. figure. figure.

    And the probability distribution for And the probability distribution for And
    the probability distribution for

    this noisy data is represented as P this noisy data is represented as P this noisy
    data is represented as P

    sigma of Xhat of X tilda. sigma of Xhat of X tilda. sigma of Xhat of X tilda.

    Okay. So uh here sigma represents the Okay. So uh here sigma represents the Okay.
    So uh here sigma represents the

    noise which is added to the data. noise which is added to the data. noise which
    is added to the data.

    Now what does the student represent in Now what does the student represent in
    Now what does the student represent in

    this case? this case? this case?

    The student is trying to learn from the The student is trying to learn from the
    The student is trying to learn from the

    feedback which is given to them. So feedback which is given to them. So feedback
    which is given to them. So

    naturally the student represents some naturally the student represents some naturally
    the student represents some

    kind of a learning model or a neural kind of a learning model or a neural kind
    of a learning model or a neural

    network represents the neural network network represents the neural network network
    represents the neural network

    trying to guess the direction trying to guess the direction trying to guess the
    direction

    back to the magnet. So this is back to the magnet. So this is back to the magnet.
    So this is

    represented as the score. Remember the represented as the score. Remember the
    represented as the score. Remember the

    score does exactly the same thing. The score does exactly the same thing. The'
  concept_slugs:
  - score-matching
  - tweedies-formula
- idx: 24
  start_sec: 1642.24
  end_sec: 1722.87
  text: 'score does exactly the same thing. The

    score tells you the direction score tells you the direction score tells you the
    direction

    to the actual data in the space. And our to the actual data in the space. And
    our to the actual data in the space. And our

    student is trying to understand the same student is trying to understand the same
    student is trying to understand the same

    thing. It''s trying the the student is thing. It''s trying the the student is
    thing. It''s trying the the student is

    trying to guess the direction trying to guess the direction

    uh of the force needed to pull the ball uh of the force needed to pull the ball
    uh of the force needed to pull the ball

    back to its original location back to its original location back to its original
    location

    which is the data point from where we which is the data point from where we which
    is the data point from where we

    started. So this is represented as S5 of started. So this is represented as S5
    of started. So this is represented as S5 of

    X tilda because we are considering the X tilda because we are considering the
    X tilda because we are considering the

    noisy samples right now. noisy samples right now. noisy samples right now.

    And the correct arrow from the original And the correct arrow from the original
    And the correct arrow from the original

    data to the noisy data which is this data to the noisy data which is this data
    to the noisy data which is this

    the flick. This correct arrow denotes the score function for the denotes the score
    function for the

    distribution of the noisy data. It is distribution of the noisy data. It is distribution
    of the noisy data. It is

    denoted as this. So this is what So this is what

    my neural network is trying to learn and my neural network is trying to learn
    and my neural network is trying to learn and

    it''s trying to match this. This is what my student is predicting. This is what
    my student is predicting.

    It''s making the student is making a lot It''s making the student is making a
    lot It''s making the student is making a lot

    of mistakes but the feedback is given'
  concept_slugs:
  - score-matching
  - tweedies-formula
- idx: 25
  start_sec: 1722.87
  end_sec: 1799.11
  text: 'of mistakes but the feedback is given of mistakes but the feedback is given

    from this. This is the true direction from this. This is the true direction from
    this. This is the true direction

    where which the student should try to where which the student should try to where
    which the student should try to

    match as close as possible. And this is given by the score function And this is
    given by the score function

    of x tilda given x. of x tilda given x. of x tilda given x.

    Now here this part becomes very crucial Now here this part becomes very crucial
    Now here this part becomes very crucial

    for us for us for us

    that we are trying to take the logarithm that we are trying to take the logarithm
    that we are trying to take the logarithm

    of the probability of x hat conditioned of the probability of x hat conditioned
    of the probability of x hat conditioned

    on x. So given the clean data on x. So given the clean data on x. So given the
    clean data

    what is the probability of what is the probability of what is the probability
    of

    the noisy data x hat given x the noisy data x hat given x the noisy data x hat
    given x

    probability of that and now your loss function boils down to and now your loss
    function boils down to

    this uh just taking a mean square error this uh just taking a mean square error
    this uh just taking a mean square error

    between these two terms. between these two terms. between these two terms.

    This is the score which you are trying This is the score which you are trying
    This is the score which you are trying

    to predict which your neural network is to predict which your neural network is
    to predict which your neural network is

    trying to predict trying to predict trying to predict

    and this is something which you''re and this is something which you''re and this
    is something which you''re

    trying to match. trying to match. trying to match.

    Now we will see that this is something Now we will see that this is something
    Now we will see that this is something

    which is tractable. which is tractable. which is tractable.

    It is not like your true'
  concept_slugs:
  - score-matching
  - tweedies-formula
- idx: 26
  start_sec: 1799.11
  end_sec: 1860.32
  text: 'It is not like your true It is not like your true

    probability distribution of data which probability distribution of data which
    probability distribution of data which

    is not tractable but it is tractable. is not tractable but it is tractable. is
    not tractable but it is tractable.

    You can actually calculate this term. You can actually calculate this term. You
    can actually calculate this term.

    you can calculate it simply because of you can calculate it simply because of
    you can calculate it simply because of

    this conditioning which happens over this conditioning which happens over this
    conditioning which happens over

    here. So essentially what you have done is So essentially what you have done is

    you are saying that I cannot uh you know you are saying that I cannot uh you know
    you are saying that I cannot uh you know

    find the find the find the

    true score at all possible points. What true score at all possible points. What
    true score at all possible points. What

    I will do is I will deliberately inject I will do is I will deliberately inject
    I will do is I will deliberately inject

    noise noise noise

    in my data so that the samples will move in my data so that the samples will move
    in my data so that the samples will move

    towards a new location and I know towards a new location and I know towards a
    new location and I know

    exactly how I have moved the samples exactly how I have moved the samples exactly
    how I have moved the samples

    from the original location to the new from the original location to the new from
    the original location to the new

    location. I know the noise which I have location. I know the noise which I have
    location. I know the noise which I have

    added. I will try to predict added. I will try to predict added. I will try to
    predict

    the score function for this noisy data. the score function for this noisy data.
    the score function for this noisy data.

    That is I will try to predict at any That is I will try to predict at any That
    is I will try to predict at any

    given any point in space given any point in space'
  concept_slugs:
  - score-matching
  - tweedies-formula
- idx: 27
  start_sec: 1860.32
  end_sec: 1922.95
  text: 'given any point in space

    how can I pull this point so that it how can I pull this point so that it how
    can I pull this point so that it

    becomes as close as possible to your becomes as close as possible to your becomes
    as close as possible to your

    noisy data noisy data noisy data

    which is the predicted score function which is the predicted score function which
    is the predicted score function

    and how you''re predicting it you''re and how you''re predicting it you''re and
    how you''re predicting it you''re

    trying to match it with the score trying to match it with the score trying to
    match it with the score

    function for the new data samples function for the new data samples function for
    the new data samples

    conditioned on the original data conditioned on the original data conditioned
    on the original data

    samples. So this act of deliberately injecting So this act of deliberately injecting

    noise this is very similar to what noise this is very similar to what noise this
    is very similar to what

    people did in diffusion. In fact we saw people did in diffusion. In fact we saw
    people did in diffusion. In fact we saw

    this for the example of Batman. Remember this for the example of Batman. Remember
    this for the example of Batman. Remember

    that was the first example that we took that was the first example that we took
    that was the first example that we took

    in our diffusion class where we slowly in our diffusion class where we slowly
    in our diffusion class where we slowly

    added a lot of noise and then the image added a lot of noise and then the image
    added a lot of noise and then the image

    became uniform. became uniform. became uniform.

    So this deliberate practice of adding So this deliberate practice of adding So
    this deliberate practice of adding

    noise noise

    is something which is is something which is is something which is

    common uh and you might be wondering why common uh and you might be wondering
    why common uh and you might be wondering why

    are we adding noise and how how is it are we adding noise and how how is it are
    we adding noise and how how is it

    really making sense. I have an excellent'
  concept_slugs:
  - score-matching
  - tweedies-formula
- idx: 28
  start_sec: 1922.95
  end_sec: 1985.36
  text: 'really making sense. I have an excellent really making sense. I have an excellent

    explanation to that which will come soon explanation to that which will come soon
    explanation to that which will come soon

    in this lecture where you will get a in this lecture where you will get a in this
    lecture where you will get a

    visual interpretation of what exactly visual interpretation of what exactly visual
    interpretation of what exactly

    happens when you add noise. How do happens when you add noise. How do happens
    when you add noise. How do

    things become suddenly so easy when you things become suddenly so easy when you
    things become suddenly so easy when you

    just add noise? Doesn''t it seem very just add noise? Doesn''t it seem very just
    add noise? Doesn''t it seem very

    trivial to just add noise and trivial to just add noise and trivial to just add
    noise and

    predict the score function for the noisy predict the score function for the noisy
    predict the score function for the noisy

    data instead for the true data? data instead for the true data? data instead for
    the true data?

    So let''s let''s try to dig deeper. So let''s let''s try to dig deeper. So let''s
    let''s try to dig deeper.

    In fact, this conditioning technique In fact, this conditioning technique In fact,
    this conditioning technique

    also appears in the variational view of also appears in the variational view of
    also appears in the variational view of

    the diffusion models in DDPM and it''s the diffusion models in DDPM and it''s
    the diffusion models in DDPM and it''s

    one of the most common tricks that we one of the most common tricks that we one
    of the most common tricks that we

    see in deep generative modeling which see in deep generative modeling which see
    in deep generative modeling which

    suddenly makes everything suddenly makes everything suddenly makes everything

    tractable. Okay. So let us simplify this further to Okay. So let us simplify this
    further to

    get a very simple loss formulation. get a very simple loss formulation. get a
    very simple loss formulation.

    If we assume that the noise is gshian which is it is the flick the which is it
    is the flick the

    perturvation to the data. We can perturvation to the data. We can'
  concept_slugs:
  - ddpm
  - score-matching
  - tweedies-formula
- idx: 29
  start_sec: 1985.36
  end_sec: 2054.869
  text: 'perturvation to the data. We can

    simplify the score function which we simplify the score function which we simplify
    the score function which we

    want to learn as follows. want to learn as follows. want to learn as follows.

    If we add a gshian noise with variance If we add a gshian noise with variance
    If we add a gshian noise with variance

    of sigma squared to each data point then of sigma squared to each data point then
    of sigma squared to each data point then

    we can write the following. we can write the following. we can write the following.

    The noisy data point is equal to the The noisy data point is equal to the The
    noisy data point is equal to the

    clean data point plus the standard deviation times a random the standard deviation
    times a random

    value between 0 and 1. And in fact we had seen the same example And in fact we
    had seen the same example

    to understand this in the diffusion to understand this in the diffusion to understand
    this in the diffusion

    lecture. lecture. lecture.

    Remember we had taken an image of a Remember we had taken an image of a Remember
    we had taken an image of a

    Batman and we had divided that image Batman and we had divided that image Batman
    and we had divided that image

    into a bunch of pixels into a bunch of pixels into a bunch of pixels

    and every pixel had some value. For and every pixel had some value. For and every
    pixel had some value. For

    example, pixel number one had a value of example, pixel number one had a value
    of example, pixel number one had a value of

    0.5. Pixel number two had a value of 0.5 0.5. Pixel number two had a value of
    0.5 0.5. Pixel number two had a value of 0.5

    etc. etc. etc.

    Now what does it mean when you add Now what does it mean when you add Now what
    does it mean when you add

    gshian noise to this image? It means gshian noise to this image? It means gshian
    noise to this image? It means

    that let''s pick this first pixel. that let''s pick this first pixel. that let''s
    pick this first pixel.

    uh the mean of this pixel is centered at'
  concept_slugs:
  - score-matching
  - tweedies-formula
- idx: 30
  start_sec: 2054.869
  end_sec: 2136.8
  text: 'uh the mean of this pixel is centered at uh the mean of this pixel is centered
    at

    0.5 because the value is 0.5 but then you add a small noise with a but then you
    add a small noise with a

    standard deviation of sigma in this case standard deviation of sigma in this case
    standard deviation of sigma in this case

    and you sample from it. and you sample from it. and you sample from it.

    So you will get values which are closer So you will get values which are closer
    So you will get values which are closer

    to 0.5 but not exactly 0.5 to 0.5 but not exactly 0.5 to 0.5 but not exactly 0.5

    and the exact formula of the values you and the exact formula of the values you
    and the exact formula of the values you

    get is written here. So for this case it get is written here. So for this case
    it get is written here. So for this case it

    will become 0.5 + will become 0.5 + will become 0.5 +

    sigma * epsilon. So if your sigma is sigma * epsilon. So if your sigma is sigma
    * epsilon. So if your sigma is

    let''s say.5 let''s say.5 let''s say.5

    +.5 and you can choose a value of the +.5 and you can choose a value of the +.5
    and you can choose a value of the

    random variable between 0 and 1. Let''s random variable between 0 and 1. Let''s
    random variable between 0 and 1. Let''s

    say you pick a value of 2. say you pick a value of 2. say you pick a value of
    2.

    So this becomes then uh how much 01 So this becomes then uh how much 01 So this
    becomes then uh how much 01

    I think 0.1 0.1

    yeah this becomes.1 and.5 +.1 is 6 yeah this becomes.1 and.5 +.1 is 6 yeah this
    becomes.1 and.5 +.1 is 6

    so this is your value of x data so this is your value of x data so this is your
    value of x data

    this is what it means by adding noise to this is what it means by adding noise
    to this is what it means by adding noise to

    your data your data your data

    And uh in fact And uh in fact'
  concept_slugs:
  - score-matching
  - tweedies-formula
- idx: 31
  start_sec: 2136.8
  end_sec: 2215.92
  text: 'And uh in fact

    this can be represented this can be represented this can be represented

    using a standard normal distribution using a standard normal distribution using
    a standard normal distribution

    like this. Now what does this like this. Now what does this like this. Now what
    does this

    distribution mean? Uh Uh

    this is a distribution where the mean is this is a distribution where the mean
    is this is a distribution where the mean is

    given by given by given by

    x and the standard deviation is given by x and the standard deviation is given
    by x and the standard deviation is given by

    sigma. sigma. sigma.

    So this this is derived from a So this this is derived from a So this this is
    derived from a

    from the typical gshian formula which from the typical gshian formula which from
    the typical gshian formula which

    goes like this. Now here x is represented by x tilda Now here x is represented
    by x tilda

    because those are your noisy data because those are your noisy data because those
    are your noisy data

    samples and the mean is derived from the samples and the mean is derived from
    the samples and the mean is derived from the

    clean data samples. Remember you are not clean data samples. Remember you are
    not clean data samples. Remember you are not

    changing the mean here. you''re only changing the mean here. you''re only changing
    the mean here. you''re only

    adding noise to the data. That is you''re adding noise to the data. That is you''re
    adding noise to the data. That is you''re

    only adding only adding only adding

    uh a standard deviation. You are not uh a standard deviation. You are not uh a
    standard deviation. You are not

    changing the mean. So that is why this changing the mean. So that is why this
    changing the mean. So that is why this

    mu becomes x and this x becomes x tilda. Uh now you can see this is why I was
    Uh now you can see this is why I was

    saying that this probability is saying that this probability is saying that this
    probability is

    tractable tractable tractable

    because you can calculate a mathematical because you can calculate a mathematical
    because you can calculate a mathematical

    expression for this probability expression for this probability'
  concept_slugs:
  - score-matching
  - tweedies-formula
- idx: 32
  start_sec: 2215.92
  end_sec: 2276.48
  text: 'expression for this probability

    distribution. distribution. distribution.

    And uh because it is tractable once we And uh because it is tractable once we
    And uh because it is tractable once we

    know the mathematical formula this know the mathematical formula this know the
    mathematical formula this

    actually looks like something like this. actually looks like something like this.
    actually looks like something like this.

    It is centered at x xhat = x and it goes It is centered at x xhat = x and it goes
    It is centered at x xhat = x and it goes

    like this like this like this

    and you can actually verify it. If x i and you can actually verify it. If x i
    and you can actually verify it. If x i

    becomes if xhat becomes very large this becomes if xhat becomes very large this
    becomes if xhat becomes very large this

    becomes very large the exponential becomes very large the exponential becomes
    very large the exponential

    becomes zero. If x hand becomes very becomes zero. If x hand becomes very becomes
    zero. If x hand becomes very

    small small small

    uh or this difference is negative it uh or this difference is negative it uh or
    this difference is negative it

    goes to negative infinity square is goes to negative infinity square is goes to
    negative infinity square is

    positive and again you get zero. So it positive and again you get zero. So it
    positive and again you get zero. So it

    might look a bit intimidating at first might look a bit intimidating at first
    might look a bit intimidating at first

    but it''s simply a gshian curve which is but it''s simply a gshian curve which
    is but it''s simply a gshian curve which is

    centered at x. centered at x. centered at x.

    Now if you take a log of this you take a Now if you take a log of this you take
    a Now if you take a log of this you take a

    log of the first term plus log of the log of the first term plus log of the log
    of the first term plus log of the

    second term. Log of exponential of second term. Log of exponential of second term.
    Log of exponential of

    anything is whatever is there in the anything is whatever is there in the'
  concept_slugs:
  - score-matching
  - tweedies-formula
- idx: 33
  start_sec: 2276.48
  end_sec: 2347.76
  text: 'anything is whatever is there in the

    exponential itself. So you get this at exponential itself. So you get this at
    exponential itself. So you get this at

    the bottom and then when you take the bottom and then when you take the bottom
    and then when you take

    gradient this vanishes because it''s a gradient this vanishes because it''s a
    gradient this vanishes because it''s a

    constant constant constant

    and you take a gradient of this it and you take a gradient of this it and you
    take a gradient of this it

    simply boils down to this. So this is simply boils down to this. So this is simply
    boils down to this. So this is

    the score function that we are trying to the score function that we are trying
    to the score function that we are trying to

    learn learn learn

    and you can try to interpret this. and you can try to interpret this. and you
    can try to interpret this.

    Remember let''s try to understand this Remember let''s try to understand this
    Remember let''s try to understand this

    for for for

    this uh example that we have taken. Okay. So uh

    now here this is x this is x and uh this is xhat. this is x and uh this is xhat.

    So x - xhat is this vector. So this is what the student is trying to So this is
    what the student is trying to

    learn. The student is trying to learn learn. The student is trying to learn learn.
    The student is trying to learn

    if I just give a tiny flick and it lands if I just give a tiny flick and it lands
    if I just give a tiny flick and it lands

    up at a new location. up at a new location. up at a new location.

    I''m trying to learn a vector which pulls I''m trying to learn a vector which
    pulls I''m trying to learn a vector which pulls

    it back exactly to the point where it it back exactly to the point where it it
    back exactly to the point where it

    started. started. started.

    And it''s so intuitive, right? because And it''s so intuitive, right? because
    And it''s so intuitive, right? because

    you you you might have thought why you you you might have thought why'
  concept_slugs:
  - score-matching
  - tweedies-formula
- idx: 34
  start_sec: 2347.76
  end_sec: 2418.56
  text: 'you you you might have thought why

    didn''t I guess it before because it it didn''t I guess it before because it it
    didn''t I guess it before because it it

    should be the vector which points from should be the vector which points from
    should be the vector which points from

    the noisy data to the original data the noisy data to the original data the noisy
    data to the original data

    which the student is trying to learn and which the student is trying to learn
    and which the student is trying to learn and

    you substitute this in the loss function you substitute this in the loss function
    you substitute this in the loss function

    and you get something like this. and you get something like this. and you get
    something like this.

    So this means that you''re simply trying So this means that you''re simply trying
    So this means that you''re simply trying

    to guess the direction of the flick. And if you look at uh And if you look at
    uh

    the DDPM example or if you think back to the DDPM example or if you think back
    to the DDPM example or if you think back to

    the DDPM example, the DDPM example, the DDPM example,

    you might think that we you might think that we you might think that we

    saw something similar towards the end saw something similar towards the end saw
    something similar towards the end

    where our network was simply trying to where our network was simply trying to
    where our network was simply trying to

    predict the amount of noise which was predict the amount of noise which was predict
    the amount of noise which was

    added in the forward pass. We tried to added in the forward pass. We tried to
    added in the forward pass. We tried to

    predict that in the reverse pass. predict that in the reverse pass. predict that
    in the reverse pass.

    And here also it it turns out that And here also it it turns out that And here
    also it it turns out that

    uh our score is that we are trying to uh our score is that we are trying to uh
    our score is that we are trying to

    predict we are trying to match the noise predict we are trying to match the noise'
  concept_slugs:
  - ddpm
  - score-matching
  - tweedies-formula
- idx: 35
  start_sec: 2418.56
  end_sec: 2482.48
  text: 'predict we are trying to match the noise

    the noise vector which has been added in the noise vector which has been added
    in the noise vector which has been added in

    the to the clean data. the to the clean data. the to the clean data.

    Okay. So let''s take a practical example Okay. So let''s take a practical example
    Okay. So let''s take a practical example

    to to to

    understand understand understand

    how this is implemented how this is implemented how this is implemented

    in practice and in in we will see this in practice and in in we will see this
    in practice and in in we will see this

    formula being used in practice and see formula being used in practice and see
    formula being used in practice and see

    how it works. how it works. how it works.

    What is the objective of this formula? What is the objective of this formula?
    What is the objective of this formula?

    The objective is simply to learn the The objective is simply to learn the The
    objective is simply to learn the

    score function at all the points score function at all the points score function
    at all the points

    just from the data itself. We already just from the data itself. We already just
    from the data itself. We already

    have one formulation we which can do have one formulation we which can do have
    one formulation we which can do

    that but it the computational complexity that but it the computational complexity
    that but it the computational complexity

    of that increases as the square square of that increases as the square square
    of that increases as the square square

    of the dimension. So it''s not very of the dimension. So it''s not very of the
    dimension. So it''s not very

    feasible. So we will take another feasible. So we will take another feasible.
    So we will take another

    example example example

    which is which which looks like this. So which is which which looks like this.
    So which is which which looks like this. So

    there are two peaks in the data as you there are two peaks in the data as you
    there are two peaks in the data as you

    can see can see can see

    which means that the density is maximum which means that the density is maximum'
  concept_slugs:
  - score-matching
  - tweedies-formula
- idx: 36
  start_sec: 2482.48
  end_sec: 2574.069
  text: 'which means that the density is maximum

    near somewhere around this maybe minus4 near somewhere around this maybe minus4
    near somewhere around this maybe minus4

    and the density is maximum somewhere and the density is maximum somewhere and
    the density is maximum somewhere

    around here maybe that represents +4. around here maybe that represents +4. around
    here maybe that represents +4.

    So this is the true distribution So this is the true distribution So this is the
    true distribution

    uh that is given to us and we want to uh that is given to us and we want to uh
    that is given to us and we want to

    predict the score function at every predict the score function at every predict
    the score function at every

    point. Let''s try to look at the Google Collab Let''s try to look at the Google
    Collab

    notebook which will help us understand notebook which will help us understand
    notebook which will help us understand

    this in detail. Okay. So Okay. So

    uh this is the real data uh this is the real data uh this is the real data

    that we are taking as an example. that we are taking as an example. that we are
    taking as an example.

    We have already looked at that. And then um after this we define the And then
    um after this we define the

    student which is the neural network. student which is the neural network. student
    which is the neural network.

    Remember the student is the Remember the student is the Remember the student is
    the

    neural network which is trying to guess neural network which is trying to guess
    neural network which is trying to guess

    the flick how much flick you have added the flick how much flick you have added
    the flick how much flick you have added

    or in other words the student is trying or in other words the student is trying
    or in other words the student is trying

    to guess the noise vector to guess the noise vector to guess the noise vector

    and here we define the student as a and here we define the student as a and here
    we define the student as a

    neural network with neural network with neural network with

    three layers first layer second layer three layers first layer second layer three
    layers first layer second layer

    and third layer.'
  concept_slugs:
  - score-matching
  - tweedies-formula
- idx: 37
  start_sec: 2575.91
  end_sec: 2631.76
  text: 'So this is the neural network that we So this is the neural network that
    we

    define and the loss function is the main define and the loss function is the main
    define and the loss function is the main

    step which I want to explain to step which I want to explain to step which I want
    to explain to

    everyone. everyone. everyone.

    Okay. So have a look at the loss Okay. So have a look at the loss Okay. So have
    a look at the loss

    function. It looks like this half into function. It looks like this half into
    function. It looks like this half into

    predicted score minus target score whole predicted score minus target score whole
    predicted score minus target score whole

    square. square. square.

    And uh here the predicted score is And uh here the predicted score is And uh here
    the predicted score is

    simply simply simply

    the model and you pass the noisy data to the model and you pass the noisy data
    to the model and you pass the noisy data to

    the model. This is what you see here. the model. This is what you see here. the
    model. This is what you see here.

    S5 of X tilda which is the noisy data S5 of X tilda which is the noisy data S5
    of X tilda which is the noisy data

    being passed to the model. How is the being passed to the model. How is the being
    passed to the model. How is the

    noisy data calculated? You take clean noisy data calculated? You take clean noisy
    data calculated? You take clean

    data and you add the noise into sigma data and you add the noise into sigma data
    and you add the noise into sigma

    term to the clean data. So you get the term to the clean data. So you get the
    term to the clean data. So you get the

    noisy data and you pass it to the model. noisy data and you pass it to the model.
    noisy data and you pass it to the model.

    You get the predicted score at the end You get the predicted score at the end
    You get the predicted score at the end

    of it. Okay. And now what is the target score?'
  concept_slugs:
  - score-matching
  - tweedies-formula
- idx: 38
  start_sec: 2631.76
  end_sec: 2699.349
  text: 'Okay. And now what is the target score?

    The target score is something which The target score is something which The target
    score is something which

    you''re trying to estimate which is minus you''re trying to estimate which is
    minus you''re trying to estimate which is minus

    of x - x tilda by sigma square. of x - x tilda by sigma square. of x - x tilda
    by sigma square.

    So here you simply see here minus of x - So here you simply see here minus of
    x - So here you simply see here minus of x -

    x by sigma square is given here x by sigma square is given here x by sigma square
    is given here

    which simplifies to minus noise * sigma. which simplifies to minus noise * sigma.
    which simplifies to minus noise * sigma.

    Why is that the case? Why is that the case? Why is that the case?

    Let''s see. So x - x tilda Let''s see. So x - x tilda Let''s see. So x - x tilda

    equal to minus equal to minus equal to minus

    if you look at this x - x tilda is equal to minus sigma * x - x tilda is equal
    to minus sigma *

    epsilon and you divide that by sigma epsilon and you divide that by sigma epsilon
    and you divide that by sigma

    square. So sigma sigma cancel. So you square. So sigma sigma cancel. So you square.
    So sigma sigma cancel. So you

    get minus epsilon by sigma which is get minus epsilon by sigma which is get minus
    epsilon by sigma which is

    exactly what they have written here exactly what they have written here exactly
    what they have written here

    where epsilon is replaced by noise where epsilon is replaced by noise where epsilon
    is replaced by noise

    and uh and uh and uh

    yeah then then you substitute this here yeah then then you substitute this here
    yeah then then you substitute this here

    you implement this and you run a you implement this and you run a you implement
    this and you run a

    training loop. I have ran it for training loop. I have ran it for training loop.
    I have ran it for

    8,800 steps. 8,800 steps. 8,800 steps.

    And uh finally you see the learned score'
  concept_slugs:
  - score-matching
  - tweedies-formula
- idx: 39
  start_sec: 2699.349
  end_sec: 2756.63
  text: 'And uh finally you see the learned score And uh finally you see the learned
    score

    function which looks something like function which looks something like function
    which looks something like

    this. Now this might seem a little bit this. Now this might seem a little bit
    this. Now this might seem a little bit

    odd to begin with but it does make odd to begin with but it does make odd to begin
    with but it does make

    sense. Let''s let''s look at a point which sense. Let''s let''s look at a point
    which sense. Let''s let''s look at a point which

    is is is

    uh uh

    so basically we see something like this so basically we see something like this
    so basically we see something like this

    right okay this is not very clear anyways I''ll okay this is not very clear anyways
    I''ll

    explain using this. Let''s let''s look at explain using this. Let''s let''s look
    at explain using this. Let''s let''s look at

    the point which which which is here the point which which which is here the point
    which which which is here

    where my cursor is. Now the score is where my cursor is. Now the score is where
    my cursor is. Now the score is

    positive which means that you are going positive which means that you are going
    positive which means that you are going

    to be pulled in the right direction to be pulled in the right direction to be
    pulled in the right direction

    towards this purple block which is the towards this purple block which is the
    towards this purple block which is the

    magnet one region that is exactly you magnet one region that is exactly you magnet
    one region that is exactly you

    want and the direction is positive until want and the direction is positive until
    want and the direction is positive until

    you reach this point. you reach this point. you reach this point.

    Why does it decrease? because as you Why does it decrease? because as you Why
    does it decrease? because as you

    move closer to the magnet, you will need move closer to the magnet, you will need
    move closer to the magnet, you will need

    less force to move it towards the less force to move it towards the less force
    to move it towards the

    magnet.'
  concept_slugs:
  - score-matching
  - tweedies-formula
- idx: 40
  start_sec: 2756.63
  end_sec: 2802.72
  text: 'magnet. magnet.

    Similarly, if you are somewhere on the Similarly, if you are somewhere on the
    Similarly, if you are somewhere on the

    right, uh the score is negative because right, uh the score is negative because
    right, uh the score is negative because

    you need to be pulled in the negative you need to be pulled in the negative you
    need to be pulled in the negative

    direction to reach towards magnet number direction to reach towards magnet number
    direction to reach towards magnet number

    two. And here also the magnitude two. And here also the magnitude two. And here
    also the magnitude

    decreases as you move closer to the decreases as you move closer to the decreases
    as you move closer to the

    magnet. magnet.

    Look at these regions in between the Look at these regions in between the Look
    at these regions in between the

    magnet. Here if you see at the top magnet. Here if you see at the top magnet.
    Here if you see at the top

    uh it''s positive because you want to uh it''s positive because you want to uh
    it''s positive because you want to

    move to the right. Similarly if you are move to the right. Similarly if you are
    move to the right. Similarly if you are

    at the bottom you want to move to the at the bottom you want to move to the at
    the bottom you want to move to the

    left. Let me see if I''ve got any plot left. Let me see if I''ve got any plot
    left. Let me see if I''ve got any plot

    for the arrows. Yeah this is exactly for the arrows. Yeah this is exactly for
    the arrows. Yeah this is exactly

    what I wanted to explain. So what I wanted to explain. So what I wanted to explain.
    So

    wherever you are the score pulls you wherever you are the score pulls you wherever
    you are the score pulls you

    towards the magnet which is closest to towards the magnet which is closest to
    towards the magnet which is closest to

    that point. So if you are on the far that point. So if you are on the far that
    point. So if you are on the far

    left you reach magnet number one. If you left you reach magnet number one. If
    you'
  concept_slugs:
  - score-matching
  - tweedies-formula
- idx: 41
  start_sec: 2802.72
  end_sec: 2852.47
  text: 'left you reach magnet number one. If you

    are on the far right, you reach magnet are on the far right, you reach magnet
    are on the far right, you reach magnet

    number two. And if you are anywhere in number two. And if you are anywhere in
    number two. And if you are anywhere in

    between, you reach whichever magnet you between, you reach whichever magnet you
    between, you reach whichever magnet you

    are closer to. And that''s exactly what are closer to. And that''s exactly what
    are closer to. And that''s exactly what

    this learned score does. this learned score does. this learned score does.

    So you see this loss function is so So you see this loss function is so So you
    see this loss function is so

    simple, right? I I find this very simple simple, right? I I find this very simple
    simple, right? I I find this very simple

    compared to compared to compared to

    uh the previous loss function that we uh the previous loss function that we uh
    the previous loss function that we

    saw where we had a trace term and we had saw where we had a trace term and we
    had saw where we had a trace term and we had

    a square of the magnitude term. a square of the magnitude term. a square of the
    magnitude term.

    that is also interpretable but it''s a that is also interpretable but it''s a
    that is also interpretable but it''s a

    bit tricky to interpret that bit tricky to interpret that bit tricky to interpret
    that

    compared to this which is fairly compared to this which is fairly compared to
    this which is fairly

    straightforward to interpret and does straightforward to interpret and does straightforward
    to interpret and does

    make a lot of sense. make a lot of sense. make a lot of sense.

    So to summarize what we have looked at So to summarize what we have looked at
    So to summarize what we have looked at

    here is uh we have looked at score here is uh we have looked at score here is
    uh we have looked at score

    matching from the lens of dnoising. matching from the lens of dnoising. matching
    from the lens of dnoising.

    We first add a noise and then we try to'
  concept_slugs:
  - score-matching
  - tweedies-formula
- idx: 42
  start_sec: 2852.47
  end_sec: 2914.64
  text: 'We first add a noise and then we try to We first add a noise and then we
    try to

    predict that noise. predict that noise. predict that noise.

    And in that process of predicting the And in that process of predicting the And
    in that process of predicting the

    noise vector, noise vector, noise vector,

    in that process of learning the noise in that process of learning the noise in
    that process of learning the noise

    vector, vector, vector,

    we are learning the score function we are learning the score function we are learning
    the score function

    itself itself itself

    which is a bit non-intuitive but you see which is a bit non-intuitive but you
    see which is a bit non-intuitive but you see

    that from the formulation that that is that from the formulation that that is
    that from the formulation that that is

    exactly what is happening. Let''s look at why adding noise makes so Let''s look
    at why adding noise makes so

    much of a difference. We will we will much of a difference. We will we will much
    of a difference. We will we will

    come to that eventually. come to that eventually. come to that eventually.

    Uh but just a short brief about Uh but just a short brief about Uh but just a
    short brief about

    once you predict the score function. We once you predict the score function. We
    once you predict the score function. We

    have already discussed this in the last have already discussed this in the last
    have already discussed this in the last

    lecture that our objective is to then lecture that our objective is to then lecture
    that our objective is to then

    sample from the score using languin sample from the score using languin sample
    from the score using languin

    dynamics dynamics dynamics

    and that is something which we can do and that is something which we can do and
    that is something which we can do

    using this formula. This is the score function and this is This is the score function
    and this is

    the noise term which we add to perturb the noise term which we add to perturb
    the noise term which we add to perturb

    us away from the local minima so that we us away from the local minima so that
    we'
  concept_slugs:
  - score-matching
  - tweedies-formula
- idx: 43
  start_sec: 2914.64
  end_sec: 2975.75
  text: 'us away from the local minima so that we

    explore the global minimas as well. explore the global minimas as well. explore
    the global minimas as well.

    So uh this is what we get So uh this is what we get So uh this is what we get

    once we use lang dynamics and we sample once we use lang dynamics and we sample
    once we use lang dynamics and we sample

    from from from

    the score function. So it does the score function. So it does the score function.
    So it does

    approximate these peaks. You can see the approximate these peaks. You can see
    the approximate these peaks. You can see the

    generated samples generated samples generated samples

    does approximate the real data which is does approximate the real data which is
    does approximate the real data which is

    what is the main overarching goal of what is the main overarching goal of what
    is the main overarching goal of

    deep generative modeling. We want our deep generative modeling. We want our deep
    generative modeling. We want our

    samples to match the distribution of our samples to match the distribution of
    our samples to match the distribution of our

    samples predicted samples to match the samples predicted samples to match the
    samples predicted samples to match the

    true distribution as close as possible true distribution as close as possible
    true distribution as close as possible

    which is exactly what we are trying to which is exactly what we are trying to
    which is exactly what we are trying to

    do in in this case. do in in this case. do in in this case.

    Okay. So an intuition about adding noise Okay. So an intuition about adding noise
    Okay. So an intuition about adding noise

    is pending which I will explain in the is pending which I will explain in the
    is pending which I will explain in the

    next part which is noise conditioned next part which is noise conditioned next
    part which is noise conditioned

    score networks. score networks. score networks.

    So you''ll get a very clear idea with So you''ll get a very clear idea with So
    you''ll get a very clear idea with

    respect to why does adding noise make so respect to why does adding noise make
    so respect to why does adding noise make so

    much of a difference. Something might be'
  concept_slugs:
  - score-matching
  - tweedies-formula
- idx: 44
  start_sec: 2975.75
  end_sec: 3026.079
  text: 'much of a difference. Something might be much of a difference. Something
    might be

    happening in the 3D space right that happening in the 3D space right that happening
    in the 3D space right that

    adding noise suddenly makes things a lot adding noise suddenly makes things a
    lot adding noise suddenly makes things a lot

    easier. So we will look at that exactly easier. So we will look at that exactly
    easier. So we will look at that exactly

    what is the purpose of adding noise and what is the purpose of adding noise and
    what is the purpose of adding noise and

    uh why does it make a lot of difference uh why does it make a lot of difference
    uh why does it make a lot of difference

    but for now we have looked at two but for now we have looked at two but for now
    we have looked at two

    alternative ways of doing score alternative ways of doing score alternative ways
    of doing score

    matching. The first method was using matching. The first method was using matching.
    The first method was using

    this formulation which this formulation which this formulation which

    worked for us in this example but the worked for us in this example but the worked
    for us in this example but the

    complexity increased as the square of complexity increased as the square of complexity
    increased as the square of

    the dimension. So it was not very the dimension. So it was not very the dimension.
    So it was not very

    practical. And uh the second one was practical. And uh the second one was practical.
    And uh the second one was

    this where the loss formulation was very this where the loss formulation was very
    this where the loss formulation was very

    simple where we are trying to just match simple where we are trying to just match
    simple where we are trying to just match

    the learned score with the noise vector the learned score with the noise vector
    the learned score with the noise vector

    which has been added to the data. which has been added to the data. which has
    been added to the data.

    Okay. So this is it for dnoising score Okay. So this is it for dnoising score'
  concept_slugs:
  - score-matching
  - tweedies-formula
- idx: 45
  start_sec: 3026.079
  end_sec: 3037.48
  text: 'Okay. So this is it for dnoising score

    matching and uh in the next part matching and uh in the next part matching and
    uh in the next part

    uh I will explain about noise condition uh I will explain about noise condition
    uh I will explain about noise condition

    score networks.'
  concept_slugs:
  - score-matching
  - tweedies-formula
---
# Lecture 6 - Denoising Score Matching | Principles of Diffusion Models

See the structured chunks above.
