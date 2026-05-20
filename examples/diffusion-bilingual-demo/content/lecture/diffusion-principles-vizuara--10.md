---
course_slug: diffusion-principles-vizuara
idx: 10
title: Lecture 1 - Deep Generative Modeling | Principles of Diffusion Models
video_url: https://www.youtube.com/watch?v=bVrweqE-r38
duration_sec: null
chunks:
- idx: 0
  start_sec: 3.75
  end_sec: 100.159
  text: 'Hello everyone and welcome to the first Hello everyone and welcome to the
    first

    lecture of the course principles of lecture of the course principles of lecture
    of the course principles of

    diffusion models. diffusion models. diffusion models.

    Let me start by sharing my screen. Okay. So the first lecture is titled Okay.
    So the first lecture is titled

    deep generative modeling. deep generative modeling. deep generative modeling.

    Let us try to understand what this means Let us try to understand what this means
    Let us try to understand what this means

    in detail. in detail. in detail.

    Imagine that uh you have thousand students thousand students

    in your school. in your school. in your school.

    Imagine that it''s a pretty big school Imagine that it''s a pretty big school
    Imagine that it''s a pretty big school

    and there are a huge number of students and there are a huge number of students
    and there are a huge number of students

    and the students have a different and the students have a different and the students
    have a different

    variations in their height. Some variations in their height. Some variations in
    their height. Some

    students are very tall, some are short students are very tall, some are short
    students are very tall, some are short

    and uh there is a general distribution and uh there is a general distribution
    and uh there is a general distribution

    in the heights of all the students. in the heights of all the students. in the
    heights of all the students.

    Now Now Now

    the main uh the main uh the main uh

    premise of today''s lecture is that premise of today''s lecture is that premise
    of today''s lecture is that

    we have samples of the heights of all we have samples of the heights of all we
    have samples of the heights of all

    these students but we do not know the these students but we do not know the these
    students but we do not know the

    true distribution of all the students true distribution of all the students true
    distribution of all the students

    heights. heights. heights.

    So you just have a few measurements of So you just have a few measurements of
    So you just have a few measurements of

    the heights of maybe a few friends of the heights of maybe a few friends of'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
- idx: 1
  start_sec: 100.159
  end_sec: 167.99
  text: 'the heights of maybe a few friends of

    yours and uh you have noted them down in yours and uh you have noted them down
    in yours and uh you have noted them down in

    your diary. your diary. your diary.

    So out of thousand students let''s say So out of thousand students let''s say
    So out of thousand students let''s say

    you have taken or collected a few you have taken or collected a few you have taken
    or collected a few

    samples maybe 50 or 60 students let''s samples maybe 50 or 60 students let''s
    samples maybe 50 or 60 students let''s

    say for example. say for example. say for example.

    Now considering this premise the main Now considering this premise the main Now
    considering this premise the main

    question that we are trying to answer in question that we are trying to answer
    in question that we are trying to answer in

    uh uh uh

    this whole series is that let''s say if a this whole series is that let''s say
    if a this whole series is that let''s say if a

    new student new student new student

    joins your school tomorrow joins your school tomorrow joins your school tomorrow

    and uh your friend tells you that hey and uh your friend tells you that hey and
    uh your friend tells you that hey

    there is a new person who is going to there is a new person who is going to there
    is a new person who is going to

    join the school uh tomorrow. join the school uh tomorrow. join the school uh tomorrow.

    Now your task is to generate a realistic Now your task is to generate a realistic
    Now your task is to generate a realistic

    height for this new student who is going height for this new student who is going
    height for this new student who is going

    to join your school. to join your school. to join your school.

    How will you do that? How will you do that? How will you do that?

    You have a few samples which are You have a few samples which are You have a few
    samples which are

    measurements of 50 to 60 students in measurements of 50 to 60 students in measurements
    of 50 to 60 students in

    your school and uh you want to make a'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
- idx: 2
  start_sec: 167.99
  end_sec: 230.799
  text: 'your school and uh you want to make a your school and uh you want to make
    a

    guess a reasonable guess about what guess a reasonable guess about what guess
    a reasonable guess about what

    would be the height of this new student would be the height of this new student
    would be the height of this new student

    who is going to join your school. who is going to join your school. who is going
    to join your school.

    Is it 4T 9 in 5t 5 in 6 ft etc. It can Is it 4T 9 in 5t 5 in 6 ft etc. It can
    Is it 4T 9 in 5t 5 in 6 ft etc. It can

    be any one of these. be any one of these. be any one of these.

    Now the height of the new student will Now the height of the new student will
    Now the height of the new student will

    definitely depend on definitely depend on definitely depend on

    the distribution of the sample data. For the distribution of the sample data.
    For the distribution of the sample data. For

    example, example, example,

    if you have collected uh student heights if you have collected uh student heights
    if you have collected uh student heights

    for students who are less than 10 years for students who are less than 10 years
    for students who are less than 10 years

    old, old, old,

    then your prediction will be that the then your prediction will be that the then
    your prediction will be that the

    new student has a height of maybe around new student has a height of maybe around
    new student has a height of maybe around

    4 to 5 ft. 4 to 5 ft. 4 to 5 ft.

    But if you have collected stu uh data But if you have collected stu uh data But
    if you have collected stu uh data

    for students who are above 15 years old, for students who are above 15 years old,
    for students who are above 15 years old,

    then your samples will have higher then your samples will have higher then your
    samples will have higher

    heights. So naturally your prediction heights. So naturally your prediction heights.
    So naturally your prediction

    will be that I think the new student will be that I think the new student'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
- idx: 3
  start_sec: 230.799
  end_sec: 315.12
  text: 'will be that I think the new student

    will have uh you know a height of maybe will have uh you know a height of maybe
    will have uh you know a height of maybe

    5'' 5 in. 5'' 5 in. 5'' 5 in.

    So your prediction is dependent on the So your prediction is dependent on the
    So your prediction is dependent on the

    sample data that sample data that sample data that

    you have collected. you have collected. you have collected.

    Okay. So now as we discussed in the Okay. So now as we discussed in the Okay.
    So now as we discussed in the

    premise we do not know the true premise we do not know the true premise we do
    not know the true

    distribution of the heights of the distribution of the heights of the distribution
    of the heights of the

    student but let''s say let''s say that student but let''s say let''s say that
    student but let''s say let''s say that

    someone gives us the true distribution. someone gives us the true distribution.
    someone gives us the true distribution.

    Let''s say the true distribution looks Let''s say the true distribution looks
    Let''s say the true distribution looks

    like follows. This is the true distribution. This is the true distribution.

    Uh Uh Uh

    so this is the distribution which so this is the distribution which so this is
    the distribution which

    will help us to you know understand will help us to you know understand will help
    us to you know understand

    the true distribution of student heights the true distribution of student heights
    the true distribution of student heights

    in the school. For example, just by in the school. For example, just by in the
    school. For example, just by

    looking at this, I can see that looking at this, I can see that looking at this,
    I can see that

    students between 160 to 170 cm are more students between 160 to 170 cm are more
    students between 160 to 170 cm are more

    in in the school and heights which are in in the school and heights which are
    in in the school and heights which are

    less than 140 and greater than 170 cm less than 140 and greater than 170 cm less
    than 140 and greater than 170 cm

    are very less to be seen. are very less to be seen.'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
- idx: 4
  start_sec: 315.12
  end_sec: 389.84
  text: 'are very less to be seen.

    Now if we have this distribution with Now if we have this distribution with Now
    if we have this distribution with

    us, we can easily say that us, we can easily say that us, we can easily say that

    look the main uh the the most probable look the main uh the the most probable
    look the main uh the the most probable

    height of the new student who is going height of the new student who is going
    height of the new student who is going

    to join is maybe somewhere around 150 to to join is maybe somewhere around 150
    to to join is maybe somewhere around 150 to

    170 cm. 170 cm. 170 cm.

    But the challenge is that we do not know But the challenge is that we do not know
    But the challenge is that we do not know

    the true distribution. We only have a the true distribution. We only have a the
    true distribution. We only have a

    few samples. few samples. few samples.

    Now this is exactly what a deep Now this is exactly what a deep Now this is exactly
    what a deep

    generative model generative model generative model

    tries to learn using a few samples. tries to learn using a few samples. tries
    to learn using a few samples.

    The deep generative model tries to The deep generative model tries to The deep
    generative model tries to

    predict the best guess for the height of predict the best guess for the height
    of predict the best guess for the height of

    the new student who is just about to the new student who is just about to the
    new student who is just about to

    join the school. join the school. join the school.

    For example, let''s say our model For example, let''s say our model For example,
    let''s say our model

    predicts the true distribution like predicts the true distribution like predicts
    the true distribution like

    this. this. this.

    So uh the green dotted line is the So uh the green dotted line is the So uh the
    green dotted line is the

    distribution which is distribution which is distribution which is

    predicted by our model and the blue predicted by our model and the blue predicted
    by our model and the blue

    curve is the true distribution. curve is the true distribution.'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
- idx: 5
  start_sec: 389.84
  end_sec: 444.319
  text: 'curve is the true distribution.

    So this is an example of a decent match. So this is an example of a decent match.
    So this is an example of a decent match.

    I can see that the model distribution I can see that the model distribution I
    can see that the model distribution

    very closely matches with the true very closely matches with the true very closely
    matches with the true

    distribution. distribution. distribution.

    So if I sample a new height from this So if I sample a new height from this So
    if I sample a new height from this

    model distribution, model distribution, model distribution,

    I can safely say that it''s going to be a I can safely say that it''s going to
    be a I can safely say that it''s going to be a

    good estimate. But let''s say if our good estimate. But let''s say if our good
    estimate. But let''s say if our

    model does a model does a model does a

    very bad job at uh very bad job at uh very bad job at uh

    identifying the two distribution. Let''s identifying the two distribution. Let''s
    identifying the two distribution. Let''s

    say this. This is our model which is say this. This is our model which is say
    this. This is our model which is

    shown in red. shown in red. shown in red.

    Now the first thing I can see from this Now the first thing I can see from this
    Now the first thing I can see from this

    graph is that this red distribution is graph is that this red distribution is
    graph is that this red distribution is

    far away from the blue distribution far away from the blue distribution far away
    from the blue distribution

    which is the true distribution. So there which is the true distribution. So there
    which is the true distribution. So there

    is this gap you can clearly see is this gap you can clearly see is this gap you
    can clearly see

    and if I use this model to predict the and if I use this model to predict the
    and if I use this model to predict the

    height of the new student what I see is height of the new student what I see is'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
