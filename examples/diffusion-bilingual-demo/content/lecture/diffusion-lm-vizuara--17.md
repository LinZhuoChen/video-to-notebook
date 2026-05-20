---
course_slug: diffusion-lm-vizuara
idx: 17
title: 'Lecture 16: Diffusion LLM Coded from Scratch Part 1'
video_url: https://www.youtube.com/watch?v=8UiH1ttMdas
duration_sec: null
chunks:
- idx: 0
  start_sec: 2.71
  end_sec: 60.719
  text: 'Okay. So now I''m going to take you Okay. So now I''m going to take you

    through the code of assembling this through the code of assembling this through
    the code of assembling this

    diffusion language model from scratch diffusion language model from scratch diffusion
    language model from scratch

    and u this code is actually and u this code is actually and u this code is actually

    exactly following these steps which we exactly following these steps which we
    exactly following these steps which we

    have seen on the whiteboard. So I think have seen on the whiteboard. So I think
    have seen on the whiteboard. So I think

    all of you will be able to follow along all of you will be able to follow along
    all of you will be able to follow along

    if you have understood the theory which if you have understood the theory which
    if you have understood the theory which

    we have covered in the earlier modules we have covered in the earlier modules
    we have covered in the earlier modules

    of this course. Okay. of this course. Okay. of this course. Okay.

    All right. So All right. So All right. So

    the first thing which you should note is the first thing which you should note
    is the first thing which you should note is

    that here I have a subscription of that here I have a subscription of that here
    I have a subscription of

    Google Collab Pro. So I have access to Google Collab Pro. So I have access to
    Google Collab Pro. So I have access to

    an A1 H100 GPU. an A1 H100 GPU. an A1 H100 GPU.

    Diffusion language models take time to Diffusion language models take time to
    Diffusion language models take time to

    train compared to train compared to train compared to

    the auto reggressive models. So you the auto reggressive models. So you the auto
    reggressive models. So you

    should have access to Google Collab Pro. should have access to Google Collab Pro.
    should have access to Google Collab Pro.

    You can get A100 GPU or an H100 GPU You can get A100 GPU or an H100 GPU You can
    get A100 GPU or an H100 GPU

    here. The H100 GPU is much faster. here. The H100 GPU is much faster.'
  concept_slugs:
  - diffusion-language-model
  - masked-diffusion
- idx: 1
  start_sec: 60.719
  end_sec: 103.04
  text: 'here. The H100 GPU is much faster.

    If you don''t have access to the Google If you don''t have access to the Google
    If you don''t have access to the Google

    Collab Pro, you can start with the T4 Collab Pro, you can start with the T4 Collab
    Pro, you can start with the T4

    GPU which is free, but it will just take GPU which is free, but it will just take
    GPU which is free, but it will just take

    a large amount of time for the model to a large amount of time for the model to
    a large amount of time for the model to

    run. run. run.

    Okay. Okay. Okay.

    So remember that So remember that So remember that

    first thing which we have to do is that first thing which we have to do is that
    first thing which we have to do is that

    we have to select the mode which we have we have to select the mode which we have
    we have to select the mode which we have

    to run. If you have a if you are on a to run. If you have a if you are on a to
    run. If you have a if you are on a

    free tire of Google Collab, I suggest free tire of Google Collab, I suggest free
    tire of Google Collab, I suggest

    that you that you that you

    select the run mode to be quick. select the run mode to be quick. select the run
    mode to be quick.

    So what you can do is if you are on a So what you can do is if you are on a So
    what you can do is if you are on a

    free trial, you can do the run mode free trial, you can do the run mode free trial,
    you can do the run mode

    equal to quick equal to quick equal to quick

    and then run this notebook. You''ll see and then run this notebook. You''ll see
    and then run this notebook. You''ll see

    that in run mode equal to quick the that in run mode equal to quick the that in
    run mode equal to quick the

    number of training steps is only 2,000. number of training steps is only 2,000.'
  concept_slugs:
  - diffusion-language-model
  - masked-diffusion
- idx: 2
  start_sec: 103.04
  end_sec: 154.08
  text: 'number of training steps is only 2,000.

    Whereas in run mode equal to budget 100 Whereas in run mode equal to budget 100
    Whereas in run mode equal to budget 100

    which is if you have compute budget or which is if you have compute budget or
    which is if you have compute budget or

    if you have Google collab pro you can if you have Google collab pro you can if
    you have Google collab pro you can

    even run for 60,000 steps. Some even run for 60,000 steps. Some even run for 60,000
    steps. Some

    variables which I''ve defined here are variables which I''ve defined here are
    variables which I''ve defined here are

    the training examples which is the the training examples which is the the training
    examples which is the

    number of rows which I want from my tiny number of rows which I want from my tiny
    number of rows which I want from my tiny

    stories data set. So let me show that stories data set. So let me show that stories
    data set. So let me show that

    data set once more. data set once more. data set once more.

    Yeah. So essentially So essentially

    train examples is number of training train examples is number of training train
    examples is number of training

    examples which I have here. There are examples which I have here. There are examples
    which I have here. There are

    2.2 million. So we can choose how many 2.2 million. So we can choose how many
    2.2 million. So we can choose how many

    we want. Here I''ve chosen 1 million in we want. Here I''ve chosen 1 million in
    we want. Here I''ve chosen 1 million in

    this budget 100 and here I''ve only this budget 100 and here I''ve only this budget
    100 and here I''ve only

    chosen 50,000 in the quick version. Then chosen 50,000 in the quick version. Then
    chosen 50,000 in the quick version. Then

    we have to select the sequence length. we have to select the sequence length.
    we have to select the sequence length.

    Sequence length is essentially the Sequence length is essentially the Sequence
    length is essentially the

    embedding dimension. Right? So if you embedding dimension. Right? So if you embedding
    dimension. Right? So if you

    take a look at the take a look at the'
  concept_slugs:
  - diffusion-language-model
  - masked-diffusion
- idx: 3
  start_sec: 154.08
  end_sec: 200.319
  text: 'take a look at the

    whiteboard you''ll see that whiteboard you''ll see that whiteboard you''ll see
    that

    this dimension which I keep talking this dimension which I keep talking this dimension
    which I keep talking

    about right this this dimension the about right this this dimension the about
    right this this dimension the

    number of columns of the token embedding number of columns of the token embedding
    number of columns of the token embedding

    matrix and the number of columns of the matrix and the number of columns of the
    matrix and the number of columns of the

    position embedding matrix and in the position embedding matrix and in the position
    embedding matrix and in the

    case of diffusion model the time case of diffusion model the time case of diffusion
    model the time

    embedding matrix also that''s my embedding matrix also that''s my embedding matrix
    also that''s my

    embedding dimension and I''ve chosen that embedding dimension and I''ve chosen
    that embedding dimension and I''ve chosen that

    to be equal to 256. to be equal to 256. to be equal to 256.

    Now actually that''s the D model. So the Now actually that''s the D model. So
    the Now actually that''s the D model. So the

    embedding dimension is the D model which embedding dimension is the D model which
    embedding dimension is the D model which

    has been chosen to be 512. So I''m going has been chosen to be 512. So I''m going
    has been chosen to be 512. So I''m going

    to look at budget 100 for now. Embedding to look at budget 100 for now. Embedding
    to look at budget 100 for now. Embedding

    dimension is 512. Sequence length that''s dimension is 512. Sequence length that''s
    dimension is 512. Sequence length that''s

    the context length basically the number the context length basically the number
    the context length basically the number

    of tokens model can look at at one time. of tokens model can look at at one time.
    of tokens model can look at at one time.

    That''s the number of rows of position That''s the number of rows of position
    That''s the number of rows of position

    embedding matrix. So sequence length embedding matrix. So sequence length embedding
    matrix. So sequence length

    essentially here in these examples we essentially here in these examples we'
  concept_slugs:
  - diffusion-language-model
  - masked-diffusion
