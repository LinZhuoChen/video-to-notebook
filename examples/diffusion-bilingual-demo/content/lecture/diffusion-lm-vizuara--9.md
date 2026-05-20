---
course_slug: diffusion-lm-vizuara
idx: 9
title: 'Lecture 8: Auto Regressive Models (ARM) Architecture Data-Transformer Blocks'
video_url: https://www.youtube.com/watch?v=SMcPFZdRU8g
duration_sec: null
chunks:
- idx: 0
  start_sec: 2.71
  end_sec: 50.0
  text: 'So the way a batch is constructed is as So the way a batch is constructed
    is as

    follows. Let''s say for now we just follows. Let''s say for now we just follows.
    Let''s say for now we just

    assume the batch size to be equal to assume the batch size to be equal to assume
    the batch size to be equal to

    one. So we have one input sequence and one. So we have one input sequence and
    one. So we have one input sequence and

    that input sequence is one day a little. that input sequence is one day a little.
    that input sequence is one day a little.

    This input sequence one day a little This input sequence one day a little This
    input sequence one day a little

    will have to pass through my language will have to pass through my language will
    have to pass through my language

    model. Now but remember that uh models model. Now but remember that uh models
    model. Now but remember that uh models

    machine learning models language models machine learning models language models
    machine learning models language models

    or AI models for that matter they can''t or AI models for that matter they can''t
    or AI models for that matter they can''t

    understand text right. So we need to understand text right. So we need to understand
    text right. So we need to

    somehow convert this text somehow convert this text somehow convert this text

    into into into

    um numerical format. So that''s where the um numerical format. So that''s where
    the um numerical format. So that''s where the

    first stage of the LLM architecture first stage of the LLM architecture first
    stage of the LLM architecture

    actually begins. The LLM architecture as actually begins. The LLM architecture
    as actually begins. The LLM architecture as

    a whole is divided into three stages. a whole is divided into three stages. a
    whole is divided into three stages.

    The first stage is the input stage. The The first stage is the input stage. The
    The first stage is the input stage. The

    second stage is the processor stage and second stage is the processor stage and
    second stage is the processor stage and

    the third stage is the output stage. the third stage is the output stage.'
  concept_slugs:
  - autoregressive-vs-diffusion
- idx: 1
  start_sec: 50.0
  end_sec: 89.68
  text: 'the third stage is the output stage.

    When we look at diffusion language When we look at diffusion language When we
    look at diffusion language

    models, there are changes in all of models, there are changes in all of models,
    there are changes in all of

    these three stages. So we need to these three stages. So we need to these three
    stages. So we need to

    understand all of them in detail. Let''s understand all of them in detail. Let''s
    understand all of them in detail. Let''s

    see what happens at the input stage see what happens at the input stage see what
    happens at the input stage

    first. What happens at the input stage first. What happens at the input stage
    first. What happens at the input stage

    is that we have this batch, right? Which is that we have this batch, right? Which
    is that we have this batch, right? Which

    is uh let me write it down. is uh let me write it down. is uh let me write it
    down.

    We have this input text which is once We have this input text which is once We
    have this input text which is once

    upon a time upon a time upon a time

    and this text has to flow through this and this text has to flow through this
    and this text has to flow through this

    entire architecture. I need to get some entire architecture. I need to get some
    entire architecture. I need to get some

    prediction. I need to compare it with prediction. I need to compare it with prediction.
    I need to compare it with

    the ground truth which is the target the ground truth which is the target the
    ground truth which is the target

    values which are input shifted to the values which are input shifted to the values
    which are input shifted to the

    right by one and I need to get the loss right by one and I need to get the loss
    right by one and I need to get the loss

    right that''s the goal so what happens right that''s the goal so what happens
    right that''s the goal so what happens

    first is that since the model cannot first is that since the model cannot'
  concept_slugs:
  - autoregressive-vs-diffusion