- idx: 6
  start_sec: 444.319
  end_sec: 504.879
  text: 'height of the new student what I see is

    that I''ll make a guess that okay fine that I''ll make a guess that okay fine
    that I''ll make a guess that okay fine

    the new student will have a height of the new student will have a height of the
    new student will have a height of

    around 140 cm but that will be quite around 140 cm but that will be quite around
    140 cm but that will be quite

    different from different from different from

    uh the the prediction from the true uh the the prediction from the true uh the
    the prediction from the true

    distribution which is around 160 to 170 distribution which is around 160 to 170
    distribution which is around 160 to 170

    cm. cm. cm.

    So from this graph we can say that if my So from this graph we can say that if
    my So from this graph we can say that if my

    model model model

    is not able to predict the two the true is not able to predict the two the true
    is not able to predict the two the true

    distribution correctly distribution correctly distribution correctly

    I will sample heights which are I will sample heights which are I will sample
    heights which are

    very different from what the true very different from what the true very different
    from what the true

    distribution would sample from. distribution would sample from. distribution would
    sample from.

    So we need to somehow train our model so So we need to somehow train our model
    so So we need to somehow train our model so

    that it learns to matches the it it that it learns to matches the it it that it
    learns to matches the it it

    learns to match the true distribution of learns to match the true distribution
    of learns to match the true distribution of

    the data. the data. the data.

    Now this is one underlying concept which Now this is one underlying concept which
    Now this is one underlying concept which

    you will see me talk about again and you will see me talk about again and you
    will see me talk about again and

    again in this series. again in this series. again in this series.

    Uh true distribution. So true Uh true distribution. So true'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
- idx: 7
  start_sec: 504.879
  end_sec: 574.88
  text: 'Uh true distribution. So true

    distribution is something which is uh in distribution is something which is uh
    in distribution is something which is uh in

    in supervised learning you''re trying to in supervised learning you''re trying
    to in supervised learning you''re trying to

    match the ground truth with match the ground truth with match the ground truth
    with

    the prediction from your model. So true the prediction from your model. So true
    the prediction from your model. So true

    distribution is something like the distribution is something like the distribution
    is something like the

    ground truth. True distribution is what ground truth. True distribution is what
    ground truth. True distribution is what

    we want to predict. But the problem is we want to predict. But the problem is
    we want to predict. But the problem is

    that we do not have enough samples to that we do not have enough samples to that
    we do not have enough samples to

    understand the true distribution. So we understand the true distribution. So we
    understand the true distribution. So we

    have to end up with an approximate and have to end up with an approximate and
    have to end up with an approximate and

    then sample from that approximate. So in mathematical terms this true So in mathematical
    terms this true

    distribution is denoted by P subscript distribution is denoted by P subscript
    distribution is denoted by P subscript

    data of X and the predicted distribution data of X and the predicted distribution
    data of X and the predicted distribution

    is denoted by P subscript PH of X. is denoted by P subscript PH of X. is denoted
    by P subscript PH of X.

    So essentially what we are trying to do So essentially what we are trying to do
    So essentially what we are trying to do

    is that we are trying to match P is that we are trying to match P is that we are
    trying to match P

    subscript 5 of X with P subscript data subscript 5 of X with P subscript data
    subscript 5 of X with P subscript data

    of X. of X. of X.

    This is exactly what deep generative This is exactly what deep generative This
    is exactly what deep generative

    models are trained to do. They are models are trained to do. They are'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
- idx: 8
  start_sec: 574.88
  end_sec: 635.6
  text: 'models are trained to do. They are

    trained so that the predicted trained so that the predicted trained so that the
    predicted

    distribution matches as close as distribution matches as close as distribution
    matches as close as

    possible to the true distribution. possible to the true distribution. possible
    to the true distribution.

    I have taken a simple example of I have taken a simple example of I have taken
    a simple example of

    students heights in uh the first part of students heights in uh the first part
    of students heights in uh the first part of

    this lecture but we will slowly move on this lecture but we will slowly move on
    this lecture but we will slowly move on

    to a more practical example where this to a more practical example where this
    to a more practical example where this

    analogy will be easily transferable. So analogy will be easily transferable. So
    analogy will be easily transferable. So

    if you have understood the key concepts if you have understood the key concepts
    if you have understood the key concepts

    of true distribution, predicted of true distribution, predicted of true distribution,
    predicted

    distribution, what we are trying to do, distribution, what we are trying to do,
    distribution, what we are trying to do,

    then you''ll able then you''ll be able to then you''ll able then you''ll be able
    to then you''ll able then you''ll be able to

    understand the more practical example understand the more practical example understand
    the more practical example

    which is which will follow soon in in which is which will follow soon in in which
    is which will follow soon in in

    this lecture. Okay. So uh let''s have a quick look at a Okay. So uh let''s have
    a quick look at a

    uh at a video which will help us to uh at a video which will help us to uh at
    a video which will help us to

    understand this in a more visual manner. understand this in a more visual manner.
    understand this in a more visual manner.

    Often times I have seen that whenever we Often times I have seen that whenever
    we Often times I have seen that whenever we

    see something visually it stays in our see something visually it stays in our'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
- idx: 9
  start_sec: 635.6
  end_sec: 731.509
  text: 'see something visually it stays in our

    mind much longer than reading a text or mind much longer than reading a text or
    mind much longer than reading a text or

    hearing from someone. So let''s look at hearing from someone. So let''s look at
    hearing from someone. So let''s look at

    this video and then quickly summarize this video and then quickly summarize this
    video and then quickly summarize

    the first section of this lecture. Okay. So I have paused on this part of Okay.
    So I have paused on this part of

    the video. We have seen two curves. The the video. We have seen two curves. The
    the video. We have seen two curves. The

    first curve which is shown in the blue first curve which is shown in the blue
    first curve which is shown in the blue

    is the true distribution of the student is the true distribution of the student
    is the true distribution of the student

    heights and the curve which is shown in heights and the curve which is shown in
    heights and the curve which is shown in

    red is the model distribution. red is the model distribution. red is the model
    distribution.

    So you can see that it is significantly So you can see that it is significantly
    So you can see that it is significantly

    off. We have not trained it properly off. We have not trained it properly off.
    We have not trained it properly

    yet. So badly trained model is far from the So badly trained model is far from
    the

    true distribution. But as the training true distribution. But as the training
    true distribution. But as the training

    proceeds, you can see that the mod model proceeds, you can see that the mod model
    proceeds, you can see that the mod model

    gets better and better gets better and better gets better and better

    and it closely follows the true height and it closely follows the true height
    and it closely follows the true height

    distribution. So deep generative models adjust their So deep generative models
    adjust their

    parameters so that the model parameters so that the model parameters so that the
    model

    distribution moves close to the true distribution moves close to the true distribution
    moves close to the true

    distribution. distribution.

    So visually if you just keep this'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
- idx: 10
  start_sec: 731.509
  end_sec: 817.99
  text: 'So visually if you just keep this So visually if you just keep this

    uh video in mind and uh video in mind and uh video in mind and

    you saw how the initial curve slowly you saw how the initial curve slowly you
    saw how the initial curve slowly

    morphs into the morphs into the morphs into the

    curve which is very close to the true curve which is very close to the true curve
    which is very close to the true

    distribution. So this morphing is distribution. So this morphing is distribution.
    So this morphing is

    something which happens when we train a something which happens when we train
    a something which happens when we train a

    deep generative model. Let me again play deep generative model. Let me again play
    deep generative model. Let me again play

    this video. So you see the morphing it slowly goes So you see the morphing it
    slowly goes

    from a badly trained model to a model from a badly trained model to a model from
    a badly trained model to a model

    which closely follows the true height which closely follows the true height which
    closely follows the true height

    distribution. distribution.

    Okay, let let''s let''s go back to the Okay, let let''s let''s go back to the
    Okay, let let''s let''s go back to the

    notes. Okay. So let''s try to capture what is Okay. So let''s try to capture what
    is

    deep generative model more formally and deep generative model more formally and
    deep generative model more formally and

    something we we''ll look at a definition something we we''ll look at a definition
    something we we''ll look at a definition

    which is not just applicable to student which is not just applicable to student
    which is not just applicable to student

    sites but it is more generally sites but it is more generally sites but it is
    more generally

    applicable to a wide range of practical applicable to a wide range of practical
    applicable to a wide range of practical

    problem sets. some of which I''m pretty problem sets. some of which I''m pretty
    problem sets. some of which I''m pretty

    sure all of you have already seen but sure all of you have already seen but sure
    all of you have already seen but

    probably not thought of it as a case'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
- idx: 11
  start_sec: 817.99
  end_sec: 900.8
  text: 'probably not thought of it as a case probably not thought of it as a case

    study which comes under the domain of study which comes under the domain of study
    which comes under the domain of

    deep generative modeling. deep generative modeling.

    Similar to the example of student Similar to the example of student Similar to
    the example of student

    heights which we saw before. Uh DGMs Uh DGMs

    take as an input a large collection of real world examples which are drawn from
    real world examples which are drawn from

    unknown and uh and and complex unknown and uh and and complex unknown and uh and
    and complex

    data distribution. and they output a data distribution. and they output a data
    distribution. and they output a

    trained neural network that trained neural network that trained neural network
    that

    parameterizes an approximate parameterizes an approximate parameterizes an approximate

    distribution. distribution.

    So what is taken as an input So what is taken as an input So what is taken as
    an input

    is a large collection of real world is a large collection of real world is a large
    collection of real world

    examples examples examples

    just as we sampled the heights of just as we sampled the heights of just as we
    sampled the heights of

    different students. different students. different students.

    Uh the real world examples can be Uh the real world examples can be Uh the real
    world examples can be

    anything. It can be images for example anything. It can be images for example
    anything. It can be images for example

    where we are given as an input a large where we are given as an input a large
    where we are given as an input a large

    collection of images and these images collection of images and these images collection
    of images and these images

    or students heights as we looked at or students heights as we looked at or students
    heights as we looked at

    before they are drawn from a unknown and before they are drawn from a unknown
    and before they are drawn from a unknown and

    a complex distribution. This is the true a complex distribution. This is the true
    a complex distribution. This is the true

    distribution distribution distribution

    and the deep generative model outputs a and the deep generative model outputs
    a'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
- idx: 12
  start_sec: 900.8
  end_sec: 963.279
  text: 'and the deep generative model outputs a

    trained neural network that distribution.

    So there are three main points here. The So there are three main points here.
    The So there are three main points here. The

    first is a large collection of data first is a large collection of data first
    is a large collection of data

    uh which is taken from some real world uh which is taken from some real world
    uh which is taken from some real world

    examples. examples. examples.

    And And And

    the key concept is that this data is the key concept is that this data is the
    key concept is that this data is

    sampled from some true distribution sampled from some true distribution sampled
    from some true distribution

    which we are not aware about which we do which we are not aware about which we
    do which we are not aware about which we do

    not know. So we don''t know what the true not know. So we don''t know what the
    true not know. So we don''t know what the true

    distribution is. All we have in our hand distribution is. All we have in our hand
    distribution is. All we have in our hand

    is the data samples is the data samples is the data samples

    and from these data samples we have to and from these data samples we have to
    and from these data samples we have to

    predict a distribution which matches the predict a distribution which matches
    the predict a distribution which matches the

    true distribution as close as possible. true distribution as close as possible.
    true distribution as close as possible.

    We have seen exactly same in the above We have seen exactly same in the above
    We have seen exactly same in the above

    video where we saw how the video where we saw how the video where we saw how the

    predicted distribution slowly matches predicted distribution slowly matches predicted
    distribution slowly matches

    the two distribution and with time as we the two distribution and with time as
    we the two distribution and with time as we

    train the neural network we get better train the neural network we get better
    train the neural network we get better

    and better. and better. and better.

    So there are two main goals of deep So there are two main goals of deep'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