- idx: 4
  start_sec: 200.319
  end_sec: 253.76
  text: 'essentially here in these examples we

    have a sequence length of four tokens, have a sequence length of four tokens,
    have a sequence length of four tokens,

    right? Whereas in actual code we have right? Whereas in actual code we have right?
    Whereas in actual code we have

    taken a sequence length to be 256. taken a sequence length to be 256. taken a
    sequence length to be 256.

    vocabulary size is 26,000 vocabulary size is 26,000 vocabulary size is 26,000

    whereas uh here I just here when I whereas uh here I just here when I whereas
    uh here I just here when I

    mentioned the size of the token mentioned the size of the token mentioned the
    size of the token

    embedding matrix I had shown a embedding matrix I had shown a embedding matrix
    I had shown a

    vocabulary size of 100,000 you can play vocabulary size of 100,000 you can play
    vocabulary size of 100,000 you can play

    around with these variables these are around with these variables these are around
    with these variables these are

    not set in stone not set in stone not set in stone

    number of layers these are actually the number of layers these are actually the
    number of layers these are actually the

    number of uh number of uh number of uh

    transformer blocks so remember this transformer blocks so remember this transformer
    blocks so remember this

    mirror notebook which I showed all of mirror notebook which I showed all of mirror
    notebook which I showed all of

    you you you

    uh which was essentially called journey uh which was essentially called journey
    uh which was essentially called journey

    of a token. So if you take a look at of a token. So if you take a look at of a
    token. So if you take a look at

    this miro notebook this miro notebook this miro notebook

    you''ll see that there are when I show you''ll see that there are when I show
    you''ll see that there are when I show

    the transformer block there are actually the transformer block there are actually
    the transformer block there are actually

    multiple transformer blocks which are multiple transformer blocks which are multiple
    transformer blocks which are

    chained to each other. So these are the chained to each other. So these are the'
  concept_slugs:
  - diffusion-language-model
  - masked-diffusion
- idx: 5
  start_sec: 253.76
  end_sec: 311.83
  text: 'chained to each other. So these are the

    uh this variable is the number of uh this variable is the number of uh this variable
    is the number of

    layers. The number of heads is layers. The number of heads is layers. The number
    of heads is

    essentially for multi head attention. In essentially for multi head attention.
    In essentially for multi head attention. In

    this journey we have so far seen only this journey we have so far seen only this
    journey we have so far seen only

    single head attention. In multi single head attention. In multi single head attention.
    In multi

    attention you have different heads. Each attention you have different heads. Each
    attention you have different heads. Each

    head has its own attention score matrix head has its own attention score matrix
    head has its own attention score matrix

    or attention weight matrix. So we or attention weight matrix. So we or attention
    weight matrix. So we

    capture a different perspective. This capture a different perspective. This capture
    a different perspective. This

    DFF is for the DFF is for the DFF is for the

    field forward field forward field forward

    neural network. So if you take a look at neural network. So if you take a look
    at neural network. So if you take a look at

    this this this

    uh if you take a look at our schematic uh if you take a look at our schematic
    uh if you take a look at our schematic

    over here, you''ll see that the feed over here, you''ll see that the feed over
    here, you''ll see that the feed

    forward in the feed forward neural forward in the feed forward neural forward
    in the feed forward neural

    network. Yeah, we mentioned that it''s an network. Yeah, we mentioned that it''s
    an network. Yeah, we mentioned that it''s an

    expansion expansion expansion

    um and a contraction, right? So when we um and a contraction, right? So when we
    um and a contraction, right? So when we

    expand the number of dimensions in the expand the number of dimensions in the
    expand the number of dimensions in the

    hidden layer are four times the hidden layer are four times the hidden layer are
    four times the

    embedding dimension. So this four here embedding dimension. So this four here
    embedding dimension. So this four here

    that''s this uh four times the D model.'
  concept_slugs:
  - diffusion-language-model
  - masked-diffusion
- idx: 6
  start_sec: 311.83
  end_sec: 361.44
  text: 'that''s this uh four times the D model. that''s this uh four times the D
    model.

    So DFF is the feed forward neural So DFF is the feed forward neural So DFF is
    the feed forward neural

    network hidden layer dimension. diffusion steps is 128. So this is diffusion steps
    is 128. So this is

    basically here in this animation I have basically here in this animation I have
    basically here in this animation I have

    shown the diffusion steps to be equal to shown the diffusion steps to be equal
    to shown the diffusion steps to be equal to

    six. Right? Time goes from 1 to 6. So six. Right? Time goes from 1 to 6. So six.
    Right? Time goes from 1 to 6. So

    128 is just we have taken 128 time 128 is just we have taken 128 time 128 is just
    we have taken 128 time

    steps. steps. steps.

    That''s it. And the rest of the things That''s it. And the rest of the things
    That''s it. And the rest of the things

    are for the optimizer. We have gradient are for the optimizer. We have gradient
    are for the optimizer. We have gradient

    accumulation so that a huge batch does accumulation so that a huge batch does
    accumulation so that a huge batch does

    not live on a GPU. We reduce the batch not live on a GPU. We reduce the batch
    not live on a GPU. We reduce the batch

    size by half so that half of the batch size by half so that half of the batch
    size by half so that half of the batch

    lives on the GPU at one time. We have a lives on the GPU at one time. We have
    a lives on the GPU at one time. We have a

    learning rate of 2 into 10 -4 batch size learning rate of 2 into 10 -4 batch size
    learning rate of 2 into 10 -4 batch size

    of 32 weight TK of.1 and warm-up steps of 32 weight TK of.1 and warm-up steps
    of 32 weight TK of.1 and warm-up steps

    of,000. These will be needed in the ADM of,000. These will be needed in the ADM
    of,000. These will be needed in the ADM

    optimizer. Okay. So you run this initial optimizer. Okay. So you run this initial'
  concept_slugs:
  - diffusion-language-model
  - masked-diffusion
- idx: 7
  start_sec: 361.44
  end_sec: 409.44
  text: 'optimizer. Okay. So you run this initial

    configuration and then you move forward. configuration and then you move forward.
    configuration and then you move forward.

    You install a bunch of dependencies You install a bunch of dependencies You install
    a bunch of dependencies

    and make sure that you have GPU support and make sure that you have GPU support
    and make sure that you have GPU support

    here. So once we run this fully uh here. So once we run this fully uh here. So
    once we run this fully uh

    sometimes H100 GPU is not available in sometimes H100 GPU is not available in
    sometimes H100 GPU is not available in

    the Google Collab Pro version. So then the Google Collab Pro version. So then
    the Google Collab Pro version. So then

    you will be given an A100 version or an you will be given an A100 version or an
    you will be given an A100 version or an

    A100 GPU. That''s also fine but it takes A100 GPU. That''s also fine but it takes
    A100 GPU. That''s also fine but it takes

    a very long time to run. I''ll give you a very long time to run. I''ll give you
    a very long time to run. I''ll give you

    other options after showing this Google other options after showing this Google
    other options after showing this Google

    collab notebook which are much much collab notebook which are much much collab
    notebook which are much much

    faster such as going to run pod for faster such as going to run pod for faster
    such as going to run pod for

    example. example. example.

    Okay. So it''s still connecting. So I Okay. So it''s still connecting. So I Okay.
    So it''s still connecting. So I

    think H100 is not available. So let''s think H100 is not available. So let''s
    think H100 is not available. So let''s

    see see see

    once this is done the next step for us once this is done the next step for us
    once this is done the next step for us

    is to load the tiny stories data. So I is to load the tiny stories data. So I
    is to load the tiny stories data. So I

    go to this uh hugging face repository go to this uh hugging face repository'
  concept_slugs:
  - diffusion-language-model
  - masked-diffusion
