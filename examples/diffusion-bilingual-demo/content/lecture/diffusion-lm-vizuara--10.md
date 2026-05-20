---
course_slug: diffusion-lm-vizuara
idx: 10
title: 'Lecture 9: Auto Regressive Models (ARM) Attention Block'
video_url: https://www.youtube.com/watch?v=sqJfniiuR88
duration_sec: null
chunks:
- idx: 0
  start_sec: 3.59
  end_sec: 52.0
  text: 'So in attention as I mentioned the main So in attention as I mentioned the
    main

    idea is to have these token embeddings idea is to have these token embeddings
    idea is to have these token embeddings

    or to have these embedding vectors for or to have these embedding vectors for
    or to have these embedding vectors for

    each token and somehow link them to each each token and somehow link them to each
    each token and somehow link them to each

    other. So we want to convert these for other. So we want to convert these for
    other. So we want to convert these for

    every token we want to convert this every token we want to convert this every
    token we want to convert this

    input vector into something which is input vector into something which is input
    vector into something which is

    called as a context vector. What it called as a context vector. What it called
    as a context vector. What it

    means is that right now if I to take a means is that right now if I to take a
    means is that right now if I to take a

    look at bright look at bright look at bright

    I have just encoded its token embedding I have just encoded its token embedding
    I have just encoded its token embedding

    position embedding and added both of position embedding and added both of position
    embedding and added both of

    those but I have no clue how much those but I have no clue how much those but
    I have no clue how much

    importance should be given to is day importance should be given to is day importance
    should be given to is day

    next the etc. What a context vector next the etc. What a context vector next the
    etc. What a context vector

    essentially means is that it''s much more essentially means is that it''s much
    more essentially means is that it''s much more

    richer than the input vector. richer than the input vector. richer than the input
    vector.

    It''s richer than the input vector. What It''s richer than the input vector. What
    It''s richer than the input vector. What

    a context vector means is that it needs a context vector means is that it needs
    a context vector means is that it needs

    to capture to capture'
  concept_slugs:
  - autoregressive-vs-diffusion
- idx: 1
  start_sec: 52.0
  end_sec: 110.469
  text: 'to capture

    if I''m looking at a particular token if I''m looking at a particular token if
    I''m looking at a particular token

    like brightite, how much attention I want to capture all of that I want to capture
    all of that

    information into the embedding vector information into the embedding vector information
    into the embedding vector

    for bright. So that will be much more for bright. So that will be much more for
    bright. So that will be much more

    richer than just having the token richer than just having the token richer than
    just having the token

    embedding and adding to the positional embedding and adding to the positional
    embedding and adding to the positional

    embedding. To do that we perform a embedding. To do that we perform a embedding.
    To do that we perform a

    sequence of operations which might look sequence of operations which might look
    sequence of operations which might look

    very non-intuitive to you at the moment very non-intuitive to you at the moment
    very non-intuitive to you at the moment

    but but but

    uh you can think of them as learnable uh you can think of them as learnable uh
    you can think of them as learnable

    matrices which we add. So humans cannot matrices which we add. So humans cannot
    matrices which we add. So humans cannot

    figure out the actual formula for figure out the actual formula for figure out
    the actual formula for

    encoding attention. Right? So we do what encoding attention. Right? So we do what
    encoding attention. Right? So we do what

    we always do. We are lazy. So we we always do. We are lazy. So we we always do.
    We are lazy. So we

    outsource everything to matrices. We outsource everything to matrices. We outsource
    everything to matrices. We

    give free parameters, trainable give free parameters, trainable give free parameters,
    trainable

    parameters and hope that with more parameters and hope that with more parameters
    and hope that with more

    parameters and more matrices, we might parameters and more matrices, we might
    parameters and more matrices, we might

    learn something. In the process, we give learn something. In the process, we give
    learn something. In the process, we give

    these fancy names like query vectors, e these fancy names like query vectors,
    e these fancy names like query vectors, e

    vectors, value vectors, etc. So what is'
  concept_slugs:
  - autoregressive-vs-diffusion
