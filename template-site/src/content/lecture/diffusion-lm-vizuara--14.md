---
course_slug: diffusion-lm-vizuara
idx: 14
title: 'Lecture 13: Diffusion LLM Training Pipeline'
video_url: https://www.youtube.com/watch?v=rUGQP6bcMiw
duration_sec: null
chunks:
- idx: 0
  start_sec: 4.309
  end_sec: 61.99
  text: 'Okay. So the next step in these key Okay. So the next step in these key

    characteristics which we mentioned and characteristics which we mentioned and
    characteristics which we mentioned and

    probably that''s the most important step probably that''s the most important step
    probably that''s the most important step

    is this noise prediction. Right. is this noise prediction. Right. is this noise
    prediction. Right.

    Basically we need a model Basically we need a model Basically we need a model

    which can help us predict the noise in which can help us predict the noise in
    which can help us predict the noise in

    the noising process the noising process the noising process

    because the whole idea is as follows. because the whole idea is as follows. because
    the whole idea is as follows.

    Right? If you take a look at this video, if you take a look at this video again,
    if you take a look at this video again,

    what we want to do is that when we start what we want to do is that when we start
    what we want to do is that when we start

    rotating the fluid slowly, we want to rotating the fluid slowly, we want to rotating
    the fluid slowly, we want to

    predict how much noise is added at each predict how much noise is added at each
    predict how much noise is added at each

    step. So that during dinoising, it will step. So that during dinoising, it will
    step. So that during dinoising, it will

    it will help us recover the original it will help us recover the original it will
    help us recover the original

    state. state. state.

    So at each step of the noising process, So at each step of the noising process,
    So at each step of the noising process,

    how can we predict the amount of noise how can we predict the amount of noise
    how can we predict the amount of noise

    which is added? The way this is done in which is added? The way this is done in
    which is added? The way this is done in

    in the case of images is that in the case of images is that in the case of images
    is that

    you take a noisy image. you take a noisy image. you take a noisy image.

    You take a noisy image.'
  concept_slugs:
  - diffusion-language-model
  - masked-diffusion
- idx: 1
  start_sec: 61.99
  end_sec: 104.469
  text: 'You take a noisy image. You take a noisy image.

    Let''s say this is a noisy image of a Let''s say this is a noisy image of a Let''s
    say this is a noisy image of a

    panda which is the example which we have panda which is the example which we have
    panda which is the example which we have

    been seeing. You take a noisy image and been seeing. You take a noisy image and
    been seeing. You take a noisy image and

    then you use a noise prediction model then you use a noise prediction model then
    you use a noise prediction model

    which is a unit model to predict the which is a unit model to predict the which
    is a unit model to predict the

    noise. How does the unit model work? noise. How does the unit model work? noise.
    How does the unit model work?

    Well, it''s a combination of Well, it''s a combination of Well, it''s a combination
    of

    CNN which is convolutional neural CNN which is convolutional neural CNN which
    is convolutional neural

    network upsampling and down sampling network upsampling and down sampling network
    upsampling and down sampling

    layer. So it can extract features from layer. So it can extract features from
    layer. So it can extract features from

    the image. So it can identify what''s the image. So it can identify what''s the
    image. So it can identify what''s

    noise and what''s not. We''ll also we also noise and what''s not. We''ll also
    we also noise and what''s not. We''ll also we also

    know the actual noise right during know the actual noise right during know the
    actual noise right during

    training. So we can predict whether the training. So we can predict whether the
    training. So we can predict whether the

    predicted noise is actually close to the predicted noise is actually close to
    the predicted noise is actually close to the

    actual noise. So loss function is actual noise. So loss function is actual noise.
    So loss function is

    defined based on the predicted noise and defined based on the predicted noise
    and defined based on the predicted noise and

    the actual noise. So we need a loss the actual noise. So we need a loss the actual
    noise. So we need a loss

    function, right? We need to predict the'
  concept_slugs:
  - diffusion-language-model
  - masked-diffusion
- idx: 2
  start_sec: 104.469
  end_sec: 164.16
  text: 'function, right? We need to predict the function, right? We need to predict
    the

    noise and then we need to compare it noise and then we need to compare it noise
    and then we need to compare it

    with the actual noise. Essentially we we with the actual noise. Essentially we
    we with the actual noise. Essentially we we

    need a model which can predict the noise need a model which can predict the noise
    need a model which can predict the noise

    added during the noising process and added during the noising process and added
    during the noising process and

    compare it with some true value. What is compare it with some true value. What
    is compare it with some true value. What is

    such model in the case of text? I want such model in the case of text? I want
    such model in the case of text? I want

    you all to take a pause at this moment you all to take a pause at this moment
    you all to take a pause at this moment

    and think about it yourself. Let''s say and think about it yourself. Let''s say
    and think about it yourself. Let''s say

    you have this noisy input text, right? you have this noisy input text, right?
    you have this noisy input text, right?

    which is uh which is uh which is uh

    uh uh uh

    the the the

    so the next day is bright and we are so the next day is bright and we are so the
    next day is bright and we are

    masking next and is so it''s the masking next and is so it''s the masking next
    and is so it''s the

    mask mask mask

    day day day

    mask and bright mask and bright mask and bright

    now that''s my input sequence right now now that''s my input sequence right now
    now that''s my input sequence right now

    okay okay okay

    and uh so this is my input sequence this and uh so this is my input sequence this
    and uh so this is my input sequence this

    is mask and uh this is mask. Okay. is mask and uh this is mask. Okay. is mask
    and uh this is mask. Okay.

    How do I predict the true values here? How do I predict the true values here?'
  concept_slugs:
  - diffusion-language-model
  - masked-diffusion
- idx: 3
  start_sec: 164.16
  end_sec: 221.92
  text: 'How do I predict the true values here?

    So what I want to do what does it mean So what I want to do what does it mean
    So what I want to do what does it mean

    prediction of noise? I somehow want to prediction of noise? I somehow want to
    prediction of noise? I somehow want to

    predict predict predict

    the true tokens the true tokens the true tokens

    at the places This is exactly what is done in images This is exactly what is done
    in images

    also. Right? What what does it mean to also. Right? What what does it mean to
    also. Right? What what does it mean to

    predict the noise from a noisy image? It predict the noise from a noisy image?
    It predict the noise from a noisy image? It

    just means that we need to predict how just means that we need to predict how
    just means that we need to predict how

    we go from the noisy image to the clean we go from the noisy image to the clean
    we go from the noisy image to the clean

    image. This is exactly what we are doing over This is exactly what we are doing
    over

    here. We need to predict how to go from here. We need to predict how to go from
    here. We need to predict how to go from

    this noisy text to the clean text. So we this noisy text to the clean text. So
    we this noisy text to the clean text. So we

    need to predict what''s the text which need to predict what''s the text which
    need to predict what''s the text which

    was here in the first place. was here in the first place. was here in the first
    place.

    Again, I invite you to pause this video Again, I invite you to pause this video
    Again, I invite you to pause this video

    at this moment and think about it. at this moment and think about it. at this
    moment and think about it.

    How do you know what the true token was How do you know what the true token was
    How do you know what the true token was

    at this position? And how do you get the at this position? And how do you get
    the'
  concept_slugs:
  - diffusion-language-model
  - masked-diffusion
