---
course_slug: diffusion-lm-vizuara
idx: 12
title: 'Lecture 11: Auto Regressive Models (ARM) Code: Pre training and Inference'
video_url: https://www.youtube.com/watch?v=1DcAjghgeYs
duration_sec: null
chunks:
- idx: 0
  start_sec: 2.8689999999999998
  end_sec: 59.91
  text: 'Before moving on to the fusion model Before moving on to the fusion model

    architecture architecture architecture

    and uh assembling it from scratch, and uh assembling it from scratch, and uh assembling
    it from scratch,

    I actually want to show you that I actually want to show you that I actually want
    to show you that

    we can build a small language model we can build a small language model we can
    build a small language model

    based on the traditional arm based on the traditional arm based on the traditional
    arm

    architecture fully from scratch. Based architecture fully from scratch. Based
    architecture fully from scratch. Based

    on what we have just seen on the on what we have just seen on the on what we have
    just seen on the

    whiteboard, we have seen this whole whiteboard, we have seen this whole whiteboard,
    we have seen this whole

    pipeline of uh how we get the data pipeline of uh how we get the data pipeline
    of uh how we get the data

    So if you look at the pipeline now, it''s So if you look at the pipeline now,
    it''s So if you look at the pipeline now, it''s

    as follows. We get the tiny stories as follows. We get the tiny stories as follows.
    We get the tiny stories

    data. Then we tokenize it. Then we data. Then we tokenize it. Then we data. Then
    we tokenize it. Then we

    create this input and output pairs. Then create this input and output pairs. Then
    create this input and output pairs. Then

    we pass the input sequences through this we pass the input sequences through this
    we pass the input sequences through this

    architecture. We get the output. We find architecture. We get the output. We find
    architecture. We get the output. We find

    the loss the loss the loss

    um we find the loss between the um we find the loss between the um we find the
    loss between the

    predictions and the targets and then we predictions and the targets and then we
    predictions and the targets and then we

    update the parameters. Then we get a new update the parameters. Then we get a
    new update the parameters. Then we get a new

    batch and this loop essentially batch and this loop essentially batch and this
    loop essentially

    continues. That''s pre-training of'
  concept_slugs:
  - autoregressive-vs-diffusion
- idx: 1
  start_sec: 59.91
  end_sec: 110.789
  text: 'continues. That''s pre-training of continues. That''s pre-training of

    language models or traditional language language models or traditional language
    language models or traditional language

    model pre-training or ARM auto model pre-training or ARM auto model pre-training
    or ARM auto

    reggressive model pre-training. We can reggressive model pre-training. We can
    reggressive model pre-training. We can

    demonstrate this end toend workflow from demonstrate this end toend workflow from
    demonstrate this end toend workflow from

    scratch using Google Collab. I''ll be scratch using Google Collab. I''ll be scratch
    using Google Collab. I''ll be

    sharing this Google Collab notebook with sharing this Google Collab notebook with
    sharing this Google Collab notebook with

    you and you''ll see that if you look at you and you''ll see that if you look at
    you and you''ll see that if you look at

    the different steps of this Google the different steps of this Google the different
    steps of this Google

    Collab notebook, you''ll see that it Collab notebook, you''ll see that it Collab
    notebook, you''ll see that it

    starts with importing the tiny stories starts with importing the tiny stories
    starts with importing the tiny stories

    data set first. The second step is to data set first. The second step is to data
    set first. The second step is to

    tokenize the data using the bite pair tokenize the data using the bite pair tokenize
    the data using the bite pair

    encoding which is the subword based encoding which is the subword based encoding
    which is the subword based

    tokenizer. Then we create the input and tokenizer. Then we create the input and
    tokenizer. Then we create the input and

    the output pairs. Then we define the the output pairs. Then we define the the
    output pairs. Then we define the

    architecture of the small language architecture of the small language architecture
    of the small language

    model. Now this architecture is uh model. Now this architecture is uh model. Now
    this architecture is uh

    exactly same as the whole architecture exactly same as the whole architecture
    exactly same as the whole architecture

    which we have seen over here. So if you which we have seen over here. So if you
    which we have seen over here. So if you

    start taking a look at um yeah the forward pass you''ll see that um yeah the forward
    pass you''ll see that

    we get the token embeddings we get the'
  concept_slugs:
  - autoregressive-vs-diffusion