- idx: 2
  start_sec: 89.68
  end_sec: 147.27
  text: 'first is that since the model cannot

    understand text these tokens these are understand text these tokens these are
    understand text these tokens these are

    called as tokens they are converted called as tokens they are converted called
    as tokens they are converted

    or rather first the sentences the or rather first the sentences the or rather
    first the sentences the

    paragraph itself is broken down into a paragraph itself is broken down into a
    paragraph itself is broken down into a

    bunch of tokens there are several bunch of tokens there are several bunch of tokens
    there are several

    schemes to do this such as wordbased schemes to do this such as wordbased schemes
    to do this such as wordbased

    tokenizer subword tokenizer tokenizer subword tokenizer tokenizer subword tokenizer

    which is bite pair encoding. which is bite pair encoding. which is bite pair encoding.

    Um let''s not get into that but just Um let''s not get into that but just Um let''s
    not get into that but just

    imagine that tokens are subsets. So if I imagine that tokens are subsets. So if
    I imagine that tokens are subsets. So if I

    have this uh have this uh have this uh

    big paragraph every token can be one big paragraph every token can be one big
    paragraph every token can be one

    word. So let''s start with word based word. So let''s start with word based word.
    So let''s start with word based

    tokenization for explanation. However tokenization for explanation. However tokenization
    for explanation. However

    remember that the actual tokenization remember that the actual tokenization remember
    that the actual tokenization

    scheme is subword tokenization which scheme is subword tokenization which scheme
    is subword tokenization which

    means a token can be a word a character means a token can be a word a character
    means a token can be a word a character

    or a merge of characters also. or a merge of characters also. or a merge of characters
    also.

    So first what we do is we convert this So first what we do is we convert this
    So first what we do is we convert this

    tokens into token ids. So let''s say once tokens into token ids. So let''s say
    once tokens into token ids. So let''s say once

    is given a token ID of 1 then this is 12'
  concept_slugs:
  - autoregressive-vs-diffusion
- idx: 3
  start_sec: 147.27
  end_sec: 192.319
  text: 'is given a token ID of 1 then this is 12 is given a token ID of 1 then this
    is 12

    then this is 50 and this is 80. then this is 50 and this is 80. then this is 50
    and this is 80.

    These token ids are then converted into These token ids are then converted into
    These token ids are then converted into

    token embeddings. This is extremely token embeddings. This is extremely token
    embeddings. This is extremely

    important. Remember what when we saw important. Remember what when we saw important.
    Remember what when we saw

    about sentences lying in a probability about sentences lying in a probability
    about sentences lying in a probability

    distribution space. We saw that words distribution space. We saw that words distribution
    space. We saw that words

    are converted into embeddings. So what are converted into embeddings. So what
    are converted into embeddings. So what

    happens is that uh every token so let''s happens is that uh every token so let''s
    happens is that uh every token so let''s

    say we start with one day a little right say we start with one day a little right
    say we start with one day a little right

    in my batch every token is converted in my batch every token is converted in my
    batch every token is converted

    into a higher dimensional token into a higher dimensional token into a higher
    dimensional token

    embedding. embedding. embedding.

    This is my first step. So every token is This is my first step. So every token
    is This is my first step. So every token is

    converted into a vector. The whole idea converted into a vector. The whole idea
    converted into a vector. The whole idea

    is that once the language model is is that once the language model is is that
    once the language model is

    trained vectors of similar words lie trained vectors of similar words lie trained
    vectors of similar words lie

    close to each other in the vector space. close to each other in the vector space.
    close to each other in the vector space.

    So for example um when the language So for example um when the language So for
    example um when the language

    model is not trained the vectors for cat model is not trained the vectors for
    cat'
  concept_slugs:
  - autoregressive-vs-diffusion
- idx: 4
  start_sec: 192.319
  end_sec: 241.92
  text: 'model is not trained the vectors for cat

    and kitten might lie further apart from and kitten might lie further apart from
    and kitten might lie further apart from

    each other. But once the language model each other. But once the language model
    each other. But once the language model

    is fully trained the vectors for cat and is fully trained the vectors for cat
    and is fully trained the vectors for cat and

    kitten will lie closer to each other. kitten will lie closer to each other. kitten
    will lie closer to each other.

    Right? So the first step is to take Right? So the first step is to take Right?
    So the first step is to take

    these tokens and then convert them into these tokens and then convert them into
    these tokens and then convert them into

    token embeddings. The way this is create token embeddings. The way this is create
    token embeddings. The way this is create

    converted is that we maintain something converted is that we maintain something
    converted is that we maintain something

    like a vocabulary. like a vocabulary. like a vocabulary.

    So let''s look at this vocabulary now. We So let''s look at this vocabulary now.
    We So let''s look at this vocabulary now. We

    maintain something which is um where maintain something which is um where maintain
    something which is um where

    should I write this? Yeah. So we should I write this? Yeah. So we should I write
    this? Yeah. So we

    maintain something which is a maintain something which is a maintain something
    which is a

    vocabulary. vocabulary. vocabulary.

    Let me increase my text size a bit. We Let me increase my text size a bit. We
    Let me increase my text size a bit. We

    maintain a vocabulary. maintain a vocabulary. maintain a vocabulary.

    What it means is that let''s say I have What it means is that let''s say I have
    What it means is that let''s say I have

    all my words in English language in my all my words in English language in my
    all my words in English language in my

    vocabulary. So let''s say uh the etc. vocabulary. So let''s say uh the etc. vocabulary.
    So let''s say uh the etc.

    This is my whole vocabulary set. I This is my whole vocabulary set. I'
  concept_slugs:
  - autoregressive-vs-diffusion
