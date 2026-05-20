---
course_slug: diffusion-lm-vizuara
idx: 16
title: 'Lecture 15: Diffusion LLM Entire Pipeline Summary'
video_url: https://www.youtube.com/watch?v=gYzDPGdNLEo
duration_sec: null
chunks:
- idx: 0
  start_sec: 2.95
  end_sec: 48.0
  text: 'Before we go to building the small Before we go to building the small

    language diffusion model from scratch language diffusion model from scratch language
    diffusion model from scratch

    and we are going to do that. Uh here is and we are going to do that. Uh here is
    and we are going to do that. Uh here is

    a file on which we are going to build a file on which we are going to build a
    file on which we are going to build

    the entire diffusion language model the entire diffusion language model the entire
    diffusion language model

    fully from scratch. Um following the fully from scratch. Um following the fully
    from scratch. Um following the

    same things which we have seen it seen same things which we have seen it seen
    same things which we have seen it seen

    on the whiteboard. on the whiteboard. on the whiteboard.

    Um I have created this website so that I Um I have created this website so that
    I Um I have created this website so that I

    can provide all of you a quick summary can provide all of you a quick summary
    can provide all of you a quick summary

    of what all we have learned so far. So of what all we have learned so far. So
    of what all we have learned so far. So

    we started out with this goal of we started out with this goal of we started out
    with this goal of

    building a small language diffusion building a small language diffusion building
    a small language diffusion

    model from scratch, right? And the idea model from scratch, right? And the idea
    model from scratch, right? And the idea

    was that well language models what they was that well language models what they
    was that well language models what they

    are essentially doing one way to view it are essentially doing one way to view
    it are essentially doing one way to view it

    probabilistically is that we have this probabilistically is that we have this
    probabilistically is that we have this

    uh underlying space let''s say this uh underlying space let''s say this uh underlying
    space let''s say this

    orange probability distribution where orange probability distribution where orange
    probability distribution where

    the the the

    uh cluster of meaningful sentences lie uh cluster of meaningful sentences lie'
  concept_slugs:
  - diffusion-language-model
- idx: 1
  start_sec: 48.0
  end_sec: 86.64
  text: 'uh cluster of meaningful sentences lie

    what language models are doing is that what language models are doing is that
    what language models are doing is that

    we are trying to find this probability we are trying to find this probability
    we are trying to find this probability

    distribution which is shown by this red distribution which is shown by this red
    distribution which is shown by this red

    dotted line. One way to do that is dotted line. One way to do that is dotted line.
    One way to do that is

    through arms which is auto reggressive through arms which is auto reggressive
    through arms which is auto reggressive

    models. But why do we have to stay models. But why do we have to stay models.
    But why do we have to stay

    limited to ARMs? Let''s try diffusion. If limited to ARMs? Let''s try diffusion.
    If limited to ARMs? Let''s try diffusion. If

    we have to try diffusion, we need to we have to try diffusion, we need to we have
    to try diffusion, we need to

    follow three things. We need to have a follow three things. We need to have a
    follow three things. We need to have a

    noising process. We need to have a model noising process. We need to have a model
    noising process. We need to have a model

    which predicts the noise. And we need a which predicts the noise. And we need
    a which predicts the noise. And we need a

    dinoising process. What''s the noising dinoising process. What''s the noising
    dinoising process. What''s the noising

    noising process which we are going to noising process which we are going to noising
    process which we are going to

    use? Well, the simple idea is that you use? Well, the simple idea is that you
    use? Well, the simple idea is that you

    just take an input sequence, you add just take an input sequence, you add just
    take an input sequence, you add

    masks to it sequentially as you go masks to it sequentially as you go masks to
    it sequentially as you go

    deeper into the noising schedule and you deeper into the noising schedule and
    you deeper into the noising schedule and you

    noise the input sequence. You corrupt noise the input sequence. You corrupt'
  concept_slugs:
  - diffusion-language-model