- idx: 2
  start_sec: 110.789
  end_sec: 160.879
  text: 'we get the token embeddings we get the we get the token embeddings we get
    the

    position embeddings we add the token position embeddings we add the token position
    embeddings we add the token

    embeddings with the position embeddings embeddings with the position embeddings
    embeddings with the position embeddings

    to get the input embedding then we pass to get the input embedding then we pass
    to get the input embedding then we pass

    the input embedding through a bunch of the input embedding through a bunch of
    the input embedding through a bunch of

    transformer blocks in each transformer transformer blocks in each transformer
    transformer blocks in each transformer

    block what happens is you''ll see a class block what happens is you''ll see a
    class block what happens is you''ll see a class

    called block in each transformer block called block in each transformer block
    called block in each transformer block

    we have a layer normalization followed we have a layer normalization followed
    we have a layer normalization followed

    by attention second layer normalization by attention second layer normalization
    by attention second layer normalization

    U and a feed forward neural network and U and a feed forward neural network and
    U and a feed forward neural network and

    here we have the shortcut connections. here we have the shortcut connections.
    here we have the shortcut connections.

    So these six steps which you see in the So these six steps which you see in the
    So these six steps which you see in the

    code map exactly to these six which we code map exactly to these six which we
    code map exactly to these six which we

    have seen layer normalization multi head have seen layer normalization multi head
    have seen layer normalization multi head

    dropout shortcut connection layer dropout shortcut connection layer dropout shortcut
    connection layer

    normalization feed forward neural normalization feed forward neural normalization
    feed forward neural

    network dropout and shortcut connection. network dropout and shortcut connection.
    network dropout and shortcut connection.

    So this is how the architecture is So this is how the architecture is So this
    is how the architecture is

    assembled and then you define the loss assembled and then you define the loss
    assembled and then you define the loss

    function like the way we have um looked function like the way we have um looked'
  concept_slugs:
  - autoregressive-vs-diffusion
- idx: 3
  start_sec: 160.879
  end_sec: 204.8
  text: 'function like the way we have um looked

    at on the whiteboard at on the whiteboard at on the whiteboard

    right we saw that once we pass the input right we saw that once we pass the input
    right we saw that once we pass the input

    sequence through this architecture we sequence through this architecture we sequence
    through this architecture we

    actually get this uh logits matrix we actually get this uh logits matrix we actually
    get this uh logits matrix we

    get this logits matrix and then what we get this logits matrix and then what we
    get this logits matrix and then what we

    have to do is that based on the target have to do is that based on the target
    have to do is that based on the target

    values we just find the probabilities values we just find the probabilities values
    we just find the probabilities

    and take the cross entropy loss that''s and take the cross entropy loss that''s
    and take the cross entropy loss that''s

    my loss function. So you might be my loss function. So you might be my loss function.
    So you might be

    wondering where have we defined the wondering where have we defined the wondering
    where have we defined the

    cross entropy loss. It''s over here. We cross entropy loss. It''s over here. We
    cross entropy loss. It''s over here. We

    get the loss function for a batch and get the loss function for a batch and get
    the loss function for a batch and

    then here is where we define the then here is where we define the then here is
    where we define the

    training configuration. We define the training configuration. We define the training
    configuration. We define the

    learning rate. We define the batch size learning rate. We define the batch size
    learning rate. We define the batch size

    which is the number of input sequences which is the number of input sequences
    which is the number of input sequences

    which we want in one batch. And then we which we want in one batch. And then we
    which we want in one batch. And then we

    define the block size which is define the block size which is define the block
    size which is

    essentially the context length or the essentially the context length or the'
  concept_slugs:
  - autoregressive-vs-diffusion
- idx: 4
  start_sec: 204.8
  end_sec: 257.04
  text: 'essentially the context length or the

    sequence length. That''s the number of sequence length. That''s the number of
    sequence length. That''s the number of

    tokens in one tokens in one tokens in one

    input sequence. Right? input sequence. Right? input sequence. Right?

    Um and here is where we define the Um and here is where we define the Um and here
    is where we define the

    training configuration for the small training configuration for the small training
    configuration for the small

    language model. We use an AdamW language model. We use an AdamW language model.
    We use an AdamW

    optimizer with learning rate um weight optimizer with learning rate um weight
    optimizer with learning rate um weight

    decay. So it has the it has two decay. So it has the it has two decay. So it has
    the it has two

    additional parameters for the momentum additional parameters for the momentum
    additional parameters for the momentum

    and variance. and variance. and variance.

    And then finally we run this And then finally we run this And then finally we
    run this

    pre-training loop. I''m currently running pre-training loop. I''m currently running
    pre-training loop. I''m currently running

    it for around 20,000 epochs or 20,000 it for around 20,000 epochs or 20,000 it
    for around 20,000 epochs or 20,000

    iterations I think. Um and then you''ll iterations I think. Um and then you''ll
    iterations I think. Um and then you''ll

    see that the loss function goes on see that the loss function goes on see that
    the loss function goes on

    decreasing for 20,000 epochs. You can decreasing for 20,000 epochs. You can decreasing
    for 20,000 epochs. You can

    plot the training loss, the validation plot the training loss, the validation
    plot the training loss, the validation

    loss. And finally you can run inference loss. And finally you can run inference
    loss. And finally you can run inference

    on the small language model which means on the small language model which means
    on the small language model which means

    that uh we finally want to see whether that uh we finally want to see whether
    that uh we finally want to see whether

    the model generates coherent stories or the model generates coherent stories or
    the model generates coherent stories or

    not. Right? The whole idea when we not. Right? The whole idea when we'
  concept_slugs:
  - autoregressive-vs-diffusion