- idx: 2
  start_sec: 110.469
  end_sec: 153.84
  text: 'vectors, value vectors, etc. So what is vectors, value vectors, etc. So what
    is

    done is that we have this input matrix, done is that we have this input matrix,
    done is that we have this input matrix,

    right? and which has five tokens in a right? and which has five tokens in a right?
    and which has five tokens in a

    sequence. Five tokens. We multiply it sequence. Five tokens. We multiply it sequence.
    Five tokens. We multiply it

    with the query weight matrix, the key with the query weight matrix, the key with
    the query weight matrix, the key

    weight matrix and the value weight weight matrix and the value weight weight matrix
    and the value weight

    matrix that leads to my query vectors, matrix that leads to my query vectors,
    matrix that leads to my query vectors,

    key vectors and my value vectors. These key vectors and my value vectors. These
    key vectors and my value vectors. These

    are all trainable. So during back are all trainable. So during back are all trainable.
    So during back

    propagation when I mentioned earlier propagation when I mentioned earlier propagation
    when I mentioned earlier

    that parameters will be updated. If you that parameters will be updated. If you
    that parameters will be updated. If you

    take a look at this part where I take a look at this part where I take a look
    at this part where I

    mentioned that updating parameters, mentioned that updating parameters, mentioned
    that updating parameters,

    this is part of the parameters which this is part of the parameters which this
    is part of the parameters which

    will be updated. will be updated. will be updated.

    So this W, Q, WK and WV are part of So this W, Q, WK and WV are part of So this
    W, Q, WK and WV are part of

    parameters which will be updated. So I parameters which will be updated. So I
    parameters which will be updated. So I

    have my query, I have my key and value have my query, I have my key and value
    have my query, I have my key and value

    and henceforth we''ll be only dealing and henceforth we''ll be only dealing and
    henceforth we''ll be only dealing

    with query key and values in the with query key and values in the'
  concept_slugs:
  - autoregressive-vs-diffusion
- idx: 3
  start_sec: 153.84
  end_sec: 196.64
  text: 'with query key and values in the

    attention block. Right? attention block. Right? attention block. Right?

    Once we have the queries and the keys Once we have the queries and the keys Once
    we have the queries and the keys

    what we do is that we multiply the what we do is that we multiply the what we
    do is that we multiply the

    queries with the keys transpose and get queries with the keys transpose and get
    queries with the keys transpose and get

    what is called as the attention scores. what is called as the attention scores.
    what is called as the attention scores.

    So if I have this is my query matrix the So if I have this is my query matrix
    the So if I have this is my query matrix the

    next day is bright and keys transpose. next day is bright and keys transpose.
    next day is bright and keys transpose.

    So each column here is a token. So the So each column here is a token. So the
    So each column here is a token. So the

    next day is bright. So if you multiply next day is bright. So if you multiply
    next day is bright. So if you multiply

    the queries with the keys, you get an the queries with the keys, you get an the
    queries with the keys, you get an

    attention score matrix. The number of attention score matrix. The number of attention
    score matrix. The number of

    rows of this attention scores is equal rows of this attention scores is equal
    rows of this attention scores is equal

    to the number of tokens which is five. to the number of tokens which is five.
    to the number of tokens which is five.

    Number of columns is also equal to five. Number of columns is also equal to five.
    Number of columns is also equal to five.

    The way to interpret this attention The way to interpret this attention The way
    to interpret this attention

    scores is that if you look at so this 5 scores is that if you look at so this
    5 scores is that if you look at so this 5

    by 5 right 1 2 3 4 5 and let me by 5 right 1 2 3 4 5 and let me'
  concept_slugs:
  - autoregressive-vs-diffusion
