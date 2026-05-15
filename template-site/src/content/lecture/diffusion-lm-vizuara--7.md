---
course_slug: diffusion-lm-vizuara
idx: 7
title: 'Lecture 6: Auto Regressive Models (ARMs) Introduction'
video_url: https://www.youtube.com/watch?v=HLet8XCXoKY
duration_sec: null
chunks:
- idx: 0
  start_sec: 3.429
  end_sec: 97.759
  text: 'To understand the concept of auto To understand the concept of auto

    reggressive models, reggressive models, reggressive models,

    let me go to the whiteboard and uh let me go to the whiteboard and uh let me go
    to the whiteboard and uh

    actually try to write down a couple of actually try to write down a couple of
    actually try to write down a couple of

    things. things. things.

    Yeah. Yeah. Yeah.

    So, So, So,

    auto reggressive models, right? auto reggressive models, right? auto reggressive
    models, right?

    They are also called as ARMs now They are also called as ARMs now They are also
    called as ARMs now

    but they''re just a but they''re just a but they''re just a

    a fancy way to understand a very um a fancy way to understand a very um a fancy
    way to understand a very um

    simple concept. Yeah. So the way language models work is Yeah. So the way language
    models work is

    as follows. they are trained for as follows. they are trained for as follows.
    they are trained for

    something which is called as a next something which is called as a next something
    which is called as a next

    token prediction task. token prediction task. token prediction task.

    So it''s called as next So it''s called as next So it''s called as next

    next next next

    oops next token next token

    prediction task. Right? What it means is prediction task. Right? What it means
    is prediction task. Right? What it means is

    that when a language model is trained, that when a language model is trained,
    that when a language model is trained,

    they are always trained to predict one they are always trained to predict one
    they are always trained to predict one

    token at a time. So during inference token at a time. So during inference token
    at a time. So during inference

    time also if you ask the question like time also if you ask the question like
    time also if you ask the question like

    once upon a time let''s say let''s say

    if I ask or if I give a prompt that once if I ask or if I give a prompt that once
    if I ask or if I give a prompt that once

    upon a time and I want the language upon a time and I want the language'
  concept_slugs:
  - autoregressive-vs-diffusion
- idx: 1
  start_sec: 97.759
  end_sec: 143.76
  text: 'upon a time and I want the language

    model to complete this prompt. model to complete this prompt. model to complete
    this prompt.

    What it will do is that it will not What it will do is that it will not What it
    will do is that it will not

    generate many tokens at once from all generate many tokens at once from all generate
    many tokens at once from all

    directions. It will generate one token directions. It will generate one token
    directions. It will generate one token

    after this. It will generate one token after this. It will generate one token
    after this. It will generate one token

    after this. It will generate the next after this. It will generate the next after
    this. It will generate the next

    token. It will generate the next token. token. It will generate the next token.
    token. It will generate the next token.

    Right? So it''s one token at a time. Right? So it''s one token at a time. Right?
    So it''s one token at a time.

    And uh this is the main concept behind And uh this is the main concept behind
    And uh this is the main concept behind

    what is called as an auto reggressive what is called as an auto reggressive what
    is called as an auto reggressive

    model. And also during the next token model. And also during the next token model.
    And also during the next token

    prediction task also what happens is prediction task also what happens is prediction
    task also what happens is

    that you first have let''s say one word that you first have let''s say one word
    that you first have let''s say one word

    or one token or one token or one token

    um let''s say this is predicted then this um let''s say this is predicted then
    this um let''s say this is predicted then this

    is again appended to the input sequence is again appended to the input sequence
    is again appended to the input sequence

    then the next token is predicted then then the next token is predicted then then
    the next token is predicted then

    these two are appended to the input these two are appended to the input these
    two are appended to the input

    sequence then the next token is sequence then the next token is'
  concept_slugs:
  - autoregressive-vs-diffusion
