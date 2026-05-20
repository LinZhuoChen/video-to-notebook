---
course_slug: diffusion-lm-vizuara
idx: 3
title: 'Lecture 2: How I began my Diffusion LLM Journey'
video_url: https://www.youtube.com/watch?v=Hyb7c4PCmwk
duration_sec: null
chunks:
- idx: 0
  start_sec: 2.23
  end_sec: 51.11
  text: 'Let''s get started. Let''s get started.

    Initially, as I mentioned, I''ll be Initially, as I mentioned, I''ll be Initially,
    as I mentioned, I''ll be

    taking you through my journey, right? taking you through my journey, right? taking
    you through my journey, right?

    So, I''ll be taking you through the exact So, I''ll be taking you through the
    exact So, I''ll be taking you through the exact

    timeline which I followed timeline which I followed timeline which I followed

    um and how I made this series on um and how I made this series on um and how I
    made this series on

    diffusion based language models. So diffusion based language models. So diffusion
    based language models. So

    honestly I had seen the this tweet by honestly I had seen the this tweet by honestly
    I had seen the this tweet by

    Andre Karpati first where he mentioned Andre Karpati first where he mentioned
    Andre Karpati first where he mentioned

    that this is interesting as first as a that this is interesting as first as a
    that this is interesting as first as a

    first large diffusion based LLM. Most of first large diffusion based LLM. Most
    of first large diffusion based LLM. Most of

    the LLMs you have been seeing are clones the LLMs you have been seeing are clones
    the LLMs you have been seeing are clones

    as far as the core modeling approach as far as the core modeling approach as far
    as the core modeling approach

    goes. They are all trained auto goes. They are all trained auto goes. They are
    all trained auto

    reggressively that is predicting tokens reggressively that is predicting tokens
    reggressively that is predicting tokens

    from left to right. Diffusion is from left to right. Diffusion is from left to
    right. Diffusion is

    different. It doesn''t go left to right different. It doesn''t go left to right
    different. It doesn''t go left to right

    but it goes all at once. You start with but it goes all at once. You start with
    but it goes all at once. You start with

    noise and gradually den noiseise into a noise and gradually den noiseise into
    a noise and gradually den noiseise into a

    token stream. So when I read this I token stream. So when I read this I token
    stream. So when I read this I

    thought that okay this is something'
  concept_slugs:
  - diffusion-language-model
- idx: 1
  start_sec: 51.11
  end_sec: 93.2
  text: 'thought that okay this is something thought that okay this is something

    cool. I had thought about diffusion only cool. I had thought about diffusion only
    cool. I had thought about diffusion only

    for images and videos but someone seems for images and videos but someone seems
    for images and videos but someone seems

    to have made it for language. to have made it for language. to have made it for
    language.

    But honestly there is one GIF or one But honestly there is one GIF or one But
    honestly there is one GIF or one

    video which when I saw it really blew my video which when I saw it really blew
    my video which when I saw it really blew my

    mind and then I knew I had to learn this mind and then I knew I had to learn this
    mind and then I knew I had to learn this

    material and make a course on it. Here''s material and make a course on it. Here''s
    material and make a course on it. Here''s

    this GIF or here''s the video. If you see this GIF or here''s the video. If you
    see this GIF or here''s the video. If you see

    on the left hand side we have an auto on the left hand side we have an auto on
    the left hand side we have an auto

    reggressive LLM over here and on the reggressive LLM over here and on the reggressive
    LLM over here and on the

    right hand side we have diffusion. So right hand side we have diffusion. So right
    hand side we have diffusion. So

    let''s play it from the start. Yeah, take let''s play it from the start. Yeah,
    take let''s play it from the start. Yeah, take

    a look on the left hand side first how a look on the left hand side first how
    a look on the left hand side first how

    tokens appear sequentially one after the tokens appear sequentially one after
    the tokens appear sequentially one after the

    other. That''s how LLMs have been other. That''s how LLMs have been other. That''s
    how LLMs have been

    operating naturally here. I''ll zoom zoom operating naturally here. I''ll zoom
    zoom operating naturally here. I''ll zoom zoom

    over here. So take a look here first over here. So take a look here first'
  concept_slugs:
  - diffusion-language-model
