---
course_slug: diffusion-lm-vizuara
idx: 11
title: 'Lecture 10: Auto Regressive Models (ARM) Output and Loss Blocks'
video_url: https://www.youtube.com/watch?v=2ekKz5pjR8k
duration_sec: null
chunks:
- idx: 0
  start_sec: 3.03
  end_sec: 55.28
  text: 'So once we come out of the attention So once we come out of the attention

    block, we have a dropout layer. Uh let block, we have a dropout layer. Uh let
    block, we have a dropout layer. Uh let

    me me me

    uh make it clean over here. Yeah. So uh make it clean over here. Yeah. So uh make
    it clean over here. Yeah. So

    once we move out of the attention block, once we move out of the attention block,
    once we move out of the attention block,

    we have the dropout layer, then a we have the dropout layer, then a we have the
    dropout layer, then a

    shortcut connection, and then the second shortcut connection, and then the second
    shortcut connection, and then the second

    layer normalization. layer normalization. layer normalization.

    So let''s start looking into this. Right So let''s start looking into this. Right
    So let''s start looking into this. Right

    now we have reached the stage where now we have reached the stage where now we
    have reached the stage where

    input vectors are converted into what input vectors are converted into what input
    vectors are converted into what

    are called as context vectors which are are called as context vectors which are
    are called as context vectors which are

    much more richer in meaning compared to much more richer in meaning compared to
    much more richer in meaning compared to

    the input vector since they also contain the input vector since they also contain
    the input vector since they also contain

    information of how every token is information of how every token is information
    of how every token is

    related to its neighbors. related to its neighbors. related to its neighbors.

    Once we have the context vectors we have Once we have the context vectors we have
    Once we have the context vectors we have

    a dropout layer. The concept of dropout a dropout layer. The concept of dropout
    a dropout layer. The concept of dropout

    is borrowed from deep learning where we is borrowed from deep learning where we
    is borrowed from deep learning where we

    randomly set some of the elements of randomly set some of the elements of randomly
    set some of the elements of

    these vectors to zero. And the reason these vectors to zero. And the reason'
  concept_slugs:
  - autoregressive-vs-diffusion
- idx: 1
  start_sec: 55.28
  end_sec: 97.84
  text: 'these vectors to zero. And the reason

    dropout is implemented is to improve the dropout is implemented is to improve
    the dropout is implemented is to improve the

    generalization performance. I always generalization performance. I always generalization
    performance. I always

    think of it like a group project. If think of it like a group project. If think
    of it like a group project. If

    there are four team members, right? there are four team members, right? there
    are four team members, right?

    There are always those two people who There are always those two people who There
    are always those two people who

    don''t do anything. How do you prevent don''t do anything. How do you prevent
    don''t do anything. How do you prevent

    this? Well, if one of the person who is this? Well, if one of the person who is
    this? Well, if one of the person who is

    doing all the work suddenly is sick and doing all the work suddenly is sick and
    doing all the work suddenly is sick and

    is not able to work, the other person is not able to work, the other person is
    not able to work, the other person

    has to pick up the slack. has to pick up the slack. has to pick up the slack.

    That''s a similar concept of dropout. If That''s a similar concept of dropout.
    If That''s a similar concept of dropout. If

    there are some lazy neurons, such as if there are some lazy neurons, such as if
    there are some lazy neurons, such as if

    this neuron is lazy and is not learning this neuron is lazy and is not learning
    this neuron is lazy and is not learning

    anything, suddenly if the neighboring anything, suddenly if the neighboring anything,
    suddenly if the neighboring

    neurons are switched off during one neurons are switched off during one neurons
    are switched off during one

    dropout forward pass, this neuron has no dropout forward pass, this neuron has
    no dropout forward pass, this neuron has no

    other option but to pick up the slack other option but to pick up the slack other
    option but to pick up the slack

    and to learn some weights that improves and to learn some weights that improves
    and to learn some weights that improves

    the generalization performance, right? the generalization performance, right?'
  concept_slugs:
  - autoregressive-vs-diffusion
- idx: 2
  start_sec: 97.84
  end_sec: 146.48
  text: 'the generalization performance, right?

    U so after dropout we again have these U so after dropout we again have these
    U so after dropout we again have these

    context vectors. Now take a look at the context vectors. Now take a look at the
    context vectors. Now take a look at the

    dimension here. We started with an dimension here. We started with an dimension
    here. We started with an

    embedding size of 768. And generally in embedding size of 768. And generally in
    embedding size of 768. And generally in

    many modern language models this many modern language models this many modern
    language models this

    embedding size is retained across the embedding size is retained across the embedding
    size is retained across the

    different layers. Right? So every token different layers. Right? So every token
    different layers. Right? So every token

    has an embedding size of 768. Layer has an embedding size of 768. Layer has an
    embedding size of 768. Layer

    normalization preserves it. The normalization preserves it. The normalization
    preserves it. The

    attention block preserves it. Dropout attention block preserves it. Dropout attention
    block preserves it. Dropout

    preserves it. Now once we come out of preserves it. Now once we come out of preserves
    it. Now once we come out of

    the first dropout right there is this the first dropout right there is this the
    first dropout right there is this

    block which is a plus sign here and block which is a plus sign here and block
    which is a plus sign here and

    that''s a shortcut connection. What it that''s a shortcut connection. What it
    that''s a shortcut connection. What it

    basically means is that we do a basically means is that we do a basically means
    is that we do a

    summation of the output from the dropout summation of the output from the dropout
    summation of the output from the dropout

    and the input from here and that goes to and the input from here and that goes
    to and the input from here and that goes to

    the second layer normalization. The the second layer normalization. The the second
    layer normalization. The

    reason this summation is done because reason this summation is done because reason
    this summation is done because

    we want to avoid the problem of we want to avoid the problem of'
  concept_slugs:
  - autoregressive-vs-diffusion
- idx: 3
  start_sec: 146.48
  end_sec: 203.75
  text: 'we want to avoid the problem of

    vanishing gradients. vanishing gradients. vanishing gradients.

    The thing is if multiple gradients The thing is if multiple gradients The thing
    is if multiple gradients

    directly multiply with each other by the directly multiply with each other by
    the directly multiply with each other by the

    time we back propagate and reach towards time we back propagate and reach towards
    time we back propagate and reach towards

    the initial layers the gradient might the initial layers the gradient might the
    initial layers the gradient might

    vanish learning stagnates. To prevent vanish learning stagnates. To prevent vanish
    learning stagnates. To prevent

    this we give an alternative path for the this we give an alternative path for
    the this we give an alternative path for the

    gradient to flow and this prevents uh gradient to flow and this prevents uh gradient
    to flow and this prevents uh

    gradient gradient gradient

    um um um

    diminishing problem or the vanishing diminishing problem or the vanishing diminishing
    problem or the vanishing

    gradient problem and it makes sure gradient problem and it makes sure gradient
    problem and it makes sure

    learning does not stagnate. You''ll see a learning does not stagnate. You''ll
    see a learning does not stagnate. You''ll see a

    shortcut connection here and you''ll see shortcut connection here and you''ll
    see shortcut connection here and you''ll see

    it here also. For this shortcut it here also. For this shortcut it here also.
    For this shortcut

    connection, we add this input. connection, we add this input. connection, we add
    this input.

    Let me reconnect my board. Let me reconnect my board. Let me reconnect my board.

    For the second shortcut connection, we For the second shortcut connection, we
    For the second shortcut connection, we

    add this input with the output from this add this input with the output from this
    add this input with the output from this

    dropout. dropout. dropout.

    Now once we come out of this shortcut Now once we come out of this shortcut Now
    once we come out of this shortcut

    connection, the next place where we go connection, the next place where we go
    connection, the next place where we go

    to is the second layer normalization. to is the second layer normalization. to
    is the second layer normalization.

    So we have to go from here to now here'
  concept_slugs:
  - autoregressive-vs-diffusion