- idx: 4
  start_sec: 196.64
  end_sec: 259.84
  text: 'by 5 right 1 2 3 4 5 and let me

    duplicate this duplicate this duplicate this

    1 2 3 1 2 3 1 2 3

    4 and 5. 4 and 5. 4 and 5.

    And And And

    this is the this is the this is the

    next next next

    day is bright. day is bright. day is bright.

    And this is the And this is the And this is the

    next day is bright. So if you take a next day is bright. So if you take a next
    day is bright. So if you take a

    look at every element of this attention look at every element of this attention
    look at every element of this attention

    matrix, it essentially captures the matrix, it essentially captures the matrix,
    it essentially captures the

    attention score between the row and the attention score between the row and the
    attention score between the row and the

    column. So if I''m looking at bright, column. So if I''m looking at bright, column.
    So if I''m looking at bright,

    this captures the attention between this captures the attention between this captures
    the attention between

    bright and this captures the attention bright and this captures the attention
    bright and this captures the attention

    between bright and next. This captures between bright and next. This captures
    between bright and next. This captures

    the attention between bright and day. the attention between bright and day. the
    attention between bright and day.

    This captures the attention between This captures the attention between This captures
    the attention between

    bright and is. And this captures the bright and is. And this captures the bright
    and is. And this captures the

    attention between bright and bright. attention between bright and bright. attention
    between bright and bright.

    That''s my attention scores matrix. This That''s my attention scores matrix. This
    That''s my attention scores matrix. This

    is the link between my input vectors and is the link between my input vectors
    and is the link between my input vectors and

    the context vectors. the context vectors. the context vectors.

    Once I get my attention score matrix, I Once I get my attention score matrix,
    I Once I get my attention score matrix, I

    want to be able to make quantitative want to be able to make quantitative want
    to be able to make quantitative

    statements like if I''m looking at statements like if I''m looking at'
  concept_slugs:
  - autoregressive-vs-diffusion
- idx: 5
  start_sec: 259.84
  end_sec: 310.24
  text: 'statements like if I''m looking at

    bright, bright, bright,

    I want to make statements like give 10% I want to make statements like give 10%
    I want to make statements like give 10%

    attention to the, give 20% attention to attention to the, give 20% attention to
    attention to the, give 20% attention to

    next, give 40% attention to day, give next, give 40% attention to day, give next,
    give 40% attention to day, give

    30% or give 20% attention to is and give 30% or give 20% attention to is and give
    30% or give 20% attention to is and give

    the remaining 10% to bright. So what I the remaining 10% to bright. So what I
    the remaining 10% to bright. So what I

    want is I want all of these to sum up to want is I want all of these to sum up
    to want is I want all of these to sum up to

    one so I can make these probabilistic one so I can make these probabilistic one
    so I can make these probabilistic

    statements. So I take my attention score statements. So I take my attention score
    statements. So I take my attention score

    matrix and I apply softmax to it so that matrix and I apply softmax to it so that
    matrix and I apply softmax to it so that

    all of the rows will sum up to one. So all of the rows will sum up to one. So
    all of the rows will sum up to one. So

    then if I look at the fifth row I can then if I look at the fifth row I can then
    if I look at the fifth row I can

    say that give 10% importance to the give say that give 10% importance to the give
    say that give 10% importance to the give

    5% importance to next give 10% 5% importance to next give 10% 5% importance to
    next give 10%

    importance to is for day give 25% importance to is for day give 25% importance
    to is for day give 25%

    importance to is and give 5% importance importance to is and give 5% importance
    importance to is and give 5% importance

    to or give 50% importance to bright. to or give 50% importance to bright.'
  concept_slugs:
  - autoregressive-vs-diffusion
- idx: 6
  start_sec: 310.24
  end_sec: 348.56
  text: 'to or give 50% importance to bright.

    Um there is also the scaling by square Um there is also the scaling by square
    Um there is also the scaling by square

    root of this square root of keys root of this square root of keys root of this
    square root of keys

    dimension which we do to make sure that dimension which we do to make sure that
    dimension which we do to make sure that

    the variance of the queries and keys the variance of the queries and keys the
    variance of the queries and keys

    transpose does not grow a lot. So once transpose does not grow a lot. So once
    transpose does not grow a lot. So once

    you do this operation you have these you do this operation you have these you
    do this operation you have these

    attention weights right but I just have attention weights right but I just have
    attention weights right but I just have

    these attention weights which are these attention weights which are these attention
    weights which are

    percentages of how much attention needs percentages of how much attention needs
    percentages of how much attention needs

    to be given to every token. I again need to be given to every token. I again need
    to be given to every token. I again need

    to multiply my input vector somehow with to multiply my input vector somehow with
    to multiply my input vector somehow with

    these proportions. Right? So this value these proportions. Right? So this value
    these proportions. Right? So this value

    until now I have used my queries matrix until now I have used my queries matrix
    until now I have used my queries matrix

    and I''ve used my keys matrix. I have not and I''ve used my keys matrix. I have
    not and I''ve used my keys matrix. I have not

    used my values matrix anywhere. So what used my values matrix anywhere. So what
    used my values matrix anywhere. So what

    we do in the last step is that we take we do in the last step is that we take
    we do in the last step is that we take

    this attention weight matrix and we this attention weight matrix and we this attention
    weight matrix and we

    multiply it with the value matrix and multiply it with the value matrix and'
  concept_slugs:
  - autoregressive-vs-diffusion
