---
course_slug: diffusion-lm-vizuara
idx: 8
title: 'Lecture 7: Auto Regressive Models (ARM) Architecture Intro'
video_url: https://www.youtube.com/watch?v=bXXDARweFlw
duration_sec: null
chunks:
- idx: 0
  start_sec: 2.71
  end_sec: 67.19
  text: 'To truly understand To truly understand

    diffusion language models, we actually diffusion language models, we actually
    diffusion language models, we actually

    really need to understand how auto really need to understand how auto really need
    to understand how auto

    reggressive models or I may also call reggressive models or I may also call reggressive
    models or I may also call

    this traditional language models. this traditional language models. this traditional
    language models.

    We really need to understand how We really need to understand how We really need
    to understand how

    traditional language models are built traditional language models are built traditional
    language models are built

    from scratch. It turns out that for diffusion language It turns out that for diffusion
    language

    models, their architecture is 80% models, their architecture is 80% models, their
    architecture is 80%

    similar to traditional language models similar to traditional language models
    similar to traditional language models

    with the addition of these three with the addition of these three with the addition
    of these three

    concepts. concepts. concepts.

    So you can think of a diffusion language So you can think of a diffusion language
    So you can think of a diffusion language

    model as these key characteristics plus model as these key characteristics plus
    model as these key characteristics plus

    80% of a arm which is auto reggressive 80% of a arm which is auto reggressive
    80% of a arm which is auto reggressive

    model architecture. model architecture. model architecture.

    So to understand diffusion language So to understand diffusion language So to
    understand diffusion language

    models from scratch, we really need to models from scratch, we really need to
    models from scratch, we really need to

    do a deep dive into auto reggressive do a deep dive into auto reggressive do a
    deep dive into auto reggressive

    models. And when I say deep dive, it''s models. And when I say deep dive, it''s
    models. And when I say deep dive, it''s

    going to be a really deep dive where I''m going to be a really deep dive where
    I''m going to be a really deep dive where I''m

    going to explain the whole architecture going to explain the whole architecture
    going to explain the whole architecture

    right from the matrix dimension of every right from the matrix dimension of every
    right from the matrix dimension of every

    small aspect like the feed forward'
  concept_slugs:
  - autoregressive-vs-diffusion
- idx: 1
  start_sec: 67.19
  end_sec: 125.2
  text: 'small aspect like the feed forward small aspect like the feed forward

    neural network block here etc. So this neural network block here etc. So this
    neural network block here etc. So this

    is going to be a very long section and is going to be a very long section and
    is going to be a very long section and

    if you''re already aware of the if you''re already aware of the if you''re already
    aware of the

    architecture of traditional language architecture of traditional language architecture
    of traditional language

    models, I would encourage you to maybe models, I would encourage you to maybe
    models, I would encourage you to maybe

    skip this part or watch it in a quick skip this part or watch it in a quick skip
    this part or watch it in a quick

    way and you can directly move to the way and you can directly move to the way
    and you can directly move to the

    next part. next part. next part.

    Okay. So let''s start with this and to Okay. So let''s start with this and to
    Okay. So let''s start with this and to

    understand this I''m going to explain how understand this I''m going to explain
    how understand this I''m going to explain how

    a traditional how a traditional language model is how a traditional language model
    is

    built from scratch and then we''ll use the same learnings to and then we''ll use
    the same learnings to

    understand how diffusion language models understand how diffusion language models
    understand how diffusion language models

    are built. So let''s motivate the example are built. So let''s motivate the example
    are built. So let''s motivate the example

    a bit. We we are going to take this tiny a bit. We we are going to take this tiny
    a bit. We we are going to take this tiny

    stories data set today. This is going to stories data set today. This is going
    to stories data set today. This is going to

    be the same data set on which we are be the same data set on which we are be the
    same data set on which we are

    going to build our language diffusion going to build our language diffusion going
    to build our language diffusion

    model. This data set essentially model. This data set essentially'
  concept_slugs:
  - autoregressive-vs-diffusion