- idx: 4
  start_sec: 203.75
  end_sec: 248.56
  text: 'So we have to go from here to now here So we have to go from here to now
    here

    which is the second layer normalization. which is the second layer normalization.
    which is the second layer normalization.

    And the second layer normalization And the second layer normalization And the
    second layer normalization

    actually works in a very similar way actually works in a very similar way actually
    works in a very similar way

    actually exactly the same way as the actually exactly the same way as the actually
    exactly the same way as the

    first layer normalization where every first layer normalization where every first
    layer normalization where every

    vector we subtract the mean divide by vector we subtract the mean divide by vector
    we subtract the mean divide by

    the square root of variance. So the the square root of variance. So the the square
    root of variance. So the

    resulting vectors have a mean of zero resulting vectors have a mean of zero resulting
    vectors have a mean of zero

    and a variance of one. and a variance of one. and a variance of one.

    Then we have a feed forward neural Then we have a feed forward neural Then we
    have a feed forward neural

    network. That''s essentially an expansion network. That''s essentially an expansion
    network. That''s essentially an expansion

    and a contraction block. So if the these and a contraction block. So if the these
    and a contraction block. So if the these

    are the inputs with dimension 768, we are the inputs with dimension 768, we are
    the inputs with dimension 768, we

    have a hidden layer whose dimensions are have a hidden layer whose dimensions
    are have a hidden layer whose dimensions are

    four times the input dimension and then four times the input dimension and then
    four times the input dimension and then

    we contract it back to the output layer. we contract it back to the output layer.
    we contract it back to the output layer.

    And the output layer has the same And the output layer has the same And the output
    layer has the same

    dimensions as the input which is 768. dimensions as the input which is 768. dimensions
    as the input which is 768.

    The activation layer here which is The activation layer here which is'
  concept_slugs:
  - autoregressive-vs-diffusion
- idx: 5
  start_sec: 248.56
  end_sec: 298.479
  text: 'The activation layer here which is

    generally preferred is JLU activation. generally preferred is JLU activation.
    generally preferred is JLU activation.

    The way it differs from RLU is that uh The way it differs from RLU is that uh
    The way it differs from RLU is that uh

    RLU is this right? So the negative RLU is this right? So the negative RLU is this
    right? So the negative

    entries are fully zero. JLO the negative entries are fully zero. JLO the negative
    entries are fully zero. JLO the negative

    entries are not fully zero but it''s entries are not fully zero but it''s entries
    are not fully zero but it''s

    something like this. something like this. something like this.

    Roughly it looks like this. And this has Roughly it looks like this. And this
    has Roughly it looks like this. And this has

    proven to be a bit better experimentally proven to be a bit better experimentally
    proven to be a bit better experimentally

    compared to RLU when training uh compared to RLU when training uh compared to
    RLU when training uh

    language models. This is a feed forward language models. This is a feed forward
    language models. This is a feed forward

    neural network which again ultimately neural network which again ultimately neural
    network which again ultimately

    preserves the dimension. And then we preserves the dimension. And then we preserves
    the dimension. And then we

    have a dropout layer over here. What have a dropout layer over here. What have
    a dropout layer over here. What

    this dropout layer does is that it again this dropout layer does is that it again
    this dropout layer does is that it again

    masks out entries randomly and puts them masks out entries randomly and puts them
    masks out entries randomly and puts them

    to zero to improve generalization. to zero to improve generalization. to zero
    to improve generalization.

    One thing which you''ll observe One thing which you''ll observe One thing which
    you''ll observe

    throughout the transformer architecture throughout the transformer architecture
    throughout the transformer architecture

    is that there are certain elements from is that there are certain elements from
    is that there are certain elements from

    traditional deep learning which have traditional deep learning which have traditional
    deep learning which have

    been borrowed and which show up been borrowed and which show up'
  concept_slugs:
  - autoregressive-vs-diffusion
- idx: 6
  start_sec: 298.479
  end_sec: 344.88
  text: 'been borrowed and which show up

    repeatedly. So which are these elements? repeatedly. So which are these elements?
    repeatedly. So which are these elements?

    You''ll see that the dropout layer is You''ll see that the dropout layer is You''ll
    see that the dropout layer is

    repeated, the layer normalization is repeated, the layer normalization is repeated,
    the layer normalization is

    repeated and the shortcut connection is repeated and the shortcut connection is
    repeated and the shortcut connection is

    repeated. All of these are not new repeated. All of these are not new repeated.
    All of these are not new

    ideas. They were existing in deep ideas. They were existing in deep ideas. They
    were existing in deep

    learning for a long time. But this learning for a long time. But this learning
    for a long time. But this

    transformer block which stacks all of it transformer block which stacks all of
    it transformer block which stacks all of it

    together is pretty new. together is pretty new. together is pretty new.

    So now once we come out of the second So now once we come out of the second So
    now once we come out of the second

    dropout layer, we have another shortcut dropout layer, we have another shortcut
    dropout layer, we have another shortcut

    connection. And that''s the end of the connection. And that''s the end of the
    connection. And that''s the end of the

    transformer block. Correct? So remember transformer block. Correct? So remember
    transformer block. Correct? So remember

    the input to the transformer block was the input to the transformer block was
    the input to the transformer block was

    these input embeddings which was the these input embeddings which was the these
    input embeddings which was the

    token embedding plus the positional token embedding plus the positional token
    embedding plus the positional

    embedding which size. So every token had embedding which size. So every token
    had embedding which size. So every token had

    a vector size of 768. a vector size of 768. a vector size of 768.

    That was the input to the transformer. That was the input to the transformer.
    That was the input to the transformer.

    The output, this is the input, the The output, this is the input, the The output,
    this is the input, the

    output to the transformer block. The output to the transformer block. The'
  concept_slugs:
  - autoregressive-vs-diffusion