- idx: 5
  start_sec: 241.92
  end_sec: 295.919
  text: 'This is my whole vocabulary set. I

    assign token ids to each of them. Let''s assign token ids to each of them. Let''s
    assign token ids to each of them. Let''s

    say this goes up till 100,000. This is say this goes up till 100,000. This is
    say this goes up till 100,000. This is

    my vocabulary. my vocabulary. my vocabulary.

    What I also do is I maintain a token What I also do is I maintain a token What
    I also do is I maintain a token

    embedding matrix. What a token embedding matrix is that What a token embedding
    matrix is that

    every token ID is essentially mapped to every token ID is essentially mapped to
    every token ID is essentially mapped to

    a higher dimensional vector. a higher dimensional vector. a higher dimensional
    vector.

    So if my embedding dimension is 768, So if my embedding dimension is 768, So if
    my embedding dimension is 768,

    the first the first the first

    the first token ID is mapped to a 768 the first token ID is mapped to a 768 the
    first token ID is mapped to a 768

    dimensional vector. The second token ID dimensional vector. The second token ID
    dimensional vector. The second token ID

    is mapped to a 768 dimensional vector. is mapped to a 768 dimensional vector.
    is mapped to a 768 dimensional vector.

    And similarly, the 100,000th token ID is And similarly, the 100,000th token ID
    is And similarly, the 100,000th token ID is

    mapped to a 768 dimensional vector. This mapped to a 768 dimensional vector. This
    mapped to a 768 dimensional vector. This

    is my token embedding matrix. So every is my token embedding matrix. So every
    is my token embedding matrix. So every

    time I want to retrieve the token time I want to retrieve the token time I want
    to retrieve the token

    embedding vector for a particular token embedding vector for a particular token
    embedding vector for a particular token

    ID. So let''s say one day a little ID. So let''s say one day a little ID. So let''s
    say one day a little

    corresponds to certain token ids. Right? corresponds to certain token ids. Right?
    corresponds to certain token ids. Right?

    If I want to retrieve the embedding If I want to retrieve the embedding'
  concept_slugs:
  - autoregressive-vs-diffusion
- idx: 6
  start_sec: 295.919
  end_sec: 352.8
  text: 'If I want to retrieve the embedding

    vectors for these, I just go to my token vectors for these, I just go to my token
    vectors for these, I just go to my token

    embedding matrix. I look at that embedding matrix. I look at that embedding matrix.
    I look at that

    particular ID and I retrieve the particular ID and I retrieve the particular ID
    and I retrieve the

    embedding vector for that particular embedding vector for that particular embedding
    vector for that particular

    token. token. token.

    That''s the first step. So I have my That''s the first step. So I have my That''s
    the first step. So I have my

    tokens and I have my I have the tokens and I have my I have the tokens and I have
    my I have the

    embedding vectors for each of these embedding vectors for each of these embedding
    vectors for each of these

    tokens. Right? So I convert every token tokens. Right? So I convert every token
    tokens. Right? So I convert every token

    into token embeddings. But we don''t stop into token embeddings. But we don''t
    stop into token embeddings. But we don''t stop

    here. There is also one more step which here. There is also one more step which
    here. There is also one more step which

    is called as the position embedding. is called as the position embedding. is called
    as the position embedding.

    What it means is that the place where a What it means is that the place where
    a What it means is that the place where a

    token appears in a sentence that also token appears in a sentence that also token
    appears in a sentence that also

    makes a big difference. For example, if makes a big difference. For example, if
    makes a big difference. For example, if

    you have sentence such as the you have sentence such as the you have sentence
    such as the

    dog dog dog

    chased the ball chased the ball chased the ball

    and it it could not catch it. Okay. Now this it it could not catch it. Okay. Now
    this it

    and this it they are the same tokens or and this it they are the same tokens or
    and this it they are the same tokens or

    the same words. So their token embedding the same words. So their token embedding'
  concept_slugs:
  - autoregressive-vs-diffusion