- idx: 8
  start_sec: 409.44
  end_sec: 456.319
  text: 'go to this uh hugging face repository

    and I load my data. I load my training and I load my data. I load my training
    and I load my data. I load my training

    data set. I load my validation data set data set. I load my validation data set
    data set. I load my validation data set

    and uh my data is loaded. The next thing and uh my data is loaded. The next thing
    and uh my data is loaded. The next thing

    which we have to do is break down my which we have to do is break down my which
    we have to do is break down my

    sentences into tokens. Right? Now we sentences into tokens. Right? Now we sentences
    into tokens. Right? Now we

    could have used a bite pair encoder could have used a bite pair encoder could
    have used a bite pair encoder

    tokenizer which is there are number of tokenizer which is there are number of
    tokenizer which is there are number of

    tokenizers which are available from tokenizers which are available from tokenizers
    which are available from

    scratch. So if you go to the tick scratch. So if you go to the tick scratch. So
    if you go to the tick

    tokenizer, tokenizer, tokenizer,

    I think if you go to tick token library I think if you go to tick token library
    I think if you go to tick token library

    here, it''s the tokenizer which openai here, it''s the tokenizer which openai
    here, it''s the tokenizer which openai

    uses. So you can directly use a uses. So you can directly use a uses. So you can
    directly use a

    tokenizer from here. But just so that we tokenizer from here. But just so that
    we tokenizer from here. But just so that we

    all learn something, I have shown how to all learn something, I have shown how
    to all learn something, I have shown how to

    train a tokenizer from scratch. So I got train a tokenizer from scratch. So I
    got train a tokenizer from scratch. So I got

    a message that GPU was not available. So a message that GPU was not available.
    So a message that GPU was not available. So

    we I''m connected to an L4 GPU at the we I''m connected to an L4 GPU at the'
  concept_slugs:
  - diffusion-language-model
  - masked-diffusion
- idx: 9
  start_sec: 456.319
  end_sec: 512.389
  text: 'we I''m connected to an L4 GPU at the

    moment. See that''s fine. So let''s see. Um Um

    yeah so here you''ll see that I''m yeah so here you''ll see that I''m yeah so
    here you''ll see that I''m

    connected to an L4 Nvidia GPU connected to an L4 Nvidia GPU connected to an L4
    Nvidia GPU

    and uh my data set is also loaded right and uh my data set is also loaded right
    and uh my data set is also loaded right

    now to train a tokenizer from scratch. now to train a tokenizer from scratch.
    now to train a tokenizer from scratch.

    Basically we are just going to use this Basically we are just going to use this
    Basically we are just going to use this

    BP trainer module. I''m not going to go BP trainer module. I''m not going to go
    BP trainer module. I''m not going to go

    into too many details of this but bite into too many details of this but bite
    into too many details of this but bite

    pair encoding essentially merges pair encoding essentially merges pair encoding
    essentially merges

    commonly occurring tokens or characters commonly occurring tokens or characters
    commonly occurring tokens or characters

    and forms tokens which needed to be and forms tokens which needed to be and forms
    tokens which needed to be

    which need to be added in the which need to be added in the which need to be added
    in the

    vocabulary. The variable which we need vocabulary. The variable which we need
    vocabulary. The variable which we need

    to create this tokenizer is my to create this tokenizer is my to create this tokenizer
    is my

    vocabulary size. So we keep on adding vocabulary size. So we keep on adding vocabulary
    size. So we keep on adding

    tokens to the vocabulary until we reach tokens to the vocabulary until we reach
    tokens to the vocabulary until we reach

    a tokenizer size. So here you can see a tokenizer size. So here you can see a
    tokenizer size. So here you can see

    that that that

    uh I have also created special tokens uh I have also created special tokens uh
    I have also created special tokens

    here such as a padding token, unknown here such as a padding token, unknown here
    such as a padding token, unknown

    token, beginning of sequence, end of'
  concept_slugs:
  - diffusion-language-model
  - masked-diffusion
- idx: 10
  start_sec: 512.389
  end_sec: 560.79
  text: 'token, beginning of sequence, end of token, beginning of sequence, end of

    sequence and a mask token. This is very sequence and a mask token. This is very
    sequence and a mask token. This is very

    important. This mask token is the one important. This mask token is the one important.
    This mask token is the one

    which uh we''ll be using during the which uh we''ll be using during the which
    uh we''ll be using during the

    noising process as I''ve already noising process as I''ve already noising process
    as I''ve already

    explained to you. and the tokenizer explained to you. and the tokenizer explained
    to you. and the tokenizer

    training training training

    all the training text is wrapped in this all the training text is wrapped in this
    all the training text is wrapped in this

    write a short story then the assistant write a short story then the assistant
    write a short story then the assistant

    and then end and then end and then end

    uh so basically I''ll take this story uh so basically I''ll take this story uh
    so basically I''ll take this story

    from my data set and then the actual from my data set and then the actual from
    my data set and then the actual

    data set will be write a story then the data set will be write a story then the
    data set will be write a story then the

    actual story and then end and this this actual story and then end and this this
    actual story and then end and this this

    whole thing will be tokenized whole thing will be tokenized whole thing will be
    tokenized

    this is just a format which I''m using this is just a format which I''m using
    this is just a format which I''m using

    for the tokenization right now I don''t for the tokenization right now I don''t
    for the tokenization right now I don''t

    think you think you think you

    worry too much about tokenization at the worry too much about tokenization at
    the worry too much about tokenization at the

    moment. In fact, you can even replace moment. In fact, you can even replace moment.
    In fact, you can even replace

    this whole tokenizer section with your this whole tokenizer section with your
    this whole tokenizer section with your

    with a tokenizer directly borrowed from'
  concept_slugs:
  - diffusion-language-model
  - masked-diffusion
- idx: 11
  start_sec: 560.79
  end_sec: 621.269
  text: 'with a tokenizer directly borrowed from with a tokenizer directly borrowed
    from

    tick token. I I I think the code should tick token. I I I think the code should
    tick token. I I I think the code should

    still work. still work. still work.

    Uh okay, what''s important is that if you Uh okay, what''s important is that if
    you Uh okay, what''s important is that if you

    have a sentence such as hello world, have a sentence such as hello world, have
    a sentence such as hello world,

    right, based on the tokenizer which we right, based on the tokenizer which we
    right, based on the tokenizer which we

    have created, we have 2 1 3 0 0 1 1 5 6 have created, we have 2 1 3 0 0 1 1 5
    6 have created, we have 2 1 3 0 0 1 1 5 6

    9 and 3. These are the tokens. If I have 9 and 3. These are the tokens. If I have
    9 and 3. These are the tokens. If I have

    something like uh these are the tokens associated with it. these are the tokens
    associated with it.

    So I think this two and three is So I think this two and three is So I think this
    two and three is

    basically the beginning of sequence and basically the beginning of sequence and
    basically the beginning of sequence and

    the end of sequence I think. Um and the the end of sequence I think. Um and the
    the end of sequence I think. Um and the

    token ID corresponding to the mask is token ID corresponding to the mask is token
    ID corresponding to the mask is

    four. Yeah, two is the beginning of four. Yeah, two is the beginning of four.
    Yeah, two is the beginning of

    sequence ID. Three is the end of sequence ID. Three is the end of sequence ID.
    Three is the end of

    sequence ID and the token ID sequence ID and the token ID sequence ID and the
    token ID

    corresponding to mask is four. This corresponding to mask is four. This corresponding
    to mask is four. This

    token ID corresponding to mask is token ID corresponding to mask is token ID corresponding
    to mask is

    very important very important very important

    because in the noising process we are'
  concept_slugs:
  - diffusion-language-model
  - masked-diffusion