- idx: 7
  start_sec: 348.56
  end_sec: 405.67
  text: 'multiply it with the value matrix and

    this gives me my context vector matrix. this gives me my context vector matrix.
    this gives me my context vector matrix.

    That''s my final output from the That''s my final output from the That''s my final
    output from the

    attention block. Now every vector every attention block. Now every vector every
    attention block. Now every vector every

    row in this context vector matrix. row in this context vector matrix. row in this
    context vector matrix.

    So this is the next day is bright. So So this is the next day is bright. So So
    this is the next day is bright. So

    let''s see how we go from the input how let''s see how we go from the input how
    let''s see how we go from the input how

    we go from the input vector to a context we go from the input vector to a context
    we go from the input vector to a context

    vector. Right? So I''m going to take vector. Right? So I''m going to take vector.
    Right? So I''m going to take

    this next as my query. This is my input this next as my query. This is my input
    this next as my query. This is my input

    vector u or these are my attention vector u or these are my attention vector u
    or these are my attention

    weights for next and this is my um weights for next and this is my um weights
    for next and this is my um

    yeah this is my input vector for next. yeah this is my input vector for next.
    yeah this is my input vector for next.

    Right? So what I''ll do is that I know Right? So what I''ll do is that I know
    Right? So what I''ll do is that I know

    that when I''m looking at next I need to that when I''m looking at next I need
    to that when I''m looking at next I need to

    give 10% attention to the 50% to next give 10% attention to the 50% to next give
    10% attention to the 50% to next

    20% to day 10% to is and 10% to bright. 20% to day 10% to is and 10% to bright.
    20% to day 10% to is and 10% to bright.

    So what I''ll do is that I''ll take the'
  concept_slugs:
  - autoregressive-vs-diffusion
- idx: 8
  start_sec: 405.67
  end_sec: 457.759
  text: 'So what I''ll do is that I''ll take the So what I''ll do is that I''ll take
    the

    values vector for each of these and values vector for each of these and values
    vector for each of these and

    multiply it with the appropriate ratio. multiply it with the appropriate ratio.
    multiply it with the appropriate ratio.

    So I''ll take the vector for the I''ll So I''ll take the vector for the I''ll
    So I''ll take the vector for the I''ll

    multiply it with multiply it with multiply it with

    0.1. I''ll take the vector for next I''ll 0.1. I''ll take the vector for next
    I''ll 0.1. I''ll take the vector for next I''ll

    multiply it with 0.5. I''ll take the multiply it with 0.5. I''ll take the multiply
    it with 0.5. I''ll take the

    vector for day I''ll multiply it with 2. vector for day I''ll multiply it with
    2. vector for day I''ll multiply it with 2.

    I''ll take the vector for is I''ll I''ll take the vector for is I''ll I''ll take
    the vector for is I''ll

    multiply it with 0.1. I''ll take the multiply it with 0.1. I''ll take the multiply
    it with 0.1. I''ll take the

    vector for bright I''ll multiply it with vector for bright I''ll multiply it with
    vector for bright I''ll multiply it with

    0.1. Essentially what we are doing is 0.1. Essentially what we are doing is 0.1.
    Essentially what we are doing is

    that I''m doing a weighted sum based on that I''m doing a weighted sum based on
    that I''m doing a weighted sum based on

    the relative importance. Right? So if the relative importance. Right? So if the
    relative importance. Right? So if

    this is my input vector for next right this is my input vector for next right
    this is my input vector for next right

    and uh these are my input vectors for and uh these are my input vectors for and
    uh these are my input vectors for

    the the the

    day day day

    is and bright. is and bright. is and bright.

    This next input vector has no This next input vector has no This next input vector
    has no

    information about the rel relative information about the rel relative information
    about the rel relative

    tokens. But now what I''m saying is that tokens. But now what I''m saying is that'
  concept_slugs:
  - autoregressive-vs-diffusion