- idx: 2
  start_sec: 86.64
  end_sec: 134.16
  text: 'noise the input sequence. You corrupt

    the input sequence. You pass this the input sequence. You pass this the input
    sequence. You pass this

    corrupted input sequence uh you pass corrupted input sequence uh you pass corrupted
    input sequence uh you pass

    this corrupted input sequence into this this corrupted input sequence into this
    this corrupted input sequence into this

    uh diffusion language model uh diffusion language model uh diffusion language
    model

    architecture. This whole architecture architecture. This whole architecture architecture.
    This whole architecture

    serves as the model which is a second serves as the model which is a second serves
    as the model which is a second

    building block for predicting the noise. building block for predicting the noise.
    building block for predicting the noise.

    That is this whole diffusion language That is this whole diffusion language That
    is this whole diffusion language

    model architecture which uh uh which I''m model architecture which uh uh which
    I''m model architecture which uh uh which I''m

    showing you right now. So the way we showing you right now. So the way we showing
    you right now. So the way we

    predict the noise in diffusion language predict the noise in diffusion language
    predict the noise in diffusion language

    models is that we pass this noisy input models is that we pass this noisy input
    models is that we pass this noisy input

    through the input block, the processor through the input block, the processor
    through the input block, the processor

    block and the output. we get the loss block and the output. we get the loss block
    and the output. we get the loss

    only for the mask tokens. only for the mask tokens. only for the mask tokens.

    There are some key differences between There are some key differences between
    There are some key differences between

    the um diffusion language model the um diffusion language model the um diffusion
    language model

    architecture and the ARM architecture architecture and the ARM architecture architecture
    and the ARM architecture

    which are highlighted in this two which are highlighted in this two which are
    highlighted in this two

    schematics if you see them side by side. schematics if you see them side by side.
    schematics if you see them side by side.

    One key difference is the time embedding One key difference is the time embedding'
  concept_slugs:
  - diffusion-language-model
- idx: 3
  start_sec: 134.16
  end_sec: 178.15
  text: 'One key difference is the time embedding

    which is not there in ARM but it''s there which is not there in ARM but it''s
    there which is not there in ARM but it''s there

    in diffusion language model. Second is in diffusion language model. Second is
    in diffusion language model. Second is

    that in multi attention we don''t have that in multi attention we don''t have
    that in multi attention we don''t have

    causality causality causality

    um in the attention scores matrix. In um in the attention scores matrix. In um
    in the attention scores matrix. In

    fact, every token can look at the tokens fact, every token can look at the tokens
    fact, every token can look at the tokens

    before it and also after it. Right? So, before it and also after it. Right? So,
    before it and also after it. Right? So,

    we don''t have this. These things are we don''t have this. These things are we
    don''t have this. These things are

    don''t need to be set to zero. Whereas in don''t need to be set to zero. Whereas
    in don''t need to be set to zero. Whereas in

    auto reggressive models or traditional auto reggressive models or traditional
    auto reggressive models or traditional

    language models, everything above the language models, everything above the language
    models, everything above the

    diagonal, all the attention scores above diagonal, all the attention scores above
    diagonal, all the attention scores above

    the diagonal set to zero. That''s not the diagonal set to zero. That''s not the
    diagonal set to zero. That''s not

    needed in the case of diffusion language needed in the case of diffusion language
    needed in the case of diffusion language

    models. models. models.

    Third thing is that we take the cross Third thing is that we take the cross Third
    thing is that we take the cross

    entropy loss only for the mask tokens. entropy loss only for the mask tokens.
    entropy loss only for the mask tokens.

    Whereas in the case of traditional Whereas in the case of traditional Whereas
    in the case of traditional

    language models, we do it for all the language models, we do it for all the language
    models, we do it for all the

    tokens in the input sequence. tokens in the input sequence. tokens in the input
    sequence.

    Fourth thing of course is that we have'
  concept_slugs:
  - diffusion-language-model