- idx: 12
  start_sec: 621.269
  end_sec: 673.279
  text: 'because in the noising process we are because in the noising process we are

    going to replace the tokens with masks going to replace the tokens with masks
    going to replace the tokens with masks

    and then we are going to use this token and then we are going to use this token
    and then we are going to use this token

    ID to represent those masks. Why have we ID to represent those masks. Why have
    we ID to represent those masks. Why have we

    added this write a short story here? added this write a short story here? added
    this write a short story here?

    Because when we are going to give the Because when we are going to give the Because
    when we are going to give the

    inference prompt, we are going to tell inference prompt, we are going to tell
    inference prompt, we are going to tell

    to write a short story. So if it''s to write a short story. So if it''s to write
    a short story. So if it''s

    included in the tokenizer training, it included in the tokenizer training, it
    included in the tokenizer training, it

    generally helps although it''s strictly generally helps although it''s strictly
    generally helps although it''s strictly

    not needed at all. [snorts] not needed at all. [snorts] not needed at all. [snorts]

    Okay. Now we come to the process of Okay. Now we come to the process of Okay.
    Now we come to the process of

    actually assembling the uh diffusion actually assembling the uh diffusion actually
    assembling the uh diffusion

    language model architecture. Right? So language model architecture. Right? So
    language model architecture. Right? So

    the diffusion language model the diffusion language model the diffusion language
    model

    architecture again to show everyone it architecture again to show everyone it
    architecture again to show everyone it

    looks something like this. Yeah, this is how the diffusion language Yeah, this
    is how the diffusion language

    model architecture actually looks like. model architecture actually looks like.
    model architecture actually looks like.

    And let me rub all of this so that And let me rub all of this so that And let
    me rub all of this so that

    becomes clearer to all of you. Yeah. becomes clearer to all of you. Yeah.'
  concept_slugs:
  - diffusion-language-model
  - masked-diffusion
- idx: 13
  start_sec: 673.279
  end_sec: 740.48
  text: 'becomes clearer to all of you. Yeah.

    And if you see that you first define a And if you see that you first define a
    And if you see that you first define a

    token embedding, position embedding and token embedding, position embedding and
    token embedding, position embedding and

    time embedding. time embedding. time embedding.

    And the place to get started to actually And the place to get started to actually
    And the place to get started to actually

    understand this code is that [snorts] understand this code is that [snorts] understand
    this code is that [snorts]

    you first have the token embeddings. you you first have the token embeddings.
    you you first have the token embeddings. you

    add it to the position embedding and add it to the position embedding and add
    it to the position embedding and

    then you add the time embedding after then you add the time embedding after then
    you add the time embedding after

    it. Right? And then this this input it. Right? And then this this input it. Right?
    And then this this input

    sequence you pass through the encoder sequence you pass through the encoder sequence
    you pass through the encoder

    block. Now what''s the encoder block? block. Now what''s the encoder block? block.
    Now what''s the encoder block?

    That''s essentially just a transformer That''s essentially just a transformer
    That''s essentially just a transformer

    encoder. So transformer encoder if you encoder. So transformer encoder if you
    encoder. So transformer encoder if you

    see yeah, we are just borrowing this yeah, we are just borrowing this

    transformer encoder from Pytor. So we transformer encoder from Pytor. So we transformer
    encoder from Pytor. So we

    don''t have to write this or code this don''t have to write this or code this
    don''t have to write this or code this

    from scratch. That just simplifies the from scratch. That just simplifies the
    from scratch. That just simplifies the

    code a lot. It just creates this entire code a lot. It just creates this entire
    code a lot. It just creates this entire

    transformer block like this. Okay. transformer block like this. Okay. transformer
    block like this. Okay.

    So here we are just going to do So here we are just going to do So here we are
    just going to do

    a transformer a transformer'
  concept_slugs:
  - diffusion-language-model
  - masked-diffusion
- idx: 14
  start_sec: 740.48
  end_sec: 791.76
  text: 'a transformer

    um we are going to do a transformer um we are going to do a transformer um we
    are going to do a transformer

    encoder layer over here and uh let''s see and attention mask equal to none. This
    and attention mask equal to none. This

    is extremely important attention mask is extremely important attention mask is
    extremely important attention mask

    equal to none essentially means that we equal to none essentially means that we
    equal to none essentially means that we

    are not having that causal attention are not having that causal attention are
    not having that causal attention

    layer which we saw in the whiteboard. So layer which we saw in the whiteboard.
    So layer which we saw in the whiteboard. So

    on the whiteboard what we saw is that on the whiteboard what we saw is that on
    the whiteboard what we saw is that

    for auto reggressive models we put this for auto reggressive models we put this
    for auto reggressive models we put this

    elements above the diagonal to be zero elements above the diagonal to be zero
    elements above the diagonal to be zero

    right in the attention scores but we are right in the attention scores but we
    are right in the attention scores but we are

    not going to do this in the diffusion not going to do this in the diffusion not
    going to do this in the diffusion

    model. So we don''t have any attention model. So we don''t have any attention
    model. So we don''t have any attention

    mask over here. So it''s very important mask over here. So it''s very important
    mask over here. So it''s very important

    to mention that attention mask equal to to mention that attention mask equal to
    to mention that attention mask equal to

    none. [snorts] none. [snorts] none. [snorts]

    Okay. So we say that attention mask Okay. So we say that attention mask Okay.
    So we say that attention mask

    equal to none. Uh we add the again we equal to none. Uh we add the again we equal
    to none. Uh we add the again we

    add the token embedding to the position add the token embedding to the position
    add the token embedding to the position

    embedding. We add the time embedding to embedding. We add the time embedding to'
  concept_slugs:
  - diffusion-language-model
  - masked-diffusion
- idx: 15
  start_sec: 791.76
  end_sec: 839.189
  text: 'embedding. We add the time embedding to

    it. The resultant input embedding we it. The resultant input embedding we it.
    The resultant input embedding we

    pass through the transformer block. Then pass through the transformer block. Then
    pass through the transformer block. Then

    we come to the output. We do a layer we come to the output. We do a layer we come
    to the output. We do a layer

    normalization and we do the logits and normalization and we do the logits and
    normalization and we do the logits and

    we return the logits. That''s all. This we return the logits. That''s all. This
    we return the logits. That''s all. This

    is the entire diffusion model is the entire diffusion model is the entire diffusion
    model

    architecture. architecture. architecture.

    Okay. Okay.

    Um and once you have understood this on Um and once you have understood this on
    Um and once you have understood this on

    the whiteboard, if you understood this the whiteboard, if you understood this
    the whiteboard, if you understood this

    architecture on the whiteboard, [snorts] architecture on the whiteboard, [snorts]
    architecture on the whiteboard, [snorts]

    what we are doing in code is exactly a what we are doing in code is exactly a
    what we are doing in code is exactly a

    representation of this architecture. representation of this architecture. representation
    of this architecture.

    There is nothing different which is There is nothing different which is There
    is nothing different which is

    being done over here. Note one more being done over here. Note one more being
    done over here. Note one more

    thing that uh we have in the forward thing that uh we have in the forward thing
    that uh we have in the forward

    pass we also have the time steps. Why do pass we also have the time steps. Why
    do pass we also have the time steps. Why do

    we have the time steps? Because for the we have the time steps? Because for the
    we have the time steps? Because for the

    time embedding we need to know which time embedding we need to know which time
    embedding we need to know which

    time time time

    um we are looking at because if you look um we are looking at because if you look
    um we are looking at because if you look

    at the time embedding matrix'
  concept_slugs:
  - diffusion-language-model
  - masked-diffusion