- idx: 2
  start_sec: 143.76
  end_sec: 186.8
  text: 'sequence then the next token is

    predicted this is during the training predicted this is during the training predicted
    this is during the training

    during inference also one new token is during inference also one new token is
    during inference also one new token is

    predicted at a time but during training predicted at a time but during training
    predicted at a time but during training

    also when we are training for the next also when we are training for the next
    also when we are training for the next

    token prediction After a new token is token prediction After a new token is token
    prediction After a new token is

    predicted, it is appended to the earlier predicted, it is appended to the earlier
    predicted, it is appended to the earlier

    sequence, then a next token is sequence, then a next token is sequence, then a
    next token is

    predicted. We''ll learn about this whole predicted. We''ll learn about this whole
    predicted. We''ll learn about this whole

    process in a lot of detail when we process in a lot of detail when we process
    in a lot of detail when we

    actually look at the architecture behind actually look at the architecture behind
    actually look at the architecture behind

    how a language model is built. But for how a language model is built. But for
    how a language model is built. But for

    now, just understand that when you look now, just understand that when you look
    now, just understand that when you look

    at sentences or when you look at text at sentences or when you look at text at
    sentences or when you look at text

    being generated here, so let me again being generated here, so let me again being
    generated here, so let me again

    uh ask this. When you look at text being uh ask this. When you look at text being
    uh ask this. When you look at text being

    generated here, it''s through an auto generated here, it''s through an auto generated
    here, it''s through an auto

    reggressive model which predicts one reggressive model which predicts one reggressive
    model which predicts one

    token at a time. So although you will token at a time. So although you will token
    at a time. So although you will

    see multiple tokens here, it''s one token see multiple tokens here, it''s one
    token'
  concept_slugs:
  - autoregressive-vs-diffusion
- idx: 3
  start_sec: 186.8
  end_sec: 238.72
  text: 'see multiple tokens here, it''s one token

    being generated at a time and the next being generated at a time and the next
    being generated at a time and the next

    token which is generated depends on the token which is generated depends on the
    token which is generated depends on the

    previous token. So see this, it''s one previous token. So see this, it''s one
    previous token. So see this, it''s one

    token at a time and the next token token at a time and the next token token at
    a time and the next token

    generates on the pre depends on the generates on the pre depends on the generates
    on the pre depends on the

    previous token. So mathematically this previous token. So mathematically this
    previous token. So mathematically this

    is expressed like this which just means is expressed like this which just means
    is expressed like this which just means

    that the future token depends on the that the future token depends on the that
    the future token depends on the

    previous tokens. That''s it. What these previous tokens. That''s it. What these
    previous tokens. That''s it. What these

    authors essentially mentioned is that there are two things right. First is there
    are two things right. First is

    what we discussed about generative AI what we discussed about generative AI what
    we discussed about generative AI

    through a probabilistic lens finding the through a probabilistic lens finding
    the through a probabilistic lens finding the

    probab probability distribution and probab probability distribution and probab
    probability distribution and

    second is the auto reggressive method. second is the auto reggressive method.
    second is the auto reggressive method.

    What they mentioned is that the auto What they mentioned is that the auto What
    they mentioned is that the auto

    reggressive method does not make reggressive method does not make reggressive
    method does not make

    language models who they are. It''s just language models who they are. It''s just
    language models who they are. It''s just

    an approach which we have chosen. Why is an approach which we have chosen. Why
    is an approach which we have chosen. Why is

    it the default approach? It it''s just it the default approach? It it''s just
    it the default approach? It it''s just

    one thing which works. But why can''t one thing which works. But why can''t'
  concept_slugs:
  - autoregressive-vs-diffusion
- idx: 4
  start_sec: 238.72
  end_sec: 286.56
  text: 'one thing which works. But why can''t

    diffusion be the default option? This is diffusion be the default option? This
    is diffusion be the default option? This is

    what Andre Karpati also mentions here, what Andre Karpati also mentions here,
    what Andre Karpati also mentions here,

    right? Only text use auto reggression. right? Only text use auto reggression.
    right? Only text use auto reggression.

    Why why only text should use this auto Why why only text should use this auto
    Why why only text should use this auto

    regression? Why can''t we use diffusion regression? Why can''t we use diffusion
    regression? Why can''t we use diffusion

    models with text generation? models with text generation? models with text generation?

    Uh that is the main thing which they Uh that is the main thing which they Uh that
    is the main thing which they

    which these authors asked. Also one more which these authors asked. Also one more
    which these authors asked. Also one more

    u one more fallacy of auto reggressive u one more fallacy of auto reggressive
    u one more fallacy of auto reggressive

    models which the authors mentioned is models which the authors mentioned is models
    which the authors mentioned is

    that that that

    um auto reggressive models actually have um auto reggressive models actually have
    um auto reggressive models actually have

    drawbacks. First is that they have slow drawbacks. First is that they have slow
    drawbacks. First is that they have slow

    inference. Why do they have slow inference. Why do they have slow inference. Why
    do they have slow

    inference? Because they are predicting inference? Because they are predicting
    inference? Because they are predicting

    one token at a time not a stream of one token at a time not a stream of one token
    at a time not a stream of

    tokens at once like how diffusion models tokens at once like how diffusion models
    tokens at once like how diffusion models

    can do. If you look at the left hand can do. If you look at the left hand can
    do. If you look at the left hand

    side that''s auto reggressive. It side that''s auto reggressive. It side that''s
    auto reggressive. It

    predicts one token at a time. So if you predicts one token at a time. So if you'
  concept_slugs:
  - autoregressive-vs-diffusion