- idx: 7
  start_sec: 344.88
  end_sec: 415.51
  text: 'output to the transformer block. The

    output of the transformer block is this. output of the transformer block is this.
    output of the transformer block is this.

    Again, we have these tokens with the Again, we have these tokens with the Again,
    we have these tokens with the

    dimension of 768. But a number of things dimension of 768. But a number of things
    dimension of 768. But a number of things

    have been changed. Every token now has have been changed. Every token now has
    have been changed. Every token now has

    information of its neighbors which has information of its neighbors which has
    information of its neighbors which has

    been encoded through the multi head been encoded through the multi head been encoded
    through the multi head

    attention mechanism. We have implemented attention mechanism. We have implemented
    attention mechanism. We have implemented

    dropout to prevent general to prevent dropout to prevent general to prevent dropout
    to prevent general to prevent

    overfitting and improve generalization. overfitting and improve generalization.
    overfitting and improve generalization.

    We have imple implemented shortcut We have imple implemented shortcut We have
    imple implemented shortcut

    connections to make sure the vanishing connections to make sure the vanishing
    connections to make sure the vanishing

    gradient problem is not there and the gradient problem is not there and the gradient
    problem is not there and the

    gradients have an alternative path to gradients have an alternative path to gradients
    have an alternative path to

    flow. flow. flow.

    All right. Now one thing which I want to All right. Now one thing which I want
    to All right. Now one thing which I want to

    mention um is that we don''t have one mention um is that we don''t have one mention
    um is that we don''t have one

    transformer block but we have multiple transformer block but we have multiple
    transformer block but we have multiple

    such transformer blocks which are such transformer blocks which are such transformer
    blocks which are

    stacked together. So let me actually try stacked together. So let me actually
    try stacked together. So let me actually try

    to find the mirro board nodes which I to find the mirro board nodes which I to
    find the mirro board nodes which I

    had on this topic. I believe it was called uh I believe it was called uh

    build neural networks from scratch, I'
  concept_slugs:
  - autoregressive-vs-diffusion
- idx: 8
  start_sec: 415.51
  end_sec: 504.4
  text: 'build neural networks from scratch, I build neural networks from scratch,
    I

    think. Let''s see. Or build LLM from think. Let''s see. Or build LLM from think.
    Let''s see. Or build LLM from

    scratch new, I think. So or if I rename it to deepsek or if I rename it to deepsek

    because I think I taught it during because I think I taught it during because
    I think I taught it during

    deepseek version. Yeah, I think it''s called journey of a Yeah, I think it''s
    called journey of a

    token. Let me see. I think these are the notes by Dr. I think these are the notes
    by Dr.

    Shriat. Yeah. So what I want to show you Shriat. Yeah. So what I want to show
    you Shriat. Yeah. So what I want to show you

    over here is that we currently saw one over here is that we currently saw one
    over here is that we currently saw one

    transformer block, right? We saw one transformer block, right? We saw one transformer
    block, right? We saw one

    transformer block. But in language transformer block. But in language transformer
    block. But in language

    modules when they are assembled, there modules when they are assembled, there
    modules when they are assembled, there

    are multiple such transformer blocks are multiple such transformer blocks are
    multiple such transformer blocks

    which are stacked together, right? So which are stacked together, right? So which
    are stacked together, right? So

    although here I have shown although here I have shown although here I have shown

    not here here I have shown one not here here I have shown one not here here I
    have shown one

    transformer block transformer block transformer block

    one transformer block actually there are one transformer block actually there
    are one transformer block actually there are

    multiple such transformer blocks stacked multiple such transformer blocks stacked
    multiple such transformer blocks stacked

    together there might be 12 24 or even together there might be 12 24 or even together
    there might be 12 24 or even

    96. 96. 96.

    So the output of the first transformer So the output of the first transformer
    So the output of the first transformer

    block goes to the second the output of block goes to the second the output of'
  concept_slugs:
  - autoregressive-vs-diffusion
- idx: 9
  start_sec: 504.4
  end_sec: 545.11
  text: 'block goes to the second the output of

    the second goes to the third. The output the second goes to the third. The output
    the second goes to the third. The output

    of the third goes to the fourth to the of the third goes to the fourth to the
    of the third goes to the fourth to the

    fifth and then we come out of the fifth and then we come out of the fifth and
    then we come out of the

    transformer block. So when I say coming transformer block. So when I say coming
    transformer block. So when I say coming

    out of the transformer block, it''s out of the transformer block, it''s out of
    the transformer block, it''s

    actually going through a series of actually going through a series of actually
    going through a series of

    transformer blocks and coming out of it. transformer blocks and coming out of
    it. transformer blocks and coming out of it.

    It''s a huge architecture, right? And It''s a huge architecture, right? And It''s
    a huge architecture, right? And

    that''s what increases the number of that''s what increases the number of that''s
    what increases the number of

    parameters of a language model. parameters of a language model. parameters of
    a language model.

    Okay, once we come out of the Okay, once we come out of the Okay, once we come
    out of the

    transformer block, then we reach the transformer block, then we reach the transformer
    block, then we reach the

    final layer which is the output layer. final layer which is the output layer.
    final layer which is the output layer.

    And in the output layer, there are two And in the output layer, there are two
    And in the output layer, there are two

    things which happen. First we again do a things which happen. First we again do
    a things which happen. First we again do a

    layer normalization which is the same layer normalization which is the same layer
    normalization which is the same

    step as the previous two layer step as the previous two layer step as the previous
    two layer

    normalization. So the output of the normalization. So the output of the normalization.
    So the output of the

    transformer block and remember when I transformer block and remember when I transformer
    block and remember when I

    say transformer block output it''s the'
  concept_slugs:
  - autoregressive-vs-diffusion
- idx: 10
  start_sec: 545.11
  end_sec: 604.0
  text: 'say transformer block output it''s the say transformer block output it''s
    the

    output from those 12 24 or 96 output from those 12 24 or 96 output from those
    12 24 or 96

    transformer blocks that output goes transformer blocks that output goes transformer
    blocks that output goes

    through a layer normalization operation through a layer normalization operation
    through a layer normalization operation

    where again for every vector we subtract where again for every vector we subtract
    where again for every vector we subtract

    the mean and we divide by with the the mean and we divide by with the the mean
    and we divide by with the

    square root of the variance. So for square root of the variance. So for square
    root of the variance. So for

    every vector ultimately we have a mean every vector ultimately we have a mean
    every vector ultimately we have a mean

    of zero and variance equal to one. Um of zero and variance equal to one. Um of
    zero and variance equal to one. Um

    and then once a layer normalization is and then once a layer normalization is
    and then once a layer normalization is

    applied another important concept to applied another important concept to applied
    another important concept to

    note over here is this output head. This note over here is this output head. This
    note over here is this output head. This

    is very important and we need to is very important and we need to is very important
    and we need to

    understand this understand this understand this

    um if we want to um if we want to um if we want to

    understand diffusion language models understand diffusion language models understand
    diffusion language models

    also because this thing also changes also because this thing also changes also
    because this thing also changes

    right. So let''s say this is the output right. So let''s say this is the output
    right. So let''s say this is the output

    u of the layer normalization. We have u of the layer normalization. We have u
    of the layer normalization. We have

    four tokens with 768. Now remember that four tokens with 768. Now remember that
    four tokens with 768. Now remember that

    every every every

    effort effort effort

    moves you right. This has as we have moves you right. This has as we have'
  concept_slugs:
  - autoregressive-vs-diffusion