- idx: 2
  start_sec: 125.2
  end_sec: 171.84
  text: 'model. This data set essentially

    consists of around 2 million stories consists of around 2 million stories consists
    of around 2 million stories

    which are such that 3 to four year old which are such that 3 to four year old
    which are such that 3 to four year old

    kids can understand them. Okay. So if kids can understand them. Okay. So if kids
    can understand them. Okay. So if

    you take a look at one story, it can be you take a look at one story, it can be
    you take a look at one story, it can be

    something like this. One day a little something like this. One day a little something
    like this. One day a little

    girl named Lily found a needle in her girl named Lily found a needle in her girl
    named Lily found a needle in her

    room. She knew it was difficult to play room. She knew it was difficult to play
    room. She knew it was difficult to play

    with it because it was sharp etc etc. with it because it was sharp etc etc. with
    it because it was sharp etc etc.

    This is one story and there are 2 This is one story and there are 2 This is one
    story and there are 2

    million such stories. Right? So let''s million such stories. Right? So let''s
    million such stories. Right? So let''s

    start with this data set. That''s the start with this data set. That''s the start
    with this data set. That''s the

    first part of building a traditional first part of building a traditional first
    part of building a traditional

    language model or building any even a language model or building any even a language
    model or building any even a

    diffusion language model for that diffusion language model for that diffusion
    language model for that

    matter. Once we have this data set, my matter. Once we have this data set, my
    matter. Once we have this data set, my

    goal is that I want to build goal is that I want to build goal is that I want
    to build

    I want to learn patterns from this data I want to learn patterns from this data
    I want to learn patterns from this data

    so that I can predict or I can generate so that I can predict or I can generate'
  concept_slugs:
  - autoregressive-vs-diffusion
- idx: 3
  start_sec: 171.84
  end_sec: 238.08
  text: 'so that I can predict or I can generate

    language. language. language.

    And what does what does it mean? So the And what does what does it mean? So the
    And what does what does it mean? So the

    goal is to goal is to goal is to

    learn learn patterns from my data learn patterns from my data

    and predict language. and predict language. and predict language.

    and predict meaningful language.

    What does this mean predict meaningful What does this mean predict meaningful
    What does this mean predict meaningful

    language? It means that if I train a language? It means that if I train a language?
    It means that if I train a

    model which has learned patterns from model which has learned patterns from model
    which has learned patterns from

    this data and if I give the model some this data and if I give the model some
    this data and if I give the model some

    sequence of sentences like once upon a sequence of sentences like once upon a
    sequence of sentences like once upon a

    time. time. time.

    If I feed this input sequence to the If I feed this input sequence to the If I
    feed this input sequence to the

    model, model, model,

    the model will generate a coherent story the model will generate a coherent story
    the model will generate a coherent story

    based on what it has learned. based on what it has learned. based on what it has
    learned.

    And remember it''s called generative AI And remember it''s called generative AI
    And remember it''s called generative AI

    because the beauty of it is that this because the beauty of it is that this because
    the beauty of it is that this

    story will not be present in the data story will not be present in the data story
    will not be present in the data

    set. The model is learning patterns from set. The model is learning patterns from
    set. The model is learning patterns from

    the data and it generating new stuff, the data and it generating new stuff, the
    data and it generating new stuff,

    new stories on its own. That''s what I new stories on its own. That''s what I
    new stories on its own. That''s what I

    want to do. And what does it mean learn want to do. And what does it mean learn'
  concept_slugs:
  - autoregressive-vs-diffusion