- idx: 9
  start_sec: 457.759
  end_sec: 510.95
  text: 'tokens. But now what I''m saying is that

    when we look at next I have information when we look at next I have information
    when we look at next I have information

    of how next relates to the other tokens. of how next relates to the other tokens.
    of how next relates to the other tokens.

    I have information that when you are I have information that when you are I have
    information that when you are

    looking at next give 10% attention to looking at next give 10% attention to looking
    at next give 10% attention to

    the so give 10% attention to the the so give 10% attention to the the so give
    10% attention to the

    give 50% attention to next give 50% give 50% attention to next give 50% give 50%
    attention to next give 50%

    attention to next give 20% attention to attention to next give 20% attention to
    attention to next give 20% attention to

    day give 10% attention to is and 10% day give 10% attention to is and 10% day
    give 10% attention to is and 10%

    attention to bright and then I''ll add attention to bright and then I''ll add
    attention to bright and then I''ll add

    all these red vectors together that all these red vectors together that all these
    red vectors together that

    gives me my context vector for next you gives me my context vector for next you
    gives me my context vector for next you

    see this context vector is much more see this context vector is much more see
    this context vector is much more

    richer than the input vector because now richer than the input vector because
    now richer than the input vector because now

    it contains the relative importance of it contains the relative importance of
    it contains the relative importance of

    how next relates to its neighbors around how next relates to its neighbors around
    how next relates to its neighbors around

    it. Why is this important? Because as we it. Why is this important? Because as
    we it. Why is this important? Because as we

    saw with the Harry Potter example, saw with the Harry Potter example, saw with
    the Harry Potter example,

    right? If you have Harry lived at right? If you have Harry lived at right? If
    you have Harry lived at

    Hogwarts and he'
  concept_slugs:
  - autoregressive-vs-diffusion
- idx: 10
  start_sec: 510.95
  end_sec: 570.08
  text: 'Hogwarts and he Hogwarts and he

    now I have encoded how he relates to now I have encoded how he relates to now
    I have encoded how he relates to

    these different tokens. these different tokens. these different tokens.

    And when my model is trained, the And when my model is trained, the And when my
    model is trained, the

    attention scores between he and Harry attention scores between he and Harry attention
    scores between he and Harry

    will be the highest. will be the highest. will be the highest.

    That is what I''m essentially aiming for That is what I''m essentially aiming
    for That is what I''m essentially aiming for

    here. The attention score between he and here. The attention score between he
    and here. The attention score between he and

    Harry will be the highest. So this Harry will be the highest. So this Harry will
    be the highest. So this

    context vector, this context vectors are context vector, this context vectors
    are context vector, this context vectors are

    much more richer than the input vectors. much more richer than the input vectors.
    much more richer than the input vectors.

    That''s the main goal of the attention That''s the main goal of the attention
    That''s the main goal of the attention

    mechanism. Now there is one subtle thing mechanism. Now there is one subtle thing
    mechanism. Now there is one subtle thing

    which I want all of you to pay attention which I want all of you to pay attention
    which I want all of you to pay attention

    to. If you took if you took a closer to. If you took if you took a closer to.
    If you took if you took a closer

    look at this right, look at this right, look at this right,

    remember that we are doing a next token remember that we are doing a next token
    remember that we are doing a next token

    prediction task. Let me remove this. We prediction task. Let me remove this. We
    prediction task. Let me remove this. We

    are doing the next token prediction are doing the next token prediction are doing
    the next token prediction

    task, right? So, let me remove all of this green let me remove all of this green

    uh symbols here. So, we are doing the next token'
  concept_slugs:
  - autoregressive-vs-diffusion