- idx: 4
  start_sec: 221.92
  end_sec: 272.32
  text: 'at this position? And how do you get the

    loss function? loss function? loss function?

    Well, the answer is extremely simple, Well, the answer is extremely simple, Well,
    the answer is extremely simple,

    right? Because we we already know what right? Because we we already know what
    right? Because we we already know what

    the true tokens are. We know that here the true tokens are. We know that here
    the true tokens are. We know that here

    the true token is next and we know that the true token is next and we know that
    the true token is next and we know that

    here the true token is is, here the true token is is, here the true token is is,

    right? Then how do we get the loss right? Then how do we get the loss right? Then
    how do we get the loss

    function? We have exactly seen how to function? We have exactly seen how to function?
    We have exactly seen how to

    propagate this input sequence through my propagate this input sequence through
    my propagate this input sequence through my

    model model model

    and I''ll get my predictions right. I''ll and I''ll get my predictions right.
    I''ll and I''ll get my predictions right. I''ll

    get my predictions get my predictions get my predictions

    for the next I''ll get my predictions for for the next I''ll get my predictions
    for for the next I''ll get my predictions for

    each of these. each of these. each of these.

    So I''ll get the next token prediction So I''ll get the next token prediction
    So I''ll get the next token prediction

    for the I''ll get the next token for the I''ll get the next token for the I''ll
    get the next token

    prediction for this mask. I''ll get the prediction for this mask. I''ll get the
    prediction for this mask. I''ll get the

    next token prediction for day. I''ll get next token prediction for day. I''ll
    get next token prediction for day. I''ll get

    the next token for mask and I''ll get the the next token for mask and I''ll get
    the the next token for mask and I''ll get the

    next token prediction for bride. next token prediction for bride. next token prediction
    for bride.

    Right. So the next token which is Right. So the next token which is'
  concept_slugs:
  - diffusion-language-model
  - masked-diffusion
- idx: 5
  start_sec: 272.32
  end_sec: 325.27
  text: 'Right. So the next token which is

    predicted at this position I''ll compare it with the true next token I''ll compare
    it with the true next token

    which should be next. which should be next. which should be next.

    The next token which is predicted at The next token which is predicted at The
    next token which is predicted at

    this position. I''ll compare it with the this position. I''ll compare it with
    the this position. I''ll compare it with the

    true next token which is bright. true next token which is bright. true next token
    which is bright.

    And I''ll use this to compute my loss And I''ll use this to compute my loss And
    I''ll use this to compute my loss

    function. So this is L1 and this is L2. function. So this is L1 and this is L2.
    function. So this is L1 and this is L2.

    So my loss function will then be L1 + L2 So my loss function will then be L1 +
    L2 So my loss function will then be L1 + L2

    / 2. Think about this for a moment, right? We Think about this for a moment, right?
    We

    are corrupting the text. We are masking are corrupting the text. We are masking
    are corrupting the text. We are masking

    it. I''m just passing the whole input it. I''m just passing the whole input it.
    I''m just passing the whole input

    sequence with the masks through the sequence with the masks through the sequence
    with the masks through the

    architecture and I''m getting the architecture and I''m getting the architecture
    and I''m getting the

    predictions. Why? How do I know I get predictions. Why? How do I know I get predictions.
    Why? How do I know I get

    the predictions? Because this is exactly the predictions? Because this is exactly
    the predictions? Because this is exactly

    what we saw in ARMs. If you see, if you what we saw in ARMs. If you see, if you
    what we saw in ARMs. If you see, if you

    remember what we saw in ARMs, remember what we saw in ARMs, remember what we saw
    in ARMs,

    in ARMs, for every input, we are getting in ARMs, for every input, we are getting
    in ARMs, for every input, we are getting

    predictions, right? For the next, these'
  concept_slugs:
  - diffusion-language-model
  - masked-diffusion
- idx: 6
  start_sec: 325.27
  end_sec: 371.52
  text: 'predictions, right? For the next, these predictions, right? For the next,
    these

    are my predictions. are my predictions. are my predictions.

    These are my predictions. I''m just going These are my predictions. I''m just
    going These are my predictions. I''m just going

    to compare the predictions for my mask to compare the predictions for my mask
    to compare the predictions for my mask

    with the true tokens with the true tokens with the true tokens

    and I''m going to get the loss function. and I''m going to get the loss function.
    and I''m going to get the loss function.

    It''s as simple as that. So I''ll compare It''s as simple as that. So I''ll compare
    It''s as simple as that. So I''ll compare

    the predicted token at this position. the predicted token at this position. the
    predicted token at this position.

    I''ll compare it with the true token at I''ll compare it with the true token at
    I''ll compare it with the true token at

    this position. I''ll get the predicted this position. I''ll get the predicted
    this position. I''ll get the predicted

    token at this position. I''ll compare it token at this position. I''ll compare
    it token at this position. I''ll compare it

    with the true token at this position. with the true token at this position. with
    the true token at this position.

    And then I''ll get the loss function And then I''ll get the loss function And
    then I''ll get the loss function

    based on the predicted token and the based on the predicted token and the based
    on the predicted token and the

    true token. And then I''ll take an true token. And then I''ll take an true token.
    And then I''ll take an

    average of these losses. That''s the average of these losses. That''s the average
    of these losses. That''s the

    model which I''m going to use. So in model which I''m going to use. So in model
    which I''m going to use. So in

    simple way the model which predicts the simple way the model which predicts the
    simple way the model which predicts the

    this model which predicts the noise this model which predicts the noise this model
    which predicts the noise

    right which is the second right which is the second right which is the second

    um second characteristics the model um second characteristics the model'
  concept_slugs:
  - diffusion-language-model
  - masked-diffusion
- idx: 7
  start_sec: 371.52
  end_sec: 434.95
  text: 'um second characteristics the model

    which predicts the noise which was a which predicts the noise which was a which
    predicts the noise which was a

    unit in the case of diffusion for unit in the case of diffusion for unit in the
    case of diffusion for

    images. This model is nothing but a images. This model is nothing but a images.
    This model is nothing but a

    transformer. is the or I should say the language is the or I should say the language

    model architecture itself. We are going to see this architecture We are going
    to see this architecture

    now just in a moment. But this now just in a moment. But this now just in a moment.
    But this

    architecture which I''m showing on on architecture which I''m showing on on architecture
    which I''m showing on on

    this side that is the model which this side that is the model which this side
    that is the model which

    predicts the noise. Okay. So now I''m predicts the noise. Okay. So now I''m predicts
    the noise. Okay. So now I''m

    just going to just going to just going to

    uh take you through this entire model uh take you through this entire model uh
    take you through this entire model

    because you''ll see that most of it because you''ll see that most of it because
    you''ll see that most of it

    actually remains exactly the same. Here actually remains exactly the same. Here
    actually remains exactly the same. Here

    we have the input in the ARM we have the input in the ARM we have the input in
    the ARM

    architecture. We saw that there is a architecture. We saw that there is a architecture.
    We saw that there is a

    input, processor and output. Here also input, processor and output. Here also
    input, processor and output. Here also

    there will be an input, processor and there will be an input, processor and there
    will be an input, processor and

    output. Here also there is a transformer output. Here also there is a transformer
    output. Here also there is a transformer

    block. Many things remain exactly the block. Many things remain exactly the block.
    Many things remain exactly the

    same. Let''s see what the differences same. Let''s see what the differences same.
    Let''s see what the differences

    are. Right? In the ARM architecture, we'
  concept_slugs:
  - diffusion-language-model
  - masked-diffusion