- idx: 11
  start_sec: 604.0
  end_sec: 661.04
  text: 'moves you right. This has as we have

    seen this is one input sequence but it seen this is one input sequence but it
    seen this is one input sequence but it

    actually has four input output actually has four input output actually has four
    input output

    prediction tasks. Right? Every effort, prediction tasks. Right? Every effort,
    prediction tasks. Right? Every effort,

    every every

    effort moves and and

    every effort every effort every effort

    moves you. Correct? So now these are my moves you. Correct? So now these are my
    moves you. Correct? So now these are my

    input. So this is input one, input two, input. So this is input one, input two,
    input. So this is input one, input two,

    input three, input four and my target. input three, input four and my target.
    input three, input four and my target.

    So I know my targets, right? So target So I know my targets, right? So target
    So I know my targets, right? So target

    one. So if every is the input, I want one. So if every is the input, I want one.
    So if every is the input, I want

    effort to be the output. If I want every effort to be the output. If I want every
    effort to be the output. If I want every

    effort to be the input, I want moves to effort to be the input, I want moves to
    effort to be the input, I want moves to

    be the output. If every effort moves is be the output. If every effort moves is
    be the output. If every effort moves is

    the input, U is the output. And if every the input, U is the output. And if every
    the input, U is the output. And if every

    effort moves you is the input, let''s say effort moves you is the input, let''s
    say effort moves you is the input, let''s say

    forward is the output. This is my forward is the output. This is my forward is
    the output. This is my

    target. But I won''t reach this target target. But I won''t reach this target
    target. But I won''t reach this target

    just when the language model starts just when the language model starts just when
    the language model starts

    training. Right? Initially I would have training. Right? Initially I would have'
  concept_slugs:
  - autoregressive-vs-diffusion
- idx: 12
  start_sec: 661.04
  end_sec: 707.44
  text: 'training. Right? Initially I would have

    some random random guesses. So this is some random random guesses. So this is
    some random random guesses. So this is

    the target and I need to have the target and I need to have the target and I need
    to have

    predictions. predictions. predictions.

    I need to make predictions for every as I need to make predictions for every as
    I need to make predictions for every as

    the input. What is the prediction? For the input. What is the prediction? For
    the input. What is the prediction? For

    every effort as the input, what is the every effort as the input, what is the
    every effort as the input, what is the

    prediction? For every effort moves as prediction? For every effort moves as prediction?
    For every effort moves as

    the input, what''s the prediction? For the input, what''s the prediction? For
    the input, what''s the prediction? For

    every effort moves you, what''s the every effort moves you, what''s the every
    effort moves you, what''s the

    prediction to make these predictions? prediction to make these predictions? prediction
    to make these predictions?

    These predictions will come from my These predictions will come from my These
    predictions will come from my

    vocabulary, right? Let''s say if my vocabulary, right? Let''s say if my vocabulary,
    right? Let''s say if my

    vocabulary has vocabulary has vocabulary has

    100,000 tokens or whatever is my 100,000 tokens or whatever is my 100,000 tokens
    or whatever is my

    vocabulary size, I want to say that from vocabulary size, I want to say that from
    vocabulary size, I want to say that from

    my vocabulary, what''s my prediction my vocabulary, what''s my prediction my vocabulary,
    what''s my prediction

    here? From my vocabulary, what''s my here? From my vocabulary, what''s my here?
    From my vocabulary, what''s my

    prediction? From my vocabulary, what''s prediction? From my vocabulary, what''s
    prediction? From my vocabulary, what''s

    my prediction? From my vocabulary, my prediction? From my vocabulary, my prediction?
    From my vocabulary,

    what''s my prediction? And then I''ll what''s my prediction? And then I''ll what''s
    my prediction? And then I''ll

    calculate the loss between the target calculate the loss between the target calculate
    the loss between the target

    and the predictions. Okay. So, how do we and the predictions. Okay. So, how do
    we'
  concept_slugs:
  - autoregressive-vs-diffusion
- idx: 13
  start_sec: 707.44
  end_sec: 754.15
  text: 'and the predictions. Okay. So, how do we

    get to the predictions? Currently we get to the predictions? Currently we get
    to the predictions? Currently we

    just have uh the output of this just have uh the output of this just have uh the
    output of this

    normalization is four tokens with each normalization is four tokens with each
    normalization is four tokens with each

    of size 768. So we need to somehow of size 768. So we need to somehow of size
    768. So we need to somehow

    transform transform transform

    from a 768 dimensional vector space to a from a 768 dimensional vector space to
    a from a 768 dimensional vector space to a

    vector space of the vocabulary size. So vector space of the vocabulary size. So
    vector space of the vocabulary size. So

    for that what we do is that we multiply for that what we do is that we multiply
    for that what we do is that we multiply

    this with a neural network with this with a neural network with this with a neural
    network with

    dimensions of 768 which is the embedding dimensions of 768 which is the embedding
    dimensions of 768 which is the embedding

    dimension and the number of columns with dimension and the number of columns with
    dimension and the number of columns with

    rows equal to the embedding dimension rows equal to the embedding dimension rows
    equal to the embedding dimension

    and the columns equal to the vocabulary and the columns equal to the vocabulary
    and the columns equal to the vocabulary

    size. Right? So when you do this size. Right? So when you do this size. Right?
    So when you do this

    multiplication you will have a vector multiplication you will have a vector multiplication
    you will have a vector

    you''ll have a matrix with four rows and you''ll have a matrix with four rows
    and you''ll have a matrix with four rows and

    but number of columns will be 50257 but number of columns will be 50257 but number
    of columns will be 50257

    which is the vocabulary size in this which is the vocabulary size in this which
    is the vocabulary size in this

    case. It can be 100,000 also whatever case. It can be 100,000 also whatever case.
    It can be 100,000 also whatever

    that''s the vocabulary size which will be'
  concept_slugs:
  - autoregressive-vs-diffusion
- idx: 14
  start_sec: 754.15
  end_sec: 821.19
  text: 'that''s the vocabulary size which will be that''s the vocabulary size which
    will be

    the number of columns. the number of columns. the number of columns.

    So you have something like every effort

    moves U and then for every token you moves U and then for every token you moves
    U and then for every token you

    have a vector which is of the size of have a vector which is of the size of have
    a vector which is of the size of

    50257. And now what I need to do is that And now what I need to do is that

    all I need to do is that I just need to all I need to do is that I just need to
    all I need to do is that I just need to

    look at these values and I need to see I look at these values and I need to see
    I look at these values and I need to see I

    need to first convert it into a vector need to first convert it into a vector
    need to first convert it into a vector

    of probabilities. So what I''ll do is of probabilities. So what I''ll do is of
    probabilities. So what I''ll do is

    that I''ll take these values and I''ll that I''ll take these values and I''ll
    that I''ll take these values and I''ll

    apply a softmax layer on top of it. apply a softmax layer on top of it. apply
    a softmax layer on top of it.

    Right? So uh what I''ll do is that I''ll take these what I''ll do is that I''ll
    take these

    values values values

    or I''ll take the each vector and I''ll or I''ll take the each vector and I''ll
    or I''ll take the each vector and I''ll

    apply soft max on top of this vector. apply soft max on top of this vector. apply
    soft max on top of this vector.

    So let me show that I apply soft max. So So let me show that I apply soft max.
    So So let me show that I apply soft max. So

    what soft max does is that every every what soft max does is that every every
    what soft max does is that every every

    vector it will make sure that each value'
  concept_slugs:
  - autoregressive-vs-diffusion