- idx: 2
  start_sec: 93.2
  end_sec: 138.949
  text: 'over here. So take a look here first

    only on the left hand side. Okay. And only on the left hand side. Okay. And only
    on the left hand side. Okay. And

    now when we restart the video then take now when we restart the video then take
    now when we restart the video then take

    a look at on the right hand side. Right? a look at on the right hand side. Right?
    a look at on the right hand side. Right?

    Take a look at the right hand side and Take a look at the right hand side and
    Take a look at the right hand side and

    how tokens appear here. tokens don''t how tokens appear here. tokens don''t how
    tokens appear here. tokens don''t

    appear one after the other but they just appear one after the other but they just
    appear one after the other but they just

    fill the screen right just how images fill the screen right just how images fill
    the screen right just how images

    are created from noise right that''s are created from noise right that''s are
    created from noise right that''s

    called dn noising in images so here''s called dn noising in images so here''s
    called dn noising in images so here''s

    how the dnoising process actually looks how the dnoising process actually looks
    how the dnoising process actually looks

    like like like

    dnoising images and if I say diffusion dnoising images and if I say diffusion
    dnoising images and if I say diffusion

    right many of you might have seen this right many of you might have seen this
    right many of you might have seen this

    right when we want to make or we want to right when we want to make or we want
    to right when we want to make or we want to

    build images one way to do this is build images one way to do this is build images
    one way to do this is

    diffusion right so you take an image you diffusion right so you take an image
    you diffusion right so you take an image you

    keep keep on adding noise to it and then keep keep on adding noise to it and then
    keep keep on adding noise to it and then

    you learn how much noise is added. So'
  concept_slugs:
  - diffusion-language-model
- idx: 3
  start_sec: 138.949
  end_sec: 187.2
  text: 'you learn how much noise is added. So you learn how much noise is added.
    So

    later you are able to take noise and later you are able to take noise and later
    you are able to take noise and

    then build images from it. People are then build images from it. People are then
    build images from it. People are

    familiar with this and this now comes familiar with this and this now comes familiar
    with this and this now comes

    naturally to people. But to think about naturally to people. But to think about
    naturally to people. But to think about

    diffusion for language it''s awesome diffusion for language it''s awesome diffusion
    for language it''s awesome

    right? We start from let''s say noise and right? We start from let''s say noise
    and right? We start from let''s say noise and

    then suddenly amazing text or meaningful then suddenly amazing text or meaningful
    then suddenly amazing text or meaningful

    text starts appearing on the screen. Now text starts appearing on the screen.
    Now text starts appearing on the screen. Now

    compare the left hand side with the compare the left hand side with the compare
    the left hand side with the

    right hand side. On the left, one token right hand side. On the left, one token
    right hand side. On the left, one token

    appears at a time. On the right, appears at a time. On the right, appears at a
    time. On the right,

    everything fills the screen at once. everything fills the screen at once. everything
    fills the screen at once.

    This GIF or this video should stay in This GIF or this video should stay in This
    GIF or this video should stay in

    your mind because we are going to build your mind because we are going to build
    your mind because we are going to build

    this. This will serve as the baseline this. This will serve as the baseline this.
    This will serve as the baseline

    material for us as the end goal which we material for us as the end goal which
    we material for us as the end goal which we

    want to reach. We want to make a want to reach. We want to make a want to reach.
    We want to make a

    diffusion model which fills the screen diffusion model which fills the screen'
  concept_slugs:
  - diffusion-language-model