- idx: 8
  start_sec: 434.95
  end_sec: 486.56
  text: 'are. Right? In the ARM architecture, we are. Right? In the ARM architecture,
    we

    remember we had the uh token embedding remember we had the uh token embedding
    remember we had the uh token embedding

    and position embedding. We added them and position embedding. We added them and
    position embedding. We added them

    for the input sequences. Right? In the for the input sequences. Right? In the
    for the input sequences. Right? In the

    case of uh case of uh case of uh

    uh diffusion models, the first change uh diffusion models, the first change uh
    diffusion models, the first change

    which happens is that in these token which happens is that in these token which
    happens is that in these token

    embeddings, one or more of these tokens embeddings, one or more of these tokens
    embeddings, one or more of these tokens

    are masked. So this is masked. are masked. So this is masked. are masked. So this
    is masked.

    That''s what we have already seen. So That''s what we have already seen. So That''s
    what we have already seen. So

    token embeddings, it''s masked. Position token embeddings, it''s masked. Position
    token embeddings, it''s masked. Position

    embeddings, these remain the same. Here embeddings, these remain the same. Here
    embeddings, these remain the same. Here

    we don''t have anything masked but token we don''t have anything masked but token
    we don''t have anything masked but token

    embedding we have a mask token here and embedding we have a mask token here and
    embedding we have a mask token here and

    which tokens to mask are is decided which tokens to mask are is decided which
    tokens to mask are is decided

    probabilistically but how many tokens to probabilistically but how many tokens
    to probabilistically but how many tokens to

    mask is decided by that noise schedule mask is decided by that noise schedule
    mask is decided by that noise schedule

    which we have. So this this noise should which we have. So this this noise should
    which we have. So this this noise should

    so let''s say we get the token embedding so let''s say we get the token embedding
    so let''s say we get the token embedding

    we get the position embedding these we get the position embedding these we get
    the position embedding these

    tokens are now masked we add the token embedding plus position'
  concept_slugs:
  - diffusion-language-model
  - masked-diffusion
- idx: 9
  start_sec: 486.56
  end_sec: 531.2
  text: 'we add the token embedding plus position

    embedding the one major difference in embedding the one major difference in embedding
    the one major difference in

    diffusion language models is that along diffusion language models is that along
    diffusion language models is that along

    with adding token embedding plus with adding token embedding plus with adding
    token embedding plus

    position embedding we also add time position embedding we also add time position
    embedding we also add time

    embeddings right so we have time steps embeddings right so we have time steps
    embeddings right so we have time steps

    for the noise schedule if those are from for the noise schedule if those are from
    for the noise schedule if those are from

    1 to 4 we have a 768 embed 768 create 1 to 4 we have a 768 embed 768 create 1
    to 4 we have a 768 embed 768 create

    dimensional vector for each of these dimensional vector for each of these dimensional
    vector for each of these

    time steps. time steps. time steps.

    And remember what I mentioned for And remember what I mentioned for And remember
    what I mentioned for

    diffusion models. In diffusion models, diffusion models. In diffusion models,
    diffusion models. In diffusion models,

    whenever we are doing a forward pass, we whenever we are doing a forward pass,
    we whenever we are doing a forward pass, we

    not only choose a batch, we also choose not only choose a batch, we also choose
    not only choose a batch, we also choose

    the time step as well. the time step as well. the time step as well.

    So if you have chosen let''s say time So if you have chosen let''s say time So
    if you have chosen let''s say time

    step equal to two, the time embedding, step equal to two, the time embedding,
    step equal to two, the time embedding,

    we''ll go to the time embedding matrix we''ll go to the time embedding matrix
    we''ll go to the time embedding matrix

    and we''ll see the vector corresponding and we''ll see the vector corresponding
    and we''ll see the vector corresponding

    to time step equal to two and that same to time step equal to two and that same
    to time step equal to two and that same

    time embedding vector is added to all my time embedding vector is added to all
    my'
  concept_slugs:
  - diffusion-language-model
  - masked-diffusion
- idx: 10
  start_sec: 531.2
  end_sec: 575.519
  text: 'time embedding vector is added to all my

    tokens. So now the input embedding is tokens. So now the input embedding is tokens.
    So now the input embedding is

    not just the token embedding plus not just the token embedding plus not just the
    token embedding plus

    position embedding. My input embedding position embedding. My input embedding
    position embedding. My input embedding

    is token embedding plus position is token embedding plus position is token embedding
    plus position

    embedding plus time embedding. There are embedding plus time embedding. There
    are embedding plus time embedding. There are

    three embedding vectors which are added three embedding vectors which are added
    three embedding vectors which are added

    together. Why do we consider time together. Why do we consider time together.
    Why do we consider time

    embedding here? Because the time at embedding here? Because the time at embedding
    here? Because the time at

    which we are predicting the noise, it''s which we are predicting the noise, it''s
    which we are predicting the noise, it''s

    also important. also important. also important.

    While dnoising, we need to know the time While dnoising, we need to know the time
    While dnoising, we need to know the time

    step at which we are denoising. Right? step at which we are denoising. Right?
    step at which we are denoising. Right?

    If we are way if it''s extremely if it''s If we are way if it''s extremely if
    it''s If we are way if it''s extremely if it''s

    extremely noisy image, it''s further extremely noisy image, it''s further extremely
    noisy image, it''s further

    along in time. If the image is not that along in time. If the image is not that
    along in time. If the image is not that

    noisy, it''s earlier in time. This is one noisy, it''s earlier in time. This is
    one noisy, it''s earlier in time. This is one

    major change. We add the time embedding major change. We add the time embedding
    major change. We add the time embedding

    also along with the token embedding plus also along with the token embedding plus
    also along with the token embedding plus

    the position embedding. That''s the first the position embedding. That''s the
    first the position embedding. That''s the first

    change. So now if you see if you compare change. So now if you see if you compare'
  concept_slugs:
  - diffusion-language-model
  - masked-diffusion
- idx: 11
  start_sec: 575.519
  end_sec: 625.68
  text: 'change. So now if you see if you compare

    these block diagrams these block diagrams these block diagrams

    in the ARM architecture, we only had the in the ARM architecture, we only had
    the in the ARM architecture, we only had the

    token embedding and position embedding. token embedding and position embedding.
    token embedding and position embedding.

    In the uh diffusion model architecture, In the uh diffusion model architecture,
    In the uh diffusion model architecture,

    we have token embedding, we have we have token embedding, we have we have token
    embedding, we have

    position embedding, and we have time position embedding, and we have time position
    embedding, and we have time

    embedding. And all these are added to embedding. And all these are added to embedding.
    And all these are added to

    each other. This resulting input each other. This resulting input each other.
    This resulting input

    embedding is then passed through through embedding is then passed through through
    embedding is then passed through through

    the transformer block. Okay. Now the the transformer block. Okay. Now the the
    transformer block. Okay. Now the

    transformer block remains exactly the transformer block remains exactly the transformer
    block remains exactly the

    same. same. same.

    The transformer block has no change. We The transformer block has no change. We
    The transformer block has no change. We

    have the layer norm, we have the multi have the layer norm, we have the multi
    have the layer norm, we have the multi

    head attention, we have dropout, head attention, we have dropout, head attention,
    we have dropout,

    shortcut, layer norm, feed forward shortcut, layer norm, feed forward shortcut,
    layer norm, feed forward

    network and dropout. So the whole flow network and dropout. So the whole flow
    network and dropout. So the whole flow

    which we have seen layer norm, multi which we have seen layer norm, multi which
    we have seen layer norm, multi

    head attention, dropout, shortcut head attention, dropout, shortcut head attention,
    dropout, shortcut

    connection here. then another layer norm connection here. then another layer norm
    connection here. then another layer norm

    feed forward neural network dropout and feed forward neural network dropout and
    feed forward neural network dropout and

    another shortcut connection. This stays another shortcut connection. This stays
    another shortcut connection. This stays

    exactly the same. The difference is in exactly the same. The difference is in'
  concept_slugs:
  - diffusion-language-model
  - masked-diffusion