- idx: 7
  start_sec: 352.8
  end_sec: 405.84
  text: 'the same words. So their token embedding

    vectors will be the same but they come vectors will be the same but they come
    vectors will be the same but they come

    at different positions, right? So their at different positions, right? So their
    at different positions, right? So their

    position embedding vectors have to be position embedding vectors have to be position
    embedding vectors have to be

    different. So along with the token different. So along with the token different.
    So along with the token

    embedding matrix, we also maintain a embedding matrix, we also maintain a embedding
    matrix, we also maintain a

    position embedding matrix. Now the difference here is that the Now the difference
    here is that the

    token embedding matrix has number of token embedding matrix has number of token
    embedding matrix has number of

    rows equal to my vocabulary size because rows equal to my vocabulary size because
    rows equal to my vocabulary size because

    I need a token embedding vector for each I need a token embedding vector for each
    I need a token embedding vector for each

    token or each word in my vocabulary. But token or each word in my vocabulary.
    But token or each word in my vocabulary. But

    the position embedding matrix the number the position embedding matrix the number
    the position embedding matrix the number

    of rows is equal to my sequence length of rows is equal to my sequence length
    of rows is equal to my sequence length

    or my context length. So if my input or my context length. So if my input or my
    context length. So if my input

    sequence is of a length 1024 then my uh number of rows here will be then my uh
    number of rows here will be

    1024 because I I just need an embedding 1024 because I I just need an embedding
    1024 because I I just need an embedding

    vector for each position and how many vector for each position and how many vector
    for each position and how many

    positions will be there. The number of positions will be there. The number of
    positions will be there. The number of

    the sequence length or my context the sequence length or my context the sequence
    length or my context

    length. So this goes from one to right length. So this goes from one to right'
  concept_slugs:
  - autoregressive-vs-diffusion
- idx: 8
  start_sec: 405.84
  end_sec: 464.08
  text: 'length. So this goes from one to right

    up to the sequence length. And I have a up to the sequence length. And I have
    a up to the sequence length. And I have a

    768 dimensional vector for my position 768 dimensional vector for my position
    768 dimensional vector for my position

    embedding. Let me mark this with a embedding. Let me mark this with a embedding.
    Let me mark this with a

    different color. different color. different color.

    So I have a 768 dimensional vector for So I have a 768 dimensional vector for
    So I have a 768 dimensional vector for

    each each of my position also. So 768 each each of my position also. So 768 each
    each of my position also. So 768

    dimensional vector for each of my dimensional vector for each of my dimensional
    vector for each of my

    positions. Okay. So remember that this dimension Okay. So remember that this dimension

    and this dimension has to be the same and this dimension has to be the same and
    this dimension has to be the same

    because we are going to add them. So if because we are going to add them. So if
    because we are going to add them. So if

    we have we have we have

    one day a little that''s my input one day a little that''s my input one day a
    little that''s my input

    sequence we first convert it into token sequence we first convert it into token
    sequence we first convert it into token

    embeddings then uh so one comes at embeddings then uh so one comes at embeddings
    then uh so one comes at

    position number one right so I look at position number one right so I look at
    position number one right so I look at

    position number one position number one position number one

    I look at position number one I take its I look at position number one I take
    its I look at position number one I take its

    embedding vector and then I add it embedding vector and then I add it embedding
    vector and then I add it

    um I add it over here so this is the vector I add it over here so this is the
    vector

    corresponding to position one this is corresponding to position one this is'
  concept_slugs:
  - autoregressive-vs-diffusion
- idx: 9
  start_sec: 464.08
  end_sec: 508.56
  text: 'corresponding to position one this is

    the vector vector corresponding to the vector vector corresponding to the vector
    vector corresponding to

    position two, vector corresponding to position two, vector corresponding to position
    two, vector corresponding to

    position three and vector corresponding position three and vector corresponding
    position three and vector corresponding

    to position four. Right? So then we add to position four. Right? So then we add
    to position four. Right? So then we add

    the token embeddings and the position the token embeddings and the position the
    token embeddings and the position

    embeddings together. Since the dimension embeddings together. Since the dimension
    embeddings together. Since the dimension

    is the same, we add the token embedding is the same, we add the token embedding
    is the same, we add the token embedding

    and the position embedding. So input and the position embedding. So input and
    the position embedding. So input

    embedding is token embedding plus embedding is token embedding plus embedding
    is token embedding plus

    position embedding. So token plus position embedding. So token plus position embedding.
    So token plus

    position input embeddings for each of my position input embeddings for each of
    my position input embeddings for each of my

    tokens, right? And this input embedding tokens, right? And this input embedding
    tokens, right? And this input embedding

    is the one which then passes through the is the one which then passes through
    the is the one which then passes through the

    second block which is my processor second block which is my processor second block
    which is my processor

    block. Now block. Now block. Now

    um so once we come out of the data block um so once we come out of the data block
    um so once we come out of the data block

    I have come out of the data block right I have come out of the data block right
    I have come out of the data block right

    now the next step is for me is to go now the next step is for me is to go now
    the next step is for me is to go

    into the processor block. This processor into the processor block. This processor
    into the processor block. This processor

    block is where all the magic happens. So block is where all the magic happens.
    So'
  concept_slugs:
  - autoregressive-vs-diffusion