- idx: 4
  start_sec: 238.08
  end_sec: 286.32
  text: 'want to do. And what does it mean learn

    patterns from the data? Well, the model patterns from the data? Well, the model
    patterns from the data? Well, the model

    needs to understand about the English needs to understand about the English needs
    to understand about the English

    language, right? It does not know language, right? It does not know language,
    right? It does not know

    anything about language. So, how will it anything about language. So, how will
    it anything about language. So, how will it

    generate meaningful sentences, generate generate meaningful sentences, generate
    generate meaningful sentences, generate

    coherent stories if it gener if it does coherent stories if it gener if it does
    coherent stories if it gener if it does

    not understand language? And what is not understand language? And what is not
    understand language? And what is

    language? Language can be split into two language? Language can be split into
    two language? Language can be split into two

    parts, right? There is grammar which is parts, right? There is grammar which is
    parts, right? There is grammar which is

    the form of a language. The lang the the form of a language. The lang the the
    form of a language. The lang the

    model needs to understand the correct model needs to understand the correct model
    needs to understand the correct

    grammar or the correct construction of grammar or the correct construction of
    grammar or the correct construction of

    sentences. For example, sentences. For example, sentences. For example,

    English language has English language has English language has

    Mary kicked the ball Mary kicked the ball Mary kicked the ball

    which is essentially a subject verb and which is essentially a subject verb and
    which is essentially a subject verb and

    an object right and there is also an object right and there is also an object
    right and there is also

    meaning. meaning. meaning.

    So the model should understand form So the model should understand form So the
    model should understand form

    which means that it should not mess up which means that it should not mess up
    which means that it should not mess up

    this order. It should not say Mary ball this order. It should not say Mary ball
    this order. It should not say Mary ball

    the kicked. That means it has not the kicked. That means it has not'
  concept_slugs:
  - autoregressive-vs-diffusion
- idx: 5
  start_sec: 286.32
  end_sec: 340.639
  text: 'the kicked. That means it has not

    understand not understood the correct understand not understood the correct understand
    not understood the correct

    grammatical constructions. And the model grammatical constructions. And the model
    grammatical constructions. And the model

    should also give sentences which have should also give sentences which have should
    also give sentences which have

    meaning. So for example, let''s say I meaning. So for example, let''s say I meaning.
    So for example, let''s say I

    have a sentence such as blue electrons have a sentence such as blue electrons
    have a sentence such as blue electrons

    eat fish. eat fish. eat fish.

    Now this sentence does not make sense. Now this sentence does not make sense.
    Now this sentence does not make sense.

    Although its form is correct, its Although its form is correct, its Although its
    form is correct, its

    meaning is not correct. meaning is not correct. meaning is not correct.

    So I want my language model to learn the So I want my language model to learn
    the So I want my language model to learn the

    form as well as the meaning from the form as well as the meaning from the form
    as well as the meaning from the

    underlying data. This looks like such a underlying data. This looks like such
    a underlying data. This looks like such a

    difficult problem problem right? Imagine difficult problem problem right? Imagine
    difficult problem problem right? Imagine

    what we are doing. We are giving the what we are doing. We are giving the what
    we are doing. We are giving the

    data to a model which knows nothing and data to a model which knows nothing and
    data to a model which knows nothing and

    we are asking the model to learn about we are asking the model to learn about
    we are asking the model to learn about

    language and not just that we are asking language and not just that we are asking
    language and not just that we are asking

    the model to generate stories out of it. the model to generate stories out of
    it. the model to generate stories out of it.

    That''s the task which we start out with. That''s the task which we start out
    with. That''s the task which we start out with.

    Okay. Now Okay. Now Okay. Now

    let me drink a cup of coffee. Yeah. So'
  concept_slugs:
  - autoregressive-vs-diffusion
- idx: 6
  start_sec: 340.639
  end_sec: 409.35
  text: 'Yeah. So

    how do we get started with this task? how do we get started with this task? how
    do we get started with this task?

    The first step is to look at our data The first step is to look at our data The
    first step is to look at our data

    itself. So let''s actually itself. So let''s actually itself. So let''s actually

    take this story and let''s see what''s actually done with and let''s see what''s
    actually done with

    this story. So I have my story over here this story. So I have my story over here
    this story. So I have my story over here

    right now right now right now

    which is my input data. Okay. And there which is my input data. Okay. And there
    which is my input data. Okay. And there

    are 2 million such stories like this. are 2 million such stories like this. are
    2 million such stories like this.

    If I want to make a machine learning If I want to make a machine learning If I
    want to make a machine learning

    model, I need to have inputs and I need model, I need to have inputs and I need
    model, I need to have inputs and I need

    to have outputs, right? So I need to to have outputs, right? So I need to to have
    outputs, right? So I need to

    generate input output pairs from this generate input output pairs from this generate
    input output pairs from this

    data. So let''s write this down. The task data. So let''s write this down. The
    task data. So let''s write this down. The task

    is to generate input input

    output output output

    pairs from this data. from this data.

    And how do we do this? Well, we first And how do we do this? Well, we first And
    how do we do this? Well, we first

    split the data into parts to create split the data into parts to create split
    the data into parts to create

    small input chunks that is decided by small input chunks that is decided by small
    input chunks that is decided by

    something which is called as the context something which is called as the context
    something which is called as the context

    size. It defines how many tokens or how'
  concept_slugs:
  - autoregressive-vs-diffusion