- idx: 5
  start_sec: 286.56
  end_sec: 334.0
  text: 'predicts one token at a time. So if you

    see to generate the same amount of text see to generate the same amount of text
    see to generate the same amount of text

    the right hand side which is diffusion the right hand side which is diffusion
    the right hand side which is diffusion

    model takes 14 iterations while an auto model takes 14 iterations while an auto
    model takes 14 iterations while an auto

    reggressive model takes 75 iterations reggressive model takes 75 iterations reggressive
    model takes 75 iterations

    which is way higher. So diffusion is far which is way higher. So diffusion is
    far which is way higher. So diffusion is far

    faster for inference. faster for inference. faster for inference.

    That''s one drawback they mentioned of That''s one drawback they mentioned of
    That''s one drawback they mentioned of

    auto reggressive models. The second auto reggressive models. The second auto reggressive
    models. The second

    drawback which they mentioned is they drawback which they mentioned is they drawback
    which they mentioned is they

    cannot handle reverse reasoning reversal cannot handle reverse reasoning reversal
    cannot handle reverse reasoning reversal

    reasoning tasks. What it means is that reasoning tasks. What it means is that
    reasoning tasks. What it means is that

    if my prompt is let''s say who is Daphne if my prompt is let''s say who is Daphne
    if my prompt is let''s say who is Daphne

    Sterling the model output is Dafany Sterling the model output is Dafany Sterling
    the model output is Dafany

    Sterling is the director of 2008 film Sterling is the director of 2008 film Sterling
    is the director of 2008 film

    the silent orchard but if I ask the the silent orchard but if I ask the the silent
    orchard but if I ask the

    model who directed the film the silent model who directed the film the silent
    model who directed the film the silent

    orchard the model may hallucinate this orchard the model may hallucinate this
    orchard the model may hallucinate this

    reverse reasoning right the model can go reverse reasoning right the model can
    go reverse reasoning right the model can go

    from Daphne Sterling to the silent torch from Daphne Sterling to the silent torch
    from Daphne Sterling to the silent torch

    it''s fine because it''s one new token it''s fine because it''s one new token'
  concept_slugs:
  - autoregressive-vs-diffusion
- idx: 6
  start_sec: 334.0
  end_sec: 381.6
  text: 'it''s fine because it''s one new token

    generated at a time but this reverse generated at a time but this reverse generated
    at a time but this reverse

    reasoning becomes very difficult for the reasoning becomes very difficult for
    the reasoning becomes very difficult for the

    model from this film it finds it model from this film it finds it model from this
    film it finds it

    difficult to guess difficult to guess difficult to guess

    who directed this who directed this who directed this

    again. Who is Tom Cruz''s mother? It''s again. Who is Tom Cruz''s mother? It''s
    again. Who is Tom Cruz''s mother? It''s

    Mary Lee. That''s fine. But who is Mary Mary Lee. That''s fine. But who is Mary
    Mary Lee. That''s fine. But who is Mary

    Le''s son? The model finds it difficult Le''s son? The model finds it difficult
    Le''s son? The model finds it difficult

    to answer because it''s reversal to answer because it''s reversal to answer because
    it''s reversal

    reasoning. Why does auto reggressive reasoning. Why does auto reggressive reasoning.
    Why does auto reggressive

    models fail at reversal reasoning or models fail at reversal reasoning or models
    fail at reversal reasoning or

    they cannot handle reversal reasoning they cannot handle reversal reasoning they
    cannot handle reversal reasoning

    because they only predict one new token because they only predict one new token
    because they only predict one new token

    into the future. So it''s going in a into the future. So it''s going in a into
    the future. So it''s going in a

    forward way always. It''s not forward way always. It''s not forward way always.
    It''s not

    biirectional. biirectional. biirectional.

    So these are drawbacks right of auto So these are drawbacks right of auto So these
    are drawbacks right of auto

    reggressive models. reggressive models. reggressive models.

    So these authors proposed that can we So these authors proposed that can we So
    these authors proposed that can we

    try some other approach? Can we try this try some other approach? Can we try this
    try some other approach? Can we try this

    probabilistic approach with diffusion probabilistic approach with diffusion probabilistic
    approach with diffusion

    models? So essentially what they models? So essentially what they models? So essentially
    what they

    mentioned is that if the true language mentioned is that if the true language'
  concept_slugs:
  - autoregressive-vs-diffusion