- idx: 16
  start_sec: 839.189
  end_sec: 887.189
  text: 'at the time embedding matrix at the time embedding matrix

    if we have t going from 1 to 128 we need if we have t going from 1 to 128 we need
    if we have t going from 1 to 128 we need

    to know at what time step we are in to to know at what time step we are in to
    to know at what time step we are in to

    choose the vector corresponding to that choose the vector corresponding to that
    choose the vector corresponding to that

    time step during the forward pass. time step during the forward pass. time step
    during the forward pass.

    Right. So I run this and I get the Right. So I run this and I get the Right. So
    I run this and I get the

    uh diffusion language model uh diffusion language model uh diffusion language
    model

    architecture. architecture.

    Then I''m just uh creating a training Then I''m just uh creating a training Then
    I''m just uh creating a training

    loader and I''m creating a validation loader and I''m creating a validation loader
    and I''m creating a validation

    loader so that we can create training loader so that we can create training loader
    so that we can create training

    and validation data quite easily. The and validation data quite easily. The and
    validation data quite easily. The

    next step is very important. Take a look next step is very important. Take a look
    next step is very important. Take a look

    at this corrupt with mask. Essentially at this corrupt with mask. Essentially
    at this corrupt with mask. Essentially

    what we are doing is before we pass the what we are doing is before we pass the
    what we are doing is before we pass the

    input ids to the uh transformer block or input ids to the uh transformer block
    or input ids to the uh transformer block or

    through the architecture itself we have through the architecture itself we have
    through the architecture itself we have

    to corrupt the input ids right. What to corrupt the input ids right. What to corrupt
    the input ids right. What

    does it mean? It means that we we have does it mean? It means that we we have
    does it mean? It means that we we have

    to based on the time step we have to add'
  concept_slugs:
  - diffusion-language-model
  - masked-diffusion
- idx: 17
  start_sec: 887.189
  end_sec: 929.839
  text: 'to based on the time step we have to add to based on the time step we have
    to add

    the mask tokens. This is what is done the mask tokens. This is what is done the
    mask tokens. This is what is done

    here. So we have t which is basically at here. So we have t which is basically
    at here. So we have t which is basically at

    what time step we are in and here what''s what time step we are in and here what''s
    what time step we are in and here what''s

    simply done is that we have this mask simply done is that we have this mask simply
    done is that we have this mask

    positions where the mask token ID is positions where the mask token ID is positions
    where the mask token ID is

    added and the rest of the token ids are added and the rest of the token ids are
    added and the rest of the token ids are

    replaced with minus 100. The reason they replaced with minus 100. The reason they
    replaced with minus 100. The reason they

    are replaced with minus 100 is because are replaced with minus 100 is because
    are replaced with minus 100 is because

    they are not going to come in the uh they are not going to come in the uh they
    are not going to come in the uh

    loss function calculation. So if you loss function calculation. So if you loss
    function calculation. So if you

    look at look at look at

    cross entropy loss pytor torch cross entropy loss pytor torch cross entropy loss
    pytor torch

    you''ll see that there is this ignore you''ll see that there is this ignore you''ll
    see that there is this ignore

    index of minus 100 which means that index of minus 100 which means that index
    of minus 100 which means that

    wherever we have minus 100 that''s not wherever we have minus 100 that''s not
    wherever we have minus 100 that''s not

    involved in the cross entropy loss involved in the cross entropy loss involved
    in the cross entropy loss

    calculation. So remember why is this calculation. So remember why is this calculation.
    So remember why is this

    done because we have already seen this done because we have already seen this'
  concept_slugs:
  - diffusion-language-model
  - masked-diffusion
- idx: 18
  start_sec: 929.839
  end_sec: 973.11
  text: 'done because we have already seen this

    on the whiteboard right to calculate the on the whiteboard right to calculate
    the on the whiteboard right to calculate the

    loss I only need to look at the mask loss I only need to look at the mask loss
    I only need to look at the mask

    tokens. I don''t need to look at the tokens. I don''t need to look at the tokens.
    I don''t need to look at the

    other tokens at all. So that''s why these other tokens at all. So that''s why
    these other tokens at all. So that''s why these

    other tokens are replaced with minus other tokens are replaced with minus other
    tokens are replaced with minus

    100. So they don''t come in my loss 100. So they don''t come in my loss 100. So
    they don''t come in my loss

    function calculation. So these minute function calculation. So these minute function
    calculation. So these minute

    differences between the diffusion differences between the diffusion differences
    between the diffusion

    language models and auto reggressive language models and auto reggressive language
    models and auto reggressive

    models are carefully scattered across models are carefully scattered across models
    are carefully scattered across

    the code. And unless you understand the the code. And unless you understand the
    the code. And unless you understand the

    theory, it will be very difficult for theory, it will be very difficult for theory,
    it will be very difficult for

    you to understand okay where is the you to understand okay where is the you to
    understand okay where is the

    where is it implemented that only the where is it implemented that only the where
    is it implemented that only the

    masked positions will be used in the masked positions will be used in the masked
    positions will be used in the

    loss function calculations because all loss function calculations because all
    loss function calculations because all

    the other input ids are replaced with the other input ids are replaced with the
    other input ids are replaced with

    minus 100. Where is it included that we minus 100. Where is it included that we
    minus 100. Where is it included that we

    won''t have a causal attention here? won''t have a causal attention here? won''t
    have a causal attention here?

    Well, it''s included over here where we'
  concept_slugs:
  - diffusion-language-model
  - masked-diffusion
- idx: 19
  start_sec: 973.11
  end_sec: 1016.88
  text: 'Well, it''s included over here where we Well, it''s included over here where
    we

    pass an attention mask equal to none. pass an attention mask equal to none. pass
    an attention mask equal to none.

    These are the small details which all of These are the small details which all
    of These are the small details which all of

    you need to be paying attention to. you need to be paying attention to. you need
    to be paying attention to.

    Okay, Okay, Okay,

    so this is how we define the input so this is how we define the input so this
    is how we define the input

    sequence and we corrupt it with noise sequence and we corrupt it with noise sequence
    and we corrupt it with noise

    which means we ask we just add masks at which means we ask we just add masks at
    which means we ask we just add masks at

    the positions where the positions where the positions where

    um we have chosen to add the mask based um we have chosen to add the mask based
    um we have chosen to add the mask based

    on the time step. Essentially the deeper on the time step. Essentially the deeper
    on the time step. Essentially the deeper

    we are into the noising schedule the we are into the noising schedule the we are
    into the noising schedule the

    more probability of adding the mask more probability of adding the mask more probability
    of adding the mask

    right and then we define the loss. right and then we define the loss. right and
    then we define the loss.

    To define the loss we just have to get To define the loss we just have to get
    To define the loss we just have to get

    the noisy ids and then we have to the noisy ids and then we have to the noisy
    ids and then we have to

    calculate the cross entropy loss between calculate the cross entropy loss between
    calculate the cross entropy loss between

    the noisy ids and the actual values at the noisy ids and the actual values at
    the noisy ids and the actual values at

    those mask positions. That''s it. those mask positions. That''s it. those mask
    positions. That''s it.

    So this is the cross entropy loss. So So this is the cross entropy loss. So'
  concept_slugs:
  - diffusion-language-model
  - masked-diffusion