- idx: 12
  start_sec: 625.68
  end_sec: 668.959
  text: 'exactly the same. The difference is in

    the attention mechanism. the attention mechanism. the attention mechanism.

    Now think about it right here. We no Now think about it right here. We no Now
    think about it right here. We no

    longer have a next token prediction longer have a next token prediction longer
    have a next token prediction

    task. What we have to do is we just have task. What we have to do is we just have
    task. What we have to do is we just have

    to predict the masks right? We just have to predict the masks right? We just have
    to predict the masks right? We just have

    to predict the masks. So if we are to predict the masks. So if we are to predict
    the masks. So if we are

    looking at this mask, I can look at looking at this mask, I can look at looking
    at this mask, I can look at

    tokens before this mask and I can look tokens before this mask and I can look
    tokens before this mask and I can look

    at tokens after this mask also. I get at tokens after this mask also. I get at
    tokens after this mask also. I get

    information of tokens behind me and I information of tokens behind me and I information
    of tokens behind me and I

    get information of tokens in front of me get information of tokens in front of
    me get information of tokens in front of me

    also. This is very different than ARMs. also. This is very different than ARMs.
    also. This is very different than ARMs.

    In ARM, if I''m looking at this position, In ARM, if I''m looking at this position,
    In ARM, if I''m looking at this position,

    I only have access to tokens which come I only have access to tokens which come
    I only have access to tokens which come

    before this position. But in diffusion before this position. But in diffusion
    before this position. But in diffusion

    models, for one token, I have access to models, for one token, I have access to
    models, for one token, I have access to

    tokens before it and after it. Which tokens before it and after it. Which tokens
    before it and after it. Which

    means that when I''m calculating the means that when I''m calculating the'
  concept_slugs:
  - diffusion-language-model
  - masked-diffusion
- idx: 13
  start_sec: 668.959
  end_sec: 748.959
  text: 'means that when I''m calculating the

    attention so the mask the mask day the mask day

    mask bright right which means that if mask bright right which means that if mask
    bright right which means that if

    I''m calculating the attention score for I''m calculating the attention score
    for I''m calculating the attention score for

    any token I can calculate the attention any token I can calculate the attention
    any token I can calculate the attention

    score for tokens before that token and score for tokens before that token and
    score for tokens before that token and

    also after that token right so if this also after that token right so if this
    also after that token right so if this

    is my attention scores matrix this will is my attention scores matrix this will
    is my attention scores matrix this will

    be a 5x5 matrix 1 2 3 4 5 1 2 3 4 5 1 2 be a 5x5 matrix 1 2 3 4 5 1 2 3 4 5 1
    2 be a 5x5 matrix 1 2 3 4 5 1 2 3 4 5 1 2

    3 4 5 In the case of auto reggressive models I In the case of auto reggressive
    models I

    will not I will not have so these will not I will not have so these will not I
    will not have so these

    attention scores right which I''m marking attention scores right which I''m marking
    attention scores right which I''m marking

    right now these attention scores will right now these attention scores will right
    now these attention scores will

    not be there I will only have these not be there I will only have these not be
    there I will only have these

    attention scores for an auto reggressive attention scores for an auto reggressive
    attention scores for an auto reggressive

    model model

    whereas whereas whereas

    for a diffusion model I can look at a for a diffusion model I can look at a for
    a diffusion model I can look at a

    token from all sides. So if I just rub token from all sides. So if I just rub
    token from all sides. So if I just rub

    this right now this right now this right now

    if I look at I essentially have this entire causal'
  concept_slugs:
  - diffusion-language-model
  - masked-diffusion
- idx: 14
  start_sec: 748.959
  end_sec: 795.2
  text: 'I essentially have this entire causal

    attention matrix which is available to attention matrix which is available to
    attention matrix which is available to

    me. I don''t have to set these values to me. I don''t have to set these values
    to me. I don''t have to set these values to

    zero like in the ARM block. So one major zero like in the ARM block. So one major
    zero like in the ARM block. So one major

    difference takes place in this attention difference takes place in this attention
    difference takes place in this attention

    module. If you look here in the auto module. If you look here in the auto module.
    If you look here in the auto

    reggressive modeling the causal reggressive modeling the causal reggressive modeling
    the causal

    attention exists which means that all attention exists which means that all attention
    exists which means that all

    the attention scores above this diagonal the attention scores above this diagonal
    the attention scores above this diagonal

    are set to zero. Whereas this does not are set to zero. Whereas this does not
    are set to zero. Whereas this does not

    happen in the case of diffusion models. happen in the case of diffusion models.
    happen in the case of diffusion models.

    We don''t have such a causal attention We don''t have such a causal attention
    We don''t have such a causal attention

    mask. We have a biirectional attention mask. We have a biirectional attention
    mask. We have a biirectional attention

    mechanism. So all of the attention mechanism. So all of the attention mechanism.
    So all of the attention

    scores remain valid. scores remain valid. scores remain valid.

    That''s one major difference and I want That''s one major difference and I want
    That''s one major difference and I want

    all of you to keep this in mind. That''s all of you to keep this in mind. That''s
    all of you to keep this in mind. That''s

    why we went into detail in the attention why we went into detail in the attention
    why we went into detail in the attention

    mechanism. That is the second major mechanism. That is the second major mechanism.
    That is the second major

    difference, right? Uh what''s the third difference, right? Uh what''s the third
    difference, right? Uh what''s the third

    major difference? The third major major difference? The third major'
  concept_slugs:
  - diffusion-language-model
  - masked-diffusion
- idx: 15
  start_sec: 795.2
  end_sec: 836.399
  text: 'major difference? The third major

    difference comes in the output token difference comes in the output token difference
    comes in the output token

    prediction, right? Uh let''s say here we prediction, right? Uh let''s say here
    we prediction, right? Uh let''s say here we

    have every effort moves you, right? and have every effort moves you, right? and
    have every effort moves you, right? and

    we have predictions and we have targets we have predictions and we have targets
    we have predictions and we have targets

    and we compute the loss for all of these and we compute the loss for all of these
    and we compute the loss for all of these

    and we add all of these losses together and we add all of these losses together
    and we add all of these losses together

    for diffusion based modeling it''s very for diffusion based modeling it''s very
    for diffusion based modeling it''s very

    different for diffusion based models different for diffusion based models different
    for diffusion based models

    let''s say this is my input sequence I let''s say this is my input sequence I
    let''s say this is my input sequence I

    have to only consider the prediction at have to only consider the prediction at
    have to only consider the prediction at

    this position and I have to consider the this position and I have to consider
    the this position and I have to consider the

    prediction at this position and I have prediction at this position and I have
    prediction at this position and I have

    to compare it with the actual value to compare it with the actual value to compare
    it with the actual value

    right so I just have to find the cross right so I just have to find the cross
    right so I just have to find the cross

    entropy loss for my mask one I have to entropy loss for my mask one I have to
    entropy loss for my mask one I have to

    find the cross entropy loss for my mask find the cross entropy loss for my mask
    find the cross entropy loss for my mask

    two and I have to take the average of two and I have to take the average of two
    and I have to take the average of

    these losses. That''s my loss. these losses. That''s my loss.'
  concept_slugs:
  - diffusion-language-model
  - masked-diffusion