- idx: 11
  start_sec: 570.08
  end_sec: 611.519
  text: 'So, we are doing the next token

    prediction task here. Um, so if next is prediction task here. Um, so if next is
    prediction task here. Um, so if next is

    the input, I want to predict what comes the input, I want to predict what comes
    the input, I want to predict what comes

    next, right? If day should be the next. next, right? If day should be the next.
    next, right? If day should be the next.

    So ideally during the next token So ideally during the next token So ideally during
    the next token

    prediction task if I''m looking at a prediction task if I''m looking at a prediction
    task if I''m looking at a

    particular token I should not have particular token I should not have particular
    token I should not have

    access to tokens which come after this access to tokens which come after this
    access to tokens which come after this

    token. So there is really no point in token. So there is really no point in token.
    So there is really no point in

    finding the attention score between next finding the attention score between next
    finding the attention score between next

    and day next and is and next and bright. and day next and is and next and bright.
    and day next and is and next and bright.

    There is no point in finding these There is no point in finding these There is
    no point in finding these

    attention scores because I cannot peak attention scores because I cannot peak
    attention scores because I cannot peak

    into the future. Similarly for the there into the future. Similarly for the there
    into the future. Similarly for the there

    is no use in finding the attention score is no use in finding the attention score
    is no use in finding the attention score

    between next day is bright. For day no between next day is bright. For day no
    between next day is bright. For day no

    need of finding the attention score need of finding the attention score need of
    finding the attention score

    between is and bright. And for is there between is and bright. And for is there
    between is and bright. And for is there

    is no need of finding the attention is no need of finding the attention'
  concept_slugs:
  - autoregressive-vs-diffusion
- idx: 12
  start_sec: 611.519
  end_sec: 659.36
  text: 'is no need of finding the attention

    score between is and bright. But for score between is and bright. But for score
    between is and bright. But for

    bright it''s fine because all the other bright it''s fine because all the other
    bright it''s fine because all the other

    tokens come before it. So essentially we tokens come before it. So essentially
    we tokens come before it. So essentially we

    only need the attention scores which I''m only need the attention scores which
    I''m only need the attention scores which I''m

    marking right now in this triangle. We marking right now in this triangle. We
    marking right now in this triangle. We

    only need these attention scores. Why? only need these attention scores. Why?
    only need these attention scores. Why?

    Because if you take again if you take a Because if you take again if you take
    a Because if you take again if you take a

    look at our Harry Potter example, right? look at our Harry Potter example, right?
    look at our Harry Potter example, right?

    Uh I keep missing that example. If you Uh I keep missing that example. If you
    Uh I keep missing that example. If you

    take a look at Yeah, if you take a look at the Harry Yeah, if you take a look
    at the Harry

    Potter example, if I want to predict the Potter example, if I want to predict
    the Potter example, if I want to predict the

    next token after he, I will not have next token after he, I will not have next
    token after he, I will not have

    access to what tokens come after, right? access to what tokens come after, right?
    access to what tokens come after, right?

    So, what''s the point of finding the So, what''s the point of finding the So,
    what''s the point of finding the

    attention scores here? I only want to attention scores here? I only want to attention
    scores here? I only want to

    find the attention scores between a find the attention scores between a find the
    attention scores between a

    token and what come before it. So, token and what come before it. So, token and
    what come before it. So,

    essentially, I only need to find the essentially, I only need to find the'
  concept_slugs:
  - autoregressive-vs-diffusion