- idx: 20
  start_sec: 1016.88
  end_sec: 1055.679
  text: 'So this is the cross entropy loss. So

    you can run this right now. Once we have you can run this right now. Once we have
    you can run this right now. Once we have

    this defined, the last step is just to this defined, the last step is just to
    this defined, the last step is just to

    define the training function and the define the training function and the define
    the training function and the

    loss function. So this is my training loss function. So this is my training loss
    function. So this is my training

    function at the moment where what I''m function at the moment where what I''m
    function at the moment where what I''m

    doing first is that this evaluation loss doing first is that this evaluation loss
    doing first is that this evaluation loss

    is after every 20 batches I''m going to is after every 20 batches I''m going to
    is after every 20 batches I''m going to

    print the loss. But here is where the print the loss. But here is where the print
    the loss. But here is where the

    real uh training happens. So what I''m real uh training happens. So what I''m
    real uh training happens. So what I''m

    going to do is that I''m going to take going to do is that I''m going to take
    going to do is that I''m going to take

    every batch from my training iteration. every batch from my training iteration.
    every batch from my training iteration.

    I''m going to uh I''m going to uh I''m going to uh

    find the diffusion loss on this batch find the diffusion loss on this batch find
    the diffusion loss on this batch

    and then what I''m going to do is that uh and then what I''m going to do is that
    uh and then what I''m going to do is that uh

    one more thing along with the batch as I one more thing along with the batch as
    I one more thing along with the batch as I

    mentioned we also need to define the mentioned we also need to define the mentioned
    we also need to define the

    time step right so when you go to the time step right so when you go to the'
  concept_slugs:
  - diffusion-language-model
  - masked-diffusion
- idx: 21
  start_sec: 1055.679
  end_sec: 1099.039
  text: 'time step right so when you go to the

    diffusion loss function you''ll see that diffusion loss function you''ll see that
    diffusion loss function you''ll see that

    uh where is the diffusion loss yeah when uh where is the diffusion loss yeah when
    uh where is the diffusion loss yeah when

    you see the diffusion loss function we you see the diffusion loss function we
    you see the diffusion loss function we

    also get this time step which is chosen also get this time step which is chosen
    also get this time step which is chosen

    uh randomly we need this time step uh randomly we need this time step uh randomly
    we need this time step

    because the corruption level depends on because the corruption level depends on
    because the corruption level depends on

    that time step Right. So if you go here, that time step Right. So if you go here,
    that time step Right. So if you go here,

    what''s actually done is that we first what''s actually done is that we first
    what''s actually done is that we first

    choose a batch of the data. choose a batch of the data. choose a batch of the
    data.

    We pass we choose a batch. Then we pass We pass we choose a batch. Then we pass
    We pass we choose a batch. Then we pass

    the model and the batch to the diffusion the model and the batch to the diffusion
    the model and the batch to the diffusion

    loss function. In the diffusion loss loss function. In the diffusion loss loss
    function. In the diffusion loss

    function, we have by default chosen a function, we have by default chosen a function,
    we have by default chosen a

    time step. And then here we pass the time step. And then here we pass the time
    step. And then here we pass the

    input batch and the time step to our input batch and the time step to our input
    batch and the time step to our

    model. This model has been defined over model. This model has been defined over
    model. This model has been defined over

    here. here. here.

    This model has been defined over here. This model has been defined over here.
    This model has been defined over here.

    Now this thing which I''m telling right Now this thing which I''m telling right'
  concept_slugs:
  - diffusion-language-model
  - masked-diffusion
- idx: 22
  start_sec: 1099.039
  end_sec: 1151.6
  text: 'Now this thing which I''m telling right

    now the corrupted input sequence is now the corrupted input sequence is now the
    corrupted input sequence is

    passed through the model is exactly passed through the model is exactly passed
    through the model is exactly

    shown over here. The corrupted sequence shown over here. The corrupted sequence
    shown over here. The corrupted sequence

    is passed through the model. It goes is passed through the model. It goes is passed
    through the model. It goes

    through this entire model architecture through this entire model architecture
    through this entire model architecture

    and we get the loss. and we get the loss. and we get the loss.

    All of this is implemented over here. We All of this is implemented over here.
    We All of this is implemented over here. We

    get the loss and then we do this is the get the loss and then we do this is the
    get the loss and then we do this is the

    optimizing step optimizer step. Once we optimizing step optimizer step. Once we
    optimizing step optimizer step. Once we

    get the loss function then we go into get the loss function then we go into get
    the loss function then we go into

    this loop of uh this loop of uh this loop of uh

    uh yeah we go into this loop of finding uh yeah we go into this loop of finding
    uh yeah we go into this loop of finding

    the partial derivative of the loss then the partial derivative of the loss then
    the partial derivative of the loss then

    updating the parameters through the updating the parameters through the updating
    the parameters through the

    optimizer that''s done over here we do optimizer that''s done over here we do
    optimizer that''s done over here we do

    optimizer step and we uh update the optimizer step and we uh update the optimizer
    step and we uh update the

    learning rate in the adm optimizer etc. learning rate in the adm optimizer etc.
    learning rate in the adm optimizer etc.

    So you run this right now and then you So you run this right now and then you
    So you run this right now and then you

    will see that the training process will see that the training process will see
    that the training process

    starts automatically. Yeah, see the training process has'
  concept_slugs:
  - diffusion-language-model
  - masked-diffusion
- idx: 23
  start_sec: 1151.6
  end_sec: 1197.52
  text: 'Yeah, see the training process has

    started. Now I''m on the L I think let''s started. Now I''m on the L I think let''s
    started. Now I''m on the L I think let''s

    see which GPU I''m on. I''m on the L4 GPU see which GPU I''m on. I''m on the L4
    GPU see which GPU I''m on. I''m on the L4 GPU

    which is actually not very fast. So the which is actually not very fast. So the
    which is actually not very fast. So the

    iterations are proceeding slowly. So iterations are proceeding slowly. So iterations
    are proceeding slowly. So

    here it''s showing that it will take here it''s showing that it will take here
    it''s showing that it will take

    around 3 hours for me. Still it''s quite around 3 hours for me. Still it''s quite
    around 3 hours for me. Still it''s quite

    good right for 60,000 iterations. If you good right for 60,000 iterations. If
    you good right for 60,000 iterations. If you

    are on T4 GPU it may take 8 to 9 hours. are on T4 GPU it may take 8 to 9 hours.
    are on T4 GPU it may take 8 to 9 hours.

    One thing which I want to point out to One thing which I want to point out to
    One thing which I want to point out to

    all of you is that although the all of you is that although the all of you is
    that although the

    inference of a diffusion model is inference of a diffusion model is inference
    of a diffusion model is

    faster, training actually is a bit faster, training actually is a bit faster,
    training actually is a bit

    slower. So slower. So slower. So

    if you scroll to the top, I''ve actually if you scroll to the top, I''ve actually
    if you scroll to the top, I''ve actually

    compared the training speeds of a compared the training speeds of a compared the
    training speeds of a

    diffusion language model and the auto diffusion language model and the auto diffusion
    language model and the auto

    reggressive model. So here if you see um reggressive model. So here if you see
    um reggressive model. So here if you see um

    in u the convergence speed so if you see in u the convergence speed so if you
    see'
  concept_slugs:
  - diffusion-language-model
  - masked-diffusion