- idx: 4
  start_sec: 187.2
  end_sec: 239.75
  text: 'diffusion model which fills the screen

    like this and it''s not one token at a like this and it''s not one token at a
    like this and it''s not one token at a

    time. So when I saw this GIF, I time. So when I saw this GIF, I time. So when
    I saw this GIF, I

    immediately thought that the left hand immediately thought that the left hand
    immediately thought that the left hand

    side where one token is predicted at a side where one token is predicted at a
    side where one token is predicted at a

    time is pretty inefficient, right? Why time is pretty inefficient, right? Why
    time is pretty inefficient, right? Why

    should only one token be predicted at a should only one token be predicted at
    a should only one token be predicted at a

    time? Why can''t we just fill the whole time? Why can''t we just fill the whole
    time? Why can''t we just fill the whole

    screen? screen? screen?

    Uh and tokens come in from left, right, Uh and tokens come in from left, right,
    Uh and tokens come in from left, right,

    anywhere. anywhere. anywhere.

    When I saw this GIF, that''s when I When I saw this GIF, that''s when I When I
    saw this GIF, that''s when I

    started to get an interest in the started to get an interest in the started to
    get an interest in the

    concept of diffusion. basically concept of diffusion. basically concept of diffusion.
    basically

    and u I knew that I had to build this and u I knew that I had to build this and
    u I knew that I had to build this

    from scratch. from scratch. from scratch.

    So to give you a bit of context I So to give you a bit of context I So to give
    you a bit of context I

    already had built this series of already had built this series of already had
    built this series of

    building a large language model from building a large language model from building
    a large language model from

    scratch which was fully auto reggressive scratch which was fully auto reggressive
    scratch which was fully auto reggressive

    which means that it predicts one token which means that it predicts one token
    which means that it predicts one token

    at a time. Um this has now become very'
  concept_slugs:
  - diffusion-language-model
- idx: 5
  start_sec: 239.75
  end_sec: 287.36
  text: 'at a time. Um this has now become very at a time. Um this has now become
    very

    popular on YouTube and it''s one of the popular on YouTube and it''s one of the
    popular on YouTube and it''s one of the

    go-to materials to learn how to build a go-to materials to learn how to build
    a go-to materials to learn how to build a

    language model from scratch. But this is language model from scratch. But this
    is language model from scratch. But this is

    auto reggressive which means it''s like auto reggressive which means it''s like
    auto reggressive which means it''s like

    something on the left hand side which we something on the left hand side which
    we something on the left hand side which we

    saw over here. saw over here. saw over here.

    Uh it''s an auto reggressive model right? Uh it''s an auto reggressive model right?
    Uh it''s an auto reggressive model right?

    So I wanted to build something similar So I wanted to build something similar
    So I wanted to build something similar

    now for diffusion models. now for diffusion models. now for diffusion models.

    And uh last year I had conducted a live And uh last year I had conducted a live
    And uh last year I had conducted a live

    lecture on when I was teaching this lecture on when I was teaching this lecture
    on when I was teaching this

    generative AI fundamentals course. Uh I generative AI fundamentals course. Uh
    I generative AI fundamentals course. Uh I

    had conducted a lecture on diffusion had conducted a lecture on diffusion had
    conducted a lecture on diffusion

    models for image generation. And these models for image generation. And these
    models for image generation. And these

    are the notes which I have prepared for are the notes which I have prepared for
    are the notes which I have prepared for

    the lecture. the lecture. the lecture.

    So before we all start building So before we all start building So before we all
    start building

    diffusion based LLMs, we first need to diffusion based LLMs, we first need to
    diffusion based LLMs, we first need to

    understand what exactly is diffusion. understand what exactly is diffusion. understand
    what exactly is diffusion.

    And uh I''m going to first walk you And uh I''m going to first walk you'
  concept_slugs:
  - diffusion-language-model