- idx: 7
  start_sec: 409.35
  end_sec: 458.479
  text: 'size. It defines how many tokens or how size. It defines how many tokens
    or how

    many words the model can pay attention many words the model can pay attention
    many words the model can pay attention

    to at one time. So let''s say my context to at one time. So let''s say my context
    to at one time. So let''s say my context

    size is four. So I divide my uh data set size is four. So I divide my uh data
    set size is four. So I divide my uh data set

    into blocks of four. into blocks of four. into blocks of four.

    Let''s say these are the blocks of four Let''s say these are the blocks of four
    Let''s say these are the blocks of four

    which I''ve divided my data set into. Okay. So I divide my entire data set Okay.
    So I divide my entire data set

    into these chunks. So these are my input into these chunks. So these are my input
    into these chunks. So these are my input

    sequences. This is so every green box is sequences. This is so every green box
    is sequences. This is so every green box is

    my input sequence my input sequence my input sequence

    and I have multiple such input and I have multiple such input and I have multiple
    such input

    sequences. That''s fine. The real u sequences. That''s fine. The real u sequences.
    That''s fine. The real u

    understanding here is how do we understanding here is how do we understanding
    here is how do we

    construct the output sequence from the construct the output sequence from the
    construct the output sequence from the

    input sequence. The way we construct the input sequence. The way we construct
    the input sequence. The way we construct the

    output sequence from the input sequence output sequence from the input sequence
    output sequence from the input sequence

    is we take the input sequence and we is we take the input sequence and we is we
    take the input sequence and we

    shift it to the right hand side by one. shift it to the right hand side by one.
    shift it to the right hand side by one.

    So So So

    if this is my first input sequence, if this is my first input sequence,'
  concept_slugs:
  - autoregressive-vs-diffusion
- idx: 8
  start_sec: 458.479
  end_sec: 518.07
  text: 'if this is my first input sequence,

    right? I shift it to the right hand side right? I shift it to the right hand side
    right? I shift it to the right hand side

    by one. If this is my second input by one. If this is my second input by one.
    If this is my second input

    sequence, I shift it to the right hand sequence, I shift it to the right hand
    sequence, I shift it to the right hand

    side by one. So you see my first input side by one. So you see my first input
    side by one. So you see my first input

    sequence is sequence is sequence is

    my first input sequence is one day a my first input sequence is one day a my first
    input sequence is one day a

    little. So let''s say my first input little. So let''s say my first input little.
    So let''s say my first input

    sequence is one day a little sequence is one day a little sequence is one day
    a little

    and my first output sequence is day day

    a a a

    little and girl. little and girl. little and girl.

    So this is my input sequence one and So this is my input sequence one and So this
    is my input sequence one and

    this is my output sequence one. Now pay this is my output sequence one. Now pay
    this is my output sequence one. Now pay

    very careful careful attention here very careful careful attention here very careful
    careful attention here

    right? uh when we train the model what right? uh when we train the model what
    right? uh when we train the model what

    we are going to tell the model is that we are going to tell the model is that
    we are going to tell the model is that

    although this looks like one input although this looks like one input although
    this looks like one input

    sequence and one output sequence it sequence and one output sequence it sequence
    and one output sequence it

    consists of four input output prediction consists of four input output prediction
    consists of four input output prediction

    tasks. What are these four? I want the tasks. What are these four? I want the
    tasks. What are these four? I want the

    model to learn that given any token it'
  concept_slugs:
  - autoregressive-vs-diffusion