- idx: 13
  start_sec: 963.279
  end_sec: 1024.559
  text: 'So there are two main goals of deep

    generative modeling. generative modeling. generative modeling.

    The first goal is that we always aim for The first goal is that we always aim
    for The first goal is that we always aim for

    realistic generation and the second goal realistic generation and the second goal
    realistic generation and the second goal

    is that we aim for controllable is that we aim for controllable is that we aim
    for controllable

    generation. generation. generation.

    Let''s think of another example. Let''s think of another example. Let''s think
    of another example.

    Let''s say we are given a bunch of images Let''s say we are given a bunch of images
    Let''s say we are given a bunch of images

    of cats and of cats and of cats and

    we want to find the underlying we want to find the underlying we want to find
    the underlying

    distribution of uh these images. We we distribution of uh these images. We we
    distribution of uh these images. We we

    want to find a distribution which can want to find a distribution which can want
    to find a distribution which can

    generate images of cats for us. generate images of cats for us. generate images
    of cats for us.

    So our goal is to So our goal is to So our goal is to

    predict a distribution which can predict a distribution which can predict a distribution
    which can

    generate images which are quite generate images which are quite generate images
    which are quite

    realistic and which are controllable. So realistic and which are controllable.
    So realistic and which are controllable. So

    I can control the different set of I can control the different set of I can control
    the different set of

    parameters. Let''s say I want images of parameters. Let''s say I want images of
    parameters. Let''s say I want images of

    cats which are uh gray in color. I want cats which are uh gray in color. I want
    cats which are uh gray in color. I want

    cats which are more furry etc. So these cats which are more furry etc. So these
    cats which are more furry etc. So these

    are the two main broad goals of deep are the two main broad goals of deep are
    the two main broad goals of deep

    generative modeling. Realistic generative modeling. Realistic'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
- idx: 14
  start_sec: 1024.559
  end_sec: 1089.52
  text: 'generative modeling. Realistic

    generation and controllable generation. generation and controllable generation.
    generation and controllable generation.

    Now let''s move to the goal of deep Now let''s move to the goal of deep Now let''s
    move to the goal of deep

    generative modeling. So we assume that generative modeling. So we assume that
    generative modeling. So we assume that

    the samples are drawn independently and the samples are drawn independently and
    the samples are drawn independently and

    identically distributed from an identically distributed from an identically distributed
    from an

    underlying complex data distribution underlying complex data distribution underlying
    complex data distribution

    which we are not aware about. which we are not aware about. which we are not aware
    about.

    The primary goal of DGM is to learn a The primary goal of DGM is to learn a The
    primary goal of DGM is to learn a

    probability distribution from a finite probability distribution from a finite
    probability distribution from a finite

    data set and it uses a deep neural data set and it uses a deep neural data set
    and it uses a deep neural

    network to parameterize a model network to parameterize a model network to parameterize
    a model

    distribution where fi represents the distribution where fi represents the distribution
    where fi represents the

    network''s trainable parameters. network''s trainable parameters. network''s trainable
    parameters.

    The training objective is to find the The training objective is to find the The
    training objective is to find the

    optimal parameters five star that optimal parameters five star that optimal parameters
    five star that

    minimizes the difference between the minimizes the difference between the minimizes
    the difference between the

    model distribution which is p5 of x and model distribution which is p5 of x and
    model distribution which is p5 of x and

    the true distribution which is p data of the true distribution which is p data
    of the true distribution which is p data of

    x. x. x.

    So this model is commonly referred to as So this model is commonly referred to
    as So this model is commonly referred to as

    generative model. generative model. generative model.

    So all of us have seen the field uh So all of us have seen the field uh So all
    of us have seen the field uh

    named as generative AI. But where does named as generative AI. But where does'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
- idx: 15
  start_sec: 1089.52
  end_sec: 1150.23
  text: 'named as generative AI. But where does

    the name generative really come from? It the name generative really come from?
    It the name generative really come from? It

    it comes from the development of it comes from the development of it comes from
    the development of

    uh this model distribution which is p5 uh this model distribution which is p5
    uh this model distribution which is p5

    of x which is trained to approximate the of x which is trained to approximate
    the of x which is trained to approximate the

    true data distribution. true data distribution. true data distribution.

    And why is it called generative model? And why is it called generative model?
    And why is it called generative model?

    Once the model is trained, we can sample Once the model is trained, we can sample
    Once the model is trained, we can sample

    from that distribution to from that distribution to from that distribution to

    generate generate generate

    new and new samples new and new samples new and new samples

    which are taken or which lie within the which are taken or which lie within the
    which are taken or which lie within the

    true distribution. true distribution. true distribution.

    So let''s take the example of cats. There So let''s take the example of cats.
    There So let''s take the example of cats. There

    is some distribution of for the cat data is some distribution of for the cat data
    is some distribution of for the cat data

    set which we are not aware about. But we set which we are not aware about. But
    we set which we are not aware about. But we

    are training the deep generative model are training the deep generative model
    are training the deep generative model

    to learn a distribution that closely to learn a distribution that closely to learn
    a distribution that closely

    approximates the distribution that can approximates the distribution that can
    approximates the distribution that can

    generate a wide variety of cats. generate a wide variety of cats. generate a wide
    variety of cats.

    So this learned model is called as a So this learned model is called as a So this
    learned model is called as a

    generative model because we are trying generative model because we are trying
    generative model because we are trying

    to generate new images of cats in this'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
- idx: 16
  start_sec: 1150.23
  end_sec: 1221.919
  text: 'to generate new images of cats in this to generate new images of cats in
    this

    case. Okay. So now let''s formally look at a Okay. So now let''s formally look
    at a

    more complex example more complex example more complex example

    where we extend our example of student where we extend our example of student
    where we extend our example of student

    heights to a slightly more complex heights to a slightly more complex heights
    to a slightly more complex

    example of cats. example of cats. example of cats.

    Let''s say that we are given a bunch of Let''s say that we are given a bunch of
    Let''s say that we are given a bunch of

    cat images which look as follows. cat images which look as follows. cat images
    which look as follows.

    Here uh I have taken 16 images of cats. Here uh I have taken 16 images of cats.
    Here uh I have taken 16 images of cats.

    So these are the data samples which are So these are the data samples which are
    So these are the data samples which are

    given to us. Now if we have understood given to us. Now if we have understood
    given to us. Now if we have understood

    the goal of DGM correctly, the goal of DGM correctly, the goal of DGM correctly,

    our our our

    next step is to find a probability next step is to find a probability next step
    is to find a probability

    distribution distribution

    which matches the true distribution as which matches the true distribution as
    which matches the true distribution as

    close as possible. close as possible. close as possible.

    The problem is that we do not know the The problem is that we do not know the
    The problem is that we do not know the

    true distribution beforehand. true distribution beforehand. true distribution
    beforehand.

    And uh And uh And uh

    looking back at the example of student looking back at the example of student
    looking back at the example of student

    heights, heights, heights,

    a true distribution can be somewhat a true distribution can be somewhat a true
    distribution can be somewhat

    complex and no one gives it to that complex and no one gives it to that complex
    and no one gives it to that

    gives gives that to us beforehand. gives gives that to us beforehand.'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
- idx: 17
  start_sec: 1221.919
  end_sec: 1284.0
  text: 'gives gives that to us beforehand.

    We get a small sneak peek into the true We get a small sneak peek into the true
    We get a small sneak peek into the true

    distribution through the data samples distribution through the data samples distribution
    through the data samples

    that we have collected. But it is our that we have collected. But it is our that
    we have collected. But it is our

    job to look at the data samples and then job to look at the data samples and then
    job to look at the data samples and then

    predict the two distribution. predict the two distribution. predict the two distribution.

    This is illustrated very nicely in this This is illustrated very nicely in this
    This is illustrated very nicely in this

    figure. So this orange contour that you figure. So this orange contour that you
    figure. So this orange contour that you

    see see see

    that is the true distribution from where that is the true distribution from where
    that is the true distribution from where

    we get our data from. So we get these 16 we get our data from. So we get these
    16 we get our data from. So we get these 16

    images from this orange contour. But images from this orange contour. But images
    from this orange contour. But

    this orange contour is not known to us this orange contour is not known to us
    this orange contour is not known to us

    beforehand. beforehand. beforehand.

    and we slowly try to predict a and we slowly try to predict a and we slowly try
    to predict a

    distribution which is shown in this distribution which is shown in this distribution
    which is shown in this

    black color. So this black contour is black color. So this black contour is black
    color. So this black contour is

    trained to match this orange contour as trained to match this orange contour as
    trained to match this orange contour as

    closely as possible. closely as possible. closely as possible.

    So you can see that I''m using the So you can see that I''m using the So you can
    see that I''m using the

    notation or the wording of contour to notation or the wording of contour to notation
    or the wording of contour to

    represent a probability distribution. represent a probability distribution.'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
- idx: 18
  start_sec: 1284.0
  end_sec: 1353.59
  text: 'represent a probability distribution.

    So orange contour is the true So orange contour is the true So orange contour
    is the true

    probability distribution and the black probability distribution and the black
    probability distribution and the black

    contour is the predicted probability contour is the predicted probability contour
    is the predicted probability

    distribution. So we are trying to morph distribution. So we are trying to morph
    distribution. So we are trying to morph

    the black contour into the orange the black contour into the orange the black
    contour into the orange

    contour through the process of training contour through the process of training
    contour through the process of training

    the deep generative model. So you might wonder that okay fine if So you might
    wonder that okay fine if

    even if we train this model to even if we train this model to even if we train
    this model to

    approximate the true data distribution approximate the true data distribution
    approximate the true data distribution

    what is the purpose of all of this why what is the purpose of all of this why
    what is the purpose of all of this why

    do we need to find the underlying data do we need to find the underlying data
    do we need to find the underlying data

    distribution which generates the data distribution which generates the data distribution
    which generates the data

    samples samples samples

    the main reason is that once a proxy for the main reason is that once a proxy
    for the main reason is that once a proxy for

    the data distribution is available we the data distribution is available we the
    data distribution is available we

    can generate an arbitrary number of new can generate an arbitrary number of new
    can generate an arbitrary number of new

    data data points using the sampling data data points using the sampling data data
    points using the sampling

    methods. methods. methods.

    This is exactly what applications like This is exactly what applications like
    This is exactly what applications like

    midjourney and stable diffusion did. midjourney and stable diffusion did. midjourney
    and stable diffusion did.

    Once Once Once

    the data is given, let''s say the data of the data is given, let''s say the data
    of the data is given, let''s say the data of

    cats and dogs is given, cats and dogs is given, cats and dogs is given,

    they developed'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