- idx: 10
  start_sec: 508.56
  end_sec: 553.829
  text: 'block is where all the magic happens. So

    initially we started out by uh thinking initially we started out by uh thinking
    initially we started out by uh thinking

    that how will the model learn the that how will the model learn the that how will
    the model learn the

    patterns from the data? It almost feels patterns from the data? It almost feels
    patterns from the data? It almost feels

    like magic right? How will it learn the like magic right? How will it learn the
    like magic right? How will it learn the

    underlying form of the language? How underlying form of the language? How underlying
    form of the language? How

    will it learn the underlying meaning? will it learn the underlying meaning? will
    it learn the underlying meaning?

    How will it understand grammar just from How will it understand grammar just from
    How will it understand grammar just from

    sentences? sentences? sentences?

    Up till now all we have done is that we Up till now all we have done is that we
    Up till now all we have done is that we

    have taken our huge amount of data. We have taken our huge amount of data. We
    have taken our huge amount of data. We

    have broken it down into tokens. Um you have broken it down into tokens. Um you
    have broken it down into tokens. Um you

    have converted tokens into token have converted tokens into token have converted
    tokens into token

    embeddings, added positional embeddings embeddings, added positional embeddings
    embeddings, added positional embeddings

    and have input embeddings. And the input and have input embeddings. And the input
    and have input embeddings. And the input

    embeddings are passed through the embeddings are passed through the embeddings
    are passed through the

    architecture. But we have not yet architecture. But we have not yet architecture.
    But we have not yet

    formulated the brain formulated the brain formulated the brain

    um of the language model architecture. um of the language model architecture.
    um of the language model architecture.

    The brain of the language model The brain of the language model The brain of the
    language model

    architecture is something which is architecture is something which is architecture
    is something which is

    called as the transformer block which we called as the transformer block which
    we called as the transformer block which we

    are also calling processor here.'
  concept_slugs:
  - autoregressive-vs-diffusion
- idx: 11
  start_sec: 553.829
  end_sec: 598.0
  text: 'are also calling processor here. are also calling processor here.

    This transformer block consists of all This transformer block consists of all
    This transformer block consists of all

    of these components which we are now of these components which we are now of these
    components which we are now

    going to go through separately. Right? going to go through separately. Right?
    going to go through separately. Right?

    The transformer block essentially has The transformer block essentially has The
    transformer block essentially has

    six major components which all of you six major components which all of you six
    major components which all of you

    need to be aware of. The first is the need to be aware of. The first is the need
    to be aware of. The first is the

    layer normalization. Second is multi layer normalization. Second is multi layer
    normalization. Second is multi

    head attention. Third is dropout. Then head attention. Third is dropout. Then
    head attention. Third is dropout. Then

    fourth is another layer normalization. fourth is another layer normalization.
    fourth is another layer normalization.

    Fifth is a feed forward neural network. Fifth is a feed forward neural network.
    Fifth is a feed forward neural network.

    And then we have another dropout. And then we have another dropout. And then we
    have another dropout.

    Interspersed with all of these Interspersed with all of these Interspersed with
    all of these

    components, we have these plus symbols components, we have these plus symbols
    components, we have these plus symbols

    which are essentially called as shortcut which are essentially called as shortcut
    which are essentially called as shortcut

    connections. connections. connections.

    When you merge all of these blocks When you merge all of these blocks When you
    merge all of these blocks

    together, it leads to a transformer together, it leads to a transformer together,
    it leads to a transformer

    block. So as you can see the transformer block. So as you can see the transformer
    block. So as you can see the transformer

    block is modular. We have layer block is modular. We have layer block is modular.
    We have layer

    normalization followed by multi head normalization followed by multi head normalization
    followed by multi head

    attention followed by dropout followed attention followed by dropout followed
    attention followed by dropout followed

    by another layer normalization followed by another layer normalization followed'
  concept_slugs:
  - autoregressive-vs-diffusion