- idx: 4
  start_sec: 178.15
  end_sec: 225.75
  text: 'Fourth thing of course is that we have Fourth thing of course is that we
    have

    noisy input with mass tokens. Whereas in noisy input with mass tokens. Whereas
    in noisy input with mass tokens. Whereas in

    the case of traditional language models, the case of traditional language models,
    the case of traditional language models,

    we have noisy input and then we try to we have noisy input and then we try to
    we have noisy input and then we try to

    minimize this loss as much as possible. minimize this loss as much as possible.
    minimize this loss as much as possible.

    The more this loss is minimized, the The more this loss is minimized, the The
    more this loss is minimized, the

    more we are able to predict the noise. more we are able to predict the noise.
    more we are able to predict the noise.

    And theoretically, the more this loss is And theoretically, the more this loss
    is And theoretically, the more this loss is

    minimized, the better we can recover the minimized, the better we can recover
    the minimized, the better we can recover the

    underlying data distribution in the underlying data distribution in the underlying
    data distribution in the

    denoising or the reverse diffusion denoising or the reverse diffusion denoising
    or the reverse diffusion

    process. process. process.

    The third step is the dnoising process The third step is the dnoising process
    The third step is the dnoising process

    or the reverse diffusion process. What or the reverse diffusion process. What
    or the reverse diffusion process. What

    essentially happens in this step is that essentially happens in this step is that
    essentially happens in this step is that

    in the dnoising process in the dnoising process in the dnoising process

    uh we start with masks and then we uh we start with masks and then we uh we start
    with masks and then we

    slowly unmask it one at a time. So one slowly unmask it one at a time. So one
    slowly unmask it one at a time. So one

    mask is unmasked in each iteration and mask is unmasked in each iteration and
    mask is unmasked in each iteration and

    then we go backwards in time. What is then we go backwards in time. What is then
    we go backwards in time. What is

    unmasked? The most confident tokens are'
  concept_slugs:
  - diffusion-language-model
- idx: 5
  start_sec: 225.75
  end_sec: 269.84
  text: 'unmasked? The most confident tokens are unmasked? The most confident tokens
    are

    essentially unmasked. So we unmask the k essentially unmasked. So we unmask the
    k essentially unmasked. So we unmask the k

    tokens with the highest confidence tokens with the highest confidence tokens with
    the highest confidence

    and at the end when we reach the end and at the end when we reach the end and
    at the end when we reach the end

    there should be no masks which is there should be no masks which is there should
    be no masks which is

    remaining. So here''s this animation remaining. So here''s this animation remaining.
    So here''s this animation

    actually shows dinoising in a good actually shows dinoising in a good actually
    shows dinoising in a good

    amount of detail and good amount of amount of detail and good amount of amount
    of detail and good amount of

    depth. This is the generation process. depth. This is the generation process.
    depth. This is the generation process.

    When we do the dnoising, we don''t train When we do the dnoising, we don''t train
    When we do the dnoising, we don''t train

    the parameters. The parameters are the parameters. The parameters are the parameters.
    The parameters are

    trained and updated in the second part trained and updated in the second part
    trained and updated in the second part

    which is the noise prediction process. which is the noise prediction process.
    which is the noise prediction process.

    The cross entropy loss, the parameters The cross entropy loss, the parameters
    The cross entropy loss, the parameters

    are updated, the model is trained. are updated, the model is trained. are updated,
    the model is trained.

    That''s it. The dnoising process we just That''s it. The dnoising process we just
    That''s it. The dnoising process we just

    generate. generate. generate.

    Here is a good gif which shows the Here is a good gif which shows the Here is
    a good gif which shows the

    dnoising. So we start with all masks and dnoising. So we start with all masks
    and dnoising. So we start with all masks and

    slowly unmask one at a time and then we slowly unmask one at a time and then we
    slowly unmask one at a time and then we

    get coherent text towards the end. get coherent text towards the end.'
  concept_slugs:
  - diffusion-language-model