- idx: 16
  start_sec: 836.399
  end_sec: 904.88
  text: 'these losses. That''s my loss.

    I don''t have to find the loss for the I don''t have to find the loss for the
    I don''t have to find the loss for the

    other positions at all. other positions at all. other positions at all.

    Even in the example which we have chosen Even in the example which we have chosen
    Even in the example which we have chosen

    over here um the mask day. So this over here um the mask day. So this over here
    um the mask day. So this

    example right the example right the example right the

    mask day

    mask and bright right. So here I only have to care. So let''s So here I only have
    to care. So let''s

    say I have my prediction here and the say I have my prediction here and the say
    I have my prediction here and the

    prediction here prediction here prediction here

    the true value is next and that comes at the true value is next and that comes
    at the true value is next and that comes at

    ID equal to 3. I just have to take ID equal to 3. I just have to take ID equal
    to 3. I just have to take

    negative log of probability at this negative log of probability at this negative
    log of probability at this

    position position position

    and here the true value is let''s say is and here the true value is let''s say
    is and here the true value is let''s say is

    comes at ID equal to 500. So then I just comes at ID equal to 500. So then I just
    comes at ID equal to 500. So then I just

    have to take negative log of probability have to take negative log of probability
    have to take negative log of probability

    of 500 and the loss of 500 and the loss of 500 and the loss

    and the loss is just then equal to and the loss is just then equal to and the
    loss is just then equal to

    negative of 1 by 2 log of P3 plus log of negative of 1 by 2 log of P3 plus log
    of negative of 1 by 2 log of P3 plus log of

    P500. P500. P500.

    So if this is let''s say 0.1 this So if this is let''s say 0.1 this'
  concept_slugs:
  - diffusion-language-model
  - masked-diffusion
- idx: 17
  start_sec: 904.88
  end_sec: 975.67
  text: 'So if this is let''s say 0.1 this

    probability and this is2 my loss in this probability and this is2 my loss in this
    probability and this is2 my loss in this

    case will be - 1 by2 log of.1 log of.1

    plus log of 2. plus log of 2. plus log of 2.

    So let''s see how much that is. -1 by 2 So let''s see how much that is. -1 by
    2 So let''s see how much that is. -1 by 2

    into log of.1 into log of.1 into log of.1

    plus log of plus log of plus log of

    that''s 84. So the loss which I''ve that''s 84. So the loss which I''ve that''s
    84. So the loss which I''ve

    obtained in this case is obtained in this case is obtained in this case is

    um um um

    so the loss which I''ve obtained in this so the loss which I''ve obtained in this
    so the loss which I''ve obtained in this

    case is 84 case is 84 case is 84

    and then I do back propagation. So the and then I do back propagation. So the
    and then I do back propagation. So the

    way this entire way this entire way this entire

    um um

    noising process happens now I''ve tried noising process happens now I''ve tried
    noising process happens now I''ve tried

    to explain it not the entire noising to explain it not the entire noising to explain
    it not the entire noising

    process but the entire flow we first process but the entire flow we first process
    but the entire flow we first

    decide a time point let''s say time equal decide a time point let''s say time
    equal decide a time point let''s say time equal

    to three right I asked 50% of the input to three right I asked 50% of the input
    to three right I asked 50% of the input

    sequences the masked input then goes sequences the masked input then goes sequences
    the masked input then goes

    through this whole architecture what are through this whole architecture what
    are through this whole architecture what are

    the changes in this architecture the changes in this architecture the changes
    in this architecture

    compared to the auto reggressive model compared to the auto reggressive model
    compared to the auto reggressive model

    we have a time embedding now which was'
  concept_slugs:
  - diffusion-language-model
  - masked-diffusion
- idx: 18
  start_sec: 975.67
  end_sec: 1022.949
  text: 'we have a time embedding now which was we have a time embedding now which
    was

    not there auto reggressive model in not there auto reggressive model in not there
    auto reggressive model in

    multi attention block uh we don''t have multi attention block uh we don''t have
    multi attention block uh we don''t have

    the causal attention now we can take the the causal attention now we can take
    the the causal attention now we can take the

    whole whole attention attention scores whole whole attention attention scores
    whole whole attention attention scores

    matrix because for each token we can matrix because for each token we can matrix
    because for each token we can

    look behind and we can look ahead also look behind and we can look ahead also
    look behind and we can look ahead also

    okay that''s why generally b models are okay that''s why generally b models are
    okay that''s why generally b models are

    good at sentiment analysis right because good at sentiment analysis right because
    good at sentiment analysis right because

    bird is also biirectional in bird models bird is also biirectional in bird models
    bird is also biirectional in bird models

    we look at a token from behind and ahead we look at a token from behind and ahead
    we look at a token from behind and ahead

    so you can look at an entire sentence so you can look at an entire sentence so
    you can look at an entire sentence

    and predict the sentiment of the and predict the sentiment of the and predict
    the sentiment of the

    sentence right It''s kind of similar sentence right It''s kind of similar sentence
    right It''s kind of similar

    here. The only difference from the BERT here. The only difference from the BERT
    here. The only difference from the BERT

    architecture is that in BERT the masking architecture is that in BERT the masking
    architecture is that in BERT the masking

    ratio is fixed. But here the masking ratio is fixed. But here the masking ratio
    is fixed. But here the masking

    ratio is different. Right? The masking ratio is different. Right? The masking
    ratio is different. Right? The masking

    ratio uh in this case actually depends ratio uh in this case actually depends
    ratio uh in this case actually depends

    on u the time step. More the time step,'
  concept_slugs:
  - diffusion-language-model
  - masked-diffusion
- idx: 19
  start_sec: 1022.949
  end_sec: 1063.2
  text: 'on u the time step. More the time step, on u the time step. More the time
    step,

    more is the masking. Less the time step, more is the masking. Less the time step,
    more is the masking. Less the time step,

    less the masking. That''s the difference less the masking. That''s the difference
    less the masking. That''s the difference

    between BERT and uh language diffusion. between BERT and uh language diffusion.
    between BERT and uh language diffusion.

    So we have chosen time equal to three. So we have chosen time equal to three.
    So we have chosen time equal to three.

    50% is masked that input sequence. we 50% is masked that input sequence. we 50%
    is masked that input sequence. we

    choose a batch. So if the batch size is choose a batch. So if the batch size is
    choose a batch. So if the batch size is

    128, we choose a batch of 128 sequences. 128, we choose a batch of 128 sequences.
    128, we choose a batch of 128 sequences.

    We mask 50% of those and we pass it We mask 50% of those and we pass it We mask
    50% of those and we pass it

    through this entire architecture. So through this entire architecture. So through
    this entire architecture. So

    this is let''s say the input sequence, it this is let''s say the input sequence,
    it this is let''s say the input sequence, it

    first goes through the token embedding. first goes through the token embedding.
    first goes through the token embedding.

    So every token is converted into an So every token is converted into an So every
    token is converted into an

    embedding vector. We add the positional embedding vector. We add the positional
    embedding vector. We add the positional

    embedding, we add the time embedding and embedding, we add the time embedding
    and embedding, we add the time embedding and

    uh so token embedding plus position uh so token embedding plus position uh so
    token embedding plus position

    embedding plus time embedding is my embedding plus time embedding is my embedding
    plus time embedding is my

    final input vector that goes through my final input vector that goes through my
    final input vector that goes through my

    transformer block. So I have my layer transformer block. So I have my layer'
  concept_slugs:
  - diffusion-language-model
  - masked-diffusion