- idx: 13
  start_sec: 659.36
  end_sec: 702.949
  text: 'essentially, I only need to find the

    attention scores of what comes in this attention scores of what comes in this
    attention scores of what comes in this

    triangle. I don''t need these attention triangle. I don''t need these attention
    triangle. I don''t need these attention

    scores. So what I''m doing right now it''s scores. So what I''m doing right now
    it''s scores. So what I''m doing right now it''s

    called as causal attention. Causal called as causal attention. Causal called as
    causal attention. Causal

    attention essentially means that we attention essentially means that we attention
    essentially means that we

    cannot peak into the future. We only cannot peak into the future. We only cannot
    peak into the future. We only

    need the attention scores of what comes need the attention scores of what comes
    need the attention scores of what comes

    in the past. This is one major in the past. This is one major in the past. This
    is one major

    difference between standard or auto difference between standard or auto difference
    between standard or auto

    reggressive diff auto reggressive models reggressive diff auto reggressive models
    reggressive diff auto reggressive models

    and diffusion models because in and diffusion models because in and diffusion
    models because in

    diffusion models we can peak into the diffusion models we can peak into the diffusion
    models we can peak into the

    future. We''ll come in we''ll come to that future. We''ll come in we''ll come
    to that future. We''ll come in we''ll come to that

    because diffusion models are because diffusion models are because diffusion models
    are

    biirectional. They look at sequences biirectional. They look at sequences biirectional.
    They look at sequences

    from both ways. But in causal attention from both ways. But in causal attention
    from both ways. But in causal attention

    we cannot peak into the future. we we we cannot peak into the future. we we we
    cannot peak into the future. we we

    have to have this attention mask. So have to have this attention mask. So have
    to have this attention mask. So

    what is done in practice is that when we what is done in practice is that when
    we what is done in practice is that when we

    construct these attention matrix all construct these attention matrix all construct
    these attention matrix all

    these attention score values are'
  concept_slugs:
  - autoregressive-vs-diffusion
- idx: 14
  start_sec: 702.949
  end_sec: 748.79
  text: 'these attention score values are these attention score values are

    essentially set to zero because we don''t essentially set to zero because we don''t
    essentially set to zero because we don''t

    need them anyways. So they don''t play a need them anyways. So they don''t play
    a need them anyways. So they don''t play a

    role in any future calculations which we role in any future calculations which
    we role in any future calculations which we

    do right here what I just showed right do right here what I just showed right
    do right here what I just showed right

    now is single head attention but the now is single head attention but the now
    is single head attention but the

    actual uh actual uh actual uh

    attention mechanism which is implemented attention mechanism which is implemented
    attention mechanism which is implemented

    in the transformer architecture is in the transformer architecture is in the transformer
    architecture is

    something which is called as multi head something which is called as multi head
    something which is called as multi head

    attention. So I''m not going into multi attention. So I''m not going into multi
    attention. So I''m not going into multi

    head attention right now because that''s head attention right now because that''s
    head attention right now because that''s

    not needed. If you want to understand not needed. If you want to understand not
    needed. If you want to understand

    multi head attention, I''ll share the multi head attention, I''ll share the multi
    head attention, I''ll share the

    link in the uh description or you can link in the uh description or you can link
    in the uh description or you can

    even take a look at this build LLM from even take a look at this build LLM from
    even take a look at this build LLM from

    scratch series to understand multi head scratch series to understand multi head
    scratch series to understand multi head

    attention. To understand diffusion attention. To understand diffusion attention.
    To understand diffusion

    models, you need to understand the models, you need to understand the models,
    you need to understand the

    attention mechanism just because you attention mechanism just because you attention
    mechanism just because you

    need to understand that the causal need to understand that the causal need to
    understand that the causal

    attention mass does not exist for'
  concept_slugs:
  - autoregressive-vs-diffusion