- idx: 9
  start_sec: 518.07
  end_sec: 564.16
  text: 'model to learn that given any token it model to learn that given any token
    it

    has to predict the next token. So if one has to predict the next token. So if
    one has to predict the next token. So if one

    so I take my first input here if one is so I take my first input here if one is
    so I take my first input here if one is

    the input I want day to be the output. the input I want day to be the output.
    the input I want day to be the output.

    Then if one day is the input, Then if one day is the input, Then if one day is
    the input,

    I want uh to be the output. If one day I want uh to be the output. If one day
    I want uh to be the output. If one day

    uh is the input, I want little to be the uh is the input, I want little to be
    the uh is the input, I want little to be the

    output. And if one day a little is the output. And if one day a little is the
    output. And if one day a little is the

    input, I want girl to be the output. You input, I want girl to be the output.
    You input, I want girl to be the output. You

    see what''s going on here? see what''s going on here? see what''s going on here?

    We have [snorts] four input and target We have [snorts] four input and target
    We have [snorts] four input and target

    or input output prediction tasks here. or input output prediction tasks here.
    or input output prediction tasks here.

    If one is the input, day will be the If one is the input, day will be the If one
    is the input, day will be the

    output. If one day is the input, O will output. If one day is the input, O will
    output. If one day is the input, O will

    be the output. If one day E is O is the be the output. If one day E is O is the
    be the output. If one day E is O is the

    input, little will be the output. And if input, little will be the output. And
    if'
  concept_slugs:
  - autoregressive-vs-diffusion
- idx: 10
  start_sec: 564.16
  end_sec: 624.88
  text: 'input, little will be the output. And if

    one day a little is the input, girl will one day a little is the input, girl will
    one day a little is the input, girl will

    be the output. be the output. be the output.

    Right? So at every Right? So at every Right? So at every

    token, we are just predicting the next token, we are just predicting the next
    token, we are just predicting the next

    token here. And not just that, the first token here. And not just that, the first
    token here. And not just that, the first

    the earlier predicted tokens are added the earlier predicted tokens are added
    the earlier predicted tokens are added

    to the input sequence for the next to the input sequence for the next to the input
    sequence for the next

    prediction. That''s why this is called as prediction. That''s why this is called
    as prediction. That''s why this is called as

    an auto reggressive It is called as auto reggressive model It is called as auto
    reggressive model

    because it''s one new token generated at because it''s one new token generated
    at because it''s one new token generated at

    each time and the previous generated each time and the previous generated each
    time and the previous generated

    token is appended to the past input to token is appended to the past input to
    token is appended to the past input to

    to predict the next token. to predict the next token. to predict the next token.

    So this is how input and target pairs So this is how input and target pairs So
    this is how input and target pairs

    are constructed and one input target are constructed and one input target are
    constructed and one input target

    pair has multiple pair has multiple pair has multiple

    uh data prediction tasks or multiple uh data prediction tasks or multiple uh data
    prediction tasks or multiple

    target prediction tasks target prediction tasks target prediction tasks

    and that''s where the term auto and that''s where the term auto and that''s where
    the term auto

    reggressive actually comes into the reggressive actually comes into the reggressive
    actually comes into the

    picture right picture right picture right

    so imagine the huge data set which we so imagine the huge data set which we'
  concept_slugs:
  - autoregressive-vs-diffusion
- idx: 11
  start_sec: 624.88
  end_sec: 679.279
  text: 'so imagine the huge data set which we

    had 2 million rows that''s but that''s had 2 million rows that''s but that''s
    had 2 million rows that''s but that''s

    coupled into in let''s say input sequence coupled into in let''s say input sequence
    coupled into in let''s say input sequence

    one input sequence two and let''s say one input sequence two and let''s say one
    input sequence two and let''s say

    input sequence sequence uh 100,000. input sequence sequence uh 100,000. input
    sequence sequence uh 100,000.

    We have output sequence one, output We have output sequence one, output We have
    output sequence one, output

    sequence two and output sequence sequence two and output sequence sequence two
    and output sequence

    100,000. 100,000. 100,000.

    And remember the output sequence is just And remember the output sequence is just
    And remember the output sequence is just

    the input sequence shifted to the right the input sequence shifted to the right
    the input sequence shifted to the right

    hand side by one. That that''s why it''s hand side by one. That that''s why it''s
    hand side by one. That that''s why it''s

    called as an auto reggressive model. Now called as an auto reggressive model.
    Now called as an auto reggressive model. Now

    the way language models work is that the way language models work is that the
    way language models work is that

    these are grouped into batches. So this these are grouped into batches. So this
    these are grouped into batches. So this

    is batch one, this is batch two, etc. is batch one, this is batch two, etc. is
    batch one, this is batch two, etc.

    And I have each batch is passed through And I have each batch is passed through
    And I have each batch is passed through

    this language model. And I have my this language model. And I have my this language
    model. And I have my

    prediction. It is compared with the true answer. It is compared with the true
    answer.

    The true answer is given by these output The true answer is given by these output
    The true answer is given by these output

    sequences. And based on the prediction sequences. And based on the prediction
    sequences. And based on the prediction

    and the true answer, I have my loss and the true answer, I have my loss'
  concept_slugs:
  - autoregressive-vs-diffusion