- idx: 19
  start_sec: 1353.59
  end_sec: 1410.24
  text: 'they developed they developed

    models which are trained to approximate models which are trained to approximate
    models which are trained to approximate

    the true data distribution of cats and the true data distribution of cats and
    the true data distribution of cats and

    dogs. Once that is available, once that dogs. Once that is available, once that
    dogs. Once that is available, once that

    model is trained, we can generate an model is trained, we can generate an model
    is trained, we can generate an

    arbitrary new set of images of cats, arbitrary new set of images of cats, arbitrary
    new set of images of cats,

    dogs, cities, animals, anything. That''s dogs, cities, animals, anything. That''s
    dogs, cities, animals, anything. That''s

    why we had image generation to tools why we had image generation to tools why
    we had image generation to tools

    which were so powerful. which were so powerful. which were so powerful.

    These tools could generate any images These tools could generate any images These
    tools could generate any images

    that we want because they have learned that we want because they have learned
    that we want because they have learned

    the underlying complex distribution the underlying complex distribution the underlying
    complex distribution

    really well. They know what constitutes really well. They know what constitutes
    really well. They know what constitutes

    the features of a cat. How do dogs the features of a cat. How do dogs the features
    of a cat. How do dogs

    exactly look like? We don''t know exactly exactly look like? We don''t know exactly
    exactly look like? We don''t know exactly

    in words what the model is learning but in words what the model is learning but
    in words what the model is learning but

    it''s somehow learning the underlying it''s somehow learning the underlying it''s
    somehow learning the underlying

    data distribution. And I think humans data distribution. And I think humans data
    distribution. And I think humans

    are also doing something like this in are also doing something like this in are
    also doing something like this in

    the in uh in in in a similar way. uh the in uh in in in a similar way. uh the
    in uh in in in a similar way. uh

    whenever we look at a cat in our mind we whenever we look at a cat in our mind
    we'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
- idx: 20
  start_sec: 1410.24
  end_sec: 1476.799
  text: 'whenever we look at a cat in our mind we

    know that this is a cat because we have know that this is a cat because we have
    know that this is a cat because we have

    formed some assumption of the formed some assumption of the formed some assumption
    of the

    distribution distribution

    through which these samples of cats are through which these samples of cats are
    through which these samples of cats are

    generated. generated. generated.

    Now we are using the same technique to Now we are using the same technique to
    Now we are using the same technique to

    train our deep generative model where train our deep generative model where train
    our deep generative model where

    the model is learning the distribution the model is learning the distribution
    the model is learning the distribution

    of cats. We do it instantaneously in our of cats. We do it instantaneously in
    our of cats. We do it instantaneously in our

    brain. But we have to train a model so brain. But we have to train a model so
    brain. But we have to train a model so

    that it learns this distribution slowly that it learns this distribution slowly
    that it learns this distribution slowly

    with time. with time. with time.

    Now the question is how is this this Now the question is how is this this Now
    the question is how is this this

    training done? How are deep generative training done? How are deep generative
    training done? How are deep generative

    models models models

    really trained? really trained? really trained?

    So uh So uh So uh

    the parameters phi are learned by the parameters phi are learned by the parameters
    phi are learned by

    minimizing the discrepancy between p minimizing the discrepancy between p minimizing
    the discrepancy between p

    data and p5. So that is minimizing the data and p5. So that is minimizing the
    data and p5. So that is minimizing the

    discrepancy between this orange contour discrepancy between this orange contour
    discrepancy between this orange contour

    and this black contour. and this black contour. and this black contour.

    Now Now

    the natural question which comes to mind the natural question which comes to mind
    the natural question which comes to mind

    is is is

    if we take two numbers I can clearly see if we take two numbers I can clearly
    see'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
- idx: 21
  start_sec: 1476.799
  end_sec: 1538.64
  text: 'if we take two numbers I can clearly see

    that the the discrepancy is the that the the discrepancy is the that the the discrepancy
    is the

    difference between the two numbers. difference between the two numbers. difference
    between the two numbers.

    But if I have two probability But if I have two probability But if I have two
    probability

    distributions distributions distributions

    how do I quantify the discrepancy how do I quantify the discrepancy how do I quantify
    the discrepancy

    between these two probability between these two probability between these two
    probability

    distributions? distributions? distributions?

    How do we know whether our probability How do we know whether our probability
    How do we know whether our probability

    distribution is closer to the two distribution is closer to the two distribution
    is closer to the two

    distribution or not? distribution or not? distribution or not?

    So this is done using a measure which is So this is done using a measure which
    is So this is done using a measure which is

    called as K divergence. called as K divergence. called as K divergence.

    We will have a look at a video now which We will have a look at a video now which
    We will have a look at a video now which

    helps us understand helps us understand helps us understand

    the the the

    fundamental concept behind KL fundamental concept behind KL fundamental concept
    behind KL

    divergence. At a broad level, KL divergence. At a broad level, KL divergence.
    At a broad level, KL

    divergence is a metric which helps us to divergence is a metric which helps us
    to divergence is a metric which helps us to

    quantify quantify quantify

    the difference between two probability the difference between two probability
    the difference between two probability

    distributions. Let''s have a look at this distributions. Let''s have a look at
    this distributions. Let''s have a look at this

    video and understand about KL divergence video and understand about KL divergence
    video and understand about KL divergence

    in detail. in detail.

    I want all of you to pay very close I want all of you to pay very close I want
    all of you to pay very close

    attention to what''s happening on the attention to what''s happening on the attention
    to what''s happening on the

    screen. I''m initially going to just run screen. I''m initially going to just
    run'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
- idx: 22
  start_sec: 1538.64
  end_sec: 1690.08
  text: 'screen. I''m initially going to just run

    this video and then um I''m going to this video and then um I''m going to this
    video and then um I''m going to

    explain different parts of it. Okay. So let''s try to unpack this. Okay. So let''s
    try to unpack this.

    Let''s say we have two distributions P Let''s say we have two distributions P
    Let''s say we have two distributions P

    and Q. P is the distribution which is and Q. P is the distribution which is and
    Q. P is the distribution which is

    shown in blue and shown in blue and shown in blue and

    we have another distribution Q which is we have another distribution Q which is
    we have another distribution Q which is

    shown in orange shown in orange shown in orange

    which is the distribution predicted by which is the distribution predicted by
    which is the distribution predicted by

    our model. our model. our model.

    So we can see that there is some So we can see that there is some So we can see
    that there is some

    difference between these two difference between these two difference between these
    two

    distributions. distributions. distributions.

    Clearly the heights of the bars are Clearly the heights of the bars are Clearly
    the heights of the bars are

    different for A, B and C. Now we want a different for A, B and C. Now we want
    a different for A, B and C. Now we want a

    way to quantify way to quantify way to quantify

    what this difference looks like. what this difference looks like. what this difference
    looks like.

    Okay. So let''s see the first approach Okay. So let''s see the first approach
    Okay. So let''s see the first approach

    which comes to our mind is why don''t we which comes to our mind is why don''t
    we which comes to our mind is why don''t we

    just take the difference? just take the difference? just take the difference?

    We take the absolute difference between We take the absolute difference between
    We take the absolute difference between

    these two and we just add them all up. The the main issue is that absolute The
    the main issue is that absolute

    difference is a great start but it difference is a great start but it'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
- idx: 23
  start_sec: 1690.08
  end_sec: 1753.84
  text: 'difference is a great start but it

    doesn''t capture everything. doesn''t capture everything. doesn''t capture everything.

    For example, if we take the absolute For example, if we take the absolute For
    example, if we take the absolute

    difference and add all these absolute difference and add all these absolute difference
    and add all these absolute

    differences up, differences up, differences up,

    it might add up to a huge value. If we it might add up to a huge value. If we
    it might add up to a huge value. If we

    have a lot of data points which are have a lot of data points which are have a
    lot of data points which are

    included in uh in the sample range. included in uh in the sample range. included
    in uh in the sample range.

    So we need a measure which is which can So we need a measure which is which can
    So we need a measure which is which can

    capture this discrepancy capture this discrepancy capture this discrepancy

    and uh which also does not blow up in and uh which also does not blow up in and
    uh which also does not blow up in

    case there are a huge number of data case there are a huge number of data case
    there are a huge number of data

    points points points

    and this is very nicely captured through and this is very nicely captured through
    and this is very nicely captured through

    ratio between these two distributions. ratio between these two distributions.
    ratio between these two distributions.

    For example, in the first case, you can For example, in the first case, you can
    For example, in the first case, you can

    see that the ratio is greater than one, see that the ratio is greater than one,
    see that the ratio is greater than one,

    which means that our model thinks that A which means that our model thinks that
    A which means that our model thinks that A

    is much less likely than reality. is much less likely than reality. is much less
    likely than reality.

    But if you look at the case C, the ratio But if you look at the case C, the ratio
    But if you look at the case C, the ratio

    between the true distribution and the between the true distribution and the'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
- idx: 24
  start_sec: 1753.84
  end_sec: 1813.029
  text: 'between the true distribution and the

    model distribution is actually less than model distribution is actually less than
    model distribution is actually less than

    one. which means that our model has one. which means that our model has one. which
    means that our model has

    predicted predicted predicted

    uh C to be much more likely than uh C to be much more likely than uh C to be much
    more likely than

    reality. reality. reality.

    So the ratio also captures the So the ratio also captures the So the ratio also
    captures the

    discrepancy really well. discrepancy really well. discrepancy really well.

    So ratio shows how many times reality is So ratio shows how many times reality
    is So ratio shows how many times reality is

    bigger or smaller than the model which bigger or smaller than the model which
    bigger or smaller than the model which

    is not captured in the difference. is not captured in the difference. is not captured
    in the difference.

    But we don''t just take the ratio but we But we don''t just take the ratio but
    we But we don''t just take the ratio but we

    take log of the ratio. Why do we take take log of the ratio. Why do we take take
    log of the ratio. Why do we take

    log? Well firstly because if the ratio log? Well firstly because if the ratio
    log? Well firstly because if the ratio

    is one which means both the outcomes is one which means both the outcomes is one
    which means both the outcomes

    both the probabilities are equal log of both the probabilities are equal log of
    both the probabilities are equal log of

    one is zero. So it''s it''s a very good one is zero. So it''s it''s a very good
    one is zero. So it''s it''s a very good

    way of capturing the difference. If both way of capturing the difference. If both
    way of capturing the difference. If both

    are same then our metric is showing that are same then our metric is showing that
    are same then our metric is showing that

    the difference is zero. the difference is zero. the difference is zero.

    Also log keeps the ratios from exploding Also log keeps the ratios from exploding
    Also log keeps the ratios from exploding

    nicely. nicely. nicely.

    So we take the log of the ratio for all'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