- idx: 15
  start_sec: 748.79
  end_sec: 799.04
  text: 'attention mass does not exist for attention mass does not exist for

    diffusion models. In multi head diffusion models. In multi head diffusion models.
    In multi head

    attention what''s actually done is that attention what''s actually done is that
    attention what''s actually done is that

    u these trainable matrices for queries u these trainable matrices for queries
    u these trainable matrices for queries

    keys and values are split across keys and values are split across keys and values
    are split across

    different heads. So every head different heads. So every head different heads.
    So every head

    essentially captures a different essentially captures a different essentially
    captures a different

    perspective and we have the attention perspective and we have the attention perspective
    and we have the attention

    score matrices for different heads. So score matrices for different heads. So
    score matrices for different heads. So

    different heads might have uh different different heads might have uh different
    different heads might have uh different

    attention scores and then we pull these attention scores and then we pull these
    attention scores and then we pull these

    attention scores together to get a final attention scores together to get a final
    attention scores together to get a final

    attention score. It just leads to a attention score. It just leads to a attention
    score. It just leads to a

    richer understanding of language because richer understanding of language because
    richer understanding of language because

    in a sentence we can capture multiple in a sentence we can capture multiple in
    a sentence we can capture multiple

    perspectives. perspectives. perspectives.

    That''s the attention block. So until now That''s the attention block. So until
    now That''s the attention block. So until now

    what you are seeing over here is that what you are seeing over here is that what
    you are seeing over here is that

    when we come out of the layer norm and when we come out of the layer norm and
    when we come out of the layer norm and

    when we pass through the multi so why is when we pass through the multi so why
    is when we pass through the multi so why is

    it called masked mask? Because we have it called masked mask? Because we have
    it called masked mask? Because we have

    that causal attention mask here right we that causal attention mask here right
    we'
  concept_slugs:
  - autoregressive-vs-diffusion
- idx: 16
  start_sec: 799.04
  end_sec: 841.269
  text: 'that causal attention mask here right we

    don''t need these attention score so we don''t need these attention score so we
    don''t need these attention score so we

    put them to zero. That''s why it''s called put them to zero. That''s why it''s
    called put them to zero. That''s why it''s called

    as a mask. as a mask. as a mask.

    So once we come out of the multi head So once we come out of the multi head So
    once we come out of the multi head

    attention block I have now see I have attention block I have now see I have attention
    block I have now see I have

    called it a context vector because now called it a context vector because now
    called it a context vector because now

    every vector is very rich. Um it is now every vector is very rich. Um it is now
    every vector is very rich. Um it is now

    a context vector because now every a context vector because now every a context
    vector because now every

    vector contains in every token contains vector contains in every token contains
    vector contains in every token contains

    information of its neighbors also. Okay information of its neighbors also. Okay
    information of its neighbors also. Okay

    so we have this so we have come out of so we have this so we have come out of
    so we have this so we have come out of

    the attention block right now and now the attention block right now and now the
    attention block right now and now

    let''s move to the next aspects which is let''s move to the next aspects which
    is let''s move to the next aspects which is

    the dropout layer. The layer norm two the dropout layer. The layer norm two the
    dropout layer. The layer norm two

    feed forward neural network and another feed forward neural network and another
    feed forward neural network and another

    dropout layer. But I hope all of you dropout layer. But I hope all of you dropout
    layer. But I hope all of you

    have understood the basics of the have understood the basics of the have understood
    the basics of the

    attention mechanism in this short uh attention mechanism in this short uh attention
    mechanism in this short uh

    explanation which I''ve tried to give'
  concept_slugs:
  - autoregressive-vs-diffusion
- idx: 17
  start_sec: 841.269
  end_sec: 867.76
  text: 'explanation which I''ve tried to give explanation which I''ve tried to give

    you. If you want to go and drill down you. If you want to go and drill down you.
    If you want to go and drill down

    into the details of matrix into the details of matrix into the details of matrix

    multiplications and how matrix multiplications and how matrix multiplications
    and how matrix

    dimensions make sense, why do we divide dimensions make sense, why do we divide
    dimensions make sense, why do we divide

    by the square root of keys dimension by the square root of keys dimension by the
    square root of keys dimension

    etc. you need to watch the build lm from etc. you need to watch the build lm from
    etc. you need to watch the build lm from

    scratch series. But I have tried to give scratch series. But I have tried to give
    scratch series. But I have tried to give

    you enough of an overview over here so you enough of an overview over here so
    you enough of an overview over here so

    you don''t feel that I don''t understand you don''t feel that I don''t understand
    you don''t feel that I don''t understand

    the attention mechanism. So I won''t the attention mechanism. So I won''t the
    attention mechanism. So I won''t

    understand this lecture. Okay.'
  concept_slugs:
  - autoregressive-vs-diffusion
---
# Lecture 9: Auto Regressive Models (ARM) Attention Block

See the structured chunks above.