- idx: 20
  start_sec: 1063.2
  end_sec: 1111.6
  text: 'transformer block. So I have my layer

    normalization multi head attention I normalization multi head attention I normalization
    multi head attention I

    have my dropout I have my skip have my dropout I have my skip have my dropout
    I have my skip

    connection I have second layer connection I have second layer connection I have
    second layer

    normalization I have my feed forward normalization I have my feed forward normalization
    I have my feed forward

    neural network I have dropout and neural network I have dropout and neural network
    I have dropout and

    another shortcut connection on the another shortcut connection on the another
    shortcut connection on the

    outset which means at the end I have my outset which means at the end I have my
    outset which means at the end I have my

    final normalization I have this logits final normalization I have this logits
    final normalization I have this logits

    matrix and I have the cross entropy loss matrix and I have the cross entropy loss
    matrix and I have the cross entropy loss

    which is only computed for the mask which is only computed for the mask which
    is only computed for the mask

    tokens that''s the second major last tokens that''s the second major last tokens
    that''s the second major last

    major difference between language major difference between language major difference
    between language

    diffusion and auto reggressive model diffusion and auto reggressive model diffusion
    and auto reggressive model

    diffusion here the Cross entropy loss is diffusion here the Cross entropy loss
    is diffusion here the Cross entropy loss is

    only calculated for the mask tokens and only calculated for the mask tokens and
    only calculated for the mask tokens and

    for nothing else. for nothing else. for nothing else.

    So to summarize the entire noising So to summarize the entire noising So to summarize
    the entire noising

    process looks like this. We have the process looks like this. We have the process
    looks like this. We have the

    let''s say we choose the batch size. We let''s say we choose the batch size. We
    let''s say we choose the batch size. We

    choose two things, right? We choose the choose two things, right? We choose the
    choose two things, right? We choose the

    batch size. We choose the time step, batch size. We choose the time step,'
  concept_slugs:
  - diffusion-language-model
  - masked-diffusion
- idx: 21
  start_sec: 1111.6
  end_sec: 1170.559
  text: 'batch size. We choose the time step,

    right? Let''s say batch size is 128. We right? Let''s say batch size is 128. We
    right? Let''s say batch size is 128. We

    assemble an input sequence of assemble an input sequence of assemble an input
    sequence of

    128 tokens uh and we choose a batch size. So we uh and we choose a batch size.
    So we

    randomly mask let''s say 50. We choose a randomly mask let''s say 50. We choose
    a randomly mask let''s say 50. We choose a

    time step. If the time step is half of time step. If the time step is half of
    time step. If the time step is half of

    the total time, we randomly mask 50% of the total time, we randomly mask 50% of
    the total time, we randomly mask 50% of

    these. So these will be replaced with these. So these will be replaced with these.
    So these will be replaced with

    mask. Okay. Now before now these this input Okay. Now before now these this input

    sequence before going through the sequence before going through the sequence before
    going through the

    transformer architecture we add the transformer architecture we add the transformer
    architecture we add the

    token embeddings plus the position token embeddings plus the position token embeddings
    plus the position

    embeddings plus the time embeddings. embeddings plus the time embeddings. embeddings
    plus the time embeddings.

    So this vector which I have shown is So this vector which I have shown is So this
    vector which I have shown is

    token embedding plus position plus time. token embedding plus position plus time.
    token embedding plus position plus time.

    And this this input vectors then go into And this this input vectors then go into
    And this this input vectors then go into

    the transformer architecture. When they the transformer architecture. When they
    the transformer architecture. When they

    come out of the transformer come out of the transformer come out of the transformer

    architecture, we get the categorical architecture, we get the categorical architecture,
    we get the categorical

    cross entropy loss only on the mask cross entropy loss only on the mask cross
    entropy loss only on the mask

    tokens. Based on this loss, we find the tokens. Based on this loss, we find the'
  concept_slugs:
  - diffusion-language-model
  - masked-diffusion
- idx: 22
  start_sec: 1170.559
  end_sec: 1227.52
  text: 'tokens. Based on this loss, we find the

    partial derivative of the loss with partial derivative of the loss with partial
    derivative of the loss with

    respect to all the parameters. And respect to all the parameters. And respect
    to all the parameters. And

    remember we have seen what what do I remember we have seen what what do I remember
    we have seen what what do I

    mean by all the parameters? Uh we have mean by all the parameters? Uh we have
    mean by all the parameters? Uh we have

    seen everything marked P over here are seen everything marked P over here are
    seen everything marked P over here are

    all the parameters. We have seen that in all the parameters. We have seen that
    in all the parameters. We have seen that in

    one of the previous lectures. This one of the previous lectures. This one of the
    previous lectures. This

    remains the same. All trainable remains the same. All trainable remains the same.
    All trainable

    parameters remain the same in ARM and in parameters remain the same in ARM and
    in parameters remain the same in ARM and in

    the language diffusion. the language diffusion. the language diffusion.

    Right? So we get the partial derivative Right? So we get the partial derivative
    Right? So we get the partial derivative

    of loss with respect to all the of loss with respect to all the of loss with respect
    to all the

    parameters. Then we update parameters. Then we update parameters. Then we update

    then we update the parameters then we update the parameters then we update the
    parameters

    according to ADAM optimizer or any other according to ADAM optimizer or any other
    according to ADAM optimizer or any other

    optimizer which you want. And then this optimizer which you want. And then this
    optimizer which you want. And then this

    entire thing goes into a loop. entire thing goes into a loop. entire thing goes
    into a loop.

    This is how I pre-train. This is how I pre-train. This is how I pre-train.

    This is how I pre-train a language This is how I pre-train a language This is
    how I pre-train a language

    diffusion model. What is implicitly happening in this What is implicitly happening
    in this

    case is the better we pre-train a case is the better we pre-train a'
  concept_slugs:
  - diffusion-language-model
  - masked-diffusion