- idx: 12
  start_sec: 598.0
  end_sec: 646.8
  text: 'by another layer normalization followed

    by feed forward followed by dropout. The by feed forward followed by dropout.
    The by feed forward followed by dropout. The

    good thing is that the transformer good thing is that the transformer good thing
    is that the transformer

    architecture mostly stays exactly the architecture mostly stays exactly the architecture
    mostly stays exactly the

    same considering language model and same considering language model and same considering
    language model and

    diffusion language models or considering diffusion language models or considering
    diffusion language models or considering

    auto reggressive models and diffusion auto reggressive models and diffusion auto
    reggressive models and diffusion

    language models. The only change language models. The only change language models.
    The only change

    essentially happens in the multi head essentially happens in the multi head essentially
    happens in the multi head

    attention part where instead of having a attention part where instead of having
    a attention part where instead of having a

    causal attention for auto reggressive causal attention for auto reggressive causal
    attention for auto reggressive

    models, we have the full attention mask models, we have the full attention mask
    models, we have the full attention mask

    for the diffusion language models. We''ll for the diffusion language models. We''ll
    for the diffusion language models. We''ll

    look at this in detail. So no need to look at this in detail. So no need to look
    at this in detail. So no need to

    worry about this right now. So let''s worry about this right now. So let''s worry
    about this right now. So let''s

    start going through each of these blocks start going through each of these blocks
    start going through each of these blocks

    separately. separately. separately.

    Uh once we have the input embeddings as Uh once we have the input embeddings as
    Uh once we have the input embeddings as

    I mentioned now we are we are entering I mentioned now we are we are entering
    I mentioned now we are we are entering

    the transformer. the transformer. the transformer.

    The first thing in the transformer is The first thing in the transformer is The
    first thing in the transformer is

    layer normalization. What this means is layer normalization. What this means is
    layer normalization. What this means is

    that so now the input tokens let''s say that so now the input tokens let''s say'
  concept_slugs:
  - autoregressive-vs-diffusion
- idx: 13
  start_sec: 646.8
  end_sec: 688.23
  text: 'that so now the input tokens let''s say

    so ideally we should we should have so ideally we should we should have so ideally
    we should we should have

    continued with the same one day a little continued with the same one day a little
    continued with the same one day a little

    but uh for some reason now it''s every but uh for some reason now it''s every
    but uh for some reason now it''s every

    effort moves you. It''s fine. I just want effort moves you. It''s fine. I just
    want effort moves you. It''s fine. I just want

    to illustrate the concept over here. So to illustrate the concept over here. So
    to illustrate the concept over here. So

    these are my input embeddings. What these are my input embeddings. What these
    are my input embeddings. What

    layer normalization does is that for layer normalization does is that for layer
    normalization does is that for

    every vector we subtract the mean and every vector we subtract the mean and every
    vector we subtract the mean and

    divide with the square root of variance. divide with the square root of variance.
    divide with the square root of variance.

    So we make sure that for each vector the So we make sure that for each vector
    the So we make sure that for each vector the

    mean is equal to zero and variance equal mean is equal to zero and variance equal
    mean is equal to zero and variance equal

    to one. For this vector mean is zero, to one. For this vector mean is zero, to
    one. For this vector mean is zero,

    variance is one. For this vector mean is variance is one. For this vector mean
    is variance is one. For this vector mean is

    0, variance is one etc. So this is a per 0, variance is one etc. So this is a
    per 0, variance is one etc. So this is a per

    vector operation or a per token vector operation or a per token vector operation
    or a per token

    operation. Actually from every vector we operation. Actually from every vector
    we operation. Actually from every vector we

    subtract the mean and divide by square subtract the mean and divide by square
    subtract the mean and divide by square

    root of variance. Why do we do this?'
  concept_slugs:
  - autoregressive-vs-diffusion