- idx: 7
  start_sec: 381.6
  end_sec: 433.99
  text: 'mentioned is that if the true language

    distribution lies somewhere here can we distribution lies somewhere here can we
    distribution lies somewhere here can we

    find the model can we make a diffusion find the model can we make a diffusion
    find the model can we make a diffusion

    based language model which tries to based language model which tries to based
    language model which tries to

    approximate this true language approximate this true language approximate this
    true language

    distribution as close as possible. This distribution as close as possible. This
    distribution as close as possible. This

    is very similar to the purple and the is very similar to the purple and the is
    very similar to the purple and the

    red probability distributions which we red probability distributions which we
    red probability distributions which we

    saw for images. If all of you remember saw for images. If all of you remember
    saw for images. If all of you remember

    this, this is the purple and the red this, this is the purple and the red this,
    this is the purple and the red

    images which we saw for image images which we saw for image images which we saw
    for image

    distribution. What if we do something distribution. What if we do something distribution.
    What if we do something

    similar for text? Let''s say this is the similar for text? Let''s say this is
    the similar for text? Let''s say this is the

    underlying true textual underlying true textual underlying true textual

    uh true probability distribution of uh true probability distribution of uh true
    probability distribution of

    meaningful text. Why can''t we train a meaningful text. Why can''t we train a
    meaningful text. Why can''t we train a

    diffusion model on on text so that it diffusion model on on text so that it diffusion
    model on on text so that it

    follows this exactly? follows this exactly? follows this exactly?

    That''s the question which these authors That''s the question which these authors
    That''s the question which these authors

    essentially asked. essentially asked. essentially asked.

    So I have summarized it in the lecture So I have summarized it in the lecture
    So I have summarized it in the lecture

    notes over here. I have mentioned that notes over here. I have mentioned that
    notes over here. I have mentioned that

    what''s the need of auto reggressive'
  concept_slugs:
  - autoregressive-vs-diffusion
- idx: 8
  start_sec: 433.99
  end_sec: 482.71
  text: 'what''s the need of auto reggressive what''s the need of auto reggressive

    models to achieve this to make the models to achieve this to make the models to
    achieve this to make the

    probability distribution close to the probability distribution close to the probability
    distribution close to the

    true distribution. Auto reggressive true distribution. Auto reggressive true distribution.
    Auto reggressive

    models also lead to the same output. models also lead to the same output. models
    also lead to the same output.

    Through them also we get a probability Through them also we get a probability
    Through them also we get a probability

    distribution close to the two true true distribution close to the two true true
    distribution close to the two true true

    distribution. But they are not the only distribution. But they are not the only
    distribution. But they are not the only

    method. Right? Why can''t we have some method. Right? Why can''t we have some
    method. Right? Why can''t we have some

    other methods which also achieve this? other methods which also achieve this?
    other methods which also achieve this?

    in particular why can''t we have in particular why can''t we have in particular
    why can''t we have

    diffusion methods can we try some other diffusion methods can we try some other
    diffusion methods can we try some other

    approach so let''s get into this right approach so let''s get into this right
    approach so let''s get into this right

    now now now

    we are now starting our journey to build we are now starting our journey to build
    we are now starting our journey to build

    a small language diffusion model from a small language diffusion model from a
    small language diffusion model from

    scratch and we are now going to get into scratch and we are now going to get into
    scratch and we are now going to get into

    the nuts and bolts of the architecture the nuts and bolts of the architecture
    the nuts and bolts of the architecture

    of language models we are going to of language models we are going to of language
    models we are going to

    understand the architecture of auto understand the architecture of auto understand
    the architecture of auto

    reggressive models how the architecture reggressive models how the architecture
    reggressive models how the architecture

    ure of diffusion models differs from'
  concept_slugs:
  - autoregressive-vs-diffusion
- idx: 9
  start_sec: 482.71
  end_sec: 496.96
  text: 'ure of diffusion models differs from ure of diffusion models differs from

    auto reggressive models and then we are auto reggressive models and then we are
    auto reggressive models and then we are

    going to going to going to

    code uh an entire diffusion language code uh an entire diffusion language code
    uh an entire diffusion language

    model from scratch. model from scratch. model from scratch.

    So let''s get started.'
  concept_slugs:
  - autoregressive-vs-diffusion
---
# Lecture 6: Auto Regressive Models (ARMs) Introduction

See the structured chunks above.