- idx: 25
  start_sec: 1813.029
  end_sec: 1876.159
  text: 'So we take the log of the ratio for all So we take the log of the ratio for
    all

    these different points and then just add these different points and then just
    add these different points and then just add

    them up together. them up together. them up together.

    This is the first step. So using log of p of x divided by q of x So using log
    of p of x divided by q of x

    gives us a smooth additive penalty for gives us a smooth additive penalty for
    gives us a smooth additive penalty for

    each outcome. each outcome. each outcome.

    But we don''t just take the log of p of x But we don''t just take the log of p
    of x But we don''t just take the log of p of x

    divided by q of x. We also multiply it divided by q of x. We also multiply it
    divided by q of x. We also multiply it

    by how important the outcome X is. by how important the outcome X is. by how important
    the outcome X is.

    So we also multiply it by P of X which So we also multiply it by P of X which
    So we also multiply it by P of X which

    means that let''s look at this first means that let''s look at this first means
    that let''s look at this first

    example case A. example case A. example case A.

    The blue bar is significantly higher The blue bar is significantly higher The
    blue bar is significantly higher

    compared to case C which means that compared to case C which means that compared
    to case C which means that

    outcome A is much more likely compared outcome A is much more likely compared
    outcome A is much more likely compared

    to outcome C. So any difference for to outcome C. So any difference for to outcome
    C. So any difference for

    outcome A should be penalized more outcome A should be penalized more outcome
    A should be penalized more

    compared to outcome C. And this is taken compared to outcome C. And this is taken
    compared to outcome C. And this is taken

    into account by multiplying by a factor into account by multiplying by a factor'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
- idx: 26
  start_sec: 1876.159
  end_sec: 1944.96
  text: 'into account by multiplying by a factor

    which is dependent on how likely the which is dependent on how likely the which
    is dependent on how likely the

    case is under the true distribution. case is under the true distribution. case
    is under the true distribution.

    So this is the final formula which is P So this is the final formula which is
    P So this is the final formula which is P

    of X multiplied by log of P of X divided of X multiplied by log of P of X divided
    of X multiplied by log of P of X divided

    by Q ofX and we just sum it all up. Here I have and we just sum it all up. Here
    I have

    just shown for three cases but you do just shown for three cases but you do just
    shown for three cases but you do

    the same mathematical calculation for the same mathematical calculation for the
    same mathematical calculation for

    all the samples of X and then just add all the samples of X and then just add
    all the samples of X and then just add

    them up together. So KL divergence adds them up together. So KL divergence adds
    them up together. So KL divergence adds

    up these penalties for every possible up these penalties for every possible up
    these penalties for every possible

    outcome. So you can see when Q is very close to P So you can see when Q is very
    close to P

    uh this ratio is going to be close to uh this ratio is going to be close to uh
    this ratio is going to be close to

    one. So log of that is going to be very one. So log of that is going to be very
    one. So log of that is going to be very

    small and that''s why KL divergence is small and that''s why KL divergence is
    small and that''s why KL divergence is

    almost near zero which is exactly what almost near zero which is exactly what
    almost near zero which is exactly what

    we want. we want. we want.

    So scale divergence compares a true So scale divergence compares a true So scale
    divergence compares a true

    distribution with a model distribution distribution with a model distribution'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
- idx: 27
  start_sec: 1944.96
  end_sec: 2013.84
  text: 'distribution with a model distribution

    Q. It is zero when P and Q are identical Q. It is zero when P and Q are identical
    Q. It is zero when P and Q are identical

    and grows as Q becomes worse. Especially and grows as Q becomes worse. Especially
    and grows as Q becomes worse. Especially

    when P of X is large and Q is very when P of X is large and Q is very when P of
    X is large and Q is very

    wrong. wrong. wrong.

    So this is the metric which we are going So this is the metric which we are going
    So this is the metric which we are going

    to use to understand to use to understand to use to understand

    how the model distribution how the model distribution how the model distribution

    differs from reality and it is differs from reality and it is differs from reality
    and it is

    quantified by this metric called KL quantified by this metric called KL quantified
    by this metric called KL

    divergence. So whenever you hear this divergence. So whenever you hear this divergence.
    So whenever you hear this

    term, I want all of you to visualize term, I want all of you to visualize term,
    I want all of you to visualize

    this video and uh have a mental picture this video and uh have a mental picture
    this video and uh have a mental picture

    that kale divergence is measuring the that kale divergence is measuring the that
    kale divergence is measuring the

    difference between two probability difference between two probability difference
    between two probability

    distributions. Okay. So uh now that we have understood Okay. So uh now that we
    have understood

    about the objective of a deep generative about the objective of a deep generative
    about the objective of a deep generative

    model, we also understand how can we model, we also understand how can we model,
    we also understand how can we

    quantify quantify

    the difference between the model the difference between the model the difference
    between the model

    predictions and the true predictions. predictions and the true predictions. predictions
    and the true predictions.

    Why don''t we start understanding about Why don''t we start understanding about
    Why don''t we start understanding about

    how do we start to train these deep how do we start to train these deep'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
- idx: 28
  start_sec: 2013.84
  end_sec: 2107.829
  text: 'how do we start to train these deep

    generative models. So let''s understand generative models. So let''s understand
    generative models. So let''s understand

    that. objectives of objectives of

    deep generative modeling is to make sure deep generative modeling is to make sure
    deep generative modeling is to make sure

    that the predicted model approaches as that the predicted model approaches as
    that the predicted model approaches as

    close as possible close as possible close as possible

    to the true distribution. Now this predicted distribution which is Now this predicted
    distribution which is

    denoted by P subscript phi denoted by P subscript phi denoted by P subscript phi

    has to be a probability distribution. has to be a probability distribution. has
    to be a probability distribution.

    So it must satisfy two fundamental So it must satisfy two fundamental So it must
    satisfy two fundamental

    properties. The first property is that properties. The first property is that
    properties. The first property is that

    of non- negativity. of non- negativity. of non- negativity.

    P of five should be greater than zero P of five should be greater than zero P
    of five should be greater than zero

    for all x in the domain. for all x in the domain. for all x in the domain.

    So we saw this for the first example So we saw this for the first example So we
    saw this for the first example

    that we looked at which was the that we looked at which was the that we looked
    at which was the

    distribution of the students heights. distribution of the students heights. distribution
    of the students heights.

    And in fact this is true for any And in fact this is true for any And in fact
    this is true for any

    probability distribution. The probability distribution. The probability distribution.
    The

    probability should always be greater probability should always be greater probability
    should always be greater

    than zero. And the second point is the than zero. And the second point is the
    than zero. And the second point is the

    integral over the entire domain should integral over the entire domain should
    integral over the entire domain should

    be one. Which means that the be one. Which means that the be one. Which means
    that the

    probabilities of all possible outcomes probabilities of all possible outcomes
    probabilities of all possible outcomes

    should always add up to one.'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
- idx: 29
  start_sec: 2107.829
  end_sec: 2165.75
  text: 'should always add up to one. should always add up to one.

    Take an example of a coin toss. Take an example of a coin toss. Take an example
    of a coin toss.

    Probability of heads is 0.5. Probability Probability of heads is 0.5. Probability
    Probability of heads is 0.5. Probability

    of tails is also 0.5. So it adds up to of tails is also 0.5. So it adds up to
    of tails is also 0.5. So it adds up to

    one. one. one.

    That''s the way probabilities are That''s the way probabilities are That''s the
    way probabilities are

    defined. So whenever we are training a defined. So whenever we are training a
    defined. So whenever we are training a

    neural network to predict the neural network to predict the neural network to
    predict the

    probabilities, probabilities, probabilities,

    we need to make sure that these two we need to make sure that these two we need
    to make sure that these two

    properties are satisfied. properties are satisfied. properties are satisfied.

    Now let''s look at the first property Now let''s look at the first property Now
    let''s look at the first property

    which is ensuring non- negativity. which is ensuring non- negativity. which is
    ensuring non- negativity.

    Ensuring non- negativity is not very Ensuring non- negativity is not very Ensuring
    non- negativity is not very

    difficult because we can simply apply a difficult because we can simply apply
    a difficult because we can simply apply a

    positive function to the raw output of positive function to the raw output of
    positive function to the raw output of

    the neural network. For example, if the the neural network. For example, if the
    the neural network. For example, if the

    output of the neural network is E, output of the neural network is E, output of
    the neural network is E,

    we can modify it by taking the absolute we can modify it by taking the absolute
    we can modify it by taking the absolute

    value of E or we can just take the value of E or we can just take the value of
    E or we can just take the

    square of E. Both of these will uh both square of E. Both of these will uh both
    square of E. Both of these will uh both

    of these operations will make sure that'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
- idx: 30
  start_sec: 2165.75
  end_sec: 2224.8
  text: 'of these operations will make sure that of these operations will make sure
    that

    the output is positive. A very common the output is positive. A very common the
    output is positive. A very common

    choice is the exponential function choice is the exponential function choice is
    the exponential function

    which makes sure that the output always which makes sure that the output always
    which makes sure that the output always

    stays positive. stays positive. stays positive.

    What about the second criteria which is What about the second criteria which is
    What about the second criteria which is

    enforcing normalization? enforcing normalization? enforcing normalization?

    Let''s understand this concept using an Let''s understand this concept using an
    Let''s understand this concept using an

    example. So we are going to take a very example. So we are going to take a very
    example. So we are going to take a very

    very simple example here. very simple example here. very simple example here.

    So what we are going to do is that we So what we are going to do is that we So
    what we are going to do is that we

    are going to take an example where three are going to take an example where three
    are going to take an example where three

    students have got marks of 40, 30 and students have got marks of 40, 30 and students
    have got marks of 40, 30 and

    20. 20. 20.

    So you can see that the total score is So you can see that the total score is
    So you can see that the total score is

    90 but it it does not add up to one. So 90 but it it does not add up to one. So
    90 but it it does not add up to one. So

    what do you do to make sure that it adds what do you do to make sure that it adds
    what do you do to make sure that it adds

    up to one? To turn scores into probabilities, we To turn scores into probabilities,
    we

    simply divide it by the total score. So simply divide it by the total score. So
    simply divide it by the total score. So

    you divide all of these numbers by 90. you divide all of these numbers by 90.'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
- idx: 31
  start_sec: 2224.8
  end_sec: 2290.56
  text: 'you divide all of these numbers by 90.

    So you get Alice, Bob and Charlie as 44, So you get Alice, Bob and Charlie as
    44, So you get Alice, Bob and Charlie as 44,

    33 and 22. And these numbers add up 33 and 22. And these numbers add up 33 and
    22. And these numbers add up

    nicely to one. nicely to one. nicely to one.

    So it looks straightforward, right? Why So it looks straightforward, right? Why
    So it looks straightforward, right? Why

    don''t we just don''t we just don''t we just

    you know divide by this factor which is you know divide by this factor which is
    you know divide by this factor which is

    the total score so that we make sure the total score so that we make sure the
    total score so that we make sure

    that the addition of all the probability that the addition of all the probability
    that the addition of all the probability

    values is one. The biggest values is one. The biggest values is one. The biggest

    challenge of this is that this challenge of this is that this challenge of this
    is that this

    normalizing constant which is also normalizing constant which is also normalizing
    constant which is also

    called as the partition function. called as the partition function. called as
    the partition function.

    It is intractable and impossible to It is intractable and impossible to It is
    intractable and impossible to

    calculate. calculate. calculate.

    Why is it impossible to calculate? Let''s Why is it impossible to calculate? Let''s
    Why is it impossible to calculate? Let''s

    have a look at this example. Essentially have a look at this example. Essentially
    have a look at this example. Essentially

    what we are saying is that we need to what we are saying is that we need to what
    we are saying is that we need to

    calculate calculate calculate

    the scores for all of these different the scores for all of these different the
    scores for all of these different

    samples and add them together and divide samples and add them together and divide
    samples and add them together and divide

    it by the scores for these samples. Now it by the scores for these samples. Now
    it by the scores for these samples. Now

    finding the scores for every single finding the scores for every single'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