- idx: 24
  start_sec: 1197.52
  end_sec: 1244.72
  text: 'in u the convergence speed so if you see

    the auto reggressive model in 15,000 the auto reggressive model in 15,000 the
    auto reggressive model in 15,000

    epochs I go from a loss of 8 to a loss epochs I go from a loss of 8 to a loss
    epochs I go from a loss of 8 to a loss

    of 2.6. So almost the whole model has of 2.6. So almost the whole model has of
    2.6. So almost the whole model has

    converged in 15,000 epochs itself. converged in 15,000 epochs itself. converged
    in 15,000 epochs itself.

    Whereas in diffusion LLM in 15,000 steps Whereas in diffusion LLM in 15,000 steps
    Whereas in diffusion LLM in 15,000 steps

    I go from a loss of 10 to just a loss of I go from a loss of 10 to just a loss
    of I go from a loss of 10 to just a loss of

    5.6. 5.6. 5.6.

    So the model actually converges slowly. So the model actually converges slowly.
    So the model actually converges slowly.

    Diffusion language models take time to Diffusion language models take time to

    converge and that''s a trait trait of converge and that''s a trait trait of converge
    and that''s a trait trait of

    diffusion models always they are a bit diffusion models always they are a bit
    diffusion models always they are a bit

    slower slower slower

    because of the mask predictions being because of the mask predictions being because
    of the mask predictions being

    involved at and we are looking at it involved at and we are looking at it involved
    at and we are looking at it

    from both sides so the attention matrix from both sides so the attention matrix
    from both sides so the attention matrix

    is a bit larger etc. is a bit larger etc. is a bit larger etc.

    Um so diffusion language models in my Um so diffusion language models in my Um
    so diffusion language models in my

    experience train a bit slowly compared experience train a bit slowly compared
    experience train a bit slowly compared

    to auto reggressive models but as you to auto reggressive models but as you to
    auto reggressive models but as you

    can see the training has started over can see the training has started over'
  concept_slugs:
  - diffusion-language-model
  - masked-diffusion
- idx: 25
  start_sec: 1244.72
  end_sec: 1294.47
  text: 'can see the training has started over

    here and we can print the loss we can here and we can print the loss we can here
    and we can print the loss we can

    print the learning rate etc. While the print the learning rate etc. While the
    print the learning rate etc. While the

    training is going on, I''ll tell you the training is going on, I''ll tell you
    the training is going on, I''ll tell you the

    next steps. What we''ll do after this next steps. What we''ll do after this next
    steps. What we''ll do after this

    training is that we then just have to training is that we then just have to training
    is that we then just have to

    proceed with generation. Right? So in proceed with generation. Right? So in proceed
    with generation. Right? So in

    generation, as I''ve mentioned already, generation, as I''ve mentioned already,
    generation, as I''ve mentioned already,

    we just carry out sequential unmasking. we just carry out sequential unmasking.
    we just carry out sequential unmasking.

    So here is a animation of generation or So here is a animation of generation or
    So here is a animation of generation or

    dnoising which we have seen. We start dnoising which we have seen. We start dnoising
    which we have seen. We start

    with masks and then sequentially unmask with masks and then sequentially unmask
    with masks and then sequentially unmask

    and uh we unmask tokens with the highest and uh we unmask tokens with the highest
    and uh we unmask tokens with the highest

    confidence. That''s the general rule, confidence. That''s the general rule, confidence.
    That''s the general rule,

    right? So this is the diffusion generate right? So this is the diffusion generate
    right? So this is the diffusion generate

    code where we start with all the masks code where we start with all the masks
    code where we start with all the masks

    and then and then and then

    the unmasking is actually done for the the unmasking is actually done for the
    the unmasking is actually done for the

    maximum confidence. That''s the entire maximum confidence. That''s the entire
    maximum confidence. That''s the entire

    logic which has been implemented over logic which has been implemented over logic
    which has been implemented over

    here. I am not going to go through this'
  concept_slugs:
  - diffusion-language-model
  - masked-diffusion
- idx: 26
  start_sec: 1294.47
  end_sec: 1339.43
  text: 'here. I am not going to go through this here. I am not going to go through
    this

    code in detail because it just code in detail because it just code in detail because
    it just

    implements the same thing, right? We we implements the same thing, right? We we
    implements the same thing, right? We we

    get the confidence scores and then we get the confidence scores and then we get
    the confidence scores and then we

    unmask the token ids with the maximum unmask the token ids with the maximum unmask
    the token ids with the maximum

    confidence. The reason I spent so much confidence. The reason I spent so much
    confidence. The reason I spent so much

    time on the whiteboard is because going time on the whiteboard is because going
    time on the whiteboard is because going

    through code is I found that if I go through code is I found that if I go through
    code is I found that if I go

    through this code generally a bit through this code generally a bit through this
    code generally a bit

    difficult for folks to understand right difficult for folks to understand right
    difficult for folks to understand right

    but if I take an actual example and show but if I take an actual example and show
    but if I take an actual example and show

    you how unmasking is done step by step you how unmasking is done step by step
    you how unmasking is done step by step

    you can relate this very easily to the you can relate this very easily to the
    you can relate this very easily to the

    code code code

    right so here''s here actually the same right so here''s here actually the same
    right so here''s here actually the same

    unmasking uh procedure is happening unmasking uh procedure is happening unmasking
    uh procedure is happening

    right now let me do this okay let me right now let me do this okay let me right
    now let me do this okay let me

    stop this for a moment and Let''s run stop this for a moment and Let''s run stop
    this for a moment and Let''s run

    with whatever I have. with whatever I have. with whatever I have.

    Uh so this is run right now and uh here'
  concept_slugs:
  - diffusion-language-model
  - masked-diffusion
- idx: 27
  start_sec: 1339.43
  end_sec: 1407.919
  text: 'Uh so this is run right now and uh here Uh so this is run right now and uh
    here

    I''m just seeing a sample inference. Once I''m just seeing a sample inference.
    Once I''m just seeing a sample inference. Once

    upon a time is the input. I''ll see that upon a time is the input. I''ll see that
    upon a time is the input. I''ll see that

    the inference is very bad right now the inference is very bad right now the inference
    is very bad right now

    because I I just stopped at uh because I I just stopped at uh because I I just
    stopped at uh

    how many steps just thousand steps but I how many steps just thousand steps but
    I how many steps just thousand steps but I

    just want to show you the workflow. just want to show you the workflow. just want
    to show you the workflow.

    Right? So technically we have finished Right? So technically we have finished
    Right? So technically we have finished

    coding the diffusion language model from coding the diffusion language model from
    coding the diffusion language model from

    scratch here. But I have just added a scratch here. But I have just added a scratch
    here. But I have just added a

    simple code to render a terminal style simple code to render a terminal style
    simple code to render a terminal style

    diff terminal style GIF. Right. Uh I diff terminal style GIF. Right. Uh I diff
    terminal style GIF. Right. Uh I

    think there is an error over here think there is an error over here think there
    is an error over here

    probably because we have not run till uh probably because we have not run till
    uh probably because we have not run till uh

    till completion and that''s I think till completion and that''s I think till completion
    and that''s I think

    that''s fine that''s fine that''s fine

    but no such file or directory as no such file or directory as

    inference.jif. here also there is an error which says here also there is an error
    which says

    cannot import. cannot import. cannot import.

    I think this is probably because the I think this is probably because the I think
    this is probably because the

    iterations did not finish. But if you iterations did not finish. But if you'
  concept_slugs:
  - diffusion-language-model
  - masked-diffusion