- idx: 15
  start_sec: 821.19
  end_sec: 876.8
  text: 'vector it will make sure that each value vector it will make sure that each
    value

    lies between 0 to one and they sum up to lies between 0 to one and they sum up
    to lies between 0 to one and they sum up to

    one. Okay. And now what I do is that I just Okay. And now what I do is that I
    just

    have to for every for every as the input have to for every for every as the input
    have to for every for every as the input

    if I want to see what''s the predicted if I want to see what''s the predicted
    if I want to see what''s the predicted

    output I just look at that highest output I just look at that highest output I
    just look at that highest

    probability token here. So if token ID probability token here. So if token ID
    probability token here. So if token ID

    number 13 has the highest probability number 13 has the highest probability number
    13 has the highest probability

    that will be my prediction here. Maybe that will be my prediction here. Maybe
    that will be my prediction here. Maybe

    that is finger. that is finger. that is finger.

    Then I look at effort right and I look Then I look at effort right and I look
    Then I look at effort right and I look

    at this vector with length 50257. That''s at this vector with length 50257. That''s
    at this vector with length 50257. That''s

    my vocabulary size. and I look at that my vocabulary size. and I look at that
    my vocabulary size. and I look at that

    token ID with the maximum probability. token ID with the maximum probability.
    token ID with the maximum probability.

    If that''s token ID number 500, let''s say If that''s token ID number 500, let''s
    say If that''s token ID number 500, let''s say

    that''s flower again for moves, let''s say token ID again for moves, let''s say
    token ID

    number one has maximum probability. So number one has maximum probability. So
    number one has maximum probability. So

    that''s a and then for you I look at that''s a and then for you I look at that''s
    a and then for you I look at

    maybe token ID number 40,000 maybe token ID number 40,000'
  concept_slugs:
  - autoregressive-vs-diffusion
- idx: 16
  start_sec: 876.8
  end_sec: 934.079
  text: 'maybe token ID number 40,000

    which is a boy So these are my predictions now and then So these are my predictions
    now and then

    I''ll find the loss function between the I''ll find the loss function between
    the I''ll find the loss function between the

    targets and my predictions right this is targets and my predictions right this
    is targets and my predictions right this is

    how you this is how you calculate the how you this is how you calculate the how
    you this is how you calculate the

    predictions and then you find the loss predictions and then you find the loss
    predictions and then you find the loss

    that''s the next token prediction task at that''s the next token prediction task
    at that''s the next token prediction task at

    so if you see for every input token all so if you see for every input token all
    so if you see for every input token all

    I''m doing is just predicting the next I''m doing is just predicting the next
    I''m doing is just predicting the next

    token with the highest probability as we token with the highest probability as
    we token with the highest probability as we

    do multiple layers of back propagation do multiple layers of back propagation
    do multiple layers of back propagation

    as the language model trains as we have as the language model trains as we have
    as the language model trains as we have

    seen over Um yeah, as we do multiple layers of Um yeah, as we do multiple layers
    of

    back propagation, right, the language back propagation, right, the language back
    propagation, right, the language

    model will start to get better and model will start to get better and model will
    start to get better and

    better and better. And as the language better and better. And as the language
    better and better. And as the language

    model continues to get better and better model continues to get better and better
    model continues to get better and better

    and better, the target and the and better, the target and the and better, the
    target and the

    predictions will start to approximate predictions will start to approximate predictions
    will start to approximate

    each other. As the target and the each other. As the target and the'
  concept_slugs:
  - autoregressive-vs-diffusion
- idx: 17
  start_sec: 934.079
  end_sec: 987.99
  text: 'each other. As the target and the

    prediction start to approximate each prediction start to approximate each prediction
    start to approximate each

    other, what will happen is that the other, what will happen is that the other,
    what will happen is that the

    probability the true probability probability the true probability probability
    the true probability

    distribution distribution distribution

    uh or the predicted probability uh or the predicted probability uh or the predicted
    probability

    distribution will start matching the distribution will start matching the distribution
    will start matching the

    true probability distribution true probability distribution true probability distribution

    as training proceeds for a large as training proceeds for a large as training
    proceeds for a large

    duration of time. duration of time. duration of time.

    That''s what we are doing over here. Now That''s what we are doing over here.
    Now That''s what we are doing over here. Now

    you might be thinking that how is the you might be thinking that how is the you
    might be thinking that how is the

    loss function exactly calculated, right? loss function exactly calculated, right?
    loss function exactly calculated, right?

    So the way to calculate the loss So the way to calculate the loss So the way to
    calculate the loss

    function it''s actually quite simple function it''s actually quite simple function
    it''s actually quite simple

    right right right

    so what we have is that let''s say we so what we have is that let''s say we so
    what we have is that let''s say we

    look at every it has a 50257 dimensional look at every it has a 50257 dimensional
    look at every it has a 50257 dimensional

    vector of probabilities associated with vector of probabilities associated with
    vector of probabilities associated with

    it it it

    and we know that if every is the input and we know that if every is the input
    and we know that if every is the input

    effort should be the output and let''s effort should be the output and let''s
    effort should be the output and let''s

    say effort is at token ID number three say effort is at token ID number three
    say effort is at token ID number three

    so if all is well and if the language so if all is well and if the language so
    if all is well and if the language

    model is trained properly the'
  concept_slugs:
  - autoregressive-vs-diffusion
- idx: 18
  start_sec: 987.99
  end_sec: 1049.2
  text: 'model is trained properly the model is trained properly the

    probability at token ID number three probability at token ID number three probability
    at token ID number three

    should be equal to one should be equal to one should be equal to one

    because if this probability is one we because if this probability is one we because
    if this probability is one we

    are very sure that effort is the token are very sure that effort is the token
    are very sure that effort is the token

    which has to come next but it won''t be which has to come next but it won''t be
    which has to come next but it won''t be

    one right because the prediction is one right because the prediction is one right
    because the prediction is

    finger so finger has the highest finger so finger has the highest finger so finger
    has the highest

    probability so P target at ID equal to 3 probability so P target at ID equal to
    3 probability so P target at ID equal to 3

    will be one which we want but P actual will be one which we want but P actual
    will be one which we want but P actual

    for ID equal to 3 is what we actually for ID equal to 3 is what we actually for
    ID equal to 3 is what we actually

    have and let''s say that''s 2 which is have and let''s say that''s 2 which is
    have and let''s say that''s 2 which is

    very low so ID Ideally we want this very low so ID Ideally we want this very low
    so ID Ideally we want this

    probability to be as close to one as probability to be as close to one as probability
    to be as close to one as

    possible. So how do we encode that in possible. So how do we encode that in possible.
    So how do we encode that in

    the loss function? We use the cross the loss function? We use the cross the loss
    function? We use the cross

    entropy loss So if if my probability was actually one So if if my probability
    was actually one

    my loss will be zero which is what we my loss will be zero which is what we'
  concept_slugs:
  - autoregressive-vs-diffusion