- idx: 6
  start_sec: 287.36
  end_sec: 336.8
  text: 'And uh I''m going to first walk you

    through diffusion in an intuitive way through diffusion in an intuitive way through
    diffusion in an intuitive way

    because I I strongly think that all of because I I strongly think that all of
    because I I strongly think that all of

    you really need to understand the you really need to understand the you really
    need to understand the

    uh intuition behind this diffusion uh intuition behind this diffusion uh intuition
    behind this diffusion

    process. Even if you don''t understand process. Even if you don''t understand
    process. Even if you don''t understand

    the mathematics, it''s fine. I don''t want the mathematics, it''s fine. I don''t
    want the mathematics, it''s fine. I don''t want

    you to be intimidated by the mathematics you to be intimidated by the mathematics
    you to be intimidated by the mathematics

    of diffusion but at least for now we of diffusion but at least for now we of diffusion
    but at least for now we

    need to understand the intuition behind need to understand the intuition behind
    need to understand the intuition behind

    diffusion. So basically when I say diffusion. So basically when I say diffusion.
    So basically when I say

    intuition we all need to understand how intuition we all need to understand how
    intuition we all need to understand how

    what is diffusion why it how it works what is diffusion why it how it works what
    is diffusion why it how it works

    for image generation and then we''ll for image generation and then we''ll for
    image generation and then we''ll

    apply the similar concepts to basically apply the similar concepts to basically
    apply the similar concepts to basically

    text right so first I want to remove text right so first I want to remove text
    right so first I want to remove

    this fear of diffusion which I had I this fear of diffusion which I had I this
    fear of diffusion which I had I

    thought whenever I thought of diffusion thought whenever I thought of diffusion
    thought whenever I thought of diffusion

    I thought it''s it involves complex I thought it''s it involves complex I thought
    it''s it involves complex

    probability and mathematical probability and mathematical probability and mathematical

    formulations will which I''ll not so I''ll formulations will which I''ll not so
    I''ll'
  concept_slugs:
  - diffusion-language-model
- idx: 7
  start_sec: 336.8
  end_sec: 383.83
  text: 'formulations will which I''ll not so I''ll

    not take that route when I explain this not take that route when I explain this
    not take that route when I explain this

    to you I''ll explain this to you in an to you I''ll explain this to you in an
    to you I''ll explain this to you in an

    intuitive So that all of you have very intuitive So that all of you have very
    intuitive So that all of you have very

    nice mental model nice mental model nice mental model

    at the end of this uh journey. So when at the end of this uh journey. So when
    at the end of this uh journey. So when

    we conclude and when we actually build we conclude and when we actually build
    we conclude and when we actually build

    a small diffusion model, a small a small diffusion model, a small a small diffusion
    model, a small

    language based diffusion model from language based diffusion model from language
    based diffusion model from

    scratch, it will look something like scratch, it will look something like scratch,
    it will look something like

    this. So you are going to build this. So you are going to build this. So you are
    going to build

    something like this at the end of this something like this at the end of this
    something like this at the end of this

    learning journey or at the end of this learning journey or at the end of this
    learning journey or at the end of this

    course. course. course.

    This has been built purely locally by me This has been built purely locally by
    me This has been built purely locally by me

    u fully from scratch. I have not relied u fully from scratch. I have not relied
    u fully from scratch. I have not relied

    on any library nothing whatsoever. This on any library nothing whatsoever. This
    on any library nothing whatsoever. This

    GIF which is a diffusion based small GIF which is a diffusion based small GIF
    which is a diffusion based small

    language model is is producing coherent language model is is producing coherent
    language model is is producing coherent

    sentences as you can see and it''s built sentences as you can see and it''s built
    sentences as you can see and it''s built

    fully from scratch. You''ll be doing this'
  concept_slugs:
  - diffusion-language-model
- idx: 8
  start_sec: 383.83
  end_sec: 463.12
  text: 'fully from scratch. You''ll be doing this fully from scratch. You''ll be
    doing this

    if you follow you follow along with me if you follow you follow along with me
    if you follow you follow along with me

    throughout this journey. throughout this journey. throughout this journey.

    Right? So let''s actually get uh get Right? So let''s actually get uh get Right?
    So let''s actually get uh get

    started. started. started.

    and uh and uh and uh

    let me connect my lecture notes. All right. So, okay. So, first we need All right.
    So, okay. So, first we need

    to understand to understand to understand

    image generation and uh what exactly are image generation and uh what exactly
    are image generation and uh what exactly are

    diffusion models and then we''ll diffusion models and then we''ll diffusion models
    and then we''ll

    understand how and why diffusion models understand how and why diffusion models
    understand how and why diffusion models

    exactly work. exactly work. exactly work.

    So, let''s take a look at this video So, let''s take a look at this video So,
    let''s take a look at this video

    first. I''m going to play this video first. I''m going to play this video first.
    I''m going to play this video

    right now. You''ll see that a small dye or a small You''ll see that a small dye
    or a small

    chemical is inserted into this liquid chemical is inserted into this liquid chemical
    is inserted into this liquid

    and then we are kind of and then we are kind of and then we are kind of

    uh steering the liquid. We are adding uh steering the liquid. We are adding uh
    steering the liquid. We are adding

    motion. motion. motion.

    So you''ll see that as the liquid is So you''ll see that as the liquid is So you''ll
    see that as the liquid is

    moved the D basically gets spread out moved the D basically gets spread out moved
    the D basically gets spread out

    the D gets diffused. the D gets diffused. the D gets diffused.

    See See See

    this is like adding noise. Let''s say you this is like adding noise. Let''s say
    you this is like adding noise. Let''s say you

    take an image you keep on adding noise take an image you keep on adding noise'
  concept_slugs:
  - diffusion-language-model