- idx: 23
  start_sec: 1227.52
  end_sec: 1278.31
  text: 'case is the better we pre-train a

    language diffusion model the better we language diffusion model the better we
    language diffusion model the better we

    are able to discover what noise is added are able to discover what noise is added
    are able to discover what noise is added

    and during the generation process or and during the generation process or and
    during the generation process or

    during the dnoising the better we''ll be during the dnoising the better we''ll
    be during the dnoising the better we''ll be

    able to find the underlying probability able to find the underlying probability
    able to find the underlying probability

    distribution right so if you look at distribution right so if you look at distribution
    right so if you look at

    this analogy over here. Yeah. So what we are doing right now is Yeah. So what
    we are doing right now is

    the noising process, right? And we are the noising process, right? And we are
    the noising process, right? And we are

    training the model to recover the noise. training the model to recover the noise.
    training the model to recover the noise.

    And the better we train this model to And the better we train this model to And
    the better we train this model to

    recover the noise, the better we''ll be recover the noise, the better we''ll be
    recover the noise, the better we''ll be

    at denoising. at denoising. at denoising.

    So the better we so in dnoising what we So the better we so in dnoising what we
    So the better we so in dnoising what we

    are going to do is that we are going to are going to do is that we are going to
    are going to do is that we are going to

    start with all masks and then we we are start with all masks and then we we are
    start with all masks and then we we are

    slowly going to uncover the masks and slowly going to uncover the masks and slowly
    going to uncover the masks and

    recover the actual tokens in that recover the actual tokens in that recover the
    actual tokens in that

    position. position. position.

    That''s why we get gifs such as this. That''s why we get gifs such as this. That''s
    why we get gifs such as this.

    Start with all masks and then we uncover'
  concept_slugs:
  - diffusion-language-model
  - masked-diffusion
- idx: 24
  start_sec: 1278.31
  end_sec: 1322.24
  text: 'Start with all masks and then we uncover Start with all masks and then we
    uncover

    tokens correct tokens at that position. tokens correct tokens at that position.
    tokens correct tokens at that position.

    But dnoising will only work if the loss But dnoising will only work if the loss
    But dnoising will only work if the loss

    function during the pre-training or function during the pre-training or function
    during the pre-training or

    understanding the noise is good. Which understanding the noise is good. Which
    understanding the noise is good. Which

    means the loss function becomes lower means the loss function becomes lower means
    the loss function becomes lower

    and lower and lower. and lower and lower. and lower and lower.

    In this large language diffusion models In this large language diffusion models
    In this large language diffusion models

    paper, they have mentioned a theoretical paper, they have mentioned a theoretical
    paper, they have mentioned a theoretical

    result here which I just want to result here which I just want to result here
    which I just want to

    mention. So this is the loss function mention. So this is the loss function mention.
    So this is the loss function

    during pre-training. All which I have during pre-training. All which I have during
    pre-training. All which I have

    explained right now. Everything which I explained right now. Everything which
    I explained right now. Everything which I

    have explained on the screen this this have explained on the screen this this
    have explained on the screen this this

    loss function which I have explained on loss function which I have explained on
    loss function which I have explained on

    the screen until now is explained in one the screen until now is explained in
    one the screen until now is explained in one

    simple formula over here. That''s why simple formula over here. That''s why simple
    formula over here. That''s why

    it''s very difficult to understand it''s very difficult to understand it''s very
    difficult to understand

    research papers until you have a firm research papers until you have a firm research
    papers until you have a firm

    background of the foundations. So this background of the foundations. So this
    background of the foundations. So this

    is the loss function. What these people is the loss function. What these people
    is the loss function. What these people

    predict is that predict is that'
  concept_slugs:
  - diffusion-language-model
  - masked-diffusion
- idx: 25
  start_sec: 1322.24
  end_sec: 1368.39
  text: 'predict is that

    the probability of actually recovering the probability of actually recovering
    the probability of actually recovering

    the true true distribution or the the true true distribution or the the true true
    distribution or the

    chances of recovering the true chances of recovering the true chances of recovering
    the true

    distribution are directly dependent on distribution are directly dependent on
    distribution are directly dependent on

    the loss function. The lower the loss the loss function. The lower the loss the
    loss function. The lower the loss

    function, the better we can recover the function, the better we can recover the
    function, the better we can recover the

    true distribution during dinoising. This true distribution during dinoising. This
    true distribution during dinoising. This

    is what is meant by this second formula. is what is meant by this second formula.
    is what is meant by this second formula.

    So dnoising is very directly linked with So dnoising is very directly linked with
    So dnoising is very directly linked with

    this loss function over here. So there this loss function over here. So there
    this loss function over here. So there

    is a link between the noising process is a link between the noising process is
    a link between the noising process

    and the dinoising. In the noising and the dinoising. In the noising and the dinoising.
    In the noising

    process, we are adding masks and we''re process, we are adding masks and we''re
    process, we are adding masks and we''re

    recovering the true value at those recovering the true value at those recovering
    the true value at those

    masks. The better we do this, the better masks. The better we do this, the better
    masks. The better we do this, the better

    will be the dnoising also. I''m not going will be the dnoising also. I''m not
    going will be the dnoising also. I''m not going

    into the mathematical details of this into the mathematical details of this into
    the mathematical details of this

    but they have mentioned that but they have mentioned that but they have mentioned
    that

    um this has been proved the loss um this has been proved the loss um this has
    been proved the loss

    function in equation three has been function in equation three has been function
    in equation three has been

    proved to be an upper bound on the'
  concept_slugs:
  - diffusion-language-model
  - masked-diffusion
- idx: 26
  start_sec: 1368.39
  end_sec: 1414.64
  text: 'proved to be an upper bound on the proved to be an upper bound on the

    negative log likelihood making it a negative log likelihood making it a negative
    log likelihood making it a

    principled objective for generative principled objective for generative principled
    objective for generative

    modeling. So what they are saying is modeling. So what they are saying is modeling.
    So what they are saying is

    that the lower the loss function is the that the lower the loss function is the
    that the lower the loss function is the

    better we''ll be at this uh true distri better we''ll be at this uh true distri
    better we''ll be at this uh true distri

    better better we''ll be at approximating better better we''ll be at approximating
    better better we''ll be at approximating

    this true distribution. this true distribution. this true distribution.

    So if the green is the true distribution So if the green is the true distribution
    So if the green is the true distribution

    and the orange is the predicted, the and the orange is the predicted, the and
    the orange is the predicted, the

    lower the loss function in pre-training, lower the loss function in pre-training,
    lower the loss function in pre-training,

    the closer these two will lie. the closer these two will lie. the closer these
    two will lie.

    So the dotted red line will lie much So the dotted red line will lie much So the
    dotted red line will lie much

    closer to the orange. If the loss closer to the orange. If the loss closer to
    the orange. If the loss

    function during pre-training is lower, function during pre-training is lower,
    function during pre-training is lower,

    what is the loss function? It''s exactly what is the loss function? It''s exactly
    what is the loss function? It''s exactly

    what we saw saw over here. what we saw saw over here. what we saw saw over here.

    The loss function essentially quantifies The loss function essentially quantifies
    The loss function essentially quantifies

    what is there at the masked masked what is there at the masked masked what is
    there at the masked masked

    positions versus what should be there at positions versus what should be there
    at positions versus what should be there at

    the masked positions. Okay. the masked positions. Okay.'
  concept_slugs:
  - diffusion-language-model
  - masked-diffusion