- idx: 19
  start_sec: 1049.2
  end_sec: 1173.76
  text: 'my loss will be zero which is what we

    want. But in this case the loss will be want. But in this case the loss will be
    want. But in this case the loss will be

    negative log of2. negative log of2. negative log of2.

    Let''s see what that is. my loss will be 69. Okay. Similarly I my loss will be
    69. Okay. Similarly I

    add the loss. So the total loss is add the loss. So the total loss is add the
    loss. So the total loss is

    negative log of negative log of negative log of

    so probability where effort so probability where effort so probability where effort

    um um

    so for every is the input effort is the so for every is the input effort is the
    so for every is the input effort is the

    target right target right target right

    for every effort is the input moves is for every effort is the input moves is
    for every effort is the input moves is

    the output so then I will add moves actually the better way to expl moves actually
    the better way to expl

    explain this is um through again um through again

    a vetorial representation. So let me do a vetorial representation. So let me do
    a vetorial representation. So let me do

    that. Every Every

    effort effort

    moves you right. Yeah. This is my vector. This is my Yeah. This is my vector.
    This is my

    vector. Now for every as the input we know that Now for every as the input we
    know that

    the output is effort. the output is effort. the output is effort.

    So I get P effort here So I get P effort here So I get P effort here

    which is let''s say equal to 02 for which is let''s say equal to 02 for which
    is let''s say equal to 02 for

    effort every effort as the input the effort every effort as the input the effort
    every effort as the input the

    target should be moves. target should be moves. target should be moves.

    So I get P moves which is what''s the So I get P moves which is what''s the So
    I get P moves which is what''s the

    probability which should actually be one probability which should actually be
    one'
  concept_slugs:
  - autoregressive-vs-diffusion
- idx: 20
  start_sec: 1173.76
  end_sec: 1286.07
  text: 'probability which should actually be one

    but maybe it''s.3 if every effort moves but maybe it''s.3 if every effort moves
    but maybe it''s.3 if every effort moves

    is the input U should be the output. is the input U should be the output. is the
    input U should be the output.

    So I get probability of u is let''s say So I get probability of u is let''s say
    So I get probability of u is let''s say

    equal to 0.1 and if u is the input I equal to 0.1 and if u is the input I equal
    to 0.1 and if u is the input I

    want forward to be the output. want forward to be the output. want forward to
    be the output.

    So if p forward So if p forward So if p forward

    is equal to let''s say 04. So the loss in is equal to let''s say 04. So the loss
    in is equal to let''s say 04. So the loss in

    this case will be negative this case will be negative this case will be negative

    log of log of log of

    log of P effort log of P effort log of P effort

    plus plus plus

    log of P moves log of P moves log of P moves

    plus plus

    log of P log of P log of P

    U log.2 log.2

    plus log of.3 plus log of 4. plus log of 4.

    So let''s calculate this log of 2 plus log of.3 log of 2 plus log of.3

    plus log of plus log of plus log of

    1 + 1 + 1 +

    log of 04 log of 04 log of 04

    that''s equal to that''s equal to that''s equal to

    oh this should be log of 04. oh this should be log of 04. oh this should be log
    of 04.

    Yeah I missed it over here. Yeah that''s Yeah I missed it over here. Yeah that''s
    Yeah I missed it over here. Yeah that''s

    equal to minus 2.619. So if you add all equal to minus 2.619. So if you add all
    equal to minus 2.619. So if you add all

    this up this up this up

    this will be equal to uh this will be equal to uh this will be equal to uh

    if we take negative of this it will be'
  concept_slugs:
  - autoregressive-vs-diffusion
- idx: 21
  start_sec: 1286.07
  end_sec: 1334.96
  text: 'if we take negative of this it will be if we take negative of this it will
    be

    equal to 2.619 619 that''s the loss for equal to 2.619 619 that''s the loss for
    equal to 2.619 619 that''s the loss for

    this batch of input sequences that''s how this batch of input sequences that''s
    how this batch of input sequences that''s how

    we calculate the loss right for this we calculate the loss right for this we calculate
    the loss right for this

    batch here I''m assuming that one batch batch here I''m assuming that one batch
    batch here I''m assuming that one batch

    only has one sequence which is every only has one sequence which is every only
    has one sequence which is every

    effort moves you ideally each batch has effort moves you ideally each batch has
    effort moves you ideally each batch has

    multiple input sequences so we add the multiple input sequences so we add the
    multiple input sequences so we add the

    losses across those input sequences once losses across those input sequences once
    losses across those input sequences once

    we have this loss we just take the we have this loss we just take the we have
    this loss we just take the

    partial we just do back propagation and partial we just do back propagation and
    partial we just do back propagation and

    find the partial derivative of loss with find the partial derivative of loss with
    find the partial derivative of loss with

    respect to all the parameters of the respect to all the parameters of the respect
    to all the parameters of the

    language model and then we update the language model and then we update the language
    model and then we update the

    parameters Then we update the parameters. Then we Then we update the parameters.
    Then we

    get new batch get new batch get new batch

    find the loss and then this thing find the loss and then this thing find the loss
    and then this thing

    happens in a loop. This is how language happens in a loop. This is how language
    happens in a loop. This is how language

    models are trained. I hope all of you models are trained. I hope all of you'
  concept_slugs:
  - autoregressive-vs-diffusion
- idx: 22
  start_sec: 1334.96
  end_sec: 1375.44
  text: 'models are trained. I hope all of you

    now see the end to end details of why now see the end to end details of why now
    see the end to end details of why

    they are called as auto reggressive they are called as auto reggressive they are
    called as auto reggressive

    models or why it''s called as the next models or why it''s called as the next
    models or why it''s called as the next

    token prediction task because literally token prediction task because literally
    token prediction task because literally

    we are just predicting the next token. we are just predicting the next token.
    we are just predicting the next token.

    we are training the model to predict the we are training the model to predict
    the we are training the model to predict the

    next new token at every uh time point. next new token at every uh time point.
    next new token at every uh time point.

    So this is how loss is calculated. And So this is how loss is calculated. And
    So this is how loss is calculated. And

    the reason I showed this loss function the reason I showed this loss function
    the reason I showed this loss function

    calculation to you in a lot of detail is calculation to you in a lot of detail
    is calculation to you in a lot of detail is

    because in diffusion language model this because in diffusion language model this
    because in diffusion language model this

    also differs a lot. But for you to also differs a lot. But for you to also differs
    a lot. But for you to

    understand how it differs, you need to understand how it differs, you need to
    understand how it differs, you need to

    first understand how loss functions are first understand how loss functions are
    first understand how loss functions are

    calculated in traditional language calculated in traditional language calculated
    in traditional language

    models. And when I say traditional models. And when I say traditional models.
    And when I say traditional

    language models, I mean auto reggressive language models, I mean auto reggressive
    language models, I mean auto reggressive

    models. models. models.

    All right. So if you take a look at the All right. So if you take a look at the'
  concept_slugs:
  - autoregressive-vs-diffusion