- idx: 32
  start_sec: 2290.56
  end_sec: 2351.349
  text: 'finding the scores for every single

    sample in this contour is going to be sample in this contour is going to be sample
    in this contour is going to be

    challenging because we do not even know challenging because we do not even know
    challenging because we do not even know

    how many samples there are and this how many samples there are and this how many
    samples there are and this

    looks like a massive task. So this is looks like a massive task. So this is looks
    like a massive task. So this is

    not possible to calculate for a complex not possible to calculate for a complex
    not possible to calculate for a complex

    scenario. We can do this for a simple scenario. We can do this for a simple scenario.
    We can do this for a simple

    example like we saw in the video. But to example like we saw in the video. But
    to example like we saw in the video. But to

    calculate this partition function for a calculate this partition function for
    a calculate this partition function for a

    practical example is impossible. practical example is impossible. practical example
    is impossible.

    This interactability is a central This interactability is a central This interactability
    is a central

    problem which motivates the development problem which motivates the development
    problem which motivates the development

    of different families of deep generative of different families of deep generative
    of different families of deep generative

    models. models. models.

    So now we are coming to the point where So now we are coming to the point where
    So now we are coming to the point where

    we understand that okay this is the we understand that okay this is the we understand
    that okay this is the

    objective of deep generative model but objective of deep generative model but
    objective of deep generative model but

    getting there is not easy because this getting there is not easy because this
    getting there is not easy because this

    partition function is very hard to partition function is very hard to partition
    function is very hard to

    calculate. So people have developed calculate. So people have developed calculate.
    So people have developed

    different methods to overcome this and different methods to overcome this and
    different methods to overcome this and

    uh we are now going to briefly discuss'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
- idx: 33
  start_sec: 2351.349
  end_sec: 2417.04
  text: 'uh we are now going to briefly discuss uh we are now going to briefly discuss

    the different families of deep the different families of deep the different families
    of deep

    generative models. generative models. generative models.

    We will do a deep dive on all these We will do a deep dive on all these We will
    do a deep dive on all these

    different sections in the later different sections in the later different sections
    in the later

    lectures. But I want to give you an lectures. But I want to give you an lectures.
    But I want to give you an

    overview of all the different models overview of all the different models overview
    of all the different models

    which are out there in the literature. which are out there in the literature.
    which are out there in the literature.

    The first set of uh prominent deep generative models is uh prominent deep generative
    models is

    called as energy based models. called as energy based models. called as energy
    based models.

    So energy based models are uh one of the So energy based models are uh one of
    the So energy based models are uh one of the

    earliest models to uh learn the earliest models to uh learn the earliest models
    to uh learn the

    probability distribution of uh the probability distribution of uh the probability
    distribution of uh the

    underlying data underlying data underlying data

    and uh the the technique used in energy and uh the the technique used in energy
    and uh the the technique used in energy

    based models is very interesting. based models is very interesting. based models
    is very interesting.

    You basically convert You basically convert You basically convert

    the probabilities to energy values. So I the probabilities to energy values. So
    I the probabilities to energy values. So I

    uh uh let me let me explain that with a uh uh let me let me explain that with
    a uh uh let me let me explain that with a

    simple rule. The rule says that assign simple rule. The rule says that assign
    simple rule. The rule says that assign

    lower energy to data points which are lower energy to data points which are lower
    energy to data points which are

    more probable and higher energy to data more probable and higher energy to data'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
- idx: 34
  start_sec: 2417.04
  end_sec: 2477.04
  text: 'more probable and higher energy to data

    points which are less probable. points which are less probable. points which are
    less probable.

    So imagine that we collect the exam So imagine that we collect the exam So imagine
    that we collect the exam

    scores of thousand students in a course scores of thousand students in a course
    scores of thousand students in a course

    and uh students don''t score numbers and uh students don''t score numbers and
    uh students don''t score numbers

    between 0 and 100 equally. between 0 and 100 equally. between 0 and 100 equally.

    there is a shape to the data. there is a shape to the data. there is a shape to
    the data.

    Let me bring in my highlighter as well Let me bring in my highlighter as well
    Let me bring in my highlighter as well

    so that can explain this properly. so that can explain this properly. so that
    can explain this properly.

    Okay. So students don''t score every Okay. So students don''t score every Okay.
    So students don''t score every

    number between 0 and 100 equally. There number between 0 and 100 equally. There
    number between 0 and 100 equally. There

    is a shape to the data. is a shape to the data. is a shape to the data.

    Um let''s say the distribution looks like Um let''s say the distribution looks
    like Um let''s say the distribution looks like

    this. Many students score around 70. Few this. Many students score around 70.
    Few this. Many students score around 70. Few

    students score around 40. Few students students score around 40. Few students
    students score around 40. Few students

    score around 90. score around 90. score around 90.

    So let''s say this is the distribution. So let''s say this is the distribution.
    So let''s say this is the distribution.

    These are the scores of the students. These are the scores of the students. These
    are the scores of the students.

    You can see that it looks a bit random. You can see that it looks a bit random.
    You can see that it looks a bit random.

    Some students are scoring 60, some are Some students are scoring 60, some are
    Some students are scoring 60, some are

    scoring 80 etc. scoring 80 etc. scoring 80 etc.

    Now what happens is that Now what happens is that'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
- idx: 35
  start_sec: 2477.04
  end_sec: 2535.119
  text: 'Now what happens is that

    we want a model that can understand this we want a model that can understand this
    we want a model that can understand this

    pattern. So energy based models do not pattern. So energy based models do not
    pattern. So energy based models do not

    assign probabilities directly but every assign probabilities directly but every
    assign probabilities directly but every

    possible score gets an energy value. possible score gets an energy value. possible
    score gets an energy value.

    Energy means how unusual the model Energy means how unusual the model Energy means
    how unusual the model

    thinks that score is. Lower energy means thinks that score is. Lower energy means
    thinks that score is. Lower energy means

    that it is more typical and higher that it is more typical and higher that it
    is more typical and higher

    energy means that it is less typical. energy means that it is less typical. energy
    means that it is less typical.

    Let''s understand that. So here you can Let''s understand that. So here you can
    Let''s understand that. So here you can

    see that 80 has a very high probability see that 80 has a very high probability
    see that 80 has a very high probability

    value. So based on this simple rule, value. So based on this simple rule, value.
    So based on this simple rule,

    assign lower energy to data points which assign lower energy to data points which
    assign lower energy to data points which

    are more probable. are more probable. are more probable.

    80 should receive a low energy. 80 should receive a low energy. 80 should receive
    a low energy.

    Similarly, 60 should also receive a low Similarly, 60 should also receive a low
    Similarly, 60 should also receive a low

    energy. So let''s let''s look at the energy. So let''s let''s look at the energy.
    So let''s let''s look at the

    energy profile. energy profile. energy profile.

    This is the energy landscape for all This is the energy landscape for all This
    is the energy landscape for all

    these scores. And we can clearly see these scores. And we can clearly see these
    scores. And we can clearly see

    that that that

    numbers around 80 have a lower energy. numbers around 80 have a lower energy.'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
- idx: 36
  start_sec: 2535.119
  end_sec: 2592.079
  text: 'numbers around 80 have a lower energy.

    numbers around 60 have a lower energy. numbers around 60 have a lower energy.
    numbers around 60 have a lower energy.

    Numbers around 30 which are not very Numbers around 30 which are not very Numbers
    around 30 which are not very

    probable at all. They have a very high probable at all. They have a very high
    probable at all. They have a very high

    energy. energy. energy.

    So uh it''s it''s it''s like if you roll a So uh it''s it''s it''s like if you
    roll a So uh it''s it''s it''s like if you roll a

    ball down this it will settle to points ball down this it will settle to points
    ball down this it will settle to points

    which are more probable which are points which are more probable which are points
    which are more probable which are points

    of lower energy. So what is done in of lower energy. So what is done in of lower
    energy. So what is done in

    energy based models is that first the energy based models is that first the energy
    based models is that first the

    energy landscape is is predicted for all energy landscape is is predicted for
    all energy landscape is is predicted for all

    the scores so that this energy landscape the scores so that this energy landscape
    the scores so that this energy landscape

    can then be easily converted to a can then be easily converted to a can then be
    easily converted to a

    probability distribution probability distribution probability distribution

    and this is done by simply taking the and this is done by simply taking the and
    this is done by simply taking the

    exponential of this energy distribution. exponential of this energy distribution.
    exponential of this energy distribution.

    So there are three steps. the the the So there are three steps. the the the So
    there are three steps. the the the

    first step is to uh understand that first step is to uh understand that first
    step is to uh understand that

    higher probabilities should receive a higher probabilities should receive a higher
    probabilities should receive a

    lower score and lower probabilities lower score and lower probabilities lower
    score and lower probabilities

    should receive a higher score. Once we should receive a higher score. Once we'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
- idx: 37
  start_sec: 2592.079
  end_sec: 2688.8
  text: 'should receive a higher score. Once we

    understand this simple rule, the understand this simple rule, the understand this
    simple rule, the

    objective of energy based models is to objective of energy based models is to
    objective of energy based models is to

    find this energy landscape. find this energy landscape. find this energy landscape.

    Once this energy landscape is found, we Once this energy landscape is found, we
    Once this energy landscape is found, we

    can easily convert that to a probability can easily convert that to a probability
    can easily convert that to a probability

    distribution. So let''s have a look at this video which So let''s have a look
    at this video which

    explains this in a more visual manner. On the x-axis we have the exam scores On
    the x-axis we have the exam scores

    and on the y-axis we have the energy. So and on the y-axis we have the energy.
    So and on the y-axis we have the energy. So

    we can see that we can see that we can see that

    exam scores around exam scores around exam scores around

    70 have a very low energy which is 70 have a very low energy which is 70 have
    a very low energy which is

    assigned by the model. So lower energy means scores which have So lower energy
    means scores which have

    higher probability which are more higher probability which are more higher probability
    which are more

    typical. And now you see the probability And now you see the probability

    distribution exactly reflects that distribution exactly reflects that distribution
    exactly reflects that

    scores which are having lower energy scores which are having lower energy scores
    which are having lower energy

    they are assigned higher probability by they are assigned higher probability by
    they are assigned higher probability by

    the model. So it is shown very nicely in this So it is shown very nicely in this

    animation. So the red point has a higher energy and So the red point has a higher
    energy and

    a low probability. The green point has a a low probability. The green point has
    a a low probability. The green point has a

    low energy but a higher probability. low energy but a higher probability. low
    energy but a higher probability.

    So energy based models uh So energy based models uh'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