- idx: 27
  start_sec: 1414.64
  end_sec: 1462.63
  text: 'the masked positions. Okay.

    So, until now we have seen the first two So, until now we have seen the first
    two So, until now we have seen the first two

    steps of diffusion based language steps of diffusion based language steps of diffusion
    based language

    models. First is what is the noising models. First is what is the noising models.
    First is what is the noising

    process and second is how do we predict process and second is how do we predict
    process and second is how do we predict

    the noise? We predict the noise through the noise? We predict the noise through
    the noise? We predict the noise through

    the language model architecture itself the language model architecture itself
    the language model architecture itself

    which I''ve depicted which I''ve depicted which I''ve depicted

    using this diagram. using this diagram. using this diagram.

    So, anytime you are confused, you can So, anytime you are confused, you can So,
    anytime you are confused, you can

    take a look at take a look at take a look at

    yeah this diagram. This is the diagram yeah this diagram. This is the diagram
    yeah this diagram. This is the diagram

    which is essentially used for predicting which is essentially used for predicting
    which is essentially used for predicting

    the noise in the case of diffusion the noise in the case of diffusion the noise
    in the case of diffusion

    models. And I hope all of you have seen models. And I hope all of you have seen
    models. And I hope all of you have seen

    the differences between the diffusion the differences between the diffusion the
    differences between the diffusion

    architecture and the uh ARM or the reg architecture and the uh ARM or the reg
    architecture and the uh ARM or the reg

    auto reggressive architecture. Time auto reggressive architecture. Time auto reggressive
    architecture. Time

    embedding is the first difference. Then embedding is the first difference. Then
    embedding is the first difference. Then

    in multi attention the causality is the in multi attention the causality is the
    in multi attention the causality is the

    second difference. Then the cross second difference. Then the cross second difference.
    Then the cross

    entropy only for the mask tokens that is entropy only for the mask tokens that
    is entropy only for the mask tokens that is

    the third difference. Noisy input here'
  concept_slugs:
  - diffusion-language-model
  - masked-diffusion
- idx: 28
  start_sec: 1462.63
  end_sec: 1509.12
  text: 'the third difference. Noisy input here the third difference. Noisy input
    here

    that''s the four difference. There are that''s the four difference. There are
    that''s the four difference. There are

    four major differences. Everything else four major differences. Everything else
    four major differences. Everything else

    essentially remains the same. That''s why essentially remains the same. That''s
    why essentially remains the same. That''s why

    I mentioned earlier that understanding I mentioned earlier that understanding
    I mentioned earlier that understanding

    the auto reggressive model architecture the auto reggressive model architecture
    the auto reggressive model architecture

    is so crucial for understanding the is so crucial for understanding the is so
    crucial for understanding the

    language diffusion model architecture. language diffusion model architecture.
    language diffusion model architecture.

    Okay. Now when I''m going to share this Okay. Now when I''m going to share this
    Okay. Now when I''m going to share this

    resources with you, there is also a resources with you, there is also a resources
    with you, there is also a

    website in which I have explained all of website in which I have explained all
    of website in which I have explained all of

    these calculations from scratch. So if these calculations from scratch. So if
    these calculations from scratch. So if

    you scroll down below, I have explained you scroll down below, I have explained
    you scroll down below, I have explained

    there is a section called vector flow. there is a section called vector flow.
    there is a section called vector flow.

    So what we do over here is that we take So what we do over here is that we take
    So what we do over here is that we take

    a toy model configuration where we a toy model configuration where we a toy model
    configuration where we

    assume vocabulary size is equal to six assume vocabulary size is equal to six
    assume vocabulary size is equal to six

    sequence length is equal to 5. Uh we sequence length is equal to 5. Uh we sequence
    length is equal to 5. Uh we

    this is a we construct a token embedding this is a we construct a token embedding
    this is a we construct a token embedding

    matrix. We construct a position matrix. We construct a position matrix. We construct
    a position

    embedding matrix and we construct a time embedding matrix and we construct a time'
  concept_slugs:
  - diffusion-language-model
  - masked-diffusion
- idx: 29
  start_sec: 1509.12
  end_sec: 1554.23
  text: 'embedding matrix and we construct a time

    embedding matrix also. And I show you embedding matrix also. And I show you embedding
    matrix also. And I show you

    how everything is done. So at each how everything is done. So at each how everything
    is done. So at each

    position we add the token embedding, position we add the token embedding, position
    we add the token embedding,

    position embedding and the time position embedding and the time position embedding
    and the time

    embedding. Then we do layer embedding. Then we do layer embedding. Then we do
    layer

    normalization vector wise. So if you normalization vector wise. So if you normalization
    vector wise. So if you

    want to go into the mathematical details want to go into the mathematical details
    want to go into the mathematical details

    of how the dimensions are retained, I''ll of how the dimensions are retained,
    I''ll of how the dimensions are retained, I''ll

    share this link with you where even I''ve share this link with you where even
    I''ve share this link with you where even I''ve

    shown everything from the attention shown everything from the attention shown
    everything from the attention

    mechanism to the shortcut connections mechanism to the shortcut connections mechanism
    to the shortcut connections

    which are also called residuals to the which are also called residuals to the
    which are also called residuals to the

    second layer normalization feed forward second layer normalization feed forward
    second layer normalization feed forward

    neural network final layer normalization neural network final layer normalization
    neural network final layer normalization

    final logits matrix and the final cross final logits matrix and the final cross
    final logits matrix and the final cross

    entropy loss. I have already shown this entropy loss. I have already shown this
    entropy loss. I have already shown this

    to you on the whiteboard but just for to you on the whiteboard but just for to
    you on the whiteboard but just for

    the sake of simplicity I''ve added this the sake of simplicity I''ve added this
    the sake of simplicity I''ve added this

    hole over here. So the entire forward hole over here. So the entire forward hole
    over here. So the entire forward

    pass pipeline for diffusion language pass pipeline for diffusion language pass
    pipeline for diffusion language

    model can be summarized here. We have'
  concept_slugs:
  - diffusion-language-model
  - masked-diffusion
- idx: 30
  start_sec: 1554.23
  end_sec: 1594.88
  text: 'model can be summarized here. We have model can be summarized here. We have

    token ids convert them into token token ids convert them into token token ids
    convert them into token

    embedding vectors add position embedding embedding vectors add position embedding
    embedding vectors add position embedding

    vectors add the time embedding vectors vectors add the time embedding vectors
    vectors add the time embedding vectors

    since you have to decide a time step at since you have to decide a time step at
    since you have to decide a time step at

    the start of the forward pass. Then we the start of the forward pass. Then we
    the start of the forward pass. Then we

    go into the transformer architecture. We go into the transformer architecture.
    We go into the transformer architecture. We

    pass through the first layer norm, pass through the first layer norm, pass through
    the first layer norm,

    attention mechanism, shortcut attention mechanism, shortcut attention mechanism,
    shortcut

    connection, second layer norm, feed connection, second layer norm, feed connection,
    second layer norm, feed

    forward neural network, another shortcut forward neural network, another shortcut
    forward neural network, another shortcut

    connection. Final then we come to the connection. Final then we come to the connection.
    Final then we come to the

    output header. We have the final layer output header. We have the final layer
    output header. We have the final layer

    normalization. We have the logits matrix normalization. We have the logits matrix
    normalization. We have the logits matrix

    and we have the cross entropy loss on and we have the cross entropy loss on and
    we have the cross entropy loss on

    the mask positions. the mask positions. the mask positions.

    All right, cool. And now we are ready to All right, cool. And now we are ready
    to All right, cool. And now we are ready to

    move to the final step which is move to the final step which is move to the final
    step which is

    essentially the dnoising process. So essentially the dnoising process. So essentially
    the dnoising process. So

    let''s get to that right now.'
  concept_slugs:
  - diffusion-language-model
  - masked-diffusion
---
# Lecture 13: Diffusion LLM Training Pipeline

See the structured chunks above.