- idx: 23
  start_sec: 1375.44
  end_sec: 1430.31
  text: 'All right. So if you take a look at the

    parameters now I hope all of you can parameters now I hope all of you can parameters
    now I hope all of you can

    visualize where all there are parameters visualize where all there are parameters
    visualize where all there are parameters

    in this right. So let me in this right. So let me in this right. So let me

    let me take this and let me bring this let me take this and let me bring this
    let me take this and let me bring this

    down over here and just for a quick down over here and just for a quick down over
    here and just for a quick

    um refresher or for a quick um refresher or for a quick um refresher or for a
    quick

    um test of whether you have understood um test of whether you have understood
    um test of whether you have understood

    it or not let''s try to when I say this it or not let''s try to when I say this
    it or not let''s try to when I say this

    PLLM PLLM PLLM

    Many of you might be thinking that where Many of you might be thinking that where
    Many of you might be thinking that where

    do the parameters actually live right do the parameters actually live right do
    the parameters actually live right

    and we have seen all of this. I just and we have seen all of this. I just and
    we have seen all of this. I just

    want to revise this once with all of want to revise this once with all of want
    to revise this once with all of

    you. you. you.

    So let''s uh So let''s uh So let''s uh

    make this GIF flow a bit and let''s see make this GIF flow a bit and let''s see
    make this GIF flow a bit and let''s see

    where all the parameters live. Okay, the where all the parameters live. Okay,
    the where all the parameters live. Okay, the

    simplest place is of course the token simplest place is of course the token simplest
    place is of course the token

    embeddings. Why is this a parameter? Why embeddings. Why is this a parameter?
    Why embeddings. Why is this a parameter? Why

    is the positional embeddings also a'
  concept_slugs:
  - autoregressive-vs-diffusion
- idx: 24
  start_sec: 1430.31
  end_sec: 1489.36
  text: 'is the positional embeddings also a is the positional embeddings also a

    parameter? Because we have the token parameter? Because we have the token parameter?
    Because we have the token

    embedding matrix and the position embedding matrix and the position embedding
    matrix and the position

    embedding matrix, right? Which we saw. embedding matrix, right? Which we saw.
    embedding matrix, right? Which we saw.

    This is the token embedding matrix. This is the token embedding matrix. This is
    the token embedding matrix.

    Position embedding matrix. This is Position embedding matrix. This is Position
    embedding matrix. This is

    initialized randomly. These are a bunch initialized randomly. These are a bunch
    initialized randomly. These are a bunch

    of parameters. We don''t know about them. of parameters. We don''t know about
    them. of parameters. We don''t know about them.

    So this is vocabulary size multiplied by So this is vocabulary size multiplied
    by So this is vocabulary size multiplied by

    embedding dimension number of embedding dimension number of embedding dimension
    number of

    parameters. And this is the sequence parameters. And this is the sequence parameters.
    And this is the sequence

    length or context length multiplied by length or context length multiplied by
    length or context length multiplied by

    the embedding dimension number of the embedding dimension number of the embedding
    dimension number of

    parameters. parameters. parameters.

    So we have the parameters in token So we have the parameters in token So we have
    the parameters in token

    embeddings, position embeddings for embeddings, position embeddings for embeddings,
    position embeddings for

    layer normalization. Actually we do have layer normalization. Actually we do have
    layer normalization. Actually we do have

    the scale and shift parameters but let''s the scale and shift parameters but let''s
    the scale and shift parameters but let''s

    not worry about this right now. For the not worry about this right now. For the
    not worry about this right now. For the

    multi head attention we have WQ. multi head attention we have WQ. multi head attention
    we have WQ.

    For the multi head attention we have uh WQ, we have W K, we have WV, and there
    WQ, we have W K, we have WV, and there

    is also an output projection head in the is also an output projection head in
    the is also an output projection head in the

    attention mechanism. So that''s also a attention mechanism. So that''s also a'
  concept_slugs:
  - autoregressive-vs-diffusion
- idx: 25
  start_sec: 1489.36
  end_sec: 1556.32
  text: 'attention mechanism. So that''s also a

    parameter. If you scroll about to the parameter. If you scroll about to the parameter.
    If you scroll about to the

    attention mechanism, you''ll see uh WQ, attention mechanism, you''ll see uh WQ,
    attention mechanism, you''ll see uh WQ,

    WQ, WK and WV. There is also an output WQ, WK and WV. There is also an output
    WQ, WK and WV. There is also an output

    head um which is at the end of the head um which is at the end of the head um
    which is at the end of the

    attention mechanism which is multiplied attention mechanism which is multiplied
    attention mechanism which is multiplied

    with the context vector matrix. So here with the context vector matrix. So here
    with the context vector matrix. So here

    is typically we have another learnable is typically we have another learnable
    is typically we have another learnable

    parameter called WO parameter called WO parameter called WO

    which is a matrix. When I say learnable which is a matrix. When I say learnable
    which is a matrix. When I say learnable

    parameter I mean a learnable matrix of parameter I mean a learnable matrix of
    parameter I mean a learnable matrix of

    parameters right then layer parameters right then layer parameters right then
    layer

    normalization 2 also has this scale and normalization 2 also has this scale and
    normalization 2 also has this scale and

    shift parameters. Yeah, layer normalization 2 has this uh Yeah, layer normalization
    2 has this uh

    scale and let me write this again. scale and let me write this again. scale and
    let me write this again.

    Yeah, does this uh Yeah, does this uh Yeah, does this uh

    scale and shift parameters right here. scale and shift parameters right here.
    scale and shift parameters right here.

    And if you look at the feed forward And if you look at the feed forward And if
    you look at the feed forward

    neural network, it also has a large neural network, it also has a large neural
    network, it also has a large

    number of parameters because we have a number of parameters because we have a
    number of parameters because we have a

    this is the feed forward neural network. this is the feed forward neural network.'
  concept_slugs:
  - autoregressive-vs-diffusion
- idx: 26
  start_sec: 1556.32
  end_sec: 1604.08
  text: 'this is the feed forward neural network.

    So we have 768 dimensions going to 4 So we have 768 dimensions going to 4 So we
    have 768 dimensions going to 4

    into 768 and then that again going to into 768 and then that again going to into
    768 and then that again going to

    768. So we have the 768 multiplied by 4 768. So we have the 768 multiplied by
    4 768. So we have the 768 multiplied by 4

    into 768 which are the total number of into 768 which are the total number of
    into 768 which are the total number of

    parameters in this region and multiplied parameters in this region and multiplied
    parameters in this region and multiplied

    by two. That''s the total number of by two. That''s the total number of by two.
    That''s the total number of

    parameters in the so the number of parameters in the so the number of parameters
    in the so the number of

    parameters in the expansion zone is 768 parameters in the expansion zone is 768
    parameters in the expansion zone is 768

    into 4 into 768. And the number of into 4 into 768. And the number of into 4 into
    768. And the number of

    parameters in the contraction zone is parameters in the contraction zone is parameters
    in the contraction zone is

    the same. the same. the same.

    Uh then we do have parameters in the Uh then we do have parameters in the Uh then
    we do have parameters in the

    final layer norm which is the scale and final layer norm which is the scale and
    final layer norm which is the scale and

    shift. Oh, I think my figure is down shift. Oh, I think my figure is down shift.
    Oh, I think my figure is down

    here. Yeah. So we have this feed forward here. Yeah. So we have this feed forward
    here. Yeah. So we have this feed forward

    neural network parameters. scale and neural network parameters. scale and neural
    network parameters. scale and

    shift parameters in the layer norm. Of shift parameters in the layer norm. Of
    shift parameters in the layer norm. Of

    course, multi-layer attention has course, multi-layer attention has course, multi-layer
    attention has

    parameters. We have parameters in the parameters. We have parameters in the'
  concept_slugs:
  - autoregressive-vs-diffusion