- idx: 9
  start_sec: 463.12
  end_sec: 523.599
  text: 'take an image you keep on adding noise

    to it. Right? You keep on adding noise to it. Right? You keep on adding noise
    to it. Right? You keep on adding noise

    to an image until it becomes fully to an image until it becomes fully to an image
    until it becomes fully

    blurred. blurred. blurred.

    That''s the forward noising process or That''s the forward noising process or
    That''s the forward noising process or

    just noising. just noising. just noising.

    And uh in diffusion what we actually do And uh in diffusion what we actually do
    And uh in diffusion what we actually do

    is that is that is that

    we have to approximate the reverse we have to approximate the reverse we have
    to approximate the reverse

    process which means that if we start process which means that if we start process
    which means that if we start

    from pure noise can we reconstruct the from pure noise can we reconstruct the
    from pure noise can we reconstruct the

    original image back from the pure noise. original image back from the pure noise.
    original image back from the pure noise.

    So the whole idea is that if the forward So the whole idea is that if the forward
    So the whole idea is that if the forward

    process is done slowly process is done slowly process is done slowly

    and uh in that forward process and uh in that forward process and uh in that forward
    process

    if we learn how much noise is added at if we learn how much noise is added at
    if we learn how much noise is added at

    each step that same information can be each step that same information can be
    each step that same information can be

    used to go back and to generate a clean used to go back and to generate a clean
    used to go back and to generate a clean

    image from noise. So see now here we are image from noise. So see now here we
    are image from noise. So see now here we are

    going in the reverse direction now right going in the reverse direction now right
    going in the reverse direction now right

    and the goal is to recover back the and the goal is to recover back the and the
    goal is to recover back the

    clean image. clean image.'
  concept_slugs:
  - diffusion-language-model
- idx: 10
  start_sec: 523.599
  end_sec: 590.56
  text: 'clean image.

    So now you''ll see that as we are going So now you''ll see that as we are going
    So now you''ll see that as we are going

    in the reverse direction slowly the dye in the reverse direction slowly the dye
    in the reverse direction slowly the dye

    or the color which we have added will or the color which we have added will or
    the color which we have added will

    come back to its original configuration. You''ll already see that it''s getting
    You''ll already see that it''s getting

    back. See here back. See here back. See here

    the D has kind of come back to its the D has kind of come back to its the D has
    kind of come back to its

    original configuration over here. original configuration over here. original configuration
    over here.

    See See

    this is beautiful right? We started from this is beautiful right? We started from
    this is beautiful right? We started from

    this similar configuration. this similar configuration. this similar configuration.

    Um like this Um like this Um like this

    we added small amount of noise and then we added small amount of noise and then
    we added small amount of noise and then

    we reversed the process and got back we reversed the process and got back we reversed
    the process and got back

    this exact same configuration. this exact same configuration. this exact same
    configuration.

    The reason this recovery was possible is The reason this recovery was possible
    is The reason this recovery was possible is

    because the noise was injected in a because the noise was injected in a because
    the noise was injected in a

    sequential manner. The noise was sequential manner. The noise was sequential manner.
    The noise was

    injected very slowly injected very slowly injected very slowly

    and that is the exact same process which and that is the exact same process which
    and that is the exact same process which

    is followed for images. is followed for images. is followed for images.

    So let''s now take a look at images and So let''s now take a look at images and
    So let''s now take a look at images and

    see how this analogy applies to images.'
  concept_slugs:
  - diffusion-language-model
---
# Lecture 2: How I began my Diffusion LLM Journey

See the structured chunks above.