- idx: 5
  start_sec: 257.04
  end_sec: 298.88
  text: 'not. Right? The whole idea when we

    started this exercise was started this exercise was started this exercise was

    um we wanted to train the model so that um we wanted to train the model so that
    um we wanted to train the model so that

    at the end the model is able to generate at the end the model is able to generate
    at the end the model is able to generate

    a coherent story. Now it''s time to test a coherent story. Now it''s time to test
    a coherent story. Now it''s time to test

    the inference. Once the model has been the inference. Once the model has been
    the inference. Once the model has been

    trained, we pass a sequence, we pass a trained, we pass a sequence, we pass a
    trained, we pass a sequence, we pass a

    sentence and ask the model to uh predict sentence and ask the model to uh predict
    sentence and ask the model to uh predict

    the next tokens. So when you run this, the next tokens. So when you run this,
    the next tokens. So when you run this,

    you will see that you get inference you will see that you get inference you will
    see that you get inference

    outputs like this. Once upon a time, outputs like this. Once upon a time, outputs
    like this. Once upon a time,

    there was a pumpkin. It was very there was a pumpkin. It was very there was a
    pumpkin. It was very

    special. The pumpkin wanted to pay to special. The pumpkin wanted to pay to special.
    The pumpkin wanted to pay to

    his family. So one day, isn''t this his family. So one day, isn''t this his family.
    So one day, isn''t this

    amazing? amazing? amazing?

    This is just a model with around 15 This is just a model with around 15 This is
    just a model with around 15

    million parameters and in just 20,000 million parameters and in just 20,000 million
    parameters and in just 20,000

    iterations, the model has entirely iterations, the model has entirely iterations,
    the model has entirely

    learned the grammar. The grammar is learned the grammar. The grammar is learned
    the grammar. The grammar is

    completely correct here. There are some completely correct here. There are some'
  concept_slugs:
  - autoregressive-vs-diffusion
- idx: 6
  start_sec: 298.88
  end_sec: 340.08
  text: 'completely correct here. There are some

    mistakes here and there, but overall the mistakes here and there, but overall
    the mistakes here and there, but overall the

    grammar makes sense. The meaning also grammar makes sense. The meaning also grammar
    makes sense. The meaning also

    does not completely make sense, but for does not completely make sense, but for
    does not completely make sense, but for

    a 3 to four year old kid, it''s pretty a 3 to four year old kid, it''s pretty
    a 3 to four year old kid, it''s pretty

    awesome to know about a special pumpkin, awesome to know about a special pumpkin,
    awesome to know about a special pumpkin,

    right? A little girl went to the woods. right? A little girl went to the woods.
    right? A little girl went to the woods.

    he was looking at the animals and he saw he was looking at the animals and he
    saw he was looking at the animals and he saw

    a little boy with a big smile on its a little boy with a big smile on its a little
    boy with a big smile on its

    face etc. So some improvements can be face etc. So some improvements can be face
    etc. So some improvements can be

    made if you increase the number of made if you increase the number of made if
    you increase the number of

    iterations to 60,000 or 100,000. But on iterations to 60,000 or 100,000. But on
    iterations to 60,000 or 100,000. But on

    one single A100 GPU, we are using an one single A100 GPU, we are using an one
    single A100 GPU, we are using an

    A100 GPU over here. Training takes place A100 GPU over here. Training takes place
    A100 GPU over here. Training takes place

    for just 30 minutes. In 30 minutes of for just 30 minutes. In 30 minutes of for
    just 30 minutes. In 30 minutes of

    training on an A100 GPU, you''re getting training on an A100 GPU, you''re getting
    training on an A100 GPU, you''re getting

    coherent stories whose grammar makes coherent stories whose grammar makes coherent
    stories whose grammar makes

    sense, whose meaning makes sense. Not sense, whose meaning makes sense. Not sense,
    whose meaning makes sense. Not

    exactly, but mostly it''s pretty cool. So exactly, but mostly it''s pretty cool.
    So'
  concept_slugs:
  - autoregressive-vs-diffusion
- idx: 7
  start_sec: 340.08
  end_sec: 358.88
  text: 'exactly, but mostly it''s pretty cool. So

    auto reggressive models definitely work auto reggressive models definitely work
    auto reggressive models definitely work

    and they give good results. Right now we and they give good results. Right now
    we and they give good results. Right now we

    have to move towards diffusion models have to move towards diffusion models have
    to move towards diffusion models

    and see how these key characteristics of and see how these key characteristics
    of and see how these key characteristics of

    diffusion models have to be retained and diffusion models have to be retained
    and diffusion models have to be retained and

    how do we generate text from these. So, how do we generate text from these. So,
    how do we generate text from these. So,

    let''s get into that right'
  concept_slugs:
  - autoregressive-vs-diffusion
---
# Lecture 11: Auto Regressive Models (ARM) Code: Pre training and Inference

See the structured chunks above.