- idx: 12
  start_sec: 679.279
  end_sec: 730.88
  text: 'and the true answer, I have my loss

    function. Right? Once I have my loss function. Right? Once I have my loss function.
    Right? Once I have my loss

    function, I find the gradient of the function, I find the gradient of the function,
    I find the gradient of the

    loss function with respect to all the loss function with respect to all the loss
    function with respect to all the

    parameters of this language model. parameters of this language model. parameters
    of this language model.

    and then I update the parameters. Right? This what I''m showing right now Right?
    This what I''m showing right now

    on the screen [snorts] is for one batch. on the screen [snorts] is for one batch.
    on the screen [snorts] is for one batch.

    This is for one batch. So let''s This is for one batch. So let''s This is for
    one batch. So let''s

    put a rectangle around it. This is for put a rectangle around it. This is for
    put a rectangle around it. This is for

    one batch. This same loop continues for one batch. This same loop continues for
    one batch. This same loop continues for

    multiple batches until I go through my multiple batches until I go through my
    multiple batches until I go through my

    entire data set. Once I go through my entire data set. Once I go through my entire
    data set. Once I go through my

    entire data set, that''s going through entire data set, that''s going through
    entire data set, that''s going through

    one epoch. Typically, language model one epoch. Typically, language model one
    epoch. Typically, language model

    training can just be done in two to training can just be done in two to training
    can just be done in two to

    three epochs since my data set is so three epochs since my data set is so three
    epochs since my data set is so

    huge. huge. huge.

    So, I go through my first batch, I get So, I go through my first batch, I get
    So, I go through my first batch, I get

    my loss, I update my parameters. my loss, I update my parameters. my loss, I update
    my parameters.

    Um, then what I''ll do is that I go Um, then what I''ll do is that I go'
  concept_slugs:
  - autoregressive-vs-diffusion
- idx: 13
  start_sec: 730.88
  end_sec: 770.48
  text: 'Um, then what I''ll do is that I go

    through my second batch, I get the loss, through my second batch, I get the loss,
    through my second batch, I get the loss,

    I update the parameters, then I go I update the parameters, then I go I update
    the parameters, then I go

    through my third batch, I get the loss, through my third batch, I get the loss,
    through my third batch, I get the loss,

    I update the parameters, and then that''s I update the parameters, and then that''s
    I update the parameters, and then that''s

    how I train my language model. Okay. how I train my language model. Okay. how
    I train my language model. Okay.

    Now you might be thinking that how do I Now you might be thinking that how do
    I Now you might be thinking that how do I

    essentially essentially essentially

    what does it mean passing a batch into what does it mean passing a batch into
    what does it mean passing a batch into

    this language model. So for that you this language model. So for that you this
    language model. So for that you

    first need to understand first need to understand first need to understand

    uh how tokens are converted into numbers uh how tokens are converted into numbers
    uh how tokens are converted into numbers

    and then you need to understand about and then you need to understand about and
    then you need to understand about

    the language model architecture itself. the language model architecture itself.
    the language model architecture itself.

    So let''s learn about that next.'
  concept_slugs:
  - autoregressive-vs-diffusion
---
# Lecture 7: Auto Regressive Models (ARM) Architecture Intro

See the structured chunks above.