- idx: 28
  start_sec: 1407.919
  end_sec: 1449.51
  text: 'iterations did not finish. But if you

    actually run um actually run um actually run um

    60,000 or 60,000 or 100,000 iterations 60,000 or 60,000 or 100,000 iterations
    60,000 or 60,000 or 100,000 iterations

    over here, you will generally see that over here, you will generally see that
    over here, you will generally see that

    the code finishes till completion. the code finishes till completion. the code
    finishes till completion.

    Um and then you just have to export this Um and then you just have to export this
    Um and then you just have to export this

    GIF and you have to save this GIF. So GIF and you have to save this GIF. So GIF
    and you have to save this GIF. So

    I''ve just written I also have another I''ve just written I also have another
    I''ve just written I also have another

    font here if you want to export the GIF font here if you want to export the GIF
    font here if you want to export the GIF

    in a slightly cooler format. But if you in a slightly cooler format. But if you
    in a slightly cooler format. But if you

    export the normal GIF, it will look export the normal GIF, it will look export
    the normal GIF, it will look

    something like this. So this is trained something like this. So this is trained
    something like this. So this is trained

    for 100,000 iterations, right? And after for 100,000 iterations, right? And after
    for 100,000 iterations, right? And after

    100,000 iterations, you will start to 100,000 iterations, you will start to 100,000
    iterations, you will start to

    see that the output starts becoming see that the output starts becoming see that
    the output starts becoming

    coherent. So the output is that once coherent. So the output is that once coherent.
    So the output is that once

    upon a time, there was a little girl upon a time, there was a little girl upon
    a time, there was a little girl

    named Lily. She loved to play with her named Lily. She loved to play with her
    named Lily. She loved to play with her

    toys and put them in a room. One day, toys and put them in a room. One day, toys
    and put them in a room. One day,

    Lily''s mom asked her to help clean up'
  concept_slugs:
  - diffusion-language-model
  - masked-diffusion
- idx: 29
  start_sec: 1449.51
  end_sec: 1490.32
  text: 'Lily''s mom asked her to help clean up Lily''s mom asked her to help clean
    up

    her toys. Lily was happy to help her mom her toys. Lily was happy to help her
    mom her toys. Lily was happy to help her mom

    put them in a box. Isn''t this amazing? put them in a box. Isn''t this amazing?
    put them in a box. Isn''t this amazing?

    This entirely coherent text generated This entirely coherent text generated This
    entirely coherent text generated

    through a pure diffusion model which we through a pure diffusion model which we
    through a pure diffusion model which we

    have built from scratch for 100,000 have built from scratch for 100,000 have built
    from scratch for 100,000

    iterations through the exact same code iterations through the exact same code
    iterations through the exact same code

    which I have shown to you right now. And which I have shown to you right now.
    And which I have shown to you right now. And

    once you run this code, once you once you run this code, once you once you run
    this code, once you

    replicate this code, you''ll also see replicate this code, you''ll also see replicate
    this code, you''ll also see

    this for yourself. The only requirement this for yourself. The only requirement
    this for yourself. The only requirement

    which you''ll need is that you''ll need to which you''ll need is that you''ll
    need to which you''ll need is that you''ll need to

    run at least for 50,000 or 60,000 run at least for 50,000 or 60,000 run at least
    for 50,000 or 60,000

    iterations and you''ll need a A100 GPU, iterations and you''ll need a A100 GPU,
    iterations and you''ll need a A100 GPU,

    H100 or if you have time, you can even H100 or if you have time, you can even
    H100 or if you have time, you can even

    do it on a T4 GPU or an L4 GPU. What I do it on a T4 GPU or an L4 GPU. What I
    do it on a T4 GPU or an L4 GPU. What I

    want to show you is that uh want to show you is that uh want to show you is that
    uh

    we can also do this on runpod. So if you we can also do this on runpod. So if
    you'
  concept_slugs:
  - diffusion-language-model
  - masked-diffusion
- idx: 30
  start_sec: 1490.32
  end_sec: 1545.75
  text: 'we can also do this on runpod. So if you

    have credentials or if you have some have credentials or if you have some have
    credentials or if you have some

    budget even $6 to $7 what I''ll suggest budget even $6 to $7 what I''ll suggest
    budget even $6 to $7 what I''ll suggest

    is go to runpod click on sign in over is go to runpod click on sign in over is
    go to runpod click on sign in over

    here here here

    and uh if you sign in through Google uh what you can do is that so I have uh what
    you can do is that so I have

    around $100 here you can actually select around $100 here you can actually select
    around $100 here you can actually select

    a GPU which is very fast. So there''s a GPU which is very fast. So there''s a
    GPU which is very fast. So there''s

    something running here right now. If I something running here right now. If I
    something running here right now. If I

    click on deploy, let''s say I choose this click on deploy, let''s say I choose
    this click on deploy, let''s say I choose this

    B200 GPU which is $519 per hour, but it B200 GPU which is $519 per hour, but it
    B200 GPU which is $519 per hour, but it

    is very it has 180 GB of VRAM. H200 has is very it has 180 GB of VRAM. H200 has
    is very it has 180 GB of VRAM. H200 has

    1441 GB of VRAM. Right now I was on L40, 1441 GB of VRAM. Right now I was on L40,
    1441 GB of VRAM. Right now I was on L40,

    I think, which is 48 GB. Not too bad. I think, which is 48 GB. Not too bad. I
    think, which is 48 GB. Not too bad.

    But let''s choose B200 But let''s choose B200 But let''s choose B200

    and let me do let''s say container disk and let me do let''s say container disk
    and let me do let''s say container disk

    of 200 GB and uh volume disk of 200 GB. of 200 GB and uh volume disk of 200 GB.
    of 200 GB and uh volume disk of 200 GB.

    I''ll set overrides. Oops. I think it was'
  concept_slugs:
  - diffusion-language-model
  - masked-diffusion
- idx: 31
  start_sec: 1545.75
  end_sec: 1643.403
  text: 'I''ll set overrides. Oops. I think it was I''ll set overrides. Oops. I think
    it was

    187. Let''s do 200. And I''ll set 187. Let''s do 200. And I''ll set 187. Let''s
    do 200. And I''ll set

    overrides over here. And then I''ll click overrides over here. And then I''ll
    click overrides over here. And then I''ll click

    on deploy on demand. Um when you click on deploy on demand, Um when you click
    on deploy on demand,

    you''ll see that uh you''ll see that uh you''ll see that uh

    it will start to spin up. Okay. So now it''s still waiting for Okay. So now it''s
    still waiting for

    connection. So probably I should just uh connection. So probably I should just
    uh connection. So probably I should just uh

    uh uh uh

    Yeah. So Jupyter Lab is ready. Ready. So Yeah. So Jupyter Lab is ready. Ready.
    So Yeah. So Jupyter Lab is ready. Ready. So

    just click on this Jupyter lab just click on this Jupyter lab just click on this
    Jupyter lab

    and then it will open this Jupyter lab and then it will open this Jupyter lab
    and then it will open this Jupyter lab

    notebook environment for you and uh once this Jupyter lab environment and uh once
    this Jupyter lab environment

    is opened for you what you can do is is opened for you what you can do is is opened
    for you what you can do is

    that you can copy paste the code into that you can copy paste the code into that
    you can copy paste the code into

    this environment. [snorts] So I click on this Python 3 kernel right So I click
    on this Python 3 kernel right

    now and open this. So you can see on the now and open this. So you can see on
    the now and open this. So you can see on the

    left hand side left hand side left hand side

    um let me get my code and I''ll upload it um let me get my code and I''ll upload
    it um let me get my code and I''ll upload it

    on the left hand side over here.'
  concept_slugs:
  - diffusion-language-model
  - masked-diffusion
---
# Lecture 16: Diffusion LLM Coded from Scratch Part 1

See the structured chunks above.