- idx: 38
  start_sec: 2688.8
  end_sec: 2762.39
  text: 'So energy based models uh

    was the first starting point for deep was the first starting point for deep was
    the first starting point for deep

    generative modeling. generative modeling.

    Then we moved on to another class of Then we moved on to another class of Then
    we moved on to another class of

    models which are called as auto models which are called as auto models which are
    called as auto

    reggressive models. This is exactly same reggressive models. This is exactly same
    reggressive models. This is exactly same

    as the way current LLMs like chat GPT as the way current LLMs like chat GPT as
    the way current LLMs like chat GPT

    work. They predict one token at a time. work. They predict one token at a time.
    work. They predict one token at a time.

    So the objective is to predict the next So the objective is to predict the next
    So the objective is to predict the next

    token token token

    and the next piece depends on everything and the next piece depends on everything
    and the next piece depends on everything

    that is generated so far. Since all of that is generated so far. Since all of
    that is generated so far. Since all of

    us are aware about large language models us are aware about large language models
    us are aware about large language models

    and how they generate tokens, I''m just and how they generate tokens, I''m just
    and how they generate tokens, I''m just

    going to play this video which uh going to play this video which uh going to play
    this video which uh

    explains this properly. explains this properly. explains this properly.

    Let me just uh open this up. Okay, so this video nicely explains how Okay, so
    this video nicely explains how

    large language models generate one uh large language models generate one uh large
    language models generate one uh

    token at a time. Initially, we start token at a time. Initially, we start token
    at a time. Initially, we start

    from once upon aer then these tokens are from once upon aer then these tokens
    are from once upon aer then these tokens are

    provided as a context to the LLM. provided as a context to the LLM. provided as
    a context to the LLM.

    After this context is seen by the LLM,'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
- idx: 39
  start_sec: 2762.39
  end_sec: 2821.03
  text: 'After this context is seen by the LLM, After this context is seen by the
    LLM,

    it predicts the next token it predicts the next token it predicts the next token

    based on the token which gets the based on the token which gets the based on the
    token which gets the

    highest probability score. Once we have highest probability score. Once we have
    highest probability score. Once we have

    once upon a time, then all of these once upon a time, then all of these once upon
    a time, then all of these

    words become a context and the next word words become a context and the next word
    words become a context and the next word

    is predicted which is there and this is predicted which is there and this is predicted
    which is there and this

    process continues till we reach the end process continues till we reach the end
    process continues till we reach the end

    of the sentence. of the sentence. of the sentence.

    So this is how auto reggressive models So this is how auto reggressive models
    So this is how auto reggressive models

    work. each each word depends on all the each each word depends on all the

    previous words and this is also an previous words and this is also an previous
    words and this is also an

    example of a deep generative model. example of a deep generative model. example
    of a deep generative model.

    Now we move to the next class of uh deep Now we move to the next class of uh deep
    Now we move to the next class of uh deep

    generative models which are called as generative models which are called as generative
    models which are called as

    variational autoenccoders. variational autoenccoders. variational autoenccoders.

    Now uh this is a pretty Now uh this is a pretty Now uh this is a pretty

    involved concept and we are going to involved concept and we are going to involved
    concept and we are going to

    cover this exactly in detail in the next cover this exactly in detail in the next
    cover this exactly in detail in the next

    lecture but I want all of you to you lecture but I want all of you to you lecture
    but I want all of you to you

    know take a look at this video first'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
- idx: 40
  start_sec: 2821.03
  end_sec: 2879.52
  text: 'know take a look at this video first know take a look at this video first

    which explains variational autoenccoders which explains variational autoenccoders
    which explains variational autoenccoders

    at a very high level. at a very high level. at a very high level.

    So we have an input which goes through So we have an input which goes through
    So we have an input which goes through

    an encoder an encoder an encoder

    and the encoder basically compresses the and the encoder basically compresses
    the and the encoder basically compresses the

    input to a small latent code. So uh the the input is is compressed So uh the the
    input is is compressed

    then the latent space it it captures the then the latent space it it captures
    the then the latent space it it captures the

    hidden structure in the data. It''s like hidden structure in the data. It''s like
    hidden structure in the data. It''s like

    a way of compressing your data and then a way of compressing your data and then
    a way of compressing your data and then

    from the Latin space the data is fed from the Latin space the data is fed from
    the Latin space the data is fed

    through the decoder and then the decoder through the decoder and then the decoder
    through the decoder and then the decoder

    turns the Latin code back into a sample turns the Latin code back into a sample
    turns the Latin code back into a sample

    which looks very similar to the input. which looks very similar to the input.
    which looks very similar to the input.

    This is very different from a This is very different from a This is very different
    from a

    traditional autoenccoder because the traditional autoenccoder because the traditional
    autoenccoder because the

    latent space is is is probabilistic. It latent space is is is probabilistic. It
    latent space is is is probabilistic. It

    it learns a distribution not a single it learns a distribution not a single it
    learns a distribution not a single

    value. So if we take an example of a cat value. So if we take an example of a
    cat value. So if we take an example of a cat

    image flowing through a autoenccoder you image flowing through a autoenccoder
    you'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
- idx: 41
  start_sec: 2879.52
  end_sec: 2934.24
  text: 'image flowing through a autoenccoder you

    can see that the latin space the image can see that the latin space the image
    can see that the latin space the image

    is blurred because we are reducing the is blurred because we are reducing the
    is blurred because we are reducing the

    number of dimensions number of dimensions number of dimensions

    it does not capture all the features it does not capture all the features it does
    not capture all the features

    which are present in the data. which are present in the data. which are present
    in the data.

    uh but the objective is to capture uh but the objective is to capture uh but the
    objective is to capture

    enough features that allow us to enough features that allow us to enough features
    that allow us to

    reconstruct the input and then once we reconstruct the input and then once we
    reconstruct the input and then once we

    have the latin space with us we can have the latin space with us we can have the
    latin space with us we can

    sample from the latin space again and sample from the latin space again and sample
    from the latin space again and

    again to generate different again to generate different again to generate different

    uh samples of of cat. uh samples of of cat. uh samples of of cat.

    So this is how variational autoenccoders So this is how variational autoenccoders
    So this is how variational autoenccoders

    work and uh they are one of the most work and uh they are one of the most work
    and uh they are one of the most

    important important important

    contributions to the families of contributions to the families of contributions
    to the families of

    prominent deep generative models. prominent deep generative models. prominent
    deep generative models.

    They they they actually laid the They they they actually laid the They they they
    actually laid the

    foundations for later advances including foundations for later advances including
    foundations for later advances including

    diffusion models. As I said we will diffusion models. As I said we will diffusion
    models. As I said we will

    cover this in detail in the next lecture cover this in detail in the next lecture
    cover this in detail in the next lecture

    which is devoted exactly on this. The which is devoted exactly on this. The'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
- idx: 42
  start_sec: 2934.24
  end_sec: 3001.76
  text: 'which is devoted exactly on this. The

    next prominent milestone is called as next prominent milestone is called as next
    prominent milestone is called as

    normalizing flows. normalizing flows. normalizing flows.

    So this is uh quite intuitive. So So this is uh quite intuitive. So So this is
    uh quite intuitive. So

    imagine you have two kinds of shapes imagine you have two kinds of shapes imagine
    you have two kinds of shapes

    like a perfect round ball and a crumpled like a perfect round ball and a crumpled
    like a perfect round ball and a crumpled

    piece of paper. piece of paper. piece of paper.

    Normalizing flows are methods which Normalizing flows are methods which Normalizing
    flows are methods which

    learn how to slowly and smoothly learn how to slowly and smoothly learn how to
    slowly and smoothly

    stretch, twist and bend the simple shape stretch, twist and bend the simple shape
    stretch, twist and bend the simple shape

    so that it exactly becomes the complex so that it exactly becomes the complex
    so that it exactly becomes the complex

    shape without tearing or gluing shape without tearing or gluing shape without
    tearing or gluing

    anything. anything. anything.

    So this this video I think uh you know So this this video I think uh you know
    So this this video I think uh you know

    explains explains explains

    normalizing flows very nicely. So you start with some some noise let''s So you
    start with some some noise let''s

    say a goshian distribution and then you say a goshian distribution and then you
    say a goshian distribution and then you

    apply different operations like you can apply different operations like you can
    apply different operations like you can

    stretch it you can twist it. It''s it''s stretch it you can twist it. It''s it''s
    stretch it you can twist it. It''s it''s

    almost like a fluid element. you can uh almost like a fluid element. you can uh
    almost like a fluid element. you can uh

    bend it and this is how you actually get bend it and this is how you actually
    get bend it and this is how you actually get

    to the true distribution. You start with to the true distribution. You start with
    to the true distribution. You start with

    some simple distribution and you twist some simple distribution and you twist'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
- idx: 43
  start_sec: 3001.76
  end_sec: 3084.23
  text: 'some simple distribution and you twist

    it, bend it, turn it to reach the true it, bend it, turn it to reach the true
    it, bend it, turn it to reach the true

    distribution which is exactly what the distribution which is exactly what the
    distribution which is exactly what the

    deep generative model tries to predict. deep generative model tries to predict.
    deep generative model tries to predict.

    Normalizing flows is a very important Normalizing flows is a very important Normalizing
    flows is a very important

    milestone in the class of u deep milestone in the class of u deep milestone in
    the class of u deep

    generative models and we are also going generative models and we are also going
    generative models and we are also going

    to cover this in detail in in in this to cover this in detail in in in this to
    cover this in detail in in in this

    course. course. course.

    The next The next The next

    uh advancement which is called as uh advancement which is called as uh advancement
    which is called as

    generative adversarial networks is more generative adversarial networks is more
    generative adversarial networks is more

    widely known in literature. It consists widely known in literature. It consists
    widely known in literature. It consists

    of two networks a generator and a of two networks a generator and a of two networks
    a generator and a

    discriminator that compete against each discriminator that compete against each
    discriminator that compete against each

    other. The generator aims to create other. The generator aims to create other.
    The generator aims to create

    realistic samples from random noise realistic samples from random noise realistic
    samples from random noise

    while the discriminator attempts to while the discriminator attempts to while
    the discriminator attempts to

    distinguish between these two samples. distinguish between these two samples.
    distinguish between these two samples.

    So uh I''m I''m just going to explain this So uh I''m I''m just going to explain
    this So uh I''m I''m just going to explain this

    using uh okay so this is an interactive which we okay so this is an interactive
    which we

    have built which uh explains this. So we have created a story which So we have
    created a story which

    explains explains

    generative adversal networks nicely. So the inspector has the objective to So
    the inspector has the objective to

    investigate'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