- idx: 14
  start_sec: 688.23
  end_sec: 737.19
  text: 'root of variance. Why do we do this? root of variance. Why do we do this?

    Because normalization really helps the Because normalization really helps the
    Because normalization really helps the

    back propagation. It leads to stable uh back propagation. It leads to stable uh
    back propagation. It leads to stable uh

    gradients when we are doing back gradients when we are doing back gradients when
    we are doing back

    propagation. It also reduces this propagation. It also reduces this propagation.
    It also reduces this

    problem of internal coariant shift which problem of internal coariant shift which
    problem of internal coariant shift which

    is the model really does not like if the is the model really does not like if
    the is the model really does not like if the

    distribution of the incoming data is distribution of the incoming data is distribution
    of the incoming data is

    different each time. So we just make different each time. So we just make different
    each time. So we just make

    sure the mean is zero and variance equal sure the mean is zero and variance equal
    sure the mean is zero and variance equal

    to one. You''ll see that throughout the to one. You''ll see that throughout the
    to one. You''ll see that throughout the

    transformer architecture we have two transformer architecture we have two transformer
    architecture we have two

    layer normalizations which actually are layer normalizations which actually are
    layer normalizations which actually are

    doing the exact same thing. doing the exact same thing. doing the exact same thing.

    Um let me mark these normalization Um let me mark these normalization Um let me
    mark these normalization

    layers for you. Right now we have this layers for you. Right now we have this
    layers for you. Right now we have this

    first layer normalization over here and first layer normalization over here and
    first layer normalization over here and

    we have this second layer normalization we have this second layer normalization
    we have this second layer normalization

    over here. But both of these do the over here. But both of these do the over here.
    But both of these do the

    exact same thing. exact same thing. exact same thing.

    That''s my first layer which is the layer That''s my first layer which is the
    layer That''s my first layer which is the layer

    normalization. The second block which I'
  concept_slugs:
  - autoregressive-vs-diffusion
- idx: 15
  start_sec: 737.19
  end_sec: 791.92
  text: 'normalization. The second block which I normalization. The second block which
    I

    want to emphasize a lot over here. This want to emphasize a lot over here. This
    want to emphasize a lot over here. This

    block is called as the multi head block is called as the multi head block is called
    as the multi head

    attention block. And this is the true attention block. And this is the true attention
    block. And this is the true

    innovation which powers innovation which powers innovation which powers

    transformers. Here the model learns transformers. Here the model learns transformers.
    Here the model learns

    context. The model learns how sentences context. The model learns how sentences
    context. The model learns how sentences

    are related to what comes in the past. are related to what comes in the past.
    are related to what comes in the past.

    Right? Right? Right?

    Here the model acquires true Here the model acquires true Here the model acquires
    true

    intelligence and it captures patterns intelligence and it captures patterns intelligence
    and it captures patterns

    between my current sentence and what between my current sentence and what between
    my current sentence and what

    comes in the past. So as the name comes in the past. So as the name comes in the
    past. So as the name

    suggests what attention means is that if suggests what attention means is that
    if suggests what attention means is that if

    I have multiple sentences right in a I have multiple sentences right in a I have
    multiple sentences right in a

    batch or multiple input sequences or batch or multiple input sequences or batch
    or multiple input sequences or

    rather to keep it simple in one input rather to keep it simple in one input rather
    to keep it simple in one input

    sequence if I have multiple tokens sequence if I have multiple tokens sequence
    if I have multiple tokens

    attention actually quantifies how much attention actually quantifies how much
    attention actually quantifies how much

    attention I need to pay each token in attention I need to pay each token in attention
    I need to pay each token in

    that that that

    uh so for example let me take an input uh so for example let me take an input
    uh so for example let me take an input

    sequence which says uh Harry Potter daughter'
  concept_slugs:
  - autoregressive-vs-diffusion
- idx: 16
  start_sec: 791.92
  end_sec: 845.11
  text: 'Harry Potter daughter

    or Harry lived or Harry lived or Harry lived

    at Hogwarts and he so let''s say this is my input and he so let''s say this is
    my input

    sequence if I want to complete this sequence if I want to complete this sequence
    if I want to complete this

    sequence if I want to predict what comes sequence if I want to predict what comes
    sequence if I want to predict what comes

    later later later

    uh it''s a next token prediction task uh it''s a next token prediction task uh
    it''s a next token prediction task

    right so I need to look at this and right so I need to look at this and right
    so I need to look at this and

    predict next but he now corresponds to predict next but he now corresponds to
    predict next but he now corresponds to

    Harry the model needs to know that the Harry the model needs to know that the
    Harry the model needs to know that the

    model needs to know that to predict the model needs to know that to predict the
    model needs to know that to predict the

    next token next token next token

    I need to give more attention to Harry I need to give more attention to Harry
    I need to give more attention to Harry

    because he corresponds to Harry. This is because he corresponds to Harry. This
    is because he corresponds to Harry. This is

    the core essence of what the attention the core essence of what the attention
    the core essence of what the attention

    mechanism is trying to do. The attention mechanism is trying to do. The attention
    mechanism is trying to do. The attention

    mechanism mechanism mechanism

    essentially says that until now until essentially says that until now until essentially
    says that until now until

    now in this entire architecture we have now in this entire architecture we have
    now in this entire architecture we have

    looked at every token separately. Right? looked at every token separately. Right?
    looked at every token separately. Right?

    We have looked at each token and We have looked at each token and We have looked
    at each token and

    performed token level operations. But we performed token level operations. But
    we performed token level operations. But we

    have not linked one token to another'
  concept_slugs:
  - autoregressive-vs-diffusion