- idx: 6
  start_sec: 269.84
  end_sec: 320.8
  text: 'get coherent text towards the end.

    Right? So this is our whole diffusion Right? So this is our whole diffusion Right?
    So this is our whole diffusion

    pipeline diffusion language model pipeline diffusion language model pipeline diffusion
    language model

    pipeline built entirely from scratch. If pipeline built entirely from scratch.
    If pipeline built entirely from scratch. If

    you want the key takeaways we have you want the key takeaways we have you want
    the key takeaways we have

    in image in image in image

    in images the way we inject noise is in images the way we inject noise is in images
    the way we inject noise is

    through a gshian process right whereas through a gshian process right whereas
    through a gshian process right whereas

    in language models we replace it with in language models we replace it with in
    language models we replace it with

    token masking. So it''s also called as token masking. So it''s also called as
    token masking. So it''s also called as

    discrete diffusion. The papers which I discrete diffusion. The papers which I
    discrete diffusion. The papers which I

    showed you earlier showed this word showed you earlier showed this word showed
    you earlier showed this word

    discrete diffusion. Right? discrete diffusion. Right? discrete diffusion. Right?

    Discrete diffusion modeling. The reason Discrete diffusion modeling. The reason
    Discrete diffusion modeling. The reason

    it''s called discrete diffusion is that it''s called discrete diffusion is that
    it''s called discrete diffusion is that

    we just unmask tokens. So these are we just unmask tokens. So these are we just
    unmask tokens. So these are

    discrete tokens which are masked rather discrete tokens which are masked rather
    discrete tokens which are masked rather

    than applying a gshian distribution to than applying a gshian distribution to
    than applying a gshian distribution to

    the whole image which is done for the whole image which is done for the whole
    image which is done for

    images. images. images.

    The second is biirectional context. The second is biirectional context. The second
    is biirectional context.

    Unlike auto reggressive models a token Unlike auto reggressive models a token
    Unlike auto reggressive models a token

    can live look both behind it and in can live look both behind it and in can live
    look both behind it and in

    front of it. So we don''t have causal front of it. So we don''t have causal'
  concept_slugs:
  - diffusion-language-model
- idx: 7
  start_sec: 320.8
  end_sec: 374.639
  text: 'front of it. So we don''t have causal

    attention. Then we generate by unmasking attention. Then we generate by unmasking
    attention. Then we generate by unmasking

    tokens one at a time. Right? That''s the tokens one at a time. Right? That''s
    the tokens one at a time. Right? That''s the

    So the whole complete pipeline is uh we So the whole complete pipeline is uh we
    So the whole complete pipeline is uh we

    do the we add the noise, we do the do the we add the noise, we do the do the we
    add the noise, we do the

    forward pass where we do the training. forward pass where we do the training.
    forward pass where we do the training.

    All the parameters are fixed. Then we do All the parameters are fixed. Then we
    do All the parameters are fixed. Then we do

    the generation in the dnoising process the generation in the dnoising process
    the generation in the dnoising process

    and then we recover the probability and then we recover the probability and then
    we recover the probability

    distribution which matches distribution which matches distribution which matches

    this underlying distribution which is this underlying distribution which is this
    underlying distribution which is

    the orange one. The orange is the true the orange one. The orange is the true
    the orange one. The orange is the true

    underlying distribution of meaningful underlying distribution of meaningful underlying
    distribution of meaningful

    sentences and the red is the predicted sentences and the red is the predicted
    sentences and the red is the predicted

    probability distribution which matches probability distribution which matches
    probability distribution which matches

    or which tries to match the true or which tries to match the true or which tries
    to match the true

    probability distribution. probability distribution. probability distribution.

    Now what we are going to do is that we Now what we are going to do is that we
    Now what we are going to do is that we

    are going to walk through a code and uh are going to walk through a code and uh
    are going to walk through a code and uh

    I''m I''m going to I''m I''m going to I''m I''m going to

    so if you zoom into here I''m going to so if you zoom into here I''m going to'
  concept_slugs:
  - diffusion-language-model
- idx: 8
  start_sec: 374.639
  end_sec: 394.96
  text: 'so if you zoom into here I''m going to

    share this code file with all of you and share this code file with all of you
    and share this code file with all of you and

    at the end of this code file we are at the end of this code file we are at the
    end of this code file we are

    going to train a diffusion model fully going to train a diffusion model fully
    going to train a diffusion model fully

    from scratch and you''ll also generate a from scratch and you''ll also generate
    a from scratch and you''ll also generate a

    cool GIF like this um which I''m showing cool GIF like this um which I''m showing
    cool GIF like this um which I''m showing

    over here you''ll generate a GIF like over here you''ll generate a GIF like over
    here you''ll generate a GIF like

    this. So let''s start with this uh coding this. So let''s start with this uh coding
    this. So let''s start with this uh coding

    module right now.'
  concept_slugs:
  - diffusion-language-model
---
# Lecture 15: Diffusion LLM Entire Pipeline Summary

See the structured chunks above.