- idx: 44
  start_sec: 3084.23
  end_sec: 3165.44
  text: 'investigate investigate

    the difference between generated art and the difference between generated art
    and the difference between generated art and

    deep fix. We basically have to identify We basically have to identify

    uh which paintings have been replaced uh which paintings have been replaced uh
    which paintings have been replaced

    and uh to that we to to do that we need and uh to that we to to do that we need
    and uh to that we to to do that we need

    to learn to distinguish between real and to learn to distinguish between real
    and to learn to distinguish between real and

    and fake samples. and fake samples. and fake samples.

    So these are just some uh activities So these are just some uh activities So these
    are just some uh activities

    where we have to you know classify where we have to you know classify where we
    have to you know classify

    whether these images were real or AI whether these images were real or AI whether
    these images were real or AI

    generated. I''m going to quickly go generated. I''m going to quickly go generated.
    I''m going to quickly go

    through this since I want to f focus on through this since I want to f focus on
    through this since I want to f focus on

    the main point. the main point. the main point.

    So in in many cases it''s it''s not very So in in many cases it''s it''s not very
    So in in many cases it''s it''s not very

    easy that uh I''m I''m really confused easy that uh I''m I''m really confused
    easy that uh I''m I''m really confused

    because it''s it''s very hard to because it''s it''s very hard to because it''s
    it''s very hard to

    distinguish. In some cases I can easily distinguish. In some cases I can easily
    distinguish. In some cases I can easily

    tell but in many cases I''m I''m rather tell but in many cases I''m I''m rather
    tell but in many cases I''m I''m rather

    confused. confused. confused.

    So this I know because this is the Gibli So this I know because this is the Gibli
    So this I know because this is the Gibli

    style which famous. Okay. So um Okay. So um

    now what what happens in u GAN is that there is a generator and a'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
- idx: 45
  start_sec: 3165.44
  end_sec: 3259.75
  text: 'there is a generator and a

    discriminator. The generator discriminator. The generator discriminator. The generator

    generates images and the role of the generates images and the role of the generates
    images and the role of the

    discriminator is to identify whether discriminator is to identify whether discriminator
    is to identify whether

    these images are uh real or they are these images are uh real or they are these
    images are uh real or they are

    fake. So initially the the the discriminator So initially the the the discriminator

    can easily tell the difference because can easily tell the difference because
    can easily tell the difference because

    it it understands that this image is it it understands that this image is it it
    understands that this image is

    completely fake. But then the artists become better and But then the artists become
    better and

    better and they learn to basically fool better and they learn to basically fool
    better and they learn to basically fool

    the discriminator. So we can actually understand this using So we can actually
    understand this using

    a nice u interactive interactive

    experiment. So experiment. So experiment. So

    you see initially this image which is you see initially this image which is you
    see initially this image which is

    generated by the generator is very bad. generated by the generator is very bad.
    generated by the generator is very bad.

    Discriminator easily catches it. Discriminator easily catches it. Discriminator
    easily catches it.

    And uh this this happens for multiple And uh this this happens for multiple And
    uh this this happens for multiple

    generations. Fake image detected generations. Fake image detected generations.
    Fake image detected

    discriminator is again uh catching the discriminator is again uh catching the
    discriminator is again uh catching the

    image as fake. But now you can see that image as fake. But now you can see that
    image as fake. But now you can see that

    the quality of the image is slowly the quality of the image is slowly the quality
    of the image is slowly

    getting better and better and there will getting better and better and there will
    getting better and better and there will

    come a point where the discriminator come a point where the discriminator come
    a point where the discriminator

    will will will

    not be able to recognize this as a fake'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
- idx: 46
  start_sec: 3259.75
  end_sec: 3315.75
  text: 'not be able to recognize this as a fake not be able to recognize this as
    a fake

    image. image. image.

    So see here real image detected the the So see here real image detected the the
    So see here real image detected the the

    the generated the generator has the generated the generator has the generated
    the generator has

    succeeded. succeeded. succeeded.

    So the reason I showed this to you is So the reason I showed this to you is So
    the reason I showed this to you is

    that I I believe it''s a very nice that I I believe it''s a very nice that I I
    believe it''s a very nice

    interactive project which builds interactive project which builds interactive
    project which builds

    intuition intuition intuition

    with respect to uh GANs. Now all of these methods can be GANs. Now all of these
    methods can be

    very nicely summarized in one simple very nicely summarized in one simple very
    nicely summarized in one simple

    diagram. We covered energy based diagram. We covered energy based diagram. We
    covered energy based

    methods, auto reggressive methods, methods, auto reggressive methods, methods,
    auto reggressive methods,

    variational autoenccoders, normalizing variational autoenccoders, normalizing
    variational autoenccoders, normalizing

    flows and GANs. The objective of all of flows and GANs. The objective of all of
    flows and GANs. The objective of all of

    these methods is to predict a these methods is to predict a these methods is to
    predict a

    probability distribution which matches probability distribution which matches
    probability distribution which matches

    as close as possible to the true as close as possible to the true as close as
    possible to the true

    distribution. distribution.

    Very similar to the student heights Very similar to the student heights Very similar
    to the student heights

    example which we started off in this example which we started off in this example
    which we started off in this

    lecture where our objective was to lecture where our objective was to lecture
    where our objective was to

    predict the height of a incoming predict the height of a incoming predict the
    height of a incoming

    student. To do that prediction, we student. To do that prediction, we student.
    To do that prediction, we

    needed to understand the distribution of needed to understand the distribution
    of needed to understand the distribution of

    student heights. But we only had a few'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
- idx: 47
  start_sec: 3315.75
  end_sec: 3370.4
  text: 'student heights. But we only had a few student heights. But we only had a
    few

    data samples. So we had to use those data samples. So we had to use those data
    samples. So we had to use those

    data samples to predict the distribution data samples to predict the distribution
    data samples to predict the distribution

    that matches as close as possible to the that matches as close as possible to
    the that matches as close as possible to the

    true distribution. true distribution.

    Now uh this is one of the main Now uh this is one of the main Now uh this is one
    of the main

    objectives of deep generative models objectives of deep generative models objectives
    of deep generative models

    where the predicted model denoted as P5 where the predicted model denoted as P5
    where the predicted model denoted as P5

    is trained to match the true model P is trained to match the true model P is trained
    to match the true model P

    data as close as possible. This data as close as possible. This data as close
    as possible. This

    difference is quantified using a matrix difference is quantified using a matrix
    difference is quantified using a matrix

    called KL divergence. Uh which we saw called KL divergence. Uh which we saw called
    KL divergence. Uh which we saw

    using a very interesting example that using a very interesting example that using
    a very interesting example that

    how the KL divergence measures the how the KL divergence measures the how the
    KL divergence measures the

    difference between two distributions by difference between two distributions by
    difference between two distributions by

    weighing uh by by penalizing the weighing uh by by penalizing the weighing uh
    by by penalizing the

    differences more if the uh original differences more if the uh original differences
    more if the uh original

    distribution is more likely. distribution is more likely. distribution is more
    likely.

    Now once we have understood the broader Now once we have understood the broader
    Now once we have understood the broader

    picture we tried to understand the picture we tried to understand the picture
    we tried to understand the

    challenges in predicting this challenges in predicting this challenges in predicting
    this

    distribution mainly we looked at finding distribution mainly we looked at finding'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
- idx: 48
  start_sec: 3370.4
  end_sec: 3424.319
  text: 'distribution mainly we looked at finding

    the normalizing factor is very difficult the normalizing factor is very difficult
    the normalizing factor is very difficult

    and uh that''s why we need more and uh that''s why we need more and uh that''s
    why we need more

    sophisticated methods where we can get sophisticated methods where we can get
    sophisticated methods where we can get

    rid of this normalizing factor which is rid of this normalizing factor which is
    rid of this normalizing factor which is

    also called as the partition function also called as the partition function also
    called as the partition function

    and all of these five methods have you and all of these five methods have you
    and all of these five methods have you

    know formed the backbone of deep know formed the backbone of deep know formed
    the backbone of deep

    generative modeling and they have given generative modeling and they have given
    generative modeling and they have given

    rise to diffusion models in general. Uh rise to diffusion models in general. Uh
    rise to diffusion models in general. Uh

    so we are going to look at these models so we are going to look at these models
    so we are going to look at these models

    in detail in detail in detail

    but uh I really want to give you a nice but uh I really want to give you a nice
    but uh I really want to give you a nice

    visual understanding of the concepts in visual understanding of the concepts in
    visual understanding of the concepts in

    this lecture. Several of these concepts this lecture. Several of these concepts
    this lecture. Several of these concepts

    might seem mathematical but once you go might seem mathematical but once you go
    might seem mathematical but once you go

    through this lecture again you can see through this lecture again you can see
    through this lecture again you can see

    the videos really help explain the story the videos really help explain the story
    the videos really help explain the story

    very nicely and the connection to very nicely and the connection to very nicely
    and the connection to

    diffusion models is also diffusion models is also diffusion models is also

    straightforward. So these classical straightforward. So these classical straightforward.
    So these classical

    families uh illustrate complimentary families uh illustrate complimentary'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
- idx: 49
  start_sec: 3424.319
  end_sec: 3476.799
  text: 'families uh illustrate complimentary

    strategies for modeling complex strategies for modeling complex strategies for
    modeling complex

    distribution and they also provide distribution and they also provide distribution
    and they also provide

    guiding principles for understanding guiding principles for understanding guiding
    principles for understanding

    diffusion models as diffusion models diffusion models as diffusion models diffusion
    models as diffusion models

    inherit ideas from several of these inherit ideas from several of these inherit
    ideas from several of these

    perspectives. perspectives. perspectives.

    So we are going to understand these So we are going to understand these So we
    are going to understand these

    models in in in detail. Through my study models in in in detail. Through my study
    models in in in detail. Through my study

    what I have realized is that what I have realized is that what I have realized
    is that

    understanding deep generative modeling understanding deep generative modeling
    understanding deep generative modeling

    process gives us a very nice perspective process gives us a very nice perspective
    process gives us a very nice perspective

    on on on

    how to think from a how to think from a how to think from a

    uh perspective which you know allows us uh perspective which you know allows us
    uh perspective which you know allows us

    to think about distributions not about to think about distributions not about
    to think about distributions not about

    single points. So we will become better single points. So we will become better
    single points. So we will become better

    at understanding what is a distribution, at understanding what is a distribution,
    at understanding what is a distribution,

    how to think from a distribution point how to think from a distribution point
    how to think from a distribution point

    of view because I understand that that of view because I understand that that
    of view because I understand that that

    might seem confusing at first. Why are might seem confusing at first. Why are
    might seem confusing at first. Why are

    we trying to predict a distribution? we trying to predict a distribution? we trying
    to predict a distribution?

    What does it mean exactly? So we will What does it mean exactly? So we will What
    does it mean exactly? So we will

    look at very practical examples as as we look at very practical examples as as
    we'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
- idx: 50
  start_sec: 3476.799
  end_sec: 3490.92
  text: 'look at very practical examples as as we

    move along. move along. move along.

    Thank you very much everyone and uh I Thank you very much everyone and uh I Thank
    you very much everyone and uh I

    hope this lecture motivates you to hope this lecture motivates you to hope this
    lecture motivates you to

    continue in this series and uh please continue in this series and uh please continue
    in this series and uh please

    let me know in the comment section if let me know in the comment section if let
    me know in the comment section if

    you have any doubts. Thank you.'
  concept_slugs:
  - vae-encoder
  - variational-lower-bound
---
# Lecture 1 - Deep Generative Modeling | Principles of Diffusion Models

See the structured chunks above.