- idx: 27
  start_sec: 1604.08
  end_sec: 1666.72
  text: 'parameters. We have parameters in the

    final layer norm. And in the output final layer norm. And in the output final
    layer norm. And in the output

    layer, why do we have parameters here? layer, why do we have parameters here?
    layer, why do we have parameters here?

    Because if you see this matrix which Because if you see this matrix which Because
    if you see this matrix which

    lies in the vocabulary space, this is lies in the vocabulary space, this is lies
    in the vocabulary space, this is

    also called as the logits matrix. also called as the logits matrix. also called
    as the logits matrix.

    So this matrix which we saw which has So this matrix which we saw which has So
    this matrix which we saw which has

    number for each token with the number of number for each token with the number
    of number for each token with the number of

    dimensions is equal to vocabulary size. dimensions is equal to vocabulary size.
    dimensions is equal to vocabulary size.

    this matrix, this entire matrix. Um, yeah, this whole matrix right here, Um, yeah,
    this whole matrix right here,

    that''s also called as the logits matrix. Okay. I don''t know why my pen has Okay.
    I don''t know why my pen has

    suddenly stopped working. suddenly stopped working. suddenly stopped working.

    Yeah. But this whole matrix is the Yeah. But this whole matrix is the Yeah. But
    this whole matrix is the

    logits matrix. logits matrix. logits matrix.

    Yeah. Yeah. Yeah.

    And the number of parameters to get here And the number of parameters to get here
    And the number of parameters to get here

    is that we need to transform the from is that we need to transform the from is
    that we need to transform the from

    the embedding dimension to the the embedding dimension to the the embedding dimension
    to the

    vocabulary size dimension. Right? So we vocabulary size dimension. Right? So we
    vocabulary size dimension. Right? So we

    have a neural network here which has have a neural network here which has have
    a neural network here which has

    these many number of parameters. So that these many number of parameters. So that
    these many number of parameters. So that

    contributes to the parameters in the contributes to the parameters in the'
  concept_slugs:
  - autoregressive-vs-diffusion
- idx: 28
  start_sec: 1666.72
  end_sec: 1711.59
  text: 'contributes to the parameters in the

    output layer. So all of these parameters output layer. So all of these parameters
    output layer. So all of these parameters

    termed as P are the trainable parameters termed as P are the trainable parameters
    termed as P are the trainable parameters

    in our language model. And if you add in our language model. And if you add in
    our language model. And if you add

    all of these parameters, that''s why the all of these parameters, that''s why
    the all of these parameters, that''s why the

    number of parameters in a language model number of parameters in a language model
    number of parameters in a language model

    sometimes goes to 50 million, 100 sometimes goes to 50 million, 100 sometimes
    goes to 50 million, 100

    billion, 100 million or even a billions. billion, 100 million or even a billions.
    billion, 100 million or even a billions.

    And remember that we don''t have one And remember that we don''t have one And
    remember that we don''t have one

    transformer block. We have multiple. So transformer block. We have multiple. So
    transformer block. We have multiple. So

    all of these parameters kind of add up. all of these parameters kind of add up.
    all of these parameters kind of add up.

    Then they''re multiplied with the number Then they''re multiplied with the number
    Then they''re multiplied with the number

    of transformer blocks. That also leads of transformer blocks. That also leads
    of transformer blocks. That also leads

    to a huge number of parameters. So when to a huge number of parameters. So when
    to a huge number of parameters. So when

    I say PLLM, I say PLLM, I say PLLM,

    uh when I say PLLM over here, it uh when I say PLLM over here, it uh when I say
    PLLM over here, it

    actually means all of these parameters. actually means all of these parameters.
    actually means all of these parameters.

    Okay, this concludes our section on Okay, this concludes our section on Okay,
    this concludes our section on

    understanding the workings of an auto understanding the workings of an auto understanding
    the workings of an auto

    reggressive model. So to I said at the reggressive model. So to I said at the
    reggressive model. So to I said at the

    start of this that to truly understand'
  concept_slugs:
  - autoregressive-vs-diffusion
- idx: 29
  start_sec: 1711.59
  end_sec: 1760.48
  text: 'start of this that to truly understand start of this that to truly understand

    diffusion language models, we really diffusion language models, we really diffusion
    language models, we really

    need to first understand auto need to first understand auto need to first understand
    auto

    reggressive models and now we have seen reggressive models and now we have seen
    reggressive models and now we have seen

    how auto reggressive models are built. how auto reggressive models are built.
    how auto reggressive models are built.

    Okay, now we are slowly starting to see Okay, now we are slowly starting to see
    Okay, now we are slowly starting to see

    that once we know auto reggressive that once we know auto reggressive that once
    we know auto reggressive

    models, how auto reggressive models are models, how auto reggressive models are
    models, how auto reggressive models are

    built. Remember what I told over here built. Remember what I told over here built.
    Remember what I told over here

    I mentioned that diffusion LLMs are just I mentioned that diffusion LLMs are just
    I mentioned that diffusion LLMs are just

    80% of auto reggressive model 80% of auto reggressive model 80% of auto reggressive
    model

    architecture plus we have these three architecture plus we have these three architecture
    plus we have these three

    steps noising predicting the noise and steps noising predicting the noise and
    steps noising predicting the noise and

    denoising. So now we have to see how denoising. So now we have to see how denoising.
    So now we have to see how

    these key characteristics are linked these key characteristics are linked these
    key characteristics are linked

    with the 80% of the ARM architecture. with the 80% of the ARM architecture. with
    the 80% of the ARM architecture.

    So we are we are going to start seeing So we are we are going to start seeing
    So we are we are going to start seeing

    this now this now this now

    uh we are essentially going to start uh we are essentially going to start uh we
    are essentially going to start

    looking at these three steps noising looking at these three steps noising looking
    at these three steps noising

    predicting the noise and denoising and predicting the noise and denoising and
    predicting the noise and denoising and

    we''ll see how the ARM architecture is we''ll see how the ARM architecture is'
  concept_slugs:
  - autoregressive-vs-diffusion
- idx: 30
  start_sec: 1760.48
  end_sec: 1767.039
  text: 'we''ll see how the ARM architecture is

    the backbone of this predicting noise the backbone of this predicting noise the
    backbone of this predicting noise

    step. So let''s start looking at that step. So let''s start looking at that step.
    So let''s start looking at that

    now.'
  concept_slugs:
  - autoregressive-vs-diffusion
---
# Lecture 10: Auto Regressive Models (ARM) Output and Loss Blocks

See the structured chunks above.