- idx: 17
  start_sec: 845.11
  end_sec: 898.32
  text: 'have not linked one token to another have not linked one token to another

    token anywhere. Even this uh layer token anywhere. Even this uh layer token anywhere.
    Even this uh layer

    normalization is an operation per token normalization is an operation per token
    normalization is an operation per token

    on each token separately. It does not on each token separately. It does not on
    each token separately. It does not

    link two tokens with each other. But to link two tokens with each other. But to
    link two tokens with each other. But to

    capture the context correctly, we really capture the context correctly, we really
    capture the context correctly, we really

    need to need to need to

    where is my Harry sentence now? Uh to where is my Harry sentence now? Uh to where
    is my Harry sentence now? Uh to

    capture the context correctly, we really capture the context correctly, we really

    need to link tokens with each other. need to link tokens with each other. need
    to link tokens with each other.

    Meanwhile, let me see where I''ve Meanwhile, let me see where I''ve Meanwhile,
    let me see where I''ve

    written. written. written.

    Yeah, Harry lived at Hogwarts, right? So Yeah, Harry lived at Hogwarts, right?
    So Yeah, Harry lived at Hogwarts, right? So

    we need to link a token with its we need to link a token with its we need to link
    a token with its

    neighbors and that''s exactly what the neighbors and that''s exactly what the
    neighbors and that''s exactly what the

    multi head attention actually does. multi head attention actually does. multi
    head attention actually does.

    So to explain the concept of multi head So to explain the concept of multi head
    So to explain the concept of multi head

    attention I need to take a slight detour attention I need to take a slight detour
    attention I need to take a slight detour

    which I am going to take right now which I am going to take right now which I
    am going to take right now

    because uh some of the concepts here because uh some of the concepts here because
    uh some of the concepts here

    will be very relevant for understanding will be very relevant for understanding
    will be very relevant for understanding

    the mask diffusion models as well. So the mask diffusion models as well. So'
  concept_slugs:
  - autoregressive-vs-diffusion
- idx: 18
  start_sec: 898.32
  end_sec: 937.199
  text: 'the mask diffusion models as well. So

    let''s understand this attention let''s understand this attention let''s understand
    this attention

    mechanism and what it''s actually doing mechanism and what it''s actually doing
    mechanism and what it''s actually doing

    in lot of detail. This module will take in lot of detail. This module will take
    in lot of detail. This module will take

    the most amount of time because the the most amount of time because the the most
    amount of time because the

    modules which come after the attention modules which come after the attention
    modules which come after the attention

    mechanism are fairly straightforward mechanism are fairly straightforward mechanism
    are fairly straightforward

    traditional models in deep learning. The traditional models in deep learning.
    The traditional models in deep learning. The

    reason I''m going deep into the attention reason I''m going deep into the attention
    reason I''m going deep into the attention

    mechanism is because mechanism is because mechanism is because

    if you see this uh if you see this uh if you see this uh

    um attention weights we are going to um attention weights we are going to um attention
    weights we are going to

    have something like a mask which differs have something like a mask which differs
    have something like a mask which differs

    between auto reggressive models and between auto reggressive models and between
    auto reggressive models and

    diffusion models. So that''s why it''s diffusion models. So that''s why it''s
    diffusion models. So that''s why it''s

    important for us to go into the details important for us to go into the details
    important for us to go into the details

    of attention mechanism, how it works and of attention mechanism, how it works
    and of attention mechanism, how it works and

    how it essentially captures context.'
  concept_slugs:
  - autoregressive-vs-diffusion
---
# Lecture 8: Auto Regressive Models (ARM) Architecture Data-Transformer Blocks

See the structured chunks above.
